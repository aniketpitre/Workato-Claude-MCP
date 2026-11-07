---
url: 'https://docs.workato.com/en/oem/oem-api/environment-roles.md'
description: >-
  Reference for the Embedded API environment roles endpoints to list, create,
  update, and delete environment roles in customer workspaces.
---

# Embedded API - Environment roles

Use the following endpoints to manage [environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) in an Embedded customer workspace.

Environment roles can have the following values:

| Value | Definition |
| --- | --- |
| system | Default roles provided by Workato. |
| custom | Roles created manually within a workspace. |
| inheritable | Custom roles from an AHQ admin or Embedded partner workspace that are inheritable by child workspaces. |
| inherited | Roles inherited by a child workspace from its AHQ or Embedded parent workspace. |

> **LEGACY ROLE COMPATIBILITY**
> 
> The following endpoints are only compatible with new roles where the `role_type` is `environment`.
> 
> Use the [/api/managed\_users/:id/roles](/en/oem/oem-api/roles) endpoints instead to manage legacy roles where the `role_type` is `privilege_group`.

## Rate limits

The environment roles resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All[](/en/oem/oem-api/environment-roles.html) | All [Environment roles](/en/oem/oem-api/environment-roles.html) endpoints | 10 requests per second |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles](#list-env-roles) | List environment roles in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles/:id](#get-env-role) | Get an environment role from a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles](#create-env-role) | Create an environment role in a customer workspace. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles/:id](#update-env-role) | Update an environment role in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles/:id](#delete-env-role) | Delete an environment role in a customer workspace. |

## List environment roles in a customer workspace

Retrieves a list of [environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) from an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filter environment roles by their name. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles?name=:name&page[number]=:page_number_value&page[size]=:page_size_value' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": 1,
      "name" : "Developer",
      "members_count": 2,
      "type": "custom",
      "created_at": "2024-08-02T13:35:11.691-07:00",
      "updated_at": "2024-08-02T13:35:11.691-07:00"
    }
  ],
  "total": 1,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

## Get an environment role from a customer workspace

Retrieves an [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) from an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the environment role to retrieve. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 1,
    "name" : "Developer",
    "config": { "team": { "privileges": "all" } },
    "members_count": 2,
    "type": "custom",
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

## Create an environment role in a customer workspace

Creates a new [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) in an Embedded customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| environment\_role | **object** _required_ | Defines the environment role to create. |
| environment\_role\[name\] | **string** _required_ | The name of the environment role to create. The maximum length is `200` characters. |
| environment\_role\[config\] | **object** _required_ | Defines the privileges assigned to the role. |
| environment\_role\[inheritable\] | **boolean** _optional_ | Child workspaces inherit the role when set to `true`. The default value is `false`. This value can only be set to `true` in Admin AHQ or Embedded partner workspaces. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "environment_role": {
          "name": ":name",
          "config": { "team": { "privileges": ":privileges" } },
          "inheritable": :true_or_false
        }
      }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 1,
    "name" : "Developer",
    "config": { "team": { "privileges": "all" } },
    "members_count": 0,
    "type": "custom",
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

## Update an environment role in a customer workspace

Updates an existing [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) in an Embedded customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the environment role to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| environment\_role | **object** _required_ | Defines the updated environment role. |
| environment\_role\[name\] | **string** _required_ | The updated name of the environment role. The maximum length is `200` characters. |
| environment\_role\[config\] | **object** _required_ | Defines the updated privileges for the role. |
| environment\_role\[inheritable\] | **boolean** _optional_ | Child workspaces inherit the role when set to `true`. The default value is `false`. This value can only be set to `true` in Admin AHQ or Embedded partner workspaces. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "environment_role": {
          "name": ":name",
          "config": { "team": { "privileges": ":privileges" } },
          "inheritable": :true_or_false
        }
      }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 1,
    "name" : "Builder",
    "config": { "team": { "privileges": "all" } },
    "members_count": 0,
    "type": "custom",
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

## Delete an environment role in a customer workspace

Deletes an [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) in an Embedded customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the environment role to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environment_roles/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The API deletes the environment role and returns an empty response body.

400 BAD REQUEST

A `400 Bad Request` error indicates that the server couldn't process the request due to client-side issues. Common causes include malformed requests, invalid fields, or violations of field constraints, such as unsupported data types.

In the following example, the request fails because the role is still assigned to collaborators:

```json
{
  "errors": [
    {
      "code": "bad_request",
      "title": "You can’t delete a role when collaborators are assigned to the role."
    }
  ]
}
```

---
