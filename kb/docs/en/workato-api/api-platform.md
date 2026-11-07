---
url: 'https://docs.workato.com/en/workato-api/api-platform.md'
description: >-
  Reference for the API platform endpoints to create and manage API collections,
  endpoints, clients, and access profiles in Workato.
---

# Developer API - API platform

The [API platform](/en/api-management) APIs allow users to programmatically create and manage API Platform assets like endpoints, collections, clients, and access profiles.

API platform endpoints allow up to 10 requests per second.

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
| All | All [API platform](/en/workato-api/api-platform.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/api\_collections](#list-api-collections) | List **API collections**. The endpoint returns the `project_id` of the project to which the collections belong in the response. |
| POST | [/api/api\_collections](#create-api-collection) | Create an **API collection** within a project you specify. |
| PUT | [/api/api\_collections/:api\_collection\_id](#update-api-collection) | Update an existing **API collection**. |
| DELETE | [/api/api\_collections/:api\_collection\_id](#delete-api-collection) | Delete an **API collection** along with its endpoints. |
| GET | [/api/api\_collections/:api\_collection\_id/openapi](#get-api-collection-openapi-specification) | Get the OpenAPI specification for an **API collection**. |
| GET | [/api/api\_endpoints](#list-api-endpoints) | List **API endpoints** in a collection. |
| POST | [/api/api\_collections/:api\_collection\_id/api\_endpoints](#create-api-endpoint) | Create an **API endpoint** within a collection you specify. |
| PUT | [/api/api\_collections/:api\_collection\_id/api\_endpoints/:api\_endpoint\_id](#update-api-endpoint) | Update an existing **API endpoint**. |
| PUT | [/api/api\_endpoints/:api\_endpoint\_id/enable](#enable-api-endpoint) | Enable an **API endpoint** in a collection. |
| PUT | [/api/api\_endpoints/:api\_endpoint\_id/disable](#disable-api-endpoint) | Disable an **API endpoint** in a collection. |
| GET | [/api/api\_endpoints/:api\_endpoint\_id/openapi](#get-api-endpoint-openapi-specification) | Get the OpenAPI specification for an **API endpoint**. |
| GET | [/api/api\_clients](#list-api-clients) | List all **API clients**. We recommend that you migrate to the [List API clients (v2)](#list-api-clients-v2) endpoint to prepare for future deprecation. |
| GET | [/api/v2/api\_clients](#list-api-clients-v2) | List all **API clients**. Workato includes the `project_id` of the project associated with the API client in the response. |
| POST | [/api/api\_clients](#create-api-client) | Create a new **API client** within a project you specify. We recommend that you migrate to the [Create API client (v2)](#create-api-client-v2) endpoint to prepare for future deprecation. |
| POST | [/api/v2/api\_clients](#create-api-client-v2) | Create a new **API client** within a project you specify. |
| GET | [/api/v2/api\_clients/:api\_client\_id](#get-api-client) | Retrieve details of an API client by ID. |
| PUT | [/api/v2/api\_clients/:api\_client\_id](#update-api-client) | Update an existing API client within a project you specify. |
| DELETE | [/api/v2/api\_clients/:api\_client\_id](#delete-api-client) | Delete an existing API client. |
| GET | [/api/api\_access\_profiles](#list-access-profiles) | List **access profiles** for an API client. We recommend that you migrate to the [List API keys](#list-api-keys) endpoint to prepare for future deprecation. |
| GET | [/api/v2/api\_clients/:api\_client\_id/api\_keys](#list-api-keys) | List **API keys** for an API client. |
| POST | [/api/api\_access\_profiles](#create-access-profile) | Create an **access profile** for an API client. We recommend that you migrate to the [Create API key](#create-an-api-key) endpoint to prepare for future deprecation. |
| POST | [/api/v2/api\_clients/:api\_client\_id/api\_keys](#create-an-api-key) | Create an **API key** for an API client. |
| PUT | [/api/api\_access\_profiles/:api\_access\_profile\_id](#update-access-profile) | Update an **access profile** for an API client. We recommend that you migrate to the [Update API key](#update-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](#update-api-key) | Update an **API key** for an API client. |
| PUT | [/api/api\_access\_profiles/:api\_access\_profile\_id/enable](#enable-access-profile) | Enable an **access profile** for an API client. We recommend that you migrate to the [Enable API key](#enable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/enable](#enable-api-key) | Enable an **API key** for an API client. |
| PUT | [/api/api\_access\_profiles/:api\_access\_profile\_id/disable](#disable-access-profile) | Disable an **access profile** for an API client. We recommend that you migrate to the [Disable API key](#disable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/disable](#disable-api-key) | Disable an **API key** for an API client. |
| PUT | [/api/api\_access\_profiles/:access\_profile\_id/refresh\_secret](#refresh-token-secret) | Refresh the token or secret for an access profile. We recommend that you migrate to the [Refresh API key secret](#refresh-api-key-secret) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/refresh\_secret](#refresh-api-key-secret) | Refresh the authentication token or OAuth 2.0 client secret for an API key. |
| DELETE | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](#delete-api-key) | Delete an existing API key. |
| GET | [/api/v2/api\_portals](#list-api-portals) | List all API portals associated with API clients in your workspace. |
| GET | [/api/cert\_bundles](#list-certificate-bundles) | List all certificate bundles. |
| POST | [/api/cert\_bundles](#create-a-certificate-bundle) | Create a new certificate bundle. |
| PUT | [/api/cert\_bundles/:certificate\_bundle\_id](#update-a-certificate-bundle) | Update a certificate bundle. |
| DELETE | [/api/cert\_bundles/:certificate\_bundle\_id](#delete-a-certificate-bundle) | Delete a certificate bundle. |
| GET | [/api/cert\_bundles/:certificate\_bundle\_id/download](#download-a-certificate-bundle) | Download the certificate bundle PEM file. |

## List API collections

List all [API collections](/en/api-mgmt/api-collections). The endpoint returns the `project_id` of the project to which the collections belong in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/api_collections
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| per\_page | **integer** | Number of API collections to return in a single page. Defaults to `100`. Max is `100`. |
| page | **integer** | Page number of the API collections to fetch. Defaults to `1`. |

### Response

```json
[
    {
        "id": 1361,
        "name": "Quote to cash",
        "version": "1.0",
        "url": "https://api.peatql.io/quote-to-cash-v1",
        "api_spec_url": "https://www.workato.com/doc/service/quote-to-cash-v1/swagger?token=4cab5bdf2cebbe2b4ahjkc9ac175f60c",
        "created_at": "2020-06-15T22:20:15.327-07:00",
        "updated_at": "2020-06-15T22:20:15.327-07:00",
        "project_id": "523144"
    }
]
```

## Create an API collection

Create an [API collection](/en/api-mgmt/api-collections) within a project you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/api_collections
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _required_ | The ID of a specific project. Retrieve a list of project IDs using the [list projects](/en/workato-api/folders#list-projects) endpoint. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the collection |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/api_collections?project_id=:project_id \
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
    "id": 1391,
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

## Update an API collection

Update an existing [API collection](/en/api-mgmt/api-collections).

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
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
curl -X PUT https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id \
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
    "id": 1391,
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

## Delete an API collection

Delete an [API collection](/en/api-mgmt/api-collections) along with all of its endpoints.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_collection\_id | **string** _required_ | ID of the API collection to delete. |

#### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id \
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

Get the OpenAPI (Swagger) specification for an [API collection](/en/api-mgmt/api-collections).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id/openapi
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_collection\_id | **string** _required_ | ID of the API collection. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| oas\_ver | **string** _optional_ | OpenAPI version to generate. Set to `2` for Swagger 2.0. Defaults to OpenAPI 3.0. |
| invocable | **boolean** _optional_ | Set to `true` to generate the specification for test mode. |

#### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id/openapi \
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

Lists all API endpoints. Specify the `api_collection_id` to obtain the list of endpoints in a specific collection.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/api_endpoints
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_collection\_id | **string** | ID of the API collection. If the parameter is not provided, all API endpoints are returned. |
| per\_page | **integer** | Number of API endpoints to return in a single page. Defaults to `100`. Max is `100`. |
| page | **integer** | Page number of the API endpoints to fetch. Defaults to `1`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/api_endpoints?api_collection_id=:api_collection_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
[
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
```

## Create an API endpoint

Create an [API endpoint](/en/api-mgmt/api-endpoints) within an [API collection](/en/api-mgmt/api-collections) you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id/api_endpoints
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
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
curl -X POST https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id/api_endpoints \
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

## Update an API endpoint

Update an existing [API endpoint](/en/api-mgmt/api-endpoints).

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id/api_endpoints/:api_endpoint_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
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
curl -X PUT https://YOUR_DATA_CENTER/api/api_collections/:api_collection_id/api_endpoints/:api_endpoint_id \
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

## Enable an API endpoint

Enables an API endpoint. You must start the associated recipe to enable the API endpoint successfully.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/api_endpoints/:api_endpoint_id/enable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_endpoint\_id | **string** | ID of the API endpoint. |

#### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/api_endpoints/:api_endpoint_id/enable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Disable an API endpoint

Disables an active API endpoint. The endpoint can no longer be called by a client.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/api_endpoints/:api_endpoint_id/disable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_endpoint\_id | **string** | ID of the API endpoint. |

#### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/api_endpoints/:api_endpoint_id/disable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Get API endpoint OpenAPI specification

Get the OpenAPI (Swagger) specification for a specific [API endpoint](/en/api-mgmt/api-endpoints).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/api_endpoints/:api_endpoint_id/openapi
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_endpoint\_id | **string** _required_ | ID of the API endpoint. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| oas\_ver | **string** _optional_ | OpenAPI version to generate. Set to `2` for Swagger 2.0. Defaults to OpenAPI 3.0. |
| invocable | **boolean** _optional_ | Set to `true` to generate the specification for test mode. |

#### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/api_endpoints/:api_endpoint_id/openapi \
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

List all [API clients](/en/api-mgmt/api-client-mgmt#api-clients). This endpoint includes the `project_id` to which the API client belongs in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/api_clients
```

</api-code>

  

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [List API clients (v2)](#list-api-clients-v2) endpoint before this date to ensure uninterrupted service.

### Response

```json
[
  {
      "id": 1255,
      "name": "Automation Inc.",
      "created_at": "2020-07-31T03:44:22.435-07:00",
      "updated_at": "2020-07-31T03:44:22.435-07:00",
      "project_id" : "523144"
  },
  {
      "id": 1890,
      "name": "Umbrella Corporation",
      "created_at": "2020-07-31T03:44:22.435-07:00",
      "updated_at": "2020-07-31T03:44:22.435-07:00",
      "project_id": "423455"
  }
]
```

## List API clients (v2)

List all [API clients](/en/api-mgmt/api-client-mgmt#api-clients). This endpoint includes the `project_id` of the API client in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/api_clients
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _optional_ | The ID of a specific project. Retrieve a list of project IDs with the [list projects](/en/workato-api/folders#list-projects) endpoint. |
| page | **integer** _optional_ | Page number. Defaults to 1. |
| per\_page | **integer** _optional_ | Page size. Defaults to 100. The maximum page size is 100. |
| cert\_bundle\_ids | **array** _optional_ | Filter clients by certificate bundle IDs. Returns only clients associated with the specified certificate bundles. |

### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/v2/api_clients \
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
      "logo": "https://s3-48296.alexv.awstf.workato.com/paperclip/api_customers/logos/000/000/001/small/psyduck.png?1729853526",
      "logo_2x": "https://s3-48296.alexv.awstf.workato.com/paperclip/api_customers/logos/000/000/001/medium/psyduck.png?1729853526",
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
          "name": "Proxy to Alex's API collection"
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

## Create an API client

Create a new [API client](/en/api-mgmt/api-client-mgmt#api-clients) within a project you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/api_clients
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Create an API client (v2)](#create-api-client-v2) endpoint before this date to ensure uninterrupted service.

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _required_ | The ID of a specific project. Retrieve a list of project IDs by using the [list projects](/en/workato-api/folders#list-projects) endpoint. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the client. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/api_clients?project_id=:project_id \
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

Create a new [API client](/en/api-mgmt/api-client-mgmt#api-clients) within a project you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/api_clients
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the client. |
| description | **string** _optional_ | Description of the client. |
| project\_id | **integer** _optional_ | ID of the project to create the client in, if applicable. |
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
curl -X POST https://YOUR_DATA_CENTER/api/v2/api_clients \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
            "name": ":name",
            "description": ":description",
            "api_portal_id": :api_portal_id,
            "auth_type": ":auth_type",
            "idp_user_id": ":idp_user_id",
            "mtls_enabled": :true_or_false
        }'
```

</api-code>

Provide the `email` field when the target portal uses magic link authentication:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/v2/api_clients \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
            "name": ":name",
            "description": ":description",
            "api_collection_ids": [:api_collection_id],
            "api_portal_id": :api_portal_id,
            "auth_type": ":auth_type",
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

Retrieve details of an [API client](/en/api-mgmt/api-client-mgmt#api-clients) by ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | ID of the API client to retrieve. |

#### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id \
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

Update an existing [API client](/en/api-mgmt/api-client-mgmt#api-clients) within a project you specify.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | ID of the API client to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Updated name of the client. |
| description | **string** _optional_ | Updated description of the client. |
| project\_id | **integer** _optional_ | Updated project ID associated with the client. |
| email | **string** _optional_ | Updated email address for the client. |
| api\_collection\_ids | **array** _required_ | Updated list of API collections assigned to the client. |
| api\_policy\_id | **integer** _required_ | Updated API policy ID. |
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
curl -X PUT https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id \
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
        "email": "damien.tan@workato.com",
        "auth_type": "token",
        "mtls_enabled": true,
        "validation_formula": "CN=api-client",
        "cert_bundle_ids": [2],
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

Delete an existing [API client](/en/api-mgmt/api-client-mgmt#api-clients).

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id
```

</api-code>

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id' \
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

List all [access profiles](/en/api-mgmt/api-client-mgmt#access-profile) for an API client. If you don't provide an API client ID, this endpoint returns access profiles for all API clients.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/api_access_profiles
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [List API keys](#list-api-keys) endpoint before this date to ensure uninterrupted service.

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** | Provide an API client ID to retrieve access profiles belonging to a specific API client. |
| per\_page | **integer** | Number of access profiles returned in a single page. Defaults to `100`. Max is `100`. |
| page | **integer** | Choose the page of access profiles to return. The starting page is `1`. Defaults to `1`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/api_access_profiles?api_client_id=:api_client_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
[
  {
    "id": 942738,
    "name": "Sales API Profile",
    "api_client_id": 933804,
    "api_collection_ids": [
      791245,
      785457,
      785404
    ],
    "active": true,
    "auth_type": "token",
    "created_at": "2023-11-07T19:39:04.294-05:00",
    "updated_at": "2023-11-07T19:39:04.294-05:00"
  },
  {
    "id": 942709,
    "name": "Purchases API Profile",
    "api_client_id": 933804,
    "api_collection_ids": [
      726374,
      743721,
      776384
    ],
    "active": true,
    "auth_type": "token",
    "created_at": "2023-11-07T18:48:19.908-05:00",
    "updated_at": "2023-11-07T18:48:19.908-05:00"
  }
]
```

## List API keys

Retrieve all API keys for an API client. Provide the `api_client_id` parameter to filter keys for a specific client. If you don’t provide the `api_client_id` parameter, the endpoint returns API keys for all clients.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _optional_ | Filter API keys for a specific API client. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys' \
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

## Create an access profile

Create an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) for an API client. To use this endpoint, the workspace must contain at least one API collection to assign to the access profile.

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Create an API key](#create-an-api-key) endpoint before this date to ensure uninterrupted service.

The response returned depends on the auth type chosen ([Auth token](/en/api-mgmt/auth-token), [JSON web token](/en/api-mgmt/jwt-token) or [OAuth 2.0](/en/api-mgmt/oauth2)).

- Auth token authorization will return the auth token in the `secret` response
- JWT token has 2 signing methods: HMAC and RSA. Depending on the chosen method, the respective secret or public is required in the payload
- OAuth 2.0 authorization will return the client ID and secret in `oauth_client_id` and `oauth_client secret`

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/api_access_profiles
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** | ID of the API client. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the access profile |
| api\_collection\_ids | **array** _required_ | IDs of collections to add to the access profile |
| active | **boolean** _required_ | Whether the access profile is disabled or enabled. A client with a disabled access profile cannot call any APIs. |
| auth\_type | **string** _required_ | Authentication method to validate requests. Available types are: [`token`](/en/api-mgmt/auth-token), [`jwt`](/en/api-mgmt/jwt-token), [`oauth2`](/en/api-mgmt/oauth2) and [`oidc`](/en/api-mgmt/oidc). |
| jwt\_method | **string** | The JWT signing method. If the _auth\_type_ is `jwt`, this is required. Available methods are `hmac` and `rsa` for HMAC and RSA respectively. |
| ip\_allow\_list | **array** | List of IP addresses to be allowlisted |
| jwt\_secret | **string** | Based on the method, specify the HMAC shared secret or the RSA public key. |
| oidc\_issuer | **string** _conditional_ | Discovery URL of identity provider or OIDC service. Provide only one of this or _oidc\_jwks\_uri_, not both. Only application if _auth\_type_ is `jwt` or `oidc`. |
| oidc\_jwks\_uri | **string** _conditional_ | JWKS URL of identity provider or OIDC service. Provide only one of this or _oidc\_issuer_, not both. Only application if _auth\_type_ is `jwt` or `oidc`. |
| access\_profile\_claim | **string** _conditional_ | If you wish to use a custom claim to identify this access profile, provide the JWT claim key here. [Learn more](/en/api-mgmt/jwt-workato-claim) Only application if _auth\_type_ is `jwt` or `oidc`. |
| required\_claims | **array** _conditional_ | Provide a list of claims that you wish to enforce.Only application if _auth\_type_ is `jwt` or `oidc`. |
| allowed\_issuers | **array** _conditional_ | Provide a list of issuers (`iss` value in JWT claims) that you wish to allow. Leave If `iss` claim is enforced in _required\_claims_, leave this blank to require any `iss` value. Only application if _auth\_type_ is `jwt` or `oidc`. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/api_access_profiles?api_client_id=:api_client_id'\
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
  	          "name": ":name",
  	          "api_collection_ids": [:api_collection_id_1, :api_collection_id_2],
              "auth_type": ":auth_type",
  	          "active": :true_or_false,
              "ip_allow_list": [":ip_1", ":ip_2"]
           }'
```

</api-code>

#### Sample request (JWT RSA)

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/api_access_profiles?api_client_id=:api_client_id'\
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
	           "name": ":name",
	           "api_collection_ids": [:api_collection_id_1, :api_collection_id_2],
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
    "id": 26985,
    "name": "New test",
    "api_client_id": 1255,
    "api_collection_ids": [
        1395
    ],
    "active": true,
    "auth_type": "token",
    "jwt_method": null,
    "jwt_secret": null,
    "oauth_client_id": null,
    "oauth_client_secret": null,
    "secret": "e3a1ce1d46c4hjk8kfj26781c6ed3073312451ee0990035bf8a4bc90c2a2",
    "created_at": "2020-08-12T08:03:05.492-07:00",
    "updated_at": "2020-08-12T08:03:05.492-07:00"
}
```

## Create an API key

Create a new API key for an API client.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | Specify the ID of the API client to create the API key for. |

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
curl  -X POST 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "active": :true_or_false,
            "ip_allow_list": [":ip_allow_list"],
            "ip_deny_list": [":ip_deny_list"]
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

## Update an access profile

Update an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) for an API client.

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Update an API key](#update-api-key) endpoint before this date to ensure uninterrupted service.

The response returned depends on the auth type chosen ([Auth token](/en/api-mgmt/auth-token), [JSON web token](/en/api-mgmt/jwt-token) or [OAuth 2.0](/en/api-mgmt/oauth2)).

- Auth token authorization will return the auth token in the `secret` response
- JWT token has 2 signing methods: HMAC and RSA. Depending on the chosen method, the respective secret or public is required in the payload
- OAuth 2.0 authorization will return the client ID and secret in `oauth_client_id` and `oauth_client secret`

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/api_access_profiles/:api_access_profile_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_access\_profile\_id | **string** _required_ | API access profile ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Existing/Updated name of the access profile |
| api\_collection\_ids | **array** _required_ | Existing/updated API collection IDs to be configured for the access profile |
| active | **boolean** _required_ | Whether the access profile is disabled or enabled. A client with a disabled access profile cannot call any APIs. |
| auth\_type | **string** _required_ | Authentication method to validate requests. Available types are: [`token`](/en/api-mgmt/auth-token), [`jwt`](/en/api-mgmt/jwt-token), [`oauth2`](/en/api-mgmt/oauth2) and [`oidc`](/en/api-mgmt/oidc). |
| ip\_allow\_list | **array** | List of IP addresses to be allowlisted |
| jwt\_method | **string** | The JWT signing method. If the _auth\_type_ is `jwt`, this is required. Available methods are `hmac` and `rsa` for HMAC and RSA respectively. |
| jwt\_secret | **string** | Based on the method, specify the HMAC shared secret or the RSA public key. |
| oidc\_issuer | **string** _conditional_ | Discovery URL of identity provider or OIDC service. Provide only one of this or _oidc\_jwks\_uri_, not both. Only application if _auth\_type_ is `jwt` or `oidc`. |
| oidc\_jwks\_uri | **string** _conditional_ | JWKS URL of identity provider or OIDC service. Provide only one of this or _oidc\_issuer_, not both. Only application if _auth\_type_ is `jwt` or `oidc`. |
| access\_profile\_claim | **string** _conditional_ | If you wish to use a custom claim to identify this access profile, provide the JWT claim key here. [Learn more](/en/api-mgmt/jwt-workato-claim) Only application if _auth\_type_ is `jwt` or `oidc`. |
| required\_claims | **array** _conditional_ | Provide a list of claims that you wish to enforce.Only application if _auth\_type_ is `jwt` or `oidc`. |
| allowed\_issuers | **array** _conditional_ | Provide a list of issuers (`iss` value in JWT claims) that you wish to allow. Leave If `iss` claim is enforced in _required\_claims_, leave this blank to require any `iss` value. Only application if _auth\_type_ is `jwt` or `oidc`. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/api_access_profiles/:access_profile_id'\
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
  	          "name": ":name",
  	          "api_collection_ids": [:api_collection_id_1, :api_collection_id_2],
              "auth_type": ":auth_type",
  	          "active": :true_or_false,
              "ip_allow_list": [":ip_1", ":ip_2"]
           }'
```

</api-code>

## Update an API key

Update an existing API key for an API client.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | ID of the API client associated with the API key. |
| api\_key\_id | **string** _required_ | ID of the API key to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Updated name of the API key. |
| ip\_allow\_list | **array** _optional_ | Updated list of IP addresses to allow requests from. |
| ip\_deny\_list | **array** _optional_ | Updated list of IP addresses to deny requests from. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
              "name": ":name",
              "ip_allow_list": [":ip_allow_list"],
              "ip_deny_list": [":ip_deny_list"]
          }'
```

</api-code>

#### Response

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

## Enable an access profile

Enable an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) belonging to an API client. Enabling an access profile will allow API calls to be accepted with the enabled profile.

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Enable an API key](#enable-api-key) endpoint before this date to ensure uninterrupted service.

This call returns `success` or error messages for Unauthorized/Bad requests.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/api_access_profiles/:api_access_profile_id/enable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_access\_profile\_id | **string** _required_ | ID of the access profile. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/api_access_profiles/:access_profile_id/enable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Enable API key

Enable an API key for an API client.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id/enable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | ID of the API client that owns the API key. |
| api\_key\_id | **string** _required_ | ID of the API key to enable. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id/enable' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
    "success": true
}
```

## Disable an access profile

Disable an [access profile](/en/api-mgmt/api-client-mgmt#access-profile) belonging to an API client. Disabling an access profile will stop allowing API calls to be accepted with the access profile.

This call returns `success` or error messages for Unauthorized/Bad requests.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/api_access_profiles/:api_access_profile_id/disable
```

</api-code>

> **DEPRECATION NOTICE**
> 
> This endpoint is planned for deprecation on December 1, 2025. Transition to the new [Disable an API key](#disable-api-key) endpoint before this date to ensure uninterrupted service.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_access\_profile\_id | **string** _required_ | ID of the access profile. |

#### Sample request (Auth token)

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/api_access_profiles/:access_profile_id/disable \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

## Disable API key

Disable an API key for an API client.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id/disable
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | ID of the API client that owns the API key. |
| api\_key\_id | **string** _required_ | ID of the API key to disable. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id/disable' \
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
PUT https://YOUR_DATA_CENTER/api/api_access_profiles/:access_profile_id/refresh_secret
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
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

Refresh the authentication token or OAuth 2.0 client secret for an API key.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id/refresh_secret
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | ID of the API client that owns the API key. |
| api\_key\_id | **string** _required_ | ID of the API key to refresh. |

### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id/refresh_secret' \
      -H 'Authorization: Bearer <api_token>'
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
        "active": true,
        "active_since": "2025-02-12T08:44:37+05:30",
        "auth_token": "572d581d91860a7c6372e9390699e26ac5917ac2520e1a917fba43b56d11edbe"
    }
}
```

## Delete API key

Delete an API key for an API client.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| api\_client\_id | **string** _required_ | ID of the API client associated with the API key. |
| api\_key\_id | **string** _required_ | ID of the API key to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/api_clients/:api_client_id/api_keys/:api_key_id' \
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

List all API portals associated with API clients in your workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/api_portals
```

</api-code>

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/api_portals' \
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

List all certificate bundles.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/cert_bundles
```

</api-code>

### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/cert_bundles \
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

Upload a new certificate bundle.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/cert_bundles
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| cert\_bundle\_pem | **file** _required_ | PEM-formatted certificate file. |
| name | **string** _optional_ | Name of the bundle. Defaults to uploaded filename. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/cert_bundles \
     -H 'Authorization: Bearer <api_token>' \
     -F "cert_bundle_pem=@:cert_bundle_pem_path" \
     -F "name=:name"
```

</api-code>

## Update a certificate bundle

Update a certificate bundle by ID.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/cert_bundles/:certificate_bundle_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| certificate\_bundle\_id | **string** _required_ | ID of the certificate bundle to update. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| cert\_bundle\_pem | **file** _optional_ | PEM-formatted certificate file. |
| name | **string** _optional_ | New name for the bundle. |

### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/cert_bundles/:certificate_bundle_id \
     -H 'Authorization: Bearer <api_token>' \
     -F "cert_bundle_pem=@:cert_bundle_pem_path" \
     -F "name=:name"
```

</api-code>

## Delete a certificate bundle

Delete a certificate bundle by ID.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/cert_bundles/:certificate_bundle_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| certificate\_bundle\_id | **string** _required_ | ID of the certificate bundle to delete. |

### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/cert_bundles/:certificate_bundle_id \
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

Download a certificate bundle by ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/cert_bundles/:certificate_bundle_id/download
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| certificate\_bundle\_id | **string** _required_ | ID of the certificate bundle to download. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/cert_bundles/:certificate_bundle_id/download' \
     -H 'Authorization: Bearer <api_token>' \
     -o cert_bundle.pem
```

</api-code>

---
