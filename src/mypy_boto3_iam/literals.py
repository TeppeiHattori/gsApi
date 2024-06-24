"""
Type annotations for iam service literal definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/literals/)

Usage::

    ```python
    from mypy_boto3_iam.literals import AccessAdvisorUsageGranularityTypeType

    data: AccessAdvisorUsageGranularityTypeType = "ACTION_LEVEL"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessAdvisorUsageGranularityTypeType",
    "ContextKeyTypeEnumType",
    "DeletionTaskStatusTypeType",
    "EntityTypeType",
    "GetAccountAuthorizationDetailsPaginatorName",
    "GetGroupPaginatorName",
    "InstanceProfileExistsWaiterName",
    "ListAccessKeysPaginatorName",
    "ListAccountAliasesPaginatorName",
    "ListAttachedGroupPoliciesPaginatorName",
    "ListAttachedRolePoliciesPaginatorName",
    "ListAttachedUserPoliciesPaginatorName",
    "ListEntitiesForPolicyPaginatorName",
    "ListGroupPoliciesPaginatorName",
    "ListGroupsForUserPaginatorName",
    "ListGroupsPaginatorName",
    "ListInstanceProfileTagsPaginatorName",
    "ListInstanceProfilesForRolePaginatorName",
    "ListInstanceProfilesPaginatorName",
    "ListMFADeviceTagsPaginatorName",
    "ListMFADevicesPaginatorName",
    "ListOpenIDConnectProviderTagsPaginatorName",
    "ListPoliciesPaginatorName",
    "ListPolicyTagsPaginatorName",
    "ListPolicyVersionsPaginatorName",
    "ListRolePoliciesPaginatorName",
    "ListRoleTagsPaginatorName",
    "ListRolesPaginatorName",
    "ListSAMLProviderTagsPaginatorName",
    "ListSSHPublicKeysPaginatorName",
    "ListServerCertificateTagsPaginatorName",
    "ListServerCertificatesPaginatorName",
    "ListSigningCertificatesPaginatorName",
    "ListUserPoliciesPaginatorName",
    "ListUserTagsPaginatorName",
    "ListUsersPaginatorName",
    "ListVirtualMFADevicesPaginatorName",
    "PermissionsBoundaryAttachmentTypeType",
    "PolicyEvaluationDecisionTypeType",
    "PolicyExistsWaiterName",
    "PolicySourceTypeType",
    "PolicyUsageTypeType",
    "ReportFormatTypeType",
    "ReportStateTypeType",
    "RoleExistsWaiterName",
    "SimulateCustomPolicyPaginatorName",
    "SimulatePrincipalPolicyPaginatorName",
    "UserExistsWaiterName",
    "assignmentStatusTypeType",
    "encodingTypeType",
    "globalEndpointTokenVersionType",
    "jobStatusTypeType",
    "policyOwnerEntityTypeType",
    "policyScopeTypeType",
    "policyTypeType",
    "sortKeyTypeType",
    "statusTypeType",
    "summaryKeyTypeType",
    "IAMServiceName",
    "ServiceName",
    "ResourceServiceName",
    "PaginatorName",
    "WaiterName",
)

AccessAdvisorUsageGranularityTypeType = Literal["ACTION_LEVEL", "SERVICE_LEVEL"]
ContextKeyTypeEnumType = Literal[
    "binary",
    "binaryList",
    "boolean",
    "booleanList",
    "date",
    "dateList",
    "ip",
    "ipList",
    "numeric",
    "numericList",
    "string",
    "stringList",
]
DeletionTaskStatusTypeType = Literal["FAILED", "IN_PROGRESS", "NOT_STARTED", "SUCCEEDED"]
EntityTypeType = Literal["AWSManagedPolicy", "Group", "LocalManagedPolicy", "Role", "User"]
GetAccountAuthorizationDetailsPaginatorName = Literal["get_account_authorization_details"]
GetGroupPaginatorName = Literal["get_group"]
InstanceProfileExistsWaiterName = Literal["instance_profile_exists"]
ListAccessKeysPaginatorName = Literal["list_access_keys"]
ListAccountAliasesPaginatorName = Literal["list_account_aliases"]
ListAttachedGroupPoliciesPaginatorName = Literal["list_attached_group_policies"]
ListAttachedRolePoliciesPaginatorName = Literal["list_attached_role_policies"]
ListAttachedUserPoliciesPaginatorName = Literal["list_attached_user_policies"]
ListEntitiesForPolicyPaginatorName = Literal["list_entities_for_policy"]
ListGroupPoliciesPaginatorName = Literal["list_group_policies"]
ListGroupsForUserPaginatorName = Literal["list_groups_for_user"]
ListGroupsPaginatorName = Literal["list_groups"]
ListInstanceProfileTagsPaginatorName = Literal["list_instance_profile_tags"]
ListInstanceProfilesForRolePaginatorName = Literal["list_instance_profiles_for_role"]
ListInstanceProfilesPaginatorName = Literal["list_instance_profiles"]
ListMFADeviceTagsPaginatorName = Literal["list_mfa_device_tags"]
ListMFADevicesPaginatorName = Literal["list_mfa_devices"]
ListOpenIDConnectProviderTagsPaginatorName = Literal["list_open_id_connect_provider_tags"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListPolicyTagsPaginatorName = Literal["list_policy_tags"]
ListPolicyVersionsPaginatorName = Literal["list_policy_versions"]
ListRolePoliciesPaginatorName = Literal["list_role_policies"]
ListRoleTagsPaginatorName = Literal["list_role_tags"]
ListRolesPaginatorName = Literal["list_roles"]
ListSAMLProviderTagsPaginatorName = Literal["list_saml_provider_tags"]
ListSSHPublicKeysPaginatorName = Literal["list_ssh_public_keys"]
ListServerCertificateTagsPaginatorName = Literal["list_server_certificate_tags"]
ListServerCertificatesPaginatorName = Literal["list_server_certificates"]
ListSigningCertificatesPaginatorName = Literal["list_signing_certificates"]
ListUserPoliciesPaginatorName = Literal["list_user_policies"]
ListUserTagsPaginatorName = Literal["list_user_tags"]
ListUsersPaginatorName = Literal["list_users"]
ListVirtualMFADevicesPaginatorName = Literal["list_virtual_mfa_devices"]
PermissionsBoundaryAttachmentTypeType = Literal["PermissionsBoundaryPolicy"]
PolicyEvaluationDecisionTypeType = Literal["allowed", "explicitDeny", "implicitDeny"]
PolicyExistsWaiterName = Literal["policy_exists"]
PolicySourceTypeType = Literal[
    "aws-managed", "group", "none", "resource", "role", "user", "user-managed"
]
PolicyUsageTypeType = Literal["PermissionsBoundary", "PermissionsPolicy"]
ReportFormatTypeType = Literal["text/csv"]
ReportStateTypeType = Literal["COMPLETE", "INPROGRESS", "STARTED"]
RoleExistsWaiterName = Literal["role_exists"]
SimulateCustomPolicyPaginatorName = Literal["simulate_custom_policy"]
SimulatePrincipalPolicyPaginatorName = Literal["simulate_principal_policy"]
UserExistsWaiterName = Literal["user_exists"]
assignmentStatusTypeType = Literal["Any", "Assigned", "Unassigned"]
encodingTypeType = Literal["PEM", "SSH"]
globalEndpointTokenVersionType = Literal["v1Token", "v2Token"]
jobStatusTypeType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
policyOwnerEntityTypeType = Literal["GROUP", "ROLE", "USER"]
policyScopeTypeType = Literal["AWS", "All", "Local"]
policyTypeType = Literal["INLINE", "MANAGED"]
sortKeyTypeType = Literal[
    "LAST_AUTHENTICATED_TIME_ASCENDING",
    "LAST_AUTHENTICATED_TIME_DESCENDING",
    "SERVICE_NAMESPACE_ASCENDING",
    "SERVICE_NAMESPACE_DESCENDING",
]
statusTypeType = Literal["Active", "Inactive"]
summaryKeyTypeType = Literal[
    "AccessKeysPerUserQuota",
    "AccountAccessKeysPresent",
    "AccountMFAEnabled",
    "AccountSigningCertificatesPresent",
    "AttachedPoliciesPerGroupQuota",
    "AttachedPoliciesPerRoleQuota",
    "AttachedPoliciesPerUserQuota",
    "GlobalEndpointTokenVersion",
    "GroupPolicySizeQuota",
    "Groups",
    "GroupsPerUserQuota",
    "GroupsQuota",
    "MFADevices",
    "MFADevicesInUse",
    "Policies",
    "PoliciesQuota",
    "PolicySizeQuota",
    "PolicyVersionsInUse",
    "PolicyVersionsInUseQuota",
    "ServerCertificates",
    "ServerCertificatesQuota",
    "SigningCertificatesPerUserQuota",
    "UserPolicySizeQuota",
    "Users",
    "UsersQuota",
    "VersionsPerPolicyQuota",
]
IAMServiceName = Literal["iam"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "alexaforbusiness",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "backupstorage",
    "batch",
    "bcm-data-exports",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-runtime",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "honeycode",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkmanager",
    "networkmonitor",
    "nimble",
    "oam",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "privatenetworks",
    "proton",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "get_account_authorization_details",
    "get_group",
    "list_access_keys",
    "list_account_aliases",
    "list_attached_group_policies",
    "list_attached_role_policies",
    "list_attached_user_policies",
    "list_entities_for_policy",
    "list_group_policies",
    "list_groups",
    "list_groups_for_user",
    "list_instance_profile_tags",
    "list_instance_profiles",
    "list_instance_profiles_for_role",
    "list_mfa_device_tags",
    "list_mfa_devices",
    "list_open_id_connect_provider_tags",
    "list_policies",
    "list_policy_tags",
    "list_policy_versions",
    "list_role_policies",
    "list_role_tags",
    "list_roles",
    "list_saml_provider_tags",
    "list_server_certificate_tags",
    "list_server_certificates",
    "list_signing_certificates",
    "list_ssh_public_keys",
    "list_user_policies",
    "list_user_tags",
    "list_users",
    "list_virtual_mfa_devices",
    "simulate_custom_policy",
    "simulate_principal_policy",
]
WaiterName = Literal["instance_profile_exists", "policy_exists", "role_exists", "user_exists"]
