---
url: 'https://docs.workato.com/en/oem/oem-api/project-roles.md'
description: >-
  Reference for Embedded API endpoints to list, get, create, update, and delete
  project roles in customer workspaces.
---

# Embedded API - Project roles

Use the following endpoints to manage [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) in an Embedded customer workspace.

Project roles can have the following values:

| Value | Definition |
| --- | --- |
| system | Default roles provided by Workato. |
| custom | Roles created manually within a workspace. |
| inheritable | Custom roles from an AHQ admin or Embedded partner workspace that are inheritable by child workspaces. |
| inherited | Roles inherited by a child workspace from its AHQ or Embedded parent workspace. |

## Rate limits

The project roles resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All[](/en/oem/oem-api/project-roles.html) | All [Project roles](/en/oem/oem-api/project-roles.html) endpoints | 10 requests per second |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/project\_roles](#list-project-roles) | List project roles in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/project\_roles/:id](#get-role) | Get a project role from a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/project\_roles](#create-role) | Create a project role in a customer workspace. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/project\_roles/:id](#update-role) | Update a project role in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/project\_roles/:id](#delete-role) | Delete a project role from a customer workspace. |

## List project roles in a customer workspace

Retrieves a list of [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) from an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filter project roles by their name. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles?name=:name&page[number]=:page_number_value&page[size]=:page_size_value' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": "prjrl-APmWpgTs-dwARGH",
      "name" : "Builder",
      "members_count": 1,
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

## Get a project role from a customer workspace

Retrieves a [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) from an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the project role to retrieve. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": {
    "id": "prjrl-APmWpgTs-dwARGH",
    "name" : "Developer",
    "config": { "recipe": { "privileges": "all" } },
    "members_count": 1,
    "type": "custom",
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

## Create a project role in a customer workspace

Creates a new [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) in an Embedded customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| project\_role | **object** _required_ | Defines the project role to create. |
| project\_role\[name\] | **string** _required_ | The name of the project role to create. The maximum length is `200` characters. |
| project\_role\[config\] | **object** _required_ | Defines the privileges for the role. |
| project\_role\[inheritable\] | **boolean** _optional_ | Child workspaces inherit the role when set to `true`. The default value is `false`. This value can only be set to `true` in Admin AHQ or Embedded partner workspaces. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "project_role": {
          "name": ":name",
          "config": { "recipe": { "privileges": ":privileges" } },
          "inheritable": :true_or_false
        }
      }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": "prjrl-APmWpgTs-dwARGH",
    "name" : "Builder",
    "config": { "recipe": { "privileges": "all" } },
    "members_count": 0,
    "type": "custom",
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

## Update a project role in a customer workspace

Updates an existing [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) in an Embedded customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the project role to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| project\_role | **object** _required_ | Defines the updated project role. |
| project\_role\[name\] | **string** _required_ | The updated project role name. The maximum length is `200` characters. |
| project\_role\[config\] | **object** _required_ | Defines the updated privileges for the project role. |
| project\_role\[inheritable\] | **boolean** _optional_ | Child workspaces inherit the role when set to `true`. The default value is `false`. This value can only be set to `true` in Admin AHQ or Embedded partner workspaces. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "project_role": {
          "name": ":name",
          "config": { "recipe": { "privileges": ":privileges" } },
          "inheritable": :true_or_false
        }
      }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": "prjrl-APmWpgTs-dwARGH",
    "name" : "Builder",
    "config": { "recipe": { "privileges": "all" } },
    "members_count": 1,
    "type": "custom",
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

## Delete a project role from a customer workspace

Deletes a project role from an Embedded customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the project role to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/project_roles/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The API deletes the project role and returns an empty response body.

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
