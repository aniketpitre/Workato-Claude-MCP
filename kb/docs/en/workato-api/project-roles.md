---
url: 'https://docs.workato.com/en/workato-api/project-roles.md'
description: >-
  Reference for the Workato project roles API to list, get, create, update, and
  delete project roles in a workspace.
---

# Developer API - Project roles

Use the following endpoints to manage your [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles).

Project roles can have the following values:

| Value | Definition |
| --- | --- |
| system | Default roles provided by Workato. |
| custom | Roles created manually within a workspace. |
| inheritable | Custom roles from an AHQ admin or Embedded partner workspace that are inheritable by child workspaces. |
| inherited | Roles inherited by a child workspace from its AHQ or Embedded parent workspace. |

## Rate limits

Project roles resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All[](/en/workato-api/project-roles.html) | All [Project roles](/en/workato-api/project-roles.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/project\_roles](#list-project-roles) | List project roles. |
| GET | [/api/project\_roles/:id](#get-role) | Get project role details. |
| POST | [/api/project\_roles](#create-role) | Create a project role. |
| PUT | [/api/project\_roles/:id](#update-role) | Update a project role. |
| DELETE | [/api/project\_roles/:id](#delete-role) | Delete a project role. |

## List project roles

Retrieves a list of [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) from a workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/project_roles
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filter project roles by their name. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/project_roles?name=:name_value&page[number]=:page_number_value&page[size]=:page_size_value' \
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

## Get project role details

Retrieves a [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/project_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project role to retrieve. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/project_roles/:id' \
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

## Create a project role

Creates a new [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/project_roles
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| project\_role | **object** _required_ | Defines the project role to create. |
| project\_role\[name\] | **string** _required_ | The name of the project role to create. The maximum length is `200` characters. |
| project\_role\[config\] | **object** _required_ | Defines the privileges assigned to the role. |
| project\_role\[inheritable\] | **boolean** _optional_ | Child workspaces inherit the role when set to `true`. The default value is `false`. This value can only be set to `true` in Admin AHQ or Embedded partner workspaces. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/project_roles' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "project_role": {
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

## Update a project role

Updates an existing [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) by its ID.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/project_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project role to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| project\_role | **object** _required_ | Defines the updated project role. |
| project\_role\[name\] | **string** _required_ | The updated name of the project role. The maximum length is `200` characters. |
| project\_role\[config\] | **object** _required_ | Defines the privileges assigned to the role. |
| project\_role\[inheritable\] | **boolean** _optional_ | Child workspaces inherit the role when set to `true`. The default value is `false`. This value can only be set to `true` in Admin AHQ or Embedded partner workspaces. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/project_roles/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "project_role": {
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

## Delete a project role

Deletes a project role by its ID.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/project_roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project role to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/project_roles/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The API deletes the project role and returns an empty response body.

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
