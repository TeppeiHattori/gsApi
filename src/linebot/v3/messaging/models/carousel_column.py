# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from linebot.v3.messaging.models.action import Action

class CarouselColumn(BaseModel):
    """
    Column object for carousel template.
    """
    thumbnail_image_url: Optional[StrictStr] = Field(None, alias="thumbnailImageUrl")
    image_background_color: Optional[StrictStr] = Field(None, alias="imageBackgroundColor")
    title: Optional[StrictStr] = None
    text: Optional[StrictStr] = None
    default_action: Optional[Action] = Field(None, alias="defaultAction")
    actions: Optional[conlist(Action)] = None

    __properties = ["thumbnailImageUrl", "imageBackgroundColor", "title", "text", "defaultAction", "actions"]

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
    def from_json(cls, json_str: str) -> CarouselColumn:
        """Create an instance of CarouselColumn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of default_action
        if self.default_action:
            _dict['defaultAction'] = self.default_action.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CarouselColumn:
        """Create an instance of CarouselColumn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CarouselColumn.parse_obj(obj)

        _obj = CarouselColumn.parse_obj({
            "thumbnail_image_url": obj.get("thumbnailImageUrl"),
            "image_background_color": obj.get("imageBackgroundColor"),
            "title": obj.get("title"),
            "text": obj.get("text"),
            "default_action": Action.from_dict(obj.get("defaultAction")) if obj.get("defaultAction") is not None else None,
            "actions": [Action.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None
        })
        return _obj

