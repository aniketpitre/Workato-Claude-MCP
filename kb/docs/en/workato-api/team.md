---
url: 'https://docs.workato.com/en/workato-api/team.md'
description: >-
  Reference for the Workato workspace collaborators API to invite, list, update,
  and delete collaborators and manage their roles.
---

# Developer API - Workspace collaborators

Use the following endpoints to manage collaborators in your [workspace](/en/user-accounts-and-teams/team-collaboration).

> **API CLIENT ACCESS**
> 
> API clients require access to the `DEV` environment to manage collaborators. Refer to [Create a client role](/en/workato-api/api-clients#create-an-api-client) to configure an API client's access.

## Rate limits

Workspace collaborator resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Invite a collaborator: [/api/member\_invitations](/en/workato-api/team.html#invite-collaborator) | 60 requests per minute Additionally, you can send one request per user and workspace ID every 20 minutes to this endpoint. |
| All | All other Workspace collaborators endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/member\_invitations](#invite-collaborator) | Invite a collaborator to a workspace. |
| GET | [/api/members](#list-collaborators) | Get list of collaborators. |
| GET | [/api/members/:id](#get-collaborator) | Get collaborator details. |
| PUT | [/api/members/:id](#update-collaborator) | Update collaborator roles. |
| DELETE | [/api/members/:id](#delete-collaborator) | Delete a collaborator. |
| GET | [/api/members/:id/project\_grants](#list-project-grants) | List a collaborator's project grants. |
| GET | [/api/members/:id/privileges](#get-privileges) | Get collaborator privileges. |
| GET | [/api/members/:id/projects\_privileges](#get-project-privileges) | Get collaborator project privileges. |

## Invite a collaborator

Invite a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) to your workspace. The API sends an email invitation if the email you provide doesn't belong to an existing user. Collaborators can join the workspace after they create a Workato account. You can invite a specific email and workspace combination once every twenty minutes.

> **RBAC 2.0 MIGRATION**
> 
> This endpoint's payload and response change after your workspace migrates to the new role-based access control model. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for details.

<api-code no-copy-method>

```bash
POST https://YOUR_DATA_CENTER/api/member_invitations
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the collaborator. |
| email | **string** _required_ | The email of the collaborator. |
| env\_roles | **object** _required_ | Defines the collaborator's environment roles. |
| env\_roles\[environment\_type\] | **string** _required_ | The type of environment in the workspace where you plan to invite the collaborator. Use `dev` for single-environment workspaces. |
| env\_roles\[name\] | **string** _required_ | The role to assign the collaborator for the specific environment. |
| env\_roles\[role\_type\] | **string** _optional_ | The type of role to assign the collaborator. Accepted values include `privilege_group` and `environment`. The default value is `privilege_group`. |
| role\_name | **string** _deprecated_ | **This field is deprecated**. Use `env_roles` instead, even for single-environment workspaces. |
| user\_group\_ids | **array of strings** _optional_ | The IDs of collaborator groups to assign. |

### Sample requests

- [Request 1: Invite a collaborator using `env_roles`](/en/workato-api/team#request-1-invite-a-collaborator-using-env-roles)
- [Request 2: Invite a collaborator using `env_roles`: No access](/en/workato-api/team#request-2-invite-a-collaborator-using-env-roles-no-access)
- [Request 3: Invite a collaborator with a nonexistent or unavailable role](/en/workato-api/team#request-3-invite-a-collaborator-with-a-nonexistent-or-unavailable-role)
- [Request 4: Invite a collaborator to a nonexistent environment](/en/workato-api/team#request-4-invite-a-collaborator-to-a-nonexistent-environment)

#### Request 1: Invite a collaborator using `env_roles`

This example request creates an invitation for the `dev`, `test`, and `prod` environments. It assigns the collaborator an `Admin` role in the `dev` environment, an `Analyst` role in the `test` environment, and an `Operator` role in the `prod` environment.

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/member_invitations' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": ":name",
        "email": ":email",
        "user_group_ids": [
          ":user_group_id_1",
          ":user_group_id_2"
        ],
        "env_roles": [
          {
            "environment_type": ":environment_type_1",
            "name": ":role_name_1",
            "role_type": ":role_type_1"
          },
          {
            "environment_type": ":environment_type_2",
            "name": ":role_name_2",
            "role_type": ":role_type_2"
          },
          {
            "environment_type": ":environment_type_3",
            "name": ":role_name_3",
            "role_type": ":role_type_3"
          }
        ]
      }'
```

</api-code>

Response 1: Invite a collaborator using env\_roles

```json
{
    "result": "ok"
}
```

#### Request 2: Invite a collaborator using `env_roles` - No access

This example creates an invitation solely for the `prod` environment. By omitting additional environments and roles from the `env_roles` object, the default behavior assigns the collaborator a `No access` role in all other environments.

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/member_invitations' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": ":name",
        "email": ":email",
        "user_group_ids": [
          ":user_group_id_1",
          ":user_group_id_2"
        ],
        "env_roles": [
          {
            "environment_type": ":environment_type",
            "name": ":role_name",
            "role_type": ":role_type"
          }
        ]
      }'
```

</api-code>

Response 2: Invite a collaborator using env\_roles - No access

```json
{
    "result": "ok"
}
```

#### Request 3: Invite a collaborator with a nonexistent or unavailable role

When you invite a collaborator using a role that doesn't exist or isn't available, this endpoint returns a `400` error: `Role Not existing role not found`.

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/member_invitations' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": ":name",
        "email": ":email",
        "user_group_ids": [
          ":user_group_id_1",
          ":user_group_id_2"
        ],
        "env_roles": [
          {
            "environment_type": ":environment_type",
            "name": "Not existing role",
            "role_type": ":role_type"
          }
        ]
      }'
```

</api-code>

Response 3: Invite a collaborator with a nonexistent or unavailable role

```json
{
    "message": "Role Not existing role not found"
}
```

#### Request 4: Invite a collaborator to a nonexistent environment

When you invite a collaborator to an environment that doesn't exist, this endpoint returns a `400` error: `Environment Not existing environment not found`.

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/member_invitations' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": ":name",
        "email": ":email",
        "user_group_ids": [
          ":user_group_id_1",
          ":user_group_id_2"
        ],
        "env_roles": [
          {
            "environment_type": "Not existing environment",
            "name": ":role_name",
            "role_type": ":role_type"
          }
        ]
      }'
```

</api-code>

Response 4: Invite a collaborator to a nonexistent environment

```json
{
    "message": "Environment Not existing environment not found"
}
```

## Get list of collaborators

Retrieve a list of all [collaborators](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) in a workspace. The response includes two primary elements:

| Element | Description |
| --- | --- |
| `data` | An array of objects, each representing a collaborator. |
| `total` | The total number of collaborators returned. |

Each collaborator object in the `data` array includes the following information:

| Field | Description |
| --- | --- |
| `id` | The user's unique identifier. |
| `grant_type` | The user's grant type. This is `team` for workspace collaborators and `federation_manager` for workspace moderators. |
| `user_groups` | An array of user groups assigned to the user. |
| `roles` | An array of system or custom roles assigned to the user in different environments. |
| `last_activity_log` | The user's latest activity in a workspace. For AHQ-enabled workspaces, it only displays the most recent action in the DEV environment. Includes activities such as sign-ins, token generation, and more. Refer to the [activity audit log reference](/en/features/activity-audit-log-reference) for a full list of captured events. |
| `external_id` | The user's external ID. |
| `name` | The user's name. |
| `email` | The user's email for signing in to Workato. |
| `time_zone` | The user's timezone. |
| `created_at` | The datetime when the user was created in Workato. |

> **ENDPOINT ACCESS**
> 
> Your API client role must be assigned the **Get collaborators** `GET /api/members` privilege to use this endpoint.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/members
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| email | **string** _optional_ | Filters the list to collaborators whose email contains the provided value. Special characters must be URL-encoded. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/members?email=:email_value' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": 12345,
      "grant_type": "federation_manager",
      "user_groups": [
        {
          "id": "ug-WxEKCibh-dTXBtz",
          "name": "All collaborators",
          "system": true
        },
        {
          "id": "ug-WxEKCibh-dTXBtg",
          "name": "Developers",
          "system": false
        }
      ],
      "roles": [
        {
          "environment_type": "dev",
          "role_name": "Admin",
          "role_type": "privilege_group"
        },
        {
          "environment_type": "test",
          "role_name": "Admin",
          "role_type": "privilege_group"
        },
        {
          "environment_type": "prod",
          "role_name": "Admin",
          "role_type": "privilege_group"
        }
      ],
      "last_activity_log": {
        "id": 2807129,
        "event_type": "user_login",
        "created_at": "2024-03-07T16:38:18.414-08:00"
      },
      "external_id": null,
      "name": "Rosario",
      "email": "rosario@example.com",
      "time_zone": "Pacific Time (US & Canada)",
      "created_at": "2021-12-14T13:01:15.935-08:00"
    },
    {
      "id": 23456,
      "grant_type": "team",
      "user_groups": [
        {
          "id": "ug-WxEKCibh-dTXBtz",
          "name": "All collaborators",
          "system": true
        },
        {
          "id": "ug-WxEKCibh-dTXBtg",
          "name": "Developers",
          "system": false
        }
      ],
      "roles": [
        {
          "environment_type": "dev",
          "role_name": "IT_Developer",
          "role_type": "privilege_group"
        },
        {
          "environment_type": "test",
          "role_name": "No access",
          "role_type": "privilege_group"
        },
        {
          "environment_type": "prod",
          "role_name": "No access",
          "role_type": "privilege_group"
        }
      ],
      "last_activity_log": {
        "id": 2807129,
        "event_type": "user_login",
        "created_at": "2024-03-07T16:38:18.414-08:00"
      },
      "external_id": null,
      "name": "Noam",
      "email": "noam@example.com",
      "time_zone": "Pacific Time (US & Canada)",
      "created_at": "2021-1-12T13:01:15.935-08:00"
    }
  ],
  "total": 2
}
```

## Get collaborator details

Get details about a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) you specify. This resource returns the following information in the response:

- User ID
- Grant type: Where `team` indicates the user is a workspace collaborator and `federation_manager` indicates the user is a workspace moderator.
- User groups
- Role
- External ID
- Name
- Email
- Timezone
- Last activity log: This displays the user's most recent action within a workspace and captures the same data as the activity audit log. For workspaces with AHQ, this only displays the last activity within the DEV environment. It can include events such as logging in, logging out, joining a workspace, generating a token, disconnecting a connection, and more. Refer to our [activity audit log reference](/en/features/activity-audit-log-reference) documentation for a complete list of activities that are captured in the log and can be returned in this request.
- Created at

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/members/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/members/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 34567,
    "grant_type": "team",
    "user_groups": [
      {
        "id": "ug-WxEKCibh-dTXBtz",
        "name": "All collaborators",
        "system": true
      },
      {
        "id": "ug-WxEKCibh-dTXBtg",
        "name": "Developers",
        "system": false
      }
    ],
    "roles": [
      {
        "environment_type": "dev",
        "role_name": "HR_Developer",
        "role_type": "privilege_group"
      },
      {
        "environment_type": "test",
        "role_name": "HR_Viewer",
        "role_type": "privilege_group"
      },
      {
        "environment_type": "prod",
        "role_name": "Operator",
        "role_type": "privilege_group"
      }
    ],
    "last_activity_log": {
      "id": 2807147,
      "event_type": "user_login",
      "created_at": "2024-03-07T16:44:39.318-08:00"
    },
    "external_id": null,
    "name": "Dana",
    "email": "dana@example.com",
    "time_zone": "Pacific Time (US & Canada)",
    "created_at": "2019-09-09T00:45:17.019-07:00"
  }
}
```

## Update collaborator roles

Updates an existing collaborator's [roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles) by their ID. To remove a collaborator's access, include `NoAccess` in the request body.

> **RBAC 2.0 MIGRATION**
> 
> This endpoint's payload and response change after your workspace migrates to the new role-based access control model. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for details.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/members/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator whose roles you plan to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| env\_roles | **object** _required_ | Defines the collaborator's updated environment roles. |
| env\_roles\[environment\_type\] | **string** _required_ | The type of workspace environment where you plan to update the collaborator's roles. Use `dev` for single-environment workspaces. |
| env\_roles\[name\] | **string** _required_ | The role to assign the collaborator for the specific environment. |
| env\_roles\[role\_type\] | **string** _optional_ | The type of role to assign the collaborator. Accepted values include `privilege_group` and `environment`. The default value is `privilege_group`. |

### Sample requests

- [Request 1: Update collaborator roles in one environment](/en/workato-api/team#request-1-update-collaborator-roles-in-one-environment)
- [Request 2: Update collaborator roles in all environments](/en/workato-api/team#request-2-update-collaborator-roles-in-all-environments)
- [Request 3: Update collaborator roles using a nonexistent or unavailable role](/en/workato-api/team#request-3-update-collaborator-roles-using-a-nonexistent-or-unavailable-role)
- [Request 4: Update collaborator roles in a nonexistent environment](/en/workato-api/team#request-4-update-collaborator-roles-in-a-nonexistent-environment)

#### Request 1: Update collaborator roles in one environment

This example request updates the collaborator's role to **Operator** in the `prod` environment. Roles in other environments are not affected.

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/members/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "env_roles": [
          {
            "environment_type": ":environment_type",
            "name": ":role_name",
            "role_type": ":role_type"
          }
        ]
      }'
```

</api-code>

Response 1: Update collaborator roles in one environment

```json
{
    "data": {
        "result": "ok"
    }
}
```

#### Request 2: Update collaborator roles in all environments

This example request updates the collaborator's role to **Operator** in the `prod` environment, **Admin** in the `dev` environment, and removes the collaborator's access to the `test` environment.

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/members/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "env_roles": [
          {
            "environment_type": ":environment_type_1",
            "name": ":role_name_1",
            "role_type": ":role_type_1"
          },
          {
            "environment_type": ":environment_type_2",
            "name": ":role_name_2",
            "role_type": ":role_type_2"
          },
          {
            "environment_type": ":environment_type_3",
            "name": ":role_name_3",
            "role_type": ":role_type_3"
          }
        ]
      }'
```

</api-code>

Response 2: Update collaborator roles in all environments

```json
{
    "data": {
        "result": "ok"
    }
}
```

#### Request 3: Update collaborator roles using a nonexistent or unavailable role

When you update a collaborator's role to one that doesn't exist or isn't available, this endpoint returns a `400` error: `Role Custom Role not found`.

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/members/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "env_roles": [
          {
            "environment_type": ":environment_type",
            "name": ":name",
            "role_type": ":role_type"
          }
        ]
      }'
```

</api-code>

Response 3: Update collaborator roles using a nonexistent or unavailable role

```json
{
    "errors": [
        {
            "code": 400,
            "title": "Role Custom Role not found"
        }
    ]
}
```

#### Request 4: Update collaborator roles in a nonexistent environment

When you update a collaborator's role in an environment that doesn't exist, this endpoint returns a `400` error: `Environment Custom Environment not found`.

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/members/:id' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "env_roles": [
          {
            "environment_type": ":environment_type",
            "name": ":role_name",
            "role_type": ":role_type"
          }
        ]
      }'
```

</api-code>

Response 4: Update collaborator roles in a nonexistent environment

```json
{
    "errors": [
        {
            "code": 400,
            "title": "Environment Custom Environment not found"
        }
    ]
}
```

## Delete a collaborator

Deletes a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) by their ID.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/members/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/members/:id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

A successful request returns a `204 No Content` status code. The collaborator is deleted, and the response body is empty.

## List a collaborator's project grants

Retrieves all project grants for a workspace. This doesn't include project access granted through [collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups).

> **PROJECT GRANTS**
> 
> A project grant assigns a [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) to a collaborator or group. Refer to [Project grants](/en/workato-api/project-grants) to manage project grants using the developer API or [Manage project access and roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#manage-project-access-and-roles) to manage project roles in the UI.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/members/:id/project_grants
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator to retrieve project grants from. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/members/:id/project_grants?page[number]=:page_number_value&page[size]=:page_size_value' \
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
        "id": 178230,
        "name": "Development",
        "environment": {
          "id": 148425,
          "type": "dev"
        },
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
        "name": "Sales",
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

## Get collaborator privileges

Retrieves the privileges and [roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles) of a collaborator by their ID. The response returns an array of roles for each [environment](/en/features/environments) (for example, `dev`, `test`, and `prod`) with the following information:

- Environment type
- User role
- All permissions assigned to the role
- Role type

The response includes roles from both the legacy model (`role_type: privilege_group`) and the new model (`role_type: environment`).

> **ENVIRONMENT PRIVILEGES ONLY**
> 
> This endpoint only returns environment-level privileges. Use it together with [Get collaborator project privileges](#get-project-privileges) to retrieve the collaborator's project-level access.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/members/:id/privileges
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator whose privileges you plan to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/members/:id/privileges' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "environment_type": "dev",
            "name": "Operator",
            "role_type": "privilege_group",
            "privileges": {
                "Recipes": [
                    "read",
                    "run",
                    "read_run_history"
                ],
                "Folders": [
                    "read"
                ],
                "Projects": [
                    "read"
                ],
                "Use in recipes": [
                    "all"
                ],
                "Test automation": [
                    "read"
                ]
            }
        },
        {
            "environment_type": "test",
            "name": "Operator",
            "role_type": "privilege_group",
            "privileges": {
                "Recipes": [
                    "read",
                    "run",
                    "read_run_history"
                ],
                "Folders": [
                    "read"
                ],
                "Projects": [
                    "read"
                ],
                "Use in recipes": [
                    "all"
                ],
                "Test automation": [
                    "read"
                ]
            }
        },
        {
            "environment_type": "prod",
            "name": "Operator",
            "role_type": "privilege_group",
            "privileges": {
                "Recipes": [
                    "read",
                    "run",
                    "read_run_history"
                ],
                "Folders": [
                    "read"
                ],
                "Projects": [
                    "read"
                ],
                "Use in recipes": [
                    "all"
                ],
                "Test automation": [
                    "read"
                ]
            }
        }
    ]
}
```

## Get collaborator project privileges

Retrieves project-level access for a collaborator. This includes access assigned directly or through membership in a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups). You can use this endpoint to audit project permissions.

> **PROJECT PRIVILEGES ONLY**
> 
> This endpoint only returns project-level privileges. Use it together with [Get collaborator privileges](#get-privileges) to retrieve the collaborator's environment-level roles and privileges.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/members/:id/projects_privileges
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the collaborator whose project privileges you plan to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/members/:id/projects_privileges' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "environment": {
        "id": 123456,
        "type": "dev"
      },
      "projects": {
        "61722": {
          "Folders": ["create", "view"]
        }
      }
    },
    {
      "environment": {
        "id": 789123,
        "type": "prod"
      },
      "projects": {
        "74137": {
          "Folders": ["view"]
        }
      }
    }
  ]
}
```

---
