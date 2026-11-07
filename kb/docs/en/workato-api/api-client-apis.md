---
url: 'https://docs.workato.com/en/workato-api/api-client-apis.md'
description: >-
  Reference for the Workato developer API endpoints to list, create, update,
  delete, and regenerate tokens for API clients and client roles.
---

# Developer API - API clients

The following endpoints allow you to manage your API clients via developer APIs. This allows you to programmatically create new API clients when onboarding new teams or rotate API tokens regularly for all your API clients.

## Rate limits

API client resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [API client](https://docs.workato.com/workato-api/api-client-apis.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/developer\_api\_clients](#list-developer-api-clients) | List **Developer API Clients**. |
| POST | [/api/developer\_api\_clients](#create-developer-api-client) | Create **Developer API Client**. |
| GET | [/api/developer\_api\_clients/:id](#get-developer-api-client-by-id) | Get **Developer API Client by ID**. |
| PUT | [/api/developer\_api\_clients/:id](#update-developer-api-client) | Update **Developer API Clients**. |
| DELETE | [/api/developer\_api\_clients/:id](#delete-developer-api-client) | Delete **Developer API Client**. |
| POST | [/api/developer\_api\_clients/:id/regenerate](#regenerate-developer-api-client-token) | Regenerate **Developer API Client token**. |
| GET | [/api/developer\_api\_client\_roles](#list-developer-api-client-roles) | List **Developer API Client roles**. |

## List Developer API clients

List all Developer API clients.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/developer_api_clients
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| per\_page | **integer** | Number of API clients to return in a single page. Defaults to `100`. Max is `100`. |
| page | **integer** | Page number of the API clients to fetch. Defaults to `1`. |

#### Sample Request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/developer_api_clients \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "count": 3,
        "items": [
            {
                "id": 40947,
                "name": "Test",
                "api_privilege_group_id": 26779,
                "created_at": "2023-02-22T01:55:35.739-08:00",
                "updated_at": "2023-02-28T01:23:18.046-08:00",
                "all_folders": false,
                "folder_ids": [
                    26138,
                    26136
                ],
                "environment_name": "Development",
                "environment_id": 3218,
                "ip_allow_list": "192.0.2.10,198.51.100.5",
                "token": {
                    "updated_at": "2023-02-22T09:55:36.427Z"
                }
            },
        ]
    }
}
```

* * *

## Create a Developer API client

Create a Developer API client.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/developer_api_clients
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **String** | Name of the API client |
| api\_privilege\_group\_id | **integer** | API client role ID |
| all\_folders | **boolean** _required_ | Flag indicating whether API client has access to all folders |
| folder\_ids | **array** | Array of folder IDs. Required if `all_folders` is false. |
| environment\_name | **string** | Name of the environment. Required if your workspace has environments enabled. |
| ip\_allow\_list | **string** _optional_ | Array of IP addresses allowed to access the API client. Defaults to all IPs if not specified. |

#### Sample Request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/developer_api_clients \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "api_privilege_group_id": :api_privilege_group_id_value,
            "environment_name": ":environment_name",
            "all_folders": :true_or_false,
            "ip_allow_list": ":ip_allow_list"
          }'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40948,
        "name": "Test Client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-02-28T02:09:07.255-08:00",
        "updated_at": "2023-02-28T02:09:07.586-08:00",
        "all_folders": true,
        "environment_name": "Development",
        "environment_id": 3218,
        "ip_allow_list": "192.0.2.10,198.51.100.5",
        "token": {
            "updated_at": "2023-02-28T10:09:07.579Z",
            "value": "wrkaus-eyJhbGciOiJSUz..."
        }
    }
}
```

* * *

## Get a Developer API client by ID

Get a Developer API client by ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/developer_api_clients/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the API Client. |

#### Sample Request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/developer_api_clients/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40948,
        "name": "Test Client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-02-28T02:09:07.255-08:00",
        "updated_at": "2023-02-28T02:09:07.586-08:00",
        "all_folders": true,
        "environment_name": "Development",
        "environment_id": 3218,
        "token": {
            "updated_at": "2023-02-28T10:09:07.579Z"
        },
        "user": {
            "id": 3218,
            "name": "Workato Customer Success test"
        }
    }
}
```

* * *

## Update a Developer API client

Update a Developer API client.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/developer_api_clients/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the API Client. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **String** | Name of the API client |
| api\_privilege\_group\_id | **integer** | API client role ID |
| all\_folders | **boolean** _required_ | Flag indicating whether API client has access to all folders |
| folder\_ids | **array** | Array of folder IDs. Required if `all_folders` is false. |
| environment\_name | **string** | Name of the environment. Required if your workspace has environments enabled. |
| ip\_allow\_list | **string** _optional_ | Array of IP addresses allowed to access the API client. Defaults to all IPs if not specified. |

#### Sample Request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/developer_api_clients/:id \
      -H 'Authorization: Bearer <api_token>'  \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "api_privilege_group_id": :api_privilege_group_id_value,
            "environment_name": ":environment_name",
            "all_folders": :true_or_false,
            "ip_allow_list": ":ip_allow_list"
          }'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40948,
        "name": "Test Client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-02-28T02:09:07.255-08:00",
        "updated_at": "2023-02-28T02:09:07.586-08:00",
        "all_folders": true,
        "environment_name": "Development",
        "environment_id": 3218,
        "ip_allow_list": "192.0.2.10,198.51.100.5",
        "token": {
            "updated_at": "2023-02-28T10:09:07.579Z"
        },
        "user": {
            "id": 3218,
            "name": "Workato Customer Success test"
        }
    }
}
```

* * *

## Delete a Developer API client

Delete a Developer API client.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/developer_api_clients/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the API Client. |

#### Sample Request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/developer_api_clients/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": "success"
}
```

* * *

## Regenerate a Developer API Client token

Regenerates the API token for an API client. This invalidates the previous API token.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/developer_api_clients/:id/regenerate
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the API Client. |

#### Sample Request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/developer_api_clients/:id/regenerate \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 40890,
        "name": "Test new API client",
        "api_privilege_group_id": 26779,
        "created_at": "2023-01-29T22:30:12.930-08:00",
        "updated_at": "2023-02-28T02:19:16.542-08:00",
        "all_folders": true,
        "environment_name": "Development",
        "environment_id": 3218,
        "token": {
            "updated_at": "2023-02-28T10:19:16.530Z",
            "value": "wrkaus-eyJhbGc..."
        }
    }
}
```

* * *

## List Developer API client roles

List all Developer API Client roles.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/developer_api_client_roles
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| per\_page | **integer** | Number of API clients to return in a single page. Defaults to `100`. Max is `100`. |
| page | **integer** | Page number of the API clients to fetch. Defaults to `1`. |

#### Sample Request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/developer_api_client_roles \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "items": [
            {
                "id": 26779,
                "name": "Admin",
                "created_at": "2023-01-18T04:31:03.302-08:00",
                "updated_at": "2023-02-28T01:23:01.427-08:00"
            },
            ...
        ],
        "count": 3,
        "page": 1,
        "per_page": 100
    }
}
```

---
