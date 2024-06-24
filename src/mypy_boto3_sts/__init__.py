"""
Main interface for sts service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sts import (
        Client,
        STSClient,
    )

    session = Session()
    client: STSClient = session.client("sts")
    ```
"""

from .client import STSClient

Client = STSClient


__all__ = ("Client", "STSClient")
