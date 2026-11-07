---
url: 'https://docs.workato.com/en/workato-api.md'
description: >-
  The Developer API lets you manage recipes, connections, jobs, and on-prem
  agents, and automate every aspect of your Workato workspace.
---

# Developer API

The Developer API offers access to a wide range of Workato resources that enable you to manage recipes, connections, jobs, and more. You can use this API to automate every aspect of your Workato workspace, from deploying recipe manifests between development and production environments to rolling out new on-prem agents within your network landscape.

> **FEATURE AVAILABILITY**
> 
> The Developer API is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

## Base URL

The Developer API is a collection of API endpoints for interacting with Workato users, recipes, and more. Each endpoint contains the **base URL** and the **resource path** to the object.

The base URL of the API endpoint depends on the [data center](/en/datacenter/datacenter-overview) you use:

### Workato Enterprise customers

- US Data Center: `https://app.workato.com/api/`
- EU Data Center: `https://app.eu.workato.com/api/`
- JP Data Center: `https://app.jp.workato.com/api/`
- SG Data Center: `https://app.sg.workato.com/api/`
- AU Data Center: `https://app.au.workato.com/api/`
- IL Data Center: `https://app.il.workato.com/api/`
- CN Data Center: `https://app.workatoapp.cn/api/`
- KR Data Center: `https://app.kr.workato.com/api/`
- UK Data Center: `https://app.uk.workato.com/api/`

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service Data Center: `https://app.trial.workato.com/api/`

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This page provides general guidance for all Workato users. If you're a Virtual Private Workato (VPW) customer, refer to your private documentation for detailed configuration guidance specific to your instances.

## Authentication

The Developer API uses API tokens to authenticate requests. You can generate an API token by creating an API client under **Workspace admin** and assigning it both a client role and project scopes.

> **LEGACY API KEY DEPRECATION**
> 
> The Developer API previously used a legacy, full-access API key and email in **request headers** or the **query parameters** to authenticate requests.
> 
> As of July 14, 2025, legacy API keys are fully deprecated. API requests authenticated through legacy API keys are rejected. Email notifications were sent to affected users on April 14, 2025, with a second batch sent in July for those still using legacy API keys. From October 14, 2025 onwards, legacy API key functionality will be completely removed for all users.
> 
> All API requests must be authenticated using **API client authentication**, with requests sent through **Authorization: Bearer headers** instead of **x-user-token** and **x-user-email** headers.
> 
> Learn more about [migrating to API client authentication](/en/workato-api/moving-to-api-client-authentication-faq).

### Provide API tokens as a bearer token

Provide your API client's API token in the request headers as a `Bearer` token.

```shell
curl  -X GET https://app.workato.com/api/users/me \
      -H 'Authorization: Bearer <api_token>'
```

### Supported formats

The Developer API supports sending request bodies with the `application/json` content-type. All replies are also encoded in `application/json; charset=utf-8`.

## How to generate an API token

You can generate an API token by creating an API client under **Workspace admin > API clients**. Learn more about [configuring API clients and roles](/en/workato-api/api-clients).

> **PERMISSION REQUIREMENTS**
> 
> You must meet one of the following requirements to create or edit API clients:
> 
> - Be signed in with the root email address of the workspace.
> - Have the [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or the legacy [Admin](/en/roles#system-roles) collaborator role.
> - Have a custom role with the [Client and access profiles privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#api-platform)

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

You can use a `x-correlation-id` with the Developer API to track and correlate requests. This improves debugging, traceability, and logging.

You can provide your own `x-correlation-id` in the request header, or Workato generates one for you. If you provide your own `x-correlation-id`, the response includes both your `x-correlation-id` and the `x-correlation-id` from Workato.

---
