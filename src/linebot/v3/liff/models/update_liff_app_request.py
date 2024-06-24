# coding: utf-8

"""
    LIFF server API

    LIFF Server API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from linebot.v3.liff.models.liff_bot_prompt import LiffBotPrompt
from linebot.v3.liff.models.liff_features import LiffFeatures
from linebot.v3.liff.models.liff_scope import LiffScope
from linebot.v3.liff.models.liff_view import LiffView

class UpdateLiffAppRequest(BaseModel):
    """
    UpdateLiffAppRequest
    https://developers.line.biz/en/reference/liff-server/#add-liff-app
    """
    view: Optional[LiffView] = None
    description: Optional[StrictStr] = Field(None, description="Name of the LIFF app.  The LIFF app name can't include \"LINE\" or similar strings, or inappropriate strings. ")
    features: Optional[LiffFeatures] = None
    permanent_link_pattern: Optional[StrictStr] = Field(None, alias="permanentLinkPattern", description="How additional information in LIFF URLs is handled. Specify `concat`. ")
    scope: Optional[conlist(LiffScope)] = None
    bot_prompt: Optional[LiffBotPrompt] = Field(None, alias="botPrompt")

    __properties = ["view", "description", "features", "permanentLinkPattern", "scope", "botPrompt"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateLiffAppRequest:
        """Create an instance of UpdateLiffAppRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of view
        if self.view:
            _dict['view'] = self.view.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateLiffAppRequest:
        """Create an instance of UpdateLiffAppRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateLiffAppRequest.parse_obj(obj)

        _obj = UpdateLiffAppRequest.parse_obj({
            "view": LiffView.from_dict(obj.get("view")) if obj.get("view") is not None else None,
            "description": obj.get("description"),
            "features": LiffFeatures.from_dict(obj.get("features")) if obj.get("features") is not None else None,
            "permanent_link_pattern": obj.get("permanentLinkPattern"),
            "scope": obj.get("scope"),
            "bot_prompt": obj.get("botPrompt")
        })
        return _obj

