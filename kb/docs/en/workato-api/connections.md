---
url: 'https://docs.workato.com/en/workato-api/connections.md'
description: >-
  Reference for the Workato developer API endpoints to list, create, update,
  disconnect, and delete connections, and get picklist values.
---

# Developer API - Connections

Use the following endpoints to manage connections.

## Rate limits

Connections resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List connections: [/api/connections](/en/workato-api/connections.html#list-connections) | 60 requests per minute |
| All | All other [Connections](/en/workato-api/connections.html) endpoints | 1 request per second |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/connections](#list-connections) | Lists connections belonging to a user. |
| POST | [/api/connections/:connection\_id/pick\_list](#get-picklist-values) | Gets picklist values for a connection. |
| POST | [/api/connections](#connections-create) | Creates a connection, including custom LLM and MCP server connections. |
| PUT | [/api/connections/:connection\_id](#update-a-connection) | Updates a connection. |
| POST | [/api/connections/:connection\_id/disconnect](#disconnect-a-connection) | Disconnects a connection. |
| DELETE | [/api/connections/:connection\_id](#delete-a-connection) | Deletes a connection. |

## List connections

Returns all connections and associated data for the authenticated Workato user.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/connections
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **string** _optional_ | Folder ID of the connection. |
| parent\_id | **string** _optional_ | Parent ID of the connection. Connection must be of the same provider. |
| project\_id | **string** _optional_ | The ID of the project containing the connection. |
| external\_id | **string** _optional_ | External identifier usually given to the user who owns the connection. |
| include\_runtime\_connections | **string** _optional_ | When `"true"` is supplied, all runtime user connections are also returned. |
| includes\[\] | **array of strings** _optional_ | Specifies additional fields to include in the response. Accepts `tags` as a value. If `tags` is supplied in the request, the response includes a `tags` field for each connection. This field contains an array of zero or more tag handles (strings). |
| updated\_after | **string** _optional_ | Filter the list of connections to include only those updated after the date and time you specify. The date and time must be provided in ISO 8601 format according to the following pattern: `YYYY-MM-DDTHH:MM:SSZ`. |

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/connections?includes[]=tags
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
[
  {
    "application": "salesforce",
    "id": 36,
    "name": "ACME Production Salesforce connection",
    "description": null,
    "authorized_at": "2015-05-26T22:53:52.528Z",
    "authorization_status": "success",
    "authorization_error": null,
    "created_at": "2015-05-26T22:53:52.532Z",
    "updated_at": "2015-05-26T22:53:52.532Z",
    "external_id": null,
    "folder_id": 4515,
    "connection_lost_at": null,
    "connection_lost_reason": null,
    "parent_id": null,
    "project_id": 12314295,
    "on_prem_group_id": null,
    "tags": [
      "tag-Abx8kS4d-Gp2YvB-CD"
    ]
  },
  {
    "application": "google_sheets",
    "id": 37,
    "name": "ACME google sheet account",
    "description": null,
    "authorized_at": "2015-05-26T22:53:52.528Z",
    "authorization_status": "success",
    "authorization_error": null,
    "created_at": "2015-05-26T22:53:52.532Z",
    "updated_at": "2015-05-26T22:53:52.532Z",
    "external_id": null,
    "folder_id": 4515,
    "connection_lost_at": null,
    "connection_lost_reason": null,
    "parent_id": null,
    "project_id": 12314295,
    "on_prem_group_id": null,
    "tags": null
  },
  {
    "application": "onprem_files",
    "id": 38,
    "name": "ACME on-prem files connection",
    "description": null,
    "authorized_at": "2015-05-26T22:53:52.528Z",
    "authorization_status": "success",
    "authorization_error": null,
    "created_at": "2015-05-26T22:53:52.532Z",
    "updated_at": "2015-05-26T22:53:52.532Z",
    "external_id": null,
    "folder_id": 4515,
    "connection_lost_at": null,
    "connection_lost_reason": null,
    "parent_id": null,
    "project_id": 12314295,
    "on_prem_group_id": 16803,
    "tags": null
  }
]
```

## Get picklist values

Returns a list of picklist values for a specified connection.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/connections/:connection_id/pick_list
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| connection\_id | **string** _required_ | The ID of the connection. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| pick\_list\_name | **string** _required_ | Name of the picklist. Refer to the [Picklist parameters](/en/oem/oem-api/picklist-parameters) reference for picklist names and parameters by connector. |
| pick\_list\_params | **Object** _optional_ | Picklist parameters, required for some picklists. |

### Sample request

This example curl request returns a list of Salesforce picklist values from the picklist `sobject_fields` for the `Account` object in Salesforce.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/connections/:connection_id/pick_list \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "pick_list_name": "sobject_fields",
            "pick_list_params": {
              "sobject_name": "Account"
            }
          }'
```

</api-code>

### Response

```json
{
    "result": [
        [
            "Account ID",
            "Id"
        ],
        [
            "Account Name",
            "Name"
        ],
        [
            "Account Type",
            "Type"
        ],
        [
            "Industry",
            "Industry"
        ],
        [
            "Annual Revenue",
            "AnnualRevenue"
        ],
        [
            "Owner ID",
            "OwnerId"
        ],
        [
            "Created Date",
            "CreatedDate"
        ]
    ]
}
```

## Create a connection

Create a new connection. This endpoint supports the following actions:

- Create a shell connection
- Create and authenticate a connection
- Create a custom LLM connection to use your own model with a genie
- Create an MCP server connection to assign to a genie

> **OAUTH CONNECTIONS**
> 
> The Developer API allows you to create OAuth 2.0 connections. However, connection types that would normally redirect you to a sign-in screen, such as `oauth` or `oauth2_auth_code_grant`, require an `oauth_token_pair` object containing an access token and a refresh token. Client credentials grant connections don't require an `oauth_token_pair` object. You can create a shell connection in cases where you don't have an access token and refresh token.
> 
> Refer to the [Connection parameters reference](/en/workato-api/connections-parameters-dev#oauth-authentication) page for more information.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/connections
```

</api-code>

### Payload

Include the following properties in the request body to filter results:

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Name of the connection. For example: `Prod JIRA connection` |
| provider | **string** _optional_ | The application type of the connection. For example: `jira` |
| parent\_id | **string** _optional_ | The ID of the parent connection. The parent connection must be the same `provider` type. [Learn more](/en/features/runtime-user-connections#what-are-parent-connections). |
| folder\_id | **string** _required_ | The ID of the project or folder containing the connection. |
| external\_id | **string** _optional_ | The external ID assigned to the connection, usually given to the user who owns the connection. |
| on\_prem\_group\_id | **integer** _optional_ | The ID of the on-prem group to associate with this connection. You can retrieve group IDs from the [List on-prem groups](/en/workato-api/on-prem#list-on-prem-groups) endpoint. |
| shell\_connection | **boolean** _optional_ | Specifies whether the connection is a shell connection or an authenticated connection. Defaults to `false` if not specified. If `shell_connection` is `false`, credentials are passed, and the connection is tested and established. If `shell_connection` is `true`, credentials are passed, but the connection isn't tested or established, and additional actions are required for authentication. |
| input | **Object** _optional_ | Connection parameters. For a list of providers and connection parameters, refer to the [Platform API connection parameter reference](/en/workato-api/connections-parameters-dev#connection-parameters-reference). For custom LLM and MCP server connections, refer to [Custom LLM connection input](#custom-llm-connection-input) and [MCP server connection input](#mcp-server-connection-input). |

#### Custom LLM connection input

Use these `input` fields to create a connection to your own LLM.

| Name | Type | Description |
| --- | --- | --- |
| provider | **string** _required_ | The LLM provider. |
| api\_key | **string** _required_ | The API key for the LLM provider. |
| api\_url | **string** _optional_ | The base URL of the LLM API. |
| model | **string** _required_ | The model the connection uses. For example: `<model_name>`. |

#### MCP server connection input

Use these `input` fields to create a connection to an MCP server.

| Name | Type | Description |
| --- | --- | --- |
| server\_url | **string** _required_ | The URL of the MCP server. |
| auth\_type | **string** _required_ | The authentication type the MCP server uses. |

> **FOLDER\_ID REQUIRED STARTING MAY 7, 2026**
> 
> Starting **May 7, 2026**, the `folder_id` parameter is required on this endpoint. The value must reference a project or folder other than the **Home assets** folder. Requests that omit `folder_id` or target the **Home assets** folder will return an error.

### Sample requests

- [Shell connection](#shell-connection)
- [Connection with credentials](#connection-credentials)
- [On-prem connection](#on-prem-connection)
- [Custom LLM connection](#custom-llm-connection)
- [MCP server connection](#mcp-server-connection)

#### Shell connection request

This creates a connection in a `Disconnected` state.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "folder_id": ":folder_id"
          }'
```

</api-code>

#### Connection with credentials

This creates and authenticates a connection.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "folder_id": ":folder_id",
            "input": {
              "host_name": ":host_name",
              "auth_type": ":auth_type",
              "email": ":email",
              "apitoken": ":apitoken"
            }
          }'
```

</api-code>

#### On-prem connection

This creates a connection associated with an on-prem group.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "folder_id": ":folder_id",
            "on_prem_group_id": :on_prem_group_id_value,
            "input": {
              "host": ":host",
              "port": ":port",
              "database": ":database",
              "username": ":username"
            }
          }'
```

</api-code>

#### Custom LLM connection

This creates a connection to your own LLM. The `id` in the response is the value you pass to a genie. Refer to [Use a custom LLM connection with a genie](#use-a-custom-llm-connection-with-a-genie).

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "provider": "byollm",
            "name": "Custom OpenAI",
            "folder_id": ":folder_id",
            "input": {
              "provider": "openai",
              "api_key": ":api_key",
              "model": "gpt-4o"
            }
          }'
```

</api-code>

#### MCP server connection

This creates a connection to an MCP server.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "folder_id": ":folder_id",
            "input": {
              "server_url": ":server_url",
              "auth_type": ":auth_type"
            }
          }'
```

</api-code>

### Response

```json
{
   "application":"jira",
   "id":36,
   "name":"Prod JIRA connection",
   "description":null,
   "authorized_at":"2023-01-26T22:53:52.528Z",
   "authorization_status":"success",
   "authorization_error":null,
   "created_at":"2023-01-26T22:53:52.532Z",
   "updated_at":"2023-01-26T22:53:52.532Z",
   "external_id":null,
   "folder_id":1892,
   "connection_lost_at":null,
   "connection_lost_reason":null,
   "parent_id":null,
   "project_id":12314295,
   "on_prem_group_id":null
}
```

The `id` is a unique identifier for the connection. For custom LLM and MCP server connections, use it to attach the connection to a genie:

- **Custom LLM connection**: Pass the `id` as `ai_provider` in [Update a genie](/en/workato-api/agent-studio#update-a-genie).
- **MCP server connection**: Pass the `id` when you [assign an MCP server to a genie](/en/workato-api/agent-studio#assign-a-skill-to-a-genie).

Example response for a custom LLM connection:

```json
{
   "application":"<provider>",
   "id":4821,
   "name":"Custom LLM connection",
   "description":null,
   "authorization_status":"success",
   "authorization_error":null,
   "folder_id":1892,
   "parent_id":null,
   "project_id":12314295,
   "on_prem_group_id":null
}
```

### Use a custom LLM connection with a genie

Convert the connection's `id` to a string and pass it as `ai_provider_id` with `ai_provider_type` set to `custom` in [Update a genie](/en/workato-api/agent-studio#update-a-genie) to power a genie with your custom LLM. The connection must use the `byollm` connector, be connected, and belong to a folder your API client can access.

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/agentic/genies/:genie_id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "ai_provider_type": "custom",
           "ai_provider_id": ":connection_id"
         }'
```

</api-code>

The following example creates a connection and captures its `id` for the genie update:

<api-code>

```shell
export LLM_CONNECTION_ID="$(
  curl -sS -X POST https://YOUR_DATA_CENTER/api/connections \
    -H 'Authorization: Bearer <api_token>' \
    -H 'Content-Type: application/json' \
    --data '{
      "provider": "byollm",
      "name": "Custom OpenAI",
      "folder_id": ":folder_id",
      "input": {
        "provider": "openai",
        "api_key": ":api_key",
        "model": "gpt-4o"
      }
    }' | jq -r '.id'
)"
```

</api-code>

## Update a connection

Updates a connection in a non-embedded workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/connections/:connection_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| connection\_id | **string** _required_ | The ID of the connection. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Name of the connection. For example: `Prod Salesforce connection` |
| parent\_id | **string** _optional_ | The ID of the parent connection. [Learn more](/en/features/runtime-user-connections#what-are-parent-connections). |
| folder\_id | **string** _optional_ | The ID of the project or folder containing the connection. |
| external\_id | **string** _optional_ | An external ID assigned to the connection. This value could reference a record in one of your other applications. |
| on\_prem\_group\_id | **integer** _optional_ | The ID of the on-prem group to associate with this connection. Set to `null` to remove the on-prem group association. You can retrieve group IDs from the [List on-prem groups](/en/workato-api/on-prem#list-on-prem-groups) endpoint. |
| shell\_connection | **boolean** _optional_ | Specifies whether the connection is a shell connection or an authenticated connection. Defaults to `false` if not specified. If `shell_connection` is `false`, credentials are passed, and the connection is tested and established. If `shell_connection` is `true`, credentials are passed, but the connection isn't tested or established, and additional actions are required for authentication. |
| input | **object** _optional_ | Connection parameters. For a list of providers and connection parameters, refer to the [Platform API connection parameter reference](/en/workato-api/connections-parameters-dev#connection-parameters-reference). You can update `input.model` for custom LLM connections. Refer to [Custom LLM connection input](#custom-llm-connection-input). |

### Sample requests

- [Update a Jira connection](#jira-update)
- [Update an Outreach connection](#outreach-update)

#### Update a Jira connection

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/connections/:connection_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "folder_id": ":folder_id",
            "input": {
              "host_name": ":host_name",
              "api_token_auth": ":api_token_auth",
              "email": ":email",
              "apitoken": ":apitoken"
            }
          }'
```

</api-code>

### Response

```json
{
   "application":"jira",
   "id":36,
   "name":"jira_connection",
   "description":null,
   "authorized_at":"2015-05-26T22:53:52.528Z",
   "authorization_status":"success",
   "authorization_error":null,
   "created_at":"2015-05-26T22:53:52.532Z",
   "updated_at":"2015-05-26T22:53:52.532Z",
   "external_id":"U12904",
   "folder_id":4515,
   "connection_lost_at":null,
   "connection_lost_reason":null,
   "parent_id":22318,
   "project_id":12314295,
   "on_prem_group_id":null
}
```

#### Update an Outreach connection

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/connections/:connection_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "input": {
              "advanced_settings": {
                "scopes": ":scopes"
              }
            }
          }'
```

</api-code>

## Disconnect a connection

Disconnects an active connection in a non-embedded workspace. If the connection is already disconnected, no action is taken.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/connections/:connection_id/disconnect
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| connection\_id | **string** _required_ | The ID of the connection. |
| force | **boolean** _optional_ | Value must be `true` to forcefully disconnect an active connection used by active recipes. Defaults to `false`. |

### Payload

No payload is expected.

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/connections/:connection_id/disconnect \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{ "force": :true_or_false }'
```

</api-code>

### Response

- Successfully disconnected an active connection or connection already disconnected.

```json
{
    "success": true,
    "status": "disconnected"

}
```

- Provided connection ID does not exist

```json
{
   "message": "Not found"
}
```

* * *

## Delete a connection

Deletes a connection in a non-embedded workspace. This method deletes active (authenticated) and disconnected connections. If the connection is used by active recipes or as an [Audit log streaming destination](/en/features/activity-audit-log-streaming-destinations), this API request fails.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/connections/:connection_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| connection\_id | **string** _required_ | The ID of the connection. |

### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/connections/:connection_id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

- [Successful deletion of an active or disconnected connection](#success)
- [Connection is used in active recipes](#active-recipes-fail)
- [Connection is used for Audit log streaming](#als-destination-fail)
- [Connection ID doesn't exist](#not-exist-fail)

#### Successful deletion of an active or disconnected connection

When you successfully delete an active (authenticated) or disconnected connection, this endpoint returns the following response:

```json
{
    "success": true,
    "status": "deleted"
}
```

#### Connection is used in active recipes

When you try to delete a connection used by an active recipe, this request fails, and the endpoint returns the following response:

```json
{
   "success": false,
   "status": "rejected",
   "message": "You can't delete a connection used by active recipes"
}
```

#### Connection is used for Audit log streaming

When you try to delete a connection used as an [Audit log streaming destination](/en/features/activity-audit-log-streaming-destinations), this request fails, and the endpoint returns the following response:

```json
{
    "success": false,
    "status": "rejected",
    "message": "You can't delete a connection used by audit log streaming"
}
```

#### Connection ID doesn't exist

If you provide a connection ID that doesn't exist in your workspace, this request fails, and the endpoint returns the following response:

```json
{
   "message": "Not found"
}
```

---
