---
url: 'https://docs.workato.com/en/workato-api/workato-identity-iam.md'
description: >-
  Reference for the Workato Identity IAM API endpoints to list, create, update,
  and delete users, user groups, and app links.
---

# Developer API - Workato Identity IAM

The [Workato Identity](/en/workato-identity) APIs allow you to programmatically manage user identities, group memberships, and access control.

Watch a quick video guide: Onboard genie users with Workato Identity IAM

[Video](https://www.youtube.com/embed/JJImOGbERWY?rel=0&si=n0RamCPy-ppowZ0F)

## Rate limits

Workato Identity IAM resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Workato Identity IAM](/en/workato-api/workato-identity-iam.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/iam/users](#list-users) | List users in the workspace. |
| GET | [/api/iam/users/:user-id](#get-user-by-id) | Retrieve details for a specific user by ID. |
| POST | [/api/iam/users](#create-user) | Create one or more new users. |
| PUT | [/api/iam/users/:user-id](#update-user) | Update an existing user. |
| DELETE | [/api/iam/users/:user-id](#delete-user) | Delete a user from the workspace. |
| POST | [/api/iam/users/:user-id/add\_to\_group](#add-user-to-group) | Add a user to a specific group. |
| POST | [/api/iam/users/:user-id/remove\_from\_group](#remove-user-from-group) | Remove a user from a specific group. |
| GET | [/api/iam/user\_groups](#list-user-groups) | List user groups in the current environment. |
| GET | [/api/iam/user\_groups/:user-group-id](#get-user-group-by-id) | Retrieve details for a specific user group by ID. |
| POST | [/api/iam/user\_groups](#create-user-group) | Create a new user group. |
| PUT | [/api/iam/user\_groups/:user-group-id](#update-user-group) | Update an existing user group. |
| DELETE | [/api/iam/user\_groups/:user-group-id](#delete-user-group) | Delete a user group. |
| POST | [/api/iam/user\_groups/:user-group-id/add\_users](#add-users-to-group) | Add multiple users to a group. |
| DELETE | [/api/iam/user\_groups/:user-group-id/remove\_users](#remove-users-from-group) | Remove multiple users from a group. |
| GET | [/api/iam/user\_groups/:user-group-id/members](#list-group-members) | List all members of a user group. |
| GET | [/api/iam/app\_links](#list-app-links) | List app links in the current environment. |
| POST | [/api/iam/app\_links](#create-app-link) | Create an app link. |
| DELETE | [/api/iam/app\_links/:id](#delete-app-link) | Delete an app link by ID. |
| DELETE | [/api/iam/app\_links](#delete-app-links) | Delete app links by IDs. |

## Users

The following endpoints enable you to manage Workato Identity users:

### List users

List all users in your workspace.

<api-code  no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/iam/users
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| query | **string** _optional_ | Search query to filter users. |
| emails\[\] | **array\[string\]** _optional_ | Filter by email addresses. |
| user\_ids\[\] | **array\[string\]** _optional_ | Filter by user IDs. |
| name | **string** _optional_ | Filter by user name. |
| user\_group\_ids\[\] | **array\[string\]** _optional_ | Filter by user group IDs. |
| environment\_id | **string** _optional_ | Filter group membership by environment ID. |
| order\_by | **string** _optional_ | Sort by `name`, `email`, or `status`. |
| order | **string** _optional_ | Sort direction: `asc` or `desc`. |
| page | **integer** _optional_ | Page number. Defaults to `1`. |
| per\_page | **integer** _optional_ | Page size. Max/default is `100`. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/iam/users?page=:page_value&per_page=:per_page_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

##### Response

```json
{
  "data": [
    {
      "id": "user-id",
      "email": "j.anderson@example.com",
      "name": "Jade Anderson",
      "status": "active",
      "last_signed_in_at": "2025-01-15T10:30:00Z",
      "created_at": "2025-01-01T00:00:00Z",
      "environment_ids": ["env-id"],
      "user_groups": [
        {
          "id": "user-group-id",
          "environment_id": "env-id",
          "name": "Developers"
        }
      ]
    }
  ],
  "total": 1,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

### Get user by ID

Retrieve details for a specific user by ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/iam/users/:user-id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-id | **string** _required_ | User ID. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/iam/users/:user-id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "user-id",
    "email": "j.anderson@example.com",
    "name": "Jade Anderson",
    "status": "active",
    "last_signed_in_at": "2025-01-15T10:30:00Z",
    "created_at": "2025-01-01T00:00:00Z",
    "environment_ids": ["env-id"],
    "user_groups": [
      {
        "id": "user-group-id",
        "environment_id": "env-id",
        "name": "Developers"
      }
    ]
  }
}
```

### Create user

Create one or more new users in your workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/iam/users
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| users\[\] | **array** _required_ | Array of user objects to create. |
| users\[\].email | **string** _optional_ | User email address. |
| users\[\].name | **string** _optional_ | User display name. |
| users\[\].user\_group\_ids\[\] | **array\[string\]** _optional_ | Group IDs. You must provide `environment_types[]` if you provide Group IDs. |
| users\[\].environment\_types\[\] | **array\[string\]** _optional_ | Environment types. For example: `dev`, `test`, or `prod`. |
| users\[\].send\_invitation | **boolean** _optional_ | Whether to send an email invitation to the user. Defaults to `true`. Must be `false` or omitted when `state` is `active`. |
| users\[\].state | **string** _optional_ | Initial state of the user. Either `active` or `invited`. Defaults to `invited`. |

##### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/iam/users \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "users": [
              {
                "email": ":email",
                "name": ":name",
                "user_group_ids": [":user_group_id"],
                "environment_types": [":environment_type"]
              }
            ]
          }'
```

</api-code>

##### Response

```json
{
  "data": [
    {
      "id": "l1fEi5N0ts0aMbLe91",
      "invitation_url": "https://www.workato.com/invitations/example-token"
    }
  ]
}
```

### Update user

Update an existing user's information, including name and group memberships.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/iam/users/:user-id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-id | **string** _required_ | User ID. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Updated user name. |
| user\_group\_ids\[\] | **array\[string\]** _optional_ | Updated list of group IDs. |
| environment\_types\[\] | **array\[string\]** _optional_ | Environment types (`dev`, `test`, `prod`). |
| environment\_user\_groups\[\] | **array\[object\]** _optional_ | Explicit environment group assignments with `id` and `environment_id`. |

##### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/iam/users/:user-id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "environment_types": [":environment_type_1", ":environment_type_2"],
            "environment_user_groups": [
              {"id": ":user_group_id", "environment_id": ":environment_id"}
            ]
          }'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "user-id",
    "email": "j.anderson@example.com",
    "name": "Developer CI/CD",
    "status": "active",
    "last_signed_in_at": "2025-01-15T10:30:00Z",
    "created_at": "2025-01-01T00:00:00Z",
    "environment_ids": ["env-id", "env-id-2"],
    "user_groups": [
      {
        "id": "user-group-id",
        "environment_id": "env-id",
        "name": "Developers"
      }
    ]
  }
}
```

### Delete user

Delete a user from your workspace.

> **PERMANENT ACTION**
> 
> This action permanently removes the user from your workspace. This action doesn't delete the user from the system.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/iam/users/:user-id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-id | **string** _required_ | User ID. |

##### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/iam/users/:user-id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
  "data": null
}
```

### Add user to group

Add a user to a specific user group.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/iam/users/:user-id/add_to_group
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-id | **string** _required_ | User ID. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_group\_id | **string** _required_ | User group ID. |
| environment\_id | **string** _optional_ | Environment ID. Defaults to the Development environment. |

##### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/iam/users/:user-id/add_to_group \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "user_group_id": ":user_group_id"
          }'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "user-id",
    "email": "j.anderson@acme.com",
    "name": "Jade Anderson",
    "status": "active",
    "last_signed_in_at": "2025-01-15T10:30:00Z",
    "created_at": "2025-01-01T00:00:00Z",
    "environment_ids": ["env-id"],
    "user_groups": [
      {
        "id": "user-group-id",
        "environment_id": "env-id",
        "name": "Developers"
      }
    ]
  }
}
```

### Remove user from group

Remove a user from a specific user group.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/iam/users/:user-id/remove_from_group
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-id | **string** _required_ | User ID. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_group\_id | **string** _required_ | User group ID. |
| environment\_id | **string** _optional_ | Environment ID. Defaults to the Development environment. |

##### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/iam/users/:user-id/remove_from_group \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "user_group_id": ":user_group_id"
          }'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "user-id",
    "email": "j.anderson@acme.com",
    "name": "Jade Anderson",
    "status": "active",
    "last_signed_in_at": "2025-01-15T10:30:00Z",
    "created_at": "2025-01-01T00:00:00Z",
    "environment_ids": ["env-id"],
    "user_groups": []
  }
}
```

## User Groups

The following endpoints enable you to manage Workato Identity groups:

### List user groups

List all user groups in the current environment.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/iam/user_groups
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| query | **string** _optional_ | Search query to filter user groups. |
| order\_by | **string** _optional_ | Field to order results by. Allowed: `name`. |
| order | **string** _optional_ | Sort direction: `asc` or `desc`. |
| page | **integer** _optional_ | Page number. Defaults to `1`. |
| per\_page | **integer** _optional_ | Page size. Max/default is `100`. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/iam/user_groups?page=:page_value&per_page=:per_page_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

##### Response

```json
{
  "data": [
    {
      "id": "user-group-id",
      "environment_id": "env-id",
      "name": "Developers",
      "users_count": 10,
      "created_at": "2025-01-01T00:00:00Z",
      "updated_at": "2025-01-10T00:00:00Z"
    }
  ],
  "total": 1,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

### Get user group by ID

Retrieve details of a specific user group by ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-group-id | **string** _required_ | User group ID. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "user-group-id",
    "environment_id": "env-id",
    "name": "Developers",
    "users_count": 10,
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-10T00:00:00Z"
  }
}
```

### Create user group

Create a new user group in your workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/iam/user_groups
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_group.name | **string** _required_ | Name of the user group. |

##### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/iam/user_groups \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "user_group": {
              "name": ":name"
            }
          }'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "user-group-id",
    "environment_id": "env-id",
    "name": "Sales Group",
    "users_count": 0,
    "created_at": "2025-01-20T00:00:00Z",
    "updated_at": "2025-01-20T00:00:00Z"
  }
}
```

### Update user group

Update an existing user group name.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-group-id | **string** _required_ | User group ID. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_group.name | **string** _required_ | Updated name for the user group. |

##### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "user_group": {
              "name": ":name"
            }
          }'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "user-group-id",
    "environment_id": "env-id",
    "name": "Sales training group",
    "users_count": 10,
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-20T00:00:00Z"
  }
}
```

### Delete user group

Delete a user group from your workspace.

> **GROUP DELETION DOESN'T DELETE USERS**
> 
> This action permanently removes the user group. Users assigned to the group aren't deleted, but are removed from this group.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-group-id | **string** _required_ | User group ID. |

##### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
  "data": null
}
```

### Add users to group

Add multiple users to a user group in a single operation.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id/add_users
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-group-id | **string** _required_ | User group ID. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_ids\[\] | **array\[string\]** _required_ | Array of user IDs to add to the group. |

##### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id/add_users \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "user_ids": [":user_id_1", ":user_id_2"]
          }'
```

</api-code>

##### Response

```json
{
  "data": null
}
```

### Remove users from group

Remove multiple users from a user group in a single operation.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id/remove_users
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-group-id | **string** _required_ | User group ID. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_ids\[\] | **array\[string\]** _required_ | Array of user IDs to remove from the group. |

##### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id/remove_users \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "user_ids": [":user_id_1", ":user_id_2"]
          }'
```

</api-code>

##### Response

```json
{
  "data": null
}
```

### List group members

List all members of a specific user group.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id/members
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| user-group-id | **string** _required_ | User group ID. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number. Defaults to `1`. |
| per\_page | **integer** _optional_ | Page size. Max/default is `100`. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/iam/user_groups/:user-group-id/members?page=:page_value&per_page=:per_page_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

##### Response

```json
{
  "data": [
    {
      "id": "user-id",
      "email": "j.anderson@acme.com",
      "name": "Jade Anderson",
      "status": "active",
      "last_signed_in_at": "2025-01-15T10:30:00Z",
      "created_at": "2025-01-01T00:00:00Z",
      "environment_ids": ["env-id"],
      "user_groups": [
        {
          "id": "user-group-id",
          "environment_id": "env-id",
          "name": "Developers"
        }
      ]
    }
  ],
  "total": 1,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

## App links

An app link maps a user's Workato Identity account to their corresponding account in a specific app, such as Slack, Microsoft Teams, or Workato GO. For example, it connects `jade@acme.com` in Workato Identity to `@jade` in Slack. You can create app links in Workato Identity without requiring users to sign in first. This allows you to send app events, notifications, or automations to your entire organization through a connected app immediately.

The following endpoints enable you to manage Workato Identity app links:

### List app links

List all app links in the current environment.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/iam/app_links
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| app\_type | **string** _optional_ | App type: `slack`, `teams`, or `matrix`. |
| app\_user\_id | **string** _optional_ | App user ID. |
| app\_user\_ids\[\] | **array\[string\]** _optional_ | App user IDs. |
| user\_id | **string** _optional_ | Workato user ID. |
| user\_ids\[\] | **array\[string\]** _optional_ | Workato user IDs. |
| state | **string** _optional_ | State: `initial` or `linked`. |
| order\_by | **string** _optional_ | Sort by `app_type`, `state`, `linked_at`, or `created_at`. |
| order | **string** _optional_ | Sort direction: `asc` or `desc`. |
| page | **integer** _optional_ | Page number. Defaults to `1`. |
| per\_page | **integer** _optional_ | Page size. Set to the default maximum of `100`. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/iam/app_links?page=:page_value&per_page=:per_page_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

##### Response

```json
{
  "data": [
    {
      "id": "7H9UjixTng97i7dTSXMYpo",
      "app_type": "slack",
      "app_user_id": "/slack/teams/T083UTJ97C1/users/U083G78PZV0",
      "user_id": "user-id",
      "state": "linked",
      "linked_at": "2025-01-15T10:30:00Z",
      "created_at": "2025-01-01T00:00:00Z",
      "updated_at": "2025-01-10T00:00:00Z",
      "auth_link": null
    },
    {
      "id": "4YYoEcATHdUVHceXUHymKY",
      "app_type": "teams",
      "app_user_id": "/teams/teams/1a30ead4-ab61-473e-8c8a-a83eb2948145/users/cb3bbf8f-579e-41c6-89ad-5927346f8944",
      "user_id": "user-id",
      "state": "linked",
      "linked_at": "2025-01-15T10:30:00Z",
      "created_at": "2025-01-01T00:00:00Z",
      "updated_at": "2025-01-10T00:00:00Z",
      "auth_link": null
    },
    {
      "id": "yDQe8Ua4PKQWT7hDMAPgi",
      "app_type": "matrix",
      "app_user_id": "marco@acme.com",
      "user_id": "user-id",
      "state": "linked",
      "linked_at": "2025-01-15T10:30:00Z",
      "created_at": "2025-01-01T00:00:00Z",
      "updated_at": "2025-01-10T00:00:00Z",
      "auth_link": null
    }
  ],
  "total": 3,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

### Create app link

Create a new app link in your workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/iam/app_links
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| app\_type | **string** _required_ | App type: `slack`, `teams`, or `matrix`. |
| app\_user\_id | **string** _required_ | User ID in the app. Format varies by app type: • Slack: `/slack/teams/{team_id}/users/{user_id}` • Teams: `/teams/teams/{team_uuid}/users/{user_uuid}` • Matrix (GO): User email address |
| user\_id | **string** _optional_ | Workato user ID. The link is created in `initial` state if omitted. |

##### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/iam/app_links \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "app_type": ":app_type",
            "app_user_id": ":app_user_id",
            "user_id": ":user_id"
          }'
```

</api-code>

##### Response

```json
{
  "data": {
    "id": "app-link-id",
    "app_type": "slack",
    "app_user_id": "/slack/teams/T083UTJ97C1/users/U083G78PZV0",
    "user_id": "user-id",
    "state": "linked",
    "linked_at": "2025-01-15T10:30:00Z",
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2025-01-10T00:00:00Z",
    "auth_link": "http://id.workato.com/portal/workspaces/<ID>/environments/<ENV ID>/sign-in?app_link_unique_id=<APP LINK ID>"
  }
}
```

### Delete app link

Delete an app link from your workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/iam/app_links/:id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | App link ID. |

##### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/iam/app_links/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
  "data": null
}
```

### Delete app links

Delete multiple app links from your workspace in a single operation.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/iam/app_links
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| ids\[\] | **array\[string\]** _optional_ | App link IDs to delete. |

##### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/iam/app_links' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "ids": [":app_link_id_1", ":app_link_id_2"]
          }'
```

</api-code>

##### Response

```json
{
  "data": null
}
```

---
