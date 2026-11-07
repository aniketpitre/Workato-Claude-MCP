---
url: 'https://docs.workato.com/en/workato-api/environment-roles.md'
description: >-
  Reference for the Workato environment roles API to list, retrieve, create,
  update, and delete environment roles in your workspace.
---

# Developer API - Environment roles

Use the following endpoints to manage your [environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles).

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
> Use the [/api/roles](/en/workato-api/roles) endpoints instead to manage legacy roles where the `role_type` is `privilege_group`.

## Rate limits

The environment roles resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All[](/en/workato-api/environment-roles.html) | All [Environment roles](/en/workato-api/environment-roles.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/environment\_roles](#list-env-roles) | List environment roles. |
| GET | [/api/environment\_roles/:id](#get-env-role) | Get environment role details. |
| POST | [/api/environment\_roles](#create-env-role) | Create an environment role. |
| PUT | [/api/environment\_roles/:id](#update-env-role) | Update an environment role. |
| DELETE | [/api/environment\_roles/:id](#delete-env-role) | Delete an environment role. |

## List environment roles

Retrieves a list of [environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) from your workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/environment_roles
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filter environment roles by their name. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/environment_roles?name=:name_value&page[number]=:page_number_value&page[size]=:page_size_value' \
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

## Get environment role details

Retrieves an [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/environment_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the environment role to retrieve. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/environment_roles/:id' \
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

## Create an environment role

Creates a new [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/environment_roles
```

</api-code>

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
curl -X POST 'https://YOUR_DATA_CENTER/api/environment_roles' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "environment_role": {
          "name": ":name",
          "config": :config,
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

## Update an environment role

Updates an existing [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) by its ID.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/environment_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the environment role to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| environment\_role | **object** _required_ | Defines the updated environment role. |
| environment\_role\[name\] | **string** _required_ | The updated name of the environment role. The maximum length is `200` characters. |
| environment\_role\[config\] | **object** _required_ | Defines the privileges assigned to the environment role. |
| environment\_role\[inheritable\] | **boolean** _optional_ | Child workspaces inherit the role when set to `true`. The default value is `false`. This value can only be set to `true` in Admin AHQ or Embedded partner workspaces. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/environment_roles/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "environment_role": {
          "name": ":name",
          "config": :config,
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

## Delete an environment role

Deletes an [environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) by its ID.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/environment_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the environment role to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/environment_roles/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The API deletes the environment role and returns an empty response body.

400 BAD REQUEST

A `400 Bad Request` error indicates that the server couldn't process the request due to client-side issues. Common causes include malformed requests, invalid fields, or violations of field constraints, such as unsupported data types.

In the following example, the request fails because the role is still assigned to some collaborators:

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
