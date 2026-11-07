---
url: 'https://docs.workato.com/en/oem/oem-api.md'
description: >-
  Workato Embedded Partner Platform APIs let partners programmatically create
  and manage customers and assets like recipes and connections.
---

# Embedded API

Workato's Embedded Partner Platform APIs enable partners to programmatically create and manage customers and assets, including recipes and connections.

> **WHO CAN USE THIS FEATURE?**
> 
> A **Embedded account** is required to use Embedded Partner APIs. Contact your Workato representative for more info.

## Base URL

The Embedded Partner APIs are a collection of endpoints for interacting with customers, recipes, and more. Each endpoint contains the `base URL` and the `resource path` to the object.

The `base URL` of the endpoint depends on the [data center](/en/datacenter/datacenter-overview) you use. Here are the `base URL`s for each of Workato's data centers:

<dl><dt>US Data Center</dt><dd><code>https://app.workato.com/api/</code></dd><dt>EU Data Center</dt><dd><code>https://app.eu.workato.com/api/</code></dd><dt>JP Data Center</dt><dd><code>https://app.jp.workato.com/api/</code></dd><dt>SG Data Center</dt><dd><code>https://app.sg.workato.com/api/</code></dd><dt>AU Data Center</dt><dd><code>https://app.au.workato.com/api/</code></dd><dt>IL Data Center</dt><dd><code>https://app.il.workato.com/api/</code></dd><dt>CN Data Center</dt><dd><code>https://app.workatoapp.cn/api/</code></dd><dt>KR Data Center</dt><dd><code>https://app.kr.workato.com/api/</code></dd><dt>UK Data Center</dt><dd><code>https://app.uk.workato.com/api/</code></dd></dl>

## Embedded APIs with Environments

The Embedded API enables you to provision Environments programmatically. The Embedded API structure also allows you to precisely target each environment (Development, Test, and Production) when using the Environments feature for your customers.

Refer to the [Embedded APIs Environments](/en/oem/oem-api/managed-users#provision-environments) for more information about provisioning the Environments feature.

### Access without Environments

The Embedded API allows you to interact with customers regardless of whether they have Environments provisioned. You must add the `managed_user_id` directly to the endpoint: `/api/managed_users/:managed_user_id` to interact with customers who do not have Environments provisioned.

### Targeted Environment access

The API enables targeted access to the Development, Test, and Production environments when interacting with customers who have Environments provisioned. Use the following endpoints based on your environment requirements:

- **Development**: Access the development environment using `/api/managed_users/:managed_user_id_dev`
- **Test**: Access the test environment using `/api/managed_users/:managed_user_id_test`
- **Production**: Access the production environment using `/api/managed_users/:managed_user_id_prod`

Refer to the [Embedded Environments APIs](/en/oem/embedded-environments/embedded-environments-api#how-to-get-the-correct-id) section in the Workato documentation for information on how to target the correct environment.

## Authentication

You must create an API Client to authenticate to the API. [Learn more](/en/workato-api/api-clients).

### Provide API tokens as a bearer token

Provide your API client's API token in the request headers as a `bearer` token.

```shell
curl -X GET 'https://app.workato.com/api/managed_users/19029/properties' \
      -H 'Authorization: Bearer <api_token>'
```

## Supported Formats

Requests sent to the API should include `Content-type: application/json` in the header:

```shell
curl  -X GET 'https://app.workato.com/api/managed_users/19029/properties?prefix=salesforce_sync.' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

Responses are encoded using `application/json; charset=utf-8`.

* * *

## HTTP response codes

- [200 Success](#_200-success)
- [400 Bad Request](#_400-bad-request)
- [401 Unauthorized](#_401-unauthorized)
- [403 Forbidden](#_403-forbidden)
- [404 Not Found](#_404-not-found)
- [500 Server Error](#_500-server-error)

### 200 Success

The `200 Success` response indicates that the request was processed successfully by the server. The response body varies depending on the endpoint and operation performed, but it typically contains the requested data or a confirmation of the action performed.

#### Sample reply

```json
{
    "success": true
}
```

### 400 Bad Request

The `400 Bad Request` error indicates that the server couldn't process the request due to client-side issues. Common causes include malformed requests, invalid fields, or violations of field constraints, such as unsupported data types.

#### Sample reply

```json
{
    "errors": [
        {
            "code": 400,
            "title": "No workspaces found matching the specified workspace filter conditions."
        }
    ]
}
```

### 401 Unauthorized

The `401 Unauthorized` error is returned when the request lacks valid authentication credentials. Common causes include missing tokens, invalid tokens, or incorrect credentials.

#### Sample reply

```json
{
    "errors": [
        {
            "code": 401,
            "title": "Unauthorized"
        }
    ]
}
```

### 403 Forbidden

The `403 Forbidden` error indicates that the client is authenticated but doesn't have the necessary permissions to access the requested resource.

#### Sample reply

```json
{
    "errors": [
        {
            "code": 403,
            "title": "Forbidden"
        }
    ]
}
```

### 404 Not Found

The `404 Not Found` error is returned when the requested resource doesn't exist or can't be found. This can occur if the URL is incorrect or the resource has been deleted.

#### Sample reply

```json
{
    "errors": [
        {
            "code": 404,
            "title": "Not found"
        }
    ]
}
```

### 500 Server Error

The `500 Server Error` code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request. This error is usually caused by server-side issues.

#### Sample reply

```json
{
    "errors": [
        {
            "code": 500,
            "title": "Server error",
            "detail": "3188c2d0-29a4-4080-908e-582e7ed82580"
        }
    ]
}
```

## Use x-correlation-ids

You can use a `x-correlation-id` with the Embedded API to track and correlate requests. This improves debugging, traceability, and logging.

You can provide your own `x-correlation-id` in the request header, or Workato generates one for you. If you provide your own `x-correlation-id`, the response includes both your `x-correlation-id` and the `x-correlation-id` from Workato.

---
