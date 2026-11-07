---
url: 'https://docs.workato.com/en/oem/oem-api/data-tables.md'
description: >-
  Reference for the Embedded API data tables resource to list, create, update,
  and delete data tables and their records in customer workspaces.
---

# Embedded API - Data tables

Refer to the following sections to programmatically manage [data tables](/en/data-tables) and their records using APIs:

- [Table management APIs](#table-management-apis)
- [Record manipulation APIs](#record-manipulation-apis)
- [Record import APIs](#record-import-apis)

> **FEATURE AVAILABILITY**
> 
> The Data Table APIs are currently accessible only to workspaces participating in Workato's Data Tables beta program. For more information, contact your customer success representative.

## Rate limits

Data table resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Data tables](/en/oem/oem-api/data-tables.html) endpoints | 60 requests per minute |

## Data center base URLs

Each data center (DC) has a dedicated base URL. Use the base URL that matches your workspace region. Select your data center in a sample request to substitute the matching base URL.

The following example shows the `data-tables` base URL modified for each data center:

| Data center | Base URL |
| --- | --- |
| US | `https://data-tables.workato.com` |
| EU | `https://data-tables.eu.workato.com` |
| JP | `https://data-tables.jp.workato.com` |
| SG | `https://data-tables.sg.workato.com` |
| AU | `https://data-tables.au.workato.com` |
| IL | `https://data-tables.il.workato.com` |
| CN | `https://data-tables.workatoapp.cn` |
| KR | `https://data-tables.kr.workato.com` |
| UK | `https://data-tables.uk.workato.com` |
| Trial | `https://data-tables.trial.workato.com` |

Workato returns a `403 Forbidden` error if you call an endpoint that doesn't match your workspace data center.

## Table management APIs

Use the endpoints below to manage and structure data tables in customer workspaces.

**Base URL**:

<api-code>

```
https://YOUR_DATA_CENTER/api
```

</api-code>

> **REGIONAL BASE URLS**
> 
> You must use the dedicated base URL that matches your workspace region. Refer to [Data center URLs](#data-center-urls) for more information.

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/data\_tables](/en/oem/oem-api/data-tables#list-data-tables) | List all data tables. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id](/en/oem/oem-api/data-tables#get-data-table-by-id) | Get data table by ID. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/data\_tables](/en/oem/oem-api/data-tables#create-data-table) | Creates a data table. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id](/en/oem/oem-api/data-tables#update-data-table) | Updates a data table. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id](/en/oem/oem-api/data-tables#delete-data-table) | Deletes a data table. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id/truncate](/en/oem/oem-api/data-tables#truncate-data-table) | Truncates a data table. |

### List data tables in a customer workspace

Returns a list of all data tables in a customer's workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number of the data tables to fetch. Defaults to 1. |
| per\_page | **integer** _optional_ | Page size. Defaults to 100. Maximum is 100. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables'
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
    "data": [
        {
            "id": "cafd30b6-23e1-4a73-9fa6-68fc18356db4",
            "name": "drtdr",
            "schema": [],
            "folder_id": 25178157,
            "created_at": "2025-05-23T13:14:11.397-07:00",
            "updated_at": "2025-05-23T13:14:11.397-07:00"
        }
    ]
}
```

### Get data table by ID

Retrieves a data table in a customer workspace using the data table's ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table you plan to retrieve. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id'
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
    "data": {
        "id": "cafd30b6-23e1-4a73-9fa6-68fc18356db4",
        "name": "drtdr",
        "schema": [],
        "folder_id": 25178157,
        "created_at": "2025-05-23T13:14:11.397-07:00",
        "updated_at": "2025-05-23T13:14:11.397-07:00"
    }
}
```

#### Record import status

The response also includes a `records_import_status` object while a [record import](#record-import-apis) is in progress, and for up to 24 hours after it completes or until it's [dismissed](#dismiss-import). Automated pipelines can use this object to detect a failed import:

| Name | Type | Description |
| --- | --- | --- |
| filename | **string** | The file name provided when starting the import. |
| total\_bytes | **integer** | The total size of the file in bytes. |
| total\_records | **integer** | The total number of records in the file. |
| status | **string** | The import status, such as `in_progress`, `completed`, or `failed`. |
| processed\_records | **integer** | The number of records processed so far. |
| eta | **string** | The estimated time of completion. Present when `status` is `in_progress`. |
| completed\_at | **string** | The time the import completed. Present when `status` is `completed`. |
| failed\_at | **string** | The time the import failed. Present when `status` is `failed`. |
| is\_internal\_error | **boolean** | Indicates whether a failure is due to an internal Workato error rather than an error in the imported data. Present when `status` is `failed`. |
| error | **string** | A human-readable description of the failure. Present when `status` is `failed`. |
| error\_record\_idx | **integer** | The 0-based index of the record that caused the failure. Present when `status` is `failed`. |
| error\_details | **object** | Contains details about the failure. Present when `status` is `failed`. Refer to [Error codes](#import-error-codes) for the possible values. |

The following example shows a completed import:

```json
{
  "data": {
    "records_import_status": {
      "filename": "bank_report.csv",
      "total_bytes": 3005,
      "total_records": 18,
      "status": "completed",
      "processed_records": 18,
      "completed_at": "2026-07-09T17:44:42.877+00:00"
    }
  }
}
```

##### Error codes

The response contains an `error_details` object when `status` is `failed`, which contains an `error_code` field with one of the following values:

| Error code | Additional fields | Description |
| --- | --- | --- |
| `MAX_TABLE_SIZE_EXCEEDED` | `max_table_size_bytes` | The import would exceed the maximum table size. |
| `MAX_NUM_RECORDS_EXCEEDED` | `max_num_records` | The import would exceed the maximum number of records per table. |
| `MAX_DOCUMENT_SIZE_EXCEEDED` | `max_document_size_bytes` | A record would exceed the maximum record size. |
| `TEXT_VALUE_TOO_LONG` | `field_id`, `field_name`, `max_text_value_chars` | A text value exceeds the maximum number of characters allowed for the field. |

> **LIMITS**
> 
> Refer to [Data tables - Quotas](/en/data-tables/data-table-limits) for the size and record quotas that apply to imports.

Failed import example

The import failed in the following example because a text value exceeds the maximum number of characters allowed for the `description` field:

```json
{
  "data": {
    "records_import_status": {
      "filename": "bank_report.csv",
      "total_bytes": 15295,
      "total_records": 1,
      "status": "failed",
      "processed_records": 0,
      "failed_at": "2026-07-13T17:05:10.565+00:00",
      "is_internal_error": false,
      "error": "value in field \"description\": text is too long (15000 characters, max allowed: 10000)",
      "error_record_idx": 0,
      "error_details": {
        "error_code": "TEXT_VALUE_TOO_LONG",
        "field_id": "4b01d22e-b888-4d1d-b90c-7c78ad75424d",
        "field_name": "description",
        "max_text_value_chars": 10000
      }
    }
  }
}
```

### Create data table

Creates a data table in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the data table to create. |
| folder\_id | **number** _required_ | Provide the ID of the folder where you plan to create the data table. |
| schema | **array** _required_ | Supply an array of nested elements to define your table structure. You must supply the column name, data type, and whether the column is required. |
| schema\[type\] | **boolean**, **date**, **date\_time**, **integer**, **number**, **string**, **file**, **relation** _required_ | The data type of the column you plan to create. |
| schema\[name\] | **string** _required_ | The name of the column you plan to create. |
| schema\[optional\] | **integer**, **boolean** _required_ | Indicates if the column is required or optional. Must be either `true`, `false`, `1`, or `0`. |
| schema\[field\_id\] | Must match regular expression: `/\h{8}-\h{4}-\h{4}-\h{4}-\h{12}/` _optional_ | Unique Universal Identifier (UUID) of the column. Must follow this format: `f47ac10b-58cc-4372-a567-0e02b2c3d479`. |
| schema\[hint\] | **string** _optional_ | Provide a hint to help your end users populate entries in a data column. The hint displays as a tooltip when you hover over the column in the user interface. |
| schema\[default\_value\] | **variable** _optional_ | The default value of the column. Must match the data type of the column specified in the request. |
| schema\[metadata\] | **hash** _optional_ | Data table metadata. |
| schema\[relation\] | **hash** _optional_ | Indicates that this table links to another data table. |
| schema\[relation\]\[table\_id\] | **string** _optional_ | The ID of the data table linked to this table. |
| schema\[relation\]\[field\_id\] | **string** _required_ | The column ID of a linked data table. |
| schema\[multivalue\] | **boolean** _optional_ | Indicates whether the column accepts multi-value input. |
|  |  |  |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables'
      -H 'Authorization: Bearer <api_token>'
      -H 'Content-Type: application/json' \
   -d '{
            "name": ":name",
            "folder_id": :folder_id_value,
            "schema": [
                {
                    "type": ":type",
                    "name": ":schema_name",
                    "optional": :true_or_false,
                    "multivalue": :true_or_false
                }
            ]
        }'
```

</api-code>

#### Response

```json
{
    "data": {
        "id": "dcb981cf-3e5e-4b79-ab78-1fe0115bc5e8",
        "name": "Resume screening",
        "schema": [
            {
                "type": "string",
                "name": "Applicant name",
                "optional": false,
                "field_id": "9b213e57-2ff9-4276-a65f-5afaa14789fd",
                "default_value": [],
                "metadata": {},
                "multivalue": true
            },
            {
                "type": "date",
                "name": "Application date",
                "optional": true,
                "field_id": "3e1c6061-ff84-47e9-80ac-145aff0f6206",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "boolean",
                "name": "Review status",
                "optional": true,
                "field_id": "e3106d74-bd0b-47a6-a936-8b7a03fd9fee",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "date_time",
                "name": "Interview time",
                "optional": true,
                "field_id": "0adb665a-8579-4cc2-a46d-8f43be7fbdbb",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "file",
                "name": "Resume",
                "optional": true,
                "field_id": "e300122c-dbd8-45f3-91fd-1bb060c92b95",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "integer",
                "name": "Years of experience",
                "optional": true,
                "field_id": "4763bde7-c46b-48d7-bc5f-cbb0e3132646",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "number",
                "name": "Salary expectation",
                "optional": true,
                "field_id": "0778952c-ce6e-4f7b-9bd1-c265a9e98702",
                "metadata": {},
                "multivalue": false
            }
        ],
        "folder_id": 25178157,
        "created_at": "2025-05-27T11:49:06.226-07:00",
        "updated_at": "2025-05-27T11:49:06.226-07:00"
    }
}
```

### Update data table

Updates a data table you specify.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table you plan to update. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The updated name of the data table. |
| folder\_id | **number** _optional_ | Provide the ID of the folder where you plan to move the data table. |
| schema | **array** _optional_ | Supply an array of nested elements to modify your table structure. You must supply the column name, data type, and whether the column is required. |
| schema\[type\] | **boolean**, **date**, **date\_time**, **integer**, **number**, **string**, **file**, **relation** _required_ | The data type of the column you plan to update. |
| schema\[name\] | **string** _required_ | The name of the column you plan to update. |
| schema\[optional\] | **integer**, **boolean** _required_ | Indicates if the column is required or optional. Must be either `true`, `false`, `1`, or `0`. |
| schema\[field\_id\] | Must match regular expression: `/\h{8}-\h{4}-\h{4}-\h{4}-\h{12}/` _optional_ | Unique Universal Identifier (UUID) of the column. Must follow this format: `f47ac10b-58cc-4372-a567-0e02b2c3d479`. |
| schema\[hint\] | **string** _optional_ | Provide a hint to help your end users populate entries in a data column. The hint displays as a tooltip when you hover over the column in the user interface. |
| schema\[default\_value\] | **variable** _optional_ | The default value of the column. Must match the data type of the column specified in the request. |
| schema\[metadata\] | **hash** _optional_ | Data table metadata. |
| schema\[relation\] | **hash** _optional_ | Indicates that this table links to another data table. |
| schema\[relation\]\[table\_id\] | **string** _optional_ | The ID of the data table linked to this table. |
| schema\[relation\]\[field\_id\] | **string** _required_ | The column ID of a linked data table. |
| schema\[multivalue\] | **boolean** _optional_ | Indicates whether the column accepts multi-value input. |
|  |  |  |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id'
      -H 'Authorization: Bearer <api_token>'
      -H 'Content-Type: application/json' \
   -d '{
            "name": ":name",
            "folder_id": :folder_id_value,
            "schema": [
                {
                    "type": ":type",
                    "name": ":schema_name",
                    "optional": :true_or_false,
                    "multivalue": :true_or_false
                }
            ]
        }'
```

</api-code>

#### Response

```json
{
    "data": {
        "id": "dcb981cf-3e5e-4b79-ab78-1fe0115bc5e8",
        "name": "Resume screening",
        "schema": [
            {
                "type": "string",
                "name": "Applicant name",
                "optional": false,
                "field_id": "c0eee384-9967-47da-b8b3-b5faa4654df8",
                "default_value": [],
                "metadata": {},
                "multivalue": true
            },
            {
                "type": "date",
                "name": "Potential start date",
                "optional": true,
                "field_id": "2c623992-ac87-4560-931e-0b3b58b3016f",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "boolean",
                "name": "Remote worker",
                "optional": true,
                "field_id": "ac4e7e53-a157-42b8-85f7-e4a2042b42c2",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "date_time",
                "name": "Interview time",
                "optional": true,
                "field_id": "749eaef4-a714-4c6a-b65e-641bf88dc11b",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "file",
                "name": "Resume",
                "optional": true,
                "field_id": "0e36fa59-1d80-475c-a83f-4f47562a641d",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "integer",
                "name": "Miles from office",
                "optional": true,
                "field_id": "e098f6ca-5165-4c54-9ff1-02d72fe91d13",
                "metadata": {},
                "multivalue": false
            },
            {
                "type": "number",
                "name": "Interviews completed",
                "optional": true,
                "field_id": "f9e5af87-57c9-4611-befb-4f43fface977",
                "metadata": {},
                "multivalue": false
            }
        ],
        "folder_id": 25178157,
        "created_at": "2025-05-27T11:49:06.226-07:00",
        "updated_at": "2025-05-27T11:49:06.226-07:00"
    }
}
```

### Delete data table

Deletes a data table in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table you plan to delete. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id'
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
    "data": {
        "status": "success"
    }
}
```

### Truncate data table

Truncates a data table you specify. Truncating a data table deletes all data from a data table, but doesn't affect the table structure.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id/truncate
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table you plan to truncate. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/data_tables/:data_table_id/truncate'
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
    "data": {
        "status": "success"
    }
}
```

## Record manipulation APIs

You can use the following endpoints to create, delete, and update data table records in customer workspaces. Refer to the OpenAPI specification at `/api/v1/openapi.json` on the [base URL](#data-center-urls) for your data center.

**Base URL**:

<api-code>

```
https://YOUR_DATA_TABLES_DC/api
```

</api-code>

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/query](#query-records) | Queries records using filters you specify. |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records](#create-record) | Creates a new record. |
| PUT | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/:record\_id](#update-record) | Updates an existing record. |
| DELETE | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/:record\_id](#delete-record) | Deletes a record you specify. |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/fields/:field\_id/file](#generate-link-to-upload-file) | Generates a link to upload a file. |
| GET | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/:record\_id/fields/:field\_id/file](#download-file-from-the-record) | Generates a link to download a file. |

### Query records

Queries records in a data table based on filters you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/query
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| data\_table\_id | **string** _required_ | The ID of the data table you plan to query. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| select | **array** _optional_ | Provide the list of columns to be retrieved from the data table. |
| where | **hash** _optional_ | Set of conditions to filter the records with. Refer to the [where clause](#where-field-structure) section for more information. |
| order | **string** or **hash** _optional_ | The column to order the results with. Provide either a **string**, or a **hash** for more advanced ordering configuration. Detailed breakdown of the **hash** structure can be found below. |
| timezone\_offset\_secs | **integer** _optional_ | The time zone offset for query. Required if the query includes comparison of a date-time field to a date value. |
| limit | **integer** _optional_ | Limits the number of records to return per page. The maximum is 200. |
| continuation\_token | **string** _optional_ | Provide the next page token from previous page's request to fetch the next set of results of the same query. |

> **INFO**
> 
> The following meta-fields can be used in `order` parameters with the fields you created: `$record_id`, `$created_at`, and `$updated_at`.

##### `where` field structure

A basic `where` clause uses the following format:

```text
{ <field>: { <operator>: <value> } }
```

You can set the `<value>` to a primitive value or an object.

**Primitive value**

Primitive values use the following syntax:

| Value type | Syntax |
| --- | --- |
| Null | `null` |
| Integer | `123` |
| Float | `1.23` |
| String | `"Josh"` |
| Boolean | `true` or `false` |
| Date (YYYY-MM-DD) | `"2001-01-01"` |
| Datetime (ISO 8601) | `"2024-06-10T12:00:00Z"` |
| File reference | `"file.txt"` |
| Record relation ID | `"05a53bd2-9ccb-4a45-b00c-67cfc05240c1"` |
| Multivalue array | `["abc", "def"]` |

For example:

```json
{
  "where": {
    "Name": { "$eq": "Josh" },
    "Room Number": { "$eq": 123 },
    "Check-in Date": { "$gt": "2025-01-01" }
  }
}
```

**Object**

Objects use the following syntax:

```json
{ "value": <value_1>, "case_sensitive": <value_2> }
```

For example:

```json
{
  "where": {
    "Name": {
      "$eq": {
        "value": "Josh",
        "case_sensitive": true
      }
    }
  }
}
```

The following table lists available `operator` values:

| Operator | Description | Example |
| --- | --- | --- |
| `$eq` | Equal | `{ "name": { "$eq": "Josh" } }` |
| `$ne` | Not equal | `{ "status": { "$ne": "inactive" } }` |
| `$gte` | Greater than or equal to | `{ "score": { "$gte": 75 } }` |
| `$gt` | Greater than | `{ "score": { "$gt": 90 } }` |
| `$lte` | Less than or equal to | `{ "amount": { "$lte": 13 } }` |
| `$lt` | Less than | `{ "amount": { "$lt": 10 } }` |
| `$in` | In (returns records where value matches any of the items in the `<value>`) | `{ "name": { "$in": ["Josh", "Bob", "Alice"] } }` |
| `$starts_with` | Starts with | `{ "email": { "$starts_with": "admin@" } }` |

###### Compound conditions

You can combine multiple conditions with `$and` compound operator using the format `{ "$and": [ <condition1>, <condition2>, ... ] }`. For example:

```json
{
  "$and": [
    {
      "name": "Josh"
    },
    {
      "id": {
        "$lte": 13
      }
    }
  ]
}
```

Alternatively, you can use the equivalent short-hand notation for the `$and` operator. For example:

```json
{
  "name": "Josh",
  "id": { "$lte": 13 }
}
```

##### `order` field hash structure

You must use the following structure when you provide a **hash** for the `order` field:

```json
{
  "by": <field>,
  "direction": "asc" | "desc",
  "case_sensitive": true | false
}
```

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/query' \
   -H 'Authorization: Bearer <api_token>' \
   -H 'Content-Type: application/json' \
   -d '{
            "select": [":select_column_1", ":select_column_2"],
            "where":
                {
                    ":where_field_1": { "$gt": :where_value_1 },
                    ":where_field_2": ":where_value_2"
                },
            "order": ":order",
            "limit": :limit_value,
            "timezone_offset_secs": :timezone_offset_secs_value
        }'
```

</api-code>

#### Response

```json
{
  "schema": [
    [ // Metafields
      { "name": "$record_id" },
      { "name": "$created_at" },
      { "name": "$updated_at" }
    ],
    [ // Fields
      { "name": "Name", "id": "2507a39a-6847-4857-88ed-c3b9c8302e02" },
      { "name": "Address", "id": "4705a22b-9139-6482-332a-ca2dd2d03sd3" },
      ...
    ]
  ],
  "data": [
    [ // Record 1
      [ // Metafields
        "e9498300-1ea3-4bf0-bdea-ffe58c101bcf",
        "2025-08-19T17:53:48.073+00:00",
        "2025-08-19T17:53:48.073+00:00"
      ],
      [ // Fields
        "Ann-Marie Tan",
        "5 Pennsylvania Ave. S320123"
      ]
    ],
    [ // Record 2
      [ // Metafields
        "900454f4-5b3d-4670-bc3c-d640915156f2",
        "2025-08-19T17:53:48.073+00:00",
        "2025-08-19T17:53:48.073+00:00"
      ],
      [ // Fields
        "John Paul Lim",
        "8 Somapah Road S210492"
      ]
    ],
    ...
  ],
  "count": 2,
  "limit": 10
}
```

### Create record

Creates a record in a specified data table.

<api-code no-copy-method>

```
POST https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| data\_table\_id | **string** _required_ | The ID of the data table where you plan to create the record. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |

#### Payload

The structure of the request payload is a key-value pair of each field. You can specify fields by their UUIDs (dollar-escaped) or names. Fields not listed in the schema are replaced with default values. Extra fields that aren't included in the schema are ignored.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records' \
   -H 'Authorization: Bearer <api_token>' \
   -H 'Content-Type: application/json' \
   -d '{
            "document":
            {
                ":field_name_1": ":field_value_1",
                ":field_name_2": :field_value_2,
                ":$field_id_uuid": :field_value_3,
                ":field_name_date": ":field_value_date",
                ":field_name_relation":
                    {
                        "record_id": ":record_id"
                    },
                ":field_name_file":
                    {
                        "filename": ":filename",
                        "upload_id": ":upload_id"
                    }
            }
        }'
```

</api-code>

#### Response

```json
{
    "data": {
        "record_id": "ab0189ca-fadf-4382-a48b-e157d966078f",
        "created_at": "2025-07-10T15:55:02.661+00:00",
        "updated_at": "2025-07-10T15:55:02.661+00:00",
        "document": [
            {
                "field_id": "42d62e3b-895d-43db-b8f7-cbb62dac71dd",
                "field_name": "name",
                "value": "Josh"
            },
            {
                "field_id": "2dca773b-eb67-4201-924d-4ccb9d577e99",
                "field_name": "multivalue",
                "value": [1,2,3]
            },
            {
                "field_id": "28c00d59-7dbe-4134-85be-937513500500",
                "field_name": "age",
                "value": 13
            },
            {
                "field_id": "0489bb65-7072-404f-9bba-e3e94a2a527b",
                "field_name": "date",
                "value": "2022-02-01"
            },
            {
                "field_id": "d6f103d9-575f-41b9-9ef0-b70e8fe38cc8",
                "field_name": "relation",
                "value": {
                    "record_id": "7a13304c-14cf-4e98-be31-331ccdb2b253",
                    "value": "Parent"
                }
            },
            {
                "field_id": "f71f1f67-0de5-422c-be73-b27b12f442c4",
                "field_name": "file",
                "value": {
                    "filename": "birth_certificate.txt"
                }
            }
        ]
    }
}
```

### Update record

Updates a record in a specified data table.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/:record_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| data\_table\_id | **string** _required_ | The ID of the data table where the record resides. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| record\_id | **string** _required_ | The ID of the record to be updated. |

#### Payload

The structure of the request payload is a key-value pair of each field. You can specify fields by their UUIDs (dollar-escaped) or names. Fields not listed in the schema aren't updated. Extra fields that aren't included in the schema are ignored.

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/:record_id' \
   -H 'Authorization: Bearer <api_token>' \
   -H 'Content-Type: application/json' \
   -d '{
            "document":
            {
                ":field_name_1": ":field_value_1",
                ":field_name_2": :field_value_2,
                ":$field_id_uuid": :field_value_3,
                ":field_name_date": ":field_value_date",
                ":field_name_relation":
                    {
                        "record_id": ":record_id"
                    },
                ":field_name_file":
                    {
                        "filename": ":filename",
                        "upload_id": ":upload_id"
                    }
            }
        }'
```

</api-code>

#### Response

```json
{
    "data": {
        "record_id": "ab0189ca-fadf-4382-a48b-e157d966078f",
        "created_at": "2025-07-10T15:55:02.661+00:00",
        "updated_at": "2025-07-10T15:55:02.661+00:00",
        "document": [
            {
                "field_id": "42d62e3b-895d-43db-b8f7-cbb62dac71dd",
                "field_name": "name",
                "value": "Josh"
            },
            {
                "field_id": "2dca773b-eb67-4201-924d-4ccb9d577e99",
                "field_name": "multivalue",
                "value": [1,2,3]
            },
            {
                "field_id": "28c00d59-7dbe-4134-85be-937513500500",
                "field_name": "age",
                "value": 13
            },
            {
                "field_id": "0489bb65-7072-404f-9bba-e3e94a2a527b",
                "field_name": "date",
                "value": "2022-02-01"
            },
            {
                "field_id": "d6f103d9-575f-41b9-9ef0-b70e8fe38cc8",
                "field_name": "relation",
                "value": {
                    "record_id": "7a13304c-14cf-4e98-be31-331ccdb2b253",
                    "value": "Parent"
                }
            },
            {
                "field_id": "f71f1f67-0de5-422c-be73-b27b12f442c4",
                "field_name": "file",
                "value": {
                    "filename": "birth_certificate.txt"
                }
            }
        ]
    }
}
```

### Delete record

Deletes a record in a specified data table.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/:record_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| data\_table\_id | **string** _required_ | The ID of the data table where the record resides. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| record\_id | **string** _required_ | The ID of the record to be deleted. |

#### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/:record_id' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

Workato returns status code `200` without a response payload if the deletion is successful.

### Generate link to upload file

Generates a link to upload a file for file-type columns. Use the resulting `upload_id` when you create or update a record.

<api-code no-copy-method>

```
POST https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/fields/:field_id/file
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| data\_table\_id | **string** _required_ | The ID of the data table where the record resides. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| field\_id | **string** _required_ | The ID of the file column for the file to be uploaded. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/fields/:field_id/file' \
   -H 'Authorization: Bearer <api_token>' \
   -H 'Content-Type: application/json'
```

</api-code>

#### Response

```json
{
  "data" : {
    "upload_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "url": "https://file-storage.workato.com/sharing/files?sign=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJXb3JrYXRvRmlsZXMiLCJhdWQiOiJ3b3JrYXRvX2ZpbGVzIiwiZXhwIjoxNzUzOTUzNTUzLCJuYmYiOjE3NTM5NTI2NTMsInN1YiI6IjY5MjY1OCIsImp0aSI6IjBmMzY4N2EyLTUzNGUtNGIxMC1iODQzLTk4NmU1MWI2YTI1MCIsIm9iaiI6eyJtZXRob2QiOiJHRVQiLCJyZXNvdXJjZSI6ImY0YWE3OWU0MjlhZjNjNGRhNTcwMGU0NTYxMTY3MzM2ZjMzOTJmNzNkZDQ0ZjhjMGExMTk4MDI5MmViNzE2NjMiLCJjb25zdHJhaW50cyI6eyJmaWxlX21heF9ieXRlcyI6bnVsbCwiZmlsZV9wYXRoIjoiL1Rlc3RpbmcvMi1zdGVwLWxvZ2luLWVucm9sbG1lbnQyMDI1LTA2LTI3VDAyMzE0Ni5odG1sIiwiZmlsZV90dGwiOm51bGwsIm5hbWVzcGFjZSI6ImFkYXB0ZXIiLCJzaGFyaW5nX2FwaV9raW5kIjoicHVibGljIiwidXNlcl9pZCI6NjkyNjU4fX19.0p-NuNaQxCs_VaTaWsQGg5aS3BwCGSrHSQOVh5xb-jXQAaHAv_RSnUs6ymV9IHMVZM2P1ikodSDGtyn7pqZItw"
  }
}
```

### Download file from the record

Generates a link to download the file in the file-type column of a record.

<api-code no-copy-method>

```
GET https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/:record_id/fields/:field_id/file
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| data\_table\_id | **string** _required_ | The ID of the data table where the record resides. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| record\_id | **string** _required_ | The ID of the record linked to the file. |
| field\_id | **string** _required_ | The ID of the file column of the file to be downloaded. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/:record_id/fields/:field_id/file'
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

Workato returns a `303` status code with the download URL inside the `LOCATION` header if the request is successful.

## Record import APIs

You can use the following endpoints to import records into a customer's data table from a file.

The following example shows a typical import flow:

Import flow

1. [Create a file upload link](#create-file-upload-link) to request a signed URL for the file.
   
2. [Upload the file](#upload-file) to the returned URL, sending the raw file bytes as the body.
   
3. Optional. [Describe the uploaded file](#describe-uploaded-file) to inspect the detected columns and record count before importing.
   
4. Add any missing columns to the table with the [Update data table](#update-data-table) endpoint. The table must already contain the columns you map to. Importing into a table with no matching columns fails.
   
5. [Start the import](#start-import), mapping file columns to table fields.
   
6. Monitor the import through the [records\_import\_status](#record-import-status) field of the **Get data table by ID** endpoint.
   
7. [Dismiss the import](#dismiss-import) to clear the import state, or call it earlier to cancel.
   

> **REGIONAL BASE URLS**
> 
> You must use the dedicated base URL that matches your workspace region. Refer to [Data center URLs](#data-center-urls) for more information.

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/file/upload\_link](#create-file-upload-link) | Creates a link to upload a file. |
| POST | [/sharing/files](#upload-file) | Uploads the file to the signed link. |
| DELETE | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/file](#delete-uploaded-file) | Deletes the uploaded file. |
| GET | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/file](#describe-uploaded-file) | Describes the uploaded file. |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/start](#start-import) | Starts importing records from the uploaded file. |
| DELETE | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import](#dismiss-import) | Dismisses or cancels the import. |

To check import status, use the [Get data table by ID](#get-data-table-by-id) endpoint and read the [records\_import\_status](#record-import-status) field.

### Create file upload link

Creates a signed link you use to upload a file for import.

<api-code no-copy-method>

```
POST https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/import/file/upload_link
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table to import records into. You can use the [List data tables](#list-data-tables) endpoint to retrieve data table IDs. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| file\_format | **hash** _required_ | The format of the file to upload. |
| file\_format\[format\] | **string** _required_ | The file format. Only `csv` is currently supported. |
| file\_format\[has\_header\] | **boolean** _required_ | Whether the file has column labels in the first row. |
| file\_format\[delimiter\] | **string** _required_ | The character used to separate values in a row. Accepted values are `comma`, `semicolon`, `space`, `tab`, `colon`, and `pipe`. |
| file\_format\[quote\] | **string** _required_ | The character used to quote values that contain the delimiter character or newlines. Accepted values are `double` and `single`. |
| file\_format\[encoding\] | **string** _required_ | The text encoding name. Supported encodings are those defined in the [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/). For example, `utf-8`. |

#### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/EA2300/tables/58408ccc-e209-491b-9873-4549b5fa48df/records/import/file/upload_link' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "file_format": {
             "format": "csv",
             "has_header": true,
             "delimiter": "comma",
             "quote": "double",
             "encoding": "utf-8"
           }
         }'
```

</api-code>

#### Response

Returns `201 Created` with the signed Workato Files URL you use to [upload the file](#upload-file).

```json
{
  "data": {
    "url": "https://file-storage.workato.com/sharing/files?sign=<signed_token>"
  }
}
```

Import already in progress

The request returns a `400 Bad Request` error with the `IMPORT_STATE_ERROR` code in the following example because an import is already in progress for the table:

```json
{
  "errors": [
    { "code": "IMPORT_STATE_ERROR", "title": "import already in progress" }
  ]
}
```

Table not found

The request returns a `404 Not Found` error in the following example because the data table doesn't exist or is outside your scope:

```json
{
  "errors": [
    { "code": "TABLE_NOT_FOUND" }
  ]
}
```

### Upload file

Upload the file to the signed URL returned by [Create file upload link](#create-file-upload-link). This endpoint doesn't require an `Authorization` header. The signature in the URL authorizes the request.

**Base URL**: the host returned in the `url` field of [Create file upload link](#create-file-upload-link)

<api-code no-copy-method>

```
POST /api/sharing/files
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| sign | **string** _required_ | The authorizing signature returned by [Create file upload link](#create-file-upload-link). |

#### Payload

Send the raw file bytes as the request body.

#### Sample request

<api-code>

```shell
curl -X POST 'https://file-storage.workato.com/sharing/files?sign=<signed_token>' \
     -H 'Content-Type: text/csv' \
     --data-binary @data.csv
```

</api-code>

#### Response

```json
{
  "file_id": "7d1ac9a4-2a6c-4951-b97a-9ab22c722500",
  "mime_type": "text/csv",
  "path": "/csv_import.4546638.c9228d13-f394-44ff-a3a2-13e04a70ea9c.csv",
  "size": 3005,
  "version_id": null
}
```

### Delete uploaded file

Deletes the file that was uploaded for import. Use this to cancel before starting an import.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/import/file
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table from which to delete the uploaded file. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/EA2300/tables/58408ccc-e209-491b-9873-4549b5fa48df/records/import/file' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

Returns `200 OK` with an empty `data` object.

```json
{
  "data": {}
}
```

No uploaded file

The request returns a `400 Bad Request` error with the `IMPORT_STATE_ERROR` code in the following example because a file wasn't uploaded for import:

```json
{
  "errors": [
    { "code": "IMPORT_STATE_ERROR", "title": "import file not found" }
  ]
}
```

Table not found

The request returns a `404 Not Found` error in the following example because the data table doesn't exist or is outside your scope:

```json
{
  "errors": [
    { "code": "TABLE_NOT_FOUND" }
  ]
}
```

### Describe uploaded file

Returns the columns and record count detected in the uploaded file so you can review them before starting the import.

<api-code no-copy-method>

```
GET https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/import/file
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table from which to describe an uploaded file. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/EA2300/tables/58408ccc-e209-491b-9873-4549b5fa48df/records/import/file' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

```json
{
  "data": {
    "columns": [
      {
        "column_id": "col1",
        "label": "report_date",
        "optional": false,
        "type": "date",
        "valid_types": ["date", "string"]
      },
      {
        "column_id": "col9",
        "label": "amount",
        "optional": false,
        "type": "number",
        "valid_types": ["number", "string"]
      }
    ],
    "file_format": {
      "delimiter": "comma",
      "encoding": "utf-8",
      "format": "csv",
      "has_header": true,
      "quote": "double"
    },
    "num_records": 18
  }
}
```

No uploaded file

The request returns a `400 Bad Request` error with the `IMPORT_STATE_ERROR` code in the following example because a file wasn't uploaded for import:

```json
{
  "errors": [
    { "code": "IMPORT_STATE_ERROR", "title": "import file not found" }
  ]
}
```

Table not found

The request returns a `404 Not Found` error in the following example because the data table doesn't exist or is outside your scope:

```json
{
  "errors": [
    { "code": "TABLE_NOT_FOUND" }
  ]
}
```

### Start import

Starts importing records from the uploaded file into the table.

> **PREREQUISITES**
> 
> The **Start import** endpoint has the following prerequisites:
> 
> - Upload a file with the [Upload file](#upload-file) endpoint.
> - Ensure all table columns exist in the target destination. Add any missing columns with the [Update data table](#update-data-table) endpoint before starting the import.

<api-code no-copy-method>

```
POST https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/import/start
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table to import records into. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| filename | **string** _required_ | The file name shown in the UI for this import. |
| fields | **array** _required_ | The mapping between file columns and table fields. Each entry maps one file column to one table field. All required table fields must be mapped, and the column and field data types must be compatible. |
| fields\[field\_id\] | **string** _conditional_ | The ID of the target table field. Provide either `field_id` or `field_name`. |
| fields\[field\_name\] | **string** _conditional_ | The name of the target table field. Provide either `field_id` or `field_name`. |
| fields\[file\_column\_index\] | **integer** _conditional_ | The 0-based index of the source file column. Provide either `file_column_index` or `file_column_label`. |
| fields\[file\_column\_label\] | **string** _conditional_ | The label of the source file column. You can use this only when the column label is unique in the file. Provide either `file_column_index` or `file_column_label`. |
| mode | **string** _required_ | The import behavior. Accepted values are `assert_table_empty`, `truncate_table`, and `append`. Refer to [Import modes](#import-modes) for more information. |

##### Import modes

The following import modes are supported:

| Mode | Behavior |
| --- | --- |
| `assert_table_empty` | The import proceeds only if the table is empty. Otherwise, it returns an error. |
| `truncate_table` | All existing records are deleted before importing. Requires the **Truncate a data table** permission. |
| `append` | Records are appended to the existing records in the table. |

#### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/EA2300/tables/58408ccc-e209-491b-9873-4549b5fa48df/records/import/start' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "filename": "data.csv",
           "fields": [
             { "field_name": "report_date", "file_column_label": "report_date" },
             { "field_name": "amount", "file_column_label": "amount" },
             { "field_name": "currency", "file_column_label": "currency" }
           ],
           "mode": "append"
         }'
```

</api-code>

#### Response

Returns `202 Accepted` with an empty `data` object when the import is successfully initiated. Track import progress with the [records\_import\_status](#record-import-status) field of the **Get data table by ID** endpoint.

```json
{
  "data": {}
}
```

Import can't be started

The request returns a `400 Bad Request` error with the `IMPORT_STATE_ERROR` code when the import can't start. For example, when a file wasn't uploaded, an import is already in progress, or the table isn't empty in `assert_table_empty` mode. The table isn't empty in the following example:

```json
{
  "errors": [
    { "code": "IMPORT_STATE_ERROR", "title": "table has records" }
  ]
}
```

Incompatible field mapping

The request returns a `400 Bad Request` error with the `IMPORT_SCHEMA_ERROR` code when the mapping is invalid. For example, due to an unknown column, a duplicate mapping, or an unmapped required field. A file column type doesn't match the target field type in the following example:

```json
{
  "errors": [
    { "code": "IMPORT_SCHEMA_ERROR", "title": "column \"Name\" (index 0) is not compatible with the type \"date\" of table field \"date_registered\" (9a2d5844-a983-43c7-b7c0-217c570b445a)" }
  ]
}
```

Table not found

The request returns a `404 Not Found` error in the following example because the data table doesn't exist or is outside your scope:

```json
{
  "errors": [
    { "code": "TABLE_NOT_FOUND" }
  ]
}
```

### Dismiss import

Dismisses the import state after an import completes, or cancels an in-progress import.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_TABLES_DC/api/v1/managed_users/:managed_user_id/tables/:data_table_id/records/import
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| data\_table\_id | **string** _required_ | The ID of the data table from which to dismiss or cancel an import. |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

#### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_TABLES_DC/api/v1/managed_users/EA2300/tables/58408ccc-e209-491b-9873-4549b5fa48df/records/import' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Response

Returns `200 OK` with an empty `data` object.

```json
{
  "data": {}
}
```

No import to dismiss

The request returns a `400 Bad Request` error with the `IMPORT_STATE_ERROR` code in the following example because no imports have started for the table:

```json
{
  "errors": [
    { "code": "IMPORT_STATE_ERROR", "title": "import not started" }
  ]
}
```

Table not found

The request returns a `404 Not Found` error in the following example because the data table doesn't exist or is outside your scope:

```json
{
  "errors": [
    { "code": "TABLE_NOT_FOUND" }
  ]
}
```

To check import status, use the [Get data table by ID](#get-data-table-by-id) endpoint and read the [records\_import\_status](#record-import-status) field.

---
