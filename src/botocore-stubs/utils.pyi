import datetime
from logging import Logger
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Mapping,
    Optional,
    Pattern,
    Tuple,
    Type,
    TypeVar,
)

from botocore.client import BaseClient
from botocore.compat import HAS_CRT as HAS_CRT
from botocore.compat import MD5_AVAILABLE as MD5_AVAILABLE
from botocore.compat import OrderedDict as OrderedDict
from botocore.compat import get_md5 as get_md5
from botocore.compat import get_tzinfo_options as get_tzinfo_options
from botocore.compat import quote as quote
from botocore.compat import urlparse as urlparse
from botocore.compat import urlsplit as urlsplit
from botocore.compat import urlunsplit as urlunsplit
from botocore.compat import zip_longest as zip_longest
from botocore.credentials import Credentials
from botocore.exceptions import ClientError as ClientError
from botocore.exceptions import ConfigNotFound as ConfigNotFound
from botocore.exceptions import ConnectionClosedError as ConnectionClosedError
from botocore.exceptions import ConnectTimeoutError as ConnectTimeoutError
from botocore.exceptions import EndpointConnectionError as EndpointConnectionError
from botocore.exceptions import HTTPClientError as HTTPClientError
from botocore.exceptions import InvalidDNSNameError as InvalidDNSNameError
from botocore.exceptions import InvalidExpressionError as InvalidExpressionError
from botocore.exceptions import InvalidHostLabelError as InvalidHostLabelError
from botocore.exceptions import InvalidIMDSEndpointError as InvalidIMDSEndpointError
from botocore.exceptions import InvalidRegionError as InvalidRegionError
from botocore.exceptions import MetadataRetrievalError as MetadataRetrievalError
from botocore.exceptions import ReadTimeoutError as ReadTimeoutError
from botocore.exceptions import SSOTokenLoadError as SSOTokenLoadError
from botocore.exceptions import UnsupportedOutpostResourceError as UnsupportedOutpostResourceError
from botocore.exceptions import (
    UnsupportedS3AccesspointConfigurationError as UnsupportedS3AccesspointConfigurationError,
)
from botocore.exceptions import UnsupportedS3ArnError as UnsupportedS3ArnError
from botocore.exceptions import UnsupportedS3ControlArnError as UnsupportedS3ControlArnError
from botocore.exceptions import (
    UnsupportedS3ControlConfigurationError as UnsupportedS3ControlConfigurationError,
)
from botocore.hooks import BaseEventHooks
from botocore.model import OperationModel, ServiceModel, Shape
from botocore.regions import BaseEndpointResolver
from botocore.session import Session
from requests.models import Response

logger: Logger = ...

_V = TypeVar("_V")

DEFAULT_METADATA_SERVICE_TIMEOUT: int
METADATA_BASE_URL: str
METADATA_BASE_URL_IPv6: str
METADATA_ENDPOINT_MODES: Tuple[str, ...]
SAFE_CHARS: str
LABEL_RE: Pattern[str]
RETRYABLE_HTTP_ERRORS: Tuple[Any, ...]
S3_ACCELERATE_WHITELIST: List[str]
EVENT_ALIASES: Dict[str, str]
CHECKSUM_HEADER_PATTERN: Pattern[str]
IPV4_PAT: str
HEX_PAT: str
LS32_PAT: str
UNRESERVED_PAT: str
IPV6_PAT: str
ZONE_ID_PAT: str
IPV6_ADDRZ_PAT: str
IPV6_ADDRZ_RE: Pattern[str]
UNSAFE_URL_CHARS: frozenset[Any]

def ensure_boolean(val: Any) -> bool: ...
def resolve_imds_endpoint_mode(session: Session) -> str: ...
def is_json_value_header(shape: Shape) -> bool: ...
def has_header(header_name: Optional[str], headers: Mapping[str, Any]) -> bool: ...
def get_service_module_name(service_model: ServiceModel) -> str: ...
def normalize_url_path(path: str) -> str: ...
def normalize_boolean(val: Any) -> Optional[bool]: ...
def remove_dot_segments(url: str) -> str: ...
def validate_jmespath_for_set(expression: Optional[str]) -> None: ...
def set_value_from_jmespath(
    source: Dict[str, Any], expression: str, value: Any, is_first: bool = ...
) -> None: ...
def is_global_accesspoint(context: Any) -> bool: ...

class _RetriesExceededError(Exception): ...

class BadIMDSRequestError(Exception):
    def __init__(self, request: Any) -> None:
        self.request: Any

class IMDSFetcher:
    def __init__(
        self,
        timeout: int = ...,
        num_attempts: int = ...,
        base_url: str = ...,
        env: Optional[Any] = ...,
        user_agent: Optional[Any] = ...,
        config: Optional[Any] = ...,
    ) -> None: ...
    def get_base_url(self) -> str: ...

class InstanceMetadataFetcher(IMDSFetcher):
    def retrieve_iam_role_credentials(self) -> Any: ...

class IMDSRegionProvider:
    def __init__(
        self,
        session: Session,
        environ: Any = ...,
        fetcher: Optional[IMDSFetcher] = ...,
    ) -> None: ...
    def provide(self) -> Any: ...

class InstanceMetadataRegionFetcher(IMDSFetcher):
    def retrieve_region(self) -> Optional[str]: ...

def merge_dicts(
    dict1: Mapping[str, Any], dict2: Mapping[str, Any], append_lists: bool = ...
) -> None: ...
def lowercase_dict(original: Mapping[str, Any]) -> Dict[str, Any]: ...
def parse_key_val_file(filename: str, _open: Callable[..., Any] = ...) -> Dict[str, str]: ...
def parse_key_val_file_contents(contents: str) -> Dict[str, str]: ...
def percent_encode_sequence(mapping: Mapping[str, Any], safe: Iterable[str] = ...) -> Any: ...
def percent_encode(input_str: str, safe: Iterable[str] = ...) -> Any: ...
def parse_timestamp(value: str) -> datetime.datetime: ...
def parse_to_aware_datetime(value: str) -> datetime.datetime: ...
def datetime2timestamp(dt: datetime.datetime, default_timezone: Optional[Any] = ...) -> int: ...
def calculate_sha256(body: str, as_hex: bool = ...) -> str: ...
def calculate_tree_hash(body: str) -> str: ...

class CachedProperty(Generic[_V]):
    def __init__(self, fget: Callable[..., _V]) -> None: ...
    def __get__(self, obj: Any, cls: Any) -> _V: ...

class ArgumentGenerator:
    def __init__(self, use_member_names: bool = ...) -> None: ...
    def generate_skeleton(self, shape: Shape) -> Any: ...

def is_valid_ipv6_endpoint_url(endpoint_url: str) -> bool: ...
def is_valid_ipv4_endpoint_url(endpoint_url: str) -> bool: ...
def is_valid_endpoint_url(endpoint_url: str) -> bool: ...
def is_valid_uri(endpoint_url: str) -> bool: ...
def validate_region_name(region_name: str) -> None: ...
def check_dns_name(bucket_name: str) -> bool: ...
def fix_s3_host(
    request: Any,
    signature_version: Any,
    region_name: Any,
    default_endpoint_url: Optional[str] = ...,
    **kwargs: Any,
) -> None: ...
def switch_to_virtual_host_style(
    request: Any, signature_version: Any, default_endpoint_url: Optional[str] = ..., **kwargs: Any
) -> None: ...
def instance_cache(func: Any) -> Any: ...
def lru_cache_weakref(*cache_args: Any, **cache_kwargs: Any) -> Any: ...
def switch_host_s3_accelerate(request: Any, operation_name: Any, **kwargs: Any) -> None: ...
def switch_host_with_param(request: Any, param_name: Any) -> None: ...
def deep_merge(base: Any, extra: Any) -> None: ...
def hyphenize_service_id(service_id: Any) -> Any: ...

class IdentityCache:
    METHOD: str = ...
    def __init__(self, client: BaseClient, credential_cls: Type[Credentials]) -> None: ...
    def get_credentials(self, **kwargs: Any) -> Credentials: ...
    def build_refresh_callback(**kwargs: Any) -> Callable[..., Any]: ...

class S3ExpressIdentityCache(IdentityCache):
    def get_credentials(self, bucket: str) -> Credentials: ...  # type: ignore [override]
    def build_refresh_callback(self, bucket: str) -> Callable[..., Any]: ...  # type: ignore [override]

class S3ExpressIdentityResolver:
    def __init__(
        self,
        client: BaseClient,
        credential_cls: Type[Credentials],
        cache: Optional[S3ExpressIdentityCache] = ...,
    ) -> None: ...
    def register(self, event_emitter: Optional[BaseEventHooks] = ...) -> None: ...
    def apply_signing_cache_key(
        self, params: Mapping[str, Any], context: Mapping[str, Any], **kwargs: Any
    ) -> None: ...
    def resolve_s3express_identity(
        self,
        request: Any,
        signing_name: str,
        region_name: str,
        signature_version: str,
        request_signer: Any,
        operation_name: str,
        **kwargs: Any,
    ) -> None: ...

class S3RegionRedirectorv2:
    def __init__(
        self, endpoint_bridge: Any, client: BaseClient, cache: Optional[Any] = ...
    ) -> None: ...
    def register(self, event_emitter: Optional[BaseEventHooks] = ...) -> None: ...
    def redirect_from_error(
        self,
        request_dict: Mapping[str, Any],
        response: Response,
        operation: OperationModel,
        **kwargs: Any,
    ) -> Any: ...
    def get_bucket_region(self, bucket: Any, response: Response) -> Any: ...
    def set_request_url(self, old_url: str, new_endpoint: str, **kwargs: Any) -> None: ...
    def redirect_from_cache(self, builtins: Any, params: Any, **kwargs: Any) -> None: ...
    def annotate_request_context(self, params: Any, context: Any, **kwargs: Any) -> None: ...

class S3RegionRedirector:
    def __init__(
        self, endpoint_bridge: Any, client: BaseClient, cache: Optional[Any] = ...
    ) -> None: ...
    def register(self, event_emitter: Optional[BaseEventHooks] = ...) -> None: ...
    def redirect_from_error(
        self,
        request_dict: Mapping[str, Any],
        response: Response,
        operation: OperationModel,
        **kwargs: Any,
    ) -> Any: ...
    def get_bucket_region(self, bucket: Any, response: Response) -> Any: ...
    def set_request_url(self, params: Any, context: Any, **kwargs: Any) -> None: ...
    def redirect_from_cache(self, params: Any, context: Any, **kwargs: Any) -> None: ...

class InvalidArnException(ValueError): ...

class ArnParser:
    def parse_arn(self, arn: str) -> Dict[str, Any]: ...
    @staticmethod
    def is_arn(value: str) -> bool: ...

class S3ArnParamHandler:
    def __init__(self, arn_parser: Optional[Any] = ...) -> None: ...
    def register(self, event_emitter: BaseEventHooks) -> None: ...
    def handle_arn(self, params: Any, model: Any, context: Any, **kwargs: Any) -> None: ...

class S3EndpointSetter:
    def __init__(
        self,
        endpoint_resolver: BaseEndpointResolver,
        region: Optional[str] = ...,
        s3_config: Optional[Any] = ...,
        endpoint_url: Optional[str] = ...,
        partition: Optional[Any] = ...,
        use_fips_endpoint: Optional[bool] = ...,
    ) -> None: ...
    def register(self, event_emitter: BaseEventHooks) -> None: ...
    def set_endpoint(self, request: Any, **kwargs: Any) -> None: ...
    def update_endpoint_to_s3_object_lambda(
        self, params: Mapping[str, Any], context: Any, **kwargs: Any
    ) -> None: ...
    def set_signer(self, context: Any, **kwargs: Any) -> str: ...

class S3ControlEndpointSetter:
    def __init__(
        self,
        endpoint_resolver: BaseEndpointResolver,
        region: Optional[str] = ...,
        s3_config: Optional[Any] = ...,
        endpoint_url: Optional[str] = ...,
        partition: Optional[Any] = ...,
        use_fips_endpoint: Optional[bool] = ...,
    ) -> None: ...
    def register(self, event_emitter: BaseEventHooks) -> None: ...
    def set_endpoint(self, request: Any, **kwargs: Any) -> None: ...

class S3ControlArnParamHandler:
    def __init__(self, arn_parser: Optional[Any] = ...) -> None: ...
    def register(self, event_emitter: BaseEventHooks) -> None: ...
    def handle_arn(self, params: Any, model: Any, context: Any, **kwargs: Any) -> None: ...

class S3ControlArnParamHandlerv2(S3ControlArnParamHandler): ...

class ContainerMetadataFetcher:
    TIMEOUT_SECONDS: int
    RETRY_ATTEMPTS: int
    SLEEP_TIME: int
    IP_ADDRESS: str
    def __init__(self, session: Optional[Any] = ..., sleep: Any = ...) -> None: ...
    def retrieve_full_uri(self, full_url: str, headers: Optional[Any] = ...) -> Any: ...
    def retrieve_uri(self, relative_uri: str) -> Any: ...
    def full_url(self, relative_uri: str) -> Any: ...

def get_environ_proxies(url: str) -> Dict[str, Any]: ...
def should_bypass_proxies(url: str) -> bool: ...
def determine_content_length(body: Any) -> Optional[int]: ...
def get_encoding_from_headers(headers: Mapping[str, Any], default: str = ...) -> str: ...
def calculate_md5(body: Any, **kwargs: Any) -> str: ...
def conditionally_calculate_checksum(params: Mapping[str, Any], **kwargs: Any) -> str: ...
def conditionally_enable_crc32(params: Mapping[str, Any], **kwargs: Any) -> None: ...
def conditionally_calculate_md5(params: Mapping[str, Any], **kwargs: Any) -> str: ...

class FileWebIdentityTokenLoader:
    def __init__(self, web_identity_token_path: Any, _open: Any = ...) -> None: ...
    def __call__(self) -> Any: ...

class SSOTokenLoader:
    def __init__(self, cache: Optional[Any] = ...) -> None: ...
    def save_token(self, start_url: str, token: str, session_name: Optional[str] = ...) -> None: ...
    def __call__(self, start_url: str, session_name: Optional[str] = ...) -> Any: ...

class EventbridgeSignerSetter:
    def __init__(
        self,
        endpoint_resolver: BaseEndpointResolver,
        region: Optional[str] = None,
        endpoint_url: Optional[str] = None,
    ) -> None: ...
    def register(self, event_emitter: BaseEventHooks) -> None: ...
    def set_endpoint_url(
        self, params: Mapping[str, Any], context: Mapping[str, Any], **kwargs: Any
    ) -> None: ...
    def check_for_global_endpoint(
        self, params: Mapping[str, Any], context: Mapping[str, Any], **kwargs: Any
    ) -> None: ...

def is_s3_accelerate_url(url: Optional[str]) -> bool: ...

class JSONFileCache:
    CACHE_DIR: Any = ...
    def __init__(self, working_dir: Any = ..., dumps_func: Optional[Any] = ...) -> None: ...
    def __contains__(self, cache_key: str) -> bool: ...
    def __getitem__(self, cache_key: str) -> Any: ...
    def __delitem__(self, cache_key: str) -> None: ...
    def __setitem__(self, cache_key: str, value: Any) -> None: ...

def is_s3express_bucket(bucket: str) -> bool: ...

SERVICE_NAME_ALIASES: Dict[str, str] = ...
CLIENT_NAME_TO_HYPHENIZED_SERVICE_ID_OVERRIDES: Dict[str, str] = ...