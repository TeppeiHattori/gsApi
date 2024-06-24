import os
import logging
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage
from linebot.exceptions import InvalidSignatureError

import boto3

# 環境変数の取得
channel_secret = os.getenv('LINE_CHANNEL_SECRET')
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

client = boto3.client('rekognition')

# ロギング設定
logging.basicConfig(level=logging.INFO)

if channel_secret is None:
    logging.error('LINE_CHANNEL_SECRET is None')
if channel_access_token is None:
    logging.error('LINE_CHANNEL_ACCESS_TOKEN is None')

handler = WebhookHandler(channel_secret)
line_bot_api = LineBotApi(channel_access_token)

def lambda_handler(event, context):
    logging.info('Event: %s', event)
    headers = event["headers"]
    body = event["body"]

    # get X-Line-Signature header value
    signature = headers['x-line-signature']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        logging.error('Invalid signature. Check your channel access token/channel secret.')
        return {"statusCode": 400, "body": "Invalid signature. Please check your channel access token/channel secret."}

    return {"statusCode": 200, "body": "OK"}

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    """ TextMessage handler """
    input_text = event.message.text
    logging.info('Received message: %s', input_text)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=input_text))

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    # ユーザーから送られてきた画像を一時ファイルとして保存
    message_content = line_bot_api.get_message_content(event.message.id)
    file_path = "/tmp/sent-image.jpg"
    with open(file_path, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    
    logging.info('Image saved to %s', file_path)

    # Rekognitionで感情分析する
    with open(file_path, 'rb') as fd:
        sent_image_binary = fd.read()
        try:
            response = client.detect_faces(Image={"Bytes": sent_image_binary},
                                           Attributes=['ALL'])
            logging.info('Rekognition response: %s', response)
        except Exception as e:
            logging.error('Rekognition error: %s', str(e))
            response = None

    # 関数定義
    def all_happy(result):
        # 検出した顔が全てHAPPYならTRUEを返す
        for detail in result["FaceDetails"]:
            if most_confident_emotion(detail["Emotions"]) != "HAPPY":
                return False
        return True

    def most_confident_emotion(emotions):
        # もっと確信度が高い感情を返す
        max_conf = 0
        result = ""
        for e in emotions:
            if max_conf < e["Confidence"]:
                max_conf = e["Confidence"]
                result = e["Type"]
        return result

    # メッセージ生成
    if response:
        if all_happy(response):
            message = "みんな、いい笑顔ですね！！"
        else:
            message = "ぼちぼちですね。気分をアゲていきましょう！"
    else:
        message = "画像解析中にエラーが発生しました。"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message)
    )

    # file_pathの画像を削除
    os.remove(file_path)
