---
url: 'https://docs.workato.com/en/oem/oem-api/custom_connectors.md'
description: >-
  Reference for the Embedded API custom connectors resource to list, retrieve,
  share, publish, and remove shared connectors programmatically.
---

# Embedded API - Custom connectors

The **Custom connectors** resource enables you to programmatically manage your shared connectors.

> **WHO CAN USE THESE ENDPOINTS?**
> 
> The endpoints in this guide are Embedded APIs and require an Embedded workspace. Contact your Workato representative for more information.

## Rate limits

Custom connector resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Custom connectors](/en/oem/oem-api/custom_connectors.html) endpoints | 60 requests per minute |

## Quick Reference

The Custom Connectors resource contains the following endpoints:

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/custom\_connectors](#search-custom-connectors) | Get custom connectors. |
| GET | [/api/custom\_connectors/:id](#get-custom-connector-by-id) | Get custom connector by ID. |
| POST | [/api/custom\_connectors/:id/oem\_share/:version](#upsert-version-of-shared-connector) | Create or update a shared connector. |
| POST | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/share](#recipe-share) | Share/publish a recipe containing a custom connector. |
| DELETE | [/api/custom\_connectors/:id/suppress\_oem\_version](#remove-shared-connector) | Remove a shared connector. |

* * *

## Search Custom Connectors

List custom adapters in your Workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/custom_connectors
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| title | **string** _optional_ | Search for connectors by their titles. Partial matches will be returned. |
| oem\_shared | **boolean** _optional_ | Search for connectors that are shared from your OEM master account. |

#### Sample Request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/custom_connectors \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": [
        {
            "id": 3067,
            "name": "new_connector_1_connector_4771_1626869205",
            "title": "Foobar",
            "latest_released_version": null,
            "latest_released_version_note": null,
            "oem_shared_version": null,
            "oem_shared_at": null,
            "released_versions": []
        },
        {
            "id": 3066,
            "name": "new_connector_1_connector_4771_1626869114",
            "title": "Acme Connector",
            "latest_released_version": 4,
            "latest_released_version_note": null,
            "oem_shared_version": 2,
            "oem_shared_at": "2022-08-08T08:05:22.047-07:00",
            "released_versions": [
                {
                    "version": 4,
                    "version_note": null,
                    "created_at": "2022-08-11T07:24:58.890-07:00",
                    "released_at": "2021-09-26T21:33:41.713-07:00"
                },
                {
                    "version": 2,
                    "version_note": "hello",
                    "created_at": "2021-07-21T05:05:34.136-07:00",
                    "released_at": "2021-09-26T21:33:41.713-07:00"
                }
            ]
        }
    ]
}
```

* * *

## Get Custom Connector by ID

Retrieve a specific custom connector by ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/custom_connectors/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The ID of the connector in your Workspace. |

#### Sample Request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/custom_connectors/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": [
        {
            "id": 3066,
            "name": "new_connector_1_connector_4771_1626869114",
            "title": "Acme Connector",
            "latest_released_version": 2,
            "latest_released_version_note": "V2",
            "oem_shared_version": 2,
            "oem_shared_at": "2022-08-08T08:05:22.047-07:00",
            "released_versions": [
                {
                    "version": 2,
                    "version_note": "V2",
                    "created_at": "2021-07-21T05:05:34.136-07:00",
                    "released_at": "2021-09-26T21:33:41.713-07:00"
                }
            ]
        }
    ]
}
```

* * *

## Upsert version of Shared Connector

Creates or updates the version of a Shared Connector in an OEM Master Account.

- If the connector is not currently shared, this creates a new shared connector at the specified version.
- If the connector is currently shared, this updates the version currently shared for this connector.

> **IMPORTANT**
> 
> The version shared must be a released version.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/custom_connectors/:id/share_oem_version/:version
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The ID of the connector in your Workspace to share. |
| version | **integer** _required_ | The version of the connector in your Workspace to share. This must be a released version. |

#### Sample Request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/custom_connectors/:id/share_oem_version/:version \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

- New shared connector created:

```json
{
    "result": {
        "success": true,
        "status": "created"
    }
}
```

- Existing shared connector version updated:

```json
{
    "result": {
        "success": true,
        "status": "updated"
    }
}
```

* * *

## Publish/share a recipe containing a Custom Connector

Allows you to publish a recipe containing a custom connector to your Private Community or share it with customers you specify.

> **IMPORTANT**
> 
> You must share your custom connector with the Embedded customer/ Private Community using the [/api/custom\_connectors/:id/oem\_share/:version](#upsert-version-of-shared-connector) endpoint prior to using this endpoint. Otherwise, Workato displays an error message.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/share
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The account ID/external ID of the Embedded customer. The external should be prefixed with a E(ex.: EA2300) and the resulting ID should be URL encoded. |
| recipe\_id | **string** _required_ | The ID of the recipe you plan to share/publish. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/share \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "success": true
    }
}
```

* * *

## Remove Shared Connector

Removes a shared connector. This does not delete the custom connector from your workspace.

> **IMPORTANT**
> 
> Using this API whilst there are customers accounts using this connector will impact their recipes.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/custom_connectors/:id/suppress_oem_version
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The ID of the shared connector in your Workspace to remove. |

#### Sample Request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/custom_connectors/:id/suppress_oem_version \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

- New shared connector created:

```json
{
    "result": {
        "success": true,
        "status": "suppressed"
    }
}
```

* * *

---
