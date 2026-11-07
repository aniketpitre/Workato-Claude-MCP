---
url: 'https://docs.workato.com/en/workato-api/collaborator-groups.md'
description: >-
  Reference for the Workato developer API endpoints to list, create, update,
  delete collaborator groups and manage their members and project grants.
---

# Developer API - Collaborator groups

Use the following endpoints to manage your [collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups).

## Rate limits

The collaborator groups resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Collaborator groups](/en/workato-api/collaborator-groups.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/user\_groups](#list-groups) | List collaborator groups. |
| GET | [/api/user\_groups/:id](#get-group) | Get collaborator group details. |
| POST | [/api/user\_groups](#create-group) | Create a collaborator group. |
| PUT | [/api/user\_groups/:id](#update-group) | Update a collaborator group. |
| DELETE | [/api/user\_groups/:id](#delete-group) | Delete a collaborator group. |
| GET | [/api/user\_groups/:id/members](#list-members) | List collaborator group members. |
| POST | [/api/user\_groups/:id/members](#add-members) | Add members to a collaborator group. |
| DELETE | [/api/user\_groups/:id/members](#remove-members) | Remove members from a collaborator group. |
| GET | [/api/user\_groups/:id/project\_grants](#list-collaborator-grants) | List a collaborator group's project grants. |

## List collaborator groups

Retrieves a list of [collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) from a workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/user_groups
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filter collaborator groups by their name. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/user_groups?page[number]=:page_number_value&page[size]=:page_size_value' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": "ug-WxEKCibh-dTXBtz",
      "name" : "All collaborators",
      "description": null,
      "members_count": 5,
      "system": true,
      "created_at": "2024-08-01T13:35:11.691-07:00",
      "updated_at": "2024-08-01T13:35:11.691-07:00"
    },
    {
      "id": "ug-APHDLgAD-cTXBtz",
      "name" : "Developers",
      "description": "Group for developers",
      "members_count": 2,
      "system": false,
      "created_at": "2024-08-02T13:35:11.691-07:00",
      "updated_at": "2024-08-02T13:35:11.691-07:00"
    }
  ],
  "total": 2,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

## Get collaborator group details

Retrieves a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/user_groups/:id
```

</api-code>

> **ALL COLLABORATORS**
> 
> The `All collaborators` group defines the default access granted to all collaborators. Each data center assigns a unique ID to `All collaborators`. Use the [List collaborator groups](#list-groups) endpoint to retrieve the `All collaborators` group ID.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator group to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/user_groups/:user_group_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": {
    "id": "ug-WxEKCibh-dTXBtz",
    "name" : "Developers",
    "description": "Group for developers",
    "members_count": 2,
    "system": false,
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

## Create a collaborator group

Creates a new [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/user_groups
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| user\_group | **object** _required_ | Defines the collaborator group to create. |
| user\_group\[name\] | **string** _required_ | The collaborator group name. The maximum length is `200` characters. |
| user\_group\[description\] | **string** _optional_ | The collaborator group description. The maximum length is `300` characters. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/user_groups' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "user_group": {
          "name": ":name",
          "description": ":description"
        }
      }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": "ug-WxEKCibh-dTXBtz",
    "name" : "Developers",
    "description": "Group for developers",
    "members_count": 1,
    "system": false,
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

400 BAD REQUEST

A `400 Bad Request` error indicates that the server couldn't process the request due to client-side issues. Common causes include malformed requests, invalid fields, or violations of field constraints, such as unsupported data types.

In the following example, the request fails because the required `name` parameter is blank:

```json
{
  "errors": [
    {
      "code": "bad_request",
      "title": "Name can't be blank"
    }
  ]
}
```

## Update a collaborator group

Updates a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) by its ID.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/user_groups/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator group to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| user\_group | **object** _required_ | Defines the updated collaborator group. |
| user\_group\[name\] | **string** _required_ | The updated name of the collaborator group. The maximum length is `200` characters. |
| user\_group\[description\] | **string** _optional_ | The updated description of the collaborator group. The maximum length is `300` characters. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/user_groups/:user_group_id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "user_group": {
          "name": ":name",
          "description": ":description"
        }
      }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": "ug-WxEKCibh-dTXBtz",
    "name" : "Developers Team",
    "description": "Team",
    "members_count": 2,
    "system": false,
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T13:35:11.691-07:00"
  }
}
```

400 BAD REQUEST

A `400 Bad Request` error indicates that the server couldn't process the request due to client-side issues. Common causes include malformed requests, invalid fields, or violations of field constraints, such as unsupported data types.

In the following example, the request fails because the required `name` parameter is blank:

```json
{
  "errors": [
    {
      "code": "bad_request",
      "title": "Name can't be blank"
    }
  ]
}
```

## Delete a collaborator group

Deletes a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) by its ID. When you delete a collaborator group, members lose project access unless they have additional access from another source.

> **ALL COLLABORATORS**
> 
> The `All collaborators` group defines the default access granted to all collaborators. You can't delete this group.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/user_groups/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator group to delete. |

### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/user_groups/:user_group_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The collaborator group is deleted, and the response body is empty.

## List collaborator group members

Retrieves members of a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/user_groups/:id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator group to retrieve members from. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| text | **string** _optional_ | Filter members by their name or email. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/user_groups/:user_group_id/members?page[number]=:page_number_value&page[size]=:page_size_value' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "user_id": 1,
      "member_invitation_id": null,
      "name" : "Dani",
      "email": "dani@workato.com",
      "type": "User",
      "avatar_url": "url"
    },
    {
      "user_id": null,
      "member_invitation_id": 1,
      "name" : "Alex",
      "email": "alex@workato.com",
      "type": "MemberInvitation",
      "avatar_url": null
    }
  ],
  "total": 2,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

## Add members to a collaborator group

Adds collaborators to an existing [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) by their IDs.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/user_groups/:id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator group to add members to. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| user\_ids | **array of integers** _required_ | The user IDs of members to add to the group. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/user_groups/:user_group_id/members' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "user_ids": [:user_id_1, :user_id_2]
      }'
```

</api-code>

### Response

A successful request returns `{ "data": null }`. This response indicates the operation succeeded, but no additional data is returned.

## Remove members from a collaborator group

Removes collaborators from a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) by their IDs.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/user_groups/:id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator group to retrieve members from. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| user\_ids | **array of integers** _conditionally required_ | The user IDs of members to remove from the group. |
| member\_invitation\_ids | **array of integers** _conditionally required_ | A list of IDs for collaborator group invitations. Members who were added by the invitations are removed from the group. |

> **CONDITIONAL REQUIREMENTS**
> 
> Requests must include either `user_ids` or `member_invitation_ids` to specify which collaborators to remove from the group. You may include both to remove collaborators based on multiple criteria.

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/user_groups/:user_group_id/members?user_ids[]=:user_id_1&user_ids[]=:user_id_2&member_invitation_ids[]=:member_invitation_id_1&member_invitation_ids[]=:member_invitation_id_2' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The API removes the member from the collaborator group and returns no content in the response body.

## List a collaborator group's project grants

Retrieves [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) assigned to a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups).

> **PROJECT GRANTS**
> 
> A project grant assigns a [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) to a collaborator or group. Refer to [Project grants](/en/workato-api/project-grants) to manage project grants using the developer API or [Manage project access and roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#manage-project-access-and-roles) to manage project roles in the UI.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/user_groups/:id/project_grants
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator group whose project grants to retrieve. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/user_groups/:user_group_id/project_grants?page[number]=:page_number_value&page[size]=:page_size_value' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": "prjgr-AQAEnmMX-b4rPeT-CD",
      "project": {
        "id": 178229,
        "name": "Development",
        "environment": {
          "id": 148425,
          "type": "dev"
        }
      },
      "project_role": {
        "id": "prjrl-AQAEnmK3-EQpeYM",
        "name": "Developers"
      }
    },
    {
      "id": "prjgr-AQAEnmKE-xpCFwT-CD",
      "project": {
        "id": 178230,
        "name": "Development",
        "environment": {
          "id": 148426,
          "type": "prod"
        },
      },
      "project_role": {
        "id": "prjrl-AQAEnmK3-EQpeYM",
        "name": "Developers"
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

---
