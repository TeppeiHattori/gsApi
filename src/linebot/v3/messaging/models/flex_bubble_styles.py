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


from typing import Optional
from pydantic.v1 import BaseModel
from linebot.v3.messaging.models.flex_block_style import FlexBlockStyle

class FlexBubbleStyles(BaseModel):
    """
    FlexBubbleStyles
    """
    header: Optional[FlexBlockStyle] = None
    hero: Optional[FlexBlockStyle] = None
    body: Optional[FlexBlockStyle] = None
    footer: Optional[FlexBlockStyle] = None

    __properties = ["header", "hero", "body", "footer"]

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
    def from_json(cls, json_str: str) -> FlexBubbleStyles:
        """Create an instance of FlexBubbleStyles from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of header
        if self.header:
            _dict['header'] = self.header.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of hero
        if self.hero:
            _dict['hero'] = self.hero.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of body
        if self.body:
            _dict['body'] = self.body.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of footer
        if self.footer:
            _dict['footer'] = self.footer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlexBubbleStyles:
        """Create an instance of FlexBubbleStyles from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlexBubbleStyles.parse_obj(obj)

        _obj = FlexBubbleStyles.parse_obj({
            "header": FlexBlockStyle.from_dict(obj.get("header")) if obj.get("header") is not None else None,
            "hero": FlexBlockStyle.from_dict(obj.get("hero")) if obj.get("hero") is not None else None,
            "body": FlexBlockStyle.from_dict(obj.get("body")) if obj.get("body") is not None else None,
            "footer": FlexBlockStyle.from_dict(obj.get("footer")) if obj.get("footer") is not None else None
        })
        return _obj

