---
url: 'https://docs.workato.com/en/oem/oem-api/data-retention.md'
description: >-
  Reference for the Embedded API data retention endpoint to update data
  retention periods in customer workspaces programmatically.
---

# Embedded API - Data retention

This API allows you to manage [data retention](/en/security/data-protection/data-retention/) periods in customer workspaces that have the Configurable Data Retention capability enabled.

## Rate limits

The data retention resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Data retention](/en/oem/oem-api/data-retention.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| PUT | [/api/managed\_users/:managed\_user\_id/update\_data\_retention](#update-data-retention) | Update a customer workspace's data retention period. |

## Update customer workspace's data retention period

Updates the data retention period for customer workspaces where the Configurable Data Retention capability is enabled. Refer to the [Data retention policies](/en/security/data-protection/data-retention/#workato-retention-policy) documentation for more information.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/update_data_retention
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The external ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| data\_retention\_ttl\_hours | **integer** _required_ | The length of time to retain data for the specified customer workspace, in hours. The minimum data retention period is `1` hour and the maximum is determined by the Embedded customer's plan. |

### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/update_data_retention' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "data_retention_ttl_hours": :data_retention_ttl_hours_value
          }'
```

</api-code>

### Response

```json
{
    "data":[]
}
```

---
