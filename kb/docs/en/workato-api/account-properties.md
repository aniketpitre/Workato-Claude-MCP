---
url: 'https://docs.workato.com/en/workato-api/account-properties.md'
description: >-
  Reference for the Workato environment properties API, with endpoints to list
  properties by prefix and upsert environment properties.
---

# Developer API - Environment properties

Use the endpoints below to manage [environment properties](/en/features/account-properties) programmatically.

## Rate limits

Environment property resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Environment properties](/en/workato-api/account-properties.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/properties](#list-properties-by-prefix) | Lists environment properties that matches a prefix. |
| POST | [/api/properties](#upsert-property) | Upserts environment properties. |

## List properties by prefix

Returns a list of environment properties belonging to a customer that matches a prefix. For example, if the prefix provided is `salesforce_sync.`, any environment property with a name **beginning** with 'salesforce\_sync.' will be returned.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/properties
```

</api-code>

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| prefix | **string** _required_ | Return properties with the given prefix. E.g: `salesforce_sync.`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/properties?prefix=salesforce_sync.' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
  "salesforce_sync.object_name": "Account",
  "salesforce_sync.object_field": "Id"
}
```

## Upsert property

Upserts environment properties. Matches by the names of the properties provided in the request.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/properties
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

### Payload

| Name | Type | Description |
| --- | --- | --- |
| properties | **Hash** _required_ | Contains the names and values of the properties to upsert. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/properties \
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
