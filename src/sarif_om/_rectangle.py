# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class Rectangle(object):
    """An area within an image."""

    bottom = attr.ib(default=None, metadata={"schema_property_name": "bottom"})
    left = attr.ib(default=None, metadata={"schema_property_name": "left"})
    message = attr.ib(default=None, metadata={"schema_property_name": "message"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    right = attr.ib(default=None, metadata={"schema_property_name": "right"})
    top = attr.ib(default=None, metadata={"schema_property_name": "top"})