---
url: 'https://docs.workato.com/en/workato-api/project-grants.md'
description: >-
  Reference for the Workato project grants API to get, list, add, update, and
  delete project role assignments for collaborators and groups.
---

# Developer API - Project grants

Use the following endpoints to manage a collaborator or group's [project grants](#what-are-project-grants).

> **API CLIENT ACCESS**
> 
> Project grant endpoints can only assign project roles to environments and projects that the API client can access. For example, an API client assigned to the `TEST` environment can only manage `TEST` projects. Additionally, if an API client is assigned to specific projects, it can only manage those projects. Refer to [Create a client role](/en/workato-api/api-clients#create-an-api-client) to configure an API client's access.

## Rate limits

The project grants resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All[](/en/workato-api/project-grants.html) | All [Project grants](/en/workato-api/project-grants.html) endpoints | 60 requests per minute |

## What are project grants?

A project grant assigns a [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) to a collaborator or group. Refer to [Manage project access and roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#manage-project-access-and-roles) to manage assigned project roles in the UI.

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/project\_grants/:id](#get-grant) | Get a project grant. |
| PUT | [/api/project\_grants/:id](#update-grant) | Update a project grant. |
| DELETE | [/api/project\_grants/:id](#delete-grant) | Delete a project grant. |
| GET | [/api/projects/:id/project\_grants](#list-grants) | List project grants by project ID. |
| PUT | [/api/projects/:id/project\_grants](#add-grants-to-project) | Add or update project grants. |

## Get a project grant

Retrieves a project grant by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/project_grants/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project grant to retrieve. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/project_grants/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data" : {
    "id": "prjgr-AQAEnmKC-Dtt9aD-CD",
    "project": {
      "id": 178229,
      "name": "Development",
      "environment": {
        "id": 148425,
        "type": "dev"
      }
    },
    "project_role": {
      "id": "prjrl-AQBGCnMB-JoFtKL",
      "name": "Developers"
    },
    "user_group": null,
    "user": {
      "id": 1,
      "name" : "Taylor",
      "email": "taylor@workato.com"
    }
  }
}
```

## Update a project grant

Updates an existing project grant by its ID.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/project_grants/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project grant to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| project\_grant | **object** _required_ | Defines the updated project grant. |
| project\_grant\[project\_role\_id\] | **string** _required_ | The ID of the project role to assign. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/project_grants/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "project_grant": {
          "project_role_id": ":project_role_id"
        }
      }'
```

</api-code>

### Response

```json
{
  "data" : {
    "id": "prjgr-AQAEnmKC-Dtt9aD-CD",
    "project": {
      "id": 178229,
      "name": "Development",
      "environment": {
        "id": 148425,
        "type": "dev"
      }
    },
    "project_role": {
      "id": "prjrl-AQBGCnMB-JoFtKL",
      "name": "Developers"
    },
    "user_group": {
      "id": "ug-WxEKCibh-dTXBtz",
      "name" : "Developers",
      "system": false
    },
    "user": null
  }
}
```

400 BAD REQUEST

A `400 Bad Request` error indicates that the server couldn't process the request due to client-side issues. Common causes include malformed requests, invalid fields, or violations of field constraints, such as unsupported data types.

In the following example, the request fails because the assignment is already taken:

```json
{
  "errors": [
    {
      "code": "bad_request",
      "title": "Assignment has already been taken"
    }
  ]
}
```

## Delete a project grant

Deletes a project grant by its ID.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/project_grants/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project grant to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/project_grants/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The API deletes the project grant and returns an empty response body.

## List project grants

Retrieves a list of grants from a project by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/projects/:id/project_grants
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project to retrieve grants from. This is distinct from the project's `folder_id`. Retrieve a list of projects and their IDs by calling the [List projects](/en/workato-api/folders#list-projects) endpoint. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/projects/:id/project_grants?page[number]=:page_number_value&page[size]=:page_size_value' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": "prjgr-AQAEnmMX-b4rPeT-CD",
      "project_role": {
        "id": "prjrl-AQAEnmK3-EQpeYM",
        "name": "Developers"
      },
      "user": {
        "id": 1,
        "name" : "Jie",
        "email": "jie@workato.com"
      },
      "user_group": null
    },
    {
      "id": "prjgr-AQAEnmKC-Dtt9aD-CD",
      "project_role": {
        "id": "prjrl-AQAEnmK3-EQpeYM",
        "name": "Developers"
      },
      "user": null,
      "user_group": {
        "id": "ug-WxEKCibh-dTXBtz",
        "name" : "Developers",
        "system": false
      }
    }
  ],
  "total": 2,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

## Add or update project grants

Adds or updates project grants for a project by its ID. You can include a maximum of 100 grants in each request.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/projects/:id/project_grants
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the project where you plan to add or update grants. This is distinct from the project's `folder_id`. Retrieve a list of projects and their IDs by calling the [List projects](/en/workato-api/folders#list-projects) endpoint. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| project\_grants | **object** _required_ | Defines project grants for the project. |
| project\_grants\[assignment\_type\] | **string** _required_ | Specifies whether to assign the role to a workspace (`User`) or collaborator group (`UserGroup`). |
| project\_grants\[assignment\_id\] | **string** _required_ | The ID of the target workspace or collaborator group. |
| project\_grants\[project\_role\_id\] | **string** _required_ | The ID of the role to assign. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/projects/:id/project_grants' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "project_grants": [
          {
            "assignment_type": ":assignment_type_1",
            "assignment_id": ":assignment_id_1",
            "project_role_id": ":project_role_id_1"
          },
          {
            "assignment_type": ":assignment_type_2",
            "assignment_id": ":assignment_id_2",
            "project_role_id": ":project_role_id_2"
          }
        ]
      }'
```

</api-code>

### Response

A successful request returns `{ "data": null }`. This response indicates the operation succeeded, but no additional data is returned.

400 BAD REQUEST

A `400 Bad Request` error indicates that the server couldn't process the request due to client-side issues. Common causes include malformed requests, invalid fields, or violations of field constraints, such as unsupported data types.

In the following example, the request fails because it exceeds the maximum number of grants per request:

```json
{
  "errors": [
    {
      "code": "bad_request",
      "title": "Max 100 project grants per request"
    }
  ]
}
```

---
