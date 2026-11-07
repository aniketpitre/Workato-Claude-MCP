---
url: 'https://docs.workato.com/en/oem/oem-api/connections.md'
description: >-
  Reference for Workato Embedded API endpoints to create, list, update,
  disconnect, and delete connections for Embedded customers.
---

# Embedded API - Connections

The **Connections** resource enables you to programmatically manage connections for Embedded customers.

> **ENDPOINT AVAILABILITY**
> 
> The endpoints in this guide are Embedded APIs and require an Embedded workspace. Contact your Workato representative for more information.

## Rate limits

Connection resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List connections: [/api/managed\_users/:managed\_user\_id /connections](/en/oem/oem-api/connections.html#list-connections) | 1,000 requests per minute |
| All | All other [Connections](/en/oem/oem-api/connections.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/connections/:adapter\_name/input\_schema](#get-connection-endpoint) | Returns input schema based on a connection's input. |
| GET | [/api/managed\_users/:managed\_user\_id/connections](#list-connections) | Returns a list of connections in Embedded user's account. |
| POST | [/api/managed\_users/:id/connections](#create-a-connection) | Allows the Embedded partner to add a shell connection in a customer's account. |
| PUT | [/api/managed\_users/:id/connections/:connection\_id](#update-a-connection) | Updates a connection in a customer workspace. |
| POST | [/api/managed\_users/:id/connections/:connection\_id/disconnect](#disconnect-a-connection) | Disconnects a connection in a customer workspace. |
| DELETE | [/api/managed\_users/:id/connections/:connection\_id](#delete-a-connection) | Deletes a connection in a customer workspace. |

* * *

## Get connection endpoint

Returns input schema based on a connection's input. It returns both the base input schema, part of the `extended_settings_schema` that activates because of the connection's input. This endpoint works at a connection level of Workato.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id/input_schema
```

</api-code>

Refer to [Get connector endpoint](/en/oem/oem-api/adapters#get-connector-endpoint) for information about the get connector endpoint.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix 'E' and be URL-encoded. For example, 'EA2300'. |
| connection\_id | **string** _required_ | The connection ID for which you plan to get the base input schema. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id/input_schema \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```JSON
{
  "result": [
    {
      "control_type": "text",
      "label": "Api key",
      "disable_formula": true,
      "optional": false,
      "type": "string",
      "name": "apiKey"
    }
  ]
}
```

## List connections

Returns all connections and associated data for the Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (ex: `EA2300`) and the resulting ID should be URL encoded. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| provider | **string** _optional_ | The application type of the connection. For example: `salesforce` |
| folder\_id | **string** _optional_ | The ID of the project or folder containing the connection. |
| parent\_id | **string** _optional_ | The ID of the parent connection. The parent connection must be the same `provider` type. [Learn more](/en/features/runtime-user-connections#what-are-parent-connections). |
| project\_id | **string** _optional_ | The ID of the project containing the connection. |
| external\_id | **string** _optional_ | The external ID assigned to the connection, usually given to the user who owns the connection. |
| include\_runtime\_connections | **string** _optional_ | When `"true"` is supplied, all runtime user connections are also returned. |
| includes\[\] | **array of strings** _optional_ | Specifies additional fields to include in the response. Accepts `tags` as a value. If `tags` is supplied in the request, the response includes a `tags` field for each connection. This field contains an array of zero or more tag handles (strings). |
| updated\_after | **string** _optional_ | Filter the list of connections to include only those updated after the date and time you specify. The date and time must be provided in ISO 8601 format according to the following pattern: `YYYY-MM-DDTHH:MM:SSZ`. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections?includes[]=:includes_value \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
 "result": [
   {
     "id": 36,
     "name": "ACME Production Salesforce connection",
     "provider": "salesforce",
     "authorized_at": "2015-05-26T22:53:52.528Z",
     "authorization_status": "success",
     "authorization_error": null,
     "created_at": "2015-05-26T22:53:52.532Z",
     "updated_at": "2015-05-26T22:53:52.532Z",
     "external_id": "U12904",
     "folder_id": 4515,
     "identity": null,
     "connection_lost_at": null,
     "connection_lost_reason": null,
     "parent_id": 22316,
     "project_id": 12314295,
     "on_prem_group_id": null,
     "tags": [
        "tag-Abx8kS4d-Gp2YvB-CD"
      ]
   },
   {
     "id": 37,
     "name": "ACME google sheet account",
     "provider": "google_sheets",
     "authorized_at": "2015-05-26T22:53:52.528Z",
     "authorization_status": "success",
     "authorization_error": null,
     "created_at": "2015-05-26T22:53:52.532Z",
     "updated_at": "2015-05-26T22:53:52.532Z",
     "external_id": "U12904",
     "folder_id": 4515,
     "identity": null,
     "connection_lost_at": "2024-06-01T12:00:00Z",
     "connection_lost_reason": "network_failure",
     "parent_id": 22317,
     "project_id": 12314296,
     "on_prem_group_id": null,
     "tags": null
   },
   {
     "id": 51234,
     "name": "ACME Quickbooks account",
     "provider": "quickbooks",
     "authorized_at": "2015-05-26T22:53:52.528Z",
     "authorization_status": "success",
     "authorization_error": null,
     "created_at": "2015-05-26T22:53:52.532Z",
     "updated_at": "2015-05-26T22:53:52.532Z",
     "external_id": "U12904",
     "folder_id": 4515,
     "identity": "acme@workato.com/1029384756102938",
     "connection_lost_at": null,
     "connection_lost_reason": null,
     "parent_id": 22317,
     "project_id": 12314297,
     "on_prem_group_id": null,
     "tags": [
        "tag-Abx8kS4d-Gp2YvB-CD"
      ]
   },
   {
     "id": 38,
     "name": "ACME on-prem files connection",
     "provider": "onprem_files",
     "authorized_at": "2015-05-26T22:53:52.528Z",
     "authorization_status": "success",
     "authorization_error": null,
     "created_at": "2015-05-26T22:53:52.532Z",
     "updated_at": "2015-05-26T22:53:52.532Z",
     "external_id": "U12904",
     "folder_id": 4515,
     "identity": null,
     "connection_lost_at": null,
     "connection_lost_reason": null,
     "parent_id": null,
     "project_id": 12314298,
     "on_prem_group_id": 16803,
     "tags": null
   }
 ]
}
```

  

> **RETRIEVE QUICKBOOKS REALM ID**
> 
> Retrieve your company's Quickbooks Realm ID using the [List connections](/en/oem/oem-api/connections#list-connections) API. Disconnect and reconnect your Quickbooks connection in Workato before calling the API to ensure the latest information is retrieved. The API returns the Realm ID in the `identity` field of the response, following your email address. In the preceding example, ACME's Realm ID is `1029384756102938`. For other connections, the identity field is returned as `null`.
> 
> Refer to the [SDK identity lambda documentation](/en/developing-connectors/sdk/sdk-reference/connection/authorization#identity) for more details on setting up the `identity` field. The lambda’s output value is returned in the `identity` field of the list connections API.

* * *

## Create a connection

Creates a connection in a customer's account. This endpoint supports the following in customer workspaces:

- Adding a shell connection, OR
- Adding and authenticating a connection

> **OAUTH CONNECTIONS**
> 
> The Workato API allows you to create OAuth 2.0 connections. However, connections types that would normally redirect you to a sign-in screen, such as `oauth` or `oauth2_auth_code_grant`, require an `oauth_token_pair` object containing an access token and a refresh token. Client credentials grant connections don't require an `oauth_token_pair` object. You can create a shell connection in cases where you don't have an access token and refresh token.
> 
> Refer to the [Connection parameters reference](/en/oem/oem-api/connections-parameters#oauth-authentication) page for more information.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (ex: `EA2300`) and the resulting ID should be URL encoded. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Name of the connection. Eg: `Prod Salesforce connection` |
| provider | **string** _optional_ | The application type of the connection. For example: `salesforce` |
| parent\_id | **string** _optional_ | The ID of the parent connection. The parent connection must be the same `provider` type. [Learn more](/en/features/runtime-user-connections#what-are-parent-connections). |
| folder\_id | **string** _required_ | The ID of the project or folder containing the connection. |
| external\_id | **string** _optional_ | The external ID assigned to the connection, usually given to the user who owns the connection. |
| on\_prem\_group\_id | **integer** _optional_ | The ID of the on-prem group to associate with this connection. You can retrieve group IDs from the [List on-prem groups](/en/oem/oem-api/on-prem#list-on-prem-groups) endpoint. |
| shell\_connection | **boolean** _optional_ | Specifies whether the connection is a shell connection or an authenticated connection. Defaults to `false` if not specified. If `shell_connection` is `false`, credentials are passed, and the connection is tested and established. If `shell_connection` is `true`, credentials are passed, but the connection isn't tested or established, and additional actions are required for authentication. |
| input | **Object** _optional_ | Connection parameters. For a list of providers and connection parameters, refer to the [Platform API Connection Parameter Reference](/en/oem/oem-api/connections-parameters). |

> **FOLDER\_ID REQUIRED STARTING MAY 7, 2026**
> 
> Starting **May 7, 2026**, the `folder_id` parameter is required on this endpoint. The value must reference a project or folder other than the **Home assets** folder. Requests that omit `folder_id` or target the **Home assets** folder will return an error.

### Sample requests

- [Shell connection (no credentials)](#shell-connection-request)
- [Connection with credentials](#connection-with-credentials)
- [On-prem connection](#on-prem-connection)

#### Shell connection request

This creates a connection in a `Disconnected` state.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "folder_id": :folder_id_value,
            "external_id": ":external_id"
          }'
```

</api-code>

#### Connection with credentials

This creates and authenticates a connection.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "folder_id": :folder_id_value,
            "input": {
              "host_name": ":host_name",
              "api_token_auth": ":api_token_auth",
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
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "provider": ":provider",
            "folder_id": :folder_id_value,
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

### Response

```json
{
   "id":36,
   "name":"jira_connection",
   "provider":"jira",
   "authorized_at":"2015-05-26T22:53:52.528Z",
   "authorization_status":"success",
   "authorization_error":null,
   "created_at":"2015-05-26T22:53:52.532Z",
   "updated_at":"2015-05-26T22:53:52.532Z",
   "external_id":"U12904",
   "folder_id":1892,
   "parent_id":22318,
   "connection_lost_at": null,
   "connection_lost_reason": null,
   "on_prem_group_id": null
}
```

* * *

## Update a connection

Updates a connection in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (ex: `EA2300`) and the resulting ID should be URL encoded. |
| connection\_id | **string** _required_ | The ID of the connection. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Name of the connection. Ex: `Prod Salesforce connection` |
| parent\_id | **string** _optional_ | The ID of the parent connection. [Learn more](/en/features/runtime-user-connections#what-are-parent-connections). |
| folder\_id | **string** _optional_ | The ID of the project or folder containing the connection. |
| external\_id | **string** _optional_ | An external ID assigned to the connection. This value could reference a record in another of your applications. |
| on\_prem\_group\_id | **integer** _optional_ | The ID of the on-prem group to associate with this connection. Set to `null` to remove the on-prem group association. You can retrieve group IDs from the [List on-prem groups](/en/oem/oem-api/on-prem#list-on-prem-groups) endpoint. |
| shell\_connection | **boolean** _optional_ | Specifies whether the connection is a shell connection or an authenticated connection. Defaults to `false` if not specified. If `shell_connection` is `false`, credentials are passed, and the connection is tested and established. If `shell_connection` is `true`, credentials are passed, but the connection isn't tested or established, and additional actions are required for authentication. |
| input | **object** _optional_ | Connection parameters. For a list of providers and connection parameters, refer to the [Platform API Connection Parameter Reference](/en/oem/oem-api/connections-parameters). |

### Sample requests

- [Update a Jira connection](#jira-update)
- [Update an Outreach connection](#outreach-update)

#### Update a Jira connection

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "folder_id": :folder_id_value,
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
   "id":36,
   "name":"jira_connection",
   "provider":"jira",
   "authorized_at":"2015-05-26T22:53:52.528Z",
   "authorization_status":"success",
   "authorization_error":null,
   "created_at":"2015-05-26T22:53:52.532Z",
   "updated_at":"2015-05-26T22:53:52.532Z",
   "external_id":"U12904",
   "folder_id":4515,
   "parent_id":22318,
   "connection_lost_at": null,
   "connection_lost_reason": null,
   "on_prem_group_id": null
}
```

#### Update an Outreach connection

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id \
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

* * *

## Disconnect a connection

Disconnects an active connection in a customer workspace. If the connection is already disconnected, then no action is taken.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id/disconnect
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (ex: `EA2300`) and the resulting ID should be URL encoded. |
| connection\_id | **string** _required_ | The ID of the connection. |
| force | **boolean** _optional_ | Value must be `true` to forcefully disconnect an active connection used by active recipes. Defaults to `false`. |

### Payload

No payload is expected

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id/disconnect?force=:force_value \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

- Successfully disconnected an active connection or connection already disconnected.

```json
{
   "result": {
    "success": true,
    "status": "disconnected"
   }
}
```

- Provided connection id does not exist

```json
{
   "message": "Not found"
}
```

* * *

## Delete a connection

Deletes a connection in a customer workspace. This method deletes active (authenticated) and disconnected connections. If the connection is used by active recipes, this API request fails.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (ex: `EA2300`) and the resulting ID should be URL encoded. |
| connection\_id | **string** _required_ | The ID of the connection. |

### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

- [Successful deletion of an active or disconnected connection](#success)
- [Connection is used in active recipes](#active-recipes-fail)
- [Connection ID doesn't exist](#not-exist-fail)

#### Successful deletion of an active or disconnected connection

When you successfully delete an active (authenticated) or disconnected connection, this endpoint returns the following response:

```json
{
    "result": {
        "success": true,
        "status": "deleted"
    }
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

#### Connection ID doesn't exist

If you provide a connection ID that doesn't exist in your customer's workspace, this request fails, and the endpoint returns the following response:

```json
{
   "message": "Not found"
}
```

---
