---
url: >-
  https://docs.workato.com/en/connectors/openapi/reference/default-connection-fields.md
description: >-
  Reference for the default connection fields used by the OpenAPI connector,
  including authentication method, document source, and OAuth 2.0 settings.
---

# OpenAPI default connection fields reference

When using the [OpenAPI connector to create custom connectors](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors), you control the fields end users see when setting up a connection.

This guide serves as a reference for the default connection fields in the [universal OpenAPI connector](/en/connectors/openapi/).

## Field reference documentation

Each connection field in the OpenAPI connector has its own section in this guide. In each section, you'll find the following info:

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>Description</strong></td><td>A description of the field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>UI name</strong></td><td>The name of the field as it displays in Workato, ex: <strong>Authentication method</strong></td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>The name of the field in the connector's source code, ex: <code>auth_method</code></td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Whether the field is required or not</td></tr></tbody></table>

## Required fields

While you can customize connection fields, the following fields must be present in [`connection.fields`](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors#add-modify-connection-fields) or [`adjust_connection`](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors#hard-code-connection-values) to successfully configure [a custom OpenAPI connector](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors):

- [Authentication method](#auth-method) (`auth_method`)- [Basic auth user](#basic-auth-user) (`basic_auth_user`) **\***- [Document content](#definition-content) (`definition_content`) **\***- [OpenAPI document source](#definition-mode) (`definition_mode`)- [Document URL](#definition-url) (`definition_url`) **\***- [Header authorization](#auth-headers) (`auth_headers`) **\***- [OAuth2 authorization URL](#authorization-url) (`authorization_url`) **\***- [OAuth2 token URL](#token-url) (`token_url`) **\***- [Client ID](#client-id) (`client_id`) **\***- [Client Secret](#client-secret) (`client_secret`) **\***- [Username](#username) (`username`) **\***- [Password](#username) (`username`) **\***- [Query param authorization](#query-params) (`query_params`) **\***- [Server URL](#base-url) (`base_url`)

> **INFO**
> 
> The `*` symbol indicates the marked field is dependent on another field. Refer to the marked field's documentation for more information.

## Allow long field hints

If set to `No`, object hints will be stripped to a single paragraph. The default is `No`.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Allow long field hints</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.allow_multi_paragraph_hint</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Authentication method

> **THIS IS A REQUIRED FIELD.**

The authentication method the connection uses. The value of this field determines what other values the user must provide for authentication:

- `none` (no other input required)
- `basic` (see [Basic auth user](#basic-auth-user) and [Basic auth password](#basic-auth-password))
- `header` (see [Header authorization](#header-authorization))
- `query` (see [Query param authorization](#query-param-auth))
- `oauth2_client_credentials` (see [OAuth2 token URL](#token-url), [How does the API require credentials to be sent to request a token?](#access-token-request-mode), [Client ID](#client-id), [Client Secret](#client-secret) and [Scopes](#scopes))
- `oauth2_authorization_code` (see [OAuth2 authorization URL](#authorization-url), [OAuth2 token URL](#token-url), [How does the API require credentials to be sent to request a token?](#access-token-request-mode), [Client ID](#client-id), [Client Secret](#client-secret) and [Scopes](#scopes))
- `oauth2_resource_owner_password` (see [OAuth2 token URL](#token-url), [Client ID](#client-id), [Client Secret](#client-secret), [Username](#username), [Password](#password) and [Scopes](#scopes))

Refer to the [OpenAPI authentication guide](/en/connectors/openapi/guides/authentication) for more info about supported authentication methods.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Authentication method</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>auth_method</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes</td></tr></tbody></table>

## Basic auth user

> **THIS IS A REQUIRED FIELD.**

The name of the application user/account.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Basic auth user</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>basic_auth_user</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, if <strong>Authentication method</strong> is set to <code>basic</code></td></tr></tbody></table>

## Basic auth password

The password of the user. An alternative to your password would be an API key or API token, retrieved from your account settings.

This should be kept secret.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Basic auth password</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>basic_auth_password</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Schema depth limit

Define the maximum depth for nested fields to be includes in the input and output schema descriptions.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Schema depth limit</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.max_schema_depth</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

> **Limit nested fields**
> 
> If your input or output schema contains too many nested fields, it may be difficult to use the connector.
> 
> For example, a `company` object has a property of `parentCompany` which is another `company` object. Further, the parent company may also have another `parentCompany`.
> 
> [Schema depth limit](#max-schema-depth) and [Schema recursion limit](#max-recursion-depth) allows you to prevent this nesting from continuing indefinitely.

## Schema recursion limit

Define the maximum depth recursive schema definitions to be included in input and output schema descriptions.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Schema recursion limit</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.max_recursion_depth</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

> **Limit nested fields**
> 
> If your input or output schema contains too many nested fields, it may be difficult to use the connector.
> 
> For example, a `company` object has a property of `parentCompany` which is another `company` object. Further, the parent company may also have another `parentCompany`.
> 
> [Schema depth limit](#max-schema-depth) and [Schema recursion limit](#max-recursion-depth) allows you to prevent this nesting from continuing indefinitely.

## Document content

> **THIS IS A REQUIRED FIELD.**

Content of the OpenAPI document. Format is either JSON or YAML. Supports OpenAPI v3.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Document content</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>definition_content</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>OpenAPI document source</strong> is set to <code>content</code></td></tr></tbody></table>

## Documentation links

Link to the application documentation, user guides, or company web site. This documentation link will be provided in the help text of your connector's triggers or actions.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Documentation link</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.documentation_href</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## OpenAPI document source

> **THIS IS A REQUIRED FIELD.**

Defines how to provide the OpenAPI document to the connector. The preferred approach is to load it from a URL. Otherwise, copy and paste the contents of the file.

The value of this field determines what other values the user must provide. Must be one of the following:

- `url` (see [Document URL](#definition-url))
- `content` (see [Document content](#definition-content))

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>OpenAPI document source</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>definition_mode</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes</td></tr></tbody></table>

## Document URL

> **THIS IS A REQUIRED FIELD.**

This URL must be publicly accessible at all times. Any future changes to the document itself appear automatically in the Workato recipe editor. The document can be in either JSON or YAML format. Supports OpenAPI v3.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Document URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>definition_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>OpenAPI document source</strong> is set to <code>url</code></td></tr></tbody></table>

## External documentation links

When defined, allows object field descriptions to link to external websites like API references or documentation.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#external-links) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>External documentation links</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.external_links</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Filter API endpoints

Defines rules for filtering endpoint.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Filter API endpoints</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.endpoint_filter_rules</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

### Sample

```ruby
{
  ...
  "advanced" => {
    "endpoint_filter_rules" => [
      {
        "type" => "include",
        "operation_id" => "createPet"
      },
      ...
    ]
  }
  ...
}
```

> **API endpoint filter rules**
> 
> You can use **include** or **exclude** filter rules.
> 
> You can also filter based on the HTTP method (`http_method`), Tag (`tag`), Operation ID (`operation_id`), or URL path (`Path`).

## Header authorization

A list of headers to be added to API requests. Used for applications that require additional headers outside of the usual username and password or API key, or if you want to customize the headers sent in the request. Header authentication can be used when you have a generated token ready for use.

Examples:  
`API-Key: 1234567890   X-API-Token: abc123`

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Header authorization</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>auth_headers</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>header</code></td></tr></tbody></table>

## Ignore request fields

Defines the specific request fields the connector should ignore.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#ignore-input-fields) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Ignore specific request fields</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.ignore_request_fields</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## OAuth2 authorization URL

URL that Workato redirects you to when you select the ‘Connect’ button. This usually brings you to the login screen of your app.

This should be publicly available from the API documentation of the app you’re connecting to, under the Authentication section.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>OAuth2 authorization URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>authorization_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 token URL

URL that Workato will retrieve an auth token from. This auth token is used to verify that we have permission to access your app and its data.

This should be publicly available from the API documentation of the app you’re connecting to, under the Authentication section.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>OAuth2 token URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>token_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 token request mode

Send client ID and secret in token request body or as a base64 encoded string in the header.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>How does the API require credentials to be sent to request a token?</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>access_token_request_mode</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code>.</td></tr></tbody></table>

## OAuth2 client ID

Public ID of the OAuth app that should be tied to Workato.

This is usually found in the Settings or Integrations page (or equivalent) of your logged in app account that you wish to connect to and should be kept secret.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Client ID</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>client_id</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 client secret

Matching private key that the application will verify along with the Client ID.

This is usually found in the Settings or Integrations page (or equivalent) of your logged in app account that you wish to connect to and should be kept secret.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Client Secret</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>client_secret</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 user

The name of the application user/account.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Username</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>username</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 password

The password of the user. An alternative to your password would be an API key or API token, retrieved from your account settings.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Password</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>username</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 scopes

Scopes are permissions that you can request from the app.

This is usually found in the Settings or Integrations page (or equivalent) of your logged in app account that you wish to connect to.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Scopes</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>scopes</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## Object hint

Defines the field in the OpenAPI document the connector should use to display object hints.

The [default implementation](#default-object_hint_field) allows the user to select between the `summary` and `description` fields.

Consider the following object from a sample OpenAPI document:

- If `summary`, **Update an existing pet** would be used as the object hint
- If `description`, **Update an existing pet by Id** would be used as the object hint

```json
{
   "paths":{
      "/pet":{
         "put":{
            "tags":[
               "pet"
            ],
            "summary":"Update an existing pet",
            "description":"Update an existing pet by Id",
            "operationId":"updatePet",
            "requestBody":{
               "description":"Update an existent pet in the store",
               "content":{ ... },
               "required":true
            }
         }
      }
   }
}
```

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#object-hints-links) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object hint</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_hint_field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Object hint substitutions

Defines a list of substitutions for object hints. Useful for modifying object hint field values and improving the object picker user experience.

Substitution objects include the following properties:

- `pattern`: A regular expression string, optionally including capture groups.
- `replacement`: The string value to replace all occurrences of `pattern`. This value may contain back-references to the `pattern`'s capture groups of:
  
  - The form `\d`, where `d` is a group **number**. For example: `\1`
  - Or `\k`, where `n` is a group **name**. For example: `\object`
  
  If a double-quoted string, both back-references must be preceded by an additional backslash (`\`). **Note**: Special match variables such as `$&` won't refer to the current match within the replacement.

Refer to the [Customizing OpenAPI interfaces guide](/connectors/openapi/guides/customizing-openapi-interfaces.html#object-hint-substitutions) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object hint substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_hint_substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Object name

Defines the field in the OpenAPI document the connector should use to display object names.

The [default implementation](#default-object_label_field) allows the user to select between the `summary` and `operation_id` fields.

Consider the following object from a sample OpenAPI document:

- If `summary`, **Update an existing pet** would be used as the object name
- If `operation_id`, **updatePet** would be used as the object name

```json
{
   "paths":{
      "/pet":{
         "put":{
            "tags":[
               "pet"
            ],
            "summary":"Update an existing pet",
            "description":"Update an existing pet by Id",
            "operationId":"updatePet",
            "requestBody":{
               "description":"Update an existent pet in the store",
               "content":{ ... },
               "required":true
            }
         }
      }
   }
}
```

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#object-names) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object name field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_label_field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Object name substitutions

Defines a list of substitutions for object names. Useful for modifying object name values and improving the object picker user experience.

Substitution objects include the following properties:

- `pattern`: A regular expression string, optionally including capture groups.
- `replacement`: The string value to replace all occurrences of `pattern`. This value may contain back-references to the `pattern`'s capture groups of:
  
  - The form `\d`, where `d` is a group **number**. For example: `\1`
  - Or `\k`, where `n` is a group **name**. For example: `\object`
  
  If a double-quoted string, both back-references must be preceded by an additional backslash (`\`). **Note**: Special match variables such as `$&` won't refer to the current match within the replacement.

Refer to the [Customizing OpenAPI interfaces guide](/connectors/openapi/guides/customizing-openapi-interfaces.html#object-hint-substitutions) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object name substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_name_substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Substitutions for grouping

Defines text-based substitution rules for endpoint grouping operations. This is useful when the built-in grouping rules do not meet the specific needs of your API structure.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-substitutions) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Substitutions for endpoint grouping</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.substitutions_for_grouping</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Operation name field

Defines the field to use for operation names in the picklist of the [**Execute API operation** action](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-assignment). Defaults to [object name field](#object-label-field).

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Operation name field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.execute_operation_label_field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Query param authorization

A list of query parameters to be added to the API requests.

Examples:  
`api_key: 1234567890   token: abc123`

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Query param authorization</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>query_params</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>query</code></td></tr></tbody></table>

## Record ID field name

Defines the name of the field that holds an object's unique ID value.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Record ID field name</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.record_id_field_name</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Static object names

Defines the a list of user-friendly names for objects and operations.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#static-object-names) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Static object names</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_label_map</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Only required if the OpenAPI document doesn't provide user-friendly names for individual API endpoints.</td></tr></tbody></table>

### Sample

```ruby
{
  ...
  "advanced" => {
    "object_label_map" => [
      {
        "operation_id" => "createPet",
        "label" => "Create a new Pet"
      },
      ...
    ]
  }
  ...
}
```

> **Object\_label\_map syntax**
> 
> You can format the `object_label_map` in the following ways:
> 
> 1. Provide an array of objects with `operation_id` and `label`. The example shown uses this syntax.
> 2. Provide an object with keys (for operation IDs) and values (display names/labels).

## Server URL

> **THIS IS A REQUIRED FIELD.**

A URL to the target host or service. Relative endpoint paths from the OpenAPI document will be appended to this URL to construct a full endpoint URL.

**Note**: If you want to hard-code this field's value - meaning end-users won't need to provide a value when setting up the connector - you'll need to provide the field in two methods:

- `adjust_connection`:
  
  ```ruby
  methods: {
      adjust_connection: lambda do |connection|
        connection.merge(
          {
            'definition_mode' => 'url',
            'definition_url' => 'https://petstore3.swagger.io/api/v3/openapi.yaml',
            'base_url' => 'https://petstore3.swagger.io/api/v3/',
            'documentation_href' => 'https://redocly.github.io/redoc/?url=https://petstore3.swagger.io/api/v3/openapi.yaml'
          }
        )
      end
    [ ... ]
  }
  ```
  
- `base_uri`:
  
  ```ruby
  base_uri: lambda do |connection|
    'https://petstore3.swagger.io/api/v3/'
  end
  ```
  

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Server URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>base_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes</td></tr></tbody></table>

## Test request URL

The relative path of an API endpoint the connector will use to test the connection.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Test endpoint path</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.test_endpoint</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Use HTTP method semantics for grouping

Indicates if HTTP methods should be used for [grouping API operations](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-assignment).

This should be enabled unless the endpoints in a Swagger file don't follow [REST guidelines](https://restfulapi.net/).

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Use HTTP method semantics for grouping operations</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.use_operation_names_for_grouping</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>
