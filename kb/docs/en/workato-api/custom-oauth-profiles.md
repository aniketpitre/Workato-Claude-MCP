---
url: 'https://docs.workato.com/en/workato-api/custom-oauth-profiles.md'
description: >-
  Reference for the Workato developer API endpoints to list, create, update, and
  delete custom OAuth profiles.
---

# Developer API - Custom OAuth profiles

Use the endpoints below to manage [custom OAuth profiles](/en/developing-connectors/registering-new-client) programmatically.

## Rate limits

Custom OAuth profile resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Custom OAuth profiles](/en/workato-api/custom-oauth-profiles.html#create-custom-oauth-profile) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/custom\_oauth\_profiles](#list-custom-oauth-profiles) | List Custom OAuth profiles. |
| GET | [/api/custom\_oauth\_profiles/:id](#get-custom-oauth-profile-by-id) | Get a Custom OAuth profile by ID. |
| POST | [/api/custom\_oauth\_profiles](#create-custom-oauth-profile) | Create a Custom OAuth profile. |
| PUT | [/api/custom\_oauth\_profiles/:id](#update-custom-oauth-profile) | Update a Custom OAuth profile. |
| DELETE | [/api/custom\_oauth\_profiles/:id](#delete-custom-oauth-profile) | Delete a Custom OAuth profile. |

## List Custom OAuth profiles

List custom OAuth profiles. Client secrets and tokens aren't returned in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/custom_oauth_profiles
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** | Page number. Defaults to 1. |
| per\_page | **integer** | Page size. Defaults to 100 (maximum is 100). |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/custom_oauth_profiles' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
  "result": [
      {
        "id": 321,
        "user_id": 123,
        "name": "Acme HubSpot OAuth app",
        "provider": "hubspot",
        "data": {
          "client_id": "example_client_id"
        },
        "shared_accounts_count": 1,
        "oem_customers_count": 5,
        "created_at": "2023-01-15T11:50:32.986-07:00",
        "updated_at": "2023-01-15T11:50:32.986-07:00"
      }
    ]
}
```

## Get Custom OAuth profile by ID

Retrieves a custom OAuth profile by ID. Client secrets and tokens aren't returned in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/custom_oauth_profiles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the Custom OAuth profile to retrieve |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/custom_oauth_profiles/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
  "result": {
    "id": 321,
    "user_id": 123,
    "name": "Acme HubSpot OAuth app",
    "provider": "hubspot",
    "data": {
      "client_id": "example_client_id"
    },
    "shared_accounts_count": 1,
    "oem_customers_count": 5,
    "created_at": "2023-01-15T11:50:32.986-07:00",
    "updated_at": "2023-01-15T11:50:32.986-07:00"
  }
}
```

## Create a Custom OAuth profile

Create a Custom OAuth profile.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/custom_oauth_profiles
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the OAuth profile. |
| provider | **string** _required_ | The name of the app tied to this Custom OAuth profile. |
| data.client\_id | **string** _required_ | The Client ID of the Custom OAuth App |
| data.client\_secret | **string** _required_ | The Client secret of the Custom OAuth App |
| data.token | **string** _optional_ | Only required for Slack Apps. The token of the Custom OAuth App |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/custom_oauth_profiles \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "provider": ":provider",
            "data": {
              "client_id": ":client_id",
              "client_secret": ":client_secret"
            }
          }'
```

</api-code>

### Response

```json
{
  "result": {
    "id": 322,
    "user_id": 123,
    "name": "My new OAuth profile",
    "provider": "hubspot",
    "data": {
      "client_id": "example_client_id"
    },
    "shared_accounts_count": 0,
    "oem_customers_count": 0,
    "created_at": "2023-01-15T11:50:32.986-07:00",
    "updated_at": "2023-01-15T11:50:32.986-07:00"
  }
}
```

## Update a Custom OAuth profile

Update a Custom OAuth profile.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/custom_oauth_profiles/:id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the Custom OAuth profile to update |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the OAuth profile. |
| provider | **string** _required_ | The name of the app tied to this Custom OAuth profile. |
| data.client\_id | **string** _required_ | The Client ID of the Custom OAuth App |
| data.client\_secret | **string** _required_ | The Client secret of the Custom OAuth App |
| data.token | **string** _optional_ | Only required for Slack Apps. The token of the Custom OAuth App |

#### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/custom_oauth_profiles/:id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "provider": ":provider",
            "data": {
              "client_id": ":client_id",
              "client_secret": ":client_secret"
            }
          }'
```

</api-code>

### Response

```json
{
  "result": {
    "id": 322,
    "user_id": 123,
    "name": "My updated OAuth profile",
    "provider": "hubspot",
    "data": {
      "client_id": "updated_client_id"
    },
    "shared_accounts_count": 0,
    "oem_customers_count": 0,
    "created_at": "2023-01-15T11:50:32.986-07:00",
    "updated_at": "2023-01-15T11:50:32.986-07:00"
  }
}
```

## Delete a Custom OAuth profile

Delete a Custom OAuth profile.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/custom_oauth_profiles/:id
```

</api-code>

### Path Parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** | ID of the Custom OAuth profile to delete |

#### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/custom_oauth_profiles/:id \
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
