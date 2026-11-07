---
url: 'https://docs.workato.com/en/oem/oem-api/roles.md'
description: >-
  Reference for Embedded API endpoints to list and copy legacy custom roles in
  customer workspaces. Legacy roles are being replaced.
---

# Embedded API - Legacy roles

Use the following endpoints to manage legacy roles in an Embedded customer workspace.

Refer to the Developer API [Legacy roles](/en/workato-api/roles) documentation to manage legacy roles in the admin team.

> **LEGACY ROLES**
> 
> This page describes legacy roles. Workato is replacing legacy roles with the new permissions model, which uses environment roles and project roles. You can migrate legacy roles using the [Role migration API](/en/oem/oem-api/role-migration) or the [in-app migration wizard](/en/user-accounts-and-teams/role-based-access/migrate-roles). Refer to the [New permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2) documentation for more information.
> 
> After migration, these endpoints are deprecated. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for the exact behavior.

## Rate limits

The roles resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Legacy roles](/en/oem/oem-api/roles.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/roles](#list-custom-roles) | List custom roles in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/roles/:role\_id/copy](#copy-a-custom-role) | Makes a copy of a custom role in a customer workspace. |

## List custom roles

Lists all custom roles in a customer workspace.

> **INHERITABLE ROLE LIMITATION**
> 
> This endpoint returns only the custom roles created directly within the specified customer workspace. It doesn't include inheritable roles created in the Embed admin workspace.

Use the [GET customer workspace member API](/en/oem/oem-api/managed-users#get-list-of-customer-account-members) to obtain a list of `role_name`s associated with a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/roles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **integer** _required_ | Managed customer ID. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| per\_page | **integer** _optional_ | The number of custom roles to retrieve. |
| page | **integer** _optional_ | The page number. If the total number of custom roles exceed the page quota, subsequent records can be retrieved by calling the next page. |
| role\_name | **string** _optional_ | The name of a custom role. Filter results by `role_name`. |

### Sample requests

- [Request 1: Get list of custom roles](#get-list-of-custom-roles)
- [Request 2: Filter results by role name](#filter-results-by-role-name)

#### Request 1: List custom roles

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/roles \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

Response 1: List custom roles

```json
[
    {
        "id": 1128,
        "name": "Workbot builder",
        "inheritable": false,
        "folder_ids": [],
        "created_at": "2022-08-31T23:37:04.777-07:00",
        "updated_at": "2022-08-31T23:37:04.777-07:00",
        "privileges": {
            "Recipes": [
                "read",
                "create"
            ],
            "Folders": [
                "read"
            ],
            "Workbot": [
                "read",
                "create",
                "update",
                "delete"
            ]
    },
    {
        "id": 546,
        "name": "Customer developer",
        "inheritable": false,
        "folder_ids": ["1232", "1224"],
        "created_at": "2020-08-14T07:23:19.599-07:00",
        "updated_at": "2020-08-14T07:23:19.599-07:00",
        "privileges": {
            "Recipes": [
                "read",
            ],
            "Folders": [
                "read"
            ],
            "Workbot": [
                "read",
                "create",
                "update"
            ]
        }
    }
]
```

#### Request 2: Filter results by role name

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/roles?role_name=:role_name \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

Response 2: Filter results by role name

```json
[
    {
        "id": 1128,
        "name": "dev",
        "inheritable": false,
        "folder_ids": [],
        "created_at": "2022-08-31T23:37:04.777-07:00",
        "updated_at": "2022-08-31T23:37:04.777-07:00",
        "privileges": {
            "Projects": [
                "read",
                "create",
                "update",
                "delete"
            ],
            "Folders": [
                "read",
                "create",
                "update",
                "delete"
            ],
            "Connections": [
                "read",
                "create",
                "update",
                "delete"
            ],
            "Recipes": [
                "read",
                "create",
                "update",
                "delete",
                "run",
                "read_run_history"
            ],
            "Connection Folders": [
                "all"
            ]
        }
    }
]
```

## Copy a custom role

Creates a copy of a custom role in a customer workspace with the ability to change the folders accessible by the role. The folder IDs can be obtained with the [GET folders](/en/oem/oem-api/folders) API endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/roles/:role_id/copy
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **integer** _required_ | Managed customer ID. |
| role\_id | **integer** _required_ | The ID of the role in the customer workspace. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the custom role. |
| folder\_ids | **array** | Array of folder IDs. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/roles/:role_id/copy \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "folder_ids": [":folder_id", ":folder_id"]
          }'
```

</api-code>

### Response

```json
{
    "id": 546,
    "name": "Customer developer",
    "inheritable": false,
    "folder_ids": ["1232", "1224"],
    "created_at": "2020-08-14T07:23:19.599-07:00",
    "updated_at": "2020-08-14T07:23:19.599-07:00"
}
```

---
