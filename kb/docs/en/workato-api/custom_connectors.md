---
url: 'https://docs.workato.com/en/workato-api/custom_connectors.md'
description: >-
  Reference for the Workato custom connectors API to create, search, update,
  validate, release, and share connectors and generate schema from JSON or CSV.
---

# Developer API - Custom connectors

The following endpoints allow you to create and manage custom connectors, validate connector code for syntax and semantic errors, and generate a [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) from sample JSON and CSV documents. The schema generation endpoints are also used in the SDK CLI tool for [schema generation commands](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-generate-schema).

## Rate limits

Custom connector resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Generate schema from JSON: [/api/sdk/generate\_schema /json](/en/workato-api/custom_connectors.html#generate-schema-from-json) | 60 requests per minute |
| POST | Generate schema from CSV: [/api/sdk/generate\_schema /csv](/en/workato-api/custom_connectors.html) | 60 requests per minute |
| All | All other [Custom connectors](/en/workato-api/custom_connectors.html) endpoints | 1 request per second |

The following additional limitations apply to custom connector resources:

| Description | Quota |
| --- | --- |
| Maximum data allowed in custom connector code | 10 MB |
| Compatible code formats | UTF-8 and JSON compatible |

## Quick reference

The Custom connectors resource contains the following endpoints:

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/sdk/generate\_schema/json](#generate-schema-from-json) | Generates Workato schema from a stringified JSON sample. |
| POST | [/api/sdk/generate\_schema/csv](#generate-schema-from-csv) | Generates Workato schema from a stringified CSV sample. |
| GET | [/api/custom\_connectors/search](#search-custom-connector) | Search for custom connectors. |
| GET | [/api/custom\_connectors/:id/code](#get-custom-connector-code) | Fetches code for a custom connector. |
| POST | [/api/sdk/validate\_code](#validate-custom-connector-code) | Validates custom connector code for syntax and semantic errors. |
| POST | [/api/custom\_connectors](#create-custom-connector) | Creates a custom connector. |
| POST | [/api/custom\_connectors/:id/release](#release-custom-connector) | Releases the latest version of a custom connector. |
| POST | [/api/custom\_connectors/:id/share](#share-custom-connector) | Shares a custom connector. |
| PUT | [/api/custom\_connectors/:id](#update-custom-connector) | Updates a custom connector. |

## Generate schema from JSON

Generates Workato schema from a stringified JSON sample.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/sdk/generate_schema/json
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| sample | **string** _optional_ | Stringified JSON of the sample document to parse. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/sdk/generate_schema/json \
      -H 'Authorization: Bearer <api_token>' \
      --data-raw '{
     "sample": ":sample"
     }'
```

</api-code>

### Response

```json
[
    {
        "control_type": "text",
        "label": "Test",
        "type": "string",
        "name": "test"
    }
]
```

## Generate schema from CSV

Generates Workato schema from a stringified CSV sample.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/sdk/generate_schema/csv
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| sample | **string** _optional_ | Stringified CSV of the sample document to parse. |
| col\_sep | **string** _optional_ | Column delimiter for the CSV sample. Must be one of `comma`, `semicolon`, `space`, `tab`, `colon`, `pipe`. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/sdk/generate_schema/csv \
      -H 'Authorization: Bearer <api_token>' \
      --data-raw '{
     "sample": ":sample",
     "col_sep": ":col_sep"
     }'
```

</api-code>

### Response

```json
[
    {
        "control_type": "text",
        "label": "First name",
        "type": "string",
        "name": "first_name"
    },
    {
        "control_type": "text",
        "label": "Last name",
        "type": "string",
        "name": "last_name"
    }
]
```

## Search custom connector

Searches for a custom connector in your workspace by title.

> **LIMITED TO TEN MOST RECENT RELEASES**
> 
> Only the ten most recently released versions are returned.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/custom_connectors/search
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| title | **string** _required_ | The title of the custom connector to search for. The search supports partial matches and is case-sensitive. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/custom_connectors/search?title=:title' \
  -H "Authorization: Bearer <api_token>"
```

</api-code>

### Sample response

```json
{
    "data": [
        {
            "id": 3066,
            "name": "new_connector_1_connector_4771_1626869114",
            "title": "Acme Connector",
            "logo": "<base_64 encoded logo>",
            "latest_version": 4,
            "latest_version_note": "Latest version",
            "latest_released_version": 3,
            "latest_released_version_note": null,
            "latest_shared_version": 4,
            "latest_shared_version_note": "Latest version",
            "oem_shared_version": 2,
            "oem_shared_at": "2024-02-02T08:05:22.047-07:00",
            "recent_released_versions": [
                {
                    "version": 3,
                    "version_note": "Fixed OAuth token refresh timeout",
                    "created_at": "2024-02-08T05:05:34.136-07:00",
                    "released_at": "2024-02-08T21:33:41.713-07:00"
                },
                {
                    "version": 2,
                    "version_note": null,
                    "created_at": "2022-08-11T07:24:58.890-07:00",
                    "released_at": "2022-08-11T21:33:41.713-07:00"
                }
            ]
        }
    ]
}
```

## Get custom connector code

The Get custom connector code operation allows you to fetch a custom connector's code.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/custom_connectors/:id/code
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| ID | Integer _required_ | The ID of the custom connector for which you plan to fetch the code. You can find your custom connector ID in the search custom connector endpoint. |

### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/custom_connectors/:id/code \
  -H "Authorization: Bearer <api_token>"
```

</api-code>

### Sample response

```json
{
  "data": {
    "code": "<connector_code_stringified>"
  }
}
```

## Validate custom connector code

Checks custom connector code for syntax and semantic errors. Use it to catch issues before you call the [Create custom connector](#create-custom-connector) or [Update custom connector](#update-custom-connector) endpoints.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/sdk/validate_code
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| code | **string** _required_ | The Ruby code for your custom connector. Ensure that the code is stringified. Your code cannot exceed 10 MB in size. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/sdk/validate_code \
  -H "Authorization: Bearer <api_token>" \
  -H "Content-Type: application/json" \
  -d '{
        "code": ":code"
      }'
```

</api-code>

### Sample response

An empty `findings` array means the code has no errors:

```json
{
    "data": {
        "findings": []
    }
}
```

Each finding describes one syntax or semantic error, with a `docs_id` you can use to look up the relevant SDK reference page:

```json
{
    "data": {
        "findings": [
            {
                "type": "syntax",
                "message": "(string):6:9: error: unexpected token tIDENTIFIER",
                "docs_id": "sdk:reference:ruby-methods",
                "line_from": 6,
                "column_from": 8,
                "line_to": 6,
                "column_to": 11
            }
        ]
    }
}
```

## Create custom connector

The Create operation allows you to create a custom connector in your workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/custom_connectors
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| title | String | The title of the custom connector you plan to create. |
| logo | String | The logo you plan to add to your custom connector. Your logo must be encoded in Base64 format. |
| description | String | A description of your custom connector. Your description is visible when you share your custom connector through a private link or through the community library. Markdown is allowed. |
| note | String | Notes for the initial version of your custom connector. |
| code | String | The Ruby code for your custom connector. Ensure that the code is stringified. Your code cannot exceed 10MB in size. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/custom_connectors \
  -H "Authorization: Bearer <api_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": ":title",
    "logo": ":logo",
    "description": ":description",
    "note": ":note",
    "code": ":code"
  }'
```

</api-code>

### Sample response

```json
{
    "id": 3066,
    "name": "new_connector_1_connector_4771_1626869114",
    "title": "Acme Connector",
    "logo": "<base_64 encoded logo>",
    "latest_version": 6,
    "latest_version_note": "Latest version",
    "latest_released_version": 4,
    "latest_released_version_note": null,
    "latest_shared_version": 6,
    "latest_shared_version_note": "Latest version",
    "oem_shared_version": 2,
    "oem_shared_at": "2022-08-08T08:05:22.047-07:00",
    "released_versions": [
        {
            "version": 4,
            "version_note": null,
            "created_at": "2022-08-11T07:24:58.890-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        },
        {
            "version": 2,
            "version_note": "hello",
            "created_at": "2021-07-21T05:05:34.136-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        }
    ]
}
```

## Update custom connector

The Update operation allows you to update a custom connector in your workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/custom_connectors/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| ID | Integer _required_ | The ID of the custom connector you plan to update. You can find your custom connector ID in the search custom connector endpoint. |

### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/custom_connectors/:id \
  -H "Authorization: Bearer <api_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": ":title",
    "logo": ":logo",
    "description": ":description",
    "note": ":note",
    "code": ":code"
  }'
```

</api-code>

### Sample response

```json
{
    "id": 3066,
    "name": "new_connector_1_connector_4771_1626869114",
    "title": "Acme Connector",
    "logo": "<base_64 encoded logo>",
    "latest_version": 6,
    "latest_version_note": "Latest version",
    "latest_released_version": 4,
    "latest_released_version_note": null,
    "latest_shared_version": 6,
    "latest_shared_version_note": "Latest version",
    "oem_shared_version": 2,
    "oem_shared_at": "2022-08-08T08:05:22.047-07:00",
    "released_versions": [
        {
            "version": 4,
            "version_note": null,
            "created_at": "2022-08-11T07:24:58.890-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        },
        {
            "version": 2,
            "version_note": "hello",
            "created_at": "2021-07-21T05:05:34.136-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        }
    ]
}
```

## Release custom connector

The Release operation allows you to release the latest version of your custom connector. After you release the new version, it is used in all future jobs.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/custom_connectors/:id/release
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| ID | Integer _required_ | The ID of the custom connector you plan to release. You can find your custom connector ID in the search custom connector endpoint. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/custom_connectors/:id/release \
  -H "Authorization: Bearer <api_token>"
```

</api-code>

### Sample response

```json

{
    "id": 3066,
    "name": "new_connector_1_connector_4771_1626869114",
    "title": "Acme Connector",
    "logo": "<base_64 encoded logo>",
    "latest_version": 6,
    "latest_version_note": "Latest version",
    "latest_released_version": 4,
    "latest_released_version_note": null,
    "latest_shared_version": 6,
    "latest_shared_version_note": "Latest version",
    "oem_shared_version": 2,
    "oem_shared_at": "2022-08-08T08:05:22.047-07:00",
    "released_versions": [
        {
            "version": 4,
            "version_note": null,
            "created_at": "2022-08-11T07:24:58.890-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        },
        {
            "version": 2,
            "version_note": "hello",
            "created_at": "2021-07-21T05:05:34.136-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        }
    ]
}
```

#### HTTP response codes

| Name | Description | Sample reply |
| --- | --- | --- |
| `200` | Success | `{"message": "Connector released successfully"}` |
| `400` | Bad request | `{"message": "Fix code errors before releasing the connector"}` or `{"message": "Connector’s released version is already the latest version"}` |

#### 400 error examples

**Syntax example**

```json
{ "errors" => [{ "code" => 400, "title" => "Line 2 has syntax errors. Please check Workato UI for further details." }] }
```

**Semantic example**

```json
{ "errors" => [{ "code" => 400, "title" => "Expected string or lambda for 'description' in 'test_trigger' trigger but got Symbol." }] }
```

**Logical example**

```json
{ "errors" => [{ "code" => 400, "title" => "The latest version of the custom connector is already released." }] }
```

## Share custom connector

The Share operation allows you to share the most recently released version of your custom connector. After you share your custom connector, all workspaces that have installed your connector through a private link or from the community library receive an update notification.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/custom_connectors/:id/share
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| ID | Integer _required_ | The ID of the custom connector you plan to share. You can find your custom connector ID in the search custom connector endpoint. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/custom_connectors/:id/share \
  -H "Authorization: Bearer <api_token>"
```

</api-code>

### Sample response

```json
{
    "id": 3066,
    "name": "new_connector_1_connector_4771_1626869114",
    "title": "Acme Connector",
    "logo": "<base_64 encoded logo>",
    "latest_version": 6,
    "latest_version_note": "Latest version",
    "latest_released_version": 4,
    "latest_released_version_note": null,
    "latest_shared_version": 6,
    "latest_shared_version_note": "Latest version",
    "oem_shared_version": 2,
    "oem_shared_at": "2022-08-08T08:05:22.047-07:00",
    "released_versions": [
        {
            "version": 4,
            "version_note": null,
            "created_at": "2022-08-11T07:24:58.890-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        },
        {
            "version": 2,
            "version_note": "hello",
            "created_at": "2021-07-21T05:05:34.136-07:00",
            "released_at": "2021-09-26T21:33:41.713-07:00"
        }
    ]
}
```

#### HTTP response codes

| Name | Description | Sample reply |
| --- | --- | --- |
| `200` | Success | `{"message": "Connector shared successfully"}` |
| `400` | Bad request | `{"message": "There is no released version to share"}` or `{"message": "Connector’s shared version is already the latest released version"}` |

#### 400 error examples

**Logical: No released version to share example**

```json
{ "errors" => [{ "code" => 400, "title" => "Release the latest version of the code first" }] }
```

**Logical: Latest release version is already shared example**

```json
{ "errors" => [{ "code" => 400, "title" => "The latest version of the custom connector is already shared" }] }
```

---
