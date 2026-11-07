---
url: 'https://docs.workato.com/en/oem/oem-api/account-properties.md'
description: >-
  Reference for Workato Embedded API environment property endpoints to list
  properties by prefix and upsert properties in a customer workspace.
---

# Embedded API - Environment properties

Use the following endpoints to manage [Environments](/en/features/account-properties) programmatically:

## Rate limits

Environment property resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List properties by prefix: [/api/managed\_users/:managed\_user\_id /properties](/en/oem/oem-api/account-properties.html#list-properties-by-prefix) | 1,000 requests per minute |
| All | All other [Environment properties](/en/oem/oem-api/account-properties.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/properties](#list-properties-by-prefix) | Returns a list of environment properties belonging to a customer that matches a prefix. |
| POST | [/api/managed\_users/:managed\_user\_id/properties](#upsert-property) | Upserts environment properties to a customer workspace. |

## List properties by prefix

Returns a list of environment properties belonging to a customer that matches a prefix. For example, if the prefix provided is `salesforce_sync.`, any account property with a name **beginning** with 'salesforce\_sync.' is returned.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties
```

</api-code>

### URL Parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| prefix | **string** _required_ | Return properties with the given prefix. For example: `salesforce_sync.`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties?prefix=:prefix_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
    "result": {
        "salesforce_sync.object_name": "Account",
        "salesforce_sync.object_field": "Id"
    }
}
```

## Upsert property

Upserts environment properties to a customer workspace. Matches by the names of the properties provided in the request.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties
```

</api-code>

  

> **PROPERTY LIMITS**
> 
> Environment properties have the following quotas:
> 
> | Description | Quota |
> | --- | --- |
> | Maximum number of environment properties per environment | 1,000 |
> | Maximum length of an environment property name | 100 characters |
> | Maximum length of an environment property value | 1,024 characters |

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| properties | **Hash** _required_ | Contains the names and values of the properties to upsert. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{ "properties": { ":property_name_1": ":property_value_1", ":property_name_2": ":property_value_2" }}'
```

</api-code>

### Response

```json
{
  "success": true
}
```

---
