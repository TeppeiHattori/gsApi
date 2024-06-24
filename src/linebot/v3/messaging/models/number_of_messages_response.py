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
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, validator

class NumberOfMessagesResponse(BaseModel):
    """
    NumberOfMessagesResponse
    """
    status: StrictStr = Field(..., description="Aggregation process status. One of:  `ready`: The number of messages can be obtained. `unready`: We haven't finished calculating the number of sent messages for the specified in date. For example, this property is returned when the delivery date or a future date is specified. Calculation usually takes about a day. `unavailable_for_privacy`: The total number of messages on the specified day is less than 20. `out_of_service`: The specified date is earlier than the date on which we first started calculating sent messages (March 31, 2018). ")
    success: Optional[StrictInt] = Field(None, description="The number of messages delivered using the phone number on the date specified in `date`. The response has this property only when the value of `status` is `ready`.  ")

    __properties = ["status", "success"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ready', 'unready', 'unavailable_for_privacy', 'out_of_service'):
            raise ValueError("must be one of enum values ('ready', 'unready', 'unavailable_for_privacy', 'out_of_service')")
        return value

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
    def from_json(cls, json_str: str) -> NumberOfMessagesResponse:
        """Create an instance of NumberOfMessagesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberOfMessagesResponse:
        """Create an instance of NumberOfMessagesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NumberOfMessagesResponse.parse_obj(obj)

        _obj = NumberOfMessagesResponse.parse_obj({
            "status": obj.get("status"),
            "success": obj.get("success")
        })
        return _obj

