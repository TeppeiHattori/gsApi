# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class WebResponse(object):
    """Describes the response to an HTTP request."""

    body = attr.ib(default=None, metadata={"schema_property_name": "body"})
    headers = attr.ib(default=None, metadata={"schema_property_name": "headers"})
    index = attr.ib(default=-1, metadata={"schema_property_name": "index"})
    no_response_received = attr.ib(default=None, metadata={"schema_property_name": "noResponseReceived"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    protocol = attr.ib(default=None, metadata={"schema_property_name": "protocol"})
    reason_phrase = attr.ib(default=None, metadata={"schema_property_name": "reasonPhrase"})
    status_code = attr.ib(default=None, metadata={"schema_property_name": "statusCode"})
    version = attr.ib(default=None, metadata={"schema_property_name": "version"})
