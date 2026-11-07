---
url: 'https://docs.workato.com/en/oem/oem-api/custom-oauth-profiles.md'
description: >-
  Reference for Workato Embedded API endpoints to assign and unassign custom
  OAuth profiles to and from customer workspaces.
---

# Embedded API - Custom OAuth profiles

Use the following endpoints to manage [custom OAuth profiles](/en/developing-connectors/registering-new-client) assigned to customers.

## Rate limits

Custom OAuth profile resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Custom OAuth profiles](/en/oem/oem-api/custom-oauth-profiles.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:managed\_user\_id/custom\_oauth\_profiles/:id/assign](#assign-custom-oauth-profile) | Assign a Custom OAuth profile to customer workspace |
| DELETE | [/api/managed\_users/:managed\_user\_id/custom\_oauth\_profiles/:id/unassign](#unassign-custom-oauth-profile) | Unassigns a Custom OAuth profile to a customer workspace. |

## Assign a custom OAuth profile

Assigns a custom OAuth profile to a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/custom_oauth_profiles/:id/assign
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| id | **integer** _required_ | ID of the custom OAuth profile within the Embedded partner workspace you plan to assign to a customer workspace. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/custom_oauth_profiles/:id/assign' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
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

## Unassign a custom OAuth profile

Unassigns a custom OAuth profile to a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/custom_oauth_profiles/:id/unassign
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| id | **integer** _required_ | ID of the custom OAuth profile within the Embedded partner workspace to assign to a customer workspace. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| force | **boolean** | When `true` unassigns the custom OAuth profile even if it is used in a customer workspace. Defaults to `false`. |

### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/custom_oauth_profiles/:id/unassign' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
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

---
