---
url: 'https://docs.workato.com/en/workato-api/roles.md'
description: >-
  Reference for the Workato legacy roles API to list, update, and copy custom
  roles in the legacy permissions model.
---

# Developer API - Legacy roles

Use the following endpoints to programmatically manage legacy roles.

> **LEGACY ROLES**
> 
> This page describes the legacy permissions model. Workato is replacing legacy roles with the new permissions model, which uses environment roles and project roles. You can migrate legacy roles using the [Role migration API](/en/workato-api/role-migration) or the [in-app migration wizard](/en/user-accounts-and-teams/role-based-access/migrate-roles). Refer to the [New permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2) documentation for more information.
> 
> After migration, these endpoints are deprecated. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for the exact behavior.

## Rate limits

The legacy roles resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Legacy roles](/en/workato-api/roles.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/roles](#list-custom-roles) | List custom roles. |
| PUT | [/api/roles/:role\_id](#update-custom-role) | Updates a custom role's project privileges. |
| POST | [/api/roles/:role\_id/copy](#copy-a-custom-role) | Makes a copy of a custom role. |

## List custom roles

Lists all custom roles.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/roles
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| per\_page | **integer** _optional_ | The number of custom roles to retrieve. |
| page | **integer** _optional_ | The page number. If the total number of custom roles exceed the page quota, subsequent records can be retrieved by calling the next page. |

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/roles \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
[
    {
        "id": 478,
        "name": "Developer role",
        "inheritable": false,
        "folder_ids": [],
        "created_at": "2020-05-20T11:54:31.706-07:00",
        "updated_at": "2020-05-20T11:54:31.706-07:00",
        "privileges": {
            "Recipes": [ ... ],
            "Folders": [ ... ],
            ...
        }
    },
    {
        "id": 446,
        "name": "Non-developer role",
        "inheritable": false,
        "folder_ids": [],
        "created_at": "2020-04-12T08:40:11.240-07:00",
        "updated_at": "2020-04-12T08:40:11.240-07:00",
        "privileges": {
            "Recipes": [ ... ],
            "Folders": [ ... ],
            ...
        }
    }
]
```

## Update a custom role

Updates the projects accessible to a custom collaborator role. You can set the privilege to all projects or specific projects by their folder IDs. The folder IDs can be obtained with the [GET folders](/en/workato-api/folders) API endpoint.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/roles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The ID of the custom role. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| all\_folders | **string** _required_ | Either "true" or "false". Must be "false" if "folder\_ids" is specified. |
| folder\_ids | **array** | Array of project IDs. |

#### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/roles/:id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "all_folders": ":true_or_false",
            "folder_ids": [:folder_id_1, :folder_id_2]
          }'
```

</api-code>

### Response

```json
{
    "id": 45899,
    "name": "Marketing Recipe Operator",
    "inheritable": false,
    "folder_ids": [
        1232,
        1224
    ],
    "created_at": "2022-12-26T02:26:04.582-08:00",
    "updated_at": "2022-12-26T02:37:04.124-08:00",
    "privileges": {
        "Recipes": [
            "read",
            "create",
            "update",
            "run",
            "read_run_history"
        ]
    }
}
```

## Copy a custom role

Creates a copy of a custom collaborator role with the ability to change the folders accessible by the role. The folder IDs can be obtained with the [GET folders](/en/workato-api/folders) API endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/roles/:id/copy
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The ID of the custom role. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the custom role. |
| folder\_ids | **array** | Array of project IDs. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/roles/:id/copy \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name",
            "folder_ids": [":folder_id_1", ":folder_id_2"]
          }'
```

</api-code>

### Response

```json
{
    "id": 546,
    "name": "Finance team developer",
    "inheritable": false,
    "folder_ids": ["1232", "1224"],
    "created_at": "2020-08-14T07:23:19.599-07:00",
    "updated_at": "2020-08-14T07:23:19.599-07:00"
}
```

---
