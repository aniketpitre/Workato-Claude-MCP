---
url: 'https://docs.workato.com/en/oem/oem-api/customer-managers.md'
description: >-
  Reference for the Embedded API customer managers resource to list, create,
  update, and delete customer managers in your account.
---

# Embedded API - Customer managers

Use the following endpoints to programmatically manage customer managers.

## Rate limits

Customer manager resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Customer managers](/en/oem/oem-api/customer-managers.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/customer\_managers](#list-customer-managers) | List all customer managers. |
| PUT | [/api/customer\_managers/:id](#update-customer-manager) | Update a customer manager. |
| POST | [/api/customer\_managers](#create-customer-manager) | Create a new customer manager. |
| DELETE | [/api/customer\_managers/:id](#delete-customer-manager) | Delete a customer manager. |

* * *

## List customer managers

Returns a list of all customer managers in an Embedded partner's account.

For customer managers with access to all workspaces in the Embedded partner's account, `moderated_workspaces` is an empty array (`[]`).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/customer_managers
```

</api-code>

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/customer_managers' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "items": [
            {
                "id": 1234,
                "user": {
                    "id": 4321,
                    "name": "ACME-HR",
                    "email": "alex@example.com.com",
                    "avatar_url": "https://example.com"
                },
                "privilege_group": {
                    "id": 247,
                    "name": "Customer Admin",
                    "system": false
                },
                "moderated_workspaces": [
                    {
                        "id": 27123,
                        "name": "Nutech"
                    },
                    {
                        "id": 29456,
                        "name": "ACME USA"
                    }
                ],
                "project_role": {
                    "id": "prjrl-AQRtExgY-cEGWTN",
                    "name": "Builder"
                }
            },
            {
                "id": 5678,
                "user": {
                    "id": 8765,
                    "name": "ACME Corp.",
                    "email": "ariel@example.com",
                    "avatar_url": "https://example.com"
                },
                "privilege_group": {
                    "id": 2,
                    "name": "Admin",
                    "system": true
                },
                "moderated_workspaces": [],
                "project_role": {
                    "id": "prjrl-AQRtExgY-cEGWTN",
                    "name": "Builder"
                }
            }
        ]
    }
}
```

* * *

## Update a customer manager

Update a customer manager's role in an Embedded partner's account.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/customer_managers/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the customer manager whose role you plan to update. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| role\_id | **string** _required_ | The legacy role to assign the customer manager. |
| project\_role\_id | **string** _optional_ | The project role to assign the customer manager. |
| permitted\_workspace\_ids | **array of integers** _optional_ | The list of workspace IDs where the customer manager should have the specified role, according to the `role_id` you provide. If omitted or set to an empty array (`[]`), this parameter grants the customer manager the specified role in _all_ workspaces in the Embedded partner's account. |

### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/customer_managers/:id' \
      -H 'Authorization: Bearer <api_token>'\
      -H 'Content-Type: application/json' \
      -d  '{
            "role_id": ":role_id",
            "permitted_workspace_ids": [:permitted_workspace_id_1, :permitted_workspace_id_2],
            "project_role_id": ":project_role_id"
           }'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 1234,
        "user": {
            "id": 4321,
            "name": "Alex",
            "email": "alex@example.com",
            "avatar_url": ""
        },
        "privilege_group": {
            "id": 2,
            "name": "Admin",
            "system": true
        },
        "moderated_workspaces": [
            {
                "id": 29456,
                "name": "ACME USA"
            },
            {
                "id": 27123,
                "name": "Nutech"
            }
        ],
        "project_role": {
            "id": "prjrl-AQRtExgY-cEGWTN",
            "name": "Builder"
        }
    }
}
```

* * *

## Create a customer manager

Creates a new customer manager in an Embedded partner's account.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/customer_managers
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| team\_collaborator\_id | **string** _required_ | The collaborator's ID. |
| role\_id | **string** _required_ | The legacy role to assign the customer manager. |
| project\_role\_id | **string** _optional_ | The project role to assign the customer manager. |
| permitted\_workspace\_ids | **array of integers** _optional_ | The list of workspace IDs where the customer manager should have the specified role, according to the `role_id` you provide. If omitted or set to an empty array (`[]`), this parameter grants the customer manager the specified role in _all_ workspaces in the Embedded partner's account. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/customer_managers' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "team_collaborator_id": :team_collaborator_id_value,
            "role_id": :role_id_value,
            "permitted_workspace_ids": [:permitted_workspace_id_1],
            "project_role_id": ":project_role_id"
          }'
```

</api-code>

### Response

```json
{
    "result": {
        "id": 1234,
        "user": {
            "id": 4321,
            "name": "Alex",
            "email": "alex@example.com",
            "avatar_url": ""
        },
        "privilege_group": {
            "id": 2,
            "name": "Admin",
            "system": true
        },
        "moderated_workspaces": [
            {
                "id": 29456,
                "name": "ACME USA"
            }
        ],
        "project_role": {
            "id": "prjrl-AQRtExgY-cEGWTN",
            "name": "Builder"
        }
    }
}
```

* * *

## Delete a customer manager

Delete a customer manager from an Embedded partner's account.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/customer_managers/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the customer manager. |

### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/customer_managers/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": "ok"
}
```

---
