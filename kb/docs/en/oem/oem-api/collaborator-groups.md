---
url: 'https://docs.workato.com/en/oem/oem-api/collaborator-groups.md'
description: >-
  Reference for Workato Embedded API endpoints to create, list, update, and
  delete collaborator groups and members in a customer workspace.
---

# Embedded API - Collaborator groups

Use the following endpoints to manage [collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace.

> **COLLABORATOR GROUP ENDPOINTS REQUIRE THE V2 PREFIX**
> 
> Collaborator group endpoints are available only under `/api/v2/`. The `/api/managed_users/:managed_user_id/user_groups` path, without `/v2/`, is a different resource that returns [identity provider user groups](/en/oem/oem-api/mcp-servers#list-identity-provider-user-groups-in-a-customer-workspace) used by MCP servers. A `GET` request to that path returns `200 OK` instead of an error, so it can look successful while returning the wrong groups.

## Rate limits

The collaborator groups resource has the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List group project grants: [/api/v2/managed\_users/:managed\_user\_id/ user\_groups/:id/project\_grants](/en/oem/oem-api/collaborator-groups.html#list-collaborator-grants) | 60 requests per minute |
| All | All other [Collaborator groups](/en/oem/oem-api/collaborator-groups.html) endpoints | 10 requests per second |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups](#list-groups) | List customer workspace collaborator groups. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id](#get-group) | Get customer workspace collaborator group details. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/user\_groups](#create-group) | Create a customer workspace collaborator group. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id](#update-group) | Update a customer workspace collaborator group. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id](#delete-group) | Delete a customer workspace collaborator group. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/members](#list-members) | List collaborator group members in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/members](#add-members) | Add members to a customer workspace collaborator group. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/members](#remove-members) | Remove members from a customer workspace collaborator group. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/project\_grants](#list-collaborator-grants) | List a customer workspace collaborator group's project grants. |

## List customer workspace collaborator groups

Retrieves a list of [collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) from an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filter collaborator groups by their name. |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups?page[number]=:page_number_value&page[size]=:page_size_value' \
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

## Get customer workspace collaborator group details

Retrieves a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) from an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id
```

</api-code>

> **ALL COLLABORATORS**
> 
> The `All collaborators` group defines the default access granted to all collaborators. Each data center assigns a unique ID to `All collaborators`. Use the [List customer workspace collaborator groups](#list-groups) endpoint to retrieve the `All collaborators` group ID.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the collaborator group to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id' \
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

## Create a customer workspace collaborator group

Creates a new [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| user\_group | **object** _required_ | Defines the collaborator group to create. |
| user\_group\[name\] | **string** _required_ | The collaborator group name. The maximum length is `200` characters. |
| user\_group\[description\] | **string** _optional_ | The collaborator group description. The maximum length is `300` characters. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups' \
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

## Update a customer workspace collaborator group

Updates a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
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
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id' \
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

## Delete a customer workspace collaborator group

Deletes a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace. When you delete a collaborator group, members lose project access unless they have additional access from another source.

> **ALL COLLABORATORS**
> 
> The `All collaborators` group defines the default access granted to all collaborators. You can't delete this group.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the collaborator group to delete. |

### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The collaborator group is deleted, and the response body is empty.

## List collaborator group members in a customer workspace

Retrieves members of a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
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
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/members?page[number]=:page_number_value&page[size]=:page_size_value' \
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

## Add members to a customer workspace collaborator group

Adds collaborators to an existing [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the collaborator group to add members to. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| user\_ids | **array of integers** _required_ | The user IDs of members to add to the group. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/members' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "user_ids": [:user_id_1, :user_id_2]
      }'
```

</api-code>

### Response

A successful request returns `{ "data": null }`. This response indicates the operation succeeded, but no additional data is returned.

## Remove members from a customer workspace collaborator group

Removes collaborators from a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the collaborator group to remove members from. |

### Query parameters

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
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/members?user_ids[]=:user_id_1&user_ids[]=:user_id_2&member_invitation_ids[]=:member_invitation_id_1&member_invitation_ids[]=:member_invitation_id_2' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The API removes the member from the collaborator group and returns no content in the response body.

## List a collaborator group's project grants

Retrieves project grants assigned to a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) in an Embedded customer workspace.

> **PROJECT GRANTS**
> 
> A project grant assigns a [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) to a collaborator or group. Refer to [Project grants](/en/oem/oem-api/project-grants) to manage project grants using the Embedded API or [Manage project access and roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#manage-project-access-and-roles) to manage project grants in the UI.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/project_grants
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| id | **string** _required_ | The ID of the collaborator group whose project grants to retrieve. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/user_groups/:id/project_grants?page[number]=:page_number_value&page[size]=:page_size_value' \
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
