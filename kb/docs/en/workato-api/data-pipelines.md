---
url: 'https://docs.workato.com/en/workato-api/data-pipelines.md'
description: >-
  Reference for the Workato data pipelines API to create, configure, start,
  stop, and clone pipelines, re-sync objects, and monitor object runs.
---

# Developer API - Data pipelines

Use the following endpoints to manage [data pipelines](/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe) programmatically. You can create and configure pipelines, start and stop them, re-sync objects, and monitor object runs. These endpoints are available in workspaces with data pipelines enabled. Data pipelines and connections are environment-scoped, so an API client can only access pipelines and connections in the environment it belongs to.

## Endpoint access

Your [API client](/en/workato-api/api-clients#api-client-benefits) must have the appropriate privileges to access these endpoints. Configure the **Data Pipelines** section when you [create](/en/workato-api/api-clients#create-a-client-role) or [edit](/en/workato-api/api-clients#edit-a-client-role) a client role to control these privileges. Refer to [Data Pipelines privileges](#data-pipelines-privileges) for the available options.

### Data Pipelines privileges

The **Data Pipelines** privilege group includes the following options:

| Privilege | Endpoint |
| --- | --- |
| **List data pipelines** | `GET /api/data_pipelines` |
| **Get data pipeline details** | `GET /api/data_pipelines/:data_pipeline_id` |
| **Create data pipeline** | `POST /api/data_pipelines` |
| **Update data pipeline** | `PUT /api/data_pipelines/:data_pipeline_id` |
| **Delete data pipeline** | `DELETE /api/data_pipelines/:data_pipeline_id` |
| **Start data pipeline** | `PUT /api/data_pipelines/:data_pipeline_id/start` |
| **Stop data pipeline** | `PUT /api/data_pipelines/:data_pipeline_id/stop` |
| **Clone data pipeline** | `POST /api/data_pipelines/:data_pipeline_id/clone` |
| **Trigger resync for data pipeline** | `POST /api/data_pipelines/:data_pipeline_id/resync` |
| **List objects in data pipeline** | `GET /api/data_pipelines/:data_pipeline_id/objects` |
| **List runs for data pipeline** | `GET /api/data_pipelines/:data_pipeline_id/runs` |
| **Get run details** | `GET /api/data_pipelines/:data_pipeline_id/runs/:run_id` |
| **List source providers** | `GET /api/data_pipelines/sources` |
| **List destination providers** | `GET /api/data_pipelines/destinations` |
| **List source objects** | `POST /api/data_pipelines/source_objects` |
| **List source object fields** | `POST /api/data_pipelines/source_object_fields` |
| **Get configuration schema** | `POST /api/data_pipelines/:data_pipeline_id/configuration` |

## Rate limits

Data pipeline resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Data pipelines](/en/workato-api/data-pipelines.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/data\_pipelines](#list-data-pipelines) | List data pipelines. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id](#get-a-data-pipeline) | Get a data pipeline. |
| POST | [/api/data\_pipelines](#create-a-data-pipeline) | Create a data pipeline. |
| PUT | [/api/data\_pipelines/:data\_pipeline\_id](#update-a-data-pipeline) | Update a data pipeline. |
| DELETE | [/api/data\_pipelines/:data\_pipeline\_id](#delete-a-data-pipeline) | Delete a data pipeline. |
| POST | [/api/data\_pipelines/:data\_pipeline\_id/clone](#clone-a-data-pipeline) | Clone a data pipeline. |
| PUT | [/api/data\_pipelines/:data\_pipeline\_id/start](#start-a-data-pipeline) | Start a data pipeline. |
| PUT | [/api/data\_pipelines/:data\_pipeline\_id/stop](#stop-a-data-pipeline) | Stop a data pipeline. |
| GET | [/api/data\_pipelines/sources](#list-source-providers) | List source providers. |
| GET | [/api/data\_pipelines/destinations](#list-destination-providers) | List destination providers. |
| POST | [/api/data\_pipelines/source\_objects](#list-source-objects) | List the objects available from a source connection. |
| POST | [/api/data\_pipelines/source\_object\_fields](#list-source-object-fields) | List the fields of a source object. |
| POST | [/api/data\_pipelines/:data\_pipeline\_id/configuration](#get-configuration-schema) | Get the configuration schema for a pipeline and validate configuration values. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id/objects](#list-pipeline-objects) | List the objects in a data pipeline. |
| POST | [/api/data\_pipelines/:data\_pipeline\_id/resync](#re-sync-objects) | Re-sync objects in a data pipeline. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id/runs](#list-pipeline-runs) | List object runs for a data pipeline. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id/runs/:run\_id](#get-a-pipeline-run) | Get an object run. |

## Create and run a pipeline

The [Get configuration schema](#get-configuration-schema) and [Update a data pipeline](#update-a-data-pipeline) endpoints require a pipeline ID, so you must create a pipeline before you configure it. Complete the following steps to create and start a pipeline with the API:

1. Call [List source providers](#list-source-providers) and [List destination providers](#list-destination-providers) to retrieve the provider names available in your workspace.
   
2. Call [List source objects](#list-source-objects) and [List source object fields](#list-source-object-fields) to review the data available from your source connection. You can retrieve connection IDs with the [List connections](/en/workato-api/connections#list-connections) endpoint.
   
3. Call [Create a data pipeline](#create-a-data-pipeline) with the source and destination providers and connection IDs.
   
4. Call [Get configuration schema](#get-configuration-schema) to retrieve the configuration fields and default values for the source, destination, or an object. Include your configuration values in the `input` field to validate them.
   
5. Call [Update a data pipeline](#update-a-data-pipeline) to save your `source_config` and `destination_config` values.
   
6. Call [Start a data pipeline](#start-a-data-pipeline) to begin syncing.
   
7. Call [List pipeline objects](#list-pipeline-objects) and [List pipeline runs](#list-pipeline-runs) to monitor sync activity. Call [Re-sync objects](#re-sync-objects) to reload data for specific objects outside the regular schedule.
   

## Error responses

The data pipelines API returns errors in the following formats.

### Error format

Most errors return an `errors` array. Each error includes a `code` and a `title` that describes the error, and can include `detail` and `reason` fields:

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

#### Unauthorized and parameter errors

`401` errors and requests with a missing or invalid parameter return a `message` field that describes the error instead of an `errors` array. The response uses the `errors` array instead if several required parameters are missing. These responses can also include `details` and `reason` fields:

```json
{
  "message": "Unauthorized"
}
```

### Error codes

The data pipelines API returns the following error codes:

| Code | Description |
| --- | --- |
| 400 | Bad request. The request is invalid or the operation failed, such as when a pipeline can't be started or a run doesn't exist. |
| 401 | Unauthorized. The API token is invalid or missing, the API client doesn't have the required privileges, or the API client can't access the folder that contains the resource. |
| 404 | The data pipeline, connection, or source object doesn't exist. |
| 422 | Validation error. Returned by the create and update endpoints. |
| 429 | Too many requests. The rate limit is exceeded. The `Retry-After` response header indicates when you can retry. |
| 500 | Internal server error. The `title` includes an error ID. |

The delete, start, stop, and re-sync endpoints return `{"success": true}` when the operation succeeds and a `400` error when it fails.

Refer to [HTTP response codes](/en/workato-api#http-response-codes) for more information.

## Pipelines

Use the following endpoints to create, update, and control data pipelines.

### List data pipelines

Returns a list of data pipelines in the environment your API client belongs to, sorted by ID in ascending order. The response includes only pipelines in folders your API client can access.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/data_pipelines
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **integer** _optional_ | Returns pipelines in the folder you specify. |
| since\_id | **integer** _optional_ | Returns pipelines with an ID greater than the value you specify. To fetch the next page, set this value to the highest `id` in the previous response. This differs from `since_id` in the [Recipes API](/en/workato-api/recipes#list-recipes-belonging-to-user-query-parameters), which returns IDs lower than the value you provide. |
| per\_page | **integer** _optional_ | Number of pipelines to return per page. Defaults to `100`. Maximum is `100`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/data_pipelines?folder_id=:folder_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "items": [
    {
      "id": 4821,
      "name": "Salesforce to Snowflake",
      "handle": "dpr-BcHkTq2x-x7Lp9Q-SM",
      "folder_id": 27180380,
      "user_id": 81234,
      "created_at": "2026-10-01T09:00:00Z",
      "updated_at": "2026-10-01T09:20:00Z",
      "source_provider": "salesforce",
      "source_shared_account_id": 10452,
      "source_config": {},
      "destination_provider": "snowflake",
      "destination_shared_account_id": 10453,
      "destination_config": {},
      "running": true,
      "last_run_at": "2026-10-14T10:00:05Z",
      "stopped_at": null,
      "last_synced_at": "2026-10-14T09:50:12Z",
      "next_sync_at": "2026-10-14T10:15:00Z",
      "successful_object_runs_count": 1248,
      "failed_object_runs_count": 3,
      "current_sync": {
        "started_at": "2026-10-14T10:00:05Z",
        "successful_object_runs_count": 4,
        "failed_object_runs_count": 0,
        "total_object_runs_count": 6
      },
      "last_sync": {
        "started_at": "2026-10-14T09:45:03Z",
        "completed_at": "2026-10-14T09:50:12Z",
        "successful_object_runs_count": 6,
        "failed_object_runs_count": 0,
        "total_object_runs_count": 6
      }
    },
    {
      "id": 4822,
      "name": "Salesforce to PostgreSQL",
      "handle": "dpr-BcJm4Wn8-q3Zr8T-SM",
      "folder_id": 27180380,
      "user_id": 81234,
      "created_at": "2026-10-02T14:30:00Z",
      "updated_at": "2026-10-03T08:15:00Z",
      "source_provider": "salesforce",
      "source_shared_account_id": 10452,
      "source_config": {},
      "destination_provider": "postgresql",
      "destination_shared_account_id": 10460,
      "destination_config": {},
      "running": false,
      "last_run_at": "2026-10-03T08:00:04Z",
      "stopped_at": "2026-10-03T08:15:00Z",
      "last_synced_at": "2026-10-03T08:04:51Z",
      "next_sync_at": null,
      "successful_object_runs_count": 212,
      "failed_object_runs_count": 0,
      "last_sync": {
        "started_at": "2026-10-03T08:00:04Z",
        "completed_at": "2026-10-03T08:04:51Z",
        "successful_object_runs_count": 4,
        "failed_object_runs_count": 0,
        "total_object_runs_count": 4
      }
    }
  ]
}
```

### Get a data pipeline

Returns the configuration and status of the data pipeline you specify.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline. You can retrieve a list of pipeline IDs by calling the [List data pipelines](#list-data-pipelines) endpoint. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "id": 4821,
  "name": "Salesforce to Snowflake",
  "handle": "dpr-BcHkTq2x-x7Lp9Q-SM",
  "folder_id": 27180380,
  "user_id": 81234,
  "created_at": "2026-10-01T09:00:00Z",
  "updated_at": "2026-10-01T09:20:00Z",
  "source_provider": "salesforce",
  "source_shared_account_id": 10452,
  "source_config": {},
  "destination_provider": "snowflake",
  "destination_shared_account_id": 10453,
  "destination_config": {},
  "running": true,
  "last_run_at": "2026-10-14T10:00:05Z",
  "stopped_at": null,
  "last_synced_at": "2026-10-14T09:50:12Z",
  "next_sync_at": "2026-10-14T10:15:00Z",
  "successful_object_runs_count": 1248,
  "failed_object_runs_count": 3,
  "current_sync": {
    "started_at": "2026-10-14T10:00:05Z",
    "successful_object_runs_count": 4,
    "failed_object_runs_count": 0,
    "total_object_runs_count": 6
  },
  "last_sync": {
    "started_at": "2026-10-14T09:45:03Z",
    "completed_at": "2026-10-14T09:50:12Z",
    "successful_object_runs_count": 6,
    "failed_object_runs_count": 0,
    "total_object_runs_count": 6
  }
}
```

#### Response fields

The list, get, create, update, and clone endpoints return data pipeline objects with the following fields. Timestamps use ISO 8601 format. Some fields, such as timestamps and counts, can return `null`.

The list, get, and update endpoints also return the sync status fields (`last_synced_at`, `next_sync_at`, `successful_object_runs_count`, `failed_object_runs_count`, `current_sync`, and `last_sync`) when sync information is available. The create and clone endpoints don't return these fields.

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** | Data pipeline ID. |
| name | **string** | Pipeline name. |
| handle | **string** | Unique string identifier for the pipeline. |
| folder\_id | **integer** | ID of the folder that contains the pipeline. |
| user\_id | **integer** | ID of the user who owns the pipeline. |
| created\_at | **string** | Time the pipeline was created. |
| updated\_at | **string** | Time the pipeline was last updated. |
| source\_provider | **string** | Source provider name, such as `salesforce`. |
| source\_shared\_account\_id | **integer** | Source connection ID. |
| source\_config | **object** | Source configuration. |
| destination\_provider | **string** | Destination provider name, such as `snowflake`. |
| destination\_shared\_account\_id | **integer** | Destination connection ID. |
| destination\_config | **object** | Destination configuration. |
| running | **boolean** | Whether the pipeline is running. |
| last\_run\_at | **string** | Time of the most recent run. |
| stopped\_at | **string** | Time the pipeline was last stopped. |
| last\_synced\_at | **string** | Time of the most recent successful sync. |
| next\_sync\_at | **string** | Time of the next scheduled sync. |
| successful\_object\_runs\_count | **integer** | Number of successful object runs. |
| failed\_object\_runs\_count | **integer** | Number of failed object runs. |
| current\_sync | **object** | Statistics for the sync in progress. Returned only while a sync is running. Refer to [Sync statistics](#sync-statistics). |
| last\_sync | **object** | Statistics for the previous sync. Returned only if the pipeline has a previous sync. Refer to [Sync statistics](#sync-statistics). |

#### Sync statistics

The `current_sync` and `last_sync` objects contain the following fields:

| Name | Type | Description |
| --- | --- | --- |
| started\_at | **string** | Time the sync started. |
| completed\_at | **string** | Time the sync completed. Returned in `last_sync` only. |
| successful\_object\_runs\_count | **integer** | Number of successful object runs in the sync. |
| failed\_object\_runs\_count | **integer** | Number of failed object runs in the sync. |
| total\_object\_runs\_count | **integer** | Total number of object runs in the sync. |

Refer to [Pipeline runs](/en/data-orchestration/data-pipeline-recipe/concepts#pipeline-runs) for more information about syncs and object runs.

### Create a data pipeline

Creates a data pipeline with the source and destination you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/data_pipelines
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Pipeline name. |
| source\_provider | **string** _required_ | Source provider name, such as `salesforce`. Call [List source providers](#list-source-providers) to retrieve the available names. |
| source\_shared\_account\_id | **integer** _required_ | Source connection ID. |
| destination\_provider | **string** _required_ | Destination provider name, such as `snowflake`. Call [List destination providers](#list-destination-providers) to retrieve the available names. |
| destination\_shared\_account\_id | **integer** _required_ | Destination connection ID. |
| folder\_id | **integer** _optional_ | ID of the folder where Workato stores the pipeline. Defaults to the Home folder. |
| source\_config | **object** _optional_ | Source configuration. Call [Get configuration schema](#get-configuration-schema) to retrieve the available fields. |
| destination\_config | **object** _optional_ | Destination configuration. Call [Get configuration schema](#get-configuration-schema) to retrieve the available fields. |

You can retrieve connection IDs with the [List connections](/en/workato-api/connections#list-connections) endpoint.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/data_pipelines' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "folder_id": :folder_id,
            "source_provider": ":source_provider",
            "source_shared_account_id": :source_connection_id,
            "destination_provider": ":destination_provider",
            "destination_shared_account_id": :destination_connection_id
          }'
```

</api-code>

#### Sample response

Workato returns a `201 Created` status and the new [data pipeline object](#data-pipeline-response-fields). The response doesn't include sync status fields.

```json
{
  "id": 4821,
  "name": "Salesforce to Snowflake",
  "handle": "dpr-BcHkTq2x-x7Lp9Q-SM",
  "folder_id": 27180380,
  "user_id": 81234,
  "created_at": "2026-10-01T09:00:00Z",
  "updated_at": "2026-10-01T09:00:00Z",
  "source_provider": "salesforce",
  "source_shared_account_id": 10452,
  "source_config": {},
  "destination_provider": "snowflake",
  "destination_shared_account_id": 10453,
  "destination_config": {},
  "running": false,
  "last_run_at": null,
  "stopped_at": null
}
```

### Update a data pipeline

Updates the name, folder, or configuration of the data pipeline you specify.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline to update. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Pipeline name. |
| folder\_id | **integer** _optional_ | ID of the folder where Workato stores the pipeline. |
| source\_config | **object** _optional_ | Source configuration. Call [Get configuration schema](#get-configuration-schema) to retrieve the available fields. |
| destination\_config | **object** _optional_ | Destination configuration. Call [Get configuration schema](#get-configuration-schema) to retrieve the available fields. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "folder_id": :folder_id
          }'
```

</api-code>

#### Sample response

Workato returns the updated [data pipeline object](#data-pipeline-response-fields).

```json
{
  "id": 4821,
  "name": "Salesforce to Snowflake (production)",
  "handle": "dpr-BcHkTq2x-x7Lp9Q-SM",
  "folder_id": 27180395,
  "user_id": 81234,
  "created_at": "2026-10-01T09:00:00Z",
  "updated_at": "2026-10-14T11:30:00Z",
  "source_provider": "salesforce",
  "source_shared_account_id": 10452,
  "source_config": {},
  "destination_provider": "snowflake",
  "destination_shared_account_id": 10453,
  "destination_config": {},
  "running": false,
  "last_run_at": "2026-10-14T10:00:05Z",
  "stopped_at": "2026-10-14T11:00:00Z",
  "last_synced_at": "2026-10-14T10:05:40Z",
  "next_sync_at": null,
  "successful_object_runs_count": 1254,
  "failed_object_runs_count": 3,
  "last_sync": {
    "started_at": "2026-10-14T10:00:05Z",
    "completed_at": "2026-10-14T10:05:40Z",
    "successful_object_runs_count": 6,
    "failed_object_runs_count": 0,
    "total_object_runs_count": 6
  }
}
```

### Delete a data pipeline

Permanently deletes the data pipeline you specify. You can't undo this action.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline to delete. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "success": true
}
```

### Clone a data pipeline

Creates a copy of the data pipeline you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/clone
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline to clone. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/clone' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

Workato returns a `201 Created` status and the cloned [data pipeline object](#data-pipeline-response-fields). The response doesn't include sync status fields and uses the same format as [Create a data pipeline](#create-a-data-pipeline-sample-response).

### Start a data pipeline

Starts the data pipeline you specify so it begins processing data. Returns a `400` error if the pipeline can't be started.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/start
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline to start. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/start' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "success": true
}
```

### Stop a data pipeline

Stops the data pipeline you specify from processing data.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/stop
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline to stop. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/stop' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "success": true
}
```

## Pipeline configuration

Use the following endpoints to discover providers, objects, and fields, and to retrieve and validate pipeline configuration.

### List source providers

Returns the source providers available for data pipelines.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/data_pipelines/sources
```

</api-code>

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/data_pipelines/sources' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "items": [
    {
      "name": "snowflake",
      "connectionless": false
    },
    {
      "name": "salesforce",
      "connectionless": false
    }
  ]
}
```

#### Response fields

The list source providers and list destination providers endpoints return an `items` array. Each item contains the following fields:

| Name | Type | Description |
| --- | --- | --- |
| name | **string** | Provider name. Use this value as the `source_provider` or `destination_provider` when you [create a data pipeline](#create-a-data-pipeline). |
| connectionless | **boolean** | Whether the provider doesn't require a connection. |

### List destination providers

Returns the destination providers available for data pipelines. The response uses the same [fields](#provider-response-fields) as List source providers.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/data_pipelines/destinations
```

</api-code>

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/data_pipelines/destinations' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "items": [
    {
      "name": "snowflake",
      "connectionless": false
    },
    {
      "name": "postgresql",
      "connectionless": false
    }
  ]
}
```

### List source objects

Returns the objects available from the source connection you specify. Returns a `404` error if the connection doesn't exist.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/data_pipelines/source_objects
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| shared\_account\_id | **integer** _required_ | Source connection ID. |
| extension | **object** _optional_ | Provider-specific extension parameters. |
| filter | **string** _optional_ | Filter expression that limits the objects returned. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/data_pipelines/source_objects' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "shared_account_id": :source_connection_id
          }'
```

</api-code>

#### Sample response

```json
{
  "items": [
    {
      "name": "Account",
      "namespace": null,
      "label": "Account",
      "workato_type": "OBJECT"
    },
    {
      "name": "Contact",
      "namespace": null,
      "label": "Contact",
      "workato_type": "OBJECT"
    }
  ]
}
```

#### Response fields

The response contains an `items` array of objects available from the source connection. Each item contains the following fields:

| Name | Type | Description |
| --- | --- | --- |
| name | **string** | Object name. Pass this value as `object_name` to [List source object fields](#list-source-object-fields). |
| namespace | **string** | Object namespace, such as a database schema. Pass this value as `object_namespace` to [List source object fields](#list-source-object-fields). Can be `null`. |
| label | **string** | Object display label. |
| workato\_type | **string** | Workato type of the object, such as `OBJECT`. |
| extension | **object** | Provider-specific object extension. |
| supported\_sync\_modes | **array of strings** | Sync modes the object supports. |

### List source object fields

Returns the field schema for an object in the source connection you specify. Returns a `404` error if the connection or object doesn't exist.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/data_pipelines/source_object_fields
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| shared\_account\_id | **integer** _required_ | Source connection ID. |
| object\_name | **string** _required_ | Object name, such as `Account`. |
| object\_namespace | **string** _optional_ | Object namespace. Omit or set to `null` to use the default namespace. |
| extension | **object** _optional_ | Provider-specific extension parameters. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/data_pipelines/source_object_fields' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "shared_account_id": :source_connection_id,
            "object_name": ":object_name"
          }'
```

</api-code>

#### Sample response

```json
{
  "fields": [
    {
      "name": "Id",
      "label": "Account ID",
      "type": "STRING",
      "workato_type": "STRING",
      "primary_key": true,
      "cursor_field": false,
      "is_deleted_field": false,
      "masking_available": false,
      "must_sync": true,
      "eligible_for": ["PK"]
    },
    {
      "name": "Name",
      "label": "Account Name",
      "type": "STRING",
      "workato_type": "STRING",
      "primary_key": false,
      "cursor_field": false,
      "is_deleted_field": false,
      "masking_available": true,
      "must_sync": false,
      "eligible_for": []
    }
  ],
  "supported_sync_modes": ["FULL", "INCREMENTAL"]
}
```

#### Response fields

| Name | Type | Description |
| --- | --- | --- |
| fields | **array of objects** | Field descriptors for the object. Refer to [Field descriptors](#field-descriptors). |
| supported\_sync\_modes | **array of strings** | Sync modes the object supports. Can be `null`. |
| supported\_sync\_strategies | **object** | Sync strategies for each supported sync mode, keyed by mode. Each strategy includes a `name` and a `label`. Can be `null`. |

#### Field descriptors

Each item in the `fields` array contains the following fields:

| Name | Type | Description |
| --- | --- | --- |
| name | **string** | Field name. |
| label | **string** | Field display label. |
| type | **string** | Field type. |
| workato\_type | **string** | Workato type of the field. |
| primary\_key | **boolean** | Whether the field is part of the primary key. |
| cursor\_field | **boolean** | Whether the field is a cursor field. |
| is\_deleted\_field | **boolean** | Whether the field marks deleted records. |
| masking\_available | **boolean** | Whether the field can be masked. |
| must\_sync | **boolean** | Whether the field is synced by default. |
| eligible\_for | **array of strings** | Roles the field can play. Empty if the source doesn't report any. |

### Get configuration schema

Returns the configuration schema, default values, and validation errors for the source, destination, or object settings of a data pipeline. Include your configuration values in the `input` field to validate them before you update or start the pipeline. Returns a `404` error if the pipeline or connection doesn't exist.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/configuration
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| type | **string** _required_ | The configuration to evaluate. Accepted values: `sources`, `destinations`, `object_settings`. |
| shared\_account\_id | **integer** _required_ | ID of the connection to evaluate the schema against. |
| object\_name | **string** _optional_ | Object name for object-level schema evaluation. |
| object\_namespace | **string** _optional_ | Object namespace. |
| object\_extension | **object** _optional_ | Provider-specific extension parameters for the object. |
| supported\_sync\_modes | **array of strings** _optional_ | Sync modes the object supports. |
| input | **object** _optional_ | Current configuration values. Workato evaluates dynamic fields against these values and returns any validation errors in the `errors` field. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/configuration' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "type": "sources",
            "shared_account_id": :source_connection_id,
            "object_name": ":object_name"
          }'
```

</api-code>

#### Sample response

The available configuration fields vary by provider. The following example shows a source with one required field that's missing from `input`:

```json
{
  "schema": [
    {
      "item_type": "schema-field",
      "name": "mode",
      "label": "Mode",
      "type": "string",
      "control_type": "select",
      "default": "simple",
      "options": [
        ["Simple", "simple"],
        ["Advanced", "advanced"]
      ],
      "extends_schema": true
    },
    {
      "item_type": "schema-field",
      "name": "required_field",
      "label": "Required field",
      "type": "string",
      "validation_problems": [
        {
          "type": "error",
          "message": "can't be blank"
        }
      ]
    }
  ],
  "default_input": {
    "mode": "simple"
  },
  "errors": {
    "source_config": [
      {
        "field": "required_field",
        "message": "can't be blank",
        "severity": "error"
      }
    ]
  }
}
```

#### Response fields

| Name | Type | Description |
| --- | --- | --- |
| schema | **array of objects** | Configuration items. Use `item_type` to tell them apart. A `schema-field` item is a configuration field. Other values, such as `object-field`, `message`, `help`, and `separator`, are structural or display items with different attributes. A `schema-field` includes `name`, `label`, and `type`, and can include attributes such as `control_type`, `default`, `options`, `hint`, `optional`, `read_only`, and `validation_problems`. |
| default\_input | **object** | Default value for each configuration field, keyed by field `name`. |
| errors | **object** | Validation errors for the values in `input`. Keyed by `destination_config` when `type` is `destinations`, and by `source_config` when `type` is `sources` or `object_settings`. Each key contains an array of errors. Each error includes a `field` with the path of the configuration field, or `objects` for object-level problems, a `message`, and a `severity` of `error` or `warning`. Field-level errors also include `object_name` when the request includes `object_name`. |

## Objects and runs

Use the following endpoints to monitor object sync status and run history, and to re-sync objects. Refer to [Monitor and manage data pipelines](/en/data-orchestration/data-pipeline-recipe/monitor) for more information about objects and runs.

### List pipeline objects

Returns the objects configured in the data pipeline you specify and their sync status.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/objects
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| limit | **integer** _optional_ | Number of objects to return per page. Defaults to `50`. Workato adjusts values outside the range of `1` to `1000` to the nearest limit. |
| offset | **integer** _optional_ | Number of objects to skip before Workato returns results. |
| sort\_by | **string** _optional_ | Field to sort results by, such as `object_label` or `run_last_state`. |
| object\_label | **string** _optional_ | Returns objects with the display label you specify. |
| run\_last\_state | **string** _optional_ | Returns objects whose most recent run has the state you specify. Refer to the `run_last_state` [response field](#list-pipeline-objects-response-fields) for possible values. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/objects?limit=:limit&offset=:offset' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "items": [
    {
      "object_namespace": null,
      "object_name": "Account",
      "object_label": "Accounts",
      "run_last_state": "synced",
      "updated_at": "2026-10-14T10:02:31Z",
      "resync_requested": false
    },
    {
      "object_namespace": null,
      "object_name": "Contact",
      "object_label": "Contacts",
      "run_last_state": "failed",
      "updated_at": "2026-10-14T10:03:12Z",
      "resync_requested": true
    }
  ]
}
```

#### Response fields

| Name | Type | Description |
| --- | --- | --- |
| object\_namespace | **string** | Object namespace. Returns `null` if the object has no namespace. |
| object\_name | **string** | Object name. |
| object\_label | **string** | Object display label. |
| run\_last\_state | **string** | State of the most recent run for the object. Possible values: `synced`, `failed`, `initial_syncing`, `syncing`, `resyncing`, `queued`, `not_synced_yet`, `cancelled`, `unknown`. |
| updated\_at | **string** | Time the object was last updated, in ISO 8601 format. |
| resync\_requested | **boolean** | Whether a re-sync is requested for the object. |

### Re-sync objects

Triggers a complete re-sync of data from the source for the objects you specify. Returns a `400` error if Workato can't start the re-sync. Refer to [Object syncs](/en/data-orchestration/data-pipeline-recipe/concepts#object-syncs) for more information.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/resync
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| objects | **array of objects** _required_ | The objects to re-sync. Use the `object_name` and `object_namespace` values from [List pipeline objects](#list-pipeline-objects). Each object contains the following fields: `name` (**string**, _required_): Object name. `namespace` (**string**, _optional_): Object namespace. Set to `null` to use the default namespace. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/resync' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "objects": [
              {
                "name": ":object_name",
                "namespace": ":object_namespace"
              }
            ]
          }'
```

</api-code>

#### Sample response

```json
{
  "success": true
}
```

### List pipeline runs

Returns the object runs for the data pipeline you specify. Each sync contains one run per object. The response includes only runs from the last 30 days.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/runs
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| object\_name | **string** _optional_ | Returns runs for the object you specify. |
| object\_namespace | **string** _optional_ | Returns runs for objects in the namespace you specify. Omit to return runs for all namespaces. |
| limit | **integer** _optional_ | Number of runs to return per page. Defaults to `25`. Maximum is `100`. |
| offset\_object\_run\_id | **string** _optional_ | Pagination cursor. Set this value to the `next_page_cursor` from the previous response to fetch the next page. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/runs?object_name=:object_name&limit=:limit' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "items": [
    {
      "id": "run-124",
      "object_namespace": null,
      "object_name": "Account",
      "state": "SUCCEEDED",
      "created_at": "2026-10-14T10:00:00Z",
      "started_at": "2026-10-14T10:00:05Z",
      "completed_at": "2026-10-14T10:02:31Z",
      "updated_at": "2026-10-14T10:02:31Z",
      "loaded_count": 120,
      "updated_count": 95,
      "inserted_count": 25,
      "extracted_count": 120,
      "run_type": "INCREMENTAL",
      "sync_type2": "REGULAR"
    },
    {
      "id": "run-123",
      "object_namespace": null,
      "object_name": "Account",
      "state": "SUCCEEDED",
      "created_at": "2026-10-14T09:45:00Z",
      "started_at": "2026-10-14T09:45:03Z",
      "completed_at": "2026-10-14T09:47:40Z",
      "updated_at": "2026-10-14T09:47:40Z",
      "loaded_count": 500,
      "updated_count": 100,
      "inserted_count": 400,
      "extracted_count": 500,
      "run_type": "INCREMENTAL",
      "sync_type2": "REGULAR"
    }
  ],
  "next_page_cursor": "run-123",
  "has_more_pages": true
}
```

#### Response fields

| Name | Type | Description |
| --- | --- | --- |
| items | **array of objects** | Object runs. Refer to [Run fields](#run-fields) for field descriptions. |
| next\_page\_cursor | **string** | ID of the last run in the response. Pass this value as `offset_object_run_id` to fetch the next page. Returns `null` when there are no more pages. |
| has\_more\_pages | **boolean** | Whether more pages are available. |

### Get a pipeline run

Returns the details of the object run you specify. Workato retrieves runs from the last 30 days only. Returns a `400` error if the run doesn't exist or is older than that.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/runs/:run_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_pipeline\_id | **integer** _required_ | The ID of the data pipeline. |
| run\_id | **string** _required_ | The ID of the run. You can retrieve run IDs with the [List pipeline runs](#list-pipeline-runs) endpoint. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/data_pipelines/:data_pipeline_id/runs/:run_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "id": "run-124",
  "object_namespace": null,
  "object_name": "Account",
  "state": "SUCCEEDED",
  "created_at": "2026-10-14T10:00:00Z",
  "started_at": "2026-10-14T10:00:05Z",
  "completed_at": "2026-10-14T10:02:31Z",
  "updated_at": "2026-10-14T10:02:31Z",
  "loaded_count": 120,
  "updated_count": 95,
  "inserted_count": 25,
  "extracted_count": 120,
  "run_type": "INCREMENTAL",
  "sync_type2": "REGULAR"
}
```

#### Run fields

Timestamps use ISO 8601 format. `object_namespace`, `started_at`, `completed_at`, and `updated_at` can return `null`. Use `run_type` and `sync_type2` together to determine the sync type of a run. Refer to [Sync types](/en/data-orchestration/sync-types) for more information.

| Name | Type | Description |
| --- | --- | --- |
| id | **string** | Run ID. |
| object\_namespace | **string** | Namespace of the object the run processed. |
| object\_name | **string** | Name of the object the run processed. |
| state | **string** | Run state, such as `STARTED`, `SUCCEEDED`, `FAILED`, or `CANCELLED`. |
| created\_at | **string** | Time the run was created. |
| started\_at | **string** | Time the run started. |
| completed\_at | **string** | Time the run completed. |
| updated\_at | **string** | Time the run was last updated. |
| loaded\_count | **integer** | Number of records loaded into the destination. |
| updated\_count | **integer** | Number of records updated. |
| inserted\_count | **integer** | Number of records inserted. |
| extracted\_count | **integer** | Number of records extracted from the source. |
| run\_type | **string** | Run type, such as `FULL` for a [full sync](/en/data-orchestration/sync-types#full-sync) or `INCREMENTAL` for an [incremental sync](/en/data-orchestration/sync-types#incremental-sync-cdc). |
| sync\_type2 | **string** | Sync type of the run, such as `REGULAR` for a run in a scheduled sync or `RESYNC` for an [object re-sync](/en/data-orchestration/sync-types#object-re-sync). |
| run\_error | **object** | Error details for a failed run. Returned only when the run has an error. Contains a `message` string and a `code` string that identifies the error type. |

---
