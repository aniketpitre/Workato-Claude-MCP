---
url: 'https://docs.workato.com/en/workato-api/project-properties.md'
description: >-
  Reference for the Workato project properties API to list and upsert
  project-level properties by project ID and name prefix.
---

# Developer API - Project properties

Use the following endpoints to manage [project properties](/en/features/project-properties) programmatically.

## Rate limits

Project property resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Project properties](/en/workato-api/project-properties.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/properties](#list-project-properties) | List project-level properties that match a prefix and project ID. |
| POST | [/api/properties](#upsert-project-properties) | Upsert project-level properties. |

## List project properties

Returns a list of project-level properties belonging to a specific project in a customer workspace that matches a `project_id` you specify. You must also include a prefix. For example, if you provide the prefix `salesforce_sync.`, any project property with a name beginning with `salesforce_sync.`, such as `salesforce_sync.admin_email`, with the `project_id` you provided is returned.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/properties
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| prefix | **string** _required_ | Returns properties that contain the prefix you provided. For example, if the prefix is `salesforce_sync.` the property `salesforce_sync.admin_email` is returned. |
| project\_id | **string** _required_ | Returns project-level properties that match the `project_id` you specify. This is distinct from the project's `folder_id`. Retrieve a list of projects and their IDs by calling the [List projects](/en/workato-api/folders#list-projects) endpoint. If this parameter is not present, this call returns [environment properties](/en/features/account-properties). |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/properties?prefix=:prefix_value&project_id=:project_id_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'

```

</api-code>

### Response

```json
{
  "public_url": "https://www.example.com",
  "admin_email": "jude.feeney@example.com"
}
```

## Upsert project properties

Upserts project properties belonging to a specific project in a customer workspace that matches a `project_id` you specify. This endpoint maps to properties based on the names you provide in the request.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/properties
```

</api-code>

  

> **PROPERTY LIMITS**
> 
> Project properties have the following quotas:
> 
> | Description | Quota |
> | --- | --- |
> | Maximum number of project properties per project | 1,000 |
> | Maximum length of project property name | 100 characters |
> | Maximum length of project property value | 1,024 characters |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _required_ | Provide the project ID that contains the project properties you plan to upsert. This is distinct from the project's `folder_id`. Retrieve a list of projects and their IDs by calling the [List projects](/en/workato-api/folders#list-projects) endpoint. If this parameter is not present, this call upserts [environment properties](/en/features/account-properties). |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| properties | **Hash** _required_ | Contains the names and values of the properties you plan to upsert. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/properties?project_id=:project_id_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{ "properties": { ":property_key_1": ":property_value_1", ":property_key_2": ":property_value_2" }}'

```

</api-code>

### Response

```json
{
  "success": true
}
```

---
