---
url: 'https://docs.workato.com/en/oem/oem-api/connections-parameters.md'
description: >-
  Reference for the connection parameters and provider values used to configure
  Workato connectors through the Embedded Platform APIs.
---

# Embedded API - Connection parameters reference

This reference contains the connection parameters required to configure connectors using Workato's APIs.

## Provider values

Every connector has a `provider` value which uniquely identifies the type of connector. For example, the Salesforce connector has a `provider: salesforce` value.

Provider values should be supplied when:

- [**Creating a connection**](/en/oem/oem-api/connections#create-a-connection) using the Platform API:

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
             "name": ":name",
             "provider": "salesforce"
           }'
```

</api-code>

- **Defining [App Access](/en/oem/oem-api/managed-users) for customers**. A connector's `provider` value can be included in the `whitelisted_apps` parameter to define the list of connectors the customer can access.
  
  For example, the following request creates an account that only has access to Salesforce and NetSuite:
  

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "notification_email": ":notification_email",
            "external_id": ":external_id",
            "whitelisted_apps": ["salesforce", "netsuite"],
            "time_zone": ":time_zone"
          }'
```

</api-code>

## Connection parameters

The following parameters describe the configuration for a given connector:

| Field | Type | Description |
| --- | --- | --- |
| **oauth** | boolean | If `true`, the connector requires OAuth. |
| **personalization** | boolean | If `true`, the connection can be used as a personalized connection in Workbot use cases. |
| **secure\_tunnel** | boolean | If `true`, the connection can be used to connect to on-premise systems. |
| **input** | array | An array of objects describing the connection parameters for the connector. When empty, no configuration is required. |

* * *

### Example: No configuration required

The following is an example of a connector that doesn't require any configuration:

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          []
      }
```

* * *

### Example: Configuration required

The following is an example of the configuration for the Airtable connector, which requires connection parameter configuration:

```json
{
    "oauth": true,
    "personalization": false,
    "input": [
        {
            "name": "authentication_type",
            "type": "select",
            "options": [
                "OAuth 2.0",
                "Personal access token",
                "API key (Deprecated)"
            ],
            "optional": false,
            "label": "Authentication type",
            "hint": "Select 'OAuth 2.0' or 'Personal access token' for current methods, 'API key' is unsupported."
        },
        {
            "name": "personal_access_token",
            "type": "string",
            "optional": true,
            "label": "Personal access token",
            "hint": "Enter your personal access token here if 'Personal access token' is the selected authentication type.",
            "conditional": {
                "field": "authentication_type",
                "value": "Personal access token"
            }
        }
    ]
}
```

* * *

## OAuth authentication

The Workato API allows you to create OAuth 2.0 connections. However, connections types that would normally redirect you to a sign-in screen, such as `oauth` or `oauth2_auth_code_grant`, require an `oauth_token_pair` object containing an access token and a refresh token. Client credentials grant connections don't require an `oauth_token_pair` object.

The following is the structure of an `oauth_token_pair` object:

```json
"oauth_token_pair": {
    "label": "OAuth Token Pair",
    "optional": true,
    "type": "object",
    "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
    "properties": [
      {
        "label": "Access Token",
        "name": "access_token",
        "type": "string",
        "optional": false
      },
      {
        "label": "Refresh Token",
        "name": "refresh_token",
        "type": "string",
        "optional": false
      }
    ]
  }
```

You can create a shell connection in cases where you don't have an access token and refresh token, such as when you create a connection for a managed user. This allows you to initialize the connection in a `Disconnected` state, and then complete authentication later in the Workato UI. Include `"shell_connection": true` in the request body or omit authorization fields to create a shell connection.

Create and authenticate a shell connection

Complete the following steps to create and authenticate a shell connection:

1. Create a shell connection using the [Create a connection](/en/oem/oem-api/connections#create-a-connection) endpoint. For example:
   
   <api-code>

   ```shell
   curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections \
         -H 'Authorization: Bearer <api_token>' \
         -H 'Content-Type: application/json' \
         -d  '{
               "name": ":name",
               "provider": "snowflake",
               "folder_id": :folder_id,
               "shell_connection": :true_or_false,
               "input": {
                   "authentication_type": ["OAuth 2.0", "oauth"],
                   "warehouse": ":warehouse",
                   "host": ":host",
                   "database": ":database",
                   "role": ":role",
                   "user": ":user",
                   "schema_name": ":schema_name",
                   "db_timezone": ["American Samoa", "American Samoa"]
                   }
               }'
   ```

   </api-code>
   
2. Sign in to Workato.
   
3. Open the project where you stored the shell connection.
   
4. Select the shell connection. ![Select the shell connection](/assets/select-shell.DgnIqCbo.png)_Select the shell connection._
   
5. Complete the remaining fields. Refer to the [Connectors](/en/connectors) section of Workato's documentation for connector-specific authentication steps. ![Complete the remaining fields](/assets/complete-remaining-fields.Dn4uSc38.png)_Complete the remaining fields._
   

* * *

## Configuration parameters and provider values by connector

The following list contains the configuration parameters and provider values for each connector.

**Note**: Only connectors that require connections are listed.

### 2Checkout

**Provider value:**

```json
"provider": "two_checkout"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Vendor code",
            "name": "vendor_code",
            "optional": false,
            "hint": "Go to 2Checkout cpanel > Integrations > Webhooks & API. Get your vendor/merchant code under the 'API' section.",
            "type": "string"
        },
        {
            "label": "Secret key",
            "name": "secret_key",
            "optional": false,
            "hint": "Go to 2Checkout cpanel > Integrations > Webhooks & API. You can find your secret key under the 'API' section.",
            "type": "string"
        }
    ]
}
```

* * *

### Active Directory

**Provider value:**

```json
"provider": "active_directory"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "On-prem connection profile",
            "name": "profile",
            "hint": "Enter the profile name from the LDAP section of your on-prem group's config.yml file to use a connection profile. Refer to the following documentation for more information: https://docs.workato.com/on-prem/agents/connection/profile.html#active-directory-profile",
            "type": "string"
        },
        {
            "label": "URL",
            "name": "url",
            "hint": "The URL should be in the format ldap://myserver.example.com:389 or ldaps://myserver.example.com:636 for SSL. You can find more information about LDAP connection here. This only applies when using a cloud profile. For example: 'ldap://acme1.ldap.com:389'. Refer to the following documentation for more information: https://docs.workato.com/on-prem/agents/connection/cloud.html#active-directory-profile",
            "type": "string"
        },
        {
            "label": "Username",
            "name": "username",
            "hint": "The username (principal) to use when authenticating with the LDAP server. This will usually be the distinguished name of an admin user. This only applies when using a cloud profile. For example: cn=Administrator",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "hint": "The password (credentials) to use when authenticating with the LDAP server. This only applies when using a cloud profile.",
            "type": "string"
        },
        {
            "label": "Base",
            "name": "base",
            "optional": true,
            "hint": "The base DN for all requests. When this attribute has been configured, all Distinguished names supplied to and received from LDAP operations will be relative to this LDAP path. This only applies when using a cloud profile. For example: dc=acme,dc=com",
            "type": "string"
        },
        {
            "label": "SSL settings",
            "name": "ssl",
            "optional": true,
            "hint": "This only applies when using a cloud profile.",
            "type": "object",
            "properties": [
                {
                    "label": "Certificate",
                    "name": "cert",
                    "optional": true,
                    "hint": "Path to the PEM encoded certificate or a trusted CA.",
                    "type": "string"
                },
                {
                    "label": "SSL certificate",
                    "name": "pem",
                    "optional": true,
                    "hint": "Full content of a PEM encoded client certificate.",
                    "type": "string"
                },
                {
                    "label": "SSL certificate key",
                    "name": "key",
                    "optional": true,
                    "hint": "Private key for mutual SSL setup. Required if SSL certificate is provided.",
                    "type": "string"
                },
                {
                    "label": "Trust all",
                    "name": "trustAll",
                    "optional": true,
                    "hint": "Set to true to enable self-signed certificates.",
                    "type": "boolean"
                }
            ]
        }
    ]
}
```

* * *

### Adobe Experience Manager

**Provider value:**

```json
"provider": "adobe_experience_manager"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select the authentication type to use for the connection. Defaults to `service_credentials`.",
            "type": "string",
            "pick_list": [
                [
                    "Basic",
                    "basic"
                ],
                [
                    "Service Credentials",
                    "service_credentials"
                ]
            ]
        },
        {
            "label": "AEM instance address",
            "name": "host_name",
            "optional": false,
            "hint": "The address of your AEM instance. If hosted locally in a private network, you will need to deploy an OPA and select the agent in a later step. If your AEM instance address is https://wkto.aem.com:8080 then your address is https://wkto.aem.com.",
            "type": "string"
        },
        {
            "label": "Port",
            "name": "port",
            "optional": true,
            "hint": "The port associated with your AEM instance. Depending on your setup, this might not be necessary. If your AEM instance address is https://wkto.aem.com:8080 then your port number is 8080.",
            "type": "integer"
        },
        {
            "label": "Service Credentials JSON",
            "name": "service_auth_json",
            "optional": false,
            "hint": "Paste the contents of the service credentials JSON obtained from the AEM developer console. Refer to the following documentation for instructions to generate the service credentials: https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html?lang=en. The service credentials' certificates expire every 365 days. Regenerate these certificates as necessary. This only applies when `Authentication type` is 'Service Credentials'.",
            "type": "string"
        },
        {
            "label": "Username",
            "name": "username",
            "optional": false,
            "hint": "The username of the user provisioned for Workato. This only applies when `Authentication type` is 'Basic'.",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "optional": false,
            "hint": "The password of the user provisioned for Workato. This only applies when `Authentication type` is 'Basic'.",
            "type": "string"
        }
    ]
}
```

* * *

### ADP Workforce Now

**Provider value:**

```json
"provider": "adp7"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Sandbox",
            "name": "sandbox",
            "optional": true,
            "hint": "Defaults to `false`.",
            "type": "boolean"
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "type": "string"
        },
        {
            "label": "SSL client certificate",
            "name": "ssl_client_cert",
            "type": "string"
        },
        {
            "label": "SSL client key",
            "name": "ssl_client_key",
            "type": "string"
        },
        {
            "label": "Custom CA certificate",
            "name": "ssl_key_passphrase",
            "optional": true,
            "type": "string"
        },
        {
            "label": "Unmask sensitive information?",
            "name": "unmask",
            "optional": true,
            "hint": "If Yes, sensitive information will be returned in the response. If No, it will not be returned. Defaults to `false`.",
            "type": "boolean"
        }
    ]
}
```

* * *

### Airbrake

**Provider value:**

```json
"provider": "airbrake"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Api key",
            "name": "api_key",
            "optional": true,
            "type": "string"
        }
    ]
}
```

* * *

### AirREGI

**Provider value:**

```json
"provider": "air_regi"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": []
}
```

* * *

### Airtable

**Provider value:**

```json
"provider": "airtable"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select authentication type. Defaults to API key (Deprecated).",
            "type": "string",
            "pick_list": [
                [
                    "OAuth 2.0",
                    "oauth2_auth_code_grant"
                ],
                [
                    "Personal access token",
                    "personal_token_authentication"
                ],
                [
                    "API key (Deprecated)",
                    "api_key"
                ]
            ]
        },
        {
            "label": "Personal access token",
            "name": "access_token",
            "optional": false,
            "hint": "Provide a personal access token. Go to the following page to create a personal access token in Airtable: https://airtable.com/create/tokens. This only applies when Authentication type is 'personal_token_authentication'.",
            "type": "string"
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "hint": "This only applies when Authentication type is 'OAuth 2.0'.",
            "type": "object",
            "properties": [
                {
                    "label": "Requested permissions (Oauth scopes)",
                    "name": "scopes",
                    "optional": true,
                    "hint": "Select scopes to request for this connection. 'data.records:read' and 'schema.bases:read' are requested automatically. Defaults to 'data.records:read', 'schema.bases:read', 'data.records:write', 'schema.bases:write' if left blank. Separate multiple values with spaces. Refer to the following Airtable documentation for more information: https://airtable.com/developers/web/api/scopes",
                    "type": "string",
                    "pick_list": [
                        [
                            "View records in a base",
                            "records_read"
                        ],
                        [
                            "View table and base schema",
                            "bases_read"
                        ],
                        [
                            "Create, edit, and delete records",
                            "records_write"
                        ],
                        [
                            "Create and edit table and bases",
                            "bases_write"
                        ],
                        [
                            "See comments in records",
                            "read_comment"
                        ],
                        [
                            "Create, edit, and delete record comments",
                            "read_write_comment"
                        ],
                        [
                            "View, create, delete webhooks for a base, as well as fetch webhook payloads.",
                            "read_write_webhook"
                        ],
                        [
                            "View information about user groups under the enterprise, their access, and their members",
                            "read_group"
                        ],
                        [
                            "View metadata about workspaces, bases, and views including collaborators",
                            "read_base"
                        ],
                        [
                            "Edit metadata of workspaces and bases, including collaborators, invites, views, and extensions",
                            "read_write_base"
                        ],
                        [
                            "View, enable, disable and delete share links for bases. Note: Share links can be used to view the data in the base.",
                            "share_base"
                        ],
                        [
                            "Manage the organization's users and groups via SCIM APIs, including provisioning and deprovisioning them.",
                            "read_write_scim"
                        ],
                        [
                            "View the organization's audit logs",
                            "read_audit"
                        ],
                        [
                            "View data about the enterprise account including workspaces ids, users, groups and email domains",
                            "read_account"
                        ],
                        [
                            "View account information of users under the enterprise, including user id, name, email and bases user has access to",
                            "read_user"
                        ],
                        [
                            "Manage users under the enterprise account, including provisioning, deactivating and deleting users",
                            "write_user"
                        ],
                        [
                            "Move bases between workspaces under the enterprise",
                            "manage_bases"
                        ]
                    ]
                }
            ]
        },
        {
            "label": "API key",
            "name": "api_key",
            "optional": false,
            "hint": "You can find the API Key on the account page: https://airtable.com/create/tokens. This only applies when Authentication type is not 'OAuth 2.0' and not 'Personal access token'.",
            "type": "string"
        }
    ]
}
```

* * *

### Amazon Cognito

**Provider value:**

```json
"provider": "aws_cognito"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Access Key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get API key from existing user or create user",
            "type": "string"
        },
        {
            "label": "Secret Access Key",
            "name": "secret_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get secret key from existing user or create user",
            "type": "string"
        },
        {
            "label": "AWS region",
            "name": "aws_region",
            "optional": false,
            "hint": "If your account url is https://eu-west-1.console.aws.amazon.com then use eu-west-1 as the region",
            "type": "string"
        },
        {
            "label": "Cognito user pool",
            "name": "cognito_user_pool",
            "optional": false,
            "type": "object",
            "properties": [
                {
                    "label": "User pool id",
                    "name": "user_pool_id",
                    "optional": false,
                    "hint": "The ID of the Cognito user pool",
                    "type": "string"
                },
                {
                    "label": "App client id",
                    "name": "app_client_id",
                    "optional": false,
                    "hint": "App client id of the app associated with the Cognito user pool",
                    "type": "string"
                },
                {
                    "label": "App client secret",
                    "name": "app_client_secret",
                    "optional": true,
                    "hint": "App client secret of the app associated with the Cognito user pool. Required if the app client is configured with a client secret.",
                    "type": "string"
                }
            ]
        },
        {
            "label": "Cognito identity pool",
            "name": "cognito_identity_pool",
            "optional": false,
            "type": "object",
            "properties": [
                {
                    "label": "Account ID",
                    "name": "account_id",
                    "hint": "AWS account ID (9+ digits)",
                    "type": "string"
                },
                {
                    "label": "Identity pool id",
                    "name": "identity_pool_id",
                    "optional": false,
                    "hint": "The ID of the Cognito identity pool",
                    "type": "string"
                }
            ]
        }
    ]
}
```

* * *

### Amazon Lex

**Provider value:**

```json
"provider": "amazon_lex_nlu"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Bot name",
            "name": "bot_name",
            "hint": "Amazon Lex Bot Name",
            "type": "string"
        },
        {
            "label": "Bot alias",
            "name": "bot_alias",
            "hint": "Amazon Lex Bot Alias",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "hint": "Region",
            "type": "string"
        },
        {
            "label": "Access key ID",
            "name": "access_key_id",
            "hint": "IAM User: Access Key Id (AWS managed policy \"AmazonLexRunBotsOnly\" should be attached to the user)",
            "type": "string"
        },
        {
            "label": "Secret access key",
            "name": "secret_access_key",
            "hint": "IAM User: Secret Access Key",
            "type": "string"
        }
    ]
}
```

* * *

### Amazon S3

**Provider value:**

```json
"provider": "amazon_s3"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authorization type",
            "name": "auth_type",
            "optional": false,
            "hint": "Defaults to Access key (Deprecated). Refer to the Amazon documentation for more information about authorization: https://docs.workato.com/connectors/s3/connection-setup.html#how-to-connect-to-amazon-s3-on-workato",
            "type": "string",
            "pick_list": [
                [
                    "Access key (Deprecated)",
                    "key_secret"
                ],
                [
                    "IAM role",
                    "role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter the IAM role ARN. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authorization type is 'IAM role'.",
            "type": "string"
        },
        {
            "label": "Access key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get API key from existing user or create new user. This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "Secret access key",
            "name": "secret_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get secret key from existing user or create new user. This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "External ID",
            "name": "external_id",
            "optional": true,
            "hint": "This only applies when Authorization type is 'IAM role' and a custom external ID is configured. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html",
            "type": "string"
        },
        {
            "label": "Restrict to bucket",
            "name": "restrict_to_bucket",
            "optional": true,
            "hint": "Use to restrict connection to specified bucket. Needed when this user has only limited s3:ListBucket access. Refer to the following Amazon documentation for more information: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
            "type": "string"
        },
        {
            "label": "Restrict to path",
            "name": "restrict_to_path",
            "optional": true,
            "hint": "Use to restrict connection to specified bucket and object or path. Needed when this user has only limited s3:ListBucket access. This only applies when you enable `Restrict to bucket`. Refer to the following Amazon documentation for more information: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "Region is typically provided in the S3 account URL. If your account URL is https://eu-west-1.console.s3.amazon.com, use eu-west-1 as the region.",
            "type": "string"
        },
        {
            "label": "Download threads",
            "name": "download_threads",
            "optional": true,
            "hint": "Use to boost download speed, default is 1, max is 20.",
            "type": "string"
        }
    ]
}
```

* * *

### Amazon S3 (Secondary)

**Provider value:**

```json
"provider": "amazon_s3_secondary"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authorization type",
            "name": "auth_type",
            "optional": false,
            "hint": "Defaults to Access key (Deprecated). Refer to the Amazon documentation for more information about authorization: https://docs.workato.com/connectors/s3/connection-setup.html#how-to-connect-to-amazon-s3-on-workato",
            "type": "string",
            "pick_list": [
                [
                    "Access key (Deprecated)",
                    "key_secret"
                ],
                [
                    "IAM role",
                    "role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter the IAM role ARN. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authorization type is 'IAM role'.",
            "type": "string"
        },
        {
            "label": "Access key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get API key from existing user or create new user. This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "Secret access key",
            "name": "secret_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get secret key from existing user or create new user. This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "External ID",
            "name": "external_id",
            "optional": true,
            "hint": "This only applies when Authorization type is 'IAM role' and a custom external ID is configured. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html",
            "type": "string"
        },
        {
            "label": "Restrict to bucket",
            "name": "restrict_to_bucket",
            "optional": true,
            "hint": "Use to restrict connection to specified bucket. Needed when this user has only limited s3:ListBucket access. Refer to the following Amazon documentation for more information: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
            "type": "string"
        },
        {
            "label": "Restrict to path",
            "name": "restrict_to_path",
            "optional": true,
            "hint": "Use to restrict connection to specified bucket and object or path. Needed when this user has only limited s3:ListBucket access. This only applies when you enable `Restrict to bucket`. Refer to the following Amazon documentation for more information: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "Region is typically provided in the S3 account URL. If your account URL is https://eu-west-1.console.s3.amazon.com, use eu-west-1 as the region.",
            "type": "string"
        },
        {
            "label": "Download threads",
            "name": "download_threads",
            "optional": true,
            "hint": "Use to boost download speed, default is 1, max is 20.",
            "type": "string"
        }
    ]
}
```

* * *

### Amazon SES

**Provider value:**

```json
"provider": "amazon_ses"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authorization type",
            "name": "auth_type",
            "optional": false,
            "hint": "Select the type of authorization that you require. Defaults to Access key (Deprecated).",
            "type": "string",
            "pick_list": [
                [
                    "Access key (Deprecated)",
                    "key_secret"
                ],
                [
                    "IAM role",
                    "role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter the IAM role ARN. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authorization type is 'IAM role'.",
            "type": "string"
        },
        {
            "label": "Access key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get API key from existing user or create new user. This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "Secret access key",
            "name": "secret_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get secret key from existing user or create new user. This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "Region is typically provided in the SES account URL. If your account URL is https://console.aws.amazon.com/ses/home?region=us-east-1, use us-east-1 as the region.",
            "type": "string"
        }
    ]
}
```

* * *

### Amazon SNS

**Provider value:**

```json
"provider": "aws_sns"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authentication type",
            "name": "auth_type",
            "hint": "Select an authentication method. Defaults to Access key auth.",
            "type": "string",
            "pick_list": [
                [
                    "Access key auth",
                    "aws_key_secret"
                ],
                [
                    "IAM Role auth",
                    "aws_role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter the IAM role ARN. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authentication type is 'IAM Role auth'.",
            "type": "string"
        },
        {
            "label": "External ID",
            "name": "external_id",
            "optional": true,
            "hint": "This only applies when Authentication type is 'IAM Role auth' and a custom external ID is configured. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html",
            "type": "string"
        },
        {
            "label": "Access Key ID",
            "name": "access_key_id",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get API key from existing user or create user. This only applies when Authentication type is not 'IAM Role auth'.",
            "type": "string"
        },
        {
            "label": "Secret Access Key",
            "name": "secret_access_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get secret key from existing user or create user. This only applies when Authentication type is not 'IAM Role auth'.",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "If your account url is https://eu-west-1.console.aws.amazon.com then use eu-west-1 as the region. This only applies when Authentication type is 'IAM Role auth' or 'Access key auth'.",
            "type": "string"
        }
    ]
}
```

* * *

### Amazon SQS

**Provider value:**

```json
"provider": "aws_sqs"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authorization type",
            "name": "auth_type",
            "optional": false,
            "hint": "Defaults to Access key. Refer to the following documentation for more information about Amazon SQS/S3 authorization: https://docs.workato.com/connectors/s3/connection-setup.html#how-to-connect-to-amazon-s3-on-workato",
            "type": "string",
            "pick_list": [
                [
                    "Access key",
                    "key_secret"
                ],
                [
                    "IAM role",
                    "role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter the IAM role ARN. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authorization type is 'IAM role'.",
            "type": "string"
        },
        {
            "label": "Access key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get API key from existing user or create new user. This only applies when Authorization type is 'Access key'.",
            "type": "string"
        },
        {
            "label": "Secret access key",
            "name": "secret_key",
            "optional": false,
            "hint": "Go to AWS account name > My Security Credentials > Users. Get secret key from existing user or create new user. This only applies when Authorization type is 'Access key'.",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "Your SQS queue region, defined in the queue ARN. If your queue ARN is arn:aws:sqs:us-east-1:641923904298:gabriel_standard_q, use us-east-1 as the region.",
            "type": "string"
        },
        {
            "label": "Version",
            "name": "version",
            "optional": false,
            "hint": "Select the SQS API version. Defaults to `2012-11-05`.",
            "type": "string",
            "pick_list": [
                [
                    "2012-11-05",
                    "2012-11-05"
                ]
            ]
        },
        {
            "label": "Service",
            "name": "service",
            "optional": false,
            "hint": "Your SQS queue service, defined in the queue ARN. If your queue ARN is arn:aws:sqs-fips:us-east-1:123456789:bennett_standard_q, use sqs-fips as the service.",
            "type": "string",
            "pick_list": [
                [
                    "SQS",
                    "sqs"
                ],
                [
                    "SQS-FIPS",
                    "sqs-fips"
                ]
            ]
        }
    ]
}
```

* * *

### AMcards

**Provider value:**

```json
"provider": "amcards"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Access token",
            "name": "access_token",
            "optional": false,
            "hint": "Go to the following page to retrieve an access token: https://amcards.com/profile/generate-access-token",
            "type": "string"
        }
    ]
}
```

* * *

### Anaplan

**Provider value:**

```json
"provider": "anaplan"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "hint": "Select an authentication type for your connection. Defaults to Username/password.",
            "type": "string",
            "pick_list": [
                [
                    "OAuth 2.0",
                    "oauth2_auth_code_grant"
                ],
                [
                    "Certificate authentication",
                    "certicate_auth"
                ],
                [
                    "Username/password",
                    "basic_auth"
                ]
            ]
        },
        {
            "label": "Username",
            "name": "username",
            "optional": false,
            "hint": "This only applies when Authentication type is 'Username/password'.",
            "type": "string"
        },
        {
            "label": "Certificate",
            "name": "certificate",
            "optional": false,
            "hint": "Enter a PEM-format certificate string. Learn how to obtain a CA certificate and convert to a PEM string here. This only applies when Authentication type is 'Certificate authentication'. Refer to the following Anaplan documentation for more information: https://help.anaplan.com/anapedia/Content/Administration_and_Security/Tenant_Administration/Security/ProcuringCACertificates.htm",
            "type": "string"
        },
        {
            "label": "Private key",
            "name": "private_key",
            "optional": false,
            "hint": "Enter a PEM-format private key string. This only applies when Authentication type is 'Certificate authentication'.",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "optional": false,
            "hint": "This only applies when Authentication type is 'Username/password'.",
            "type": "string"
        },
        {
            "label": "Data Centre",
            "name": "data_centre",
            "optional": true,
            "hint": "Select the required datacentre. Defaults to Anaplan Data Center.",
            "type": "string",
            "pick_list": [
                [
                    "Anaplan Data Center",
                    "anaplan"
                ],
                [
                    "AWS Australia",
                    "au1a.app2.anaplan"
                ],
                [
                    "GCP Canada",
                    "ca1a.app.anaplan"
                ],
                [
                    "AWS Indonesia",
                    "id1.app.anaplan"
                ]
            ]
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "optional": false,
            "hint": "Your application's client ID. For more information, see how to Create an OAuth 2.0 client. This only applies when Authentication type is 'OAuth 2.0'. Refer to the following Anaplan documentation for more information: https://help.anaplan.com/create-an-oauth-20-client-0984a799-a667-4e70-8759-a134be32f48c",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "optional": false,
            "hint": "Your application's client secret. You can get this value from Administration > Security > OAuth Clients. This only applies when Authentication type is 'OAuth 2.0'.",
            "type": "string"
        }
    ]
}
```

* * *

### Apache Kafka

**Provider value:**

```json
"provider": "kafka"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "On-prem connection profile",
            "name": "profile",
            "hint": "Enter the profile name from the kafka section of your on-prem group's config.yml file to use a connection profile. Refer to the following documentation for more information: https://docs.workato.com/on-prem/agents/connection/profile.html#apache-kafka-profile",
            "type": "string"
        },
        {
            "label": "URL",
            "name": "url",
            "hint": "You can find more information about Kafka connection here. This only applies when using a cloud profile. For example: `kafka://localhost:9092,kafka+ssl://localhost:9093`. Refer to the following documentation for more information: https://docs.workato.com/on-prem/agents/connection/cloud.html#apache-kafka-profile",
            "type": "string"
        },
        {
            "label": "Timeout",
            "name": "timeout",
            "optional": true,
            "hint": "In seconds. This only applies when using a cloud profile",
            "type": "integer"
        },
        {
            "label": "SSL settings",
            "name": "ssl",
            "optional": true,
            "hint": "This only applies when using a cloud profile",
            "type": "object",
            "properties": [
                {
                    "label": "Server certificate",
                    "name": "cert",
                    "optional": true,
                    "hint": "Content or path to X509 server certificate in .pem format. Refer to the following documentation for more information about Kafka SSL configuration: https://docs.workato.com/connectors/kafka.html",
                    "type": "string"
                },
                {
                    "label": "SSL client certificate",
                    "name": "pem",
                    "optional": true,
                    "hint": "Content or path to X509 client certificate in .pem format.",
                    "type": "string"
                },
                {
                    "label": "SSL client key",
                    "name": "key",
                    "optional": true,
                    "hint": "Content or path to RSA client key in .pem format.",
                    "type": "string"
                },
                {
                    "label": "SSL client key password",
                    "name": "keyPassword",
                    "optional": true,
                    "hint": "Optional password for SSL client key.",
                    "type": "string"
                }
            ]
        },
        {
            "label": "Additional properties for Kafka connection",
            "name": "additional_properties",
            "optional": true,
            "hint": "This only applies when using a cloud profile",
            "type": "array",
            "of": "object",
            "properties": [
                {
                    "label": "Key",
                    "name": "key",
                    "type": "string"
                },
                {
                    "label": "Value",
                    "name": "value",
                    "type": "string"
                }
            ]
        }
    ]
}
```

* * *

### Apollo.io

**Provider value:**

```json
"provider": "apollo"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "API key",
            "name": "api_key",
            "optional": false,
            "hint": "Enter an API key from the Developer portal (https://developer.apollo.io/). A master key unlocks all source objects. A scoped key only grants access to contacts and accounts.",
            "type": "string"
        }
    ]
}
```

* * *

### Apttus

**Provider value:**

```json
"provider": "apttus"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Sandbox",
            "name": "sandbox",
            "optional": true,
            "hint": "Is this connecting to a sandbox account? Defaults to `false`.",
            "type": "boolean"
        }
    ]
}
```

* * *

### Apttus Intelligent Cloud

**Provider value:**

```json
"provider": "apttus_intelligent_cloud"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Subdomain",
            "name": "subdomain",
            "optional": false,
            "hint": "Your AIC cloud name as found in your apttus AIC URL",
            "type": "string",
            "url": ".apttuscloud.com"
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "optional": false,
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "optional": false,
            "type": "string"
        },
        {
            "label": "Directory ID",
            "name": "directory_id",
            "optional": false,
            "hint": "Refer to the following page for your directory ID: https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Properties.",
            "type": "string"
        }
    ]
}
```

* * *

### Asana

**Provider value:**

```json
"provider": "asana"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": []
}
```

* * *

### AscentERP

**Provider value:**

```json
"provider": "ascent_erp"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Sandbox",
            "name": "sandbox",
            "optional": true,
            "hint": "Is this connecting to a sandbox account? Defaults to `false`.",
            "type": "boolean"
        }
    ]
}
```

* * *

### AWS Cognito

**Provider value:**

```json
"provider": "aws_cognito"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Access Key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get API key from existing user or create user",
            "type": "string"
        },
        {
            "label": "Secret Access Key",
            "name": "secret_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get secret key from existing user or create user",
            "type": "string"
        },
        {
            "label": "AWS region",
            "name": "aws_region",
            "optional": false,
            "hint": "If your account url is https://eu-west-1.console.aws.amazon.com then use eu-west-1 as the region",
            "type": "string"
        },
        {
            "label": "Cognito user pool",
            "name": "cognito_user_pool",
            "optional": false,
            "type": "object",
            "properties": [
                {
                    "label": "User pool id",
                    "name": "user_pool_id",
                    "optional": false,
                    "hint": "The ID of the Cognito user pool",
                    "type": "string"
                },
                {
                    "label": "App client id",
                    "name": "app_client_id",
                    "optional": false,
                    "hint": "App client id of the app associated with the Cognito user pool",
                    "type": "string"
                },
                {
                    "label": "App client secret",
                    "name": "app_client_secret",
                    "optional": true,
                    "hint": "App client secret of the app associated with the Cognito user pool. Required if the app client is configured with a client secret.",
                    "type": "string"
                }
            ]
        },
        {
            "label": "Cognito identity pool",
            "name": "cognito_identity_pool",
            "optional": false,
            "type": "object",
            "properties": [
                {
                    "label": "Account ID",
                    "name": "account_id",
                    "hint": "AWS account ID (9+ digits)",
                    "type": "string"
                },
                {
                    "label": "Identity pool id",
                    "name": "identity_pool_id",
                    "optional": false,
                    "hint": "The ID of the Cognito identity pool",
                    "type": "string"
                }
            ]
        }
    ]
}
```

* * *

### AWS Lambda

**Provider value:**

```json
"provider": "aws_lambda"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authorization type",
            "name": "auth_type",
            "optional": false,
            "hint": "Defaults to Access key (Deprecated). Refer to the following documentation for more information about AWS Lambda authorization: https://docs.workato.com/connectors/s3/connection-setup.html#how-to-connect-to-amazon-s3-on-workato",
            "type": "string",
            "pick_list": [
                [
                    "Access key (Deprecated)",
                    "key_secret"
                ],
                [
                    "IAM role",
                    "role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter the IAM role ARN. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authorization type is 'IAM role'. Ensure you include all the policies referenced on the following page: https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-features",
            "type": "string"
        },
        {
            "label": "Access Key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get API key from existing user or create user (with AWSLambdaFullAccess permission). This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "Secret Access Key",
            "name": "secret_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get secret key from existing user or create user (with AWSLambdaFullAccess permission). This only applies when Authorization type is 'Access key (Deprecated)'.",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "If your account url is https://eu-west-1.console.aws.amazon.com then use eu-west-1 as the region",
            "type": "string"
        },
        {
            "label": "External ID",
            "name": "external_id",
            "optional": true,
            "hint": "This only applies when Authorization type is 'IAM role' and a custom external ID is configured. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html",
            "type": "string"
        }
    ]
}
```

* * *

### AWS SNS

**Provider value:**

```json
"provider": "aws_sns"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authentication type",
            "name": "auth_type",
            "hint": "Select an authentication method. Defaults to Access key auth.",
            "type": "string",
            "pick_list": [
                [
                    "Access key auth",
                    "aws_key_secret"
                ],
                [
                    "IAM Role auth",
                    "aws_role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter the IAM role ARN. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authentication type is 'IAM Role auth'.",
            "type": "string"
        },
        {
            "label": "External ID",
            "name": "external_id",
            "optional": true,
            "hint": "This only applies when Authentication type is 'IAM Role auth' and a custom external ID is configured. Refer to the Amazon 'Create a role to give permissions to an IAM user' documentation for more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html",
            "type": "string"
        },
        {
            "label": "Access Key ID",
            "name": "access_key_id",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get API key from existing user or create user. This only applies when Authentication type is not 'IAM Role auth'.",
            "type": "string"
        },
        {
            "label": "Secret Access Key",
            "name": "secret_access_key",
            "optional": false,
            "hint": "Click on your AWS account name > Security Credentials > Users. Get secret key from existing user or create user. This only applies when Authentication type is not 'IAM Role auth'.",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "If your account url is https://eu-west-1.console.aws.amazon.com then use eu-west-1 as the region. This only applies when Authentication type is 'IAM Role auth' or 'Access key auth'.",
            "type": "string"
        }
    ]
}
```

* * *

### Azure Blob Storage

**Provider value:**

```json
"provider": "azure_blob_storage"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Storage account",
            "name": "storage_account",
            "optional": false,
            "hint": "Name of your storage account. Go to Azure Portal > select your Storage account.",
            "type": "string"
        },
        {
            "label": "Connection account type",
            "name": "account_type",
            "optional": true,
            "hint": "Choose whether to sign in with a Common, Organization or Tenant-specific connection account type. Common supports personal, enterprise and multi-tenant accounts which are not tenant-specific. Organization supports multi-tenant enterprise accounts. The tenant-specific option requires Tenant ID/Domain to be provided. Default is set to Common type. Learn more about Microsoft account types. Refer to the following documentation for more information: https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration#authority",
            "type": "string",
            "pick_list": [
                [
                    "Common",
                    "common"
                ],
                [
                    "Organization",
                    "organization"
                ],
                [
                    "Tenant specific",
                    "tenant"
                ]
            ]
        },
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select the authentication type. Default is set to Authorization code grant. For Client credentials grant, provide the Client ID and Client secret under Advanced settings and ensure that the app has sufficient permissions to access the Storage account provided in the connection. This only applies when `Connection account type` is 'Tenant specific'. Defaults to Authorization code grant.",
            "type": "string",
            "pick_list": [
                [
                    "Authorization code grant",
                    "oauth2_auth_code_grant"
                ],
                [
                    "Client credentials",
                    "oauth2_client_credentials_grant"
                ]
            ]
        },
        {
            "label": "Tenant ID/Domain",
            "name": "tenant_id",
            "optional": false,
            "hint": "Provide the tenant ID of the Azure Active Directory (Azure AD) tenant (a GUID), or its tenant domain. This only applies when `Connection account type` is 'Tenant specific'.",
            "type": "string"
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "hint": "Advanced settings for the connection.",
            "type": "object",
            "properties": [
                {
                    "label": "OAuth 2.0 authorization code scopes",
                    "name": "auth_code_scopes",
                    "optional": true,
                    "hint": "Select additional OAuth 2.0 authorization code grant scopes to request for this connection. The `Management` scope is required to set up dynamic webhook triggers under Azure Blob Storage. The selected scopes are added to the minimal scopes required to establish a connection with Azure Blob Storage. If left blank, the default scopes are set. This only applies when `Authentication type` is not 'Client credentials'.",
                    "type": "string",
                    "delimiter": " "
                },
                {
                    "label": "OAuth 2.0 client credentials scopes",
                    "name": "client_credential_scopes",
                    "optional": true,
                    "hint": "Select additional OAuth 2.0 client credentials grant scopes to request for this connection. Make sure that the specified scopes are also defined in your Azure app registration. The `Management` scope is required to set up dynamic webhook triggers under Azure Blob Storage. The selected scopes are added to the minimal scopes required to establish a connection with Azure Blob Storage. If left blank, the default scopes are set. This only applies when `Authentication type` is 'Client credentials'.",
                    "type": "string",
                    "delimiter": " "
                },
                {
                    "label": "Client ID",
                    "name": "client_id",
                    "optional": true,
                    "hint": "Go to **Azure Portal > select App registrations > select your Application** to get your client ID. Refer to the Azure `Authorize access to blobs by using Microsoft Entra ID` documentation for more information: https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app. Required if authentication type is set to `Client credentials`.",
                    "type": "string"
                },
                {
                    "label": "Client secret",
                    "name": "client_secret",
                    "optional": true,
                    "hint": "Go to **Azure Portal > select App registrations > select your Application > select Certificates & secrets** to get your client secret. Refer to the Azure `Authorize access to blobs by using Microsoft Entra ID` documentation for more information: https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app. Required if authentication type is set to `Client credentials`.",
                    "type": "string"
                },
                {
                    "label": "Access key",
                    "name": "access_key",
                    "optional": true,
                    "hint": "Optional. Enter an access key for the **Generate presigned URL** action. Go to Azure Portal of your account and select the Storage account used for this connection to get your access key.",
                    "type": "string"
                }
            ]
        }
    ]
}
```

* * *

### Azure Key Vault

**Provider value:**

```json
"provider": "azure_key_vault"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Vault URL",
            "name": "vault_url",
            "type": "string"
        },
        {
            "label": "Tenant ID",
            "name": "tenant_id",
            "type": "string"
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "type": "string"
        },
        {
            "label": "Client Secret",
            "name": "client_secret",
            "type": "string"
        }
    ]
}
```

* * *

### Azure Monitor

**Provider value:**

```json
"provider": "azure_monitor"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select the authentication type. Its recommended to use client credential authentication type since shared key is deprecated. Defaults to Client Credentials.",
            "type": "string",
            "pick_list": [
                [
                    "Client Credentials",
                    "client_credentials"
                ],
                [
                    "Shared Key",
                    "api_key"
                ]
            ]
        },
        {
            "label": "Tenant ID",
            "name": "tenant_id",
            "optional": false,
            "hint": "Enter the tenant ID of your Open Connect client. This only applies when `Authentication type` is 'Client Credentials'.",
            "type": "string"
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "optional": false,
            "hint": "Enter the client ID of your Open Connect client. This only applies when `Authentication type` is 'Client Credentials'.",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "optional": false,
            "hint": "Enter the client secret of your Open Connect client. This only applies when `Authentication type` is 'Client Credentials'.",
            "type": "string"
        },
        {
            "label": "Data collection endpoint",
            "name": "host",
            "optional": false,
            "hint": "Enter your data collection endpoint URL. For example: https://your-instance-name.useast-1.ingest.monitor.azure.com. This only applies when `Authentication type` is 'Client Credentials'.",
            "type": "string"
        },
        {
            "label": "Workspace ID",
            "name": "workspace_id",
            "optional": false,
            "hint": "Enter the ID of your logs analytics Workspace. Go to **Settings > Log Analytics** in your logs analytics workspace and click **agents** to retrieve this value. This only applies when `Authentication type` is 'Shared Key'.",
            "type": "string"
        },
        {
            "label": "Shared key",
            "name": "shared_key",
            "optional": false,
            "hint": "Enter the primary or secondary key of the Workspace. Go to **Settings > Log Analytics** in your logs analytics workspace and click **agents** to retrieve this value. This only applies when `Authentication type` is 'Shared Key'.",
            "type": "string"
        }
    ]
}
```

* * *

### Azure OpenAI

**Provider value:**

```json
"provider": "azure_open_ai"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select the authentication type. Default is set to Api key.",
            "type": "string",
            "pick_list": [
                [
                    "Api key",
                    "api_key"
                ],
                [
                    "OAuth 2.0",
                    "oauth2_auth_code_grant"
                ]
            ]
        },
        {
            "label": "Api key",
            "name": "api_key",
            "optional": false,
            "hint": "Provide an API key. This only applies when Authentication type is 'Api key'. Refer to the following documentation for more information: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#authentication",
            "type": "string"
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "optional": false,
            "hint": "Provide the OAuth 2.0 Client ID for your Azure application. This only applies when Authentication type is 'OAuth 2.0'.",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "optional": false,
            "hint": "Provide the OAuth 2.0 Client secret for your Azure application. This only applies when Authentication type is 'OAuth 2.0'.",
            "type": "string"
        },
        {
            "label": "Sub domain",
            "name": "sub_domain",
            "optional": false,
            "hint": "Enter the subdomain of your organization.",
            "type": "string",
            "url": ".openai.azure.com"
        }
    ]
}
```

* * *

### BambooHR

**Provider value:**

```json
"provider": "bamboohr"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Choose how you want to authenticate. Defaults to 'api_token'.",
            "type": "string",
            "pick_list": [
                [
                    "API Token",
                    "api_token"
                ],
                [
                    "OAuth2.0",
                    "oauth2.0"
                ]
            ]
        },
        {
            "label": "API token",
            "name": "api_token",
            "optional": false,
            "hint": "Enter your sub-domain in the following URL to retrieve an API token: 'https://[sub-domain].bamboohr.com/settings/permissions/api.php'. This only applies when authentication type is 'api_token'.",
            "type": "string"
        },
        {
            "label": "Sub-domain",
            "name": "subdomain",
            "optional": false,
            "hint": "Your BambooHR subdomain is most often your company name.",
            "type": "string"
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "hint": "This only applies when authentication type is 'oauth2.0'.",
            "type": "object",
            "properties": [
                {
                    "label": "OAuth scopes",
                    "name": "scope",
                    "optional": true,
                    "hint": "Select scopes (https://documentation.bamboohr.com/reference/scopes) to request for this connection. Defaults to the following scopes: 'openid', 'offline_access', 'email', 'public.user', 'employee_directory', 'employee', 'employee.write', 'employee:custom_fields', 'employee:custom_fields.write', 'employee:job', 'employee:job.write', 'employee:contact', 'employee:contact.write', 'employee:education', 'employee:education.write', 'employee:emergency_contacts', 'employee:emergency_contacts.write', 'employee:dependent', 'employee:dependent.write', 'employee:assets', 'employee:assets.write', 'employee:compensation', 'employee:compensation.write', 'employee:identification', 'employee:identification.write', 'employee:vaccination', 'employee:vaccination.write', 'employee:name', 'employee:name.write', 'employee:demographic', 'employee:demographic.write', 'employee:payroll', 'employee:payroll.write', 'employee:photo', 'employee:tabs', 'employee:tabs.write', 'employee:management', 'employee:management.write', 'sensitive_employee:address', 'sensitive_employee:address.write', 'sensitive_employee:creditcards', 'sensitive_employee:creditcards.write', 'benefit', 'benefit.write', 'time_off', 'time_off.write', 'report', 'field', 'user', 'webhooks'. The following are included in addition to any custom selected scopes: 'public.user', 'employee', 'offline_access', 'openid', 'email'. When 'public.integration' is selected, only 'offline_access' is included as a minimum scope instead; 'public.user', 'employee', 'openid' and 'email' are incompatible with 'public.integration' and aren't appended. Separate multiple values with spaces.",
                    "type": "string",
                    "delimiter": " ",
                    "options": [
                        [
                            "Employee - Write",
                            "employee.write"
                        ],
                        [
                            "Employee - Assets",
                            "employee:assets"
                        ],
                        [
                            "Employee - Assets Write",
                            "employee:assets.write"
                        ],
                        [
                            "Employee - Compensation",
                            "employee:compensation"
                        ],
                        [
                            "Employee - Compensation Write",
                            "employee:compensation.write"
                        ],
                        [
                            "Employee - Contact",
                            "employee:contact"
                        ],
                        [
                            "Employee - Contact Write",
                            "employee:contact.write"
                        ],
                        [
                            "Employee - Custom Fields",
                            "employee:custom_fields"
                        ],
                        [
                            "Employee - Custom Fields Write",
                            "employee:custom_fields.write"
                        ],
                        [
                            "Employee - Custom Fields Encrypted",
                            "employee:custom_fields_encrypted"
                        ],
                        [
                            "Employee - Custom Fields Encrypted Write",
                            "employee:custom_fields_encrypted.write"
                        ],
                        [
                            "Employee - Demographic",
                            "employee:demographic"
                        ],
                        [
                            "Employee - Demographic Write",
                            "employee:demographic.write"
                        ],
                        [
                            "Employee - Dependent",
                            "employee:dependent"
                        ],
                        [
                            "Employee - Dependent Write",
                            "employee:dependent.write"
                        ],
                        [
                            "Employee - Dependent SSN",
                            "employee:dependent:ssn"
                        ],
                        [
                            "Employee - Dependent SSN Write",
                            "employee:dependent:ssn.write"
                        ],
                        [
                            "Employee - Education",
                            "employee:education"
                        ],
                        [
                            "Employee - Education Write",
                            "employee:education.write"
                        ],
                        [
                            "Employee - Emergency Contacts",
                            "employee:emergency_contacts"
                        ],
                        [
                            "Employee - Emergency Contacts Write",
                            "employee:emergency_contacts.write"
                        ],
                        [
                            "Employee - File",
                            "employee:file"
                        ],
                        [
                            "Employee - File Write",
                            "employee:file.write"
                        ],
                        [
                            "Employee - Identification",
                            "employee:identification"
                        ],
                        [
                            "Employee - Identification Write",
                            "employee:identification.write"
                        ],
                        [
                            "Employee - Job",
                            "employee:job"
                        ],
                        [
                            "Employee - Job Write",
                            "employee:job.write"
                        ],
                        [
                            "Employee - Management",
                            "employee:management"
                        ],
                        [
                            "Employee - Management Write",
                            "employee:management.write"
                        ],
                        [
                            "Employee - Name",
                            "employee:name"
                        ],
                        [
                            "Employee - Name Write",
                            "employee:name.write"
                        ],
                        [
                            "Employee - Payroll",
                            "employee:payroll"
                        ],
                        [
                            "Employee - Payroll Write",
                            "employee:payroll.write"
                        ],
                        [
                            "Employee - Photo",
                            "employee:photo"
                        ],
                        [
                            "Employee - Photo Write",
                            "employee:photo.write"
                        ],
                        [
                            "Employee - Providers",
                            "employee:providers"
                        ],
                        [
                            "Employee - Providers Write",
                            "employee:providers.write"
                        ],
                        [
                            "Employee - Providers Payroll",
                            "employee:providers:payroll"
                        ],
                        [
                            "Employee - Providers Payroll Write",
                            "employee:providers:payroll.write"
                        ],
                        [
                            "Employee - Tabs",
                            "employee:tabs"
                        ],
                        [
                            "Employee - Tabs Write",
                            "employee:tabs.write"
                        ],
                        [
                            "Employee - Vaccination",
                            "employee:vaccination"
                        ],
                        [
                            "Employee - Vaccination Write",
                            "employee:vaccination.write"
                        ],
                        [
                            "Employee Directory",
                            "employee_directory"
                        ],
                        [
                            "Company - Administration",
                            "company:administration"
                        ],
                        [
                            "Company - Administration Write",
                            "company:administration.write"
                        ],
                        [
                            "Company - Info",
                            "company:info"
                        ],
                        [
                            "Company - Details",
                            "company:details"
                        ],
                        [
                            "Company - Details Write",
                            "company:details.write"
                        ],
                        [
                            "Company - File",
                            "company_file"
                        ],
                        [
                            "Company - File Write",
                            "company_file.write"
                        ],
                        [
                            "Sensitive Employee - Address",
                            "sensitive_employee:address"
                        ],
                        [
                            "Sensitive Employee - Address Write",
                            "sensitive_employee:address.write"
                        ],
                        [
                            "Sensitive Employee - Credit Cards",
                            "sensitive_employee:creditcards"
                        ],
                        [
                            "Sensitive Employee - Credit Cards Write",
                            "sensitive_employee:creditcards.write"
                        ],
                        [
                            "Sensitive Employee - Protected Info",
                            "sensitive_employee:protected_info"
                        ],
                        [
                            "Sensitive Employee - Protected Info Write",
                            "sensitive_employee:protected_info.write"
                        ],
                        [
                            "Hiring - Applications",
                            "hiring:applications"
                        ],
                        [
                            "Hiring - Applications Write",
                            "hiring:applications.write"
                        ],
                        [
                            "Hiring - Job Openings",
                            "hiring:job_openings"
                        ],
                        [
                            "Hiring - Job Openings Write",
                            "hiring:job_openings.write"
                        ],
                        [
                            "Hiring - Checkr",
                            "hiring:checkr"
                        ],
                        [
                            "Hiring - Checkr Write",
                            "hiring:checkr.write"
                        ],
                        [
                            "Hiring - Offers",
                            "hiring:offers"
                        ],
                        [
                            "Hiring - Offers Write",
                            "hiring:offers.write"
                        ],
                        [
                            "Hiring - Settings",
                            "hiring:settings"
                        ],
                        [
                            "Hiring - Settings Write",
                            "hiring:settings.write"
                        ],
                        [
                            "Hiring - Talent Pools",
                            "hiring:talent_pools"
                        ],
                        [
                            "Hiring - Talent Pools Write",
                            "hiring:talent_pools.write"
                        ],
                        [
                            "Benefit",
                            "benefit"
                        ],
                        [
                            "Benefit Write",
                            "benefit.write"
                        ],
                        [
                            "Data Cleaner",
                            "data_cleaner"
                        ],
                        [
                            "Data Cleaner Write",
                            "data_cleaner.write"
                        ],
                        [
                            "Error Management",
                            "error_management"
                        ],
                        [
                            "Error Management Write",
                            "error_management.write"
                        ],
                        [
                            "Goal",
                            "goal"
                        ],
                        [
                            "Goal Write",
                            "goal.write"
                        ],
                        [
                            "Tasks",
                            "tasks"
                        ],
                        [
                            "Tasks Write",
                            "tasks.write"
                        ],
                        [
                            "Access Level",
                            "access_level"
                        ],
                        [
                            "Benchmarking Compensation",
                            "benchmarking:compensation"
                        ],
                        [
                            "Compensation Benchmarks",
                            "compensation_benchmarks"
                        ],
                        [
                            "Compensation Benchmarks Write",
                            "compensation_benchmarks.write"
                        ],
                        [
                            "Field",
                            "field"
                        ],
                        [
                            "Field Write",
                            "field.write"
                        ],
                        [
                            "Gridlets",
                            "gridlets"
                        ],
                        [
                            "Meta",
                            "meta"
                        ],
                        [
                            "Training",
                            "training"
                        ],
                        [
                            "Training Write",
                            "training.write"
                        ],
                        [
                            "User",
                            "user"
                        ],
                        [
                            "User Management",
                            "user:management"
                        ],
                        [
                            "User Management Write",
                            "user:management.write"
                        ],
                        [
                            "Webhooks",
                            "webhooks"
                        ],
                        [
                            "Webhooks Write",
                            "webhooks.write"
                        ],
                        [
                            "Payroll",
                            "payroll"
                        ],
                        [
                            "Payroll Write",
                            "payroll.write"
                        ],
                        [
                            "Payroll - ACH Returns",
                            "payroll:ach_returns"
                        ],
                        [
                            "Payroll - ACH Returns Write",
                            "payroll:ach_returns.write"
                        ],
                        [
                            "Payroll - Beneficial Owners",
                            "payroll:beneficial_owners"
                        ],
                        [
                            "Payroll - Beneficial Owners Write",
                            "payroll:beneficial_owners.write"
                        ],
                        [
                            "Payroll - Earnings",
                            "payroll:earnings"
                        ],
                        [
                            "Payroll - Legal Entities",
                            "payroll:legal_entities"
                        ],
                        [
                            "Payroll - Pay Cycles",
                            "payroll:pay_cycles"
                        ],
                        [
                            "Payroll - Pay Periods",
                            "payroll:pay_periods"
                        ],
                        [
                            "Payroll - Pay Schedules",
                            "payroll:pay_schedules"
                        ],
                        [
                            "Payroll - Pay Stubs",
                            "payroll:pay_stubs"
                        ],
                        [
                            "Payroll - Payrolls",
                            "payroll:payrolls"
                        ],
                        [
                            "Payroll - Retirements",
                            "payroll:retirements"
                        ],
                        [
                            "Report",
                            "report"
                        ],
                        [
                            "Time Off",
                            "time_off"
                        ],
                        [
                            "Time Off Write",
                            "time_off.write"
                        ],
                        [
                            "Time Tracking",
                            "time_tracking"
                        ],
                        [
                            "Time Tracking Write",
                            "time_tracking.write"
                        ],
                        [
                            "Public Integration",
                            "public.integration"
                        ],
                        [
                            "Public User",
                            "public.user"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### Basecamp 2

**Provider value:**

```json
"provider": "basecamp"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Account ID",
            "name": "account_id",
            "hint": "Your account ID is the numeric portion of the browser URL shown when you're logged in. For example, '2551808' is the account ID in the following URL: 'https://basecamp.com/2551808/'.",
            "type": "integer"
        }
    ]
}
```

* * *

### Bigtincan

**Provider value:**

```json
"provider": "bigtincan"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": []
}
```

* * *

### Bill.com

**Provider value:**

```json
"provider": "bill"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "User name",
            "name": "userName",
            "hint": "Enter the user's email ID.",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "hint": "Enter the user's password.",
            "type": "string"
        },
        {
            "label": "Organization ID",
            "name": "orgId",
            "hint": "Refer to the following documentation to learn how to get this ID: 'https://developer.bill.com/v2/docs/sign-up-process#retrieve-organization-id-with-the-api'.",
            "type": "string"
        },
        {
            "label": "Environment",
            "name": "environment",
            "optional": false,
            "hint": "Refer to the sandbox environment details (https://developer.bill.com/hc/en-us/articles/360035430211-Sandbox-Environment) or production environment details (https://developer.bill.com/hc/en-us/articles/360035431311-Production-Environment) for more information. Defaults to 'api'.",
            "type": "string",
            "pick_list": [
                [
                    "Production",
                    "api"
                ],
                [
                    "Sandbox",
                    "api-stage"
                ]
            ]
        },
        {
            "label": "Dev key",
            "name": "devKey",
            "optional": true,
            "hint": "Optional. Enter a developer key. The default key is used if you don't provide one. Refer to the following documentation to retrieve a developer key: https://developer.bill.com/docs/api-sandbox-sign-up#generate-developer-key",
            "type": "string"
        }
    ]
}
```

* * *

### BIM 360

**Provider value:**

```json
"provider": "bim360"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Advanced settings",
            "name": "custom_oauth",
            "optional": true,
            "hint": "Enter the client ID and secret of the custom Autodesk Platform Services (APS) OAuth App. Required in case the BIM 360 instance is located outside the US. Refer to the following documentation to learn more about creating the custom APS OAuth App: 'https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/'.",
            "type": "object",
            "properties": [
                {
                    "label": "Client ID",
                    "name": "client_id",
                    "optional": true,
                    "hint": "Enter the Client ID to set up a custom OAuth connection. Refer to the following documentation to learn how to generate the client ID: 'https://docs.workato.com/connectors/bim360.html#how-to-connect-to-bim-360-on-workato'.",
                    "type": "string"
                },
                {
                    "label": "Client secret",
                    "name": "client_secret",
                    "optional": true,
                    "hint": "Enter the Client secret to set up a custom OAuth connection. Refer to the following documentation to learn how to generate the client secret: 'https://docs.workato.com/connectors/bim360.html#how-to-connect-to-bim-360-on-workato'.",
                    "type": "string"
                },
                {
                    "label": "Requested permissions (OAuth scopes)",
                    "name": "scopes",
                    "optional": true,
                    "hint": "Select permissions to request for this connection. Defaults to 'user:read', 'account:read', 'data:write', 'data:read', 'data:create', 'account:write' if left blank. Selecting permissions from picklist overwrites the default permission. The minimum permission required is 'user-profile:read'; this is requested in addition to selected permissions. Separate multiple values with spaces. Refer to the following documentation for more information about scopes: 'https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/scopes'.",
                    "type": "string",
                    "options": [
                        [
                            "user:read",
                            "user:read"
                        ],
                        [
                            "account:read",
                            "account:read"
                        ],
                        [
                            "data:write",
                            "data:write"
                        ],
                        [
                            "data:read",
                            "data:read"
                        ],
                        [
                            "data:create",
                            "data:create"
                        ],
                        [
                            "account:write",
                            "account:write"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### Bitbucket

**Provider value:**

```json
"provider": "bitbucket"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Bitbucket hostname",
            "name": "hostname",
            "optional": true,
            "hint": "Host (and optional port) of your server. For example, 'http://localhost:7990/rest/api'. This only applies when using an on-prem agent.",
            "type": "string"
        }
    ]
}
```

* * *

### Box

**Provider value:**

```json
"provider": "box"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select an authentication type for your connection. Defaults to 'oauth2_auth_code_grant'.",
            "type": "string",
            "pick_list": [
                [
                    "Authorization code grant",
                    "oauth2_auth_code_grant"
                ],
                [
                    "Client credentials",
                    "client_credentials"
                ],
                [
                    "JWT",
                    "jwt"
                ]
            ]
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "hint": "This only applies when authentication type is 'oauth2_auth_code_grant'.",
            "type": "object",
            "properties": [
                {
                    "label": "Requested permissions (Oauth scopes)",
                    "name": "api_scope",
                    "optional": true,
                    "hint": "Select permissions (https://developer.box.com/docs/scopes) to request for this connection. Defaults to the following scopes: 'root_readonly', 'root_readwrite', 'manage_app_users', 'manage_managed_users', 'manage_groups', 'manage_webhook'. Selecting permissions from picklist overwrites the default permission. The minimum permission required is 'root_readonly'; this is requested in addition to selected permissions. Separate multiple values with commas.",
                    "type": "string",
                    "delimiter": ",",
                    "options": [
                        [
                            "Read files and folders",
                            "root_readonly"
                        ],
                        [
                            "Read and write files and folders",
                            "root_readwrite"
                        ],
                        [
                            "Manage app users",
                            "manage_app_users"
                        ],
                        [
                            "Manage managed users",
                            "manage_managed_users"
                        ],
                        [
                            "Manage groups",
                            "manage_groups"
                        ],
                        [
                            "Manage webhooks",
                            "manage_webhook"
                        ],
                        [
                            "Manage enterprise properties",
                            "manage_enterprise_properties"
                        ],
                        [
                            "Manage retention policies",
                            "manage_data_retention"
                        ],
                        [
                            "Global content manager",
                            "gcm"
                        ],
                        [
                            "Admin can make calls on behalf of users",
                            "admin_on_behalf_of"
                        ],
                        [
                            "Manage signature requests",
                            "sign_requests.readwrite"
                        ],
                        [
                            "Manage Box AI API",
                            "ai.readwrite"
                        ],
                        [
                            "Manage Box Relay",
                            "manage_triggers"
                        ]
                    ]
                }
            ]
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "hint": "Enter the client ID. This only applies when authentication type is 'client_credentials' or 'jwt'.",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "hint": "Enter the client secret. This only applies when authentication type is 'client_credentials' or 'jwt'.",
            "type": "string"
        },
        {
            "label": "Subject type",
            "name": "subject_type",
            "hint": "Select the subject type for authentication. This only applies when authentication type is 'client_credentials' or 'jwt'. Defaults to 'user'.",
            "type": "string",
            "pick_list": [
                [
                    "Service account",
                    "enterprise"
                ],
                [
                    "Managed user",
                    "user"
                ]
            ]
        },
        {
            "label": "Enterprise ID",
            "name": "enterprise_id",
            "hint": "Enter the Enterprise ID. This only applies when authentication type is 'client_credentials' or 'jwt', and subject type is 'enterprise'.",
            "type": "string"
        },
        {
            "label": "User ID",
            "name": "user_id",
            "hint": "Enter the User ID. This only applies when authentication type is 'client_credentials' or 'jwt', and subject type is 'user'.",
            "type": "string"
        },
        {
            "label": "Private key",
            "name": "private_key",
            "hint": "Enter the RSA private key for JWT signing. This is the private key that corresponds to the public key configured in your Box app. This only applies when authentication type is 'jwt'.",
            "type": "string"
        },
        {
            "label": "Private Key Passphrase",
            "name": "private_key_passphrase",
            "optional": true,
            "hint": "Optional. Enter a passphrase for the private key if it is encrypted. This only applies when authentication type is 'jwt'.",
            "type": "string"
        },
        {
            "label": "Public key ID",
            "name": "public_key_id",
            "optional": true,
            "hint": "Enter the ID of the public key used to sign the JWT. Use this when an application defines multiple key pairs. This only applies when authentication type is 'jwt'.",
            "type": "string"
        }
    ]
}
```

* * *

### Braintree

**Provider value:**

```json
"provider": "braintree"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Merchant ID",
            "name": "merchant_id",
            "optional": false,
            "hint": "Enter a merchant ID from Settings > API in the Braintree control panel.",
            "type": "string"
        },
        {
            "label": "Public key",
            "name": "public_key",
            "optional": false,
            "hint": "Enter a public key from Settings > API in the Braintree control panel.",
            "type": "string"
        },
        {
            "label": "Private key",
            "name": "private_key",
            "optional": false,
            "hint": "Enter a private key from Settings > API in the Braintree control panel.",
            "type": "string"
        },
        {
            "label": "Environment",
            "name": "environment",
            "optional": false,
            "hint": "Defaults to 'PRODUCTION'.",
            "type": "string",
            "pick_list": [
                [
                    "Production",
                    "PRODUCTION"
                ],
                [
                    "Sandbox",
                    "SANDBOX"
                ]
            ]
        }
    ]
}
```

* * *

### BrickFTP

**Provider value:**

```json
"provider": "brick_ftp"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "API Key",
            "name": "api_key",
            "hint": "Go to 'https://yoursite.brickftp.com/sites/edit?group=api' to enable REST and retrieve an API key.",
            "type": "string"
        }
    ]
}
```

* * *

### Bynder

**Provider value:**

```json
"provider": "bynder"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Domain",
            "name": "base_url",
            "optional": false,
            "hint": "Enter the Bynder domain found in your Bynder URL. For example, 'acme.getbynder.com' is the domain in the following URL: 'https://acme.getbynder.com'.",
            "type": "string"
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "type": "object",
            "properties": [
                {
                    "label": "Scopes",
                    "name": "scopes",
                    "optional": true,
                    "hint": "Specify the scopes to request for this connection. Refer to the following documentation for the scopes we request by default: https://docs.workato.com/connectors/bynder.html. Separate multiple values with spaces.",
                    "type": "string",
                    "delimiter": " ",
                    "options": [
                        [
                            "Read asset usage",
                            "asset.usage:read"
                        ],
                        [
                            "Asset read",
                            "asset:read"
                        ],
                        [
                            "Asset write",
                            "asset:write"
                        ],
                        [
                            "Create & delete asset usage",
                            "asset.usage:write"
                        ],
                        [
                            "Read collections",
                            "collection:read"
                        ],
                        [
                            "Write collections",
                            "collection:write"
                        ],
                        [
                            "Create & delete metaproperty and dependency",
                            "meta.assetbank:write"
                        ],
                        [
                            "Workflow campaign read",
                            "workflow.campaign:read"
                        ],
                        [
                            "Workflow campaign write",
                            "workflow.campaign:write"
                        ],
                        [
                            "Workflow group read",
                            "workflow.group:read"
                        ],
                        [
                            "Workflow group write",
                            "workflow.group:write"
                        ],
                        [
                            "Workflow job read",
                            "workflow.job:read"
                        ],
                        [
                            "Workflow job write",
                            "workflow.job:write"
                        ],
                        [
                            "Workflow preset read",
                            "workflow.preset:read"
                        ],
                        [
                            "Brandstore order read",
                            "brandstore.order:read"
                        ],
                        [
                            "Brandstore order write",
                            "brandstore.order:write"
                        ],
                        [
                            "Meta workflow read",
                            "meta.workflow:read"
                        ],
                        [
                            "Current profile read",
                            "current.profile:read"
                        ],
                        [
                            "Current user read",
                            "current.user:read"
                        ],
                        [
                            "Admin profile read",
                            "admin.profile:read"
                        ],
                        [
                            "Admin user read",
                            "admin.user:read"
                        ],
                        [
                            "Admin user write",
                            "admin.user:write"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### Callable recipes by Workato

**Provider value:**

```json
"provider": "workato_service"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### CandidateZip

**Provider value:**

```json
"provider": "candidate_zip"
```

* * *

### Celonis

**Provider value:**

```json
"provider": "celonis"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Chargebee

**Provider value:**

```json
"provider": "chargebee"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "API key",
            "name": "api_key",
            "optional": false,
            "hint": "Enter a Chargebee API key with access to API v1 and v2.",
            "type": "string"
        },
        {
            "label": "Subdomain",
            "name": "subdomain",
            "optional": false,
            "hint": "Enter your Chargebee subdomain.",
            "type": "string"
        },
        {
            "label": "Product catalog",
            "name": "product_catalog",
            "optional": false,
            "hint": "Select the Chargebee product catalog for this connection. Defaults to 'PC 2.0'.",
            "type": "string",
            "pick_list": [
                [
                    "PC 1.0",
                    "PC 1.0"
                ],
                [
                    "PC 2.0",
                    "PC 2.0"
                ]
            ]
        }
    ]
}
```

* * *

### Chatter

**Provider value:**

```json
"provider": "chatter"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": []
}
```

* * *

### Cisco Webex Teams

**Provider value:**

```json
"provider": "cisco_spark"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select authentication type. Defaults to 'oauth2_auth_code_grant'.",
            "type": "string",
            "pick_list": [
                [
                    "OAuth 2.0",
                    "oauth2_auth_code_grant"
                ],
                [
                    "Bot access token",
                    "bot_token"
                ]
            ]
        },
        {
            "label": "Bot access token",
            "name": "access_token",
            "optional": false,
            "hint": "Enter a Bot access token. Refer to the following URL to create a bot in the developer portal and obtain an access token: 'https://developer.webex.com/docs/bots'. This only applies when authentication type is 'bot_token'.",
            "type": "string"
        }
    ]
}
```

* * *

### Clearbit

**Provider value:**

```json
"provider": "clearbit"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Api key",
            "name": "api_key",
            "optional": true,
            "hint": "Enter your Clearbit API key. Refer to the following page to retrieve this value: 'https://dashboard.clearbit.com/keys'",
            "type": "string"
        }
    ]
}
```

* * *

### Cloud Watch

**Provider value:**

```json
"provider": "cloud_watch"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Authorization type",
            "name": "auth_type",
            "optional": false,
            "hint": "Specify the authentication type to use for this connection. Defaults to 'key_secret'. Refer to the AWS Cloud Watch authorization guide for more information: 'https://docs.workato.com/connectors/s3/connection-setup.html#how-to-connect-to-amazon-s3-on-workato'.",
            "type": "string",
            "pick_list": [
                [
                    "Access key",
                    "key_secret"
                ],
                [
                    "IAM role",
                    "role_based"
                ]
            ]
        },
        {
            "label": "IAM role ARN",
            "name": "assume_role",
            "optional": false,
            "hint": "Enter an IAM role ARN. Workato generates a unique external ID for every Workato user, such as 'workato-user-84762'. You must provide this external ID when creating an IAM role in Amazon S3 and include all policies listed in the following AWS guide: (https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-features). Refer to the following documentation for more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html. This only applies when Authorization type is 'role_based'.",
            "type": "string"
        },
        {
            "label": "Access Key ID",
            "name": "api_key",
            "optional": false,
            "hint": "Enter an API key. Sign in to your AWS account and go to 'My Security Credentials > Users' to retrieve this value. This only applies when Authorization type is 'key_secret'.",
            "type": "string"
        },
        {
            "label": "Secret Access Key",
            "name": "secret_key",
            "optional": false,
            "hint": "Enter a secret key. Sign in to your AWS account and go to 'My Security Credentials > Users' to retrieve this value. This only applies when Authorization type is 'key_secret'.",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "Enter your AWS region. For example, 'eu-west-1' is the region in the following account url: 'https://eu-west-1.console.aws.amazon.com'",
            "type": "string"
        },
        {
            "label": "External ID",
            "name": "external_id",
            "optional": true,
            "hint": "Use this field's current value as the External ID in the new role definition if you're migrating to a new IAM role. Refer to the following documentation for more information: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html'. This only applies when Authorization type is 'role_based' and an external ID is configured.",
            "type": "string"
        }
    ]
}
```

* * *

### Codeship

**Provider value:**

```json
"provider": "codeship"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "API key",
            "name": "api_key",
            "optional": false,
            "hint": "Enter a Codeship API key. Sign in to Codeship and go to 'My Account > Account settings' to retrieve this value.",
            "type": "string"
        }
    ]
}
```

* * *

### Collection by Workato

**Provider value:**

```json
"provider": "workato_smart_list"
```

* * *

### Confluence

**Provider value:**

```json
"provider": "confluence"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Auth type",
            "name": "auth_type",
            "type": "string",
            "pick_list": [
                [
                    "Basic",
                    "basic"
                ],
                [
                    "API token",
                    "api_token"
                ],
                [
                    "OAuth 2.0",
                    "oauth"
                ]
            ]
        },
        {
            "label": "Confluence subdomain",
            "name": "subdomain",
            "optional": false,
            "hint": "Enter the Confluence subdomain found in your URL. This doesn't apply when using an on-prem agent.",
            "type": "string"
        },
        {
            "label": "Confluence root URI",
            "name": "root_uri",
            "optional": false,
            "hint": "Enter the root URI (protocol, optional port, hostname) of your Confluence host. For example, 'https://confluence.intranet.acme.com:7654'. Most built-in actions only support Confluence Cloud. Use Custom Actions for Data Center. This field only applies when using an on-prem agent.",
            "type": "string"
        },
        {
            "label": "Email",
            "name": "email",
            "hint": "This only applies when Auth type is 'api_token'.",
            "type": "string"
        },
        {
            "label": "API token",
            "name": "apitoken",
            "hint": "Enter your Confluence API token. Refer to the following page to retrieve this value: 'https://id.atlassian.com/manage/api-tokens'. This only applies when Auth type is 'api_token'.",
            "type": "string"
        },
        {
            "label": "Username",
            "name": "username",
            "hint": "Enter your user name (not email). This only applies when Auth type is 'basic'.",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "hint": "Enter your password. This only applies when Auth type is 'basic'.",
            "type": "string"
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "optional": false,
            "hint": "Enter your client ID. This only applies when Auth type is 'oauth'.",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "optional": false,
            "hint": "Enter your client secret. This only applies when Auth type is 'oauth'.",
            "type": "string"
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "hint": "This only applies when Auth type is 'oauth'.",
            "type": "object",
            "properties": [
                {
                    "label": "Classic scopes",
                    "name": "scopes",
                    "optional": true,
                    "hint": "Select classic scopes (https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) to request for this connection. Specify only the scopes that the client is authorized to use. Selected scopes override the default scopes. Defaults to 'read:confluence-groups', 'read:confluence-content.summary', 'write:confluence-content', 'search:confluence' if left blank. This only applies when Confluence root URI is not configured. Separate multiple values with spaces.",
                    "type": "string",
                    "options": [
                        [
                            "Write Confluence content",
                            "write:confluence-content"
                        ],
                        [
                            "Read Confluence space summary",
                            "read:confluence-space.summary"
                        ],
                        [
                            "Manage Confluence space details",
                            "write:confluence-space"
                        ],
                        [
                            "Upload Confluence attachments",
                            "write:confluence-file"
                        ],
                        [
                            "Read Confluence content properties",
                            "read:confluence-props"
                        ],
                        [
                            "Write Confluence content properties",
                            "write:confluence-props"
                        ],
                        [
                            "Manage Confluence global settings",
                            "manage:confluence-configuration"
                        ],
                        [
                            "Read Confluence detailed content",
                            "read:confluence-content.all"
                        ],
                        [
                            "Read Confluence content summary",
                            "read:confluence-content.summary"
                        ],
                        [
                            "Search Confluence content and space summaries",
                            "search:confluence"
                        ],
                        [
                            "Read content permission in Confluence",
                            "read:confluence-content.permission"
                        ],
                        [
                            "Read user",
                            "read:confluence-user"
                        ],
                        [
                            "Read user groups",
                            "read:confluence-groups"
                        ],
                        [
                            "Create, remove and update user groups",
                            "write:confluence-groups"
                        ],
                        [
                            "Download content attachments",
                            "readonly:content.attachment:confluence"
                        ]
                    ]
                },
                {
                    "label": "Granular scopes",
                    "name": "granular_scopes",
                    "optional": true,
                    "hint": "Select granular scopes (https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/#granular-scopes) to request for this connection. Specify only the scopes that the client is authorized to use. This only applies when Confluence root URI is not configured. Separate multiple values with spaces.",
                    "type": "string",
                    "options": [
                        [
                            "View content",
                            "read:content:confluence"
                        ],
                        [
                            "View content details",
                            "read:content-details:confluence"
                        ],
                        [
                            "Create and update content",
                            "write:content:confluence"
                        ],
                        [
                            "Delete content",
                            "delete:content:confluence"
                        ],
                        [
                            "View space details",
                            "read:space-details:confluence"
                        ],
                        [
                            "View analytics for content",
                            "read:analytics.content:confluence"
                        ],
                        [
                            "View audit records",
                            "read:audit-log:confluence"
                        ],
                        [
                            "Create audit records",
                            "write:audit-log:confluence"
                        ],
                        [
                            "View Confluence settings",
                            "read:configuration:confluence"
                        ],
                        [
                            "Update Confluence settings",
                            "write:configuration:confluence"
                        ],
                        [
                            "View pages",
                            "read:page:confluence"
                        ],
                        [
                            "Create and update pages",
                            "write:page:confluence"
                        ],
                        [
                            "Delete pages",
                            "delete:page:confluence"
                        ],
                        [
                            "View blogposts",
                            "read:blogpost:confluence"
                        ],
                        [
                            "Create and update blogposts",
                            "write:blogpost:confluence"
                        ],
                        [
                            "Delete blogposts",
                            "delete:blogpost:confluence"
                        ],
                        [
                            "View whiteboards",
                            "read:whiteboard:confluence"
                        ],
                        [
                            "Create and update whiteboards",
                            "write:whiteboard:confluence"
                        ],
                        [
                            "Delete whiteboards",
                            "delete:whiteboard:confluence"
                        ],
                        [
                            "View databases",
                            "read:database:confluence"
                        ],
                        [
                            "Create and update databases",
                            "write:database:confluence"
                        ],
                        [
                            "Delete databases",
                            "delete:database:confluence"
                        ],
                        [
                            "View Smart Links in the content tree",
                            "read:embed:confluence"
                        ],
                        [
                            "Create and update Smart Links in the content tree",
                            "write:embed:confluence"
                        ],
                        [
                            "Delete Smart Links in the content tree",
                            "delete:embed:confluence"
                        ],
                        [
                            "View folders",
                            "read:folder:confluence"
                        ],
                        [
                            "Create and update folders",
                            "write:folder:confluence"
                        ],
                        [
                            "Delete folders",
                            "delete:folder:confluence"
                        ],
                        [
                            "View custom content",
                            "read:custom-content:confluence"
                        ],
                        [
                            "Create and update custom content",
                            "write:custom-content:confluence"
                        ],
                        [
                            "Delete custom content",
                            "delete:custom-content:confluence"
                        ],
                        [
                            "View and download content attachments",
                            "read:attachment:confluence"
                        ],
                        [
                            "Create and update content attachments",
                            "write:attachment:confluence"
                        ],
                        [
                            "Delete content attachments",
                            "delete:attachment:confluence"
                        ],
                        [
                            "View comments",
                            "read:comment:confluence"
                        ],
                        [
                            "Create and update comments",
                            "write:comment:confluence"
                        ],
                        [
                            "Delete comments",
                            "delete:comment:confluence"
                        ],
                        [
                            "View content templates",
                            "read:template:confluence"
                        ],
                        [
                            "Create, update, and delete content templates",
                            "write:template:confluence"
                        ],
                        [
                            "View labels",
                            "read:label:confluence"
                        ],
                        [
                            "Add and remove labels",
                            "write:label:confluence"
                        ],
                        [
                            "Check content permissions",
                            "read:content.permission:confluence"
                        ],
                        [
                            "View content properties",
                            "read:content.property:confluence"
                        ],
                        [
                            "Create, update, and delete content properties",
                            "write:content.property:confluence"
                        ],
                        [
                            "View content restrictions",
                            "read:content.restriction:confluence"
                        ],
                        [
                            "Update content restrictions",
                            "write:content.restriction:confluence"
                        ],
                        [
                            "View content summaries",
                            "read:content.metadata:confluence"
                        ],
                        [
                            "Read hierarchical content",
                            "read:hierarchical-content:confluence"
                        ],
                        [
                            "View watchers of content, spaces, or labels",
                            "read:watcher:confluence"
                        ],
                        [
                            "Add and remove watchers of content, spaces, or labels",
                            "write:watcher:confluence"
                        ],
                        [
                            "View groups",
                            "read:group:confluence"
                        ],
                        [
                            "Create, update, and delete groups",
                            "write:group:confluence"
                        ],
                        [
                            "View inline tasks",
                            "read:inlinetask:confluence"
                        ],
                        [
                            "Mark inline task status",
                            "write:inlinetask:confluence"
                        ],
                        [
                            "View entity relationships",
                            "read:relation:confluence"
                        ],
                        [
                            "Create and update entity relationships",
                            "write:relation:confluence"
                        ],
                        [
                            "View spaces",
                            "read:space:confluence"
                        ],
                        [
                            "Create and update spaces",
                            "write:space:confluence"
                        ],
                        [
                            "Delete spaces",
                            "delete:space:confluence"
                        ],
                        [
                            "View space permissions",
                            "read:space.permission:confluence"
                        ],
                        [
                            "Update space permissions",
                            "write:space.permission:confluence"
                        ],
                        [
                            "View space properties",
                            "read:space.property:confluence"
                        ],
                        [
                            "Create, update, and delete space properties",
                            "write:space.property:confluence"
                        ],
                        [
                            "View user properties",
                            "read:user.property:confluence"
                        ],
                        [
                            "Create, update, and delete user properties",
                            "write:user.property:confluence"
                        ],
                        [
                            "View space settings",
                            "read:space.setting:confluence"
                        ],
                        [
                            "Update space settings",
                            "write:space.setting:confluence"
                        ],
                        [
                            "View user details",
                            "read:user:confluence"
                        ],
                        [
                            "View tasks",
                            "read:task:confluence"
                        ],
                        [
                            "Update tasks",
                            "write:task:confluence"
                        ],
                        [
                            "Read email addresses",
                            "read:email-address:confluence"
                        ]
                    ]
                },
                {
                    "label": "Self hosted scopes",
                    "name": "self_hosted_scopes",
                    "optional": true,
                    "hint": "Select scopes (https://confluence.atlassian.com/doc/oauth-2-0-scopes-for-incoming-links-1115674734.html) to request for this connection. Specify only the scopes that the client is authorized to use. Selected scopes override the default scopes. Defaults to 'READ', 'WRITE', 'ADMIN' if left blank. This only applies when Confluence root URI is configured. Separate multiple values with spaces.",
                    "type": "string",
                    "options": [
                        [
                            "View content",
                            "READ"
                        ],
                        [
                            "Create, update, and delete content",
                            "WRITE"
                        ],
                        [
                            "Administer Confluence",
                            "ADMIN"
                        ],
                        [
                            "Administer Confluence system",
                            "SYSTEM_ADMIN"
                        ],
                        [
                            "Read all content",
                            "READ_ALL"
                        ],
                        [
                            "Manage subscriptions",
                            "MANAGE_SUBSCRIPTIONS"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### Confluence (Secondary)

**Provider value:**

```
"provider": "confluence_secondary"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Auth type",
            "name": "auth_type",
            "type": "string",
            "pick_list": [
                [
                    "Basic",
                    "basic"
                ],
                [
                    "API token",
                    "api_token"
                ],
                [
                    "OAuth 2.0",
                    "oauth"
                ]
            ]
        },
        {
            "label": "Confluence subdomain",
            "name": "subdomain",
            "optional": false,
            "hint": "Enter the Confluence subdomain found in your URL. This doesn't apply when using an on-prem agent.",
            "type": "string"
        },
        {
            "label": "Confluence root URI",
            "name": "root_uri",
            "optional": false,
            "hint": "Enter the root URI (protocol, optional port, hostname) of your Confluence host. For example, 'https://confluence.intranet.acme.com:7654'. Most built-in actions only support Confluence Cloud. Use Custom Actions for Data Center. This field only applies when using an on-prem agent.",
            "type": "string"
        },
        {
            "label": "Email",
            "name": "email",
            "hint": "This only applies when Auth type is 'api_token'.",
            "type": "string"
        },
        {
            "label": "API token",
            "name": "apitoken",
            "hint": "Enter your Confluence API token. Refer to the following page to retrieve this value: 'https://id.atlassian.com/manage/api-tokens'. This only applies when Auth type is 'api_token'.",
            "type": "string"
        },
        {
            "label": "Username",
            "name": "username",
            "hint": "Enter your user name (not email). This only applies when Auth type is 'basic'.",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "hint": "Enter your password. This only applies when Auth type is 'basic'.",
            "type": "string"
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "optional": false,
            "hint": "Enter your client ID. This only applies when Auth type is 'oauth'.",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "optional": false,
            "hint": "Enter your client secret. This only applies when Auth type is 'oauth'.",
            "type": "string"
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "hint": "This only applies when Auth type is 'oauth'.",
            "type": "object",
            "properties": [
                {
                    "label": "Classic scopes",
                    "name": "scopes",
                    "optional": true,
                    "hint": "Select classic scopes (https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/) to request for this connection. Specify only the scopes that the client is authorized to use. Selected scopes override the default scopes. Defaults to 'read:confluence-groups', 'read:confluence-content.summary', 'write:confluence-content', 'search:confluence' if left blank. This only applies when Confluence root URI is not configured. Separate multiple values with spaces.",
                    "type": "string",
                    "options": [
                        [
                            "Write Confluence content",
                            "write:confluence-content"
                        ],
                        [
                            "Read Confluence space summary",
                            "read:confluence-space.summary"
                        ],
                        [
                            "Manage Confluence space details",
                            "write:confluence-space"
                        ],
                        [
                            "Upload Confluence attachments",
                            "write:confluence-file"
                        ],
                        [
                            "Read Confluence content properties",
                            "read:confluence-props"
                        ],
                        [
                            "Write Confluence content properties",
                            "write:confluence-props"
                        ],
                        [
                            "Manage Confluence global settings",
                            "manage:confluence-configuration"
                        ],
                        [
                            "Read Confluence detailed content",
                            "read:confluence-content.all"
                        ],
                        [
                            "Read Confluence content summary",
                            "read:confluence-content.summary"
                        ],
                        [
                            "Search Confluence content and space summaries",
                            "search:confluence"
                        ],
                        [
                            "Read content permission in Confluence",
                            "read:confluence-content.permission"
                        ],
                        [
                            "Read user",
                            "read:confluence-user"
                        ],
                        [
                            "Read user groups",
                            "read:confluence-groups"
                        ],
                        [
                            "Create, remove and update user groups",
                            "write:confluence-groups"
                        ],
                        [
                            "Download content attachments",
                            "readonly:content.attachment:confluence"
                        ]
                    ]
                },
                {
                    "label": "Granular scopes",
                    "name": "granular_scopes",
                    "optional": true,
                    "hint": "Select granular scopes (https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/#granular-scopes) to request for this connection. Specify only the scopes that the client is authorized to use. This only applies when Confluence root URI is not configured. Separate multiple values with spaces.",
                    "type": "string",
                    "options": [
                        [
                            "View content",
                            "read:content:confluence"
                        ],
                        [
                            "View content details",
                            "read:content-details:confluence"
                        ],
                        [
                            "Create and update content",
                            "write:content:confluence"
                        ],
                        [
                            "Delete content",
                            "delete:content:confluence"
                        ],
                        [
                            "View space details",
                            "read:space-details:confluence"
                        ],
                        [
                            "View analytics for content",
                            "read:analytics.content:confluence"
                        ],
                        [
                            "View audit records",
                            "read:audit-log:confluence"
                        ],
                        [
                            "Create audit records",
                            "write:audit-log:confluence"
                        ],
                        [
                            "View Confluence settings",
                            "read:configuration:confluence"
                        ],
                        [
                            "Update Confluence settings",
                            "write:configuration:confluence"
                        ],
                        [
                            "View pages",
                            "read:page:confluence"
                        ],
                        [
                            "Create and update pages",
                            "write:page:confluence"
                        ],
                        [
                            "Delete pages",
                            "delete:page:confluence"
                        ],
                        [
                            "View blogposts",
                            "read:blogpost:confluence"
                        ],
                        [
                            "Create and update blogposts",
                            "write:blogpost:confluence"
                        ],
                        [
                            "Delete blogposts",
                            "delete:blogpost:confluence"
                        ],
                        [
                            "View whiteboards",
                            "read:whiteboard:confluence"
                        ],
                        [
                            "Create and update whiteboards",
                            "write:whiteboard:confluence"
                        ],
                        [
                            "Delete whiteboards",
                            "delete:whiteboard:confluence"
                        ],
                        [
                            "View databases",
                            "read:database:confluence"
                        ],
                        [
                            "Create and update databases",
                            "write:database:confluence"
                        ],
                        [
                            "Delete databases",
                            "delete:database:confluence"
                        ],
                        [
                            "View Smart Links in the content tree",
                            "read:embed:confluence"
                        ],
                        [
                            "Create and update Smart Links in the content tree",
                            "write:embed:confluence"
                        ],
                        [
                            "Delete Smart Links in the content tree",
                            "delete:embed:confluence"
                        ],
                        [
                            "View folders",
                            "read:folder:confluence"
                        ],
                        [
                            "Create and update folders",
                            "write:folder:confluence"
                        ],
                        [
                            "Delete folders",
                            "delete:folder:confluence"
                        ],
                        [
                            "View custom content",
                            "read:custom-content:confluence"
                        ],
                        [
                            "Create and update custom content",
                            "write:custom-content:confluence"
                        ],
                        [
                            "Delete custom content",
                            "delete:custom-content:confluence"
                        ],
                        [
                            "View and download content attachments",
                            "read:attachment:confluence"
                        ],
                        [
                            "Create and update content attachments",
                            "write:attachment:confluence"
                        ],
                        [
                            "Delete content attachments",
                            "delete:attachment:confluence"
                        ],
                        [
                            "View comments",
                            "read:comment:confluence"
                        ],
                        [
                            "Create and update comments",
                            "write:comment:confluence"
                        ],
                        [
                            "Delete comments",
                            "delete:comment:confluence"
                        ],
                        [
                            "View content templates",
                            "read:template:confluence"
                        ],
                        [
                            "Create, update, and delete content templates",
                            "write:template:confluence"
                        ],
                        [
                            "View labels",
                            "read:label:confluence"
                        ],
                        [
                            "Add and remove labels",
                            "write:label:confluence"
                        ],
                        [
                            "Check content permissions",
                            "read:content.permission:confluence"
                        ],
                        [
                            "View content properties",
                            "read:content.property:confluence"
                        ],
                        [
                            "Create, update, and delete content properties",
                            "write:content.property:confluence"
                        ],
                        [
                            "View content restrictions",
                            "read:content.restriction:confluence"
                        ],
                        [
                            "Update content restrictions",
                            "write:content.restriction:confluence"
                        ],
                        [
                            "View content summaries",
                            "read:content.metadata:confluence"
                        ],
                        [
                            "Read hierarchical content",
                            "read:hierarchical-content:confluence"
                        ],
                        [
                            "View watchers of content, spaces, or labels",
                            "read:watcher:confluence"
                        ],
                        [
                            "Add and remove watchers of content, spaces, or labels",
                            "write:watcher:confluence"
                        ],
                        [
                            "View groups",
                            "read:group:confluence"
                        ],
                        [
                            "Create, update, and delete groups",
                            "write:group:confluence"
                        ],
                        [
                            "View inline tasks",
                            "read:inlinetask:confluence"
                        ],
                        [
                            "Mark inline task status",
                            "write:inlinetask:confluence"
                        ],
                        [
                            "View entity relationships",
                            "read:relation:confluence"
                        ],
                        [
                            "Create and update entity relationships",
                            "write:relation:confluence"
                        ],
                        [
                            "View spaces",
                            "read:space:confluence"
                        ],
                        [
                            "Create and update spaces",
                            "write:space:confluence"
                        ],
                        [
                            "Delete spaces",
                            "delete:space:confluence"
                        ],
                        [
                            "View space permissions",
                            "read:space.permission:confluence"
                        ],
                        [
                            "Update space permissions",
                            "write:space.permission:confluence"
                        ],
                        [
                            "View space properties",
                            "read:space.property:confluence"
                        ],
                        [
                            "Create, update, and delete space properties",
                            "write:space.property:confluence"
                        ],
                        [
                            "View user properties",
                            "read:user.property:confluence"
                        ],
                        [
                            "Create, update, and delete user properties",
                            "write:user.property:confluence"
                        ],
                        [
                            "View space settings",
                            "read:space.setting:confluence"
                        ],
                        [
                            "Update space settings",
                            "write:space.setting:confluence"
                        ],
                        [
                            "View user details",
                            "read:user:confluence"
                        ],
                        [
                            "View tasks",
                            "read:task:confluence"
                        ],
                        [
                            "Update tasks",
                            "write:task:confluence"
                        ],
                        [
                            "Read email addresses",
                            "read:email-address:confluence"
                        ]
                    ]
                },
                {
                    "label": "Self hosted scopes",
                    "name": "self_hosted_scopes",
                    "optional": true,
                    "hint": "Select scopes (https://confluence.atlassian.com/doc/oauth-2-0-scopes-for-incoming-links-1115674734.html) to request for this connection. Specify only the scopes that the client is authorized to use. Selected scopes override the default scopes. Defaults to 'READ', 'WRITE', 'ADMIN' if left blank. This only applies when Confluence root URI is configured. Separate multiple values with spaces.",
                    "type": "string",
                    "options": [
                        [
                            "View content",
                            "READ"
                        ],
                        [
                            "Create, update, and delete content",
                            "WRITE"
                        ],
                        [
                            "Administer Confluence",
                            "ADMIN"
                        ],
                        [
                            "Administer Confluence system",
                            "SYSTEM_ADMIN"
                        ],
                        [
                            "Read all content",
                            "READ_ALL"
                        ],
                        [
                            "Manage subscriptions",
                            "MANAGE_SUBSCRIPTIONS"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### Confluent Cloud

**Provider value:**

```json
"provider": "confluent_cloud"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Seed brokers",
            "name": "seed_brokers",
            "hint": "Enter a comma separated list of seed brokers in the format 'host:port'.",
            "type": "string"
        },
        {
            "label": "Username",
            "name": "username",
            "hint": "Enter your username for SASL/PLAIN authentication. Refer to the following page for more information: 'https://docs.confluent.io/current/kafka/authentication_sasl/authentication_sasl_plain.html#sasl-plain-overview'.",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "hint": "Enter your password.",
            "type": "string"
        },
        {
            "label": "Stream governance",
            "name": "stream_governance",
            "optional": true,
            "type": "object",
            "properties": [
                {
                    "label": "Stream Governance API URL",
                    "name": "api_url",
                    "optional": false,
                    "hint": "Provide the URL of your Stream Governance API (Schema Registry and Stream Catalog API).",
                    "type": "string"
                },
                {
                    "label": "Stream Governance username",
                    "name": "api_username",
                    "optional": false,
                    "hint": "Provide the username for your schema registry.",
                    "type": "string"
                },
                {
                    "label": "Stream Governance password",
                    "name": "api_password",
                    "optional": false,
                    "hint": "Provide the password for your schema registry.",
                    "type": "string"
                }
            ]
        }
    ]
}
```

* * *

### Cornerstone OnDemand

**Provider value:**

```json
"provider": "cornerstone_ondemand"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Portal",
            "name": "portal",
            "optional": false,
            "hint": "Enter the portal prefix of your Cornerstone OnDemand domain. For example, 'acme' is the portal prefix for 'https://acme.csod.com'.",
            "type": "string"
        },
        {
            "label": "Region",
            "name": "region",
            "optional": false,
            "hint": "Select the region in which your Cornerstone OnDemand application is hosted. Defaults to 'com'.",
            "type": "string",
            "pick_list": [
                [
                    "U.S.",
                    "com"
                ],
                [
                    "Canada",
                    "ca"
                ],
                [
                    "Europe",
                    "eu"
                ],
                [
                    "United Kingdom",
                    "co.uk"
                ],
                [
                    "Japan",
                    "jp"
                ],
                [
                    "Singapore",
                    "sg"
                ],
                [
                    "Australia",
                    "au"
                ]
            ]
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "optional": false,
            "hint": "Enter the client ID for your Cornerstone OnDemand OAuth application.",
            "type": "string"
        },
        {
            "label": "Client Secret",
            "name": "client_secret",
            "optional": false,
            "hint": "Enter the client secret for your Cornerstone OnDemand OAuth application.",
            "type": "string"
        },
        {
            "label": "Scopes",
            "name": "scope",
            "optional": false,
            "hint": "Select the OAuth scopes required for your connection. By default, the 'reportingmetadata:view' and 'obj_metadata:read' scopes are requested. Workato requests all scopes if more than 18 scopes are selected due to CSOD API limitations. Refer to the following documentation for more information: 'https://csod.dev/guides/getting-started/authentication.html#acquire-a-token-and-make-an-api-call'. Separate multiple values with commas.",
            "type": "string",
            "options": [
                [
                    "Read Address core",
                    "obj_address_core:read"
                ],
                [
                    "Read Timezone core",
                    "obj_timezone_core:read"
                ],
                [
                    "Read Timezone localization",
                    "obj_timezone_local_core:read"
                ],
                [
                    "Read Assessment evaluation core",
                    "obj_assessment_evaluation_core:read"
                ],
                [
                    "Read Assessment response core",
                    "obj_assessment_response_core:read"
                ],
                [
                    "Read Assessment result core",
                    "obj_assessment_result_core:read"
                ],
                [
                    "Read Assessment test core",
                    "obj_assessment_test_core:read"
                ],
                [
                    "Read Assessment type core",
                    "obj_assessment_type_core:read"
                ],
                [
                    "Read Application custom field enum localization",
                    "obj_application_cf_enum_local2_core:read"
                ],
                [
                    "Read Availability type",
                    "obj_AvailabilityType:read"
                ],
                [
                    "Read Capability",
                    "obj_Capability:read"
                ],
                [
                    "Read Capability localization",
                    "obj_Capability_local:read"
                ],
                [
                    "Read Capability category",
                    "obj_CapabilityCategory:read"
                ],
                [
                    "Read Capability category localization",
                    "obj_CapabilityCategory_local:read"
                ],
                [
                    "Read Capability category map",
                    "obj_CapabilityCategoryMap:read"
                ],
                [
                    "Read Capability model",
                    "obj_CapabilityModel:read"
                ],
                [
                    "Read Capability model localization",
                    "obj_CapabilityModel_local:read"
                ],
                [
                    "Read Capability model availability",
                    "obj_CapabilityModelAvailability:read"
                ],
                [
                    "Read Capability model capability map",
                    "obj_CapabilityModelCapabilityMap:read"
                ],
                [
                    "Read Capability model target map",
                    "obj_CapabilityModelTargetMap:read"
                ],
                [
                    "Read Capability source",
                    "obj_CapabilitySource:read"
                ],
                [
                    "Read Capability status",
                    "obj_CapabilityStatus:read"
                ],
                [
                    "Read Capability type",
                    "obj_CapabilityType:read"
                ],
                [
                    "Read Category status",
                    "obj_CategoryStatus:read"
                ],
                [
                    "Read Certification category localization",
                    "obj_certification_category_local_core:read"
                ],
                [
                    "Read Certification core",
                    "obj_certification_core:read"
                ],
                [
                    "Read Certification family localization",
                    "obj_certification_family_local_core:read"
                ],
                [
                    "Read Certification localization",
                    "obj_certification_local_core:read"
                ],
                [
                    "Read Check-In",
                    "obj_CheckIn:read"
                ],
                [
                    "Read Check-In comment",
                    "obj_CheckInComment:read"
                ],
                [
                    "Read Check-In follow-up",
                    "obj_CheckInFollowUp:read"
                ],
                [
                    "Read Check-In meeting",
                    "obj_CheckInMeeting:read"
                ],
                [
                    "Read Check-In note",
                    "obj_CheckInNote2:read"
                ],
                [
                    "Read Check-In participant",
                    "obj_CheckInParticipant:read"
                ],
                [
                    "Read Check-In template",
                    "obj_CheckInTemplate:read"
                ],
                [
                    "Read Check-In template localization",
                    "obj_CheckInTemplate_local:read"
                ],
                [
                    "Read Check-In topic",
                    "obj_CheckInTopic:read"
                ],
                [
                    "Read Compensation type localization",
                    "obj_compensation_type_local_core:read"
                ],
                [
                    "Read Course rating core",
                    "obj_course_rating_core:read"
                ],
                [
                    "Read Culture core",
                    "obj_culture_core:read"
                ],
                [
                    "Read Language core",
                    "obj_language_core:read"
                ],
                [
                    "Read Currency core",
                    "obj_currency_core:read"
                ],
                [
                    "Read Curriculum due date type localization",
                    "obj_curriculum_due_date_type_local_core:read"
                ],
                [
                    "Read Curriculum structure core",
                    "obj_curriculum_structure_core:read"
                ],
                [
                    "Read Development plan action step core",
                    "obj_devplan_action_step_core:read"
                ],
                [
                    "Read Development plan activity type core",
                    "obj_devplan_activity_type_core:read"
                ],
                [
                    "Read Development plan activity type localization",
                    "obj_devplan_activity_type_local_core:read"
                ],
                [
                    "Read Development plan category core",
                    "obj_devplan_category_core:read"
                ],
                [
                    "Read Development plan category localization",
                    "obj_devplan_category_local_core:read"
                ],
                [
                    "Read Development plan custom fields",
                    "obj_devplan_cf_core:read"
                ],
                [
                    "Read Development plan custom field enum localization",
                    "obj_devplan_cf_enum_local2_core:read"
                ],
                [
                    "Read Development plan core",
                    "obj_devplan_core:read"
                ],
                [
                    "Read Development plan objective category core",
                    "obj_devplan_objective_category_core:read"
                ],
                [
                    "Read Development plan objective category localization",
                    "obj_devplan_objective_category_local_core:read"
                ],
                [
                    "Read Development plan objective core",
                    "obj_devplan_objective_core:read"
                ],
                [
                    "Read Development plan status core",
                    "obj_devplan_status_core:read"
                ],
                [
                    "Read Development plan status localization",
                    "obj_devplan_status_local_core:read"
                ],
                [
                    "Read Development plan training core",
                    "obj_devplan_training_core:read"
                ],
                [
                    "Read Expert validation",
                    "obj_ExpertValidation:read"
                ],
                [
                    "Read Feedback badge localization",
                    "obj_feedback_badge_local_core:read"
                ],
                [
                    "Read Goal association core",
                    "obj_goal_association_core:read"
                ],
                [
                    "Read Goal category association core",
                    "obj_goal_category_association_core:read"
                ],
                [
                    "Read Goal category core",
                    "obj_goal_category_core:read"
                ],
                [
                    "Read Goal category localization",
                    "obj_goal_category_local_core:read"
                ],
                [
                    "Read Goal core",
                    "obj_goal_core:read"
                ],
                [
                    "Read Goal perspective core",
                    "obj_goal_perspective_core:read"
                ],
                [
                    "Read Goal perspective localization",
                    "obj_goal_perspective_local_core:read"
                ],
                [
                    "Read Goal target core",
                    "obj_goal_target_core:read"
                ],
                [
                    "Read Goal task core",
                    "obj_goal_task_core:read"
                ],
                [
                    "Read Instructor core",
                    "obj_instructor_core:read"
                ],
                [
                    "Read Job applicant core",
                    "obj_job_applicant_core:read"
                ],
                [
                    "Read Job application core",
                    "obj_job_application_core:read"
                ],
                [
                    "Read Job application disposition localization",
                    "obj_job_application_disposition_local_core:read"
                ],
                [
                    "Read Job application status localization",
                    "obj_job_application_status_local_core:read"
                ],
                [
                    "Read Job application submission source core",
                    "obj_job_application_submission_source_core:read"
                ],
                [
                    "Read Job application workflow core",
                    "obj_job_application_workflow_core:read"
                ],
                [
                    "Read Job requisition custom fields",
                    "obj_job_requisition_cf_core:read"
                ],
                [
                    "Read Job requisition core",
                    "obj_job_requisition_core:read"
                ],
                [
                    "Read Job requisition EEO category core",
                    "obj_job_requisition_eeo_category_core:read"
                ],
                [
                    "Read Job requisition employment type localization",
                    "obj_job_requisition_employment_type_local_core:read"
                ],
                [
                    "Read Job requisition target OU core",
                    "obj_job_requisition_target_ou_core:read"
                ],
                [
                    "Read Job requisition template core",
                    "obj_job_requisition_template_core:read"
                ],
                [
                    "Read Job requisition template localization",
                    "obj_job_requisition_template_local_core:read"
                ],
                [
                    "Read Offer letter custom field enum localization",
                    "obj_offer_letter_cf_enum_local2_core:read"
                ],
                [
                    "Read OU custom fields",
                    "obj_ou_cf_core:read"
                ],
                [
                    "Read OU custom field enum localization",
                    "obj_ou_cf_enum_local2_core:read"
                ],
                [
                    "Read OU custom field text localization",
                    "obj_ou_cf_text_local_core:read"
                ],
                [
                    "Read OU core",
                    "obj_ou_core:read"
                ],
                [
                    "Read OU hierarchy core",
                    "obj_ou_hierarchy_core:read"
                ],
                [
                    "Read OU localization",
                    "obj_ou_local_core:read"
                ],
                [
                    "Read OU type core",
                    "obj_ou_type_core:read"
                ],
                [
                    "Read OU type localization",
                    "obj_ou_type_local_core:read"
                ],
                [
                    "Read Performance review custom field enum localization",
                    "obj_performance_review_cf_enum_local2_core:read"
                ],
                [
                    "Read QnA answer bank core",
                    "obj_qna_answer_bank_core:read"
                ],
                [
                    "Read QnA container core",
                    "obj_qna_container_core:read"
                ],
                [
                    "Read QnA correct answer core",
                    "obj_qna_correct_answer_core:read"
                ],
                [
                    "Read QnA item audit core",
                    "obj_qna_item_audit_core:read"
                ],
                [
                    "Read QnA question category core",
                    "obj_qna_question_category_core:read"
                ],
                [
                    "Read QnA question category localization",
                    "obj_qna_question_category_local_core:read"
                ],
                [
                    "Read QnA question core",
                    "obj_qna_question_core:read"
                ],
                [
                    "Read QnA question type localization",
                    "obj_qna_question_type_local_core:read"
                ],
                [
                    "Read QnA section core",
                    "obj_qna_section_core:read"
                ],
                [
                    "Read QnA structure core",
                    "obj_qna_structure_core:read"
                ],
                [
                    "Read QnA target person core",
                    "obj_qna_target_person_core:read"
                ],
                [
                    "Read QnA text localization",
                    "obj_qna_text_local_core:read"
                ],
                [
                    "Read SCORM session",
                    "obj_scorm_session:read"
                ],
                [
                    "Read SCORM subsession",
                    "obj_scorm_subsession:read"
                ],
                [
                    "Read SCORM subsession interaction",
                    "obj_scorm_subsession_interaction:read"
                ],
                [
                    "Read SCORM subsession interaction correct response",
                    "obj_scorm_subsession_interaction_correct_response:read"
                ],
                [
                    "Read SCORM 2004 activity session history",
                    "obj_scorm2004_activity_session_history:read"
                ],
                [
                    "Read SCORM 2004 interaction history",
                    "obj_scorm2004_interaction_history:read"
                ],
                [
                    "Read Skill",
                    "obj_Skill:read"
                ],
                [
                    "Read Skills graph link",
                    "obj_SkillsGraphLink:read"
                ],
                [
                    "Read Skills graph link method",
                    "obj_SkillsGraphLinkMethod:read"
                ],
                [
                    "Read Skills graph link type",
                    "obj_SkillsGraphLinkType:read"
                ],
                [
                    "Read SMP task review localization",
                    "obj_smp_task_review_local_core:read"
                ],
                [
                    "Read Succession custom field enum2 localization",
                    "obj_succession_cf_enum_local2_core:read"
                ],
                [
                    "Read Subject core",
                    "obj_subject_core:read"
                ],
                [
                    "Read Subject equivalent core",
                    "obj_subject_equivalent_core:read"
                ],
                [
                    "Read Subject localization",
                    "obj_subject_local_core:read"
                ],
                [
                    "Read Subject training core",
                    "obj_subject_training_core:read"
                ],
                [
                    "Read Target type",
                    "obj_TargetType:read"
                ],
                [
                    "Read Task localization",
                    "obj_task_local_core:read"
                ],
                [
                    "Read Task review rating localization",
                    "obj_task_review_rating_local_core:read"
                ],
                [
                    "Read Task review step localization",
                    "obj_task_review_step_local_core:read"
                ],
                [
                    "Read Task status localization",
                    "obj_task_status_local_core:read"
                ],
                [
                    "Read Training assignment core",
                    "obj_training_assignment_core:read"
                ],
                [
                    "Read Training assignment detail core",
                    "obj_training_assignment_detail_core:read"
                ],
                [
                    "Read Training assignment LAT core",
                    "obj_training_assignment_lat_core:read"
                ],
                [
                    "Read Training assignment user core",
                    "obj_training_assignment_user_core:read"
                ],
                [
                    "Read Training availability by OU core",
                    "obj_training_availability_by_ou_core:read"
                ],
                [
                    "Read Training availability by user core",
                    "obj_training_availability_by_user_core:read"
                ],
                [
                    "Read Training available culture core",
                    "obj_training_available_culture_core:read"
                ],
                [
                    "Read Training bundle core",
                    "obj_training_bundle_core:read"
                ],
                [
                    "Read Training bundle manifest core",
                    "obj_training_bundle_manifest_core:read"
                ],
                [
                    "Read Training custom fields",
                    "obj_training_cf_core:read"
                ],
                [
                    "Read Training custom field enum localization",
                    "obj_training_cf_enum_local2_core:read"
                ],
                [
                    "Read Training custom field text localization",
                    "obj_training_cf_text_local_core:read"
                ],
                [
                    "Read Training contact core",
                    "obj_training_contact_core:read"
                ],
                [
                    "Read Training core",
                    "obj_training_core:read"
                ],
                [
                    "Read Training equivalency core",
                    "obj_training_equivalency_core:read"
                ],
                [
                    "Read Training exemption reason localization",
                    "obj_training_exemption_reason_local_core:read"
                ],
                [
                    "Read Training forecast custom field enum localization",
                    "obj_training_forecast_cf_enum_local2_core:read"
                ],
                [
                    "Read Training ILT facility core",
                    "obj_training_ilt_facility_core:read"
                ],
                [
                    "Read Training ILT facility type localization",
                    "obj_training_ilt_facility_type_local_core:read"
                ],
                [
                    "Read Training ILT session core",
                    "obj_training_ilt_session_core:read"
                ],
                [
                    "Read Training license core",
                    "obj_training_license_core:read"
                ],
                [
                    "Read Training localization",
                    "obj_training_local_core:read"
                ],
                [
                    "Read Training material type core",
                    "obj_training_material_type_core:read"
                ],
                [
                    "Read Training material type localization",
                    "obj_training_material_type_local_core:read"
                ],
                [
                    "Read Training model core",
                    "obj_training_model_core:read"
                ],
                [
                    "Read Training model localization",
                    "obj_training_model_local_core:read"
                ],
                [
                    "Read Training model training object core",
                    "obj_training_model_training_object_core:read"
                ],
                [
                    "Read Training part attendance core",
                    "obj_training_part_attendance_core:read"
                ],
                [
                    "Read Training part instructor core",
                    "obj_training_part_instructor_core:read"
                ],
                [
                    "Read Training part localization",
                    "obj_training_part_local_core:read"
                ],
                [
                    "Read Training part2 core",
                    "obj_training_part2_core:read"
                ],
                [
                    "Read Training provider core",
                    "obj_training_provider_core:read"
                ],
                [
                    "Read Training provider instructor membership core",
                    "obj_training_provider_instructor_membership_core:read"
                ],
                [
                    "Read Training relationship core",
                    "obj_training_relationship_core:read"
                ],
                [
                    "Read Training relationship type core",
                    "obj_training_relationship_type_core:read"
                ],
                [
                    "Read Training removal reason localization",
                    "obj_training_removal_reason_local_core:read"
                ],
                [
                    "Read Training requirement tag category core",
                    "obj_training_requirement_tag_category_core:read"
                ],
                [
                    "Read Training requirement tag category localization",
                    "obj_training_requirement_tag_category_local_core:read"
                ],
                [
                    "Read Training requirement tag core",
                    "obj_training_requirement_tag_core:read"
                ],
                [
                    "Read Training requirement tag localization",
                    "obj_training_requirement_tag_local_core:read"
                ],
                [
                    "Read Training SCORM core",
                    "obj_training_scorm_core:read"
                ],
                [
                    "Read Training status type localization",
                    "obj_training_status_type_local_core:read"
                ],
                [
                    "Read Training type core",
                    "obj_training_type_core:read"
                ],
                [
                    "Read Training type localization",
                    "obj_training_type_local_core:read"
                ],
                [
                    "Read Training purchase core",
                    "obj_training_purchase_core:read"
                ],
                [
                    "Read Training purchase line item core",
                    "obj_training_purchase_line_item_core:read"
                ],
                [
                    "Read Training purchase payer core",
                    "obj_training_purchase_payer_core:read"
                ],
                [
                    "Read Training purchase payment type core",
                    "obj_training_purchase_payment_type_core:read"
                ],
                [
                    "Read Training purchaser overrides core",
                    "obj_training_purchaser_overrides_core:read"
                ],
                [
                    "Read Transcript action core",
                    "obj_transcript_action_core:read"
                ],
                [
                    "Read Transcript action localization",
                    "obj_transcript_action_local_core:read"
                ],
                [
                    "Read Transcript action reason core",
                    "obj_transcript_action_reason_core:read"
                ],
                [
                    "Read Transcript action reason localization",
                    "obj_transcript_action_reason_local_core:read"
                ],
                [
                    "Read Transcript assignment core",
                    "obj_transcript_assignment_core:read"
                ],
                [
                    "Read Transcript custom fields",
                    "obj_transcript_cf_core:read"
                ],
                [
                    "Read Transcript core",
                    "obj_transcript_core:read"
                ],
                [
                    "Read Transcript delivery method localization",
                    "obj_transcript_delivery_method_local_core:read"
                ],
                [
                    "Read Transcript origin type localization",
                    "obj_transcript_origin_type_local_core:read"
                ],
                [
                    "Read Transcript source assignment core",
                    "obj_transcript_src_assignment_core:read"
                ],
                [
                    "Read Transcript status group core",
                    "obj_transcript_status_group_core:read"
                ],
                [
                    "Read Transcript status group membership core",
                    "obj_transcript_status_group_membership_core:read"
                ],
                [
                    "Read Transcript status localization",
                    "obj_transcript_status_local_core:read"
                ],
                [
                    "Read User category localization",
                    "obj_user_category_local_core:read"
                ],
                [
                    "Read User custom field enum localization",
                    "obj_user_cf_enum_local2_core:read"
                ],
                [
                    "Read User dynamic relation core",
                    "obj_user_dynamic_relation_core:read"
                ],
                [
                    "Read User employment status localization",
                    "obj_user_employment_status_local_core:read"
                ],
                [
                    "Read User leave reason localization",
                    "obj_user_leave_reason_local_core:read"
                ],
                [
                    "Read User login core",
                    "obj_user_login_core:read"
                ],
                [
                    "Read User OU core",
                    "obj_user_ou_core:read"
                ],
                [
                    "Read User OU multi core",
                    "obj_user_ou_multi_core:read"
                ],
                [
                    "Read User OU pivoted core",
                    "obj_user_ou_pivoted_core:read"
                ],
                [
                    "Read User OU status localization",
                    "obj_user_ou_status_local_core:read"
                ],
                [
                    "Read User rehire eligibility localization",
                    "obj_user_rehire_eligibility_local_core:read"
                ],
                [
                    "Read User status core",
                    "obj_user_status_core:read"
                ],
                [
                    "Read User status localization",
                    "obj_user_status_local_core:read"
                ],
                [
                    "Read User sub category core",
                    "obj_user_sub_category_core:read"
                ],
                [
                    "Read User sub category localization",
                    "obj_user_sub_category_local_core:read"
                ],
                [
                    "Read User termination reason category core",
                    "obj_user_termination_reason_category_core:read"
                ],
                [
                    "Read User termination reason category localization",
                    "obj_user_termination_reason_category_local_core:read"
                ],
                [
                    "Read User termination reason core",
                    "obj_user_termination_reason_core:read"
                ],
                [
                    "Read User termination reason localization",
                    "obj_user_termination_reason_local_core:read"
                ],
                [
                    "Read User type localization",
                    "obj_user_type_local_core:read"
                ],
                [
                    "Read User capability status",
                    "obj_UserCapabilityStatus:read"
                ],
                [
                    "Read User rating visibility local",
                    "obj_UserRatingVisibility_local:read"
                ],
                [
                    "Read User custom fields",
                    "obj_users_cf_core:read"
                ],
                [
                    "Read User core",
                    "obj_users_core:read"
                ],
                [
                    "Read User skill map",
                    "obj_UserSkillMap:read"
                ],
                [
                    "Read User skills",
                    "obj_UserSkills:read"
                ],
                [
                    "Read Training unit key code",
                    "vw_rpt_training_unit_key_code:read"
                ],
                [
                    "Read Training available language",
                    "vw_rpt_training_available_language:read"
                ],
                [
                    "Read Training ILT Session Instructor",
                    "vw_rpt_training_ilt_session_instructor:read"
                ],
                [
                    "Read Transaction custom field",
                    "vw_rpt_transaction_cf:read"
                ],
                [
                    "Read Transaction billing account",
                    "vw_rpt_transaction_billing_account:read"
                ],
                [
                    "Read Transaction credit card type",
                    "vw_rpt_transaction_credit_card_type:read"
                ],
                [
                    "Read Transaction custom field option local",
                    "vw_rpt_transaction_custom_field_option_local:read"
                ],
                [
                    "Read Transcript part attendance",
                    "vw_rpt_transcript_part_attendance:read"
                ],
                [
                    "Read Training schedule",
                    "vw_rpt_training_schedule:read"
                ]
            ]
        }
    ]
}
```

* * *

### Coupa

**Provider value:**

```json
"provider": "coupa"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": false,
            "hint": "Select the authentication type. Defaults to 'api_key'.",
            "type": "string",
            "pick_list": [
                [
                    "Authorization code grant",
                    "oauth2_auth_code_grant"
                ],
                [
                    "Client credentials",
                    "oauth2_client_credentials_grant"
                ],
                [
                    "API key",
                    "api_key"
                ]
            ]
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "hint": "Enter the client ID of your Open Connect client. This only applies when Authentication type is 'oauth2_auth_code_grant' or 'oauth2_client_credentials_grant'.",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "hint": "Enter the client secret of your Open Connect client. This only applies when Authentication type is 'oauth2_auth_code_grant' or 'oauth2_client_credentials_grant'.",
            "type": "string"
        },
        {
            "label": "Scopes",
            "name": "scopes",
            "optional": false,
            "hint": "Select the scopes in Coupa this connection will have access to. Selecting scopes which your OpenIDConnect account does not have access to results in an error. The 'core.common.read' and 'offline_access' scopes are selected by default when Authentication type is 'oauth2_auth_code_grant'. The 'core.common.read' scope is selected by default when Authentication type is 'oauth2_client_credentials_grant'. Ensure the default scope is included in the scopes added while creating the account in Coupa. Scopes take the form 'service.object.right', for example: 'core.accounting.read' or 'core.accounting.write'. You can find the full list of available scopes on your Coupa instance's 'Scope management' page. Refer to the following documentation for more information: 'https://docs.coupa.com/en/developer-documentation/the-coupa-core-api/oauth-2.0-and-oidc/openid-connect-clients#scopes-0'. This only applies when Authentication type is 'oauth2_auth_code_grant' or 'oauth2_client_credentials_grant'. Separate multiple values with spaces.",
            "type": "string"
        },
        {
            "label": "Host",
            "name": "host",
            "optional": false,
            "hint": "Enter your Coupa URL, for example: 'https://your-instance-name.coupacloud.com'",
            "type": "string"
        },
        {
            "label": "API key",
            "name": "api_key",
            "hint": "Enter an API key. Go to https://your-instance-name.coupacloud.com/api_keys to retrieve this value. This only applies when Authentication type is 'api_key'.",
            "type": "string"
        }
    ]
}
```

* * *

### CSV tools by Workato

**Provider value:**

```json
"provider": "csv_parser"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Custom LLM for Workato Genie

**Provider value:**

```json
"provider": "byollm"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "LLM Provider",
            "name": "provider",
            "optional": false,
            "hint": "Choose the LLM provider to use for this connection.",
            "type": "string",
            "pick_list": [
                [
                    "Anthropic",
                    "anthropic"
                ],
                [
                    "OpenAI Compatible",
                    "openai"
                ],
                [
                    "Azure OpenAI",
                    "azure"
                ],
                [
                    "AWS Bedrock",
                    "bedrock"
                ]
            ]
        },
        {
            "label": "API Key",
            "name": "api_key",
            "optional": false,
            "hint": "Enter an API key for your LLM provider. Refer to one of the following pages to retrieve this value: https://platform.openai.com/api-keys for OpenAI Compatible, https://console.anthropic.com/settings/keys for Anthropic, or https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveServices for Azure OpenAI. This only applies when the LLM provider is 'openai', 'anthropic', or 'azure'.",
            "type": "string"
        },
        {
            "label": "API URL",
            "name": "api_url",
            "optional": true,
            "hint": "Enter an API base URL. Leave this field blank to use the provider's default: https://api.openai.com/v1 for OpenAI Compatible, or https://api.anthropic.com/v1 for Anthropic. Enter a value manually to use a custom OpenAI-compatible API. If an on-prem group is selected, the URL must be reachable from the on-prem agent's network; private DNS names and IP addresses are allowed. This only applies when the LLM Provider is 'openai' or 'anthropic'.",
            "type": "string"
        },
        {
            "label": "Organization ID",
            "name": "organization_id",
            "optional": true,
            "hint": "Optional. Enter an organization ID for OpenAI accounts with multiple organizations. This only applies when the LLM provider is 'openai'.",
            "type": "string"
        },
        {
            "label": "Project ID",
            "name": "project_id",
            "optional": true,
            "hint": "Optional. Enter a project ID for OpenAI accounts with multiple projects. This only applies when the LLM provider is 'openai'.",
            "type": "string"
        },
        {
            "label": "Model",
            "name": "model",
            "optional": false,
            "hint": "Select from the list or enter a custom model name. Available options depend on the selected LLM Provider. This only applies when the LLM Provider is 'openai', 'anthropic', or 'azure'.",
            "type": "string",
            "pick_list": [
                [
                    "Claude Sonnet 4.5",
                    "claude-sonnet-4-5-20250929"
                ],
                [
                    "Claude Haiku 4.5",
                    "claude-haiku-4-5-20251001"
                ],
                [
                    "Claude Opus 4.1",
                    "claude-opus-4-1-20250805"
                ],
                [
                    "Claude Sonnet 3.7 (legacy)",
                    "claude-3-7-sonnet-20250219"
                ],
                [
                    "Claude Sonnet 4 (legacy)",
                    "claude-sonnet-4-20250514"
                ],
                [
                    "GPT-5.1",
                    "gpt-5.1"
                ],
                [
                    "GPT-5",
                    "gpt-5"
                ],
                [
                    "GPT-5 mini",
                    "gpt-5-mini"
                ],
                [
                    "GPT-4.1",
                    "gpt-4.1"
                ],
                [
                    "GPT-4.1 mini",
                    "gpt-4.1-mini"
                ],
                [
                    "GPT-4o",
                    "gpt-4o"
                ],
                [
                    "GPT-4o mini",
                    "gpt-4o-mini"
                ]
            ]
        },
        {
            "label": "Endpoint URL",
            "name": "endpoint_url",
            "optional": false,
            "hint": "Enter an Azure service endpoint URL, for example 'https://your-resource.openai.azure.com'. If an on-prem group is selected, the URL must be reachable from the on-prem agent's network (private DNS names and IP addresses are allowed). This only applies when the LLM provider is 'azure'.",
            "type": "string"
        },
        {
            "label": "API Version",
            "name": "api_version",
            "optional": true,
            "hint": "Enter an Azure API version. Defaults to '2024-08-01-preview'. This only applies when the LLM provider is 'azure'.",
            "type": "string"
        },
        {
            "label": "AWS Access Key ID",
            "name": "access_key_id",
            "optional": false,
            "hint": "Enter your AWS Access Key ID for authentication. This only applies when the LLM provider is 'bedrock'.",
            "type": "string"
        },
        {
            "label": "AWS Secret Access Key",
            "name": "secret_access_key",
            "optional": false,
            "hint": "Enter your AWS Secret Access Key for authentication. This only applies when the LLM provider is 'bedrock'.",
            "type": "string"
        },
        {
            "label": "AWS Session Token",
            "name": "session_token",
            "optional": true,
            "hint": "Enter an AWS session token for temporary credentials. This only applies when the LLM provider is 'bedrock'.",
            "type": "string"
        },
        {
            "label": "AWS Region",
            "name": "region",
            "optional": true,
            "hint": "Enter the region that hosts your Bedrock model. Defaults to 'us-east-1'. This only applies when the LLM provider is 'bedrock'.",
            "type": "string",
            "pick_list": [
                [
                    "US East (N. Virginia)",
                    "us-east-1"
                ],
                [
                    "US West (Oregon)",
                    "us-west-2"
                ],
                [
                    "Asia Pacific (Singapore)",
                    "ap-southeast-1"
                ],
                [
                    "Asia Pacific (Sydney)",
                    "ap-southeast-2"
                ],
                [
                    "Europe (Frankfurt)",
                    "eu-central-1"
                ],
                [
                    "Europe (Ireland)",
                    "eu-west-1"
                ],
                [
                    "Canada (Central)",
                    "ca-central-1"
                ],
                [
                    "Asia Pacific (Tokyo)",
                    "ap-northeast-1"
                ]
            ]
        },
        {
            "label": "Model ID",
            "name": "model_id",
            "optional": false,
            "hint": "Enter a Bedrock model ID or inference profile ARN, for example 'anthropic.claude-3-sonnet-20240229-v1:0'. This only applies when the LLM provider is 'bedrock'.",
            "type": "string"
        }
    ]
}
```

* * *

### cXML

**Provider value:**

```json
"provider": "cxml"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Network user ID",
            "name": "network_user_id",
            "type": "string"
        },
        {
            "label": "Shared secret",
            "name": "shared_secret",
            "type": "string"
        },
        {
            "label": "Buyer network user ID",
            "name": "buyer_network_user_id",
            "type": "string"
        },
        {
            "label": "Purchase order URL",
            "name": "purchase_order_url",
            "hint": "Enter the URL for submitting the purchase order cXML. Defaults to 'http://www.workato.com/ariba/purchase_order/1/78'.",
            "type": "string"
        }
    ]
}
```

* * *

### CyberArk Conjur

**Provider value:**

```json
"provider": "cyberark_conjur"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Server URL",
            "name": "server_url",
            "hint": "Enter the server URL for connections to Conjur Cloud, for example: 'https://{subdomain}.secretsmgr.cyberark.cloud/api/'. Refer to the following documentation for more information: 'https://docs.workato.com/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur.html'",
            "type": "string"
        },
        {
            "label": "Organization account name",
            "name": "account_name",
            "hint": "Enter the organization account name. Enter 'conjur' to connect to Conjur Cloud. Refer to the following guide for more information: 'https://docs.workato.com/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur.html'.",
            "type": "string"
        },
        {
            "label": "Login ID",
            "name": "login",
            "hint": "Enter the login ID for host authentication, prefixed with 'host/'. For example: 'host/workato-app/workato-user-1'",
            "type": "string"
        },
        {
            "label": "API Key",
            "name": "api_key",
            "type": "string"
        }
    ]
}
```

* * *

### Deputy

**Provider value:**

```json
"provider": "deputy"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### docparser

**Provider value:**

```json
"provider": "docparser"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "API Key",
                  "hint": "Go to Account -> API Access to get the API key"
              }
          ]
      }
```

* * *

### DocuSign

**Provider value:**

```json
"provider": "docusign"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Demo",
            "default": "false",
            "optional": true,
            "hint": "Specify whether this is a demo account.",
            "type": "boolean",
            "name": "demo"
        },
        {
            "label": "Account ID",
            "optional": true,
            "hint": "Use this field to specify a single Docusign account when you have multiple. You can find the specific account's ID under **Settings > Apps and Keys > API Account ID**. By default, this connection selects the first DocuSign account tagged to the user.",
            "type": "string",
            "name": "account_id"
        },
        {
            "label": "Connect key",
            "optional": true,
            "hint": "Provide an active connect key that is configured in your DocuSign account to validate your webhook requests. Refer to the docusign 'Add HMAC keys for your app' documentation for more information about setting up connect keys in DocuSign: https://developers.docusign.com/platform/webhooks/connect/setting-up-hmac/ ",
            "type": "string",
            "name": "connect_key"
        }
    ]
}
```

* * *

### DocuSign (Secondary)

**Provider value:**

```json
"provider": "docusign_secondary"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Demo",
            "default": "false",
            "optional": true,
            "hint": "Specify whether this is a demo account.",
            "type": "boolean",
            "name": "demo"
        },
        {
            "label": "Account ID",
            "optional": true,
            "hint": "Use this field to specify a single Docusign account when you have multiple. You can find the specific account's ID under **Settings > Apps and Keys > API Account ID**. By default, this connection selects the first DocuSign account tagged to the user.",
            "type": "string",
            "name": "account_id"
        },
        {
            "label": "Connect key",
            "optional": true,
            "hint": "Provide an active connect key that is configured in your DocuSign account to validate your webhook requests. Refer to the docusign 'Add HMAC keys for your app' documentation for more information about setting up connect keys in DocuSign: https://developers.docusign.com/platform/webhooks/connect/setting-up-hmac/ ",
            "type": "string",
            "name": "connect_key"
        }
    ]
}
```

* * *

### Dropbox

**Provider value:**

```json
"provider": "dropbox"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Egnyte

**Provider value:**

```json
"provider": "egnyte"
```

* * *

### Eloqua

**Provider value:**

```json
"provider": "eloqua"
```

* * *

### Email by Workato

**Provider value:**

```json
"provider": "email"
```

* * *

### eTapestry

**Provider value:**

```json
"provider": "etapestry"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "loginId",
                  "type": "string",
                  "label": "Login ID"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password",
                  "hint": "Password for login"
              }
          ]
      }
```

* * *

### Eventbrite

**Provider value:**

```json
"provider": "event_brite"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Evernote

**Provider value:**

```json
"provider": "evernote"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### everydayhero

**Provider value:**

```json
"provider": "everydayhero"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Expensify

**Provider value:**

```json
"provider": "expensify"
```

View connection parameter JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "partner_user_id",
                  "type": "string",
                  "label": "Partner user ID",
                  "hint": "Generate user ID and secret in Expensify <a href=\"https://www.expensify.com/tools/integrations/\">integration settings</a>"
              },
              {
                  "name": "partner_user_secret",
                  "type": "string",
                  "label": "Partner user secret"
              }
          ]
      }
```

* * *

### Facebook

**Provider value:**

```json
"provider": "facebook"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Fairsail

**Provider value:**

```json
"provider": "fairsail"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### Feedly

**Provider value:**

```json
"provider": "feedly"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### File tools by Workato

**Provider value:**

```json
"provider": "file_connector"
```

* * *

### FinancialForce

**Provider value:**

```json
"provider": "financialforce"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

### Force.com

**Provider value:**

```json
"provider": "forcecom"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### FreshBooks

**Provider value:**

```json
"provider": "fresh_books"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "auth_token",
                  "type": "string",
                  "label": "Authentication Token",
                  "hint": "From your FreshBooks page, My Account - FreshBooks API"
              },
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Subdomain",
                  "hint": "Your account name as it appears in your FreshBooks web address, usually your company name"
              }
          ]
      }
```

* * *

### Freshdesk

**Provider value:**

```json
"provider": "fresh_desk"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "API key",
                  "hint": "You can find the API key under, \"User Profile\" drop-down (top right corner of your helpdesk) > Profile Settings > Your API Key"
              },
              {
                  "name": "help_desk_name",
                  "type": "string",
                  "label": "Helpdesk name",
                  "hint": "yourcompany.freshdesk.com"
              }
          ]
      }
```

* * *

### FTP/FTPS

**Provider value:**

```json
"provider": "ftps"
```

View connection parameters JSON

```json
{
    "oauth": false,
    "personalization": true,
    "input": [
        {
            "label": "On-prem connection profile",
            "hint": "You can find profile names in the ftp section of an on-prem group's config.yml file. Refer to the Workato SFTP documentation for more information: https://docs.workato.com/on-prem/agents/connection/profile.html#on-prem-sftp-profile",
            "type": "string",
            "name": "profile"
        },
        {
            "label": "Server type",
            "hint": "Select whether your FTP server is secure or non-secure. Ensure you have Workato IP addresses whitelisted. Refer to the Workato security documentation for more information: https://docs.workato.com/security.html",
            "default": "ftp-s",
            "type": "string",
            "name": "servertype",
            "pick_list": [
                [
                    "FTP-S",
                    "FTP-S"
                ],
                [
                    "FTP",
                    "FTP"
                ]
            ]
        },
        {
            "label": "Verify cert",
            "optional": true,
            "hint": "Select whether to verify FTPS server certificates",
            "type": "boolean",
            "name": "verify_cert"
        },
        {
            "label": "FTPS connection type",
            "optional": true,
            "type": "string",
            "name": "ftps_conn",
            "pick_list": [
                [
                    "Explicit",
                    "Explicit"
                ],
                [
                    "Implicit",
                    "Implicit"
                ]
            ]
        },
        {
            "label": "Host name",
            "hint": "Enter the server's host name. For example: companyname.sampleftp.com",
            "type": "string",
            "name": "hostname"
        },
        {
            "label": "Port",
            "optional": true,
            "type": "string",
            "name": "port"
        },
        {
            "label": "Username",
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "options": true,
            "type": "string",
            "name": "password"
        },
        {
            "label": "Advanced settings",
            "optional": true,
            "type": "object",
            "name": "advanced_settings",
            "properties": [
                {
                    "label": "Port",
                    "optional": true,
                    "hint": "Specify the port number if your FTPS server uses a port other than the default (`21`).",
                    "type": "string",
                    "name": "port"
                },
                {
                    "label": "Login before send buffer size",
                    "optional": true,
                    "hint": "Select whether to send `PASS` before any other FTP command.",
                    "type": "boolean",
                    "name": "login_before_send_buffer_size"
                }
            ]
        },
        {
            "label": "SSL settings",
            "optional": true,
            "type": "object",
            "name": "ssl",
            "properties": [
                {
                    "label": "FTPS connection type",
                    "optional": true,
                    "type": "string",
                    "name": "implicit",
                    "pick_list": [
                        [
                            "Explicit",
                            "false"
                        ],
                        [
                            "Implicit",
                            "true"
                        ]
                    ]
                },
                {
                    "label": "Server certificate",
                    "hint": "X509 server certification in .pem format",
                    "optional": true,
                    "type": "string",
                    "name": "cert"
                },
                {
                    "label": "Trust all",
                    "optional": true,
                    "hint": "This forces the client to trust any certificate chain. Workato supports self-signed server certificates.",
                    "type": "boolean",
                    "name": "trustAll"
                }
            ]
        }
    ]
}
```

* * *

### FTP/FTPS (Secondary)

**Provider value:**

```json
"provider": "ftps_secondary"
```

View connection parameters JSON

```json
{
    "oauth": false,
    "personalization": true,
    "input": [
        {
            "label": "On-prem connection profile",
            "hint": "You can find profile names in the ftp section of an on-prem group's config.yml file. Refer to the Workato SFTP documentation for more information: https://docs.workato.com/on-prem/agents/connection/profile.html#on-prem-sftp-profile",
            "type": "string",
            "name": "profile"
        },
        {
            "label": "Server type",
            "hint": "Select whether your FTP server is secure or non-secure. Ensure you have Workato IP addresses whitelisted. Refer to the Workato security documentation for more information: https://docs.workato.com/security.html",
            "default": "ftp-s",
            "type": "string",
            "name": "servertype",
            "pick_list": [
                [
                    "FTP-S",
                    "FTP-S"
                ],
                [
                    "FTP",
                    "FTP"
                ]
            ]
        },
        {
            "label": "Verify cert",
            "optional": true,
            "hint": "Select whether to verify FTPS server certificates",
            "type": "boolean",
            "name": "verify_cert"
        },
        {
            "label": "FTPS connection type",
            "optional": true,
            "type": "string",
            "name": "ftps_conn",
            "pick_list": [
                [
                    "Explicit",
                    "Explicit"
                ],
                [
                    "Implicit",
                    "Implicit"
                ]
            ]
        },
        {
            "label": "Host name",
            "hint": "Enter the server's host name. For example: companyname.sampleftp.com",
            "type": "string",
            "name": "hostname"
        },
        {
            "label": "Port",
            "optional": true,
            "type": "string",
            "name": "port"
        },
        {
            "label": "Username",
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "options": true,
            "type": "string",
            "name": "password"
        },
        {
            "label": "Advanced settings",
            "optional": true,
            "type": "object",
            "name": "advanced_settings",
            "properties": [
                {
                    "label": "Port",
                    "optional": true,
                    "hint": "Specify the port number if your FTPS server uses a port other than the default (`21`).",
                    "type": "string",
                    "name": "port"
                },
                {
                    "label": "Login before send buffer size",
                    "optional": true,
                    "hint": "Select whether to send `PASS` before any other FTP command.",
                    "type": "boolean",
                    "name": "login_before_send_buffer_size"
                }
            ]
        },
        {
            "label": "SSL settings",
            "optional": true,
            "type": "object",
            "name": "ssl",
            "properties": [
                {
                    "label": "FTPS connection type",
                    "optional": true,
                    "type": "string",
                    "name": "implicit",
                    "pick_list": [
                        [
                            "Explicit",
                            "false"
                        ],
                        [
                            "Implicit",
                            "true"
                        ]
                    ]
                },
                {
                    "label": "Server certificate",
                    "hint": "X509 server certification in .pem format",
                    "optional": true,
                    "type": "string",
                    "name": "cert"
                },
                {
                    "label": "Trust all",
                    "optional": true,
                    "hint": "This forces the client to trust any certificate chain. Workato supports self-signed server certificates.",
                    "type": "boolean",
                    "name": "trustAll"
                }
            ]
        }
    ]
}
```

* * *

### FullContact

**Provider value:**

```json
"provider": "fullcontact"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "apiKey",
                  "type": "string",
                  "label": "API key",
                  "hint": "<a href=\"https://portal.fullcontact.com/admin\" target=\"_blank\" rel=\"noopener\">How do I find my Fullcontact API key?</a>"
              }
          ]
      }
```

* * *

### Funraise

**Provider value:**

```json
"provider": "funraise"
```

* * *

### GitHub

**Provider value:**

```json
"provider": "github"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Gmail

**Provider value:**

```json
"provider": "gmail"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "read_email_permission",
                  "type": "boolean",
                  "optional": true,
                  "label": "Read email permission",
                  "hint": "Based on Google's updated security policies, Gmail triggers or download attachment\nactions can only be used by paid Google Workspace account. To use them, enable this setting\nand request your Google Workspace admin to whitelist the Workato Gmail Connector app and\ngrant it read email permission before linking your GMail account here.\n<a href=\"https://docs.workato.com/connectors/gmail.html\" target=\"_blank\">Learn more</a>\n"
              }
          ]
      }
```

* * *

### Gong.io

**Provider value:**

```json
"provider": "gong"
```

* * *

### Google BigQuery

**Provider value:**

```json
"provider": "google_big_query"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "oauth_token_pair": {
      "label": "OAuth Token Pair",
      "optional": true,
      "type": "object",
      "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
      "properties": [
        {
          "label": "Access Token",
          "name": "access_token",
          "type": "string",
          "optional": false
        },
        {
          "label": "Refresh Token",
          "name": "refresh_token",
          "type": "string",
          "optional": false
        }
      ]
    },
      "input": [
        {
          "label": "Authentication type",
          "default": "oauth",
          "hint": "Refer to the BigQuery documentation for more information about configuring different authentication types: https://docs.workato.com/connectors/bigquery.html#how-to-connect-to-bigquery-on-workato",
          "type": "string",
          "name": "authentication_type",
          "pick_list": [
            [
              "OAuth 2.0",
              "oauth"
            ],
            [
            "Service account",
            "service_auth"
            ]
          ],
          },
          {
          "label": "GCP Project service account email",
          "hint": "The email address of the service account. This field is only available **Authentication type** is set to **Service account**. Refer to the Google documentation for more information about Google Service Accounts: https://developers.google.com/identity/protocols/oauth2/service-account/.",
          "type": "string",
          "name": "service_email"
        },
        {
          "label": "Private key",
          "hint": "Copy and paste the private key that came from the downloaded JSON. This field is only available **Authentication type** is set to **Service account**. Refer to the Google documentation for more information about Google Service Accounts: https://developers.google.com/identity/protocols/oauth2/service-account/.",
          "type": "string",
          "name": "private_key"
        },
        {
          "label": "Advanced settings",
          "optional": true,
          "type": "object",
          "name": "advanced_settings",
          "properties": [
            {
              "label": "Requested permissions (Service auth scopes)",
              "optional": true,
              "hint": "Select permissions to request permissions for this connection. This field is only available **Authentication type** is set to **Service account**. Refer to the Google documentation for more information about Google Service Accounts: https://developers.google.com/identity/protocols/oauth2/service-account/. Defaults to `https://www.googleapis.com/auth/bigquery` and `https://www.googleapis.com/auth/bigquery.insertdata` if left blank. Selecting permissions from the picklist overwrites the default permission. Refer to the Google scopes documentation for more information: https://developers.google.com/identity/protocols/oauth2/scopes#bigquery",
              "type": "string",
              "name": "scope",
              "options": [
                [
                  "View and manage your data in Google BigQuery",
                  "https://www.googleapis.com/auth/bigquery"
                ],
                [
                  "Insert data into Google BigQuery",
                  "https://www.googleapis.com/auth/bigquery.insertdata"
                ],
                [
                  "View and manage your data across Google Cloud Platform services",
                  "https://www.googleapis.com/auth/cloud-platform"
                ],
                [
                  "View your data across Google Cloud Platform services",
                  "https://www.googleapis.com/auth/cloud-platform.read-only"
                ],
                [
                  "Manage your data and permissions in Google Cloud Storage",
                  "https://www.googleapis.com/auth/devstorage.full_control"
                ],
                [
                  "View your data in Google Cloud Storage",
                  "https://www.googleapis.com/auth/devstorage.read_only"
                ],
                [
                  "Manage your data in Google Cloud Storage",
                  "https://www.googleapis.com/auth/devstorage.read_write"
                ]
              ]
            }
          ]
        }
      ]
    }
```

* * *

### Google Calendar

**Provider value:**

```json
"provider": "google_calendar"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google Contacts

**Provider value:**

```json
"provider": "google_contacts"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google Dialogflow

**Provider value:**

```json
"provider": "api_ai_nlu"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "Service account JSON",
            "name": "service_account_data",
            "hint": "JSON private key downloaded from the service account tied to your Dialogflow agent. Refer to the Dialogflow connector documentation for more information: https://docs.workato.com/en/connectors/dialogflow#google-dialogflow",
            "type": "string"
        }
    ]
}
```

* * *

### Google Drive

**Provider value:**

```json
"provider": "google_drive"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google People

**Provider value:**

```json
"provider": "google_people"
```

* * *

### Google Sheets

**Provider value:**

```json
"provider": "google_sheets"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google Speech to Text

**Provider value:**

```json
"provider": "google_speech_to_text"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google Text to Speech

**Provider value:**

```json
"provider": "google_text_to_speech"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google Translate

**Provider value:**

```json
"provider": "google_translate"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google Vision

**Provider value:**

```json
"provider": "google_vision"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Google Workspace

**Provider value:**

```json
"provider": "google_workspace"
```

* * *

### Goombal

**Provider value:**

```json
"provider": "goombal"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "Email",
                  "type": "string",
                  "label": "Email"
              },
              {
                  "name": "Password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "instance",
                  "type": "string",
                  "optional": true,
                  "label": "Instance",
                  "hint": "Leave empty to default to <b>app</b>"
              }
          ]
      }
```

* * *

### GotoWebinar

**Provider value:**

```json
"provider": "goto_webinar"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Greenhouse

**Provider value:**

```json
"provider": "greenhouse"
```

* * *

### HipChat

**Provider value:**

```json
"provider": "hipchat"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "subdomain",
                  "type": "string",
                  "optional": false,
                  "label": "Subdomain",
                  "hint": "If your HipChat url is https://abc.hipchat.com, then subdomain is 'abc'"
              },
              {
                  "name": "auth_token",
                  "type": "string",
                  "optional": false,
                  "label": "Access token",
                  "hint": "Go to yourdomain.hipchat.com/account/api and create new token. Select \"View Group\" or \"View Room\" as one of the scopes"
              }
          ]
      }
```

* * *

### HTTP (OAuth2)

**Provider value:**

```json
"provider": "rest_oauth"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "oauth2_auth_url",
                  "type": "string",
                  "label": "OAuth2 auth URL",
                  "hint": "Use <b>https://www.workato.com/oauth/callback</b> as callback url. <a href='https://docs.workato.com/developing-connectors/http/connection-setup.html#authentication-type-oauth2-authorization-code-grant'\n                                    target='_blank'>Learn how to authenticate</a>"
              },
              {
                  "name": "oauth2_token_url",
                  "type": "string",
                  "label": "OAuth2 token URL"
              },
              {
                  "name": "oauth2_client_id",
                  "type": "string",
                  "label": "OAuth2 client ID"
              },
              {
                  "name": "oauth2_client_secret",
                  "type": "string",
                  "label": "OAuth2 client secret"
              }
          ]
      }
```

* * *

### HTTP

**Provider value:**

```json
"provider": "rest"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "hint": "Select an authentication method. Refer to the Workato HTTP documentation for more information: https://docs.workato.com/developing-connectors/http/connection-setup.html",
            "type": "string",
            "name": "auth_type",
            "pick_list": [
                [
                    "None",
                    "no_auth"
                ],
                [
                    "Basic",
                    "basic"
                ],
                [
                    "Header auth",
                    "headers"
                ],
                [
                    "Query params",
                    "query"
                ],
                [
                    "On-prem NTLM",
                    "ntlm"
                ],
                [
                    "OAuth 2 (authorization code grant)",
                    "oauth2_auth_code_grant"
                ],
                [
                    "OAuth 2 (client credentials grant)",
                    "oauth2_client_credentials_grant"
                ],
                [
                    "AWS access key auth",
                    "aws_key_secret"
                ],
                [
                    "AWS IAM role auth",
                    "aws_role_based"
                ],
                [
                    "Azure OAuth 2 (authorization code grant)",
                    "azure_oauth2_auth_code_grant"
                ],
                [
                    "Azure OAuth 2 (client credentials grant)",
                    "azure_oauth2_client_credentials_grant"
                ],
                [
                    "Custom",
                    "custom"
                ]
            ]
        },
        {
            "label": "AWS name",
            "optional": false,
            "hint": "Select an AWS service.",
            "type": "string",
            "name": "aws_service",
            "pick_list": [
                [
                    "Amazon S3",
                    "s3"
                ],
                [
                    "Amazon Lambda",
                    "lambda"
                ],
                [
                    "Amazon SNS",
                    "sns"
                ],
                [
                    "Amazon Redshift",
                    "redshift"
                ],
                [
                    "Amazon SES",
                    "email"
                ],
                [
                    "Amazon SQS",
                    "sqs"
                ],
                [
                    "Amazon Cloud Watch",
                    "monitoring"
                ],
                [
                    "Amazon Lex (Models)",
                    "models.lex"
                ],
                [
                    "Amazon Lex (Run-time)",
                    "runtime.lex"
                ],
                [
                    "Amazon Glacier",
                    "glacier"
                ],
                [
                    "Amazon Cloud front",
                    "cloudfront"
                ],
                [
                    "Amazon Kinesis Data Analytics",
                    "kinesisanalytics"
                ],
                [
                    "Amazon Kinesis Data Firehose",
                    "firehose"
                ],
                [
                    "Amazon Kinesis Data Streams",
                    "kinesis"
                ],
                [
                    "Amazon Kinesis Video Streams ",
                    "kinesisvideo"
                ],
                [
                    "Dynamo DB",
                    "dynamodb"
                ]
            ]
        },
        {
            "label": "Region",
            "optional": false,
            "hint": "You can find your region in your account URL. For example, if your account URL is 'https://eu-west-1.console.s3.amazon.com', use 'eu-west-1' as the region.",
            "type": "string",
            "name": "aws_region"
        },
        {
            "label": "IAM role ARN",
            "optional": false,
            "type": "string",
            "name": "aws_assume_role",
            "help": {
                "title": "Using IAM Role authorization",
                "text": "Provide your IAM role ARN in the IAM role ARN field. Refer to the 'How to retrieve IAM role ARN' documentation for more information: https://docs.workato.com/en/developing-connectors/http/connection-setup.html#authentication-type-aws-iam-role-auth"
            }
        },
        {
            "label": "AWS access key ID",
            "optional": false,
            "hint": "Provide your AWS access key ID. Go to your AWS account and click **My Security Credentials > Users** to find the access key ID.",
            "type": "string",
            "name": "aws_api_key"
        },
        {
            "label": "Secret access key",
            "optional": false,
            "hint": "Provide your secret access key. Go to your AWS account and click **My Security Credentials > Users** to find your secret access key.",
            "type": "string",
            "name": "aws_secret_key"
        },
        {
            "label": "Azure Tenant ID",
            "optional": false,
            "hint": "Provide your tenant ID in the Azure Tenant ID field. If you have an Azure subscription, enter your Tenant ID. Otherwise, use common.",
            "type": "string",
            "name": "azure_tenant_id"
        },
        {
            "label": "On-prem NTLM profile",
            "hint": "Enter the NTLM Profile name given in the on-prem agent's config.yml file.",
            "type": "string",
            "name": "profile"
        },
        {
            "label": "Basic auth user",
            "optional": true,
            "type": "string",
            "name": "basic_user"
        },
        {
            "label": "Basic auth password",
            "optional": true,
            "type": "string",
            "name": "basic_password"
        },
        {
            "label": "Username",
            "optional": true,
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "optional": true,
            "type": "string",
            "name": "password"
        },
        {
            "label": "Header authorization",
            "optional": true,
            "hint": "Add custom auth headers",
            "type": "array",
            "name": "header_pair",
            "properties": [
                {
                    "label": "Key",
                    "type": "string",
                    "name": "param"
                },
                {
                    "label": "Value",
                    "type": "string",
                    "name": "value"
                }
            ]
        },
        {
            "label": "Endpoint has case-sensitive headers?",
            "default": "false",
            "optional": true,
            "hint": "Set to 'No' to convert the header names to sentence case. For example: `x-api-key` to `X-api-key`. Set this to 'Yes' if your endpoint headers are case-sensitive. Defaults to 'No'. This field has no effect when the **Wait for response** field is set to 'Yes' or when the connection uses an on-prem agent.",
            "type": "boolean",
            "name": "case_sensitive_headers"
        },
        {
            "label": "URL parameters",
            "optional": true,
            "type": "array",
            "name": "url_param",
            "properties": [
                {
                    "label": "Key",
                    "type": "string",
                    "name": "param"
                },
                {
                    "label": "Value",
                    "type": "string",
                    "name": "value"
                }
            ]
        },
        {
            "label": "OAuth2 authorization URL",
            "type": "string",
            "name": "oauth2_auth_url",
            "hint": "Refer to the Workato HTTP OAuth documentation to retrieve this value: https://docs.workato.com/developing-connectors/http.html#set-up-your-oauth-2-0-connection'"
        },
        {
            "label": "OAuth2 token URL",
            "type": "string",
            "name": "oauth2_token_url"
        },
        {
            "label": "OAuth2 client ID",
            "type": "string",
            "name": "oauth2_client_id"
        },
        {
            "label": "OAuth2 client secret",
            "type": "string",
            "name": "oauth2_client_secret"
        },
        {
            "label": "Azure endpoint version",
            "optional": true,
            "default": "2.0",
            "hint": "Select the version of the Azure endpoints to use. Default is 2.0",
            "type": "string",
            "name": "azure_endpoint_version",
            "pick_list": [
                [
                    "1.0",
                    "1.0"
                ],
                [
                    "2.0",
                    "2.0"
                ]
            ]
        },
        {
            "label": "How does the API require credentials to be sent to request a token?",
            "optional": true,
            "hint": "Select whether to send the client ID and secret in the token request body or as a base64 encoded string in the header.",
            "type": "string",
            "name": "param_type",
            "pick_list": [
                [
                    "Header",
                    "basic"
                ],
                [
                    "Body",
                    "payload"
                ]
            ]
        },
        {
            "label": "Base URL",
            "hint": "Set the Base URL for all requests. Recipes cannot override this value.",
            "optional": true,
            "type": "string",
            "name": "base_url"
        },
        {
            "label": "Use custom TLS/SSL certificate settings",
            "default": "false",
            "optional": true,
            "hint": "Use PEM format if you use custom certificate/key settings.",
            "type": "boolean",
            "name": "ssl_params"
        },
        {
            "label": "TLS server custom CA certificate",
            "optional": true,
            "type": "string",
            "name": "ssl_ca_cert",
            "help": {
                "title": "For servers using self-signed or custom root CAs",
                "text": "Enter your API server's self-signed certificate or a certificate signed by a non-standard root certificate authority. Separate certificates by an empty line if more than one intermediate is needed to complete the chain."
            }
        },
        {
            "label": "TLS client certificate",
            "optional": true,
            "type": "string",
            "name": "ssl_client_cert"
        },
        {
            "label": "TLS client key",
            "optional": true,
            "type": "string",
            "name": "ssl_client_key"
        },
        {
            "label": "TLS client intermediate certificates",
            "type": "string",
            "name": "ssl_client_intermediate_chain",
            "optional": true,
            "help": {
                "title": "Client intermediate certificate chain",
                "text": "Enter certificates if your client certificate relies on one or more intermediate certificates to link it to a root certificate authority trusted by your API server. Separate certificates by an empty line if more than one intermediate is needed to complete the chain."
            }
        },
        {
            "label": "Advanced settings",
            "optional": true,
            "type": "object",
            "name": "advanced_settings",
            "properties": [
                {
                    "label": "OAuth2 scopes",
                    "optional": true,
                    "hint": "Scope for access request. Separate each value with a space.",
                    "type": "string",
                    "name": "oauth2_scope"
                },
                {
                    "label": "Azure resource URI",
                    "hint": "Enter the resource URI for the Azure service you're requesting access to. Only one resource can be requested per connection. Go to **Azure Portal > App registrations > Your registration app > API permissions > Manage**. Click the permission name to retrieve the resource URI. Refer to the Microsoft Azure documentation for more information: https://learn.microsoft.com/en-us/rest/api/azure",
                    "type": "string",
                    "name": "azure_resource_uri"
                },
                {
                    "label": "Restrict to bucket",
                    "optional": true,
                    "hint": "Use this field to restrict the connection to a specific bucket. This is required when a user has limited s3:ListBucket access. Learn more: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
                    "type": "string",
                    "name": "aws_restrict_to_bucket"
                },
                {
                    "label": "Restrict to path",
                    "optional": true,
                    "hint": "Use this field to restrict the connection to a specific bucket and object or path. This is required when a user has limited s3:ListBucket access. Learn more: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
                    "type": "string",
                    "name": "aws_restrict_to_path"
                },
                {
                    "label": "Token settings",
                    "optional": true,
                    "hint": "Default is Access Token",
                    "type": "string",
                    "name": "token_settings",
                    "options": [
                        [
                            "Use Access Token",
                            "access_token"
                        ],
                        [
                            "Use ID Token",
                            "id_token"
                        ]
                    ]
                }
            ]
        },
        {
            "label": "NTLM authentication",
            "hint": "Enter the NTLM authentication domain and workstation.",
            "type": "string",
            "name": "auth"
        },
        {
            "label": "Username",
            "hint": "Enter the NTLM authentication username.",
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "hint": "Enter the NTLM authentication password.",
            "type": "string",
            "name": "password"
        },
        {
            "label": "Base URL",
            "hint": "Enter the base URL for NTLM resources.",
            "type": "string",
            "name": "base_url"
        },
        {
            "label": "Optional properties",
            "optional": true,
            "type": "object",
            "name": "optional_properties",
            "properties": [
                {
                    "label": "Connections per route",
                    "optional": true,
                    "hint": "Sets the number of connections per route/host.",
                    "type": "integer",
                    "name": "cm_default_max_per_route"
                },
                {
                    "label": "Maximum connections",
                    "hint": "Sets the maximum number of connections.",
                    "optional": true,
                    "type": "integer",
                    "name": "cm_max_total"
                },
                {
                    "label": "Timeout",
                    "optional": true,
                    "hint": "The timeout in milliseconds used when requesting a connection.",
                    "type": "integer",
                    "name": "http_connect_timeout"
                },
                {
                    "label": "Connection request timeout",
                    "optional": true,
                    "hint": "The timeout in milliseconds until a connection is established.",
                    "type": "integer",
                    "name": "http_connection_request_timeout"
                },
                {
                    "label": "Socket timeout",
                    "optional": true,
                    "hint": "The socket timeout in milliseconds, which is the timeout for waiting for data. This is the maximum period of inactivity between two consecutive data packets.",
                    "type": "integer",
                    "name": "http_socket_timeout"
                },
                {
                    "label": "Verify host",
                    "optional": true,
                    "default": "true",
                    "hint": "Specifies whether to enable verification of the host name for SSL/TLS connections.",
                    "type": "boolean",
                    "name": "verifyHost"
                },
                {
                    "label": "Trust all",
                    "optional": true,
                    "default": "false",
                    "hint": "Specifies whether trust all certificates for SSL/TLS connections.",
                    "type": "boolean",
                    "name": "trustAll"
                }
            ]
        }
    ]
}
```

* * *

### HTTP (Secondary)

**Provider value:**

```json
"provider": "rest_secondary"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Authentication type",
            "hint": "Select an authentication method. Refer to the Workato HTTP documentation for more information: https://docs.workato.com/developing-connectors/http/connection-setup.html",
            "type": "string",
            "name": "auth_type",
            "pick_list": [
                [
                    "None",
                    "no_auth"
                ],
                [
                    "Basic",
                    "basic"
                ],
                [
                    "Header auth",
                    "headers"
                ],
                [
                    "Query params",
                    "query"
                ],
                [
                    "On-prem NTLM",
                    "ntlm"
                ],
                [
                    "OAuth 2 (authorization code grant)",
                    "oauth2_auth_code_grant"
                ],
                [
                    "OAuth 2 (client credentials grant)",
                    "oauth2_client_credentials_grant"
                ],
                [
                    "AWS access key auth",
                    "aws_key_secret"
                ],
                [
                    "AWS IAM role auth",
                    "aws_role_based"
                ],
                [
                    "Azure OAuth 2 (authorization code grant)",
                    "azure_oauth2_auth_code_grant"
                ],
                [
                    "Azure OAuth 2 (client credentials grant)",
                    "azure_oauth2_client_credentials_grant"
                ],
                [
                    "Custom",
                    "custom"
                ]
            ]
        },
        {
            "label": "AWS name",
            "optional": false,
            "hint": "Select an AWS service.",
            "type": "string",
            "name": "aws_service",
            "pick_list": [
                [
                    "Amazon S3",
                    "s3"
                ],
                [
                    "Amazon Lambda",
                    "lambda"
                ],
                [
                    "Amazon SNS",
                    "sns"
                ],
                [
                    "Amazon Redshift",
                    "redshift"
                ],
                [
                    "Amazon SES",
                    "email"
                ],
                [
                    "Amazon SQS",
                    "sqs"
                ],
                [
                    "Amazon Cloud Watch",
                    "monitoring"
                ],
                [
                    "Amazon Lex (Models)",
                    "models.lex"
                ],
                [
                    "Amazon Lex (Run-time)",
                    "runtime.lex"
                ],
                [
                    "Amazon Glacier",
                    "glacier"
                ],
                [
                    "Amazon Cloud front",
                    "cloudfront"
                ],
                [
                    "Amazon Kinesis Data Analytics",
                    "kinesisanalytics"
                ],
                [
                    "Amazon Kinesis Data Firehose",
                    "firehose"
                ],
                [
                    "Amazon Kinesis Data Streams",
                    "kinesis"
                ],
                [
                    "Amazon Kinesis Video Streams ",
                    "kinesisvideo"
                ],
                [
                    "Dynamo DB",
                    "dynamodb"
                ]
            ]
        },
        {
            "label": "Region",
            "optional": false,
            "hint": "You can find your region in your account URL. For example, if your account URL is 'https://eu-west-1.console.s3.amazon.com', use 'eu-west-1' as the region.",
            "type": "string",
            "name": "aws_region"
        },
        {
            "label": "IAM role ARN",
            "optional": false,
            "type": "string",
            "name": "aws_assume_role",
            "help": {
                "title": "Using IAM Role authorization",
                "text": "Provide your IAM role ARN in the IAM role ARN field. Refer to the 'How to retrieve IAM role ARN' documentation for more information: https://docs.workato.com/en/developing-connectors/http/connection-setup.html#authentication-type-aws-iam-role-auth"
            }
        },
        {
            "label": "AWS access key ID",
            "optional": false,
            "hint": "Provide your AWS access key ID. Go to your AWS account and click **My Security Credentials > Users** to find the access key ID.",
            "type": "string",
            "name": "aws_api_key"
        },
        {
            "label": "Secret access key",
            "optional": false,
            "hint": "Provide your secret access key. Go to your AWS account and click **My Security Credentials > Users** to find your secret access key.",
            "type": "string",
            "name": "aws_secret_key"
        },
        {
            "label": "Azure Tenant ID",
            "optional": false,
            "hint": "Provide your tenant ID in the Azure Tenant ID field. If you have an Azure subscription, enter your Tenant ID. Otherwise, use common.",
            "type": "string",
            "name": "azure_tenant_id"
        },
        {
            "label": "On-prem NTLM profile",
            "hint": "Enter the NTLM Profile name given in the on-prem agent's config.yml file.",
            "type": "string",
            "name": "profile"
        },
        {
            "label": "Basic auth user",
            "optional": true,
            "type": "string",
            "name": "basic_user"
        },
        {
            "label": "Basic auth password",
            "optional": true,
            "type": "string",
            "name": "basic_password"
        },
        {
            "label": "Username",
            "optional": true,
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "optional": true,
            "type": "string",
            "name": "password"
        },
        {
            "label": "Header authorization",
            "optional": true,
            "hint": "Add custom auth headers",
            "type": "array",
            "name": "header_pair",
            "properties": [
                {
                    "label": "Key",
                    "type": "string",
                    "name": "param"
                },
                {
                    "label": "Value",
                    "type": "string",
                    "name": "value"
                }
            ]
        },
        {
            "label": "Endpoint has case-sensitive headers?",
            "default": "false",
            "optional": true,
            "hint": "Set to 'No' to convert the header names to sentence case. For example: `x-api-key` to `X-api-key`. Set this to 'Yes' if your endpoint headers are case-sensitive. Defaults to 'No'. This field has no effect when the **Wait for response** field is set to 'Yes' or when the connection uses an on-prem agent.",
            "type": "boolean",
            "name": "case_sensitive_headers"
        },
        {
            "label": "URL parameters",
            "optional": true,
            "type": "array",
            "name": "url_param",
            "properties": [
                {
                    "label": "Key",
                    "type": "string",
                    "name": "param"
                },
                {
                    "label": "Value",
                    "type": "string",
                    "name": "value"
                }
            ]
        },
        {
            "label": "OAuth2 authorization URL",
            "type": "string",
            "name": "oauth2_auth_url",
            "hint": "Refer to the Workato HTTP OAuth documentation to retrieve this value: https://docs.workato.com/developing-connectors/http.html#set-up-your-oauth-2-0-connection'"
        },
        {
            "label": "OAuth2 token URL",
            "type": "string",
            "name": "oauth2_token_url"
        },
        {
            "label": "OAuth2 client ID",
            "type": "string",
            "name": "oauth2_client_id"
        },
        {
            "label": "OAuth2 client secret",
            "type": "string",
            "name": "oauth2_client_secret"
        },
        {
            "label": "Azure endpoint version",
            "optional": true,
            "default": "2.0",
            "hint": "Select the version of the Azure endpoints to use. Default is 2.0",
            "type": "string",
            "name": "azure_endpoint_version",
            "pick_list": [
                [
                    "1.0",
                    "1.0"
                ],
                [
                    "2.0",
                    "2.0"
                ]
            ]
        },
        {
            "label": "How does the API require credentials to be sent to request a token?",
            "optional": true,
            "hint": "Select whether to send the client ID and secret in the token request body or as a base64 encoded string in the header.",
            "type": "string",
            "name": "param_type",
            "pick_list": [
                [
                    "Header",
                    "basic"
                ],
                [
                    "Body",
                    "payload"
                ]
            ]
        },
        {
            "label": "Base URL",
            "hint": "Set the Base URL for all requests. Recipes cannot override this value.",
            "optional": true,
            "type": "string",
            "name": "base_url"
        },
        {
            "label": "Use custom TLS/SSL certificate settings",
            "default": "false",
            "optional": true,
            "hint": "Use PEM format if you use custom certificate/key settings.",
            "type": "boolean",
            "name": "ssl_params"
        },
        {
            "label": "TLS server custom CA certificate",
            "optional": true,
            "type": "string",
            "name": "ssl_ca_cert",
            "help": {
                "title": "For servers using self-signed or custom root CAs",
                "text": "Enter your API server's self-signed certificate or a certificate signed by a non-standard root certificate authority. Separate certificates by an empty line if more than one intermediate is needed to complete the chain."
            }
        },
        {
            "label": "TLS client certificate",
            "optional": true,
            "type": "string",
            "name": "ssl_client_cert"
        },
        {
            "label": "TLS client key",
            "optional": true,
            "type": "string",
            "name": "ssl_client_key"
        },
        {
            "label": "TLS client intermediate certificates",
            "type": "string",
            "name": "ssl_client_intermediate_chain",
            "optional": true,
            "help": {
                "title": "Client intermediate certificate chain",
                "text": "Enter certificates if your client certificate relies on one or more intermediate certificates to link it to a root certificate authority trusted by your API server. Separate certificates by an empty line if more than one intermediate is needed to complete the chain."
            }
        },
        {
            "label": "Advanced settings",
            "optional": true,
            "type": "object",
            "name": "advanced_settings",
            "properties": [
                {
                    "label": "OAuth2 scopes",
                    "optional": true,
                    "hint": "Scope for access request. Separate each value with a space.",
                    "type": "string",
                    "name": "oauth2_scope"
                },
                {
                    "label": "Azure resource URI",
                    "hint": "Enter the resource URI for the Azure service you're requesting access to. Only one resource can be requested per connection. Go to **Azure Portal > App registrations > Your registration app > API permissions > Manage**. Click the permission name to retrieve the resource URI. Refer to the Microsoft Azure documentation for more information: https://learn.microsoft.com/en-us/rest/api/azure",
                    "type": "string",
                    "name": "azure_resource_uri"
                },
                {
                    "label": "Restrict to bucket",
                    "optional": true,
                    "hint": "Use this field to restrict the connection to a specific bucket. This is required when a user has limited s3:ListBucket access. Learn more: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
                    "type": "string",
                    "name": "aws_restrict_to_bucket"
                },
                {
                    "label": "Restrict to path",
                    "optional": true,
                    "hint": "Use this field to restrict the connection to a specific bucket and object or path. This is required when a user has limited s3:ListBucket access. Learn more: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-buckets",
                    "type": "string",
                    "name": "aws_restrict_to_path"
                },
                {
                    "label": "Token settings",
                    "optional": true,
                    "hint": "Default is Access Token",
                    "type": "string",
                    "name": "token_settings",
                    "options": [
                        [
                            "Use Access Token",
                            "access_token"
                        ],
                        [
                            "Use ID Token",
                            "id_token"
                        ]
                    ]
                }
            ]
        },
        {
            "label": "NTLM authentication",
            "hint": "Enter the NTLM authentication domain and workstation.",
            "type": "string",
            "name": "auth"
        },
        {
            "label": "Username",
            "hint": "Enter the NTLM authentication username.",
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "hint": "Enter the NTLM authentication password.",
            "type": "string",
            "name": "password"
        },
        {
            "label": "Base URL",
            "hint": "Enter the base URL for NTLM resources.",
            "type": "string",
            "name": "base_url"
        },
        {
            "label": "Optional properties",
            "optional": true,
            "type": "object",
            "name": "optional_properties",
            "properties": [
                {
                    "label": "Connections per route",
                    "optional": true,
                    "hint": "Sets the number of connections per route/host.",
                    "type": "integer",
                    "name": "cm_default_max_per_route"
                },
                {
                    "label": "Maximum connections",
                    "hint": "Sets the maximum number of connections.",
                    "optional": true,
                    "type": "integer",
                    "name": "cm_max_total"
                },
                {
                    "label": "Timeout",
                    "optional": true,
                    "hint": "The timeout in milliseconds used when requesting a connection.",
                    "type": "integer",
                    "name": "http_connect_timeout"
                },
                {
                    "label": "Connection request timeout",
                    "optional": true,
                    "hint": "The timeout in milliseconds until a connection is established.",
                    "type": "integer",
                    "name": "http_connection_request_timeout"
                },
                {
                    "label": "Socket timeout",
                    "optional": true,
                    "hint": "The socket timeout in milliseconds, which is the timeout for waiting for data. This is the maximum period of inactivity between two consecutive data packets.",
                    "type": "integer",
                    "name": "http_socket_timeout"
                },
                {
                    "label": "Verify host",
                    "optional": true,
                    "default": "true",
                    "hint": "Specifies whether to enable verification of the host name for SSL/TLS connections.",
                    "type": "boolean",
                    "name": "verifyHost"
                },
                {
                    "label": "Trust all",
                    "optional": true,
                    "default": "false",
                    "hint": "Specifies whether trust all certificates for SSL/TLS connections.",
                    "type": "boolean",
                    "name": "trustAll"
                }
            ]
        }
    ]
}
```

* * *

### HubSpot

**Provider value:**

```json
"provider": "hubspot"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced settings",
                  "properties":
                  [
                      {
                          "name": "scopes",
                          "type": "string",
                          "optional": true,
                          "label": "Scopes",
                          "hint": "               Select the areas of HubSpot this connection will have access to. Selecting scopes which your HubSpot account does not have access to will result in an error. Our default selection should be enough when working with contacts, companies, and deals.\n",
                          "default": "contacts"
                      }
                  ]
              }
          ]
      }
```

* * *

### IBM Watson Workspace

**Provider value:**

```json
"provider": "ibm_workspace"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Infusionsoft

**Provider value:**

```json
"provider": "infusionsoft"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Insightly

**Provider value:**

```json
"provider": "insightly"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "Api key",
                  "hint": "Click the drop-down at the top right corner of the home page. API KEY found under the 'User settings'"
              }
          ]
      }
```

* * *

### Instagram

**Provider value:**

```json
"provider": "instagram"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Intercom

**Provider value:**

```json
"provider": "intercom"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "user_ids",
                  "type": "string",
                  "optional": true,
                  "label": "Example user IDs",
                  "hint": "                   Provide comma separated Intercom user IDs, for example, <b>54253</b>, for Workato to retrieve the custom fields set up for these users.\n                   Maximum of <b>3</b> user IDs can be provided.\n"
              }
          ]
      }
```

* * *

### JavaScript

**Provider value:**

```json
"provider": "js_eval"
```

* * *

### JDBC

**Provider value:**

```json
"provider": "jdbc"
```

View connection parameters JSON

```json
{
    "oauth": false,
    "personalization": true,
    "input": [
        {
            "label": "On-prem connection profile",
            "type": "string",
            "name": "profile"
        },
        {
            "label": "JDBC connection URL",
            "hint": "Enter your JDBC URL. Refer to the database connection documentation for more information: https://docs.workato.com/on-prem/agents/connection/cloud.html#database-profile",
            "type": "string",
            "name": "url"
        },
        {
            "label": "JDBC driver class name",
            "hint": "Enter the fully-qualified name of the JDBC driver class for the given database.",
            "optional": true,
            "type": "string",
            "name": "driver"
        },
        {
            "label": "User name",
            "optional": true,
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "optional": true,
            "type": "string",
            "name": "password"
        },
        {
            "label": "Pooling settings",
            "optional": true,
            "type": "object",
            "name": "pooling",
            "properties": [
                {
                    "label": "Minimum pool size",
                    "optional": true,
                    "hint": "Enter the minimum number of connections for OPA to maintain in the pool, including both idle and in-use connections. The default is 1.",
                    "type": "integer",
                    "name": "minSize"
                },
                {
                    "label": "Maximum pool size",
                    "optional": true,
                    "hint": "Enter the maximum number of connections for OPA to maintain in the pool. When the pool reaches this size and no idle connections are available, Workato blocks new connection attempts until the 'Timeout' period ends. Defaults to 10.",
                    "type": "integer",
                    "name": "maxSize"
                },
                {
                    "label": "Idle timeout",
                    "optional": true,
                    "hint": "The maximum amount of time in seconds the connection is allowed to sit idle in the pool before removal. A value of 0 means connections aren't removed from the pool. Defaults to 30 minutes.",
                    "type": "integer",
                    "name": "idleTimeout"
                },
                {
                    "label": "Maximum lifetime",
                    "optional": true,
                    "hint": "The maximum lifetime in seconds of a connection in the pool. When a connection is idle and reaches this timeout, even if recently used, Workato removes it from the pool. Defaults to 30 minutes.",
                    "type": "integer",
                    "name": "maxLifetime"
                },
                {
                    "label": "Timeout",
                    "optional": true,
                    "hint": "The maximum lifetime in seconds of a connection in the pool. When a connection is idle and reaches this timeout, even if recently used, Workato removes it from the pool. Defaults to 30 minutes.",
                    "type": "integer",
                    "name": "timeout"
                }
            ]
        },
        {
            "label": "Schema",
            "optional": true,
            "type": "string",
            "name": "schema_name"
        },
        {
            "type": "array",
            "name": "additional_properties",
            "label": "Additional properties for JDBC connection",
            "optional": true,
            "properties": [
                {
                    "label": "Key",
                    "type": "string",
                    "name": "key"
                },
                {
                    "label": "Value",
                    "type": "string",
                    "name": "value"
                }
            ]
        }
    ]
}
```

* * *

### JDBC (Secondary)

**Provider value:**

```json
"provider": "jdbc_secondary"
```

View connection parameters JSON

```json
{
    "oauth": false,
    "personalization": true,
    "input": [
        {
            "label": "On-prem connection profile",
            "type": "string",
            "name": "profile"
        },
        {
            "label": "JDBC connection URL",
            "hint": "Enter your JDBC URL. Refer to the database connection documentation for more information: https://docs.workato.com/on-prem/agents/connection/cloud.html#database-profile",
            "type": "string",
            "name": "url"
        },
        {
            "label": "JDBC driver class name",
            "hint": "Enter the fully-qualified name of the JDBC driver class for the given database.",
            "optional": true,
            "type": "string",
            "name": "driver"
        },
        {
            "label": "User name",
            "optional": true,
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "optional": true,
            "type": "string",
            "name": "password"
        },
        {
            "label": "Pooling settings",
            "optional": true,
            "type": "object",
            "name": "pooling",
            "properties": [
                {
                    "label": "Minimum pool size",
                    "optional": true,
                    "hint": "Enter the minimum number of connections for OPA to maintain in the pool, including both idle and in-use connections. The default is 1.",
                    "type": "integer",
                    "name": "minSize"
                },
                {
                    "label": "Maximum pool size",
                    "optional": true,
                    "hint": "Enter the maximum number of connections for OPA to maintain in the pool. When the pool reaches this size and no idle connections are available, Workato blocks new connection attempts until the 'Timeout' period ends. Defaults to 10.",
                    "type": "integer",
                    "name": "maxSize"
                },
                {
                    "label": "Idle timeout",
                    "optional": true,
                    "hint": "The maximum amount of time in seconds the connection is allowed to sit idle in the pool before removal. A value of 0 means connections aren't removed from the pool. Defaults to 30 minutes.",
                    "type": "integer",
                    "name": "idleTimeout"
                },
                {
                    "label": "Maximum lifetime",
                    "optional": true,
                    "hint": "The maximum lifetime in seconds of a connection in the pool. When a connection is idle and reaches this timeout, even if recently used, Workato removes it from the pool. Defaults to 30 minutes.",
                    "type": "integer",
                    "name": "maxLifetime"
                },
                {
                    "label": "Timeout",
                    "optional": true,
                    "hint": "The maximum lifetime in seconds of a connection in the pool. When a connection is idle and reaches this timeout, even if recently used, Workato removes it from the pool. Defaults to 30 minutes.",
                    "type": "integer",
                    "name": "timeout"
                }
            ]
        },
        {
            "label": "Schema",
            "optional": true,
            "type": "string",
            "name": "schema_name"
        },
        {
            "type": "array",
            "name": "additional_properties",
            "label": "Additional properties for JDBC connection",
            "optional": true,
            "properties": [
                {
                    "label": "Key",
                    "type": "string",
                    "name": "key"
                },
                {
                    "label": "Value",
                    "type": "string",
                    "name": "value"
                }
            ]
        }
    ]
}
```

* * *

### Jenkins

**Provider value:**

```json
"provider": "jenkins"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "root_uri",
                  "type": "string",
                  "optional": false,
                  "label": "Jenkins root URI",
                  "hint": "                  Host (and optional port) of your Jenkins server. Eg. http://workato-jenkins.<br>\n                  Go to Manage Jenkins-> Configure Global Security. Uncheck <b>Prevent Cross Site Request Forgery exploits</b>.\n"
              },
              {
                  "name": "username",
                  "type": "string",
                  "optional": false,
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": false,
                  "label": "Password"
              }
          ]
      }
```

* * *

### Jira

**Provider value:**

```json
"provider": "jira"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Auth type",
            "hint": "Select the authentication type for your Jira account. Jira Server and Jira Data center do not support OAuth 2.0.",
            "type": "string",
            "name": "auth_type",
            "pick_list": [
                [
                    "Basic",
                    "basic"
                ],
                [
                    "API token",
                    "api_token"
                ],
                [
                    "OAuth 2.0",
                    "oauth"
                ],
                [
                    "Personal access token",
                    "access_token"
                ]
            ]
        },
        {
            "label": "Host name",
            "hint": "Enter the Jira instance URL used to sign in to Jira. For example: 'workato.atlassian.net'.",
            "type": "string",
            "name": "host_name",
            "toggle_hint": "Enter HTTPS subdomain",
            "toggle_field": {
                "type": "string",
                "name": "host_url"
            }
        },
        {
            "label": "Personal access token",
            "optional": false,
            "hint": "Refer to the following guide to generate a personal access token: 'https://docs.workato.com/en/connectors/jira.html#personal-access-tokens'",
            "type": "string",
            "name": "token"
        },
        {
            "label": "Email",
            "type": "string",
            "name": "email"
        },
        {
            "label": "API token",
            "hint": "Refer to the following documentation to create API tokens: 'https://id.atlassian.com'",
            "type": "string",
            "name": "apitoken"
        },
        {
            "label": "Username",
            "hint": "Enter your e-mail username or enter 'admin' to sign in as the creator of the Jira instance. For example, if the e-mail is 'johndoe@workato.com', the username is 'johndoe'.",
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "hint": "From 1 Dec 2018, Atlassian is deprecating basic auth with password for Jira (cloud only). Update your connection to use API tokens instead. Refer to the Jira connector documentation for more information: 'https://https://docs.workato.com/connectors/jira.html#how-to-connect-to-jira-on-workato'.",
            "type": "string",
            "name": "password"
        },
        {
            "label": "Advanced settings",
            "optional": true,
            "type": "object",
            "name": "advanced_settings",
            "properties": [
                {
                    "label": "Scopes",
                    "optional": true,
                    "hint": "Select scopes to request for this connection. Only select scopes that the client is authorized to use. Default scopes are provided in addition to the scopes you select. Defaults to the following permissions if left blank: 'read:jira-user', 'write:jira-work', 'manage:jira-project', 'read:jira-work', 'manage:jira-webhook'. Refer to the jira scope documentation for more information: 'https://developer.atlassian.com/cloud/jira/platform/scopes-for-connect-and-oauth-2-3LO-apps/'",
                    "type": "string",
                    "name": "scopes",
                    "options": [
                        [
                            "View user profiles",
                            "read:jira-user"
                        ],
                        [
                            "View Jira issue data",
                            "read:jira-work"
                        ],
                        [
                            "Create and manage issues",
                            "write:jira-work"
                        ],
                        [
                            "Manage project settings",
                            "manage:jira-project"
                        ],
                        [
                            "Manage Jira webhooks",
                            "manage:jira-webhook"
                        ],
                        [
                            "Manage Jira global settings",
                            "manage:jira-configuration"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### Jira (Secondary)

**Provider value:**

```json
"provider": "jira_secondary"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Auth type",
            "hint": "Select the authentication type for your Jira account. Jira Server and Jira Data center do not support OAuth 2.0.",
            "type": "string",
            "name": "auth_type",
            "pick_list": [
                [
                    "Basic",
                    "basic"
                ],
                [
                    "API token",
                    "api_token"
                ],
                [
                    "OAuth 2.0",
                    "oauth"
                ],
                [
                    "Personal access token",
                    "access_token"
                ]
            ]
        },
        {
            "label": "Host name",
            "hint": "Enter the Jira instance URL used to sign in to Jira. For example: 'workato.atlassian.net'.",
            "type": "string",
            "name": "host_name",
            "toggle_hint": "Enter HTTPS subdomain",
            "toggle_field": {
                "type": "string",
                "name": "host_url"
            }
        },
        {
            "label": "Personal access token",
            "optional": false,
            "hint": "Refer to the following guide to generate a personal access token: 'https://docs.workato.com/en/connectors/jira.html#personal-access-tokens'",
            "type": "string",
            "name": "token"
        },
        {
            "label": "Email",
            "type": "string",
            "name": "email"
        },
        {
            "label": "API token",
            "hint": "Refer to the following documentation to create API tokens: 'https://id.atlassian.com'",
            "type": "string",
            "name": "apitoken"
        },
        {
            "label": "Username",
            "hint": "Enter your e-mail username or enter 'admin' to sign in as the creator of the Jira instance. For example, if the e-mail is 'johndoe@workato.com', the username is 'johndoe'.",
            "type": "string",
            "name": "username"
        },
        {
            "label": "Password",
            "hint": "From 1 Dec 2018, Atlassian is deprecating basic auth with password for Jira (cloud only). Update your connection to use API tokens instead. Refer to the Jira connector documentation for more information: 'https://https://docs.workato.com/connectors/jira.html#how-to-connect-to-jira-on-workato'.",
            "type": "string",
            "name": "password"
        },
        {
            "label": "Advanced settings",
            "optional": true,
            "type": "object",
            "name": "advanced_settings",
            "properties": [
                {
                    "label": "Scopes",
                    "optional": true,
                    "hint": "Select scopes to request for this connection. Only select scopes that the client is authorized to use. Default scopes are provided in addition to the scopes you select. Defaults to the following permissions if left blank: 'read:jira-user', 'write:jira-work', 'manage:jira-project', 'read:jira-work', 'manage:jira-webhook'. Refer to the jira scope documentation for more information: 'https://developer.atlassian.com/cloud/jira/platform/scopes-for-connect-and-oauth-2-3LO-apps/'",
                    "type": "string",
                    "name": "scopes",
                    "options": [
                        [
                            "View user profiles",
                            "read:jira-user"
                        ],
                        [
                            "View Jira issue data",
                            "read:jira-work"
                        ],
                        [
                            "Create and manage issues",
                            "write:jira-work"
                        ],
                        [
                            "Manage project settings",
                            "manage:jira-project"
                        ],
                        [
                            "Manage Jira webhooks",
                            "manage:jira-webhook"
                        ],
                        [
                            "Manage Jira global settings",
                            "manage:jira-configuration"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### JIRA Service Desk

**Provider value:**

```json
"provider": "jira_service_desk"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "host_name",
                  "type": "string",
                  "label": "Host name",
                  "hint": "Refer to the URL of your Jira account and complete the above URL. For example, <b>workato.atlassian.net</b>"
              },
              {
                  "name": "host_url",
                  "type": "string",
                  "label": "Host name with protocol",
                  "hint": "Refer to the URL of your Jira account and specify the above URL.<br>for example, <b>http://workato.atlassian.net</b>"
              },
              {
                  "name": "api_token_auth",
                  "type": "boolean",
                  "label": "API token authentication?",
                  "hint": "Is authentication based on API tokens? If Yes, provide <b>Email</b> & <b>API token</b>. If No, provide <b>Username</b> & <b>Password</b>.",
                  "default": "false"
              },
              {
                  "name": "email",
                  "type": "string",
                  "optional": true,
                  "label": "Email"
              },
              {
                  "name": "apitoken",
                  "type": "string",
                  "optional": true,
                  "label": "API token",
                  "hint": "             Get/create API tokens by going to <a href='https://id.atlassian.com' target='_blank' ><b>id.atlassian.com</b></a> > <b>API tokens</b> > <b>Create API token</b>.\n"
              }
          ]
      }
```

* * *

### JMS

**Provider value:**

```json
"provider": "jms"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem JMS connection profile"
              }
          ]
      }
```

* * *

### JobScience

**Provider value:**

```json
"provider": "jobscience"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### Jobvite

**Provider value:**

```json
"provider": "jobvite"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "API Key",
                  "hint": "Enter the <b>Api Key</b> from jobvite."
              },
              {
                  "name": "secret",
                  "type": "string",
                  "label": "Secret",
                  "hint": "Enter the <b>Secret</b> from jobvite."
              },
              {
                  "name": "use_staging",
                  "type": "boolean",
                  "label": "Use Staging",
                  "hint": "If selected, staging jobvite instance will be used",
                  "default": "false"
              },
              {
                  "name": "use_v2",
                  "type": "boolean",
                  "optional": true,
                  "label": "Use V2 API",
                  "hint": "If selected, V2 version will be used",
                  "default": "false"
              }
          ]
      }
```

* * *

### JSON parser by Workato

**Provider value:**

```json
"provider": "json_parser"
```

* * *

### JSON Web Token (JWT)

**Provider value:**

```json
"provider": "jwt"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "alg",
                  "type": "string",
                  "label": "Signing algorithm",
                  "hint": "Select the JWT signing algorithm",
                  "pick_list":
                  [
                      [
                          "HMAC using SHA-256",
                          "HS256"
                      ],
                      [
                          "HMAC using SHA-384",
                          "HS384"
                      ],
                      [
                          "HMAC using SHA-512",
                          "HS512"
                      ],
                      [
                          "RSA using SHA-256",
                          "RS256"
                      ],
                      [
                          "RSA using SHA-384",
                          "RS384"
                      ],
                      [
                          "RSA using SHA-512",
                          "RS512"
                      ]
                  ],
                  "default": "HS256"
              },
              {
                  "name": "hmac_secret",
                  "type": "string",
                  "optional": true,
                  "label": "HMAC shared secret",
                  "hint": "Enter the shared HMAC secret(min 32 characters)"
              },
              {
                  "name": "public_key",
                  "type": "string",
                  "optional": true,
                  "label": "Public key",
                  "hint": "                                Learn how to generate a pair of Public key and Private key\n                                <a href=\"https://docs.workato.com/features/pgp-encryption.html\" target=\"_blank\">here</a>.\n"
              },
              {
                  "name": "private_key",
                  "type": "string",
                  "optional": true,
                  "label": "Private key",
                  "hint": "                                 Learn how to generate a pair of Public key and Private key\n                                 <a href=\"https://docs.workato.com/features/pgp-encryption.html\" target=\"_blank\">here</a>.\n"
              },
              {
                  "name": "passphrase",
                  "type": "string",
                  "optional": true,
                  "label": "Passphrase",
                  "hint": "Passphrase for encrypted private key"
              }
          ]
      }
```

* * *

### JumpCloud

**Provider value:**

```json
"provider": "jump_cloud"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "API key",
                  "hint": "Click <a href='https://docs.jumpcloud.com/2.0/authentication-and-authorization/authentication-and-authorization-overview#access-your-api-key' target='_blank'>here</a> to get API key."
              },
              {
                  "name": "org_id",
                  "type": "string",
                  "optional": true,
                  "label": "Organization ID",
                  "hint": "<span class='provider'>Organization ID </span> is required for all multi-tenant admins. Click <a href='https://docs.jumpcloud.com/2.0/authentication-and-authorization/multi-tenant-organization-api-headers#to-obtain-an-individual-organization-id-via-the-ui' target='_blank'>here</a> to get Organization ID."
              }
          ]
      }
```

* * *

### Kenandy

**Provider value:**

```json
"provider": "kenandy"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### Kizen

**Provider value:**

```json
"provider": "kizen"
```

* * *

### Knack

**Provider value:**

```json
"provider": "knack"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "app_id",
                  "type": "string",
                  "optional": false,
                  "label": "Application ID",
                  "hint": "Hover over gear icon, Select API & Code -> get Application ID"
              },
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "API Key",
                  "hint": "Hover over gear icon, Select API & Code -> get API Key"
              }
          ]
      }
```

* * *

### Librato

**Provider value:**

```json
"provider": "librato"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "username",
                  "type": "string",
                  "optional": false,
                  "label": "Username",
                  "hint": "Go to Account Settings->API Token. GET token. eg: abc@efg.com"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": false,
                  "label": "Password or personal API key",
                  "hint": "If its API key, Go to Account Settings->API Token. GET API Key"
              }
          ]
      }
```

* * *

### LinkedIn

**Provider value:**

```json
"provider": "linkedin"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Logger by Workato

**Provider value:**

```json
"provider": "logger"
```

* * *

### Lookup tables by Workato

**Provider value:**

```json
"provider": "lookup_table"
```

* * *

### Magento 2

**Provider value:**

```json
"provider": "magento"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "server",
                  "type": "string",
                  "optional": false,
                  "label": "Server domain",
                  "hint": "Enter your full URL, for example, <b>http://mymagentostore.com</b>"
              },
              {
                  "name": "username",
                  "type": "string",
                  "optional": false,
                  "label": "Username",
                  "hint": "If account type is admin, enter username. Otherwise, enter email address"
              },
              {
                  "name": "account_type",
                  "type": "string",
                  "optional": false,
                  "label": "Account type",
                  "hint": "Select if your connected account is an admin or non-admin account",
                  "pick_list":
                  [
                      [
                          "admin",
                          "admin"
                      ],
                      [
                          "customer",
                          "customer"
                      ]
                  ]
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": false,
                  "label": "Password"
              }
          ]
      }
```

* * *

### MailChimp

**Provider value:**

```json
"provider": "mailchimp"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Mapper by Workato

**Provider value:**

```json
"provider": "workato_mapper"
```

* * *

### Marketo

**Provider value:**

```json
"provider": "marketo"
```

View connection parameters JSON

```json
{
    "oauth": false,
    "personalization": true,
    "input": [
        {
            "label": "REST Endpoint",
            "hint": "Provide the base URL of your Marketo instance. Refer to the Marketo developer documentation for more information: 'https://developers.marketo.com/documentation/rest/endpoint-url/'",
            "type": "string",
            "name": "endpoint"
        },
        {
            "label": "Custom Service client ID",
            "hint": "Enter a Marketo client ID. Refer to the Marketo developer documentation for more information: 'https://developers.marketo.com/documentation/rest/custom-service/'",
            "type": "string",
            "name": "client_id"
        },
        {
            "label": "Custom Service client secret",
            "hint": "Enter a Marketo client secret. Refer to the Marketo connector documentation for more information: 'https://docs.workato.com/en/connectors/marketo.html'",
            "type": "string",
            "name": "client_secret"
        }
    ]
}
```

* * *

### Marketo (Secondary)

**Provider value:**

```json
"provider": "marketo_secondary"
```

View connection parameters JSON

```json
{
    "oauth": false,
    "personalization": true,
    "input": [
        {
            "label": "REST Endpoint",
            "hint": "Provide the base URL of your Marketo instance. Refer to the Marketo developer documentation for more information: 'https://developers.marketo.com/documentation/rest/endpoint-url/'",
            "type": "string",
            "name": "endpoint"
        },
        {
            "label": "Custom Service client ID",
            "hint": "Enter a Marketo client ID. Refer to the Marketo developer documentation for more information: 'https://developers.marketo.com/documentation/rest/custom-service/'",
            "type": "string",
            "name": "client_id"
        },
        {
            "label": "Custom Service client secret",
            "hint": "Enter a Marketo client secret. Refer to the Marketo connector documentation for more information: 'https://docs.workato.com/en/connectors/marketo.html'",
            "type": "string",
            "name": "client_secret"
        }
    ]
}
```

* * *

### Maxio

**Provider value:**

```json
"provider": "chargify"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "API Key",
            "name": "api_key",
            "hint": "Enter an API key. Retrieve this value from the “API Access” tab of your seller dashboard.",
            "type": "string"
        },
        {
            "label": "Sub-domain",
            "name": "subdomain",
            "hint": "Enter your Maxio subdomain. This is most often your company name.",
            "type": "string"
        }
    ]
}
```

* * *

### Message template by Workato

**Provider value:**

```json
"provider": "workato_template"
```

* * *

### Microsoft Dynamics 365

**Provider value:**

```json
"provider": "microsoft_dynamics_crm"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Subdomain",
                  "hint": "             If your Microsoft Dynamics 365 URL is <b>https://abc.crm.dynamics.com</b>,\n             subdomain will be <b>abc.crm.dynamics.com</b>\n"
              },
              {
                  "name": "account_type",
                  "type": "string",
                  "label": "Account type",
                  "pick_list":
                  [
                      [
                          "On premise",
                          "onpremises"
                      ],
                      [
                          "Cloud",
                          "online"
                      ]
                  ]
              },
              {
                  "name": "adfs_name",
                  "type": "string",
                  "optional": true,
                  "label": "AD domain name",
                  "hint": "             Requires, if the account type is 'On premise'.\n             If your AD server is <b>https://abc.adfs.dynamics.com/adfs</b>, AD domain name will be <b>abc.adfs.dynamics.com</b>\n"
              },
              {
                  "name": "client_id",
                  "type": "string",
                  "label": "Client ID",
                  "hint": "Click <a target='_blank' href=http://docs.workato.com/connectors/dynamics-crm.html>here</a> to know how to get client ID"
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "optional": true,
                  "label": "Client secret"
              }
          ]
      }
```

* * *

### Microsoft Dynamics Business Central

**Provider value:**

```json
"provider": "business_central"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Tenant ID",
            "name": "tenant_id",
            "optional": false,
            "hint": "Enter your Tenant ID. Sign in to the Microsoft Azure portal (http://portal.azure.com/) and go to the Azure Active Directory Overview page to retrieve this value.",
            "type": "string"
        },
        {
            "label": "Environment name",
            "name": "environment",
            "optional": false,
            "hint": "Defaults to 'Production'.",
            "type": "string",
            "pick_list": [
                [
                    "Production",
                    "Production"
                ],
                [
                    "Sandbox",
                    "Sandbox"
                ]
            ]
        },
        {
            "label": "Company ID",
            "name": "company_id",
            "optional": true,
            "hint": "Enter the company ID to use by default for actions. Leave this field blank to specify the company in each action. Open Business Central and go to 'Companies' to retrieve a company ID.",
            "type": "string"
        }
    ]
}
```

* * *

### Microsoft Sharepoint

**Provider value:**

```json
"provider": "microsoft_sharepoint"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "subdomain",
                  "type": "string",
                  "optional": false,
                  "label": "Subdomain",
                  "hint": "Enter your SharePoint subdomain as found in your SharePoint URL. If your SharePoint URL is <b>https://abc.sharepoint.com</b>, then subdomain is <b>abc</b>"
              },
              {
                  "name": "domain",
                  "type": "string",
                  "label": "Domain",
                  "hint": "Enter full URL of your SharePoint domain. <b>for example, https://company-name.sharepoint.com</b>."
              },
              {
                  "name": "client_id",
                  "type": "string",
                  "optional": true,
                  "label": "Client ID",
                  "hint": "<a href='https://docs.workato.com/connectors/sharepoint.html' target='_blank'>Click here</a> to learn how to generate Client ID and Client secret."
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "optional": true,
                  "label": "Client secret",
                  "hint": "<a href='https://docs.workato.com/connectors/sharepoint.html' target='_blank'>Click here</a> to learn how to generate Client ID and Client secret."
              },
              {
                  "name": "connection_siteurl",
                  "type": "string",
                  "optional": true,
                  "label": "Site name",
                  "hint": "                  The name of the SharePoint site you want to connect to. Use this field if you only have access to that specific site, but not the home site.\n                  If left blank, Workato will connect to your default home site.\n                  Use the site name as found in the URL of site page. eg. If the URL is <b>https://company-name.sharepoint.com/sites/product</b>, then use <b>product</b>.\n"
              }
          ]
      }
```

* * *

### Miro

**Provider value:**

```json
"provider": "miro_board"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "client_id",
                  "type": "string",
                  "optional": false,
                  "label": "Client ID"
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "optional": false,
                  "label": "Client secret"
              }
          ]
      }
```

* * *

### Mixpanel

**Provider value:**

```json
"provider": "mixpanel"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "Api key",
                  "hint": "Can be found in your account menu within the projects tab"
              },
              {
                  "name": "api_secret",
                  "type": "string",
                  "label": "Api secret",
                  "hint": "Can be found in your account menu within the projects tab"
              }
          ]
      }
```

* * *

### MySQL

**Provider value:**

```json
"provider": "mysql"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "label": "Port"
              },
              {
                  "name": "database",
                  "type": "string",
                  "label": "Database"
              }
          ]
      }
```

* * *

### MySQL (Secondary)

**Provider value:**

```json
"provider": "mysql_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "label": "Port"
              },
              {
                  "name": "database",
                  "type": "string",
                  "label": "Database"
              }
          ]
      }
```

* * *

### Namely

**Provider value:**

```json
"provider": "namely"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "company",
                  "type": "string",
                  "label": "Company",
                  "hint": "If your Namely url is https://acme.namely.com then use <b>acme</b> as value."
              }
          ]
      }
```

* * *

### NationBuilder

**Provider value:**

```json
"provider": "nationbuilder"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "slug",
                  "type": "string",
                  "label": "Nation",
                  "hint": "Your NationBuilder \"nation\", for example, <b>voteforpedro</b>.nationbuilder.com"
              }
          ]
      }
```

* * *

### NetSuite

**Provider value:**

```json
"provider": "netsuite"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "account",
                  "type": "string",
                  "label": "Account ID",
                  "hint": "Login as Administrator, then in <b>Setup Menu</b>, find in <b>Integration</b> > <b>Web Services Preferences</b>"
              },
              {
                  "name": "tokenId",
                  "type": "string",
                  "label": "Token ID"
              },
              {
                  "name": "tokenSecret",
                  "type": "string",
                  "label": "Token secret"
              },
              {
                  "name": "timezone",
                  "type": "string",
                  "optional": true,
                  "label": "Account timezone",
                  "hint": "Needed for consistency with NetSuite - pick same as your NetSuite profile",
                  "pick_list":
                  [
                      [
                          "American Samoa (-11:00)",
                          "American Samoa"
                      ],
                      [
                          "International Date Line West (-11:00)",
                          "International Date Line West"
                      ],
                      [
                          "Midway Island (-11:00)",
                          "Midway Island"
                      ],
                      [
                          "Hawaii (-10:00)",
                          "Hawaii"
                      ],
                      [
                          "Alaska (-9:00)",
                          "Alaska"
                      ],
                      [
                          "Pacific Time (US & Canada) (-8:00)",
                          "Pacific Time (US & Canada)"
                      ],
                      [
                          "Tijuana (-8:00)",
                          "Tijuana"
                      ],
                      [
                          "Arizona (-7:00)",
                          "Arizona"
                      ],
                      [
                          "Chihuahua (-7:00)",
                          "Chihuahua"
                      ],
                      [
                          "Mazatlan (-7:00)",
                          "Mazatlan"
                      ],
                      [
                          "Mountain Time (US & Canada) (-7:00)",
                          "Mountain Time (US & Canada)"
                      ],
                      [
                          "Central America (-6:00)",
                          "Central America"
                      ],
                      [
                          "Central Time (US & Canada) (-6:00)",
                          "Central Time (US & Canada)"
                      ],
                      [
                          "Guadalajara (-6:00)",
                          "Guadalajara"
                      ],
                      [
                          "Mexico City (-6:00)",
                          "Mexico City"
                      ],
                      [
                          "Monterrey (-6:00)",
                          "Monterrey"
                      ],
                      [
                          "Saskatchewan (-6:00)",
                          "Saskatchewan"
                      ],
                      [
                          "Bogota (-5:00)",
                          "Bogota"
                      ],
                      [
                          "Eastern Time (US & Canada) (-5:00)",
                          "Eastern Time (US & Canada)"
                      ],
                      [
                          "Indiana (East) (-5:00)",
                          "Indiana (East)"
                      ],
                      [
                          "Lima (-5:00)",
                          "Lima"
                      ],
                      [
                          "Quito (-5:00)",
                          "Quito"
                      ],
                      [
                          "Atlantic Time (Canada) (-4:00)",
                          "Atlantic Time (Canada)"
                      ],
                      [
                          "Caracas (-4:00)",
                          "Caracas"
                      ],
                      [
                          "Georgetown (-4:00)",
                          "Georgetown"
                      ],
                      [
                          "La Paz (-4:00)",
                          "La Paz"
                      ],
                      [
                          "Santiago (-4:00)",
                          "Santiago"
                      ],
                      [
                          "Newfoundland (-4:30)",
                          "Newfoundland"
                      ],
                      [
                          "Brasilia (-3:00)",
                          "Brasilia"
                      ],
                      [
                          "Buenos Aires (-3:00)",
                          "Buenos Aires"
                      ],
                      [
                          "Greenland (-3:00)",
                          "Greenland"
                      ],
                      [
                          "Montevideo (-3:00)",
                          "Montevideo"
                      ],
                      [
                          "Mid-Atlantic (-2:00)",
                          "Mid-Atlantic"
                      ],
                      [
                          "Azores (-1:00)",
                          "Azores"
                      ],
                      [
                          "Cape Verde Is. (-1:00)",
                          "Cape Verde Is."
                      ],
                      [
                          "Casablanca (+0:00)",
                          "Casablanca"
                      ],
                      [
                          "Dublin (+0:00)",
                          "Dublin"
                      ],
                      [
                          "Edinburgh (+0:00)",
                          "Edinburgh"
                      ],
                      [
                          "Lisbon (+0:00)",
                          "Lisbon"
                      ],
                      [
                          "London (+0:00)",
                          "London"
                      ],
                      [
                          "Monrovia (+0:00)",
                          "Monrovia"
                      ],
                      [
                          "UTC (+0:00)",
                          "UTC"
                      ],
                      [
                          "Amsterdam (+1:00)",
                          "Amsterdam"
                      ],
                      [
                          "Belgrade (+1:00)",
                          "Belgrade"
                      ],
                      [
                          "Berlin (+1:00)",
                          "Berlin"
                      ],
                      [
                          "Bern (+1:00)",
                          "Bern"
                      ],
                      [
                          "Bratislava (+1:00)",
                          "Bratislava"
                      ],
                      [
                          "Brussels (+1:00)",
                          "Brussels"
                      ],
                      [
                          "Budapest (+1:00)",
                          "Budapest"
                      ],
                      [
                          "Copenhagen (+1:00)",
                          "Copenhagen"
                      ],
                      [
                          "Ljubljana (+1:00)",
                          "Ljubljana"
                      ],
                      [
                          "Madrid (+1:00)",
                          "Madrid"
                      ],
                      [
                          "Paris (+1:00)",
                          "Paris"
                      ],
                      [
                          "Prague (+1:00)",
                          "Prague"
                      ],
                      [
                          "Rome (+1:00)",
                          "Rome"
                      ],
                      [
                          "Sarajevo (+1:00)",
                          "Sarajevo"
                      ],
                      [
                          "Skopje (+1:00)",
                          "Skopje"
                      ],
                      [
                          "Stockholm (+1:00)",
                          "Stockholm"
                      ],
                      [
                          "Vienna (+1:00)",
                          "Vienna"
                      ],
                      [
                          "Warsaw (+1:00)",
                          "Warsaw"
                      ],
                      [
                          "West Central Africa (+1:00)",
                          "West Central Africa"
                      ],
                      [
                          "Zagreb (+1:00)",
                          "Zagreb"
                      ],
                      [
                          "Athens (+2:00)",
                          "Athens"
                      ],
                      [
                          "Bucharest (+2:00)",
                          "Bucharest"
                      ],
                      [
                          "Cairo (+2:00)",
                          "Cairo"
                      ],
                      [
                          "Harare (+2:00)",
                          "Harare"
                      ],
                      [
                          "Helsinki (+2:00)",
                          "Helsinki"
                      ],
                      [
                          "Jerusalem (+2:00)",
                          "Jerusalem"
                      ],
                      [
                          "Kaliningrad (+2:00)",
                          "Kaliningrad"
                      ],
                      [
                          "Kyiv (+2:00)",
                          "Kyiv"
                      ],
                      [
                          "Pretoria (+2:00)",
                          "Pretoria"
                      ],
                      [
                          "Riga (+2:00)",
                          "Riga"
                      ],
                      [
                          "Sofia (+2:00)",
                          "Sofia"
                      ],
                      [
                          "Tallinn (+2:00)",
                          "Tallinn"
                      ],
                      [
                          "Vilnius (+2:00)",
                          "Vilnius"
                      ],
                      [
                          "Baghdad (+3:00)",
                          "Baghdad"
                      ],
                      [
                          "Istanbul (+3:00)",
                          "Istanbul"
                      ],
                      [
                          "Kuwait (+3:00)",
                          "Kuwait"
                      ],
                      [
                          "Minsk (+3:00)",
                          "Minsk"
                      ],
                      [
                          "Moscow (+3:00)",
                          "Moscow"
                      ],
                      [
                          "Nairobi (+3:00)",
                          "Nairobi"
                      ],
                      [
                          "Riyadh (+3:00)",
                          "Riyadh"
                      ],
                      [
                          "St. Petersburg (+3:00)",
                          "St. Petersburg"
                      ],
                      [
                          "Tehran (+3:30)",
                          "Tehran"
                      ],
                      [
                          "Abu Dhabi (+4:00)",
                          "Abu Dhabi"
                      ],
                      [
                          "Baku (+4:00)",
                          "Baku"
                      ],
                      [
                          "Muscat (+4:00)",
                          "Muscat"
                      ],
                      [
                          "Samara (+4:00)",
                          "Samara"
                      ],
                      [
                          "Tbilisi (+4:00)",
                          "Tbilisi"
                      ],
                      [
                          "Volgograd (+4:00)",
                          "Volgograd"
                      ],
                      [
                          "Yerevan (+4:00)",
                          "Yerevan"
                      ],
                      [
                          "Kabul (+4:30)",
                          "Kabul"
                      ],
                      [
                          "Ekaterinburg (+5:00)",
                          "Ekaterinburg"
                      ],
                      [
                          "Islamabad (+5:00)",
                          "Islamabad"
                      ],
                      [
                          "Karachi (+5:00)",
                          "Karachi"
                      ],
                      [
                          "Tashkent (+5:00)",
                          "Tashkent"
                      ],
                      [
                          "Chennai (+5:30)",
                          "Chennai"
                      ],
                      [
                          "Kolkata (+5:30)",
                          "Kolkata"
                      ],
                      [
                          "Mumbai (+5:30)",
                          "Mumbai"
                      ],
                      [
                          "New Delhi (+5:30)",
                          "New Delhi"
                      ],
                      [
                          "Sri Jayawardenepura (+5:30)",
                          "Sri Jayawardenepura"
                      ],
                      [
                          "Kathmandu (+5:45)",
                          "Kathmandu"
                      ],
                      [
                          "Almaty (+6:00)",
                          "Almaty"
                      ],
                      [
                          "Astana (+6:00)",
                          "Astana"
                      ],
                      [
                          "Dhaka (+6:00)",
                          "Dhaka"
                      ],
                      [
                          "Urumqi (+6:00)",
                          "Urumqi"
                      ],
                      [
                          "Rangoon (+6:30)",
                          "Rangoon"
                      ],
                      [
                          "Bangkok (+7:00)",
                          "Bangkok"
                      ],
                      [
                          "Hanoi (+7:00)",
                          "Hanoi"
                      ],
                      [
                          "Jakarta (+7:00)",
                          "Jakarta"
                      ],
                      [
                          "Krasnoyarsk (+7:00)",
                          "Krasnoyarsk"
                      ],
                      [
                          "Novosibirsk (+7:00)",
                          "Novosibirsk"
                      ],
                      [
                          "Beijing (+8:00)",
                          "Beijing"
                      ],
                      [
                          "Chongqing (+8:00)",
                          "Chongqing"
                      ],
                      [
                          "Hong Kong (+8:00)",
                          "Hong Kong"
                      ],
                      [
                          "Irkutsk (+8:00)",
                          "Irkutsk"
                      ],
                      [
                          "Kuala Lumpur (+8:00)",
                          "Kuala Lumpur"
                      ],
                      [
                          "Perth (+8:00)",
                          "Perth"
                      ],
                      [
                          "Singapore (+8:00)",
                          "Singapore"
                      ],
                      [
                          "Taipei (+8:00)",
                          "Taipei"
                      ],
                      [
                          "Ulaanbaatar (+8:00)",
                          "Ulaanbaatar"
                      ],
                      [
                          "Osaka (+9:00)",
                          "Osaka"
                      ],
                      [
                          "Sapporo (+9:00)",
                          "Sapporo"
                      ],
                      [
                          "Seoul (+9:00)",
                          "Seoul"
                      ],
                      [
                          "Tokyo (+9:00)",
                          "Tokyo"
                      ],
                      [
                          "Yakutsk (+9:00)",
                          "Yakutsk"
                      ],
                      [
                          "Adelaide (+9:30)",
                          "Adelaide"
                      ],
                      [
                          "Darwin (+9:30)",
                          "Darwin"
                      ],
                      [
                          "Brisbane (+10:00)",
                          "Brisbane"
                      ],
                      [
                          "Canberra (+10:00)",
                          "Canberra"
                      ],
                      [
                          "Guam (+10:00)",
                          "Guam"
                      ],
                      [
                          "Hobart (+10:00)",
                          "Hobart"
                      ],
                      [
                          "Melbourne (+10:00)",
                          "Melbourne"
                      ],
                      [
                          "Port Moresby (+10:00)",
                          "Port Moresby"
                      ],
                      [
                          "Sydney (+10:00)",
                          "Sydney"
                      ],
                      [
                          "Vladivostok (+10:00)",
                          "Vladivostok"
                      ],
                      [
                          "Magadan (+11:00)",
                          "Magadan"
                      ],
                      [
                          "New Caledonia (+11:00)",
                          "New Caledonia"
                      ],
                      [
                          "Solomon Is. (+11:00)",
                          "Solomon Is."
                      ],
                      [
                          "Srednekolymsk (+11:00)",
                          "Srednekolymsk"
                      ],
                      [
                          "Auckland (+12:00)",
                          "Auckland"
                      ],
                      [
                          "Fiji (+12:00)",
                          "Fiji"
                      ],
                      [
                          "Kamchatka (+12:00)",
                          "Kamchatka"
                      ],
                      [
                          "Marshall Is. (+12:00)",
                          "Marshall Is."
                      ],
                      [
                          "Wellington (+12:00)",
                          "Wellington"
                      ],
                      [
                          "Chatham Is. (+12:45)",
                          "Chatham Is."
                      ],
                      [
                          "Nuku'alofa (+13:00)",
                          "Nuku'alofa"
                      ],
                      [
                          "Samoa (+13:00)",
                          "Samoa"
                      ],
                      [
                          "Tokelau Is. (+13:00)",
                          "Tokelau Is."
                      ]
                  ]
              },
              {
                  "name": "ignoreReadOnlyFields",
                  "type": "boolean",
                  "optional": true,
                  "label": "Ignore read-only fields",
                  "hint": "Ignore read-only fields in add and update operation? If set to <b>No</b>, the action will throw error on trying to write to read-only fields.",
                  "default": "false"
              },
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "properties": [
                    {
                        "name": "consumerKey",
                        "type": "string",
                        "label": "Consumer key"
                    },
                    {
                        "name": "consumerSecret",
                        "type": "string",
                        "label": "Consumer secret"
                    },
                  ]
              }
          ]
      }
```

* * *

### NetSuite (Secondary)

**Provider values:**

```json
"provider": "netsuite_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "account",
                  "type": "string",
                  "label": "Account ID",
                  "hint": "Login as Administrator, then in <b>Setup Menu</b>, find in <b>Integration</b> > <b>Web Services Preferences</b>"
              },
              {
                  "name": "tokenId",
                  "type": "string",
                  "label": "Token ID"
              },
              {
                  "name": "tokenSecret",
                  "type": "string",
                  "label": "Token secret"
              },
              {
                  "name": "timezone",
                  "type": "string",
                  "optional": true,
                  "label": "Account timezone",
                  "hint": "Needed for consistency with NetSuite - pick same as your NetSuite profile",
                  "pick_list":
                  [
                      [
                          "American Samoa (-11:00)",
                          "American Samoa"
                      ],
                      [
                          "International Date Line West (-11:00)",
                          "International Date Line West"
                      ],
                      [
                          "Midway Island (-11:00)",
                          "Midway Island"
                      ],
                      [
                          "Hawaii (-10:00)",
                          "Hawaii"
                      ],
                      [
                          "Alaska (-9:00)",
                          "Alaska"
                      ],
                      [
                          "Pacific Time (US & Canada) (-8:00)",
                          "Pacific Time (US & Canada)"
                      ],
                      [
                          "Tijuana (-8:00)",
                          "Tijuana"
                      ],
                      [
                          "Arizona (-7:00)",
                          "Arizona"
                      ],
                      [
                          "Chihuahua (-7:00)",
                          "Chihuahua"
                      ],
                      [
                          "Mazatlan (-7:00)",
                          "Mazatlan"
                      ],
                      [
                          "Mountain Time (US & Canada) (-7:00)",
                          "Mountain Time (US & Canada)"
                      ],
                      [
                          "Central America (-6:00)",
                          "Central America"
                      ],
                      [
                          "Central Time (US & Canada) (-6:00)",
                          "Central Time (US & Canada)"
                      ],
                      [
                          "Guadalajara (-6:00)",
                          "Guadalajara"
                      ],
                      [
                          "Mexico City (-6:00)",
                          "Mexico City"
                      ],
                      [
                          "Monterrey (-6:00)",
                          "Monterrey"
                      ],
                      [
                          "Saskatchewan (-6:00)",
                          "Saskatchewan"
                      ],
                      [
                          "Bogota (-5:00)",
                          "Bogota"
                      ],
                      [
                          "Eastern Time (US & Canada) (-5:00)",
                          "Eastern Time (US & Canada)"
                      ],
                      [
                          "Indiana (East) (-5:00)",
                          "Indiana (East)"
                      ],
                      [
                          "Lima (-5:00)",
                          "Lima"
                      ],
                      [
                          "Quito (-5:00)",
                          "Quito"
                      ],
                      [
                          "Atlantic Time (Canada) (-4:00)",
                          "Atlantic Time (Canada)"
                      ],
                      [
                          "Caracas (-4:00)",
                          "Caracas"
                      ],
                      [
                          "Georgetown (-4:00)",
                          "Georgetown"
                      ],
                      [
                          "La Paz (-4:00)",
                          "La Paz"
                      ],
                      [
                          "Santiago (-4:00)",
                          "Santiago"
                      ],
                      [
                          "Newfoundland (-4:30)",
                          "Newfoundland"
                      ],
                      [
                          "Brasilia (-3:00)",
                          "Brasilia"
                      ],
                      [
                          "Buenos Aires (-3:00)",
                          "Buenos Aires"
                      ],
                      [
                          "Greenland (-3:00)",
                          "Greenland"
                      ],
                      [
                          "Montevideo (-3:00)",
                          "Montevideo"
                      ],
                      [
                          "Mid-Atlantic (-2:00)",
                          "Mid-Atlantic"
                      ],
                      [
                          "Azores (-1:00)",
                          "Azores"
                      ],
                      [
                          "Cape Verde Is. (-1:00)",
                          "Cape Verde Is."
                      ],
                      [
                          "Casablanca (+0:00)",
                          "Casablanca"
                      ],
                      [
                          "Dublin (+0:00)",
                          "Dublin"
                      ],
                      [
                          "Edinburgh (+0:00)",
                          "Edinburgh"
                      ],
                      [
                          "Lisbon (+0:00)",
                          "Lisbon"
                      ],
                      [
                          "London (+0:00)",
                          "London"
                      ],
                      [
                          "Monrovia (+0:00)",
                          "Monrovia"
                      ],
                      [
                          "UTC (+0:00)",
                          "UTC"
                      ],
                      [
                          "Amsterdam (+1:00)",
                          "Amsterdam"
                      ],
                      [
                          "Belgrade (+1:00)",
                          "Belgrade"
                      ],
                      [
                          "Berlin (+1:00)",
                          "Berlin"
                      ],
                      [
                          "Bern (+1:00)",
                          "Bern"
                      ],
                      [
                          "Bratislava (+1:00)",
                          "Bratislava"
                      ],
                      [
                          "Brussels (+1:00)",
                          "Brussels"
                      ],
                      [
                          "Budapest (+1:00)",
                          "Budapest"
                      ],
                      [
                          "Copenhagen (+1:00)",
                          "Copenhagen"
                      ],
                      [
                          "Ljubljana (+1:00)",
                          "Ljubljana"
                      ],
                      [
                          "Madrid (+1:00)",
                          "Madrid"
                      ],
                      [
                          "Paris (+1:00)",
                          "Paris"
                      ],
                      [
                          "Prague (+1:00)",
                          "Prague"
                      ],
                      [
                          "Rome (+1:00)",
                          "Rome"
                      ],
                      [
                          "Sarajevo (+1:00)",
                          "Sarajevo"
                      ],
                      [
                          "Skopje (+1:00)",
                          "Skopje"
                      ],
                      [
                          "Stockholm (+1:00)",
                          "Stockholm"
                      ],
                      [
                          "Vienna (+1:00)",
                          "Vienna"
                      ],
                      [
                          "Warsaw (+1:00)",
                          "Warsaw"
                      ],
                      [
                          "West Central Africa (+1:00)",
                          "West Central Africa"
                      ],
                      [
                          "Zagreb (+1:00)",
                          "Zagreb"
                      ],
                      [
                          "Athens (+2:00)",
                          "Athens"
                      ],
                      [
                          "Bucharest (+2:00)",
                          "Bucharest"
                      ],
                      [
                          "Cairo (+2:00)",
                          "Cairo"
                      ],
                      [
                          "Harare (+2:00)",
                          "Harare"
                      ],
                      [
                          "Helsinki (+2:00)",
                          "Helsinki"
                      ],
                      [
                          "Jerusalem (+2:00)",
                          "Jerusalem"
                      ],
                      [
                          "Kaliningrad (+2:00)",
                          "Kaliningrad"
                      ],
                      [
                          "Kyiv (+2:00)",
                          "Kyiv"
                      ],
                      [
                          "Pretoria (+2:00)",
                          "Pretoria"
                      ],
                      [
                          "Riga (+2:00)",
                          "Riga"
                      ],
                      [
                          "Sofia (+2:00)",
                          "Sofia"
                      ],
                      [
                          "Tallinn (+2:00)",
                          "Tallinn"
                      ],
                      [
                          "Vilnius (+2:00)",
                          "Vilnius"
                      ],
                      [
                          "Baghdad (+3:00)",
                          "Baghdad"
                      ],
                      [
                          "Istanbul (+3:00)",
                          "Istanbul"
                      ],
                      [
                          "Kuwait (+3:00)",
                          "Kuwait"
                      ],
                      [
                          "Minsk (+3:00)",
                          "Minsk"
                      ],
                      [
                          "Moscow (+3:00)",
                          "Moscow"
                      ],
                      [
                          "Nairobi (+3:00)",
                          "Nairobi"
                      ],
                      [
                          "Riyadh (+3:00)",
                          "Riyadh"
                      ],
                      [
                          "St. Petersburg (+3:00)",
                          "St. Petersburg"
                      ],
                      [
                          "Tehran (+3:30)",
                          "Tehran"
                      ],
                      [
                          "Abu Dhabi (+4:00)",
                          "Abu Dhabi"
                      ],
                      [
                          "Baku (+4:00)",
                          "Baku"
                      ],
                      [
                          "Muscat (+4:00)",
                          "Muscat"
                      ],
                      [
                          "Samara (+4:00)",
                          "Samara"
                      ],
                      [
                          "Tbilisi (+4:00)",
                          "Tbilisi"
                      ],
                      [
                          "Volgograd (+4:00)",
                          "Volgograd"
                      ],
                      [
                          "Yerevan (+4:00)",
                          "Yerevan"
                      ],
                      [
                          "Kabul (+4:30)",
                          "Kabul"
                      ],
                      [
                          "Ekaterinburg (+5:00)",
                          "Ekaterinburg"
                      ],
                      [
                          "Islamabad (+5:00)",
                          "Islamabad"
                      ],
                      [
                          "Karachi (+5:00)",
                          "Karachi"
                      ],
                      [
                          "Tashkent (+5:00)",
                          "Tashkent"
                      ],
                      [
                          "Chennai (+5:30)",
                          "Chennai"
                      ],
                      [
                          "Kolkata (+5:30)",
                          "Kolkata"
                      ],
                      [
                          "Mumbai (+5:30)",
                          "Mumbai"
                      ],
                      [
                          "New Delhi (+5:30)",
                          "New Delhi"
                      ],
                      [
                          "Sri Jayawardenepura (+5:30)",
                          "Sri Jayawardenepura"
                      ],
                      [
                          "Kathmandu (+5:45)",
                          "Kathmandu"
                      ],
                      [
                          "Almaty (+6:00)",
                          "Almaty"
                      ],
                      [
                          "Astana (+6:00)",
                          "Astana"
                      ],
                      [
                          "Dhaka (+6:00)",
                          "Dhaka"
                      ],
                      [
                          "Urumqi (+6:00)",
                          "Urumqi"
                      ],
                      [
                          "Rangoon (+6:30)",
                          "Rangoon"
                      ],
                      [
                          "Bangkok (+7:00)",
                          "Bangkok"
                      ],
                      [
                          "Hanoi (+7:00)",
                          "Hanoi"
                      ],
                      [
                          "Jakarta (+7:00)",
                          "Jakarta"
                      ],
                      [
                          "Krasnoyarsk (+7:00)",
                          "Krasnoyarsk"
                      ],
                      [
                          "Novosibirsk (+7:00)",
                          "Novosibirsk"
                      ],
                      [
                          "Beijing (+8:00)",
                          "Beijing"
                      ],
                      [
                          "Chongqing (+8:00)",
                          "Chongqing"
                      ],
                      [
                          "Hong Kong (+8:00)",
                          "Hong Kong"
                      ],
                      [
                          "Irkutsk (+8:00)",
                          "Irkutsk"
                      ],
                      [
                          "Kuala Lumpur (+8:00)",
                          "Kuala Lumpur"
                      ],
                      [
                          "Perth (+8:00)",
                          "Perth"
                      ],
                      [
                          "Singapore (+8:00)",
                          "Singapore"
                      ],
                      [
                          "Taipei (+8:00)",
                          "Taipei"
                      ],
                      [
                          "Ulaanbaatar (+8:00)",
                          "Ulaanbaatar"
                      ],
                      [
                          "Osaka (+9:00)",
                          "Osaka"
                      ],
                      [
                          "Sapporo (+9:00)",
                          "Sapporo"
                      ],
                      [
                          "Seoul (+9:00)",
                          "Seoul"
                      ],
                      [
                          "Tokyo (+9:00)",
                          "Tokyo"
                      ],
                      [
                          "Yakutsk (+9:00)",
                          "Yakutsk"
                      ],
                      [
                          "Adelaide (+9:30)",
                          "Adelaide"
                      ],
                      [
                          "Darwin (+9:30)",
                          "Darwin"
                      ],
                      [
                          "Brisbane (+10:00)",
                          "Brisbane"
                      ],
                      [
                          "Canberra (+10:00)",
                          "Canberra"
                      ],
                      [
                          "Guam (+10:00)",
                          "Guam"
                      ],
                      [
                          "Hobart (+10:00)",
                          "Hobart"
                      ],
                      [
                          "Melbourne (+10:00)",
                          "Melbourne"
                      ],
                      [
                          "Port Moresby (+10:00)",
                          "Port Moresby"
                      ],
                      [
                          "Sydney (+10:00)",
                          "Sydney"
                      ],
                      [
                          "Vladivostok (+10:00)",
                          "Vladivostok"
                      ],
                      [
                          "Magadan (+11:00)",
                          "Magadan"
                      ],
                      [
                          "New Caledonia (+11:00)",
                          "New Caledonia"
                      ],
                      [
                          "Solomon Is. (+11:00)",
                          "Solomon Is."
                      ],
                      [
                          "Srednekolymsk (+11:00)",
                          "Srednekolymsk"
                      ],
                      [
                          "Auckland (+12:00)",
                          "Auckland"
                      ],
                      [
                          "Fiji (+12:00)",
                          "Fiji"
                      ],
                      [
                          "Kamchatka (+12:00)",
                          "Kamchatka"
                      ],
                      [
                          "Marshall Is. (+12:00)",
                          "Marshall Is."
                      ],
                      [
                          "Wellington (+12:00)",
                          "Wellington"
                      ],
                      [
                          "Chatham Is. (+12:45)",
                          "Chatham Is."
                      ],
                      [
                          "Nuku'alofa (+13:00)",
                          "Nuku'alofa"
                      ],
                      [
                          "Samoa (+13:00)",
                          "Samoa"
                      ],
                      [
                          "Tokelau Is. (+13:00)",
                          "Tokelau Is."
                      ]
                  ]
              },
              {
                  "name": "ignoreReadOnlyFields",
                  "type": "boolean",
                  "optional": true,
                  "label": "Ignore read-only fields",
                  "hint": "Ignore read-only fields in add and update operation? If set to <b>No</b>, the action will throw error on trying to write to read-only fields.",
                  "default": "false"
              },
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "properties": [
                    {
                        "name": "consumerKey",
                        "type": "string",
                        "label": "Consumer key"
                    },
                    {
                        "name": "consumerSecret",
                        "type": "string",
                        "label": "Consumer secret"
                    },
                  ]
              }
          ]
      }
```

* * *

### New Relic

**Provider values:**

```json
"provider": "new_relic"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "API Key",
                  "hint": "Go to Account settings->API Keys and get API key"
              }
          ]
      }
```

* * *

### Nimble CRM

**Provider values:**

```json
"provider": "nimblecrm"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Okta

**Provider values:**

```json
"provider": "okta"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "oauth_token_pair": {
    "label": "OAuth Token Pair",
    "optional": true,
    "type": "object",
    "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
    "properties": [
      {
        "label": "Access Token",
        "name": "access_token",
        "type": "string",
        "optional": false
      },
      {
        "label": "Refresh Token",
        "name": "refresh_token",
        "type": "string",
        "optional": false
      }
    ]
  },
  "input": [
    {
      "label": "Authentication type",
      "optional": false,
      "hint": "Select the authentication type to connect with Okta.",
      "type": "string",
      "name": "authentication_type",
      "default": "api_key",
      "pick_list": [
        [
          "Authorization code grant",
          "oauth2_auth_code_grant"
        ],
        [
          "Client credentials",
          "oauth2_client_credentials_grant"
        ],
        [
          "API key",
          "api_key"
        ]
      ]
    },
    {
      "label": "Okta domain",
      "hint": "Your Okta domain name as found in your Okta URL. For example: mycompany.okta.com, mytest.oktapreview.com.",
      "optional": false,
      "type": "string",
      "name": "subdomain"
    },
    {
      "label": "Client ID",
      "optional": false,
      "hint": "Refer to the following Okta documentation to obtain a client ID and client secret: https://developer.okta.com/docs/guides/implement-oauth-for-okta/main/#create-an-oauth-2-0-app-in-okta.",
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Client secret",
      "optional": false,
      "hint": "Refer to the following Okta documentation to obtain a client ID and client secret: https://developer.okta.com/docs/guides/implement-oauth-for-okta/main/#create-an-oauth-2-0-app-in-okta.",
      "type": "string",
      "name": "client_secret"
    },
    {
      "label": "Private key",
      "optional": false,
      "hint": "Enter the private key in PEM format. Refer to the Okta private key information to generate this value: https://developer.okta.com/docs/guides/implement-oauth-for-okta-serviceapp/main/#generate-the-jwk-using-the-admin-console",
      "type": "string",
      "name": "private_key"
    },
    {
      "label": "API Key",
      "optional": false,
      "hint": "Sign in to the Okta admin console as an administrator and go to Security > API > Create Token to create an API key.",
      "type": "string",
      "name": "api_key"
    },
    {
      "label": "Advanced settings",
      "optional": true,
      "type": "object",
      "name": "advanced_settings",
      "properties": [
        {
          "label": "OAuth 2.0 scopes",
          "optional": true,
          "hint": "Select OAuth 2.0 Scopes to request for this connection. Make sure to specify the required scopes based on the ones defined in Okta > Applications > Applications > Okta API Scopes. The selected scopes are added with okta.logs.read, okta.schemas.read, offline_access, openid which are minimal scopes required to establish connection with Okta. Ensure that okta.users.read is selected to connect using a custom role. The following default scopes are set if left blank: okta.logs.read, okta.schemas.read, offline_access, openid, okta.eventHooks.manage, okta.users.manage, okta.groups.manage, okta.apps.read. Refer to the Okta OAuth 2.0 documentation for more information: https://developer.okta.com/docs/api/oauth2/#oauth-20-scopes",
          "type": "string",
          "name": "scopes",
          "options": [
            [
              "okta.users.manage",
              "OKTA_USERS_MANAGE"
            ],
            [
              "okta.users.read",
              "OKTA_USERS_READ"
            ],
            [
              "okta.linkedObjects.manage",
              "OKTA_LINKEDOBJECTS_MANAGE"
            ],
            [
              "okta.linkedObjects.read",
              "OKTA_LINKEDOBJECTS_READ"
            ],
            [
              "okta.profileMappings.manage",
              "OKTA_PROFILEMAPPINGS_MANAGE"
            ],
            [
              "okta.profileMappings.read",
              "OKTA_PROFILEMAPPINGS_READ"
            ],
            [
              "okta.userTypes.manage",
              "OKTA_USERTYPES_MANAGE"
            ],
            [
              "okta.userTypes.read",
              "OKTA_USERTYPES_READ"
            ],
            [
              "okta.clients.manage",
              "OKTA_CLIENTS_MANAGE"
            ],
            [
              "okta.clients.register",
              "OKTA_CLIENTS_REGISTER"
            ],
            [
              "okta.clients.read",
              "OKTA_CLIENTS_READ"
            ],
            [
              "okta.appGrants.manage",
              "OKTA_APPGRANTS_MANAGE"
            ],
            [
              "okta.appGrants.read",
              "OKTA_APPGRANTS_READ"
            ],
            [
              "okta.policies.manage",
              "OKTA_POLICIES_MANAGE"
            ],
            [
              "okta.policies.read",
              "OKTA_POLICIES_READ"
            ],
            [
              "okta.groups.manage",
              "OKTA_GROUPS_MANAGE"
            ],
            [
              "okta.groups.read",
              "OKTA_GROUPS_READ"
            ],
            [
              "okta.inlineHooks.manage",
              "OKTA_INLINEHOOKS_MANAGE"
            ],
            [
              "okta.inlineHooks.read",
              "OKTA_INLINEHOOKS_READ"
            ],
            [
              "okta.eventHooks.manage",
              "OKTA_EVENTHOOKS_MANAGE"
            ],
            [
              "okta.eventHooks.read",
              "OKTA_EVENTHOOKS_READ"
            ],
            [
              "okta.events.read",
              "OKTA_EVENTS_READ"
            ],
            [
              "okta.apps.manage",
              "OKTA_APPS_MANAGE"
            ],
            [
              "okta.apps.read",
              "OKTA_APPS_READ"
            ],
            [
              "okta.schemas.manage",
              "OKTA_SCHEMAS_MANAGE"
            ],
            [
              "okta.idps.manage",
              "OKTA_IDPS_MANAGE"
            ],
            [
              "okta.idps.read",
              "OKTA_IDPS_READ"
            ],
            [
              "okta.factors.manage",
              "OKTA_FACTORS_MANAGE"
            ],
            [
              "okta.factors.read",
              "OKTA_FACTORS_READ"
            ],
            [
              "okta.riskProviders.manage",
              "OKTA_RISKPROVIDERS_MANAGE"
            ],
            [
              "okta.riskProviders.read",
              "OKTA_RISKPROVIDERS_READ"
            ],
            [
              "okta.roles.manage",
              "OKTA_ROLES_MANAGE"
            ],
            [
              "okta.roles.read",
              "OKTA_ROLES_READ"
            ],
            [
              "okta.domains.manage",
              "OKTA_DOMAINS_MANAGE"
            ],
            [
              "okta.domains.read",
              "OKTA_DOMAINS_READ"
            ],
            [
              "okta.brands.manage",
              "OKTA_BRANDS_MANAGE"
            ],
            [
              "okta.brands.read",
              "OKTA_BRANDS_READ"
            ],
            [
              "okta.sessions.manage",
              "OKTA_SESSIONS_MANAGE"
            ],
            [
              "okta.sessions.read",
              "OKTA_SESSIONS_READ"
            ],
            [
              "okta.templates.manage",
              "OKTA_TEMPLATES_MANAGE"
            ],
            [
              "okta.templates.read",
              "OKTA_TEMPLATES_READ"
            ],
            [
              "okta.trustedOrigins.manage",
              "OKTA_TRUSTEDORIGINS_MANAGE"
            ],
            [
              "okta.trustedOrigins.read",
              "OKTA_TRUSTEDORIGINS_READ"
            ],
            [
              "okta.threatInsights.manage",
              "OKTA_THREATINSIGHTS_MANAGE"
            ],
            [
              "okta.threatInsights.read",
              "OKTA_THREATINSIGHTS_READ"
            ],
            [
              "okta.behaviors.manage",
              "OKTA_BEHAVIORS_MANAGE"
            ],
            [
              "okta.behaviors.read",
              "OKTA_BEHAVIORS_READ"
            ],
            [
              "okta.networkZones.manage",
              "OKTA_NETWORKZONES_MANAGE"
            ],
            [
              "okta.networkZones.read",
              "OKTA_NETWORKZONES_READ"
            ],
            [
              "okta.agentPools.manage",
              "OKTA_AGENTPOOLS_MANAGE"
            ],
            [
              "okta.agentPools.read",
              "OKTA_AGENTPOOLS_READ"
            ],
            [
              "okta.reports.read",
              "OKTA_REPORTS_READ"
            ],
            [
              "okta.features.manage",
              "OKTA_FEATURES_MANAGE"
            ],
            [
              "okta.features.read",
              "OKTA_FEATURES_READ"
            ],
            [
              "okta.certificateAuthorities.manage",
              "OKTA_CERTIFICATEAUTHORITIES_MANAGE"
            ],
            [
              "okta.certificateAuthorities.read",
              "OKTA_CERTIFICATEAUTHORITIES_READ"
            ],
            [
              "okta.principalRateLimits.manage",
              "OKTA_PRINCIPALRATELIMITS_MANAGE"
            ],
            [
              "okta.principalRateLimits.read",
              "OKTA_PRINCIPALRATELIMITS_READ"
            ],
            [
              "okta.rateLimits.manage",
              "OKTA_RATELIMITS_MANAGE"
            ],
            [
              "okta.rateLimits.read",
              "OKTA_RATELIMITS_READ"
            ],
            [
              "okta.apiTokens.manage",
              "OKTA_APITOKENS_MANAGE"
            ],
            [
              "okta.apiTokens.read",
              "OKTA_APITOKENS_READ"
            ],
            [
              "okta.users.manage.self",
              "OKTA_USERS_MANAGE_SELF"
            ],
            [
              "okta.users.read.self",
              "OKTA_USERS_READ_SELF"
            ],
            [
              "email",
              "EMAIL"
            ],
            [
              "profile",
              "PROFILE"
            ],
            [
              "address",
              "ADDRESS"
            ],
            [
              "phone",
              "PHONE"
            ],
            [
              "groups",
              "GROUPS"
            ]
          ]
        },
        {
          "label": "Client credential scopes",
          "optional": true,
          "hint": "Select client credential scopes to request for this connection. Make sure to specify the required scopes based on the ones defined in Okta > Applications > Applications > Okta API Scopes. The selected scopes are added with okta.logs.read, okta.schemas.read which are minimal scopes required to establish connection with Okta. Ensure that okta.users.read is selected to connect using a custom role. The following default scopes are set if left blank: okta.logs.read, okta.schemas.read, okta.eventHooks.manage, okta.users.manage, okta.groups.manage, okta.apps.read. Refer to the Okta OAuth 2.0 documentation for more information: https://developer.okta.com/docs/api/oauth2/#oauth-20-scopes",
          "type": "string",
          "name": "client_credential_scopes",
          "options": [
            [
              "okta.users.manage",
              "OKTA_USERS_MANAGE"
            ],
            [
              "okta.users.read",
              "OKTA_USERS_READ"
            ],
            [
              "okta.linkedObjects.manage",
              "OKTA_LINKEDOBJECTS_MANAGE"
            ],
            [
              "okta.linkedObjects.read",
              "OKTA_LINKEDOBJECTS_READ"
            ],
            [
              "okta.profileMappings.manage",
              "OKTA_PROFILEMAPPINGS_MANAGE"
            ],
            [
              "okta.profileMappings.read",
              "OKTA_PROFILEMAPPINGS_READ"
            ],
            [
              "okta.userTypes.manage",
              "OKTA_USERTYPES_MANAGE"
            ],
            [
              "okta.userTypes.read",
              "OKTA_USERTYPES_READ"
            ],
            [
              "okta.clients.manage",
              "OKTA_CLIENTS_MANAGE"
            ],
            [
              "okta.clients.register",
              "OKTA_CLIENTS_REGISTER"
            ],
            [
              "okta.clients.read",
              "OKTA_CLIENTS_READ"
            ],
            [
              "okta.appGrants.manage",
              "OKTA_APPGRANTS_MANAGE"
            ],
            [
              "okta.appGrants.read",
              "OKTA_APPGRANTS_READ"
            ],
            [
              "okta.policies.manage",
              "OKTA_POLICIES_MANAGE"
            ],
            [
              "okta.policies.read",
              "OKTA_POLICIES_READ"
            ],
            [
              "okta.groups.manage",
              "OKTA_GROUPS_MANAGE"
            ],
            [
              "okta.groups.read",
              "OKTA_GROUPS_READ"
            ],
            [
              "okta.inlineHooks.manage",
              "OKTA_INLINEHOOKS_MANAGE"
            ],
            [
              "okta.inlineHooks.read",
              "OKTA_INLINEHOOKS_READ"
            ],
            [
              "okta.eventHooks.manage",
              "OKTA_EVENTHOOKS_MANAGE"
            ],
            [
              "okta.eventHooks.read",
              "OKTA_EVENTHOOKS_READ"
            ],
            [
              "okta.events.read",
              "OKTA_EVENTS_READ"
            ],
            [
              "okta.apps.manage",
              "OKTA_APPS_MANAGE"
            ],
            [
              "okta.apps.read",
              "OKTA_APPS_READ"
            ],
            [
              "okta.schemas.manage",
              "OKTA_SCHEMAS_MANAGE"
            ],
            [
              "okta.idps.manage",
              "OKTA_IDPS_MANAGE"
            ],
            [
              "okta.idps.read",
              "OKTA_IDPS_READ"
            ],
            [
              "okta.factors.manage",
              "OKTA_FACTORS_MANAGE"
            ],
            [
              "okta.factors.read",
              "OKTA_FACTORS_READ"
            ],
            [
              "okta.riskProviders.manage",
              "OKTA_RISKPROVIDERS_MANAGE"
            ],
            [
              "okta.riskProviders.read",
              "OKTA_RISKPROVIDERS_READ"
            ],
            [
              "okta.roles.manage",
              "OKTA_ROLES_MANAGE"
            ],
            [
              "okta.roles.read",
              "OKTA_ROLES_READ"
            ],
            [
              "okta.domains.manage",
              "OKTA_DOMAINS_MANAGE"
            ],
            [
              "okta.domains.read",
              "OKTA_DOMAINS_READ"
            ],
            [
              "okta.brands.manage",
              "OKTA_BRANDS_MANAGE"
            ],
            [
              "okta.brands.read",
              "OKTA_BRANDS_READ"
            ],
            [
              "okta.sessions.manage",
              "OKTA_SESSIONS_MANAGE"
            ],
            [
              "okta.sessions.read",
              "OKTA_SESSIONS_READ"
            ],
            [
              "okta.templates.manage",
              "OKTA_TEMPLATES_MANAGE"
            ],
            [
              "okta.templates.read",
              "OKTA_TEMPLATES_READ"
            ],
            [
              "okta.trustedOrigins.manage",
              "OKTA_TRUSTEDORIGINS_MANAGE"
            ],
            [
              "okta.trustedOrigins.read",
              "OKTA_TRUSTEDORIGINS_READ"
            ],
            [
              "okta.threatInsights.manage",
              "OKTA_THREATINSIGHTS_MANAGE"
            ],
            [
              "okta.threatInsights.read",
              "OKTA_THREATINSIGHTS_READ"
            ],
            [
              "okta.behaviors.manage",
              "OKTA_BEHAVIORS_MANAGE"
            ],
            [
              "okta.behaviors.read",
              "OKTA_BEHAVIORS_READ"
            ],
            [
              "okta.networkZones.manage",
              "OKTA_NETWORKZONES_MANAGE"
            ],
            [
              "okta.networkZones.read",
              "OKTA_NETWORKZONES_READ"
            ],
            [
              "okta.agentPools.manage",
              "OKTA_AGENTPOOLS_MANAGE"
            ],
            [
              "okta.agentPools.read",
              "OKTA_AGENTPOOLS_READ"
            ],
            [
              "okta.reports.read",
              "OKTA_REPORTS_READ"
            ],
            [
              "okta.features.manage",
              "OKTA_FEATURES_MANAGE"
            ],
            [
              "okta.features.read",
              "OKTA_FEATURES_READ"
            ],
            [
              "okta.certificateAuthorities.manage",
              "OKTA_CERTIFICATEAUTHORITIES_MANAGE"
            ],
            [
              "okta.certificateAuthorities.read",
              "OKTA_CERTIFICATEAUTHORITIES_READ"
            ],
            [
              "okta.principalRateLimits.manage",
              "OKTA_PRINCIPALRATELIMITS_MANAGE"
            ],
            [
              "okta.principalRateLimits.read",
              "OKTA_PRINCIPALRATELIMITS_READ"
            ],
            [
              "okta.rateLimits.manage",
              "OKTA_RATELIMITS_MANAGE"
            ],
            [
              "okta.rateLimits.read",
              "OKTA_RATELIMITS_READ"
            ],
            [
              "okta.apiTokens.manage",
              "OKTA_APITOKENS_MANAGE"
            ],
            [
              "okta.apiTokens.read",
              "OKTA_APITOKENS_READ"
            ]
          ]
        }
      ]
    }
  ]
}
```

* * *

### Okta (Secondary)

**Provider values:**

```json
"provider": "okta_secondary"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "oauth_token_pair": {
    "label": "OAuth Token Pair",
    "optional": true,
    "type": "object",
    "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
    "properties": [
      {
        "label": "Access Token",
        "name": "access_token",
        "type": "string",
        "optional": false
      },
      {
        "label": "Refresh Token",
        "name": "refresh_token",
        "type": "string",
        "optional": false
      }
    ]
  },
  "input": [
    {
      "label": "Authentication type",
      "optional": false,
      "hint": "Select the authentication type to connect with Okta.",
      "type": "string",
      "name": "authentication_type",
      "default": "api_key",
      "pick_list": [
        [
          "Authorization code grant",
          "oauth2_auth_code_grant"
        ],
        [
          "Client credentials",
          "oauth2_client_credentials_grant"
        ],
        [
          "API key",
          "api_key"
        ]
      ]
    },
    {
      "label": "Okta domain",
      "hint": "Your Okta domain name as found in your Okta URL. For example: mycompany.okta.com, mytest.oktapreview.com.",
      "optional": false,
      "type": "string",
      "name": "subdomain"
    },
    {
      "label": "Client ID",
      "optional": false,
      "hint": "Refer to the following Okta documentation to obtain a client ID and client secret: https://developer.okta.com/docs/guides/implement-oauth-for-okta/main/#create-an-oauth-2-0-app-in-okta.",
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Client secret",
      "optional": false,
      "hint": "Refer to the following Okta documentation to obtain a client ID and client secret: https://developer.okta.com/docs/guides/implement-oauth-for-okta/main/#create-an-oauth-2-0-app-in-okta.",
      "type": "string",
      "name": "client_secret"
    },
    {
      "label": "Private key",
      "optional": false,
      "hint": "Enter the private key in PEM format. Refer to the Okta private key information to generate this value: https://developer.okta.com/docs/guides/implement-oauth-for-okta-serviceapp/main/#generate-the-jwk-using-the-admin-console",
      "type": "string",
      "name": "private_key"
    },
    {
      "label": "API Key",
      "optional": false,
      "hint": "Sign in to the Okta admin console as an administrator and go to Security > API > Create Token to create an API key.",
      "type": "string",
      "name": "api_key"
    },
    {
      "label": "Advanced settings",
      "optional": true,
      "type": "object",
      "name": "advanced_settings",
      "properties": [
        {
          "label": "OAuth 2.0 scopes",
          "optional": true,
          "hint": "Select OAuth 2.0 Scopes to request for this connection. Make sure to specify the required scopes based on the ones defined in Okta > Applications > Applications > Okta API Scopes. The selected scopes are added with okta.logs.read, okta.schemas.read, offline_access, openid which are minimal scopes required to establish connection with Okta. Ensure that okta.users.read is selected to connect using a custom role. The following default scopes are set if left blank: okta.logs.read, okta.schemas.read, offline_access, openid, okta.eventHooks.manage, okta.users.manage, okta.groups.manage, okta.apps.read. Refer to the Okta OAuth 2.0 documentation for more information: https://developer.okta.com/docs/api/oauth2/#oauth-20-scopes",
          "type": "string",
          "name": "scopes",
          "options": [
            [
              "okta.users.manage",
              "OKTA_USERS_MANAGE"
            ],
            [
              "okta.users.read",
              "OKTA_USERS_READ"
            ],
            [
              "okta.linkedObjects.manage",
              "OKTA_LINKEDOBJECTS_MANAGE"
            ],
            [
              "okta.linkedObjects.read",
              "OKTA_LINKEDOBJECTS_READ"
            ],
            [
              "okta.profileMappings.manage",
              "OKTA_PROFILEMAPPINGS_MANAGE"
            ],
            [
              "okta.profileMappings.read",
              "OKTA_PROFILEMAPPINGS_READ"
            ],
            [
              "okta.userTypes.manage",
              "OKTA_USERTYPES_MANAGE"
            ],
            [
              "okta.userTypes.read",
              "OKTA_USERTYPES_READ"
            ],
            [
              "okta.clients.manage",
              "OKTA_CLIENTS_MANAGE"
            ],
            [
              "okta.clients.register",
              "OKTA_CLIENTS_REGISTER"
            ],
            [
              "okta.clients.read",
              "OKTA_CLIENTS_READ"
            ],
            [
              "okta.appGrants.manage",
              "OKTA_APPGRANTS_MANAGE"
            ],
            [
              "okta.appGrants.read",
              "OKTA_APPGRANTS_READ"
            ],
            [
              "okta.policies.manage",
              "OKTA_POLICIES_MANAGE"
            ],
            [
              "okta.policies.read",
              "OKTA_POLICIES_READ"
            ],
            [
              "okta.groups.manage",
              "OKTA_GROUPS_MANAGE"
            ],
            [
              "okta.groups.read",
              "OKTA_GROUPS_READ"
            ],
            [
              "okta.inlineHooks.manage",
              "OKTA_INLINEHOOKS_MANAGE"
            ],
            [
              "okta.inlineHooks.read",
              "OKTA_INLINEHOOKS_READ"
            ],
            [
              "okta.eventHooks.manage",
              "OKTA_EVENTHOOKS_MANAGE"
            ],
            [
              "okta.eventHooks.read",
              "OKTA_EVENTHOOKS_READ"
            ],
            [
              "okta.events.read",
              "OKTA_EVENTS_READ"
            ],
            [
              "okta.apps.manage",
              "OKTA_APPS_MANAGE"
            ],
            [
              "okta.apps.read",
              "OKTA_APPS_READ"
            ],
            [
              "okta.schemas.manage",
              "OKTA_SCHEMAS_MANAGE"
            ],
            [
              "okta.idps.manage",
              "OKTA_IDPS_MANAGE"
            ],
            [
              "okta.idps.read",
              "OKTA_IDPS_READ"
            ],
            [
              "okta.factors.manage",
              "OKTA_FACTORS_MANAGE"
            ],
            [
              "okta.factors.read",
              "OKTA_FACTORS_READ"
            ],
            [
              "okta.riskProviders.manage",
              "OKTA_RISKPROVIDERS_MANAGE"
            ],
            [
              "okta.riskProviders.read",
              "OKTA_RISKPROVIDERS_READ"
            ],
            [
              "okta.roles.manage",
              "OKTA_ROLES_MANAGE"
            ],
            [
              "okta.roles.read",
              "OKTA_ROLES_READ"
            ],
            [
              "okta.domains.manage",
              "OKTA_DOMAINS_MANAGE"
            ],
            [
              "okta.domains.read",
              "OKTA_DOMAINS_READ"
            ],
            [
              "okta.brands.manage",
              "OKTA_BRANDS_MANAGE"
            ],
            [
              "okta.brands.read",
              "OKTA_BRANDS_READ"
            ],
            [
              "okta.sessions.manage",
              "OKTA_SESSIONS_MANAGE"
            ],
            [
              "okta.sessions.read",
              "OKTA_SESSIONS_READ"
            ],
            [
              "okta.templates.manage",
              "OKTA_TEMPLATES_MANAGE"
            ],
            [
              "okta.templates.read",
              "OKTA_TEMPLATES_READ"
            ],
            [
              "okta.trustedOrigins.manage",
              "OKTA_TRUSTEDORIGINS_MANAGE"
            ],
            [
              "okta.trustedOrigins.read",
              "OKTA_TRUSTEDORIGINS_READ"
            ],
            [
              "okta.threatInsights.manage",
              "OKTA_THREATINSIGHTS_MANAGE"
            ],
            [
              "okta.threatInsights.read",
              "OKTA_THREATINSIGHTS_READ"
            ],
            [
              "okta.behaviors.manage",
              "OKTA_BEHAVIORS_MANAGE"
            ],
            [
              "okta.behaviors.read",
              "OKTA_BEHAVIORS_READ"
            ],
            [
              "okta.networkZones.manage",
              "OKTA_NETWORKZONES_MANAGE"
            ],
            [
              "okta.networkZones.read",
              "OKTA_NETWORKZONES_READ"
            ],
            [
              "okta.agentPools.manage",
              "OKTA_AGENTPOOLS_MANAGE"
            ],
            [
              "okta.agentPools.read",
              "OKTA_AGENTPOOLS_READ"
            ],
            [
              "okta.reports.read",
              "OKTA_REPORTS_READ"
            ],
            [
              "okta.features.manage",
              "OKTA_FEATURES_MANAGE"
            ],
            [
              "okta.features.read",
              "OKTA_FEATURES_READ"
            ],
            [
              "okta.certificateAuthorities.manage",
              "OKTA_CERTIFICATEAUTHORITIES_MANAGE"
            ],
            [
              "okta.certificateAuthorities.read",
              "OKTA_CERTIFICATEAUTHORITIES_READ"
            ],
            [
              "okta.principalRateLimits.manage",
              "OKTA_PRINCIPALRATELIMITS_MANAGE"
            ],
            [
              "okta.principalRateLimits.read",
              "OKTA_PRINCIPALRATELIMITS_READ"
            ],
            [
              "okta.rateLimits.manage",
              "OKTA_RATELIMITS_MANAGE"
            ],
            [
              "okta.rateLimits.read",
              "OKTA_RATELIMITS_READ"
            ],
            [
              "okta.apiTokens.manage",
              "OKTA_APITOKENS_MANAGE"
            ],
            [
              "okta.apiTokens.read",
              "OKTA_APITOKENS_READ"
            ],
            [
              "okta.users.manage.self",
              "OKTA_USERS_MANAGE_SELF"
            ],
            [
              "okta.users.read.self",
              "OKTA_USERS_READ_SELF"
            ],
            [
              "email",
              "EMAIL"
            ],
            [
              "profile",
              "PROFILE"
            ],
            [
              "address",
              "ADDRESS"
            ],
            [
              "phone",
              "PHONE"
            ],
            [
              "groups",
              "GROUPS"
            ]
          ]
        },
        {
          "label": "Client credential scopes",
          "optional": true,
          "hint": "Select client credential scopes to request for this connection. Make sure to specify the required scopes based on the ones defined in Okta > Applications > Applications > Okta API Scopes. The selected scopes are added with okta.logs.read, okta.schemas.read which are minimal scopes required to establish connection with Okta. Ensure that okta.users.read is selected to connect using a custom role. The following default scopes are set if left blank: okta.logs.read, okta.schemas.read, okta.eventHooks.manage, okta.users.manage, okta.groups.manage, okta.apps.read. Refer to the Okta OAuth 2.0 documentation for more information: https://developer.okta.com/docs/api/oauth2/#oauth-20-scopes",
          "type": "string",
          "name": "client_credential_scopes",
          "options": [
            [
              "okta.users.manage",
              "OKTA_USERS_MANAGE"
            ],
            [
              "okta.users.read",
              "OKTA_USERS_READ"
            ],
            [
              "okta.linkedObjects.manage",
              "OKTA_LINKEDOBJECTS_MANAGE"
            ],
            [
              "okta.linkedObjects.read",
              "OKTA_LINKEDOBJECTS_READ"
            ],
            [
              "okta.profileMappings.manage",
              "OKTA_PROFILEMAPPINGS_MANAGE"
            ],
            [
              "okta.profileMappings.read",
              "OKTA_PROFILEMAPPINGS_READ"
            ],
            [
              "okta.userTypes.manage",
              "OKTA_USERTYPES_MANAGE"
            ],
            [
              "okta.userTypes.read",
              "OKTA_USERTYPES_READ"
            ],
            [
              "okta.clients.manage",
              "OKTA_CLIENTS_MANAGE"
            ],
            [
              "okta.clients.register",
              "OKTA_CLIENTS_REGISTER"
            ],
            [
              "okta.clients.read",
              "OKTA_CLIENTS_READ"
            ],
            [
              "okta.appGrants.manage",
              "OKTA_APPGRANTS_MANAGE"
            ],
            [
              "okta.appGrants.read",
              "OKTA_APPGRANTS_READ"
            ],
            [
              "okta.policies.manage",
              "OKTA_POLICIES_MANAGE"
            ],
            [
              "okta.policies.read",
              "OKTA_POLICIES_READ"
            ],
            [
              "okta.groups.manage",
              "OKTA_GROUPS_MANAGE"
            ],
            [
              "okta.groups.read",
              "OKTA_GROUPS_READ"
            ],
            [
              "okta.inlineHooks.manage",
              "OKTA_INLINEHOOKS_MANAGE"
            ],
            [
              "okta.inlineHooks.read",
              "OKTA_INLINEHOOKS_READ"
            ],
            [
              "okta.eventHooks.manage",
              "OKTA_EVENTHOOKS_MANAGE"
            ],
            [
              "okta.eventHooks.read",
              "OKTA_EVENTHOOKS_READ"
            ],
            [
              "okta.events.read",
              "OKTA_EVENTS_READ"
            ],
            [
              "okta.apps.manage",
              "OKTA_APPS_MANAGE"
            ],
            [
              "okta.apps.read",
              "OKTA_APPS_READ"
            ],
            [
              "okta.schemas.manage",
              "OKTA_SCHEMAS_MANAGE"
            ],
            [
              "okta.idps.manage",
              "OKTA_IDPS_MANAGE"
            ],
            [
              "okta.idps.read",
              "OKTA_IDPS_READ"
            ],
            [
              "okta.factors.manage",
              "OKTA_FACTORS_MANAGE"
            ],
            [
              "okta.factors.read",
              "OKTA_FACTORS_READ"
            ],
            [
              "okta.riskProviders.manage",
              "OKTA_RISKPROVIDERS_MANAGE"
            ],
            [
              "okta.riskProviders.read",
              "OKTA_RISKPROVIDERS_READ"
            ],
            [
              "okta.roles.manage",
              "OKTA_ROLES_MANAGE"
            ],
            [
              "okta.roles.read",
              "OKTA_ROLES_READ"
            ],
            [
              "okta.domains.manage",
              "OKTA_DOMAINS_MANAGE"
            ],
            [
              "okta.domains.read",
              "OKTA_DOMAINS_READ"
            ],
            [
              "okta.brands.manage",
              "OKTA_BRANDS_MANAGE"
            ],
            [
              "okta.brands.read",
              "OKTA_BRANDS_READ"
            ],
            [
              "okta.sessions.manage",
              "OKTA_SESSIONS_MANAGE"
            ],
            [
              "okta.sessions.read",
              "OKTA_SESSIONS_READ"
            ],
            [
              "okta.templates.manage",
              "OKTA_TEMPLATES_MANAGE"
            ],
            [
              "okta.templates.read",
              "OKTA_TEMPLATES_READ"
            ],
            [
              "okta.trustedOrigins.manage",
              "OKTA_TRUSTEDORIGINS_MANAGE"
            ],
            [
              "okta.trustedOrigins.read",
              "OKTA_TRUSTEDORIGINS_READ"
            ],
            [
              "okta.threatInsights.manage",
              "OKTA_THREATINSIGHTS_MANAGE"
            ],
            [
              "okta.threatInsights.read",
              "OKTA_THREATINSIGHTS_READ"
            ],
            [
              "okta.behaviors.manage",
              "OKTA_BEHAVIORS_MANAGE"
            ],
            [
              "okta.behaviors.read",
              "OKTA_BEHAVIORS_READ"
            ],
            [
              "okta.networkZones.manage",
              "OKTA_NETWORKZONES_MANAGE"
            ],
            [
              "okta.networkZones.read",
              "OKTA_NETWORKZONES_READ"
            ],
            [
              "okta.agentPools.manage",
              "OKTA_AGENTPOOLS_MANAGE"
            ],
            [
              "okta.agentPools.read",
              "OKTA_AGENTPOOLS_READ"
            ],
            [
              "okta.reports.read",
              "OKTA_REPORTS_READ"
            ],
            [
              "okta.features.manage",
              "OKTA_FEATURES_MANAGE"
            ],
            [
              "okta.features.read",
              "OKTA_FEATURES_READ"
            ],
            [
              "okta.certificateAuthorities.manage",
              "OKTA_CERTIFICATEAUTHORITIES_MANAGE"
            ],
            [
              "okta.certificateAuthorities.read",
              "OKTA_CERTIFICATEAUTHORITIES_READ"
            ],
            [
              "okta.principalRateLimits.manage",
              "OKTA_PRINCIPALRATELIMITS_MANAGE"
            ],
            [
              "okta.principalRateLimits.read",
              "OKTA_PRINCIPALRATELIMITS_READ"
            ],
            [
              "okta.rateLimits.manage",
              "OKTA_RATELIMITS_MANAGE"
            ],
            [
              "okta.rateLimits.read",
              "OKTA_RATELIMITS_READ"
            ],
            [
              "okta.apiTokens.manage",
              "OKTA_APITOKENS_MANAGE"
            ],
            [
              "okta.apiTokens.read",
              "OKTA_APITOKENS_READ"
            ]
          ]
        }
      ]
    }
  ]
}
```

* * *

### On-prem command-line scripts

**Provider values:**

```json
"provider": "onprem_command_line_scripts"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem command-line scripts profile",
                  "hint": "Profile name given in the <b>config.yml</b> file"
              }
          ]
      }
```

* * *

### On-prem files

**Provider values:**

```json
"provider": "onprem_files"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile",
                  "hint": "Profile name given in the <b>config.yml</b> file"
              }
          ]
      }
```

* * *

### On-prem files (Secondary)

**Provider values:**

```json
"provider": "onprem_files_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile",
                  "hint": "Profile name given in the <b>config.yml</b> file"
              }
          ]
      }
```

* * *

### OneDrive

**Provider values:**

```json
"provider": "onedrive"
```

View connection parameters reference

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "account_type",
                  "type": "string",
                  "optional": false,
                  "label": "Account type",
                  "hint": "Select your Onedrive account type",
                  "pick_list":
                  [
                      [
                          "Personal",
                          "personal"
                      ],
                      [
                          "Business",
                          "business"
                      ]
                  ],
                  "default": "personal"
              }
          ]
      }
```

* * *

### Oracle

**Provider values:**

```json
"provider": "oracle"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Database host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "optional": true,
                  "label": "Database port",
                  "hint": "Port number, default is 1521",
                  "default": 1521
              },
              {
                  "name": "user",
                  "type": "string",
                  "label": "User name"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": true,
                  "label": "Password"
              },
              {
                  "name": "dbname",
                  "type": "string",
                  "label": "Database name"
              }
          ]
      }
```

* * *

### Oracle (Secondary)

**Provider values:**

```json
"provider": "oracle_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Database host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "optional": true,
                  "label": "Database port",
                  "hint": "Port number, default is 1521",
                  "default": 1521
              },
              {
                  "name": "user",
                  "type": "string",
                  "label": "User name"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": true,
                  "label": "Password"
              },
              {
                  "name": "dbname",
                  "type": "string",
                  "label": "Database name"
              }
          ]
      }
```

* * *

### Oracle E-Business Suite

**Provider values:**

```json
"provider": "oracle_ebs"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "instance_url",
                  "type": "string",
                  "label": "Instance URL",
                  "hint": "URL of the instance. Eg: 'https://oracleebs.mycompany.com:8000/'. <br>\nDeploy User PL/SQL service (internal name: FND_USER_PKG) with service name as 'user'\n"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "user_service_name",
                  "type": "string",
                  "label": "User service name",
                  "hint": "Name of the PL/SQL REST service name used while deployment"
              }
          ]
      }
```

* * *

### Oracle Fusion

**Provider values:**

```json
"provider": "oracle_fusion"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "user",
                  "type": "string",
                  "label": "User"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              }
          ]
      }
```

* * *

### Outlook

**Provider values:**

```json
"provider": "outlook"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced settings",
                  "properties":
                  [
                      {
                          "name": "api_scope",
                          "type": "string",
                          "optional": true,
                          "label": "Requested permissions (Oauth scopes)",
                          "hint": "                     Select <a href=\"https://docs.microsoft.com/en-us/graph/permissions-reference#mail-permissions\" target=\"_blank\">permissions</a>\n                     to request for this connection. Defaults to minimum permissions if left blank.\n                     Minimum permissions required are <b>mail.read</b>, <b>mail.send</b>, <b>calendars.readwrite</b>, <b>offline_access</b>, <b>mail.Read.Shared</b>;\n                     these are requested in addition to selected permissions.\n"
                      }
                  ]
              }
          ]
      }
```

* * *

### Outreach

**Provider values:**

```json
"provider": "outreach"
```

* * *

### OutSystems

**Provider values:**

```json
"provider": "out_systems"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "API_key",
                  "type": "string",
                  "optional": false,
                  "label": "API key",
                  "hint": "Type in an API key generated using the security configuration page, on the <b>OutSystems Workato Connector</b>. If you don't have the <b>OutSystems Workato Connector</b> installed on your server, please get it from the <a href='https://www.outsystems.com/forge/' target='_blank'>OutSystems Forge</a>."
              },
              {
                  "name": "EnvironmentURL",
                  "type": "string",
                  "optional": false,
                  "label": "Environment URL",
                  "hint": "Your OutSystems environment URL (eg: YOUR_PERSONAL.outsystemscloud.com)."
              }
          ]
      }
```

* * *

### Pagerduty

**Provider values:**

```json
"provider": "pagerduty"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "API key",
                  "hint": "Go to Configuration -> API Access and get API Key"
              }
          ]
      }
```

* * *

### ParseHub

**Provider values:**

```json
"provider": "parsehub"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "Api key",
                  "hint": "Select your ParseHub account name-> Select Account-> Get your api key"
              }
          ]
      }
```

* * *

### Percolate

**Provider values:**

```json
"provider": "percolate"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "client_id",
                  "type": "string",
                  "optional": false,
                  "label": "Client ID",
                  "hint": "To create client ID, the system admin or manager can click <a href='https://percolate.com/app/settings/developer/apps/new' target='_blank'>here</a> to register a new client application."
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "optional": false,
                  "label": "Client secret",
                  "hint": "To create client secret, the system admin or manager can click <a href='https://percolate.com/app/settings/developer/apps/new' target='_blank'>here</a> to register a new client application."
              },
              {
                  "name": "environment",
                  "type": "string",
                  "optional": false,
                  "label": "Environment",
                  "pick_list":
                  [
                      [
                          "Production",
                          "production"
                      ],
                      [
                          "Sandbox",
                          "sandbox"
                      ],
                      [
                          "Internal",
                          "internal"
                      ]
                  ]
              }
          ]
      }
```

* * *

### PGP

**Provider values:**

```json
"provider": "pgp"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "public_key",
                  "type": "string",
                  "optional": true,
                  "label": "Public key (deprecated)",
                  "hint": "Provide the public key in Encrypt and Verify action input."
              },
              {
                  "name": "private_key",
                  "type": "string",
                  "optional": true,
                  "label": "Private key",
                  "hint": "Private is required for decrypt and sign actions. Learn how to generate a pair of Public key and Private key\n<a href=\"https://docs.workato.com/features/pgp-encryption.html\" target=\"_blank\">here</a>.\n"
              },
              {
                  "name": "passphrase",
                  "type": "string",
                  "optional": true,
                  "label": "Passphrase",
                  "hint": "Passphrase of the keys you have generated."
              }
          ]
      }
```

* * *

### Pingdom

**Provider value:**

```json
"provider": "pingdom"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "app_key",
                  "type": "string",
                  "optional": false,
                  "label": "Application key"
              },
              {
                  "name": "username",
                  "type": "string",
                  "optional": false,
                  "label": "Username",
                  "hint": "Your username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": false,
                  "label": "Password"
              }
          ]
      }
```

* * *

### Pipedrive

**Provider value:**

```json
"provider": "pipedrive"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_token",
                  "type": "string",
                  "label": "Api token",
                  "hint": "API token is found in the API tab under Personal settings (Settings > Personal > API)"
              }
          ]
      }
```

* * *

### Pivotal Tracker

**Provider value:**

```json
"provider": "pivotal_tracker"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": true,
                  "label": "API key",
                  "hint": "Select your account name -> Profile. Scroll down to end of the page to get API token"
              }
          ]
      }
```

* * *

### PlanGrid

**Provider value:**

```json
"provider": "plan_grid"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Podio

**Provider value:**

```json
"provider": "podio"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### PostgreSQL

**Provider value:**

```json
"provider": "postgresql"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Database host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "label": "Database port"
              },
              {
                  "name": "user",
                  "type": "string",
                  "label": "User name"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": true,
                  "label": "Password"
              },
              {
                  "name": "dbname",
                  "type": "string",
                  "label": "Database name"
              },
              {
                  "name": "schema_name",
                  "type": "string",
                  "optional": true,
                  "label": "Schema",
                  "hint": "\"public\" schema by default"
              }
          ]
      }
```

### PostgreSQL (Secondary)

**Provider value:**

```json
"provider": "postgresql_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Database host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "label": "Database port"
              },
              {
                  "name": "user",
                  "type": "string",
                  "label": "User name"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": true,
                  "label": "Password"
              },
              {
                  "name": "dbname",
                  "type": "string",
                  "label": "Database name"
              },
              {
                  "name": "schema_name",
                  "type": "string",
                  "optional": true,
                  "label": "Schema",
                  "hint": "\"public\" schema by default"
              }
          ]
      }
```

* * *

### Product Hunt

**Provider value:**

```json
"provider": "product_hunt"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "username",
                  "type": "string",
                  "optional": false,
                  "label": "Username",
                  "hint": "Your Product Hunt Username. Remove \"@\" prefix."
              }
          ]
      }
```

* * *

### Prontoforms

**Provider value:**

```json
"provider": "prontoforms"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "Api key"
              },
              {
                  "name": "api_secret",
                  "type": "string",
                  "label": "Api secret"
              }
          ]
      }
```

* * *

### Propel

**Provider value:**

```json
"provider": "propel"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### PubSub by Workato

**Provider value:**

```json
"provider": "workato_pub_sub"
```

* * *

### Quick Base

**Provider value:**

```json
"provider": "quickbase"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Sub-domain",
                  "hint": "Your Quick Base subdomain is most often your company name"
              },
              {
                  "name": "user_token_auth",
                  "type": "boolean",
                  "label": "User-token authentication?",
                  "hint": "Is authentication based on user tokens? If yes, provide <b>User token</b>. If no, provide <b>Username</b> & <b>Password</b>.",
                  "default": "false"
              },
              {
                  "name": "usertoken",
                  "type": "string",
                  "optional": true,
                  "label": "User token",
                  "hint": "Get/create user token by clicking on <b>Your profile > My preferences > Manage User Tokens</b>. <a href='https://help.quickbase.com/api-guide/manage_user_tokens.html' target='_blank' >Learn more</a>"
              },
              {
                  "name": "username",
                  "type": "string",
                  "optional": true,
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": true,
                  "label": "Password"
              }
          ]
      }
```

* * *

### Quick Base (Secondary)

**Provider value:**

```json
"provider": "quickbase_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Sub-domain",
                  "hint": "Your Quick Base subdomain is most often your company name"
              },
              {
                  "name": "user_token_auth",
                  "type": "boolean",
                  "label": "User-token authentication?",
                  "hint": "Is authentication based on user tokens? If yes, provide <b>User token</b>. If no, provide <b>Username</b> & <b>Password</b>.",
                  "default": "false"
              },
              {
                  "name": "usertoken",
                  "type": "string",
                  "optional": true,
                  "label": "User token",
                  "hint": "Get/create user token by clicking on <b>Your profile > My preferences > Manage User Tokens</b>. <a href='https://help.quickbase.com/api-guide/manage_user_tokens.html' target='_blank' >Learn more</a>"
              },
              {
                  "name": "username",
                  "type": "string",
                  "optional": true,
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": true,
                  "label": "Password"
              }
          ]
      }
```

* * *

### QuickBooks Online

**Provider value:**

```json
"provider": "quickbooks"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Quip

**Provider value:**

```json
"provider": "quip"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "Personal API token",
                  "hint": "Personal API token. Click <a href=\"https://quip.com/api/personal-token\">here</a> to generate API token"
              }
          ]
      }
```

* * *

### Raiser's Edge NXT

**Provider value:**

```json
"provider": "raisers_edge"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### RecipeOps by Workato

**Provider value:**

```json
"provider": "workato_app"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "connecting_to_account",
                  "type": "boolean",
                  "label": "Whose account are you managing?",
                  "pick_list":
                  [
                      [
                          "My account",
                          "current"
                      ],
                      [
                          "Someone else's account",
                          "other"
                      ]
                  ],
                  "default": "nil"
              },
              {
                  "name": "email",
                  "type": "string",
                  "label": "Email",
                  "hint": "Managed account’s email"
              },
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "API key",
                  "hint": "Ask the account holder to provide the API key found here: <a href=\"http://localhost:3000/users/current/edit#api_key\" target=\"_blank\">http://localhost:3000/users/current/edit#api_key</a>"
              }
          ]
      }
```

* * *

### Redshift

**Provider value:**

```json
"provider": "redshift"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "url",
                  "type": "string",
                  "label": "URL",
                  "hint": "Redshift JDBC URL."
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "schema_name",
                  "type": "string",
                  "optional": true,
                  "label": "Schema",
                  "hint": "\"public\" schema by default"
              }
          ]
      }
```

* * *

### Redshift (Secondary)

**Provider value:**

```json
"provider": "redshift_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "url",
                  "type": "string",
                  "label": "URL",
                  "hint": "Redshift JDBC URL."
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "schema_name",
                  "type": "string",
                  "optional": true,
                  "label": "Schema",
                  "hint": "\"public\" schema by default"
              }
          ]
      }
```

* * *

### RegOnline® by Lanyon

**Provider value:**

```json
"provider": "active_reg_online"
```

View connection parameters JSON

```json
{
    "personalization": true,
    "input": [
        {
            "label": "API Token",
            "name": "api_token",
            "hint": "API token is found at the bottom of the RegOnline 'Edit User' screen.",
            "type": "string"
        }
    ]
}
```

* * *

### Replicon

**Provider value:**

```json
"provider": "replicon"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "company",
                  "type": "string",
                  "label": "Company",
                  "hint": "The company name associated with your login"
              },
              {
                  "name": "user_token_auth",
                  "type": "boolean",
                  "label": "User-token authentication?",
                  "hint": "Is authentication based on user tokens? If <b>Yes</b>, provide <b>User token</b>. Is <b>No</b>, provide <b>Username</b> & <b>Password</b>.",
                  "default": "false"
              },
              {
                  "name": "usertoken",
                  "type": "string",
                  "optional": true,
                  "label": "User token",
                  "hint": "Use this API https://<b>region</b>.replicon.com/<b>Company name</b>/services/AuthenticationService1.svc/help/test/CreateAccessToken to get user token"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Login name"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": true,
                  "label": "Password"
              },
              {
                  "name": "subdomain",
                  "type": "string",
                  "optional": true,
                  "label": "Subdomain",
                  "hint": "Leave to default (global) for production instances",
                  "default": "global"
              }
          ]
      }
```

* * *

### Revel Systems

**Provider value:**

```json
"provider": "revel_systems"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Subdomain",
                  "hint": "Your revel systems subdomain, usually a company name; for example, the <b>api-playground</b> part in https://api-playground.revelup.com"
              },
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "Api key"
              },
              {
                  "name": "api_secret",
                  "type": "string",
                  "label": "Api secret"
              }
          ]
      }
```

* * *

### RingCentral

**Provider value:**

```json
"provider": "ringcentral"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "development",
                  "type": "number",
                  "optional": true,
                  "label": "Development",
                  "hint": "Leave empty to connect production account. Provide <b>true</b> for development account <b>false</b> for production account."
              }
          ]
      }
```

* * *

### Rollbar

**Provider value:**

```json
"provider": "rollbar"
```

* * *

### Ruby

**Provider value:**

```json
"provider": "workato_custom_code"
```

* * *

### Sage Intacct

**Provider value:**

```json
"provider": "intacct"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "login_username",
                  "type": "string",
                  "label": "Login username"
              },
              {
                  "name": "login_password",
                  "type": "string",
                  "label": "Login password"
              },
              {
                  "name": "company_id",
                  "type": "string",
                  "label": "Company ID"
              },
              {
                  "name": "location_id",
                  "type": "string",
                  "optional": true,
                  "label": "Location ID",
                  "hint": "If not specified, it takes the top level(all entities)"
              }
          ]
      }
```

* * *

### Sage Live

**Provider value:**

```json
"provider": "sagelive"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### Salesforce

**Provider value:**

```json
"provider": "salesforce"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              },
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced settings",
                  "properties":
                  [
                      {
                          "name": "custom_login_url",
                          "type": "string",
                          "optional": true,
                          "label": "Salesforce community custom domain URL",
                          "hint": "                   Enter your Salesforce community's custom domain URL, eg. <b>acme-domain.force.com</b>.\n                   <a target='_blank' href='https://docs.workato.com/connectors/salesforce.html#connecting-to-custom-domains'>Learn more</a>\n"
                      },
                      {
                          "name": "api_scope",
                          "type": "string",
                          "optional": true,
                          "label": "Requested permissions (Oauth scopes)",
                          "hint": "                     Select <a href=\"https://help.salesforce.com/articleView?id=remoteaccess_oauth_scopes.htm&type=5\" target=\"_blank\">permissions</a>\n                      to request for this connection. Defaults to <b>full</b> (all permissions) if left blank.\n                     <br/>Minimum permissions required are <b>basic info</b>, <b>manage data</b> and <b>make\n                      requests at any time</b>;\n                     those are requested in addition to selected permissions.\n"
                      }
                  ]
              }
          ]
      }
```

* * *

### Salesforce (Secondary)

**Provider value:**

```json
"provider": "salesforce_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              },
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced settings",
                  "properties":
                  [
                      {
                          "name": "custom_login_url",
                          "type": "string",
                          "optional": true,
                          "label": "Salesforce community custom domain URL",
                          "hint": "                   Enter your Salesforce community's custom domain URL, eg. <b>acme-domain.force.com</b>.\n                   <a target='_blank' href='https://docs.workato.com/connectors/salesforce.html#connecting-to-custom-domains'>Learn more</a>\n"
                      },
                      {
                          "name": "api_scope",
                          "type": "string",
                          "optional": true,
                          "label": "Requested permissions (Oauth scopes)",
                          "hint": "                     Select <a href=\"https://help.salesforce.com/articleView?id=remoteaccess_oauth_scopes.htm&type=5\" target=\"_blank\">permissions</a>\n                      to request for this connection. Defaults to <b>full</b> (all permissions) if left blank.\n                     <br/>Minimum permissions required are <b>basic info</b>, <b>manage data</b> and <b>make\n                      requests at any time</b>;\n                     those are requested in addition to selected permissions.\n"
                      }
                  ]
              }
          ]
      }
```

* * *

### Salesforce CPQ

**Provider value:**

```json
"provider": "steelbrick"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### SalesforceIQ

**Provider value:**

```json
"provider": "relateiq"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "API Key",
                  "hint": "Create in your SalesforceIQ account: Organization > settings > integrations"
              },
              {
                  "name": "api_secret",
                  "type": "string",
                  "label": "API Secret"
              }
          ]
      }
```

* * *

### Salesforce Marketing Cloud

**Provider value:**

```json
"provider": "salesforce_marketing_cloud"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "flag",
                  "type": "boolean",
                  "label": "Are you using a new installed package?",
                  "hint": "Legacy packages (created before 1st August 2019) uses a different set of fields to connect.",
                  "default": "false"
              },
              {
                  "name": "instance",
                  "type": "string",
                  "label": "Instance",
                  "hint": "Select the instance of your account. Eg: Select <b>s7</b>, if the instance URL is <b>https://mc.s7.exacttarget.com</b>.",
                  "pick_list":
                  [
                      [
                          "s1",
                          "s1"
                      ],
                      [
                          "s4",
                          "s4"
                      ],
                      [
                          "s6",
                          "s6"
                      ],
                      [
                          "s7",
                          "s7"
                      ],
                      [
                          "s10",
                          "s10"
                      ],
                      [
                          "test",
                          "test"
                      ]
                  ]
              },
              {
                  "name": "instance_name",
                  "type": "string",
                  "label": "Instance name",
                  "hint": "Enter the instance of your account. Eg: Enter <b>s7</b>, if the instance URL is <b>https://mc.s7.exacttarget.com</b>."
              },
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Subdomain",
                  "hint": "Enter the sub-domain of your account."
              },
              {
                  "name": "client_id",
                  "type": "string",
                  "label": "Client ID",
                  "hint": "                   Create client credentials with read and write access for <b>channels</b>, <b>assets</b>, <b>contacts</b>, <b>data</b>. To access shared content, use\n                   credentials of business unit where content belongs.\n                   To create client credentials refer\n                   <a href=\"https://developer.salesforce.com/docs/atlas.en-us.mc-getting-started.meta/mc-getting-started/app-center-types.htm\" target=\"_blank\">here</a>.\n"
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "label": "Client secret"
              }
          ]
      }
```

* * *

### SAP Concur

**Provider value:**

```json
"provider": "concur"
```

View connection parameters JSON

```json
{
    "oauth": true,
    "personalization": true,
    "oauth_token_pair": {
        "label": "OAuth Token Pair",
        "optional": true,
        "type": "object",
        "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
        "properties": [
            {
                "label": "Access Token",
                "name": "access_token",
                "type": "string",
                "optional": false
            },
            {
                "label": "Refresh Token",
                "name": "refresh_token",
                "type": "string",
                "optional": false
            }
        ]
    },
    "input": [
        {
            "label": "Implementation instance",
            "name": "sandbox",
            "optional": true,
            "hint": "Specify whether this connection is to an implementation instance. Refer to the following page for more information: 'https://docs.workato.com/connectors/concur.html'. Defaults to 'false'.",
            "type": "boolean"
        },
        {
            "label": "Authentication type",
            "name": "authentication_type",
            "optional": true,
            "hint": "Select the authentication type. This only applies when Implementation instance is 'false'.",
            "type": "string",
            "pick_list": [
                [
                    "Password grant",
                    "password_grant"
                ],
                [
                    "Refresh token grant",
                    "refresh_token"
                ],
                [
                    "Authorization code grant",
                    "authorization_grant"
                ]
            ]
        },
        {
            "label": "Username",
            "name": "user_name",
            "hint": "Specify the username or user ID. This only applies when Implementation instance is 'true' or Authentication type is 'password_grant'.",
            "type": "string"
        },
        {
            "label": "Password",
            "name": "password",
            "hint": "Enter a password. This only applies when Implementation instance is 'true' or Authentication type is 'password_grant'.",
            "type": "string"
        },
        {
            "label": "Location",
            "name": "location",
            "hint": "Select the location of your implementation server.",
            "type": "string",
            "pick_list": [
                [
                    "US Production",
                    "us"
                ],
                [
                    "EU Production",
                    "emea"
                ],
                [
                    "CN Production",
                    "cn"
                ],
                [
                    "PSCC Production",
                    "usg"
                ],
                [
                    "US Implementation",
                    "us-impl"
                ],
                [
                    "EU Implementation",
                    "emea-impl"
                ]
            ]
        },
        {
            "label": "Client ID",
            "name": "client_id",
            "hint": "Provide the client ID for your application. This only applies when Implementation instance is 'true' or Authentication type is not 'authorization_grant'.",
            "type": "string"
        },
        {
            "label": "Client secret",
            "name": "client_secret",
            "hint": "Provide the client secret for your application. This only applies when Implementation instance is 'true' or Authentication type is not 'authorization_grant'.",
            "type": "string"
        },
        {
            "label": "Refresh token",
            "name": "refresh_token",
            "hint": "Provide a refresh token for your application. This only applies when Authentication type is 'refresh_token'.",
            "type": "string"
        },
        {
            "label": "Advanced settings",
            "name": "advanced_settings",
            "optional": true,
            "hint": "This only applies when Authentication type is 'authorization_grant' and Implementation instance is 'false'.",
            "type": "object",
            "properties": [
                {
                    "label": "Scopes",
                    "name": "scope",
                    "optional": true,
                    "hint": "Select additional OAuth 2.0 scopes to request for this connection. The minimum scopes, 'openid', 'user.read', 'EXPRPT' are always requested in addition to your selection. The following scopes are requested by default: 'openid', 'user.read', 'user.write', 'EXPRPT', 'expense.report.read', 'expense.report.readwrite', 'LIST', 'spend.list.read', 'spend.list.write', 'spend.listitem.read', 'spend.listitem.write', 'spend.listitem.delete', 'IMAGE', 'ATTEND', 'CONFIG', 'INVPMT', 'INVVEN', 'identity.user.core.read', 'identity.user.coresensitive.read', 'identity.user.enterprise.read', 'identity.user.coreenterprise.writeonly', 'identity.user.externalID.writeonly', 'identity.user.ids.read', 'user.provision.read', 'user.provision.write', 'spend.user.general.read', 'spend.user.general.writeonly', 'travel.user.general.read', 'expense.config.groups.restricted.read', 'expense.config.policies.restricted.read', 'expense.config.expensetypes.restricted.read', 'expense.config.paymenttypes.restricted.read', 'expense.config.attendeetypes.restricted.read'. Separate multiple values with spaces.",
                    "type": "string",
                    "options": [
                        [
                            "Attend",
                            "ATTEND"
                        ],
                        [
                            "Attendee Admin Read",
                            "attendee.admin.read"
                        ],
                        [
                            "Attendee Read",
                            "attendee.read"
                        ],
                        [
                            "Attendee Write",
                            "attendee.write"
                        ],
                        [
                            "Attendee Writeonly",
                            "attendee.writeonly"
                        ],
                        [
                            "Bank",
                            "BANK"
                        ],
                        [
                            "Budget Item Read",
                            "budgetitem.read"
                        ],
                        [
                            "Budget Item Write",
                            "budgetitem.write"
                        ],
                        [
                            "Cards Account Writeonly",
                            "cards.account.writeonly"
                        ],
                        [
                            "Cards Bulk Request Read",
                            "cards.bulkrequest.read"
                        ],
                        [
                            "Cards Transaction Read",
                            "cards.transaction.read"
                        ],
                        [
                            "Cards Transaction Writeonly",
                            "cards.transaction.writeonly"
                        ],
                        [
                            "CCard",
                            "CCARD"
                        ],
                        [
                            "CompD",
                            "COMPD"
                        ],
                        [
                            "Company Read",
                            "company.read"
                        ],
                        [
                            "Company Write",
                            "company.write"
                        ],
                        [
                            "Config",
                            "CONFIG"
                        ],
                        [
                            "ConReq",
                            "CONREQ"
                        ],
                        [
                            "Credit Card Account Read",
                            "creditcardaccount.read"
                        ],
                        [
                            "Emerg",
                            "EMERG"
                        ],
                        [
                            "Events Topic Read",
                            "events.topic.read"
                        ],
                        [
                            "Expense Config Attendee Types Restricted Read",
                            "expense.config.attendeetypes.restricted.read"
                        ],
                        [
                            "Expense Config Groups Restricted Read",
                            "expense.config.groups.restricted.read"
                        ],
                        [
                            "Expense Config Policies Restricted Read",
                            "expense.config.policies.restricted.read"
                        ],
                        [
                            "Expense Config Expense Types Restricted Read",
                            "expense.config.expensetypes.restricted.read"
                        ],
                        [
                            "Expense Config Payment Types Restricted Read",
                            "expense.config.paymenttypes.restricted.read"
                        ],
                        [
                            "Expense Exchange Rate Writeonly",
                            "expense.exchangerate.writeonly"
                        ],
                        [
                            "Expense Report Read",
                            "expense.report.read"
                        ],
                        [
                            "Expense Report Read Write",
                            "expense.report.readwrite"
                        ],
                        [
                            "Expense Report Tax Read Write",
                            "expense.report.tax.readwrite"
                        ],
                        [
                            "Expense Report Workflow Status Write",
                            "expense.report.workflowstatus.write"
                        ],
                        [
                            "Extrct",
                            "EXTRCT"
                        ],
                        [
                            "Fiscal Calendar Read",
                            "fiscalcalendar.read"
                        ],
                        [
                            "Fiscal Calendar Write",
                            "fiscalcalendar.write"
                        ],
                        [
                            "FISvc",
                            "FISVC"
                        ],
                        [
                            "Identity User Core Read",
                            "identity.user.core.read"
                        ],
                        [
                            "Identity User Core Sensitive Read",
                            "identity.user.coresensitive.read"
                        ],
                        [
                            "Identity User Emails Verified Writeonly",
                            "identity.user.emails.verified.writeonly"
                        ],
                        [
                            "Identity User Enterprise Read",
                            "identity.user.enterprise.read"
                        ],
                        [
                            "Identity User Core Enterprise Writeonly",
                            "identity.user.coreenterprise.writeonly"
                        ],
                        [
                            "Identity User External ID Writeonly",
                            "identity.user.externalID.writeonly"
                        ],
                        [
                            "Identity User IDs Read",
                            "identity.user.ids.read"
                        ],
                        [
                            "Identity User SAP Read",
                            "identity.user.sap.read"
                        ],
                        [
                            "Identity User SAP Writeonly",
                            "identity.user.sap.writeonly"
                        ],
                        [
                            "Image",
                            "IMAGE"
                        ],
                        [
                            "Insght",
                            "INSGHT"
                        ],
                        [
                            "Invoice Payment Confirmation Read",
                            "invoice.paymentconfirmation.read"
                        ],
                        [
                            "Invoice Payment Confirmation Write",
                            "invoice.paymentconfirmation.write"
                        ],
                        [
                            "Invoice Provider Payment Write",
                            "invoice.providerpayment.write"
                        ],
                        [
                            "InvPmt",
                            "INVPMT"
                        ],
                        [
                            "InvPO",
                            "INVPO"
                        ],
                        [
                            "InvTV",
                            "INVTV"
                        ],
                        [
                            "InvVen",
                            "INVVEN"
                        ],
                        [
                            "Itiner",
                            "ITINER"
                        ],
                        [
                            "List",
                            "LIST"
                        ],
                        [
                            "Locality Read",
                            "locality.read"
                        ],
                        [
                            "Locate Location Read",
                            "locate.location.read"
                        ],
                        [
                            "Locate Location Write",
                            "locate.location.write"
                        ],
                        [
                            "Medic",
                            "MEDIC"
                        ],
                        [
                            "Notif",
                            "NOTIF"
                        ],
                        [
                            "PassV",
                            "PASSV"
                        ],
                        [
                            "PayBat",
                            "PAYBAT"
                        ],
                        [
                            "Purchase Request Read",
                            "purchaserequest.read"
                        ],
                        [
                            "Purchase Request Write",
                            "purchaserequest.write"
                        ],
                        [
                            "Quick Expense Writeonly",
                            "quickexpense.writeonly"
                        ],
                        [
                            "RctImg",
                            "RCTIMG"
                        ],
                        [
                            "Receipts Read",
                            "receipts.read"
                        ],
                        [
                            "Receipts Write",
                            "receipts.write"
                        ],
                        [
                            "Receipts Writeonly",
                            "receipts.writeonly"
                        ],
                        [
                            "Spend Docs Receipts Compliance Read",
                            "spenddocs.receipts.compliance.read"
                        ],
                        [
                            "Spend Docs Receipts Compliance Write",
                            "spenddocs.receipts.compliance.write"
                        ],
                        [
                            "Spend Docs Receipts Compliance Writeonly",
                            "spenddocs.receipts.compliance.writeonly"
                        ],
                        [
                            "Spend Docs Receipts Read",
                            "spenddocs.receipts.read"
                        ],
                        [
                            "Spend Docs Receipts Write",
                            "spenddocs.receipts.write"
                        ],
                        [
                            "Spend Docs Receipts Writeonly",
                            "spenddocs.receipts.writeonly"
                        ],
                        [
                            "Spend List Delete",
                            "spend.list.delete"
                        ],
                        [
                            "Spend List Read",
                            "spend.list.read"
                        ],
                        [
                            "Spend List Write",
                            "spend.list.write"
                        ],
                        [
                            "Spend List Item Delete",
                            "spend.listitem.delete"
                        ],
                        [
                            "Spend List Item Read",
                            "spend.listitem.read"
                        ],
                        [
                            "Spend List Item Write",
                            "spend.listitem.write"
                        ],
                        [
                            "Spend User General Read",
                            "spend.user.general.read"
                        ],
                        [
                            "Spend User General Writeonly",
                            "spend.user.general.writeonly"
                        ],
                        [
                            "TaxInv",
                            "TAXINV"
                        ],
                        [
                            "TMCSP",
                            "TMCSP"
                        ],
                        [
                            "Travel Allowance Days Read",
                            "travelallowance.allowancedays.read"
                        ],
                        [
                            "Travel Allowance Configuration Read",
                            "travelallowance.configuration.read"
                        ],
                        [
                            "Travel Allowance Itinerary Read",
                            "travelallowance.itinerary.read"
                        ],
                        [
                            "Travel Allowance Itinerary Writeonly",
                            "travelallowance.itinerary.writeonly"
                        ],
                        [
                            "Travel Allowance Itinerary Result Read",
                            "travelallowance.itineraryresult.read"
                        ],
                        [
                            "Travel Hotel Write",
                            "travel.hotel.write"
                        ],
                        [
                            "Travel Itinerary Read",
                            "travel.itinerary.read"
                        ],
                        [
                            "Travel Receipts Read",
                            "travel.receipts.read"
                        ],
                        [
                            "Travel Receipts Write",
                            "travel.receipts.write"
                        ],
                        [
                            "Travel Request Write",
                            "travelrequest.write"
                        ],
                        [
                            "Travel User General Read",
                            "travel.user.general.read"
                        ],
                        [
                            "Travel User Private Read",
                            "travel.user.private.read"
                        ],
                        [
                            "TSAI",
                            "TSAI"
                        ],
                        [
                            "TrvPrf",
                            "TRVPRF"
                        ],
                        [
                            "TrvPts",
                            "TRVPTS"
                        ],
                        [
                            "TrvReq",
                            "TRVREQ"
                        ],
                        [
                            "TWS",
                            "TWS"
                        ],
                        [
                            "UnUtx",
                            "UNUTX"
                        ],
                        [
                            "User Write",
                            "user.write"
                        ],
                        [
                            "User Provision Read",
                            "user.provision.read"
                        ],
                        [
                            "User Provision Write",
                            "user.provision.write"
                        ]
                    ]
                }
            ]
        }
    ]
}
```

* * *

### SAP D4C

**Provider value:**

```json
"provider": "sap_d4c"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "endpoint",
                  "type": "string",
                  "label": "Endpoint",
                  "hint": "Eg. 'my123456.vlab.sapbydesign.com'"
              }
          ]
      }
```

* * *

### SAP OData

**Provider value:**

```json
"provider": "sap_s4_hana_cloud"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "domain",
                  "type": "string",
                  "label": "Service URL",
                  "hint": "Your SAP Service URL to validate authentication. For example, <b>http://sap.intranet.acme.com:7654/sap/opu/odata/sap/ZEMPLOYEE_SRV</b>."
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "client",
                  "type": "string",
                  "optional": true,
                  "label": "Client",
                  "hint": "SAP client ID. Leave blank to use the default logon client."
              }
          ]
      }
```

* * *

### SAP RFC

**Provider value:**

```json
"provider": "sap"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem agent connection profile",
                  "hint": "<a href='https://docs.workato.com/connectors/sap.html' target='_blank'>Click here</a> to learn how to configure SAP connection."
              }
          ]
      }
```

* * *

### Scheduler by Workato

**Provider value:**

```json
"provider": "clock"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### SendGrid

**Provider value:**

```json
"provider": "sendgrid"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "API key",
                  "hint": "Go to settings -> API keys -> create API key"
              }
          ]
      }
```

* * *

### ServiceM8

**Provider value:**

```json
"provider": "servicem8"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "user",
                  "type": "string",
                  "label": "User"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              }
          ]
      }
```

* * *

### ServiceMax

**Provider value:**

```json
"provider": "service_max"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### ServiceNow

**Provider value:**

```json
"provider": "service_now"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "authentication_type",
                  "type": "string",
                  "label": "Authentication type",
                  "hint": "Only Istanbul version or later supports OAuth 2.0. <a href=\"http://docs.workato.com/connectors/servicenow.html\" target=\"_blank\">Learn more</a> about the authentication types.",
                  "pick_list":
                  [
                      [
                          "Username/Password",
                          "basic"
                      ],
                      [
                          "OAuth 2.0",
                          "oauth"
                      ]
                  ],
                  "default": "basic"
              },
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Instance name",
                  "hint": "If your ServiceNow url is <b>https://acme.service-now.com</b>, then instance name is <b>'acme'</b>."
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username",
                  "hint": "Make sure that you have sufficient access control to all the tables you wish to work with. <a href=\"http://docs.workato.com/connectors/servicenow.html#roles-and-permissions-required-to-connect\" target=\"_blank\">Learn more</a>."
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "client_id",
                  "type": "string",
                  "label": "Client ID",
                  "hint": "<a href=\"http://docs.workato.com/connectors/servicenow.html#oauth-20\" target=\"_blank\">Learn more</a> about setting up OAuth in your ServiceNow instance."
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "label": "Client secret"
              }
          ]
      }
```

* * *

### ServiceNow (Secondary)

**Provider value:**

```json
"provider": "service_now_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "authentication_type",
                  "type": "string",
                  "label": "Authentication type",
                  "hint": "Only Istanbul version or later supports OAuth 2.0. <a href=\"http://docs.workato.com/connectors/servicenow.html\" target=\"_blank\">Learn more</a> about the authentication types.",
                  "pick_list":
                  [
                      [
                          "Username/Password",
                          "basic"
                      ],
                      [
                          "OAuth 2.0",
                          "oauth"
                      ]
                  ],
                  "default": "basic"
              },
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Instance name",
                  "hint": "If your ServiceNow url is <b>https://acme.service-now.com</b>, then instance name is <b>'acme'</b>."
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username",
                  "hint": "Make sure that you have sufficient access control to all the tables you wish to work with. <a href=\"http://docs.workato.com/connectors/servicenow.html#roles-and-permissions-required-to-connect\" target=\"_blank\">Learn more</a>."
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "client_id",
                  "type": "string",
                  "label": "Client ID",
                  "hint": "<a href=\"http://docs.workato.com/connectors/servicenow.html#oauth-20\" target=\"_blank\">Learn more</a> about setting up OAuth in your ServiceNow instance."
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "label": "Client secret"
              }
          ]
      }
```

* * *

### SFTP

**Provider value:**

```json
"provider": "sftp"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "auth_type",
                  "type": "string",
                  "label": "Auth type",
                  "pick_list":
                  [
                      [
                          "Username/password",
                          "username_password"
                      ],
                      [
                          "Public/private key pair",
                          "pubkey"
                      ]
                  ],
                  "default": "username_password"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "private_key",
                  "type": "string",
                  "label": "Private key",
                  "hint": "Please use an OpenSSH private key, without password protection. <a href=\"https://www.ssh.com/ssh/keygen/\" target=\"_blank\">Learn more</a>"
              },
              {
                  "name": "hostname",
                  "type": "string",
                  "label": "Hostname",
                  "hint": "Contact your SFTP server administrator to whitelist Workato IP addresses. <a href=\"http://docs.workato.com/security.html\" target=\"_blank\">Learn more</a>"
              },
              {
                  "name": "port",
                  "type": "integer",
                  "label": "Port",
                  "hint": "The standard port is 22, contact your SFTP server administrator for the correct port.",
              },
              {
                  "name": "host_key_fingerprint",
                  "type": "string",
                  "optional": true,
                  "label": "Host key fingerprint",
                  "hint": "The connection will still be encrypted without this, but without protection against <a href=\"https://en.wikipedia.org/wiki/Man-in-the-middle_attack\">MITM</a><br/>Contact SFTP server administrator for the key fingerprint."
              },
              {
                  "name": "transfer_buffer_size",
                  "type": "integer",
                  "label": "Transfer buffer size",
                  "hint": "Size of the buffer used to transfer files. Minimum is 32768.\nLarger sizes, if supported by the SFTP server, generally speed up transfers.\nMaximum is 327680.\n",
              },
              {
                  "name": "force_close",
                  "type": "boolean",
                  "optional": true,
                  "label": "Force close",
                  "hint": "Shuts down the underlying SSH connection at the end of the transaction.\nOnly needed for servers where the connection attempt seems to hang, should\nbe left unset otherwise to allow a clean connection close.\n"
              }
          ]
      }
```

* * *

### SFTP (Secondary)

**Provider value:**

```json
"provider": "sftp_secondary
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "auth_type",
                  "type": "string",
                  "label": "Auth type",
                  "pick_list":
                  [
                      [
                          "Username/password",
                          "username_password"
                      ],
                      [
                          "Public/private key pair",
                          "pubkey"
                      ]
                  ],
                  "default": "username_password"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "private_key",
                  "type": "string",
                  "label": "Private key",
                  "hint": "Please use an OpenSSH private key, without password protection. <a href=\"https://www.ssh.com/ssh/keygen/\" target=\"_blank\">Learn more</a>"
              },
              {
                  "name": "hostname",
                  "type": "string",
                  "label": "Hostname",
                  "hint": "Contact your SFTP server administrator to whitelist Workato IP addresses. <a href=\"http://docs.workato.com/security.html\" target=\"_blank\">Learn more</a>"
              },
              {
                  "name": "port",
                  "type": "integer",
                  "label": "Port",
                  "hint": "The standard port is 22, contact your SFTP server administrator for the correct port.",
              },
              {
                  "name": "host_key_fingerprint",
                  "type": "string",
                  "optional": true,
                  "label": "Host key fingerprint",
                  "hint": "The connection will still be encrypted without this, but without protection against <a href=\"https://en.wikipedia.org/wiki/Man-in-the-middle_attack\">MITM</a><br/>Contact SFTP server administrator for the key fingerprint."
              },
              {
                  "name": "transfer_buffer_size",
                  "type": "integer",
                  "label": "Transfer buffer size",
                  "hint": "Size of the buffer used to transfer files. Minimum is 32768.\nLarger sizes, if supported by the SFTP server, generally speed up transfers.\nMaximum is 327680.\n",
              },
              {
                  "name": "force_close",
                  "type": "boolean",
                  "optional": true,
                  "label": "Force close",
                  "hint": "Shuts down the underlying SSH connection at the end of the transaction.\nOnly needed for servers where the connection attempt seems to hang, should\nbe left unset otherwise to allow a clean connection close.\n"
              }
          ]
      }
```

* * *

### Shopify

**Provider value:**

```json
"provider": "shopify"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "shop_name",
                  "type": "string",
                  "label": "Shop Name",
                  "hint": "Your shop name Eg. <b>shopname</b>.myshopify.com/admin"
              }
          ]
      }
```

* * *

### Showpad

**Provider value:**

```json
"provider": "showpad"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Subdomain",
                  "hint": "Your Showpad subdomain, usually a company name; for example, the <b>acme</b> part in https://acme.showpad.biz"
              }
          ]
      }
```

* * *

### Slack

**Provider value:**

```json
"provider": "slack"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Slack (Secondary)

**Provider value:**

```json
"provider": "slack_secondary"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Smartsheet

**Provider value:**

```json
"provider": "smartsheet"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced settings",
                  "properties":
                  [
                      {
                          "name": "api_scope",
                          "type": "string",
                          "optional": true,
                          "label": "Requested permissions (Oauth scopes)",
                          "hint": "                      Select <a href=\"https://smartsheet-platform.github.io/api-docs/#access-scopes\" target=\"_blank\">permissions</a>\n                      to request for this connection. Defaults to minimum permissions, if left blank.\n                      <br/>Minimum permissions required are <b>READ_SHEETS</b>, <b>WRITE_SHEETS</b>, <b>ADMIN_WEBHOOKS</b> and <b>CREATE_SHEETS</b>;\n                      those are requested in addition to selected permissions.\n"
                      }
                  ]
              }
          ]
      }
```

* * *

### SMS by Workato

**Provider value:**

```json
"provider": "sms"
```

* * *

### Snowflake

**Provider value:**

```json
"provider": "snowflake"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "input": [
    {
      "label": "Account identifier",
      "optional": false,
      "hint": "Account identifier of your Snowflake instance. This depends on the cloud platform, such as AWS, Azure, or GCP, and region where your Snowflake instance is hosted. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#how-to-connect-to-snowflake-on-workato",
      "type": "string",
      "name": "host"
    },
    {
      "label": "Warehouse",
      "hint": "Full name of warehouse to perform all operations for this connection. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#warehouse-considerations",
      "type": "string",
      "name": "warehouse"
    },
    {
      "label": "Database name",
      "type": "string",
      "name": "database"
    },
    {
      "label": "Authentication type",
      "default": "key_pair",
      "type": "string",
      "name": "authentication_type",
      "pick_list": [
        [
          "OAuth 2.0",
          "oauth"
        ],
        [
          "Key-pair authentication",
          "key_pair"
        ],
        [
          "Username/Password (Deprecated)",
          "basic"
        ]
      ]
    },
    {
      "label": "User name",
      "type": "string",
      "name": "user"
    },
    {
      "label": "Password",
      "hint": "Snowflake plans to deprecate single-factor password authentication for users by November 2025. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#configure-username-password-authentication",
      "optional": true,
      "type": "string",
      "name": "password"
    },
    {
      "label": "Private key",
      "optional": true,
      "hint": "Paste your private key in PKCS 8 format. Use '\n' characters sequence to join all pem lines into one json string. The Private key field is ignored by the connection when the Password field is provided. Refer to the Snowflake Key Pair Authentication documentation for more information: https://docs.snowflake.com/en/user-guide/key-pair-auth",
      "type": "string",
      "name": "private_key"
    },
    {
      "label": "Private key passphrase",
      "optional": true,
      "hint": "You must enter the passphrase if the private key is encrypted.",
      "type": "string",
      "name": "private_key_passphrase"
    },
    {
      "label": "Client ID",
      "hint": "Refer to the Snowflake connector documentation to obtain a Client ID and Client secret: https://docs.workato.com/connectors/snowflake.html#configuring-oauth-2-0",
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Client secret",
      "hint": "Refer to the Snowflake connector documentation to obtain a Client ID and Client secret: https://docs.workato.com/connectors/snowflake.html#configuring-oauth-2-0",
      "type": "string",
      "name": "client_secret"
    },
    {
      "label": "Role",
      "optional": true,
      "hint": "Specify the role for requests using this connection. This role must be an existing role assigned to the user. Leave blank to use the default role of the user.",
      "type": "string",
      "name": "role"
    },
    {
      "label": "Schema",
      "optional": true,
      "hint": "PUBLIC schema by default",
      "type": "string",
      "name": "schema_name"
    },
    {
      "label": "Use improved datetime handling (Recommended)",
      "optional": true,
      "hint": "Defaults to true. Enable this if you plan to specify the timezone for timestamp columns during insertion and retrieval. Make sure you specify the timezone in the next field.",
      "type": "boolean",
      "name": "improved_datetime_handling"
    },
    {
      "label": "Database timezone",
      "optional": true,
      "hint": "Highly recommended if your database contains timestamps with timezone values. This timezone will be applied to all timestamps inserted to the database. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#database-timezone",
      "type": "string",
      "name": "db_timezone",
      "pick_list": [
        [
          "American Samoa",
          "American Samoa"
        ],
        [
          "International Date Line West",
          "International Date Line West"
        ],
        [
          "Midway Island",
          "Midway Island"
        ],
        [
          "Hawaii",
          "Hawaii"
        ],
        [
          "Alaska",
          "Alaska"
        ],
        [
          "Pacific Time (US & Canada)",
          "Pacific Time (US & Canada)"
        ],
        [
          "Tijuana",
          "Tijuana"
        ],
        [
          "Arizona",
          "Arizona"
        ],
        [
          "Chihuahua",
          "Chihuahua"
        ],
        [
          "Mazatlan",
          "Mazatlan"
        ],
        [
          "Mountain Time (US & Canada)",
          "Mountain Time (US & Canada)"
        ],
        [
          "Central America",
          "Central America"
        ],
        [
          "Central Time (US & Canada)",
          "Central Time (US & Canada)"
        ],
        [
          "Guadalajara",
          "Guadalajara"
        ],
        [
          "Mexico City",
          "Mexico City"
        ],
        [
          "Monterrey",
          "Monterrey"
        ],
        [
          "Saskatchewan",
          "Saskatchewan"
        ],
        [
          "Bogota",
          "Bogota"
        ],
        [
          "Eastern Time (US & Canada)",
          "Eastern Time (US & Canada)"
        ],
        [
          "Indiana (East)",
          "Indiana (East)"
        ],
        [
          "Lima",
          "Lima"
        ],
        [
          "Quito",
          "Quito"
        ],
        [
          "Atlantic Time (Canada)",
          "Atlantic Time (Canada)"
        ],
        [
          "Caracas",
          "Caracas"
        ],
        [
          "Georgetown",
          "Georgetown"
        ],
        [
          "La Paz",
          "La Paz"
        ],
        [
          "Santiago",
          "Santiago"
        ],
        [
          "Newfoundland",
          "Newfoundland"
        ],
        [
          "Brasilia",
          "Brasilia"
        ],
        [
          "Buenos Aires",
          "Buenos Aires"
        ],
        [
          "Greenland",
          "Greenland"
        ],
        [
          "Montevideo",
          "Montevideo"
        ],
        [
          "Mid-Atlantic",
          "Mid-Atlantic"
        ],
        [
          "Azores",
          "Azores"
        ],
        [
          "Cape Verde Is.",
          "Cape Verde Is."
        ],
        [
          "Casablanca",
          "Casablanca"
        ],
        [
          "Dublin",
          "Dublin"
        ],
        [
          "Edinburgh",
          "Edinburgh"
        ],
        [
          "Lisbon",
          "Lisbon"
        ],
        [
          "London",
          "London"
        ],
        [
          "Monrovia",
          "Monrovia"
        ],
        [
          "UTC",
          "UTC"
        ],
        [
          "Amsterdam",
          "Amsterdam"
        ],
        [
          "Belgrade",
          "Belgrade"
        ],
        [
          "Berlin",
          "Berlin"
        ],
        [
          "Bern",
          "Bern"
        ],
        [
          "Bratislava",
          "Bratislava"
        ],
        [
          "Brussels",
          "Brussels"
        ],
        [
          "Budapest",
          "Budapest"
        ],
        [
          "Copenhagen",
          "Copenhagen"
        ],
        [
          "Ljubljana",
          "Ljubljana"
        ],
        [
          "Madrid",
          "Madrid"
        ],
        [
          "Paris",
          "Paris"
        ],
        [
          "Prague",
          "Prague"
        ],
        [
          "Rome",
          "Rome"
        ],
        [
          "Sarajevo",
          "Sarajevo"
        ],
        [
          "Skopje",
          "Skopje"
        ],
        [
          "Stockholm",
          "Stockholm"
        ],
        [
          "Vienna",
          "Vienna"
        ],
        [
          "Warsaw",
          "Warsaw"
        ],
        [
          "West Central Africa",
          "West Central Africa"
        ],
        [
          "Zagreb",
          "Zagreb"
        ],
        [
          "Athens",
          "Athens"
        ],
        [
          "Bucharest",
          "Bucharest"
        ],
        [
          "Cairo",
          "Cairo"
        ],
        [
          "Harare",
          "Harare"
        ],
        [
          "Helsinki",
          "Helsinki"
        ],
        [
          "Jerusalem",
          "Jerusalem"
        ],
        [
          "Kaliningrad",
          "Kaliningrad"
        ],
        [
          "Kyiv",
          "Kyiv"
        ],
        [
          "Pretoria",
          "Pretoria"
        ],
        [
          "Riga",
          "Riga"
        ],
        [
          "Sofia",
          "Sofia"
        ],
        [
          "Tallinn",
          "Tallinn"
        ],
        [
          "Vilnius",
          "Vilnius"
        ],
        [
          "Baghdad",
          "Baghdad"
        ],
        [
          "Istanbul",
          "Istanbul"
        ],
        [
          "Kuwait",
          "Kuwait"
        ],
        [
          "Minsk",
          "Minsk"
        ],
        [
          "Moscow",
          "Moscow"
        ],
        [
          "Nairobi",
          "Nairobi"
        ],
        [
          "Riyadh",
          "Riyadh"
        ],
        [
          "St. Petersburg",
          "St. Petersburg"
        ],
        [
          "Tehran",
          "Tehran"
        ],
        [
          "Abu Dhabi",
          "Abu Dhabi"
        ],
        [
          "Baku",
          "Baku"
        ],
        [
          "Muscat",
          "Muscat"
        ],
        [
          "Samara",
          "Samara"
        ],
        [
          "Tbilisi",
          "Tbilisi"
        ],
        [
          "Volgograd",
          "Volgograd"
        ],
        [
          "Yerevan",
          "Yerevan"
        ],
        [
          "Kabul",
          "Kabul"
        ],
        [
          "Ekaterinburg",
          "Ekaterinburg"
        ],
        [
          "Islamabad",
          "Islamabad"
        ],
        [
          "Karachi",
          "Karachi"
        ],
        [
          "Tashkent",
          "Tashkent"
        ],
        [
          "Chennai",
          "Chennai"
        ],
        [
          "Kolkata",
          "Kolkata"
        ],
        [
          "Mumbai",
          "Mumbai"
        ],
        [
          "New Delhi",
          "New Delhi"
        ],
        [
          "Sri Jayawardenepura",
          "Sri Jayawardenepura"
        ],
        [
          "Kathmandu",
          "Kathmandu"
        ],
        [
          "Almaty",
          "Almaty"
        ],
        [
          "Astana",
          "Astana"
        ],
        [
          "Dhaka",
          "Dhaka"
        ],
        [
          "Urumqi",
          "Urumqi"
        ],
        [
          "Rangoon",
          "Rangoon"
        ],
        [
          "Bangkok",
          "Bangkok"
        ],
        [
          "Hanoi",
          "Hanoi"
        ],
        [
          "Jakarta",
          "Jakarta"
        ],
        [
          "Krasnoyarsk",
          "Krasnoyarsk"
        ],
        [
          "Novosibirsk",
          "Novosibirsk"
        ],
        [
          "Beijing",
          "Beijing"
        ],
        [
          "Chongqing",
          "Chongqing"
        ],
        [
          "Hong Kong",
          "Hong Kong"
        ],
        [
          "Irkutsk",
          "Irkutsk"
        ],
        [
          "Kuala Lumpur",
          "Kuala Lumpur"
        ],
        [
          "Perth",
          "Perth"
        ],
        [
          "Singapore",
          "Singapore"
        ],
        [
          "Taipei",
          "Taipei"
        ],
        [
          "Ulaanbaatar",
          "Ulaanbaatar"
        ],
        [
          "Osaka",
          "Osaka"
        ],
        [
          "Sapporo",
          "Sapporo"
        ],
        [
          "Seoul",
          "Seoul"
        ],
        [
          "Tokyo",
          "Tokyo"
        ],
        [
          "Yakutsk",
          "Yakutsk"
        ],
        [
          "Adelaide",
          "Adelaide"
        ],
        [
          "Darwin",
          "Darwin"
        ],
        [
          "Brisbane",
          "Brisbane"
        ],
        [
          "Canberra",
          "Canberra"
        ],
        [
          "Guam",
          "Guam"
        ],
        [
          "Hobart",
          "Hobart"
        ],
        [
          "Melbourne",
          "Melbourne"
        ],
        [
          "Port Moresby",
          "Port Moresby"
        ],
        [
          "Sydney",
          "Sydney"
        ],
        [
          "Vladivostok",
          "Vladivostok"
        ],
        [
          "Magadan",
          "Magadan"
        ],
        [
          "New Caledonia",
          "New Caledonia"
        ],
        [
          "Solomon Is.",
          "Solomon Is."
        ],
        [
          "Srednekolymsk",
          "Srednekolymsk"
        ],
        [
          "Auckland",
          "Auckland"
        ],
        [
          "Fiji",
          "Fiji"
        ],
        [
          "Kamchatka",
          "Kamchatka"
        ],
        [
          "Marshall Is.",
          "Marshall Is."
        ],
        [
          "Wellington",
          "Wellington"
        ],
        [
          "Chatham Is.",
          "Chatham Is."
        ],
        [
          "Nuku'alofa",
          "Nuku'alofa"
        ],
        [
          "Samoa",
          "Samoa"
        ],
        [
          "Tokelau Is.",
          "Tokelau Is."
        ]
      ]
    }
  ]
}
```

* * *

### Snowflake (Secondary)

**Provider value:**

```json
"provider": "snowflake_secondary"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "input": [
    {
      "label": "Account identifier",
      "optional": false,
      "hint": "Account identifier of your Snowflake instance. This depends on the cloud platform, such as AWS, Azure, or GCP, and region where your Snowflake instance is hosted. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#how-to-connect-to-snowflake-on-workato",
      "type": "string",
      "name": "host"
    },
    {
      "label": "Warehouse",
      "hint": "Full name of warehouse to perform all operations for this connection. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#warehouse-considerations",
      "type": "string",
      "name": "warehouse"
    },
    {
      "label": "Database name",
      "type": "string",
      "name": "database"
    },
    {
      "label": "Authentication type",
      "default": "key_pair",
      "type": "string",
      "name": "authentication_type",
      "pick_list": [
        [
          "OAuth 2.0",
          "oauth"
        ],
        [
          "Key-pair authentication",
          "key_pair"
        ],
        [
          "Username/Password (Deprecated)",
          "basic"
        ]
      ]
    },
    {
      "label": "User name",
      "type": "string",
      "name": "user"
    },
    {
      "label": "Password",
      "hint": "Snowflake plans to deprecate single-factor password authentication for users by November 2025. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#configure-username-password-authentication",
      "optional": true,
      "type": "string",
      "name": "password"
    },
    {
      "label": "Private key",
      "optional": true,
      "hint": "Paste your private key in PKCS 8 format. Use '\n' characters sequence to join all pem lines into one json string. The Private key field is ignored by the connection when the Password field is provided. Refer to the Snowflake Key Pair Authentication documentation for more information: https://docs.snowflake.com/en/user-guide/key-pair-auth",
      "type": "string",
      "name": "private_key"
    },
    {
      "label": "Private key passphrase",
      "optional": true,
      "hint": "You must enter the passphrase if the private key is encrypted.",
      "type": "string",
      "name": "private_key_passphrase"
    },
    {
      "label": "Client ID",
      "hint": "Refer to the Snowflake connector documentation to obtain a Client ID and Client secret: https://docs.workato.com/connectors/snowflake.html#configuring-oauth-2-0",
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Client secret",
      "hint": "Refer to the Snowflake connector documentation to obtain a Client ID and Client secret: https://docs.workato.com/connectors/snowflake.html#configuring-oauth-2-0",
      "type": "string",
      "name": "client_secret"
    },
    {
      "label": "Role",
      "optional": true,
      "hint": "Specify the role for requests using this connection. This role must be an existing role assigned to the user. Leave blank to use the default role of the user.",
      "type": "string",
      "name": "role"
    },
    {
      "label": "Schema",
      "optional": true,
      "hint": "PUBLIC schema by default",
      "type": "string",
      "name": "schema_name"
    },
    {
      "label": "Use improved datetime handling (Recommended)",
      "optional": true,
      "hint": "Defaults to true. Enable this if you plan to specify the timezone for timestamp columns during insertion and retrieval. Make sure you specify the timezone in the next field.",
      "type": "boolean",
      "name": "improved_datetime_handling"
    },
    {
      "label": "Database timezone",
      "optional": true,
      "hint": "Highly recommended if your database contains timestamps with timezone values. This timezone will be applied to all timestamps inserted to the database. Refer to the Snowflake connector documentation for more information: https://docs.workato.com/connectors/snowflake.html#database-timezone",
      "type": "string",
      "name": "db_timezone",
      "pick_list": [
        [
          "American Samoa",
          "American Samoa"
        ],
        [
          "International Date Line West",
          "International Date Line West"
        ],
        [
          "Midway Island",
          "Midway Island"
        ],
        [
          "Hawaii",
          "Hawaii"
        ],
        [
          "Alaska",
          "Alaska"
        ],
        [
          "Pacific Time (US & Canada)",
          "Pacific Time (US & Canada)"
        ],
        [
          "Tijuana",
          "Tijuana"
        ],
        [
          "Arizona",
          "Arizona"
        ],
        [
          "Chihuahua",
          "Chihuahua"
        ],
        [
          "Mazatlan",
          "Mazatlan"
        ],
        [
          "Mountain Time (US & Canada)",
          "Mountain Time (US & Canada)"
        ],
        [
          "Central America",
          "Central America"
        ],
        [
          "Central Time (US & Canada)",
          "Central Time (US & Canada)"
        ],
        [
          "Guadalajara",
          "Guadalajara"
        ],
        [
          "Mexico City",
          "Mexico City"
        ],
        [
          "Monterrey",
          "Monterrey"
        ],
        [
          "Saskatchewan",
          "Saskatchewan"
        ],
        [
          "Bogota",
          "Bogota"
        ],
        [
          "Eastern Time (US & Canada)",
          "Eastern Time (US & Canada)"
        ],
        [
          "Indiana (East)",
          "Indiana (East)"
        ],
        [
          "Lima",
          "Lima"
        ],
        [
          "Quito",
          "Quito"
        ],
        [
          "Atlantic Time (Canada)",
          "Atlantic Time (Canada)"
        ],
        [
          "Caracas",
          "Caracas"
        ],
        [
          "Georgetown",
          "Georgetown"
        ],
        [
          "La Paz",
          "La Paz"
        ],
        [
          "Santiago",
          "Santiago"
        ],
        [
          "Newfoundland",
          "Newfoundland"
        ],
        [
          "Brasilia",
          "Brasilia"
        ],
        [
          "Buenos Aires",
          "Buenos Aires"
        ],
        [
          "Greenland",
          "Greenland"
        ],
        [
          "Montevideo",
          "Montevideo"
        ],
        [
          "Mid-Atlantic",
          "Mid-Atlantic"
        ],
        [
          "Azores",
          "Azores"
        ],
        [
          "Cape Verde Is.",
          "Cape Verde Is."
        ],
        [
          "Casablanca",
          "Casablanca"
        ],
        [
          "Dublin",
          "Dublin"
        ],
        [
          "Edinburgh",
          "Edinburgh"
        ],
        [
          "Lisbon",
          "Lisbon"
        ],
        [
          "London",
          "London"
        ],
        [
          "Monrovia",
          "Monrovia"
        ],
        [
          "UTC",
          "UTC"
        ],
        [
          "Amsterdam",
          "Amsterdam"
        ],
        [
          "Belgrade",
          "Belgrade"
        ],
        [
          "Berlin",
          "Berlin"
        ],
        [
          "Bern",
          "Bern"
        ],
        [
          "Bratislava",
          "Bratislava"
        ],
        [
          "Brussels",
          "Brussels"
        ],
        [
          "Budapest",
          "Budapest"
        ],
        [
          "Copenhagen",
          "Copenhagen"
        ],
        [
          "Ljubljana",
          "Ljubljana"
        ],
        [
          "Madrid",
          "Madrid"
        ],
        [
          "Paris",
          "Paris"
        ],
        [
          "Prague",
          "Prague"
        ],
        [
          "Rome",
          "Rome"
        ],
        [
          "Sarajevo",
          "Sarajevo"
        ],
        [
          "Skopje",
          "Skopje"
        ],
        [
          "Stockholm",
          "Stockholm"
        ],
        [
          "Vienna",
          "Vienna"
        ],
        [
          "Warsaw",
          "Warsaw"
        ],
        [
          "West Central Africa",
          "West Central Africa"
        ],
        [
          "Zagreb",
          "Zagreb"
        ],
        [
          "Athens",
          "Athens"
        ],
        [
          "Bucharest",
          "Bucharest"
        ],
        [
          "Cairo",
          "Cairo"
        ],
        [
          "Harare",
          "Harare"
        ],
        [
          "Helsinki",
          "Helsinki"
        ],
        [
          "Jerusalem",
          "Jerusalem"
        ],
        [
          "Kaliningrad",
          "Kaliningrad"
        ],
        [
          "Kyiv",
          "Kyiv"
        ],
        [
          "Pretoria",
          "Pretoria"
        ],
        [
          "Riga",
          "Riga"
        ],
        [
          "Sofia",
          "Sofia"
        ],
        [
          "Tallinn",
          "Tallinn"
        ],
        [
          "Vilnius",
          "Vilnius"
        ],
        [
          "Baghdad",
          "Baghdad"
        ],
        [
          "Istanbul",
          "Istanbul"
        ],
        [
          "Kuwait",
          "Kuwait"
        ],
        [
          "Minsk",
          "Minsk"
        ],
        [
          "Moscow",
          "Moscow"
        ],
        [
          "Nairobi",
          "Nairobi"
        ],
        [
          "Riyadh",
          "Riyadh"
        ],
        [
          "St. Petersburg",
          "St. Petersburg"
        ],
        [
          "Tehran",
          "Tehran"
        ],
        [
          "Abu Dhabi",
          "Abu Dhabi"
        ],
        [
          "Baku",
          "Baku"
        ],
        [
          "Muscat",
          "Muscat"
        ],
        [
          "Samara",
          "Samara"
        ],
        [
          "Tbilisi",
          "Tbilisi"
        ],
        [
          "Volgograd",
          "Volgograd"
        ],
        [
          "Yerevan",
          "Yerevan"
        ],
        [
          "Kabul",
          "Kabul"
        ],
        [
          "Ekaterinburg",
          "Ekaterinburg"
        ],
        [
          "Islamabad",
          "Islamabad"
        ],
        [
          "Karachi",
          "Karachi"
        ],
        [
          "Tashkent",
          "Tashkent"
        ],
        [
          "Chennai",
          "Chennai"
        ],
        [
          "Kolkata",
          "Kolkata"
        ],
        [
          "Mumbai",
          "Mumbai"
        ],
        [
          "New Delhi",
          "New Delhi"
        ],
        [
          "Sri Jayawardenepura",
          "Sri Jayawardenepura"
        ],
        [
          "Kathmandu",
          "Kathmandu"
        ],
        [
          "Almaty",
          "Almaty"
        ],
        [
          "Astana",
          "Astana"
        ],
        [
          "Dhaka",
          "Dhaka"
        ],
        [
          "Urumqi",
          "Urumqi"
        ],
        [
          "Rangoon",
          "Rangoon"
        ],
        [
          "Bangkok",
          "Bangkok"
        ],
        [
          "Hanoi",
          "Hanoi"
        ],
        [
          "Jakarta",
          "Jakarta"
        ],
        [
          "Krasnoyarsk",
          "Krasnoyarsk"
        ],
        [
          "Novosibirsk",
          "Novosibirsk"
        ],
        [
          "Beijing",
          "Beijing"
        ],
        [
          "Chongqing",
          "Chongqing"
        ],
        [
          "Hong Kong",
          "Hong Kong"
        ],
        [
          "Irkutsk",
          "Irkutsk"
        ],
        [
          "Kuala Lumpur",
          "Kuala Lumpur"
        ],
        [
          "Perth",
          "Perth"
        ],
        [
          "Singapore",
          "Singapore"
        ],
        [
          "Taipei",
          "Taipei"
        ],
        [
          "Ulaanbaatar",
          "Ulaanbaatar"
        ],
        [
          "Osaka",
          "Osaka"
        ],
        [
          "Sapporo",
          "Sapporo"
        ],
        [
          "Seoul",
          "Seoul"
        ],
        [
          "Tokyo",
          "Tokyo"
        ],
        [
          "Yakutsk",
          "Yakutsk"
        ],
        [
          "Adelaide",
          "Adelaide"
        ],
        [
          "Darwin",
          "Darwin"
        ],
        [
          "Brisbane",
          "Brisbane"
        ],
        [
          "Canberra",
          "Canberra"
        ],
        [
          "Guam",
          "Guam"
        ],
        [
          "Hobart",
          "Hobart"
        ],
        [
          "Melbourne",
          "Melbourne"
        ],
        [
          "Port Moresby",
          "Port Moresby"
        ],
        [
          "Sydney",
          "Sydney"
        ],
        [
          "Vladivostok",
          "Vladivostok"
        ],
        [
          "Magadan",
          "Magadan"
        ],
        [
          "New Caledonia",
          "New Caledonia"
        ],
        [
          "Solomon Is.",
          "Solomon Is."
        ],
        [
          "Srednekolymsk",
          "Srednekolymsk"
        ],
        [
          "Auckland",
          "Auckland"
        ],
        [
          "Fiji",
          "Fiji"
        ],
        [
          "Kamchatka",
          "Kamchatka"
        ],
        [
          "Marshall Is.",
          "Marshall Is."
        ],
        [
          "Wellington",
          "Wellington"
        ],
        [
          "Chatham Is.",
          "Chatham Is."
        ],
        [
          "Nuku'alofa",
          "Nuku'alofa"
        ],
        [
          "Samoa",
          "Samoa"
        ],
        [
          "Tokelau Is.",
          "Tokelau Is."
        ]
      ]
    }
  ]
}
```

* * *

### Splunk

**Provider value:**

```json
"provider": "splunk"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "server_url",
                  "type": "string",
                  "label": "Server URL",
                  "hint": "                   The URL of the Splunk management port (for example, https://yourdomain:8089).\n                   You MUST install the <a href='https://splunkbase.splunk.com/apps/#/search/workato'>Workato Add-on for Splunk</a> first.\n"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username",
                  "hint": "The Splunk username (for example, admin)"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password",
                  "hint": "The password for the Splunk username"
              }
          ]
      }
```

* * *

### SQL Server

**Provider value:**

```json
"provider": "mssql"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username",
                  "hint": "For Azure SQL use username@server"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "optional": true,
                  "label": "Port",
                  "hint": "Port number, default is 1433",
                  "default": 1433
              },
              {
                  "name": "database",
                  "type": "string",
                  "label": "Database"
              },
              {
                  "name": "azure",
                  "type": "boolean",
                  "optional": true,
                  "label": "Azure SQL",
                  "hint": "Choose 'yes' if connecting to Azure SQL",
                  "default": "false"
              }
          ]
      }
```

* * *

### SQL Server (Secondary)

**Provider value:**

```json
"provider": "mssql_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "profile",
                  "type": "string",
                  "label": "On-prem connection profile"
              },
              {
                  "name": "username",
                  "type": "string",
                  "label": "Username",
                  "hint": "For Azure SQL use username@server"
              },
              {
                  "name": "password",
                  "type": "string",
                  "label": "Password"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Host"
              },
              {
                  "name": "port",
                  "type": "string",
                  "optional": true,
                  "label": "Port",
                  "hint": "Port number, default is 1433",
                  "default": 1433
              },
              {
                  "name": "database",
                  "type": "string",
                  "label": "Database"
              },
              {
                  "name": "azure",
                  "type": "boolean",
                  "optional": true,
                  "label": "Azure SQL",
                  "hint": "Choose 'yes' if connecting to Azure SQL",
                  "default": "false"
              }
          ]
      }
```

* * *

### Stripe

**Provider value:**

```json
"provider": "stripe"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "oauth_token_pair": {
    "label": "OAuth Token Pair",
    "optional": true,
    "type": "object",
    "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
    "properties": [
      {
        "label": "Access Token",
        "name": "access_token",
        "type": "string",
        "optional": false
      },
      {
        "label": "Refresh Token",
        "name": "refresh_token",
        "type": "string",
        "optional": false
      }
    ]
  },
  "input": [
    {
      "label": "Authentication type",
      "default": "oauth2_auth_code_grant",
      "hint": "Select the authentication type.",
      "optional": false,
      "type": "string",
      "name": "authentication_type",
      "pick_list": [
        [
          "Authorization code grant",
          "oauth2_auth_code_grant"
        ],
        [
          "API key",
          "api_key"
        ]
      ]
    },
    {
      "label": "Demo",
      "default": "false",
      "optional": true,
      "hint": "Specify whether this connection is for a demo account.",
      "type": "boolean",
      "name": "demo"
    },
    {
      "label": "API key",
      "optional": false,
      "hint": "Provide your Stripe API secret key. Go to 'Developers dashboard > API keys' to manage your API keys. Provide the test mode secret key to access test mode data. Otherwise, provide the live mode secret key to access actual account data. Refer to the Stripe documentation to learn more: https://docs.stripe.com/keys",
      "type": "string",
      "name": "api_key"
    }
  ]
}
```

* * *

### SuccessFactors

**Provider value:**

```json
"provider": "success_factors"
```

View connection parameters JSON

```json
{
  "oauth": false,
  "personalization": true,
  "input": [
    {
      "type": "string",
      "name": "authentication",
      "label": "Authentication type",
      "optional": false,
      "pick_list": [
        [
          "Basic",
          "basic"
        ],
        [
          "OAuth 2.0",
          "oauth2"
        ]
      ]
    },
    {
      "name": "odata_version",
      "label": "OData version",
      "hint": "Select the OData version of your SAP system. Odata v4 is only supported by Oauth 2.0 authentication. Defaults to OData V2 if left blank.",
      "optional": true,
      "type": "string",
      "default": "v2",
      "pick_list": [
        [
          "OData V2",
          "v2"
        ],
        [
          "OData V4",
          "v4"
        ]
      ]
    },
    {
      "label": "Company ID",
      "optional": false,
      "hint": "Enter your company ID. Select 'Show Version Information' from the profile drop-down menu in SuccessFactors to find your Company ID, or retrieve the ID from the URL after 'company='. Refer to the SuccessFactors connector documentation for more information: https://docs.workato.com/connectors/successfactors/successfactors.html#connection-setup",
      "type": "string",
      "name": "company"
    },
    {
      "label": "User ID",
      "optional": false,
      "hint": "Enter your SAP SuccessFactors user ID.",
      "type": "string",
      "name": "user_id"
    },
    {
      "label": "Password",
      "optional": false,
      "type": "string",
      "name": "password"
    },
    {
      "label": "Client ID",
      "optional": false,
      "hint": "Enter the OAuth client ID. You can generate this API Key in the SAP SuccessFactors API Center.",
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Private key",
      "optional": false,
      "hint": "Enter the X.509 private key that signs SAML assertion. You can use the private key of a self-signed X.509 certificate or the private key of an X.509 certificate generated by SAP SuccessFactors. The private key is a base64-encoded string enclosed between -----BEGIN ENCRYPTED PRIVATE KEY----- and ----- END ENCRYPTED PRIVATE KEY-----. Enter only the enclosed string without the beginning and ending lines to avoid an error.",
      "type": "string",
      "name": "private_key"
    },
    {
      "label": "Environment",
      "optional": false,
      "hint": "Select your corresponding SuccessFactors environment. Refer to the following knowledge base to find the mapping between your API endpoint and SuccessFactors environment: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/af2b8d5437494b12be88fe374eba75b6.html",
      "type": "string",
      "name": "environment",
      "pick_list": [
        [
          "DC2 (DC57) Production",
          "https://api2.successfactors.eu"
        ],
        [
          "DC2 (DC57) SalesDemo",
          "https://apisalesdemo2.successfactors.eu"
        ],
        [
          "DC2 (DC57) Preview",
          "https://api2preview.sapsf.eu"
        ],
        [
          "DC4 (DC68) Production",
          "https://api4.successfactors.com"
        ],
        [
          "DC4 (DC68) SalesDemo",
          "https://api68sales.successfactors.com"
        ],
        [
          "DC4 (DC68) Preview",
          "https://api4preview.sapsf.com"
        ],
        [
          "DC8 (DC70) Production",
          "https://api8.successfactors.com"
        ],
        [
          "DC8 (DC70) SalesDemo",
          "https://apisalesdemo8.successfactors.com"
        ],
        [
          "DC8 (DC70) Preview",
          "https://api8preview.sapsf.com"
        ],
        [
          "DC10 (DC66) Production",
          "https://api10.successfactors.com"
        ],
        [
          "DC10 (DC66) Preview",
          "https://api10preview.sapsf.com"
        ],
        [
          "DC12 (DC33) Production",
          "https://api012.successfactors.eu"
        ],
        [
          "DC12 Rot",
          "https://apirot.successfactors.eu"
        ],
        [
          "DC12 (DC33) Preview",
          "https://api12preview.sapsf.eu"
        ],
        [
          "DC15 (DC30) Production",
          "https://api15.sapsf.cn"
        ],
        [
          "DC15 (DC30) Preview",
          "https://api15preview.sapsf.cn"
        ],
        [
          "DC16 Production",
          "https://api16.sapsf.eu"
        ],
        [
          "DC17 (DC60) Preview",
          "https://api17preview.sapsf.com"
        ],
        [
          "DC17 (DC60) Production",
          "https://api17.sapsf.com"
        ],
        [
          "DC18 Preview",
          "https://api18preview.sapsf.com"
        ],
        [
          "DC18 Production",
          "https://api18.sapsf.com"
        ],
        [
          "DC19 (DC62) Preview",
          "https://api19preview.sapsf.com"
        ],
        [
          "DC19 (DC62) Production",
          "https://api19.sapsf.com"
        ],
        [
          "DC22 Preview",
          "https://api22preview.sapsf.com"
        ],
        [
          "DC22 Production",
          "https://api22.sapsf.com"
        ],
        [
          "DC23 Preview",
          "https://api23preview.sapsf.com"
        ],
        [
          "DC23 Production",
          "https://api23.sapsf.com"
        ],
        [
          "DC40 SalesDemo",
          "https://api40sales.sapsf.com"
        ],
        [
          "DC41 Preview",
          "https://api41preview.sapsf.com"
        ],
        [
          "DC41 Production",
          "https://api41.sapsf.com"
        ],
        [
          "DC42 Preview",
          "https://api42preview.sapsf.com"
        ],
        [
          "DC42 Production",
          "https://api42.sapsf.com"
        ],
        [
          "DC44 (DC52) Preview",
          "https://api44preview.sapsf.com"
        ],
        [
          "DC44 (DC52) Production",
          "https://api44.sapsf.com"
        ],
        [
          "DC47 Preview",
          "https://api47preview.sapsf.com"
        ],
        [
          "DC47 Production",
          "https://api47.sapsf.com"
        ],
        [
          "DC50 Preview",
          "https://api50preview.sapsf.com"
        ],
        [
          "DC50 Production",
          "https://api50.sapsf.com"
        ],
        [
          "DC55 Preview",
          "https://api55preview.sapsf.eu"
        ],
        [
          "DC55 Production",
          "https://api55.sapsf.eu"
        ],
        [
          "DC74 Preview",
          "https://api74preview.sapsf.eu"
        ],
        [
          "DC74 Production",
          "https://api74.sapsf.eu"
        ]
      ]
    },
    {
      "label": "Application interface key",
      "optional": true,
      "hint": "When left blank, defaults to Workato's application interface key.",
      "type": "string",
      "name": "application_interface_key"
    },
    {
      "label": "API server Timezone",
      "optional": true,
      "hint": "Select the API server standard UTC time zone. For example, -0500 for DC8 Production environment. Refer to the SAP documentaion for more information about tenant and server time zones: https://help.sap.com/docs/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/8e0d540f96474717bbf18df51e54e522/d5e86fa8bb564058820592217d3a21d4.html",
      "type": "string",
      "name": "timezone",
      "pick_list": [
        [
          "UTC",
          "UTC"
        ],
        [
          "UTC +1",
          "+0100"
        ],
        [
          "UTC +8",
          "+0800"
        ],
        [
          "UTC +10",
          "+1000"
        ],
        [
          "UTC -5",
          "-0500"
        ]
      ]
    }
  ]
}
```

* * *

### SurveyMonkey

**Provider value:**

```json
"provider": "surveymonkey"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Tango Card

**Provider value:**

```json
"provider": "tango_card"
```

* * *

### TaskRay

**Provider value:**

```json
"provider": "taskray"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### TrackVia

**Provider value:**

```json
"provider": "trackvia"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "custom_domain",
                  "type": "string",
                  "optional": "true",
                  "label": "TrackVia subdomain",
                  "hint": "Enter your TrackVia subdomain. For example, customdomain.trackvia.com. By default, <b>go.trackvia.com</b> will be used."
              }
          ]
      }
```

* * *

### Tradeshift

**Provider value:**

```json
"provider": "tradeshift"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "              If <b>yes</b>, click <a target='_blank' href=https://sandbox.tradeshift.com/#/apps/Tradeshift.AppStore/apps/Workato.tradeshiftAdapterProduction>here</a> to activate your sandbox account else click <a target='_blank' href=https://go.tradeshift.com/#/apps/Tradeshift.AppStore/apps/Workato.tradeshiftAdapterProduction>here</a> to activate your production account.\n",
                  "default": "false"
              }
          ]
      }
```

* * *

### Trello

**Provider value:**

```json
"provider": "trello"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### TSheets

**Provider value:**

```json
"provider": "tsheets"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Twilio

**Provider value:**

```json
"provider": "twilio"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "sid",
                  "type": "string",
                  "label": "Account SID",
                  "hint": "See your Twilio <a href=\"https://www.twilio.com/user/account\">account page</a>"
              },
              {
                  "name": "token",
                  "type": "string",
                  "label": "Auth token",
                  "hint": "See your Twilio <a href=\"https://www.twilio.com/user/account\">account page</a>"
              }
          ]
      }
```

* * *

### Twitter

**Provider value:**

```json
"provider": "twitter"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Twitter Ads

**Provider value:**

```json
"provider": "twitter_ads"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Unbounce

**Provider value:**

```json
"provider": "unbounce"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "Api key",
                  "hint": "Profile (top right) > Manage Account > API Access"
              }
          ]
      }
```

* * *

### Variables by Workato

**Provider value:**

```json
"provider": "workato_variable"
```

* * *

### Veeva CRM

**Provider value:**

```json
"provider": "veeva"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### Vend

**Provider value:**

```json
"provider": "vend"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Vlocity

**Provider value:**

```json
"provider": "vlocity"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "sandbox",
                  "type": "boolean",
                  "optional": true,
                  "label": "Sandbox",
                  "hint": "Is this connecting to a sandbox account?",
                  "default": "false"
              }
          ]
      }
```

* * *

### Watson Tone Analyzer

**Provider value:**

```json
"provider": "watson_tone_analyzer"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "username",
                  "type": "string",
                  "optional": false,
                  "label": "Username",
                  "hint": "Require Cloud Foundry service credentials. <a href='https://cloud.ibm.com/docs/services/watson?topic=watson-creating-credentials#creating-credentials' target='_blank'>Learn more</a>"
              },
              {
                  "name": "password",
                  "type": "string",
                  "optional": false,
                  "label": "Password",
                  "hint": "Require Cloud Foundry service credentials. <a href='https://cloud.ibm.com/docs/services/watson?topic=watson-creating-credentials#creating-credentials' target='_blank'>Learn more</a>"
              }
          ]
      }
```

* * *

### Webhooks

**Provider value:**

```json
"provider": "workato_webhooks"
```

* * *

### WebMerge

**Provider value:**

```json
"provider": "webmerge"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "optional": false,
                  "label": "API key",
                  "hint": "Select your profile icon->Api Access to get the API key"
              },
              {
                  "name": "api_secret",
                  "type": "string",
                  "optional": false,
                  "label": "API secret",
                  "hint": "Select your profile icon->Api Access to get the API secret"
              }
          ]
      }
```

* * *

### WooCommerce

**Provider value:**

```json
"provider": "woocommerce"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "consumer_key",
                  "type": "string",
                  "label": "Consumer key",
                  "hint": "Consumer key is found at API tab of WooCommerce settings"
              },
              {
                  "name": "consumer_secret",
                  "type": "string",
                  "label": "Consumer secret",
                  "hint": "Consumer secret is found at API tab of WooCommerce settings"
              },
              {
                  "name": "host",
                  "type": "string",
                  "label": "Host",
                  "hint": "If your WooCommerce home page url is https://app.Woocommerce.com, then use app.Woocommerce.com"
              },
              {
                  "name": "order_ids",
                  "type": "string",
                  "optional": true,
                  "label": "Example order IDs",
                  "hint": "Comma separated order IDs to sample custom fields. Takes up to 3 values"
              }
          ]
      }
```

* * *

### WordPress.com

**Provider value:**

```json
"provider": "word_press"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Workbot for Microsoft Teams

**Provider value:**

```json
"provider": "teams_bot"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Workbot for Microsoft Teams Old

**Provider value:**

```json
"provider": "skype_bot"
```

Connection parameter configuration **_is not required_** for this connector.

* * *

### Workbot for Slack

**Provider value:**

```json
"provider": "slack_bot"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "nlu_provider_shared_account_id",
                  "type": "string",
                  "optional": true,
                  "label": "NLU provider",
                  "hint": "Choose a connection for your conversational interface. Supports Google's DialogFlow and Amazon Lex."
              },
              {
                  "name": "advanced",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced",
                  "hint": "Additional fields that are not needed for most users",
                  "properties":
                  [
                      {
                          "name": "extra_tokens",
                          "type": "string",
                          "optional": true,
                          "label": "Slash commands verification tokens",
                          "hint": "Used for invoking Custom Integration slash commands. Each slash command has a token. Separate tokens with commas to support multiple slash commands. <a href='https://docs.workato.com/workbot/legacy-slash-commands.html#configuring-the-workbot-connection' target='_blank'>Learn more.</a>"
                      },
                      {
                          "name": "custom_help",
                          "type": "string",
                          "optional": true,
                          "label": "Custom help",
                          "hint": "Provide simple text help OR rich help using a JSON document corresponding to Slack message.You can build a rich help message using the <a href='https://api.slack.com/docs/messages/builder' target='_blank'>Slack message builder.</a>"
                      }
                  ]
              }
          ]
      }
```

* * *

### Workday

**Provider value:**

```json
"provider": "workday"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": false,
  "oauth_token_pair": {
    "label": "OAuth Token Pair",
    "optional": true,
    "type": "object",
    "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
    "properties": [
      {
        "label": "Access Token",
        "name": "access_token",
        "type": "string",
        "optional": false
      },
      {
        "label": "Refresh Token",
        "name": "refresh_token",
        "type": "string",
        "optional": false
      }
    ]
  },
  "input": [
    {
      "label": "Authentication type",
      "optional": false,
      "default": "oauth2_auth_code_grant",
      "hint": "Select the authentication type. OAuth2.0 is required to work with custom objects and WQL.",
      "type": "string",
      "name": "authentication_type",
      "pick_list": [
        [
          "OAuth 2.0",
          "oauth2_auth_code_grant"
        ],
        [
          "Basic",
          "basic"
        ],
        [
          "Hybrid (Deprecated)",
          "hybrid"
        ]
      ]
    },
    {
      "label": "Tenant ID",
      "hint": "You can find your Tenant ID in the Workday URL while you are logged in. For example the tenant ID is sample_company in the following URL: https://impl.workday.com/sample_company/d/home.html",
      "type": "string",
      "name": "tenant_id"
    },
    {
      "label": "WSDL URL",
      "hint": "Requires a wsdl url. Refer to Workday for more information: https://community.workday.com/articles/6120#endpoint",
      "default": "https://wd2-impl-services1.workday.com/ccx/service/",
      "type": "string",
      "name": "base_uri"
    },
    {
      "label": "Login name",
      "type": "string",
      "name": "login"
    },
    {
      "label": "Password",
      "type": "string",
      "name": "password"
    },
    {
      "label": "Client ID",
      "hint": "Found in API Client settings",
      "optional": false,
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Client secret",
      "hint": "Found in API Client settings",
      "optional": false,
      "type": "string",
      "name": "client_secret"
    },
    {
      "label": "Refresh token",
      "hint": "Enter a refresh token to use an API client for Integrations.",
      "optional": true,
      "type": "string",
      "name": "refresh_token"
    },
    {
      "label": "Authorization endpoint",
      "hint": "You can find the authorization endpoint in the Workday API Client settings.",
      "optional": false,
      "type": "string",
      "name": "authorization_endpoint"
    },
    {
      "label": "Token endpoint",
      "hint": "You can find the token endpoint in the Workday API Client settings.",
      "optional": false,
      "type": "string",
      "name": "token_endpoint"
    },
    {
      "label": "Workday tenant timezone",
      "optional": true,
      "hint": "Enter your Workday tenant timezone. You can find the tenant timezone in your Workday tenant settings. Workday returns data effective from the current day in PST time by default. This may differ from your Workday tenant's timezone. Selecting a timezone makes data retrieved consistent with your Workday tenant.",
      "type": "string",
      "name": "time_zone",
      "pick_list": [
        [
          "American Samoa",
          "American Samoa"
        ],
        [
          "International Date Line West",
          "International Date Line West"
        ],
        [
          "Midway Island",
          "Midway Island"
        ],
        [
          "Hawaii",
          "Hawaii"
        ],
        [
          "Alaska",
          "Alaska"
        ],
        [
          "Pacific Time (US & Canada)",
          "Pacific Time (US & Canada)"
        ],
        [
          "Tijuana",
          "Tijuana"
        ],
        [
          "Arizona",
          "Arizona"
        ],
        [
          "Chihuahua",
          "Chihuahua"
        ],
        [
          "Mazatlan",
          "Mazatlan"
        ],
        [
          "Mountain Time (US & Canada)",
          "Mountain Time (US & Canada)"
        ],
        [
          "Central America",
          "Central America"
        ],
        [
          "Central Time (US & Canada)",
          "Central Time (US & Canada)"
        ],
        [
          "Guadalajara",
          "Guadalajara"
        ],
        [
          "Mexico City",
          "Mexico City"
        ],
        [
          "Monterrey",
          "Monterrey"
        ],
        [
          "Saskatchewan",
          "Saskatchewan"
        ],
        [
          "Bogota",
          "Bogota"
        ],
        [
          "Eastern Time (US & Canada)",
          "Eastern Time (US & Canada)"
        ],
        [
          "Indiana (East)",
          "Indiana (East)"
        ],
        [
          "Lima",
          "Lima"
        ],
        [
          "Quito",
          "Quito"
        ],
        [
          "Atlantic Time (Canada)",
          "Atlantic Time (Canada)"
        ],
        [
          "Caracas",
          "Caracas"
        ],
        [
          "Georgetown",
          "Georgetown"
        ],
        [
          "La Paz",
          "La Paz"
        ],
        [
          "Santiago",
          "Santiago"
        ],
        [
          "Newfoundland",
          "Newfoundland"
        ],
        [
          "Brasilia",
          "Brasilia"
        ],
        [
          "Buenos Aires",
          "Buenos Aires"
        ],
        [
          "Greenland",
          "Greenland"
        ],
        [
          "Montevideo",
          "Montevideo"
        ],
        [
          "Mid-Atlantic",
          "Mid-Atlantic"
        ],
        [
          "Azores",
          "Azores"
        ],
        [
          "Cape Verde Is.",
          "Cape Verde Is."
        ],
        [
          "Casablanca",
          "Casablanca"
        ],
        [
          "Dublin",
          "Dublin"
        ],
        [
          "Edinburgh",
          "Edinburgh"
        ],
        [
          "Lisbon",
          "Lisbon"
        ],
        [
          "London",
          "London"
        ],
        [
          "Monrovia",
          "Monrovia"
        ],
        [
          "UTC",
          "UTC"
        ],
        [
          "Amsterdam",
          "Amsterdam"
        ],
        [
          "Belgrade",
          "Belgrade"
        ],
        [
          "Berlin",
          "Berlin"
        ],
        [
          "Bern",
          "Bern"
        ],
        [
          "Bratislava",
          "Bratislava"
        ],
        [
          "Brussels",
          "Brussels"
        ],
        [
          "Budapest",
          "Budapest"
        ],
        [
          "Copenhagen",
          "Copenhagen"
        ],
        [
          "Ljubljana",
          "Ljubljana"
        ],
        [
          "Madrid",
          "Madrid"
        ],
        [
          "Paris",
          "Paris"
        ],
        [
          "Prague",
          "Prague"
        ],
        [
          "Rome",
          "Rome"
        ],
        [
          "Sarajevo",
          "Sarajevo"
        ],
        [
          "Skopje",
          "Skopje"
        ],
        [
          "Stockholm",
          "Stockholm"
        ],
        [
          "Vienna",
          "Vienna"
        ],
        [
          "Warsaw",
          "Warsaw"
        ],
        [
          "West Central Africa",
          "West Central Africa"
        ],
        [
          "Zagreb",
          "Zagreb"
        ],
        [
          "Athens",
          "Athens"
        ],
        [
          "Bucharest",
          "Bucharest"
        ],
        [
          "Cairo",
          "Cairo"
        ],
        [
          "Harare",
          "Harare"
        ],
        [
          "Helsinki",
          "Helsinki"
        ],
        [
          "Jerusalem",
          "Jerusalem"
        ],
        [
          "Kaliningrad",
          "Kaliningrad"
        ],
        [
          "Kyiv",
          "Kyiv"
        ],
        [
          "Pretoria",
          "Pretoria"
        ],
        [
          "Riga",
          "Riga"
        ],
        [
          "Sofia",
          "Sofia"
        ],
        [
          "Tallinn",
          "Tallinn"
        ],
        [
          "Vilnius",
          "Vilnius"
        ],
        [
          "Baghdad",
          "Baghdad"
        ],
        [
          "Istanbul",
          "Istanbul"
        ],
        [
          "Kuwait",
          "Kuwait"
        ],
        [
          "Minsk",
          "Minsk"
        ],
        [
          "Moscow",
          "Moscow"
        ],
        [
          "Nairobi",
          "Nairobi"
        ],
        [
          "Riyadh",
          "Riyadh"
        ],
        [
          "St. Petersburg",
          "St. Petersburg"
        ],
        [
          "Tehran",
          "Tehran"
        ],
        [
          "Abu Dhabi",
          "Abu Dhabi"
        ],
        [
          "Baku",
          "Baku"
        ],
        [
          "Muscat",
          "Muscat"
        ],
        [
          "Samara",
          "Samara"
        ],
        [
          "Tbilisi",
          "Tbilisi"
        ],
        [
          "Volgograd",
          "Volgograd"
        ],
        [
          "Yerevan",
          "Yerevan"
        ],
        [
          "Kabul",
          "Kabul"
        ],
        [
          "Ekaterinburg",
          "Ekaterinburg"
        ],
        [
          "Islamabad",
          "Islamabad"
        ],
        [
          "Karachi",
          "Karachi"
        ],
        [
          "Tashkent",
          "Tashkent"
        ],
        [
          "Chennai",
          "Chennai"
        ],
        [
          "Kolkata",
          "Kolkata"
        ],
        [
          "Mumbai",
          "Mumbai"
        ],
        [
          "New Delhi",
          "New Delhi"
        ],
        [
          "Sri Jayawardenepura",
          "Sri Jayawardenepura"
        ],
        [
          "Kathmandu",
          "Kathmandu"
        ],
        [
          "Almaty",
          "Almaty"
        ],
        [
          "Astana",
          "Astana"
        ],
        [
          "Dhaka",
          "Dhaka"
        ],
        [
          "Urumqi",
          "Urumqi"
        ],
        [
          "Rangoon",
          "Rangoon"
        ],
        [
          "Bangkok",
          "Bangkok"
        ],
        [
          "Hanoi",
          "Hanoi"
        ],
        [
          "Jakarta",
          "Jakarta"
        ],
        [
          "Krasnoyarsk",
          "Krasnoyarsk"
        ],
        [
          "Novosibirsk",
          "Novosibirsk"
        ],
        [
          "Beijing",
          "Beijing"
        ],
        [
          "Chongqing",
          "Chongqing"
        ],
        [
          "Hong Kong",
          "Hong Kong"
        ],
        [
          "Irkutsk",
          "Irkutsk"
        ],
        [
          "Kuala Lumpur",
          "Kuala Lumpur"
        ],
        [
          "Perth",
          "Perth"
        ],
        [
          "Singapore",
          "Singapore"
        ],
        [
          "Taipei",
          "Taipei"
        ],
        [
          "Ulaanbaatar",
          "Ulaanbaatar"
        ],
        [
          "Osaka",
          "Osaka"
        ],
        [
          "Sapporo",
          "Sapporo"
        ],
        [
          "Seoul",
          "Seoul"
        ],
        [
          "Tokyo",
          "Tokyo"
        ],
        [
          "Yakutsk",
          "Yakutsk"
        ],
        [
          "Adelaide",
          "Adelaide"
        ],
        [
          "Darwin",
          "Darwin"
        ],
        [
          "Brisbane",
          "Brisbane"
        ],
        [
          "Canberra",
          "Canberra"
        ],
        [
          "Guam",
          "Guam"
        ],
        [
          "Hobart",
          "Hobart"
        ],
        [
          "Melbourne",
          "Melbourne"
        ],
        [
          "Port Moresby",
          "Port Moresby"
        ],
        [
          "Sydney",
          "Sydney"
        ],
        [
          "Vladivostok",
          "Vladivostok"
        ],
        [
          "Magadan",
          "Magadan"
        ],
        [
          "New Caledonia",
          "New Caledonia"
        ],
        [
          "Solomon Is.",
          "Solomon Is."
        ],
        [
          "Srednekolymsk",
          "Srednekolymsk"
        ],
        [
          "Auckland",
          "Auckland"
        ],
        [
          "Fiji",
          "Fiji"
        ],
        [
          "Kamchatka",
          "Kamchatka"
        ],
        [
          "Marshall Is.",
          "Marshall Is."
        ],
        [
          "Wellington",
          "Wellington"
        ],
        [
          "Chatham Is.",
          "Chatham Is."
        ],
        [
          "Nuku'alofa",
          "Nuku'alofa"
        ],
        [
          "Samoa",
          "Samoa"
        ],
        [
          "Tokelau Is.",
          "Tokelau Is."
        ]
      ]
    },
    {
      "label": "Advanced settings",
      "optional": true,
      "type": "object",
      "name": "advanced_settings",
      "properties": [
        {
          "label": "Advanced XML payload for multiple ID values",
          "default": "false",
          "optional": true,
          "hint": "Fields with multiple values are each wrapped within a container by default. Setting the value to 'yes' unwraps the values. Refer to the Workday connector documentation for more information: https://docs.workato.com/connectors/workday.html#workday-connector",
          "type": "boolean",
          "name": "unwrap_arrays"
        }
      ]
    }
  ]
}
```

* * *

### Workday REST

**Provider value:**

```json
"provider": "workday_rest"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "rest_api_endpoint",
                  "type": "string",
                  "label": "REST API endpoint",
                  "hint": "                 Found in the API client details page. Learn how to register an API client\n                 <a href='https://docs.workato.com/connectors/workday/connection_setup.html#register-api-client' target=_blank>here</a>.\n",
                  "default": "https://wd2-impl-services1.workday.com/ccx/service/acme"
              },
              {
                  "name": "authorization_endpoint",
                  "type": "string",
                  "label": "Authorization endpoint",
                  "hint": "Found in the API client details page."
              },
              {
                  "name": "token_endpoint",
                  "type": "string",
                  "label": "Token endpoint",
                  "hint": "Found in the API client details page."
              },
              {
                  "name": "client_id",
                  "type": "string",
                  "label": "Client ID",
                  "hint": "Found in the API client details page."
              },
              {
                  "name": "client_secret",
                  "type": "string",
                  "label": "Client secret",
                  "hint": "Found in the API client details page."
              },
              {
                  "name": "refresh_token",
                  "type": "string",
                  "optional": true,
                  "label": "Refresh token",
                  "hint": "                 Provide a refresh token if this connection needs to be authorized by an integration user instead of a user account.\n                 Authorization step will be skipped.\n"
              }
          ]
      }
```

* * *

### Workday Web Services

**Provider value:**

```json
"provider": "workday_oauth"
```

* * *

### Workfront

**Provider value:**

```json
"provider": "workfront"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "oauth_token_pair": {
    "label": "OAuth Token Pair",
    "optional": true,
    "type": "object",
    "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
    "properties": [
      {
        "label": "Access Token",
        "name": "access_token",
        "type": "string",
        "optional": false
      },
      {
        "label": "Refresh Token",
        "name": "refresh_token",
        "type": "string",
        "optional": false
      }
    ]
  },
  "input": [
    {
      "label": "Authentication type",
      "hint": "Select authentication type",
      "optional": false,
      "default": "api_key",
      "type": "string",
      "name": "authentication_type",
      "pick_list": [
        [
          "OAuth 2.0",
          "oauth2_auth_code_grant"
        ],
        [
          "API key",
          "api_key"
        ]
      ]
    },
    {
      "label": "API key",
      "optional": false,
      "hint": "Your Workfront API key",
      "type": "string",
      "name": "api_key"
    },
    {
      "label": "Client ID",
      "optional": false,
      "hint": "Go to 'Setup > System > OAuth2 Applications > Client ID' to create a client ID and secret.",
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Client secret",
      "optional": false,
      "hint": "Go to 'Setup > System > OAuth2 Applications > Client secret' to create a client ID and secret.",
      "type": "string",
      "name": "client_secret"
    },
    {
      "label": "Subdomain",
      "optional": false,
      "hint": "Enter your Workfront subdomain name as found in your Workfront URL.",
      "type": "string",
      "name": "subdomain"
    },
    {
      "label": "API version",
      "default": "14.0",
      "hint": "Enter the API version to use in your connection. The default version is 14.0",
      "optional": true,
      "type": "string",
      "name": "api_version"
    },
    {
      "label": "Account timezone",
      "optional": true,
      "hint": "Enter an account timezone for consistency with Workfront. All date and time fields are converted to this timezone.",
      "type": "string",
      "name": "timezone",
      "pick_list": [
        [
          "American Samoa",
          "American Samoa"
        ],
        [
          "International Date Line West",
          "International Date Line West"
        ],
        [
          "Midway Island",
          "Midway Island"
        ],
        [
          "Hawaii",
          "Hawaii"
        ],
        [
          "Alaska",
          "Alaska"
        ],
        [
          "Pacific Time (US & Canada)",
          "Pacific Time (US & Canada)"
        ],
        [
          "Tijuana",
          "Tijuana"
        ],
        [
          "Arizona",
          "Arizona"
        ],
        [
          "Chihuahua",
          "Chihuahua"
        ],
        [
          "Mazatlan",
          "Mazatlan"
        ],
        [
          "Mountain Time (US & Canada)",
          "Mountain Time (US & Canada)"
        ],
        [
          "Central America",
          "Central America"
        ],
        [
          "Central Time (US & Canada)",
          "Central Time (US & Canada)"
        ],
        [
          "Guadalajara",
          "Guadalajara"
        ],
        [
          "Mexico City",
          "Mexico City"
        ],
        [
          "Monterrey",
          "Monterrey"
        ],
        [
          "Saskatchewan",
          "Saskatchewan"
        ],
        [
          "Bogota",
          "Bogota"
        ],
        [
          "Eastern Time (US & Canada)",
          "Eastern Time (US & Canada)"
        ],
        [
          "Indiana (East)",
          "Indiana (East)"
        ],
        [
          "Lima",
          "Lima"
        ],
        [
          "Quito",
          "Quito"
        ],
        [
          "Atlantic Time (Canada)",
          "Atlantic Time (Canada)"
        ],
        [
          "Caracas",
          "Caracas"
        ],
        [
          "Georgetown",
          "Georgetown"
        ],
        [
          "La Paz",
          "La Paz"
        ],
        [
          "Santiago",
          "Santiago"
        ],
        [
          "Newfoundland",
          "Newfoundland"
        ],
        [
          "Brasilia",
          "Brasilia"
        ],
        [
          "Buenos Aires",
          "Buenos Aires"
        ],
        [
          "Greenland",
          "Greenland"
        ],
        [
          "Montevideo",
          "Montevideo"
        ],
        [
          "Mid-Atlantic",
          "Mid-Atlantic"
        ],
        [
          "Azores",
          "Azores"
        ],
        [
          "Cape Verde Is.",
          "Cape Verde Is."
        ],
        [
          "Casablanca",
          "Casablanca"
        ],
        [
          "Dublin",
          "Dublin"
        ],
        [
          "Edinburgh",
          "Edinburgh"
        ],
        [
          "Lisbon",
          "Lisbon"
        ],
        [
          "London",
          "London"
        ],
        [
          "Monrovia",
          "Monrovia"
        ],
        [
          "UTC",
          "UTC"
        ],
        [
          "Amsterdam",
          "Amsterdam"
        ],
        [
          "Belgrade",
          "Belgrade"
        ],
        [
          "Berlin",
          "Berlin"
        ],
        [
          "Bern",
          "Bern"
        ],
        [
          "Bratislava",
          "Bratislava"
        ],
        [
          "Brussels",
          "Brussels"
        ],
        [
          "Budapest",
          "Budapest"
        ],
        [
          "Copenhagen",
          "Copenhagen"
        ],
        [
          "Ljubljana",
          "Ljubljana"
        ],
        [
          "Madrid",
          "Madrid"
        ],
        [
          "Paris",
          "Paris"
        ],
        [
          "Prague",
          "Prague"
        ],
        [
          "Rome",
          "Rome"
        ],
        [
          "Sarajevo",
          "Sarajevo"
        ],
        [
          "Skopje",
          "Skopje"
        ],
        [
          "Stockholm",
          "Stockholm"
        ],
        [
          "Vienna",
          "Vienna"
        ],
        [
          "Warsaw",
          "Warsaw"
        ],
        [
          "West Central Africa",
          "West Central Africa"
        ],
        [
          "Zagreb",
          "Zagreb"
        ],
        [
          "Athens",
          "Athens"
        ],
        [
          "Bucharest",
          "Bucharest"
        ],
        [
          "Cairo",
          "Cairo"
        ],
        [
          "Harare",
          "Harare"
        ],
        [
          "Helsinki",
          "Helsinki"
        ],
        [
          "Jerusalem",
          "Jerusalem"
        ],
        [
          "Kaliningrad",
          "Kaliningrad"
        ],
        [
          "Kyiv",
          "Kyiv"
        ],
        [
          "Pretoria",
          "Pretoria"
        ],
        [
          "Riga",
          "Riga"
        ],
        [
          "Sofia",
          "Sofia"
        ],
        [
          "Tallinn",
          "Tallinn"
        ],
        [
          "Vilnius",
          "Vilnius"
        ],
        [
          "Baghdad",
          "Baghdad"
        ],
        [
          "Istanbul",
          "Istanbul"
        ],
        [
          "Kuwait",
          "Kuwait"
        ],
        [
          "Minsk",
          "Minsk"
        ],
        [
          "Moscow",
          "Moscow"
        ],
        [
          "Nairobi",
          "Nairobi"
        ],
        [
          "Riyadh",
          "Riyadh"
        ],
        [
          "St. Petersburg",
          "St. Petersburg"
        ],
        [
          "Tehran",
          "Tehran"
        ],
        [
          "Abu Dhabi",
          "Abu Dhabi"
        ],
        [
          "Baku",
          "Baku"
        ],
        [
          "Muscat",
          "Muscat"
        ],
        [
          "Samara",
          "Samara"
        ],
        [
          "Tbilisi",
          "Tbilisi"
        ],
        [
          "Volgograd",
          "Volgograd"
        ],
        [
          "Yerevan",
          "Yerevan"
        ],
        [
          "Kabul",
          "Kabul"
        ],
        [
          "Ekaterinburg",
          "Ekaterinburg"
        ],
        [
          "Islamabad",
          "Islamabad"
        ],
        [
          "Karachi",
          "Karachi"
        ],
        [
          "Tashkent",
          "Tashkent"
        ],
        [
          "Chennai",
          "Chennai"
        ],
        [
          "Kolkata",
          "Kolkata"
        ],
        [
          "Mumbai",
          "Mumbai"
        ],
        [
          "New Delhi",
          "New Delhi"
        ],
        [
          "Sri Jayawardenepura",
          "Sri Jayawardenepura"
        ],
        [
          "Kathmandu",
          "Kathmandu"
        ],
        [
          "Almaty",
          "Almaty"
        ],
        [
          "Astana",
          "Astana"
        ],
        [
          "Dhaka",
          "Dhaka"
        ],
        [
          "Urumqi",
          "Urumqi"
        ],
        [
          "Rangoon",
          "Rangoon"
        ],
        [
          "Bangkok",
          "Bangkok"
        ],
        [
          "Hanoi",
          "Hanoi"
        ],
        [
          "Jakarta",
          "Jakarta"
        ],
        [
          "Krasnoyarsk",
          "Krasnoyarsk"
        ],
        [
          "Novosibirsk",
          "Novosibirsk"
        ],
        [
          "Beijing",
          "Beijing"
        ],
        [
          "Chongqing",
          "Chongqing"
        ],
        [
          "Hong Kong",
          "Hong Kong"
        ],
        [
          "Irkutsk",
          "Irkutsk"
        ],
        [
          "Kuala Lumpur",
          "Kuala Lumpur"
        ],
        [
          "Perth",
          "Perth"
        ],
        [
          "Singapore",
          "Singapore"
        ],
        [
          "Taipei",
          "Taipei"
        ],
        [
          "Ulaanbaatar",
          "Ulaanbaatar"
        ],
        [
          "Osaka",
          "Osaka"
        ],
        [
          "Sapporo",
          "Sapporo"
        ],
        [
          "Seoul",
          "Seoul"
        ],
        [
          "Tokyo",
          "Tokyo"
        ],
        [
          "Yakutsk",
          "Yakutsk"
        ],
        [
          "Adelaide",
          "Adelaide"
        ],
        [
          "Darwin",
          "Darwin"
        ],
        [
          "Brisbane",
          "Brisbane"
        ],
        [
          "Canberra",
          "Canberra"
        ],
        [
          "Guam",
          "Guam"
        ],
        [
          "Hobart",
          "Hobart"
        ],
        [
          "Melbourne",
          "Melbourne"
        ],
        [
          "Port Moresby",
          "Port Moresby"
        ],
        [
          "Sydney",
          "Sydney"
        ],
        [
          "Vladivostok",
          "Vladivostok"
        ],
        [
          "Magadan",
          "Magadan"
        ],
        [
          "New Caledonia",
          "New Caledonia"
        ],
        [
          "Solomon Is.",
          "Solomon Is."
        ],
        [
          "Srednekolymsk",
          "Srednekolymsk"
        ],
        [
          "Auckland",
          "Auckland"
        ],
        [
          "Fiji",
          "Fiji"
        ],
        [
          "Kamchatka",
          "Kamchatka"
        ],
        [
          "Marshall Is.",
          "Marshall Is."
        ],
        [
          "Wellington",
          "Wellington"
        ],
        [
          "Chatham Is.",
          "Chatham Is."
        ],
        [
          "Nuku'alofa",
          "Nuku'alofa"
        ],
        [
          "Samoa",
          "Samoa"
        ],
        [
          "Tokelau Is.",
          "Tokelau Is."
        ]
      ]
    }
  ]
}
```

* * *

### Workfront (Secondary)

**Provider value:**

```json
"provider": "workfront_secondary"
```

View connection parameters JSON

```json
{
  "oauth": true,
  "personalization": true,
  "oauth_token_pair": {
    "label": "OAuth Token Pair",
    "optional": true,
    "type": "object",
    "hint": "Allows you to create authorization code grant connections. You can create a shell connection in cases where you don't have an access token and refresh token.",
    "properties": [
      {
        "label": "Access Token",
        "name": "access_token",
        "type": "string",
        "optional": false
      },
      {
        "label": "Refresh Token",
        "name": "refresh_token",
        "type": "string",
        "optional": false
      }
    ]
  },
  "input": [
    {
      "label": "Authentication type",
      "hint": "Select authentication type",
      "optional": false,
      "default": "api_key",
      "type": "string",
      "name": "authentication_type",
      "pick_list": [
        [
          "OAuth 2.0",
          "oauth2_auth_code_grant"
        ],
        [
          "API key",
          "api_key"
        ]
      ]
    },
    {
      "label": "API key",
      "optional": false,
      "hint": "Your Workfront API key",
      "type": "string",
      "name": "api_key"
    },
    {
      "label": "Client ID",
      "optional": false,
      "hint": "Go to 'Setup > System > OAuth2 Applications > Client ID' to create a client ID and secret.",
      "type": "string",
      "name": "client_id"
    },
    {
      "label": "Client secret",
      "optional": false,
      "hint": "Go to 'Setup > System > OAuth2 Applications > Client secret' to create a client ID and secret.",
      "type": "string",
      "name": "client_secret"
    },
    {
      "label": "Subdomain",
      "optional": false,
      "hint": "Enter your Workfront subdomain name as found in your Workfront URL.",
      "type": "string",
      "name": "subdomain"
    },
    {
      "label": "API version",
      "default": "14.0",
      "hint": "Enter the API version to use in your connection. The default version is 14.0",
      "optional": true,
      "type": "string",
      "name": "api_version"
    },
    {
      "label": "Account timezone",
      "optional": true,
      "hint": "Enter an account timezone for consistency with Workfront. All date and time fields are converted to this timezone.",
      "type": "string",
      "name": "timezone",
      "pick_list": [
        [
          "American Samoa",
          "American Samoa"
        ],
        [
          "International Date Line West",
          "International Date Line West"
        ],
        [
          "Midway Island",
          "Midway Island"
        ],
        [
          "Hawaii",
          "Hawaii"
        ],
        [
          "Alaska",
          "Alaska"
        ],
        [
          "Pacific Time (US & Canada)",
          "Pacific Time (US & Canada)"
        ],
        [
          "Tijuana",
          "Tijuana"
        ],
        [
          "Arizona",
          "Arizona"
        ],
        [
          "Chihuahua",
          "Chihuahua"
        ],
        [
          "Mazatlan",
          "Mazatlan"
        ],
        [
          "Mountain Time (US & Canada)",
          "Mountain Time (US & Canada)"
        ],
        [
          "Central America",
          "Central America"
        ],
        [
          "Central Time (US & Canada)",
          "Central Time (US & Canada)"
        ],
        [
          "Guadalajara",
          "Guadalajara"
        ],
        [
          "Mexico City",
          "Mexico City"
        ],
        [
          "Monterrey",
          "Monterrey"
        ],
        [
          "Saskatchewan",
          "Saskatchewan"
        ],
        [
          "Bogota",
          "Bogota"
        ],
        [
          "Eastern Time (US & Canada)",
          "Eastern Time (US & Canada)"
        ],
        [
          "Indiana (East)",
          "Indiana (East)"
        ],
        [
          "Lima",
          "Lima"
        ],
        [
          "Quito",
          "Quito"
        ],
        [
          "Atlantic Time (Canada)",
          "Atlantic Time (Canada)"
        ],
        [
          "Caracas",
          "Caracas"
        ],
        [
          "Georgetown",
          "Georgetown"
        ],
        [
          "La Paz",
          "La Paz"
        ],
        [
          "Santiago",
          "Santiago"
        ],
        [
          "Newfoundland",
          "Newfoundland"
        ],
        [
          "Brasilia",
          "Brasilia"
        ],
        [
          "Buenos Aires",
          "Buenos Aires"
        ],
        [
          "Greenland",
          "Greenland"
        ],
        [
          "Montevideo",
          "Montevideo"
        ],
        [
          "Mid-Atlantic",
          "Mid-Atlantic"
        ],
        [
          "Azores",
          "Azores"
        ],
        [
          "Cape Verde Is.",
          "Cape Verde Is."
        ],
        [
          "Casablanca",
          "Casablanca"
        ],
        [
          "Dublin",
          "Dublin"
        ],
        [
          "Edinburgh",
          "Edinburgh"
        ],
        [
          "Lisbon",
          "Lisbon"
        ],
        [
          "London",
          "London"
        ],
        [
          "Monrovia",
          "Monrovia"
        ],
        [
          "UTC",
          "UTC"
        ],
        [
          "Amsterdam",
          "Amsterdam"
        ],
        [
          "Belgrade",
          "Belgrade"
        ],
        [
          "Berlin",
          "Berlin"
        ],
        [
          "Bern",
          "Bern"
        ],
        [
          "Bratislava",
          "Bratislava"
        ],
        [
          "Brussels",
          "Brussels"
        ],
        [
          "Budapest",
          "Budapest"
        ],
        [
          "Copenhagen",
          "Copenhagen"
        ],
        [
          "Ljubljana",
          "Ljubljana"
        ],
        [
          "Madrid",
          "Madrid"
        ],
        [
          "Paris",
          "Paris"
        ],
        [
          "Prague",
          "Prague"
        ],
        [
          "Rome",
          "Rome"
        ],
        [
          "Sarajevo",
          "Sarajevo"
        ],
        [
          "Skopje",
          "Skopje"
        ],
        [
          "Stockholm",
          "Stockholm"
        ],
        [
          "Vienna",
          "Vienna"
        ],
        [
          "Warsaw",
          "Warsaw"
        ],
        [
          "West Central Africa",
          "West Central Africa"
        ],
        [
          "Zagreb",
          "Zagreb"
        ],
        [
          "Athens",
          "Athens"
        ],
        [
          "Bucharest",
          "Bucharest"
        ],
        [
          "Cairo",
          "Cairo"
        ],
        [
          "Harare",
          "Harare"
        ],
        [
          "Helsinki",
          "Helsinki"
        ],
        [
          "Jerusalem",
          "Jerusalem"
        ],
        [
          "Kaliningrad",
          "Kaliningrad"
        ],
        [
          "Kyiv",
          "Kyiv"
        ],
        [
          "Pretoria",
          "Pretoria"
        ],
        [
          "Riga",
          "Riga"
        ],
        [
          "Sofia",
          "Sofia"
        ],
        [
          "Tallinn",
          "Tallinn"
        ],
        [
          "Vilnius",
          "Vilnius"
        ],
        [
          "Baghdad",
          "Baghdad"
        ],
        [
          "Istanbul",
          "Istanbul"
        ],
        [
          "Kuwait",
          "Kuwait"
        ],
        [
          "Minsk",
          "Minsk"
        ],
        [
          "Moscow",
          "Moscow"
        ],
        [
          "Nairobi",
          "Nairobi"
        ],
        [
          "Riyadh",
          "Riyadh"
        ],
        [
          "St. Petersburg",
          "St. Petersburg"
        ],
        [
          "Tehran",
          "Tehran"
        ],
        [
          "Abu Dhabi",
          "Abu Dhabi"
        ],
        [
          "Baku",
          "Baku"
        ],
        [
          "Muscat",
          "Muscat"
        ],
        [
          "Samara",
          "Samara"
        ],
        [
          "Tbilisi",
          "Tbilisi"
        ],
        [
          "Volgograd",
          "Volgograd"
        ],
        [
          "Yerevan",
          "Yerevan"
        ],
        [
          "Kabul",
          "Kabul"
        ],
        [
          "Ekaterinburg",
          "Ekaterinburg"
        ],
        [
          "Islamabad",
          "Islamabad"
        ],
        [
          "Karachi",
          "Karachi"
        ],
        [
          "Tashkent",
          "Tashkent"
        ],
        [
          "Chennai",
          "Chennai"
        ],
        [
          "Kolkata",
          "Kolkata"
        ],
        [
          "Mumbai",
          "Mumbai"
        ],
        [
          "New Delhi",
          "New Delhi"
        ],
        [
          "Sri Jayawardenepura",
          "Sri Jayawardenepura"
        ],
        [
          "Kathmandu",
          "Kathmandu"
        ],
        [
          "Almaty",
          "Almaty"
        ],
        [
          "Astana",
          "Astana"
        ],
        [
          "Dhaka",
          "Dhaka"
        ],
        [
          "Urumqi",
          "Urumqi"
        ],
        [
          "Rangoon",
          "Rangoon"
        ],
        [
          "Bangkok",
          "Bangkok"
        ],
        [
          "Hanoi",
          "Hanoi"
        ],
        [
          "Jakarta",
          "Jakarta"
        ],
        [
          "Krasnoyarsk",
          "Krasnoyarsk"
        ],
        [
          "Novosibirsk",
          "Novosibirsk"
        ],
        [
          "Beijing",
          "Beijing"
        ],
        [
          "Chongqing",
          "Chongqing"
        ],
        [
          "Hong Kong",
          "Hong Kong"
        ],
        [
          "Irkutsk",
          "Irkutsk"
        ],
        [
          "Kuala Lumpur",
          "Kuala Lumpur"
        ],
        [
          "Perth",
          "Perth"
        ],
        [
          "Singapore",
          "Singapore"
        ],
        [
          "Taipei",
          "Taipei"
        ],
        [
          "Ulaanbaatar",
          "Ulaanbaatar"
        ],
        [
          "Osaka",
          "Osaka"
        ],
        [
          "Sapporo",
          "Sapporo"
        ],
        [
          "Seoul",
          "Seoul"
        ],
        [
          "Tokyo",
          "Tokyo"
        ],
        [
          "Yakutsk",
          "Yakutsk"
        ],
        [
          "Adelaide",
          "Adelaide"
        ],
        [
          "Darwin",
          "Darwin"
        ],
        [
          "Brisbane",
          "Brisbane"
        ],
        [
          "Canberra",
          "Canberra"
        ],
        [
          "Guam",
          "Guam"
        ],
        [
          "Hobart",
          "Hobart"
        ],
        [
          "Melbourne",
          "Melbourne"
        ],
        [
          "Port Moresby",
          "Port Moresby"
        ],
        [
          "Sydney",
          "Sydney"
        ],
        [
          "Vladivostok",
          "Vladivostok"
        ],
        [
          "Magadan",
          "Magadan"
        ],
        [
          "New Caledonia",
          "New Caledonia"
        ],
        [
          "Solomon Is.",
          "Solomon Is."
        ],
        [
          "Srednekolymsk",
          "Srednekolymsk"
        ],
        [
          "Auckland",
          "Auckland"
        ],
        [
          "Fiji",
          "Fiji"
        ],
        [
          "Kamchatka",
          "Kamchatka"
        ],
        [
          "Marshall Is.",
          "Marshall Is."
        ],
        [
          "Wellington",
          "Wellington"
        ],
        [
          "Chatham Is.",
          "Chatham Is."
        ],
        [
          "Nuku'alofa",
          "Nuku'alofa"
        ],
        [
          "Samoa",
          "Samoa"
        ],
        [
          "Tokelau Is.",
          "Tokelau Is."
        ]
      ]
    }
  ]
}
```

* * *

### Wrike

**Provider value:**

```json
"provider": "wrike"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced settings",
                  "properties":
                  [
                      {
                          "name": "api_scope",
                          "type": "string",
                          "optional": true,
                          "label": "Api scope",
                          "hint": "               Select <a href=\"https://developers.wrike.com/documentation/api/overview\" target=\"_blank\">permissions</a>\n               to request for this connection. Defaults to <b>Default</b> if left blank.\n               <br/>Minimum permissions required is <b>Default</b>, which are requested in addition to selected permissions.\n"
                      }
                  ]
              }
          ]
      }
```

* * *

### Wrike (Secondary)

**Provider value:**

```json
"provider": "wrike_secondary"
```

View connection parameters JSON

```json
      {
          "oauth": true,
          "personalization": true,
          "input":
          [
              {
                  "name": "advanced_settings",
                  "type": "object",
                  "optional": true,
                  "label": "Advanced settings",
                  "properties":
                  [
                      {
                          "name": "api_scope",
                          "type": "string",
                          "optional": true,
                          "label": "Api scope",
                          "hint": "               Select <a href=\"https://developers.wrike.com/documentation/api/overview\" target=\"_blank\">permissions</a>\n               to request for this connection. Defaults to <b>Default</b> if left blank.\n               <br/>Minimum permissions required is <b>Default</b>, which are requested in addition to selected permissions.\n"
                      }
                  ]
              }
          ]
      }
```

* * *

### Wufoo

**Provider value:**

```json
"provider": "wufoo"
```

View connection parameters JSON

```json
      {
          "oauth": false,
          "personalization": false,
          "input":
          [
              {
                  "name": "api_key",
                  "type": "string",
                  "label": "API key",
                  "hint": "<a href=\"http://www.wufoo.com/docs/api/v3/#key\" target=\"_blank\">How do I find the Wufoo API key?</a>"
              },
              {
                  "name": "subdomain",
                  "type": "string",
                  "label": "Sub-domain",
                  "hint": "Enter only the subdomain (located before .wufoo.com)"
              }
          ]
      }
```

* * *

### Xactly

**Provider value:**

```json
"provider": "xactly"
```

View connection parameters JSON

```json
      {
         "oauth":false,
         "personalization":false,
         "input":[
            {
               "name":"subdomain",
               "type":"string",
               "optional":false,
               "label":"Sub-domain"
            },
            {
               "name":"client_id",
               "type":"string",
               "optional":false,
               "label":"Client ID"
            },
            {
               "name":"consumer",
               "type":"string",
               "optional":false,
               "label":"Consumer"
            },
            {
               "name":"username",
               "type":"string",
               "optional":false,
               "label":"Username"
            },
            {
               "name":"password",
               "type":"string",
               "optional":false,
               "label":"Password"
            }
         ]
      }
```

* * *

### Xero

**Provider value:**

```json
"provider": "xero"
```

View connection parameters JSON

```json
      {
         "oauth":true,
         "personalization":true,
         "input":[
            {
               "name":"payroll",
               "type":"boolean",
               "optional":true,
               "label":"Payroll",
               "hint":"Select 'Yes' if Xero account is enabled for payroll, note that payroll connectivity is only available in AU and US editions",
               "default":"false"
            }
         ]
      }
```

* * *

### Xero Practice Manager

**Provider value:**

```json
"provider": "xero_practice_manager"
```

* * *

### XML tools by Workato

**Provider value:**

```json
"provider": "xml_tools"
```

* * *

### YAML parser by Workato

**Provider value:**

```json
"provider": "yaml_parser"
```

* * *

### Zendesk

**Provider value:**

```json
"provider": "zendesk"
```

View connection parameters JSON

```json
      {
         "oauth":true,
         "personalization":true,
         "input":[
            {
               "name":"subdomain",
               "type":"string",
               "label":"Subdomain",
               "hint":"If your Zendesk URL is https://acme.zendesk.com then your subdomain is <b>acme</b>"
            },
            {
               "name":"authentication_type",
               "type":"string",
               "label":"Authentication type",
               "pick_list":[
                  [
                     "Basic",
                     "basic"
                  ],
                  [
                     "OAuth 2.0",
                     "oauth"
                  ]
               ],
               "default":"oauth"
            },
            {
               "name":"username",
               "type":"string",
               "label":"Username",
               "hint":"When authenticating with tokens, add <b>/token</b> to the end of your username."
            },
            {
               "name":"password",
               "type":"string",
               "label":"Password",
               "hint":"                   Enter api token if you are using api token authentication. Click <a href='https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-' target=\"_blank\">here</a> to generate api token.\n"
            }
         ]
      }
```

* * *

### Zendesk (Secondary)

**Provider value:**

```json
"provider": "zendesk_secondary"
```

View connection parameters JSON

```json
      {
         "oauth":true,
         "personalization":true,
         "input":[
            {
               "name":"subdomain",
               "type":"string",
               "label":"Subdomain",
               "hint":"If your Zendesk URL is https://acme.zendesk.com then your subdomain is <b>acme</b>"
            },
            {
               "name":"authentication_type",
               "type":"string",
               "label":"Authentication type",
               "pick_list":[
                  [
                     "Basic",
                     "basic"
                  ],
                  [
                     "OAuth 2.0",
                     "oauth"
                  ]
               ],
               "default":"oauth"
            },
            {
               "name":"username",
               "type":"string",
               "label":"Username",
               "hint":"When authenticating with tokens, add <b>/token</b> to the end of your username."
            },
            {
               "name":"password",
               "type":"string",
               "label":"Password",
               "hint":"                   Enter api token if you are using api token authentication. Click <a href='https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-' target=\"_blank\">here</a> to generate api token.\n"
            }
         ]
      }
```

* * *

### Zendesk Sunshine

**Provider value:**

```json
"provider": "zendesk_sunshine"
```

* * *

### Zenefits

**Provider value:**

```json
"provider": "zenefits"
```

View connection parameters JSON

```json
      {
         "oauth":true,
         "personalization":true,
         "input":[

         ]
      }
```

* * *

### Zoho CRM

**Provider value:**

```json
"provider": "zohocrm"
```

View connection parameters JSON

```json
      {
         "oauth":true,
         "personalization":true,
         "input":[
            {
               "name":"timezone",
               "type":"string",
               "optional":true,
               "label":"Account timezone",
               "hint":"Needed for consistency with Zoho - pick same as your Zoho profile",
               "pick_list":[
                  [
                     "American Samoa (-11:00)",
                     "American Samoa"
                  ],
                  [
                     "International Date Line West (-11:00)",
                     "International Date Line West"
                  ],
                  [
                     "Midway Island (-11:00)",
                     "Midway Island"
                  ],
                  [
                     "Hawaii (-10:00)",
                     "Hawaii"
                  ],
                  [
                     "Alaska (-9:00)",
                     "Alaska"
                  ],
                  [
                     "Pacific Time (US & Canada) (-8:00)",
                     "Pacific Time (US & Canada)"
                  ],
                  [
                     "Tijuana (-8:00)",
                     "Tijuana"
                  ],
                  [
                     "Arizona (-7:00)",
                     "Arizona"
                  ],
                  [
                     "Chihuahua (-7:00)",
                     "Chihuahua"
                  ],
                  [
                     "Mazatlan (-7:00)",
                     "Mazatlan"
                  ],
                  [
                     "Mountain Time (US & Canada) (-7:00)",
                     "Mountain Time (US & Canada)"
                  ],
                  [
                     "Central America (-6:00)",
                     "Central America"
                  ],
                  [
                     "Central Time (US & Canada) (-6:00)",
                     "Central Time (US & Canada)"
                  ],
                  [
                     "Guadalajara (-6:00)",
                     "Guadalajara"
                  ],
                  [
                     "Mexico City (-6:00)",
                     "Mexico City"
                  ],
                  [
                     "Monterrey (-6:00)",
                     "Monterrey"
                  ],
                  [
                     "Saskatchewan (-6:00)",
                     "Saskatchewan"
                  ],
                  [
                     "Bogota (-5:00)",
                     "Bogota"
                  ],
                  [
                     "Eastern Time (US & Canada) (-5:00)",
                     "Eastern Time (US & Canada)"
                  ],
                  [
                     "Indiana (East) (-5:00)",
                     "Indiana (East)"
                  ],
                  [
                     "Lima (-5:00)",
                     "Lima"
                  ],
                  [
                     "Quito (-5:00)",
                     "Quito"
                  ],
                  [
                     "Atlantic Time (Canada) (-4:00)",
                     "Atlantic Time (Canada)"
                  ],
                  [
                     "Caracas (-4:00)",
                     "Caracas"
                  ],
                  [
                     "Georgetown (-4:00)",
                     "Georgetown"
                  ],
                  [
                     "La Paz (-4:00)",
                     "La Paz"
                  ],
                  [
                     "Santiago (-4:00)",
                     "Santiago"
                  ],
                  [
                     "Newfoundland (-4:30)",
                     "Newfoundland"
                  ],
                  [
                     "Brasilia (-3:00)",
                     "Brasilia"
                  ],
                  [
                     "Buenos Aires (-3:00)",
                     "Buenos Aires"
                  ],
                  [
                     "Greenland (-3:00)",
                     "Greenland"
                  ],
                  [
                     "Montevideo (-3:00)",
                     "Montevideo"
                  ],
                  [
                     "Mid-Atlantic (-2:00)",
                     "Mid-Atlantic"
                  ],
                  [
                     "Azores (-1:00)",
                     "Azores"
                  ],
                  [
                     "Cape Verde Is. (-1:00)",
                     "Cape Verde Is."
                  ],
                  [
                     "Casablanca (+0:00)",
                     "Casablanca"
                  ],
                  [
                     "Dublin (+0:00)",
                     "Dublin"
                  ],
                  [
                     "Edinburgh (+0:00)",
                     "Edinburgh"
                  ],
                  [
                     "Lisbon (+0:00)",
                     "Lisbon"
                  ],
                  [
                     "London (+0:00)",
                     "London"
                  ],
                  [
                     "Monrovia (+0:00)",
                     "Monrovia"
                  ],
                  [
                     "UTC (+0:00)",
                     "UTC"
                  ],
                  [
                     "Amsterdam (+1:00)",
                     "Amsterdam"
                  ],
                  [
                     "Belgrade (+1:00)",
                     "Belgrade"
                  ],
                  [
                     "Berlin (+1:00)",
                     "Berlin"
                  ],
                  [
                     "Bern (+1:00)",
                     "Bern"
                  ],
                  [
                     "Bratislava (+1:00)",
                     "Bratislava"
                  ],
                  [
                     "Brussels (+1:00)",
                     "Brussels"
                  ],
                  [
                     "Budapest (+1:00)",
                     "Budapest"
                  ],
                  [
                     "Copenhagen (+1:00)",
                     "Copenhagen"
                  ],
                  [
                     "Ljubljana (+1:00)",
                     "Ljubljana"
                  ],
                  [
                     "Madrid (+1:00)",
                     "Madrid"
                  ],
                  [
                     "Paris (+1:00)",
                     "Paris"
                  ],
                  [
                     "Prague (+1:00)",
                     "Prague"
                  ],
                  [
                     "Rome (+1:00)",
                     "Rome"
                  ],
                  [
                     "Sarajevo (+1:00)",
                     "Sarajevo"
                  ],
                  [
                     "Skopje (+1:00)",
                     "Skopje"
                  ],
                  [
                     "Stockholm (+1:00)",
                     "Stockholm"
                  ],
                  [
                     "Vienna (+1:00)",
                     "Vienna"
                  ],
                  [
                     "Warsaw (+1:00)",
                     "Warsaw"
                  ],
                  [
                     "West Central Africa (+1:00)",
                     "West Central Africa"
                  ],
                  [
                     "Zagreb (+1:00)",
                     "Zagreb"
                  ],
                  [
                     "Athens (+2:00)",
                     "Athens"
                  ],
                  [
                     "Bucharest (+2:00)",
                     "Bucharest"
                  ],
                  [
                     "Cairo (+2:00)",
                     "Cairo"
                  ],
                  [
                     "Harare (+2:00)",
                     "Harare"
                  ],
                  [
                     "Helsinki (+2:00)",
                     "Helsinki"
                  ],
                  [
                     "Jerusalem (+2:00)",
                     "Jerusalem"
                  ],
                  [
                     "Kaliningrad (+2:00)",
                     "Kaliningrad"
                  ],
                  [
                     "Kyiv (+2:00)",
                     "Kyiv"
                  ],
                  [
                     "Pretoria (+2:00)",
                     "Pretoria"
                  ],
                  [
                     "Riga (+2:00)",
                     "Riga"
                  ],
                  [
                     "Sofia (+2:00)",
                     "Sofia"
                  ],
                  [
                     "Tallinn (+2:00)",
                     "Tallinn"
                  ],
                  [
                     "Vilnius (+2:00)",
                     "Vilnius"
                  ],
                  [
                     "Baghdad (+3:00)",
                     "Baghdad"
                  ],
                  [
                     "Istanbul (+3:00)",
                     "Istanbul"
                  ],
                  [
                     "Kuwait (+3:00)",
                     "Kuwait"
                  ],
                  [
                     "Minsk (+3:00)",
                     "Minsk"
                  ],
                  [
                     "Moscow (+3:00)",
                     "Moscow"
                  ],
                  [
                     "Nairobi (+3:00)",
                     "Nairobi"
                  ],
                  [
                     "Riyadh (+3:00)",
                     "Riyadh"
                  ],
                  [
                     "St. Petersburg (+3:00)",
                     "St. Petersburg"
                  ],
                  [
                     "Tehran (+3:30)",
                     "Tehran"
                  ],
                  [
                     "Abu Dhabi (+4:00)",
                     "Abu Dhabi"
                  ],
                  [
                     "Baku (+4:00)",
                     "Baku"
                  ],
                  [
                     "Muscat (+4:00)",
                     "Muscat"
                  ],
                  [
                     "Samara (+4:00)",
                     "Samara"
                  ],
                  [
                     "Tbilisi (+4:00)",
                     "Tbilisi"
                  ],
                  [
                     "Volgograd (+4:00)",
                     "Volgograd"
                  ],
                  [
                     "Yerevan (+4:00)",
                     "Yerevan"
                  ],
                  [
                     "Kabul (+4:30)",
                     "Kabul"
                  ],
                  [
                     "Ekaterinburg (+5:00)",
                     "Ekaterinburg"
                  ],
                  [
                     "Islamabad (+5:00)",
                     "Islamabad"
                  ],
                  [
                     "Karachi (+5:00)",
                     "Karachi"
                  ],
                  [
                     "Tashkent (+5:00)",
                     "Tashkent"
                  ],
                  [
                     "Chennai (+5:30)",
                     "Chennai"
                  ],
                  [
                     "Kolkata (+5:30)",
                     "Kolkata"
                  ],
                  [
                     "Mumbai (+5:30)",
                     "Mumbai"
                  ],
                  [
                     "New Delhi (+5:30)",
                     "New Delhi"
                  ],
                  [
                     "Sri Jayawardenepura (+5:30)",
                     "Sri Jayawardenepura"
                  ],
                  [
                     "Kathmandu (+5:45)",
                     "Kathmandu"
                  ],
                  [
                     "Almaty (+6:00)",
                     "Almaty"
                  ],
                  [
                     "Astana (+6:00)",
                     "Astana"
                  ],
                  [
                     "Dhaka (+6:00)",
                     "Dhaka"
                  ],
                  [
                     "Urumqi (+6:00)",
                     "Urumqi"
                  ],
                  [
                     "Rangoon (+6:30)",
                     "Rangoon"
                  ],
                  [
                     "Bangkok (+7:00)",
                     "Bangkok"
                  ],
                  [
                     "Hanoi (+7:00)",
                     "Hanoi"
                  ],
                  [
                     "Jakarta (+7:00)",
                     "Jakarta"
                  ],
                  [
                     "Krasnoyarsk (+7:00)",
                     "Krasnoyarsk"
                  ],
                  [
                     "Novosibirsk (+7:00)",
                     "Novosibirsk"
                  ],
                  [
                     "Beijing (+8:00)",
                     "Beijing"
                  ],
                  [
                     "Chongqing (+8:00)",
                     "Chongqing"
                  ],
                  [
                     "Hong Kong (+8:00)",
                     "Hong Kong"
                  ],
                  [
                     "Irkutsk (+8:00)",
                     "Irkutsk"
                  ],
                  [
                     "Kuala Lumpur (+8:00)",
                     "Kuala Lumpur"
                  ],
                  [
                     "Perth (+8:00)",
                     "Perth"
                  ],
                  [
                     "Singapore (+8:00)",
                     "Singapore"
                  ],
                  [
                     "Taipei (+8:00)",
                     "Taipei"
                  ],
                  [
                     "Ulaanbaatar (+8:00)",
                     "Ulaanbaatar"
                  ],
                  [
                     "Osaka (+9:00)",
                     "Osaka"
                  ],
                  [
                     "Sapporo (+9:00)",
                     "Sapporo"
                  ],
                  [
                     "Seoul (+9:00)",
                     "Seoul"
                  ],
                  [
                     "Tokyo (+9:00)",
                     "Tokyo"
                  ],
                  [
                     "Yakutsk (+9:00)",
                     "Yakutsk"
                  ],
                  [
                     "Adelaide (+9:30)",
                     "Adelaide"
                  ],
                  [
                     "Darwin (+9:30)",
                     "Darwin"
                  ],
                  [
                     "Brisbane (+10:00)",
                     "Brisbane"
                  ],
                  [
                     "Canberra (+10:00)",
                     "Canberra"
                  ],
                  [
                     "Guam (+10:00)",
                     "Guam"
                  ],
                  [
                     "Hobart (+10:00)",
                     "Hobart"
                  ],
                  [
                     "Melbourne (+10:00)",
                     "Melbourne"
                  ],
                  [
                     "Port Moresby (+10:00)",
                     "Port Moresby"
                  ],
                  [
                     "Sydney (+10:00)",
                     "Sydney"
                  ],
                  [
                     "Vladivostok (+10:00)",
                     "Vladivostok"
                  ],
                  [
                     "Magadan (+11:00)",
                     "Magadan"
                  ],
                  [
                     "New Caledonia (+11:00)",
                     "New Caledonia"
                  ],
                  [
                     "Solomon Is. (+11:00)",
                     "Solomon Is."
                  ],
                  [
                     "Srednekolymsk (+11:00)",
                     "Srednekolymsk"
                  ],
                  [
                     "Auckland (+12:00)",
                     "Auckland"
                  ],
                  [
                     "Fiji (+12:00)",
                     "Fiji"
                  ],
                  [
                     "Kamchatka (+12:00)",
                     "Kamchatka"
                  ],
                  [
                     "Marshall Is. (+12:00)",
                     "Marshall Is."
                  ],
                  [
                     "Wellington (+12:00)",
                     "Wellington"
                  ],
                  [
                     "Chatham Is. (+12:45)",
                     "Chatham Is."
                  ],
                  [
                     "Nuku'alofa (+13:00)",
                     "Nuku'alofa"
                  ],
                  [
                     "Samoa (+13:00)",
                     "Samoa"
                  ],
                  [
                     "Tokelau Is. (+13:00)",
                     "Tokelau Is."
                  ]
               ]
            },
            {
               "name":"data_center",
               "type":"string",
               "optional":true,
               "label":"Data center",
               "hint":"You can find this at the end of your Zoho URL 'https://accounts.zoho.[Data center]'. Default value: 'Others(com)'",
               "pick_list":[
                  [
                     "China(cn)",
                     "com.cn"
                  ],
                  [
                     "Europe(eu)",
                     "eu"
                  ],
                  [
                     "India(in)",
                     "in"
                  ],
                  [
                     "Others(com)",
                     "com"
                  ]
               ],
               "default":"com"
            }
         ]
      }
```

* * *

### Zoho Invoice

**Provider value:**

```json
"provider": "zoho_invoice"
```

View connection parameters JSON

```json
      {
         "oauth":false,
         "personalization":false,
         "input":[
            {
               "name":"auth_token",
               "type":"string",
               "label":"Authentication token",
               "hint":"Create your Zoho invoice token <a target='_blank' rel='noopener' href=\"https://accounts.zoho.com/apiauthtoken/create?SCOPE=ZohoInvoice/invoiceapi\">here</a>"
            },
            {
               "name":"timezone",
               "type":"string",
               "optional":true,
               "label":"Account timezone",
               "hint":"Needed for consistency with Zoho - pick same as your Zoho profile",
               "pick_list":[
                  [
                     "American Samoa (-11:00)",
                     "American Samoa"
                  ],
                  [
                     "International Date Line West (-11:00)",
                     "International Date Line West"
                  ],
                  [
                     "Midway Island (-11:00)",
                     "Midway Island"
                  ],
                  [
                     "Hawaii (-10:00)",
                     "Hawaii"
                  ],
                  [
                     "Alaska (-9:00)",
                     "Alaska"
                  ],
                  [
                     "Pacific Time (US & Canada) (-8:00)",
                     "Pacific Time (US & Canada)"
                  ],
                  [
                     "Tijuana (-8:00)",
                     "Tijuana"
                  ],
                  [
                     "Arizona (-7:00)",
                     "Arizona"
                  ],
                  [
                     "Chihuahua (-7:00)",
                     "Chihuahua"
                  ],
                  [
                     "Mazatlan (-7:00)",
                     "Mazatlan"
                  ],
                  [
                     "Mountain Time (US & Canada) (-7:00)",
                     "Mountain Time (US & Canada)"
                  ],
                  [
                     "Central America (-6:00)",
                     "Central America"
                  ],
                  [
                     "Central Time (US & Canada) (-6:00)",
                     "Central Time (US & Canada)"
                  ],
                  [
                     "Guadalajara (-6:00)",
                     "Guadalajara"
                  ],
                  [
                     "Mexico City (-6:00)",
                     "Mexico City"
                  ],
                  [
                     "Monterrey (-6:00)",
                     "Monterrey"
                  ],
                  [
                     "Saskatchewan (-6:00)",
                     "Saskatchewan"
                  ],
                  [
                     "Bogota (-5:00)",
                     "Bogota"
                  ],
                  [
                     "Eastern Time (US & Canada) (-5:00)",
                     "Eastern Time (US & Canada)"
                  ],
                  [
                     "Indiana (East) (-5:00)",
                     "Indiana (East)"
                  ],
                  [
                     "Lima (-5:00)",
                     "Lima"
                  ],
                  [
                     "Quito (-5:00)",
                     "Quito"
                  ],
                  [
                     "Atlantic Time (Canada) (-4:00)",
                     "Atlantic Time (Canada)"
                  ],
                  [
                     "Caracas (-4:00)",
                     "Caracas"
                  ],
                  [
                     "Georgetown (-4:00)",
                     "Georgetown"
                  ],
                  [
                     "La Paz (-4:00)",
                     "La Paz"
                  ],
                  [
                     "Santiago (-4:00)",
                     "Santiago"
                  ],
                  [
                     "Newfoundland (-4:30)",
                     "Newfoundland"
                  ],
                  [
                     "Brasilia (-3:00)",
                     "Brasilia"
                  ],
                  [
                     "Buenos Aires (-3:00)",
                     "Buenos Aires"
                  ],
                  [
                     "Greenland (-3:00)",
                     "Greenland"
                  ],
                  [
                     "Montevideo (-3:00)",
                     "Montevideo"
                  ],
                  [
                     "Mid-Atlantic (-2:00)",
                     "Mid-Atlantic"
                  ],
                  [
                     "Azores (-1:00)",
                     "Azores"
                  ],
                  [
                     "Cape Verde Is. (-1:00)",
                     "Cape Verde Is."
                  ],
                  [
                     "Casablanca (+0:00)",
                     "Casablanca"
                  ],
                  [
                     "Dublin (+0:00)",
                     "Dublin"
                  ],
                  [
                     "Edinburgh (+0:00)",
                     "Edinburgh"
                  ],
                  [
                     "Lisbon (+0:00)",
                     "Lisbon"
                  ],
                  [
                     "London (+0:00)",
                     "London"
                  ],
                  [
                     "Monrovia (+0:00)",
                     "Monrovia"
                  ],
                  [
                     "UTC (+0:00)",
                     "UTC"
                  ],
                  [
                     "Amsterdam (+1:00)",
                     "Amsterdam"
                  ],
                  [
                     "Belgrade (+1:00)",
                     "Belgrade"
                  ],
                  [
                     "Berlin (+1:00)",
                     "Berlin"
                  ],
                  [
                     "Bern (+1:00)",
                     "Bern"
                  ],
                  [
                     "Bratislava (+1:00)",
                     "Bratislava"
                  ],
                  [
                     "Brussels (+1:00)",
                     "Brussels"
                  ],
                  [
                     "Budapest (+1:00)",
                     "Budapest"
                  ],
                  [
                     "Copenhagen (+1:00)",
                     "Copenhagen"
                  ],
                  [
                     "Ljubljana (+1:00)",
                     "Ljubljana"
                  ],
                  [
                     "Madrid (+1:00)",
                     "Madrid"
                  ],
                  [
                     "Paris (+1:00)",
                     "Paris"
                  ],
                  [
                     "Prague (+1:00)",
                     "Prague"
                  ],
                  [
                     "Rome (+1:00)",
                     "Rome"
                  ],
                  [
                     "Sarajevo (+1:00)",
                     "Sarajevo"
                  ],
                  [
                     "Skopje (+1:00)",
                     "Skopje"
                  ],
                  [
                     "Stockholm (+1:00)",
                     "Stockholm"
                  ],
                  [
                     "Vienna (+1:00)",
                     "Vienna"
                  ],
                  [
                     "Warsaw (+1:00)",
                     "Warsaw"
                  ],
                  [
                     "West Central Africa (+1:00)",
                     "West Central Africa"
                  ],
                  [
                     "Zagreb (+1:00)",
                     "Zagreb"
                  ],
                  [
                     "Athens (+2:00)",
                     "Athens"
                  ],
                  [
                     "Bucharest (+2:00)",
                     "Bucharest"
                  ],
                  [
                     "Cairo (+2:00)",
                     "Cairo"
                  ],
                  [
                     "Harare (+2:00)",
                     "Harare"
                  ],
                  [
                     "Helsinki (+2:00)",
                     "Helsinki"
                  ],
                  [
                     "Jerusalem (+2:00)",
                     "Jerusalem"
                  ],
                  [
                     "Kaliningrad (+2:00)",
                     "Kaliningrad"
                  ],
                  [
                     "Kyiv (+2:00)",
                     "Kyiv"
                  ],
                  [
                     "Pretoria (+2:00)",
                     "Pretoria"
                  ],
                  [
                     "Riga (+2:00)",
                     "Riga"
                  ],
                  [
                     "Sofia (+2:00)",
                     "Sofia"
                  ],
                  [
                     "Tallinn (+2:00)",
                     "Tallinn"
                  ],
                  [
                     "Vilnius (+2:00)",
                     "Vilnius"
                  ],
                  [
                     "Baghdad (+3:00)",
                     "Baghdad"
                  ],
                  [
                     "Istanbul (+3:00)",
                     "Istanbul"
                  ],
                  [
                     "Kuwait (+3:00)",
                     "Kuwait"
                  ],
                  [
                     "Minsk (+3:00)",
                     "Minsk"
                  ],
                  [
                     "Moscow (+3:00)",
                     "Moscow"
                  ],
                  [
                     "Nairobi (+3:00)",
                     "Nairobi"
                  ],
                  [
                     "Riyadh (+3:00)",
                     "Riyadh"
                  ],
                  [
                     "St. Petersburg (+3:00)",
                     "St. Petersburg"
                  ],
                  [
                     "Tehran (+3:30)",
                     "Tehran"
                  ],
                  [
                     "Abu Dhabi (+4:00)",
                     "Abu Dhabi"
                  ],
                  [
                     "Baku (+4:00)",
                     "Baku"
                  ],
                  [
                     "Muscat (+4:00)",
                     "Muscat"
                  ],
                  [
                     "Samara (+4:00)",
                     "Samara"
                  ],
                  [
                     "Tbilisi (+4:00)",
                     "Tbilisi"
                  ],
                  [
                     "Volgograd (+4:00)",
                     "Volgograd"
                  ],
                  [
                     "Yerevan (+4:00)",
                     "Yerevan"
                  ],
                  [
                     "Kabul (+4:30)",
                     "Kabul"
                  ],
                  [
                     "Ekaterinburg (+5:00)",
                     "Ekaterinburg"
                  ],
                  [
                     "Islamabad (+5:00)",
                     "Islamabad"
                  ],
                  [
                     "Karachi (+5:00)",
                     "Karachi"
                  ],
                  [
                     "Tashkent (+5:00)",
                     "Tashkent"
                  ],
                  [
                     "Chennai (+5:30)",
                     "Chennai"
                  ],
                  [
                     "Kolkata (+5:30)",
                     "Kolkata"
                  ],
                  [
                     "Mumbai (+5:30)",
                     "Mumbai"
                  ],
                  [
                     "New Delhi (+5:30)",
                     "New Delhi"
                  ],
                  [
                     "Sri Jayawardenepura (+5:30)",
                     "Sri Jayawardenepura"
                  ],
                  [
                     "Kathmandu (+5:45)",
                     "Kathmandu"
                  ],
                  [
                     "Almaty (+6:00)",
                     "Almaty"
                  ],
                  [
                     "Astana (+6:00)",
                     "Astana"
                  ],
                  [
                     "Dhaka (+6:00)",
                     "Dhaka"
                  ],
                  [
                     "Urumqi (+6:00)",
                     "Urumqi"
                  ],
                  [
                     "Rangoon (+6:30)",
                     "Rangoon"
                  ],
                  [
                     "Bangkok (+7:00)",
                     "Bangkok"
                  ],
                  [
                     "Hanoi (+7:00)",
                     "Hanoi"
                  ],
                  [
                     "Jakarta (+7:00)",
                     "Jakarta"
                  ],
                  [
                     "Krasnoyarsk (+7:00)",
                     "Krasnoyarsk"
                  ],
                  [
                     "Novosibirsk (+7:00)",
                     "Novosibirsk"
                  ],
                  [
                     "Beijing (+8:00)",
                     "Beijing"
                  ],
                  [
                     "Chongqing (+8:00)",
                     "Chongqing"
                  ],
                  [
                     "Hong Kong (+8:00)",
                     "Hong Kong"
                  ],
                  [
                     "Irkutsk (+8:00)",
                     "Irkutsk"
                  ],
                  [
                     "Kuala Lumpur (+8:00)",
                     "Kuala Lumpur"
                  ],
                  [
                     "Perth (+8:00)",
                     "Perth"
                  ],
                  [
                     "Singapore (+8:00)",
                     "Singapore"
                  ],
                  [
                     "Taipei (+8:00)",
                     "Taipei"
                  ],
                  [
                     "Ulaanbaatar (+8:00)",
                     "Ulaanbaatar"
                  ],
                  [
                     "Osaka (+9:00)",
                     "Osaka"
                  ],
                  [
                     "Sapporo (+9:00)",
                     "Sapporo"
                  ],
                  [
                     "Seoul (+9:00)",
                     "Seoul"
                  ],
                  [
                     "Tokyo (+9:00)",
                     "Tokyo"
                  ],
                  [
                     "Yakutsk (+9:00)",
                     "Yakutsk"
                  ],
                  [
                     "Adelaide (+9:30)",
                     "Adelaide"
                  ],
                  [
                     "Darwin (+9:30)",
                     "Darwin"
                  ],
                  [
                     "Brisbane (+10:00)",
                     "Brisbane"
                  ],
                  [
                     "Canberra (+10:00)",
                     "Canberra"
                  ],
                  [
                     "Guam (+10:00)",
                     "Guam"
                  ],
                  [
                     "Hobart (+10:00)",
                     "Hobart"
                  ],
                  [
                     "Melbourne (+10:00)",
                     "Melbourne"
                  ],
                  [
                     "Port Moresby (+10:00)",
                     "Port Moresby"
                  ],
                  [
                     "Sydney (+10:00)",
                     "Sydney"
                  ],
                  [
                     "Vladivostok (+10:00)",
                     "Vladivostok"
                  ],
                  [
                     "Magadan (+11:00)",
                     "Magadan"
                  ],
                  [
                     "New Caledonia (+11:00)",
                     "New Caledonia"
                  ],
                  [
                     "Solomon Is. (+11:00)",
                     "Solomon Is."
                  ],
                  [
                     "Srednekolymsk (+11:00)",
                     "Srednekolymsk"
                  ],
                  [
                     "Auckland (+12:00)",
                     "Auckland"
                  ],
                  [
                     "Fiji (+12:00)",
                     "Fiji"
                  ],
                  [
                     "Kamchatka (+12:00)",
                     "Kamchatka"
                  ],
                  [
                     "Marshall Is. (+12:00)",
                     "Marshall Is."
                  ],
                  [
                     "Wellington (+12:00)",
                     "Wellington"
                  ],
                  [
                     "Chatham Is. (+12:45)",
                     "Chatham Is."
                  ],
                  [
                     "Nuku'alofa (+13:00)",
                     "Nuku'alofa"
                  ],
                  [
                     "Samoa (+13:00)",
                     "Samoa"
                  ],
                  [
                     "Tokelau Is. (+13:00)",
                     "Tokelau Is."
                  ]
               ]
            },
            {
               "name":"data_center",
               "type":"string",
               "optional":true,
               "label":"Data center",
               "hint":"You can find this at the end of your Zoho URL 'https://accounts.zoho.[Data center]'. Default value: 'Others(com)'",
               "pick_list":[
                  [
                     "China(cn)",
                     "cn"
                  ],
                  [
                     "Europe(eu)",
                     "eu"
                  ],
                  [
                     "Others(com)",
                     "com"
                  ]
               ],
               "default":"com"
            }
         ]
      }
```

* * *

### Zoom

**Provider value:**

```json
"provider": "zoom"
```

* * *

### ZoomInfo

**Provider value:**

```json
"provider": "zoom_info"
```

* * *

### Zuora

**Provider value:**

```json
"provider": "zuora"
```

View connection parameters JSON

```json
      {
         "oauth":false,
         "personalization":false,
         "input":[
            {
               "name":"client_id",
               "type":"string",
               "optional":false,
               "label":"Client ID",
               "hint":"Click <a href='https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User' target='_blank'>here</a> for client ID"
            },
            {
               "name":"client_secret",
               "type":"string",
               "optional":false,
               "label":"Client secret",
               "hint":"Click <a href='https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User' target='_blank'>here</a> for client secret"
            },
            {
               "name":"environment",
               "type":"string",
               "optional":false,
               "label":"Environment",
               "hint":"Click <a href='https://jp.zuora.com/api-reference/#section/Introduction/Endpoints' target='_blank'>here</a> for environment details",
               "pick_list":[
                  [
                     "US Production",
                     "rest"
                  ],
                  [
                     "US Sandbox",
                     "rest.apisandbox"
                  ],
                  [
                     "US Performance Test",
                     "rest.pt1"
                  ],
                  [
                     "EU Production",
                     "rest.eu"
                  ],
                  [
                     "EU Sandbox",
                     "rest.sandbox.eu"
                  ]
               ]
            },
            {
               "name":"version",
               "type":"string",
               "optional":false,
               "label":"Zuora SOAP API Version",
               "hint":"WSDL Service Version for example, 91.0, Find the <a href='https://knowledgecenter.zuora.com/DC_Developers/G_SOAP_API/Zuora_SOAP_API_Version_History' target='_blank'>latest version</a>."
            }
         ]
      }
```

* * *

### Zuora for Salesforce

**Provider value:**

```json
"provider": "zuora_forcecom"
```

View connection parameters JSON

```json
      {
         "oauth":true,
         "personalization":true,
         "input":[
            {
               "name":"sandbox",
               "type":"boolean",
               "optional":true,
               "label":"Sandbox",
               "hint":"Is this connecting to a sandbox account?",
               "default":"false"
            }
         ]
      }
```

---
