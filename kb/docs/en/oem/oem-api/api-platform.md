---
url: 'https://docs.workato.com/en/oem/oem-api/api-platform.md'
description: >-
  Reference for Workato Embedded API platform endpoints to create and manage API
  collections, endpoints, clients, and access profiles.
---

# Embedded API - API platform

The [API platform](/en/api-management) APIs allow users to programmatically create and manage API platform assets like endpoints, collections, clients, and access profiles.

All endpoints listed here are Embedded APIs and require an Embedded workspace. The [API platform](/en/api-management) feature is available to customers on specific pricing plans and should be enabled in both the partner admin and customer workspaces. Contact your Workato representative to enable these privileges.

For Embedded partners looking to enable API platform for their customers, use this [guide](/en/oem/apip-enablement) for more information.

> **DEPRECATION NOTICE**
> 
> The following endpoints are scheduled for deprecation on December 1, 2025:
> 
> - [List API clients](#list-api-clients)
> - [Create an API client](#create-api-client)
> - [List access profiles](#list-access-profiles)
> - [Create an access profile](#create-access-profile)
> - [Update an access profile](#update-access-profile)
> - [Enable access profile](#enable-access-profile)
> - [Disable access profile](#disable-access-profile)
> - [Refresh token/secret](#refresh-token-secret)
> 
> Migrate to the following endpoints before this date to avoid service interruptions:
> 
> - [List API clients (v2)](#list-api-clients-v2)
> - [Create an API client (v2)](#create-api-client-v2)
> - [List API keys](#list-api-keys)
> - [Create an API key](#create-an-api-key)
> - [Update an API key](#update-api-key)
> - [Enable API key](#enable-api-key)
> - [Disable API key](#disable-api-key)
> - [Refresh API key secret](#refresh-api-key-secret)

## Rate limits

API platform resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [API portals](/en/oem/oem-api/api-platform.html#list-api-portals) endpoints | 60 requests per minute |
| All | All [API collections](/en/oem/oem-api/api-platform.html#list-api-collections) endpoints | 1,000 requests per minute |
| All | All [API endpoint](/en/oem/oem-api/api-platform.html#list-api-endpoints) endpoints | 1,000 requests per minute |
| All | All [API clients](/en/oem/oem-api/api-platform.html#list-api-clients) endpoints | 1,000 requests per minute |
| All | All [API access profiles](/en/oem/oem-api/api-platform.html#list-access-profiles) endpoints | 1,000 requests per minute |
| All | All [API certificate bundles](/en/oem/oem-api/api-platform.html#list-certificate-bundles) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:id/api\_collections](#list-api-collections) | List **API collections** in a customer workspace. The endpoint returns the `project_id` of the project to which the collections belong in the response. |
| POST | [/api/managed\_users/:id/api\_collections](#create-api-collection) | Create an **API collection** in a customer workspace within a project you specify. |
| PUT | [/api/managed\_users/:id/api\_collections/:api\_collection\_id](#update-api-collection) | Update an existing **API collection** in a customer workspace. |
| DELETE | [/api/managed\_users/:id/api\_collections/:api\_collection\_id](#delete-api-collection) | Delete an **API collection** along with its endpoints in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_collections/:api\_collection\_id/openapi](#get-api-collection-openapi-specification) | Get the OpenAPI specification for an **API collection** in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_endpoints](#list-api-endpoints) | List **API endpoints** in a collection. |
| POST | [/api/managed\_users/:id/api\_collections/:api\_collection\_id/api\_endpoints](#create-api-endpoint) | Create an **API endpoint** within a collection in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_collections/:api\_collection\_id/api\_endpoints/:api\_endpoint\_id](#update-api-endpoint) | Update an existing **API endpoint** in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_endpoints/:api\_endpoint\_id/enable](#enable-api-endpoint) | Enable an **API endpoint** in a collection. |
| PUT | [/api/managed\_users/:id/api\_endpoints/:api\_endpoint\_id/disable](#disable-api-endpoint) | Disable an **API endpoint** in a collection. |
| GET | [/api/managed\_users/:id/api\_endpoints/:api\_endpoint\_id/openapi](#get-api-endpoint-openapi-specification) | Get the OpenAPI specification for an **API endpoint** in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_clients](#list-api-clients) | List all **API clients** in a customer workspace. Workato includes the `project_id` of the project associated with the API client in the response. We recommend that you migrate to the [List API clients (v2)](#list-api-clients-v2) endpoint to prepare for future deprecation. |
| GET | [/api/v2/managed\_users/:id/api\_clients](#list-api-clients-v2) | List all **API clients** in a customer workspace. Workato includes the `project_id` of the project associated with the API client in the response. |
| POST | [/api/managed\_users/:id/api\_clients](#create-api-client) | Create a new **API client** in a customer workspace within a project you specify. We recommend that you migrate to the [Create API client (v2)](#create-api-client-v2) endpoint to prepare for future deprecation. |
| POST | [/api/v2/managed\_users/:id/api\_clients](#create-api-client-v2) | Create a new **API client** in a customer workspace within a project you specify. |
| GET | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id](#get-api-client) | Retrieve details of an API client in a customer workspace using its ID. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id](#update-api-client) | Update an existing API client within a project you specify in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id](#delete-api-client) | Delete an existing API client in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_access\_profiles?api\_client\_id=:client\_id](#list-access-profiles) | List **access profiles** for an API client in a customer workspace. We recommend that you migrate to the [List API keys](#list-api-keys) endpoint to prepare for future deprecation. |
| GET | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys](#list-api-keys) | List **API keys** for an API client in a customer workspace. |
| POST | [/api/managed\_users/:id/api\_access\_profiles](#create-access-profile) | Create an **access profile** for an API client in a customer workspace. We recommend that you migrate to the [Create API key](#create-an-api-key) endpoint to prepare for future deprecation. |
| POST | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys](#create-an-api-key) | Create an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles/:api\_access\_profile\_id](#update-access-profile) | Update an **access profile** for an API client in a customer workspace. We recommend that you migrate to the [Update API key](#update-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](#update-api-key) | Update an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles/:api\_access\_profile\_id/enable](#enable-access-profile) | Enable an **access profile** for an API client in a customer workspace. We recommend that you migrate to the [Enable API key](#enable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/enable](#enable-api-key) | Enable an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles/:api\_access\_profile\_id/disable](#disable-access-profile) | Disable an **access profile** for an API client in a customer workspace. We recommend that you migrate to the [Disable API key](#disable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/disable](#disable-api-key) | Disable an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles/:access\_profile\_id/refresh\_secret](#refresh-token-secret) | Refresh an access profile's **token or secret**. We recommend that you migrate to the [Refresh API key secret](#refresh-api-key-secret) endpoint to prepare for future deprecation. |
| POST | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/refresh\_secret](#refresh-api-key-secret) | Refresh the authentication token or OAuth 2.0 client secret for an API key in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](#delete-api-key) | Delete an existing API key in a customer workspace. |
| GET | [/api/v2/managed\_users/:id/api\_portals](#list-api-portals) | List all API portals associated with API clients in a customer workspace. |
| GET | [/api/managed\_users/:id/cert\_bundles](#list-certificate-bundles) | List all certificate bundles in a customer workspace. |
| POST | [/api/managed\_users/:id/cert\_bundles](#create-a-certificate-bundle) | Create a new certificate bundle in a customer workspace. |
| PUT | [/api/managed\_users/:id/cert\_bundles/:certificate\_bundle\_id](#update-a-certificate-bundle) | Update a certificate bundle in a customer workspace. |
| DELETE | [/api/managed\_users/:id/cert\_bundles/:certificate\_bundle\_id](#delete-a-certificate-bundle) | Delete a certificate bundle in a customer workspace. |
| GET | [/api/managed\_users/:id/cert\_bundles/:certificate\_bundle\_id/download](#download-a-certificate-bundle) | Download the certificate bundle PEM file in a customer workspace. |

## Base path

For all the APIs above, the base path is `/api/managed_users/:managed_user_id` where the customer ID is required in as a URL parameter.

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

**Example:**

```
https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections
```

## List API collections

List all [API collections](/en/api-mgmt/api-collections) in a customer workspace. This endpoint returns the `project_id` of the project to which the collections belong in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Response

```json
{
    "result": [
        {
            "id": 1388,
            "name": "Zuora sync",
            "version": "5",
            "url": "https://api.na.workato.com/abstergoi/created-collection-v5",
            "api_spec_url": "https://www.workato.com/doc/service/created-collection-v5/swagger?token=65989339c72899ahjk9fb173c657cf9511",
            "created_at": "2020-07-31T08:09:29.062-07:00",
            "updated_at": "2020-07-31T08:19:27.703-07:00",
            "project_id": "523144"
        }
    ]
}
```

## Create API collection

Create an [API collection](/en/api-mgmt/api-collections) in a customer workspace within a project you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _required_ | The ID of a specific project. Retrieve a list of project IDs using the [list projects](/en/oem/oem-api/project-properties#list-projects) endpoint. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the collection |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections?project_id=:project_id_value \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
          }'
```

</api-code>

### Response

```json
{
    "id": 1397,
    "name": "Netsuite customers",
    "version": "1.0",
    "url": "https://api.na.workato.com/abstergoi/netsuite-customers-v1",
    "api_spec_url": "https://www.workato.com/doc/service/netsuite-customers-v1/swagger?token=774513f8a712djkls90s7f5a3165eb96d",
    "project_id": "523144",
    "public_access": false,
    "created_at": "2020-07-31T08:24:31.439-07:00",
    "updated_at": "2020-07-31T08:24:31.439-07:00"
}
```

## Update API collection

Update an existing [API collection](/en/api-mgmt/api-collections) in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_collection\_id | **string** _required_ | ID of the API collection to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Updated name of the collection. |
| proxy\_connection\_id | **string** _optional_ | Updated ID of the proxy connection for proxy mode. Pass `null` to clear. |
| public\_access | **boolean** _optional_ | Whether to allow unauthenticated public access. Only configurable for proxy collections on a custom domain. |

#### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name"
         }'
```

</api-code>

### Response

```json
{
    "id": 1397,
    "name": "Netsuite customers (EMEA)",
    "version": "1.0",
    "url": "https://api.na.workato.com/abstergoi/netsuite-customers-v1",
    "api_spec_url": "https://www.workato.com/doc/service/netsuite-customers-v1/swagger?token=774513f8a712djkls90s7f5a3165eb96d",
    "project_id": "523144",
    "public_access": false,
    "created_at": "2020-07-31T08:24:31.439-07:00",
    "updated_at": "2020-08-01T09:12:04.221-07:00"
}
```

## Delete API collection

Delete an [API collection](/en/api-mgmt/api-collections) along with all of its endpoints in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_collection\_id | **string** _required_ | ID of the API collection to delete. |

#### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id \
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

## Get API collection OpenAPI specification

Get the OpenAPI (Swagger) specification for an [API collection](/en/api-mgmt/api-collections) in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id/openapi
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_collection\_id | **string** _required_ | ID of the API collection. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| oas\_ver | **string** _optional_ | OpenAPI version to generate. Set to `2` for Swagger 2.0. Defaults to OpenAPI 3.0. |
| invocable | **boolean** _optional_ | Set to `true` to generate the specification for test mode. |

#### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id/openapi \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "openapi": "3.0.0",
    "info": {
        "title": "API platform",
        "version": "1.0",
        "description": "This page lists the REST services exposed by Netsuite customers. An API key is required to invoke the services. Contact the service owner to get your API key."
    },
    "servers": [
        {
            "url": "https://api.na.workato.com/abstergoi/netsuite-customers-v1"
        }
    ],
    "tags": [
        { "name": "Active", "description": "Active services" },
        { "name": "Inactive", "description": "Inactive services" }
    ],
    "paths": {
        "/salesforce/search": {
            "get": {
                "summary": "salesforce search",
                "operationId": "9903",
                "responses": {
                    "200": {
                        "description": "200",
                        "content": {
                            "application/json": {
                                "schema": { "type": "object", "properties": {} }
                            }
                        }
                    }
                },
                "security": [{ "api_key": [] }],
                "tags": ["Inactive"]
            }
        }
    },
    "components": {
        "securitySchemes": {
            "api_key": {
                "type": "apiKey",
                "description": "Regular API token",
                "name": "API-Token",
                "in": "header"
            },
            "oauth2": {
                "type": "apiKey",
                "description": "JWT or OAuth 2.0 token",
                "name": "Authorization",
                "in": "header"
            }
        }
    },
    "security": [{ "api_key": [] }, { "oauth2": [] }]
}
```

## List API endpoints

Lists all API endpoints in a customer workspace. Specify the `api_collection_id` to obtain the list of endpoints in a specific collection.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_collection\_id | **string** _optional_ | ID of the API collection to list endpoints from. Leave this field blank to retrieve all API endpoints. |
| page | **integer** _optional_ | Page number of the API endpoints to retrieve. Defaults to `1`. |
| per\_page | **integer** _optional_ | Number of API endpoints to include in each page. Defaults to `100`. Maximum is `100`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints?api_collection_id=:api_collection_id_value&page=:page_value&per_page=:per_page_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
    "result": [
        {
            "id": 9903,
            "api_collection_id": 1391,
            "flow_id": 39999,
            "name": "salesforce search",
            "method": "GET",
            "url": "https://api.na.workato.com/abstergoi/netsuite-customers-v1/salesforce/search",
            "legacy_url": null,
            "base_path": "/abstergoi/netsuite-customers-v1/salesforce/search",
            "path": "salesforce/search",
            "active": false,
            "legacy": false,
            "created_at": "2020-08-05T05:59:55.991-07:00",
            "updated_at": "2020-08-05T05:59:55.991-07:00"
        }
    ]
}
```

## Create API endpoint

Create an [API endpoint](/en/api-mgmt/api-endpoints) within an [API collection](/en/api-mgmt/api-collections) in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id/api_endpoints
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_collection\_id | **string** _required_ | ID of the API collection to create the endpoint in. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the endpoint. |
| method | **string** _required_ | HTTP method used by the endpoint, such as `GET`, `POST`, `PUT`, `PATCH`, or `DELETE`. |
| path | **string** _required_ | Path for the endpoint, relative to the collection's base URL. |
| description | **string** _optional_ | Description of the endpoint. |
| flow\_id | **string** _optional_ | ID of the API recipe associated with this endpoint. |
| use\_cache | **boolean** _optional_ | Whether to cache the response of the endpoint. Defaults to `false`. |
| cache\_keys | **array** _optional_ | List of request parameters to match the cache on. |
| cache\_ttl | **integer** _conditional_ | Cache TTL in seconds. **Required** when `use_cache` is `true`. |
| recipe\_timeout | **integer** _optional_ | API timeout, in seconds. Defaults to `30`. |
| validate\_request | **boolean** _optional_ | Whether to activate OpenAPI request validation. Defaults to `false`. |
| validation\_formula | **string** _optional_ | Ruby formula used to validate requests. |

#### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id/api_endpoints \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name",
           "method": ":method",
           "path": ":path",
           "flow_id": ":flow_id"
         }'
```

</api-code>

### Response

```json
{
    "id": 9904,
    "api_collection_id": 1391,
    "flow_id": 40001,
    "name": "salesforce upsert",
    "method": "POST",
    "url": "https://api.na.workato.com/abstergoi/netsuite-customers-v1/salesforce/upsert",
    "legacy_url": null,
    "base_path": "/abstergoi/netsuite-customers-v1/salesforce/upsert",
    "path": "salesforce/upsert",
    "active": false,
    "legacy": false,
    "description": "Upsert a Salesforce record",
    "use_cache": false,
    "cache_keys": [],
    "cache_ttl": 0,
    "recipe_timeout": null,
    "validate_request": false,
    "validation_formula": null,
    "created_at": "2020-08-05T05:59:55.991-07:00",
    "updated_at": "2020-08-05T05:59:55.991-07:00"
}
```

## Update API endpoint

Update an existing [API endpoint](/en/api-mgmt/api-endpoints) in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id/api_endpoints/:api_endpoint_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_collection\_id | **string** _required_ | ID of the API collection the endpoint belongs to. |
| api\_endpoint\_id | **string** _required_ | ID of the API endpoint to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Updated name of the endpoint. |
| method | **string** _optional_ | Updated HTTP method used by the endpoint. |
| path | **string** _optional_ | Updated path for the endpoint, relative to the collection's base URL. |
| description | **string** _optional_ | Updated description of the endpoint. |
| flow\_id | **string** _optional_ | Updated ID of the API recipe associated with this endpoint. |
| use\_cache | **boolean** _optional_ | Whether to cache the response of the endpoint. |
| cache\_keys | **array** _optional_ | Updated list of request parameters to match the cache on. |
| cache\_ttl | **integer** _conditional_ | Updated cache TTL in seconds. **Required** when `use_cache` is `true`. |
| recipe\_timeout | **integer** _optional_ | Updated API timeout, in seconds. |
| validate\_request | **boolean** _optional_ | Whether to activate OpenAPI request validation. |
| validation\_formula | **string** _optional_ | Updated Ruby formula used to validate requests. |

#### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_collections/:api_collection_id/api_endpoints/:api_endpoint_id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name",
           "description": ":description"
         }'
```

</api-code>

### Response

```json
{
    "id": 9904,
    "api_collection_id": 1391,
    "flow_id": 40001,
    "name": "salesforce upsert (v2)",
    "method": "POST",
    "url": "https://api.na.workato.com/abstergoi/netsuite-customers-v1/salesforce/upsert",
    "legacy_url": null,
    "base_path": "/abstergoi/netsuite-customers-v1/salesforce/upsert",
    "path": "salesforce/upsert",
    "active": false,
    "legacy": false,
    "description": "Upsert a Salesforce record, including custom fields",
    "use_cache": false,
    "cache_keys": [],
    "cache_ttl": 0,
    "recipe_timeout": null,
    "validate_request": false,
    "validation_formula": null,
    "created_at": "2020-08-05T05:59:55.991-07:00",
    "updated_at": "2020-08-06T11:32:18.774-07:00"
}
```

## Enable API endpoint

Enables an API endpoint. You must start the associated recipe to enable the API endpoint successfully.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints/:api_endpoint_id/enable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_endpoint\_id | **string** | ID of the API endpoint. |

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints/:api_endpoint_id/enable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Disable API endpoint

Disables an active API endpoint. The endpoint can no longer be called by a client.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints/:api_endpoint_id/disable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_endpoint\_id | **string** | ID of the API endpoint. |

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints/:api_endpoint_id/disable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Get API endpoint OpenAPI specification

Get the OpenAPI (Swagger) specification for a specific [API endpoint](/en/api-mgmt/api-endpoints) in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints/:api_endpoint_id/openapi
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_endpoint\_id | **string** _required_ | ID of the API endpoint. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| oas\_ver | **string** _optional_ | OpenAPI version to generate. Set to `2` for Swagger 2.0. Defaults to OpenAPI 3.0. |
| invocable | **boolean** _optional_ | Set to `true` to generate the specification for test mode. |

#### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_endpoints/:api_endpoint_id/openapi \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "openapi": "3.0.0",
    "info": {
        "title": "API platform",
        "version": "1.0",
        "description": "This page lists the REST services exposed by Netsuite customers. An API key is required to invoke the services. Contact the service owner to get your API key."
    },
    "servers": [
        {
            "url": "https://api.na.workato.com/abstergoi/netsuite-customers-v1"
        }
    ],
    "tags": [
        { "name": "Active", "description": "Active services" },
        { "name": "Inactive", "description": "Inactive services" }
    ],
    "paths": {
        "/salesforce/search": {
            "get": {
                "summary": "salesforce search",
                "description": "Search for a Salesforce record",
                "operationId": "9903",
                "parameters": [],
                "responses": {
                    "401": {
                        "description": "Unauthorized",
                        "content": {
                            "application/json": {
                                "schema": { "type": "object", "properties": { "message": { "type": "string" } } }
                            }
                        }
                    },
                    "422": {
                        "description": "Processing error",
                        "content": {
                            "application/json": {
                                "schema": { "type": "object", "properties": { "message": { "type": "string" } } }
                            }
                        }
                    },
                    "500": {
                        "description": "Server error",
                        "content": {
                            "application/json": {
                                "schema": { "type": "object", "properties": { "message": { "type": "string" } } }
                            }
                        }
                    },
                    "200": {
                        "description": "200",
                        "content": {
                            "application/json": {
                                "schema": { "type": "object", "properties": {} }
                            }
                        },
                        "headers": {}
                    }
                },
                "security": [{ "api_key": [] }],
                "x-use-cache": false,
                "x-cache-ttl": 0,
                "x-cache-keys": [],
                "x-cache-size-limit": 10240,
                "tags": ["Inactive"]
            }
        }
    },
    "components": {
        "securitySchemes": {
            "api_key": {
                "type": "apiKey",
                "description": "Regular API token",
                "name": "API-Token",
                "in": "header"
            },
            "oauth2": {
                "type": "apiKey",
                "description": "JWT or OAuth 2.0 token",
                "name": "Authorization",
                "in": "header"
            }
        }
    },
    "security": [{ "api_key": [] }, { "oauth2": [] }]
}
```

## List API clients

List all [API clients](/en/api-mgmt/api-client-mgmt#api-clients) in a customer workspace. This endpoint includes the `project_id` to which the API client belongs in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_clients
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Migrate to the new [List API clients (v2)](#list-api-clients-v2) endpoint before this date to ensure uninterrupted service.

### Response

```json
{
    "result": [
        {
            "id": 1255,
            "name": "Automation Inc.",
            "created_at": "2020-07-31T03:44:22.435-07:00",
            "updated_at": "2020-07-31T03:44:22.435-07:00",
            "project_id": "523144"
        },
        {
            "id": 1890,
            "name": "Umbrella Corporation",
            "created_at": "2020-07-31T03:44:22.435-07:00",
            "updated_at": "2020-07-31T03:44:22.435-07:00",
            "project_id": "423455"
        }
    ]
}
```

## List API clients (v2)

List all [API clients](/en/api-mgmt/api-client-mgmt#api-clients) in a customer workspace. This endpoint includes the `project_id` of the API client in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _optional_ | The ID of a specific project. Retrieve a list of project IDs with the [list projects](/en/workato-api/folders#list-projects) endpoint. |
| page | **integer** _optional_ | Page number. Defaults to 1. |
| per\_page | **integer** _optional_ | Page size. Defaults to 100. The maximum page size is 100. |
| cert\_bundle\_ids | **array** _optional_ | Filter clients by certificate bundle IDs. Returns only clients associated with the specified certificate bundles. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 1,
            "name": "Test client",
            "description": "",
            "active_api_keys_count": 2,
            "total_api_keys_count": 2,
            "created_at": "2023-05-25T08:08:21.413-07:00",
            "updated_at": "2024-10-25T03:52:07.122-07:00",
            "logo": "https://s3-48296.devenv.awstf.workato.com/paperclip/api_customers/logos/000/000/001/small/psyduck.png?1729853526",
            "logo_2x": "https://s3-48296.devenv.awstf.workato.com/paperclip/api_customers/logos/000/000/001/medium/psyduck.png?1729853526",
            "is_legacy": true,
            "api_policies": [
                {
                    "id": 2,
                    "name": "Internal – Admins"
                }
            ],
            "api_collections": [
                {
                    "id": 1,
                    "name": "Echo collection"
                },
                {
                    "id": 2,
                    "name": "Proxy"
                },
                {
                    "id": 4,
                    "name": "Proxy to Vlad's API collection"
                },
                {
                    "id": 6,
                    "name": "San Sanych"
                }
            ]
        }
    ],
    "count": 1,
    "page": 1,
    "per_page": 100
}
```

## Create API client

Create a new [API client](/en/api-mgmt/api-client-mgmt#api-clients) in a customer workspace within a project you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_clients
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Create an API client (v2)](#create-api-client-v2) endpoint before this date to ensure uninterrupted service.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Query parameters

This endpoint does not require any query parameters.

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the client. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_clients?project_id=:project_id_value \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
          }'
```

</api-code>

### Response

```json
{
    "id": 1255,
    "name": "Automation Inc.",
    "created_at": "2020-07-31T03:44:22.435-07:00",
    "updated_at": "2020-07-31T03:44:22.435-07:00"
}
```

## Create an API client (v2)

Create a new [API client](/en/api-mgmt/api-client-mgmt#api-clients) in a specified project in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the client. |
| description | **string** _optional_ | Description of the client. |
| project\_id | **integer** _optional_ | ID of the project where you plan to create the client. |
| api\_portal\_id | **integer** _conditional_ | The ID of the API portal to assign the client, if applicable. Required when the `idp_user_id` or `email` field is provided in the request payload. |
| idp\_user\_id | **string** _conditional_ | Workato Identity user ID for the client. Required when `api_portal_id` refers to an identity portal. |
| email | **string** _conditional_ | Email address for the client. Applies only to magic link portals. New portals are identity portals and require `idp_user_id` instead. |
| api\_collection\_ids | **array** _required_ | IDs of API collections to assign to the client. |
| api\_policy\_id | **integer** _optional_ | ID of the API policy to apply. |
| auth\_type | **string** _required_ | Authentication method to validate requests. Supported types include `token`, `jwt`, `oauth2` and `oidc`. |
| jwt\_method | **string** _conditional_ | The JWT signing method. **Required** when `auth_type` is `jwt`. Supported methods include `hmac` (HMAC) and `rsa` (RSA). |
| jwt\_secret | **string** _conditional_ | HMAC shared secret or RSA public key. **Required** when `auth_type` is `jwt`. |
| oidc\_issuer | **string** _conditional_ | Discovery URL for the OIDC identity provider. Specify this or `oidc_jwks_uri` when `auth_type` is `jwt` or `oidc`. |
| oidc\_jwks\_uri | **string** _conditional_ | JWKS URL for the OIDC identity provider. Specify this or `oidc_issuer` when `auth_type` is `jwt` or `oidc`. |
| access\_profile\_claim | **string** _conditional_ | JWT claim key used to identify the access profile. Applicable when `auth_type` is `jwt` or `oidc`. [Learn more](/en/api-mgmt/jwt-workato-claim). |
| required\_claims | **array** _conditional_ | List of claims to enforce. Applicable when `auth_type` is `jwt` or `oidc`. |
| allowed\_issuers | **array** _conditional_ | List of issuers (iss claim) to allow. If the `iss` claim is enforced in `required_claims`, leave this blank to allow any issuer. Applicable when `auth_type` is `jwt` or `oidc`. |
| mtls\_enabled | **boolean** _optional_ | Whether mutual TLS is enabled for this client. |
| validation\_formula | **string** _optional_ | Formula to validate client certificates. |
| cert\_bundle\_ids | **array** _optional_ | Certificate bundle IDs used for mTLS. |

#### Sample request

Provide the `idp_user_id` field when the target portal is an identity portal:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
            "name": ":name",
            "description": ":description",
            "api_portal_id": :api_portal_id,
            "auth_type": "token",
            "idp_user_id": ":idp_user_id",
            "mtls_enabled": :true_or_false
        }'
```

</api-code>

Provide the `email` field when the target portal uses magic link authentication:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
            "name": ":name",
            "description": ":description",
            "api_collection_ids": [:api_collection_id],
            "api_portal_id": :api_portal_id,
            "auth_type": "token",
            "api_policy_id": :api_policy_id,
            "email": ":email",
            "mtls_enabled": :true_or_false,
            "validation_formula": ":validation_formula",
            "cert_bundle_ids": [:cert_bundle_id]
        }'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 1204662,
        "name": "Test user Inc.",
        "description": "API client for Product Catalog",
        "active_api_keys_count": 0,
        "total_api_keys_count": 0,
        "mtls_enabled": false,
        "created_at": "2026-06-22T23:21:18.873+08:00",
        "updated_at": "2026-06-22T23:21:18.873+08:00",
        "is_legacy": false,
        "auth_type": "token",
        "idp_user_id": "eshSUgjCGb4ZnF51FjEL3b",
        "api_collections": [],
        "api_keys": []
    }
}
```

## Get API client

Retrieve details of an [API client](/en/api-mgmt/api-client-mgmt#api-clients) in a customer workspace using its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _required_ | ID of the API client to retrieve. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 42116,
        "name": "Automation Inc.",
        "description": "API client for Product Catalog",
        "active_api_keys_count": 0,
        "total_api_keys_count": 0,
        "created_at": "2025-02-12T08:36:51.748+05:30",
        "updated_at": "2025-02-12T08:36:51.748+05:30",
        "is_legacy": false,
        "email": "alex.das@workato.com",
        "auth_type": "token",
        "api_collections": [
            {
                "id": 6883,
                "name": "Product Catalog"
            }
        ],
        "api_keys": []
    }
}
```

## Update API client

Update an existing [API client](/en/api-mgmt/api-client-mgmt#api-clients) within a project you specify in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _required_ | ID of the API client to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Updated name of the client. |
| description | **string** _optional_ | Updated description of the client. |
| project\_id | **integer** _optional_ | Updated project ID associated with the client. |
| email | **string** _optional_ | Updated email address for the client. |
| api\_collection\_ids | **array** _required_ | Updated list of API collections assigned to the client. |
| api\_policy\_id | **integer** _optional_ | Updated API policy ID. |
| jwt\_method | **string** _conditional_ | Updated JWT signing method. **Required** when `auth_type` is `jwt`. Supported methods include `hmac` (HMAC) and `rsa` (RSA). |
| jwt\_secret | **string** _conditional_ | Updated HMAC shared secret or RSA public key. **Required** when `auth_type` is `jwt`. |
| oidc\_issuer | **string** _conditional_ | Updated discovery URL for the OIDC identity provider. Specify this or `oidc_jwks_uri` when `auth_type` is `jwt` or `oidc`. |
| oidc\_jwks\_uri | **string** _conditional_ | Updated JWKS URL for the OIDC identity provider. Specify this or `oidc_issuer` when `auth_type` is `jwt` or `oidc`. |
| access\_profile\_claim | **string** _conditional_ | Updated JWT claim key used to identify the access profile. Applicable when `auth_type` is `jwt` or `oidc`. [Learn more](/en/api-mgmt/jwt-workato-claim). |
| required\_claims | **array** _conditional_ | Updated list of claims to enforce. Applicable when `auth_type` is `jwt` or `oidc`. |
| allowed\_issuers | **array** _conditional_ | Updated list of issuers (iss claim) to allow. If the `iss` claim is enforced in `required_claims`, leave this blank to allow any issuer. Applicable when `auth_type` is `jwt` or `oidc`. |
| mtls\_enabled | **boolean** _optional_ | Whether mutual TLS is enabled for this client. |
| validation\_formula | **string** _optional_ | Updated formula to validate client certificates. |
| cert\_bundle\_ids | **array** _optional_ | Updated certificate bundle IDs used for mTLS. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name",
           "description": ":description"
         }'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 42116,
        "name": "Mustard Inc.",
        "description": "API client for Automation workflows",
        "active_api_keys_count": 0,
        "total_api_keys_count": 0,
        "created_at": "2025-02-12T08:36:51.748+05:30",
        "updated_at": "2025-02-12T08:40:27.607+05:30",
        "is_legacy": false,
        "email": "alex.das@workato.com",
        "auth_type": "token",
        "mtls_enabled": true,
        "validation_formula": "CN=api-client",
        "cert_bundle_ids": [3],
        "api_collections": [
            {
                "id": 6883,
                "name": "1"
            }
        ],
        "api_keys": []
    }
}
```

### Delete API client

Delete an existing [API client](/en/api-mgmt/api-client-mgmt#api-clients) in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id
```

</api-code>

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "success": true
}
```

## List access profiles

List all [access profiles](/en/api-mgmt/api-client-mgmt#access-profile) belonging to an API client in a customer workspace. If you don't provide an API client ID, the resource lists all access profiles for all API clients in the customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles?api_client_id=:client_id
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [List API keys](#list-api-keys) endpoint before this date to ensure uninterrupted service.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _optional_ | API client ID for the client that you plan to retrieve access profiles from. |
| api\_token | **string** _required_ | The API token is the token for any API client in your Embedded API platform. You can create a new Embedded API platform API client in your admin account by going to **Workspace access > API clients**. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles?api_client_id=:api_client_id_value'\
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json

"result": [
    {
      "id": 31387,
      "name": "Financial API Client",
      "api_client_id": 4663,
      "api_collection_ids": [
        3574
      ],
      "active": true,
      "auth_type": "token",
      "created_at": "2023-11-21T09:58:30.980-09:00",
      "updated_at": "2023-11-21T09:58:30.980-09:00"
    }
  ]
```

## List API keys

Retrieve all API keys for an API client in a customer workspace. You can optionally provide the `api_client_id` parameter to filter API keys for a specific client. If you don’t provide the `api_client_id` parameter, the endpoint returns API keys for all clients in the customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _optional_ | ID of the API client to filter API keys. If you don't specify the `api_client_id` in the request, the endpoint returns API keys for all clients in the workspace. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 17,
            "name": "Heat",
            "auth_type": "token",
            "ip_allow_list": [],
            "ip_deny_list": [
                "192.168.0.1"
            ],
            "active": true,
            "active_since": "2025-02-04T18:57:35-08:00",
            "auth_token": "dda2"
        }
    ],
    "count": 1,
    "page": 1,
    "per_page": 100
}
```

## Create access profile

Create an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) belonging to an API client in a customer workspace. To use this endpoint, the customer workspace must have at least one API collection to assign to the access profile.

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Create an API key](#create-an-api-key) endpoint before this date to ensure uninterrupted service.

The response returned depends on the auth type chosen ([Auth token](/en/api-mgmt/auth-token), [JSON web token](/en/api-mgmt/jwt-token) or [OAuth 2.0](/en/api-mgmt/oauth2)).

- Auth token authorization will return the auth token in the `secret` response
- JWT token has 2 signing methods: HMAC and RSA. Depending on the chosen method, the respective secret or public is required in the payload
- OAuth 2.0 authorization will return the client ID and secret in `oauth_client_id` and `oauth_client secret`

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | API client ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the access profile |
| api\_collection\_ids | **List of integers** _required_ | IDs of collections to add to the access profile |
| active | **boolean** _required_ | Whether the access profile is disabled or enabled. A client with a disabled access profile cannot call any APIs. |
| auth\_type | **string** _required_ | Authentication method to validate requests. Available options are: `token`, `jwt` and `oauth2` for [Auth token](/en/api-mgmt/auth-token), [JSON web token](/en/api-mgmt/jwt-token) and [OAuth 2.0](/en/api-mgmt/oauth2) respectively. |
| jwt\_method | **string** | The JWT signing method. If the _auth\_type_ is `jwt`, this is required. Available options are `hmac` and `rsa` for HMAC and RSA respectively. |
| jwt\_secret | **string** | Based on the method, specify the HMAC shared secret or the RSA public key. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles?api_client_id=:api_client_id_value'\
      -H 'Authorization: Bearer <api_token>' \
      -d '{
  	          "name": ":name",
  	          "api_collection_ids": [:api_collection_id, :api_collection_id],
              "auth_type": ":auth_type",
  	          "active": :true_or_false
           }'
```

</api-code>

#### Sample request (JWT HMAC)

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles?api_client_id=:api_client_id_value'\
      -H 'Authorization: Bearer <api_token>' \
      -d '{
	           "name": ":name",
	           "api_collection_ids": [:api_collection_id, :api_collection_id],
	           "auth_type": ":auth_type",
	           "jwt_method": ":jwt_method",
	           "jwt_secret": ":jwt_secret",
	           "active": :true_or_false
           }'
```

</api-code>

### Response (Auth token)

```json
{
    "id": 26967,
    "name": "Sales team",
    "api_group_ids": [
        1391,
        1388
    ],
    "active": true,
    "auth_type": "token",
    "jwt_method": null,
    "jwt_secret": null,
    "oauth_client_id": null,
    "oauth_client_secret": null,
    "secret": "xxxxxxxxxxx",
    "created_at": "2020-07-31T09:48:55.337-07:00",
    "updated_at": "2020-07-31T09:48:55.337-07:00"
}
```

## Create an API key

Create an API key for an API client in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _required_ | Provide the ID of the API client you plan to create the API key for. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the API key. |
| active | **boolean** _required_ | Indicates whether the API key is enabled or disabled. Disabled keys cannot call any APIs. |
| ip\_allow\_list | **array** _optional_ | List of IP addresses to add to the allowlist. |
| ip\_deny\_list | **array** _optional_ | List of IP addresses to deny requests from. |

#### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "active": :true_or_false,
            "ip_allow_list": [":ip_address"],
            "ip_deny_list": [":ip_address"]
          }'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 37326,
        "name": "Automation Inc.",
        "auth_type": "token",
        "ip_allow_list": ["8.8.8.8/24"],
        "ip_deny_list": ["192.168.0.0/16"],
        "active": true,
        "active_since": "2025-02-12T08:41:44+05:30",
        "auth_token": "72b378def0c1d83e6a015e654a744c380655565a68c591cf9f3598d0d14bdb5f"
    }
}
```

## Update access profile

Update an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) belonging to an API client in a customer workspace.

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Update an API key](#update-api-key) endpoint before this date to ensure uninterrupted service.

The response returned depends on the auth type chosen ([Auth token](/en/api-mgmt/auth-token), [JSON web token](/en/api-mgmt/jwt-token) or [OAuth 2.0](/en/api-mgmt/oauth2)).

- Auth token authorization will return the auth token in the `secret` response
- JWT token has 2 signing methods: HMAC and RSA. Depending on the chosen method, the respective secret or public is required in the payload
- OAuth 2.0 authorization will return the client ID and secret in `oauth_client_id` and `oauth_client secret`

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles/:api_access_profile_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_access\_profile\_id | **string** _required_ | API access profile ID. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | API client ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the access profile |
| api\_collection\_ids | **string** _required_ | IDs of collections to add to the access profile |
| active | **boolean** _required_ | Whether the access profile is disabled or enabled. A client with a disabled access profile cannot call any APIs. |
| auth\_type | **string** _required_ | Authentication method to validate requests. Available options are: `token`, `jwt` and `oauth2` for [Auth token](/en/api-mgmt/auth-token), [JSON web token](/en/api-mgmt/jwt-token) and [OAuth 2.0](/en/api-mgmt/oauth2) respectively. |
| jwt\_method | **string** | The JWT signing method. If the _auth\_type_ is `jwt`, this is required. Available options are `hmac` and `rsa` for HMAC and RSA respectively. |
| jwt\_secret | **string** | Based on the method, specify the HMAC shared secret or the RSA public key. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles/:api_access_profile_id?api_client_id=:api_client_id_value'\
      -H 'Authorization: Bearer <api_token>' \
      -d '{
  	          "name": ":name",
  	          "api_collection_ids": [:api_collection_id, :api_collection_id],
              "auth_type": ":auth_type",
  	          "active": :true_or_false
           }'
```

</api-code>

## Update an API key

Update an API key for an API client in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _required_ | Specify the ID of the API client associated with the API key you plan to update. |
| api\_key\_id | **string** _required_ | ID of the API key to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Updated name of the API key. |
| ip\_allow\_list | **array** _optional_ | Updated list of IP addresses to allow. |
| ip\_deny\_list | **array** _optional_ | Updated list of IP addresses to deny requests from. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
              "name": ":name",
              "ip_allow_list": [":ip_address"],
              "ip_deny_list": [":ip_address"]
          }'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 37326,
        "name": "Mustard Inc.",
        "auth_type": "token",
        "ip_allow_list": ["8.8.8.8/24"],
        "ip_deny_list": ["192.168.0.0/16"],
        "active": false,
        "active_since": "2025-02-12T08:41:44+05:30",
        "auth_token": "db5f"
    }
}
```

## Enable access profile

Enable an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) belonging to an API client in a customer workspace. Enabling an access profile allows API calls to be accepted with the enabled profile.

This call returns `success` or error messages for Unauthorized/Bad requests.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles/:api_access_profile_id/enable
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Enable an API key](#enable-api-key) endpoint before this date to ensure uninterrupted service.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_access\_profile\_id | **string** _required_ | ID of the access profile. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles/:api_access_profile_id/enable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Enable API key

Enable an API key for an API client in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id/enable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _required_ | Specify the ID of the API client associated with the API key you plan to enable. |
| api\_key\_id | **string** _required_ | ID of the API key to enable. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id/enable' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
    "success": true
}
```

## Disable access profile

Disable an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) belonging to an API client in a customer workspace. Disabling an access profile will stop allowing API calls to be accepted with the access profile.

This call returns `success` or error messages for Unauthorized/Bad requests.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles/:api_access_profile_id/disable
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Disable an API key](#disable-api-key) endpoint before this date to ensure uninterrupted service.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_access\_profile\_id | **string** _required_ | ID of the access profile. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles/:api_access_profile_id/disable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Disable API key

Disable an API key for an API client in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id/disable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _required_ | Specify the ID of the API client associated with the API key you plan to disable. |
| api\_key\_id | **string** _required_ | ID of the API key to disable. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id/disable' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
    "success": true
}
```

## Refresh token/secret

Refreshes the auth token or OAuth 2.0 client secret. This endpoint will fail if the authorization type on the access profile is `JWT`.

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Refresh API key secret](#refresh-api-key-secret) endpoint before this date to ensure uninterrupted service.

The response returned depends on the authorization type of the access profile ([Auth token](/en/api-mgmt/auth-token) or [OAuth 2.0](/en/api-mgmt/oauth2)).

- Auth token authorization will return a new auth token in the `secret` response
- OAuth 2.0 authorization will return a new client ID and secret in `oauth_client_id` and `oauth_client secret`

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api_access_profiles/:access_profile_id/refresh_secret
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| access\_profile\_id | **string** _required_ | API access profile ID |

### Response (Auth token)

```json
{
    "id": 26962,
    "name": "Sales team",
    "api_client_id": 1255,
    "api_collection_ids": [
        1391
    ],
    "active": true,
    "auth_type": "token",
    "jwt_method": null,
    "jwt_secret": null,
    "oauth_client_id": null,
    "oauth_client_secret": null,
    "secret": "xxxxxxxxxxx",
    "created_at": "2020-07-31T09:10:03.310-07:00",
    "updated_at": "2020-08-05T06:08:46.290-07:00"
}
```

## Refresh API key secret

Refreshes the auth token or OAuth 2.0 client secret in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id/refresh_secret
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| api\_client\_id | **string** _required_ | Specify the ID of the API client associated with the API key. |
| api\_key\_id | **string** _required_ | ID of the API key to refresh. |

### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id/refresh_secret' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 3455,
        "name": "Mustard Inc.",
        "auth_type": "token",
        "ip_allow_list": ["8.8.8.8/24"],
        "ip_deny_list": ["192.168.0.0/16"],
        "active": true,
        "active_since": "2025-02-12T08:44:37+05:30",
        "auth_token": "572d581d91860a7c6372e9390699e26ac5917ac2520e1a917fba43b56d11edbe"
    }
}
```

## Delete API key

Delete an API key for an API client in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id
```

</api-code>

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_clients/:api_client_id/api_keys/:api_key_id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "success": true
}
```

## List API portals

List all API portals associated with API clients in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_portals
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/api_portals' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 37,
            "user_id": 14487,
            "name": "IDEA Lifestyle",
            "subdomain": "idea",
            "brand_color": "#371093",
            "api_collection_ids": [
                6882
            ],
            "created_at": "2024-12-13T08:46:37.125+05:30",
            "updated_at": "2025-02-10T14:10:21.440+05:30",
            "logo": "https://workato-staging-assets.s3.amazonaws.com/api_portal/models/portals/logos/000/000/037/small/007.png?1734059797",
            "logo_2x": "https://workato-staging-assets.s3.amazonaws.com/api_portal/models/portals/logos/000/000/037/medium/007.png?1734059797"
        }
    ],
    "count": 1,
    "page": 1,
    "per_page": 100
}
```

## List certificate bundles

List all certificate bundles in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
  "data": [
    {
      "id": 1,
      "name": "cert1",
      "cert_count": 3,
      "leaf_ca_cn": "intermediate_ca_two",
      "expires_at": "2025-04-10T18:49:20.000-07:00",
      "updated_at": "2025-03-27T02:03:56.045-07:00",
      "client_count": 1
    }
  ],
  "count": 1,
  "page": 1,
  "per_page": 20
}
```

## Create a certificate bundle

Upload a new certificate bundle in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| cert\_bundle\_pem | **file** _required_ | PEM-formatted certificate file. |
| name | **string** _optional_ | Name of the bundle. Defaults to uploaded filename. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles \
     -H 'Authorization: Bearer <api_token>' \
     -F "cert_bundle_pem=@:cert_bundle_pem_file" \
     -F "name=:name"
```

</api-code>

## Update a certificate bundle

Update a certificate bundle by ID in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles/:certificate_bundle_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| certificate\_bundle\_id | **string** _required_ | ID of the certificate bundle to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| cert\_bundle\_pem | **file** _optional_ | PEM-formatted certificate file. |
| name | **string** _optional_ | New name for the bundle. |

### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/cert_bundles/:certificate_bundle_id \
     -H 'Authorization: Bearer <api_token>' \
     -F "cert_bundle_pem=@:cert_bundle_pem_file" \
     -F "name=:name"
```

</api-code>

## Delete a certificate bundle

Delete a certificate bundle by ID in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles/:certificate_bundle_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| certificate\_bundle\_id | **string** _required_ | ID of the certificate bundle to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles/:certificate_bundle_id \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
  "success": true
}
```

## Download a certificate bundle

Download a certificate bundle by ID in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles/:certificate_bundle_id/download
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` and be URL encoded. For example, `EA2300`. |
| certificate\_bundle\_id | **string** _required_ | ID of the certificate bundle to download. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/cert_bundles/:certificate_bundle_id/download' \
     -H 'Authorization: Bearer <api_token>' \
     -o cert_bundle.pem
```

</api-code>

---
