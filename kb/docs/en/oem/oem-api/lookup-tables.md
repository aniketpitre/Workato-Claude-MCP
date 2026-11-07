---
url: 'https://docs.workato.com/en/oem/oem-api/lookup-tables.md'
description: >-
  Reference for the Embedded API lookup tables resource to list, create, and
  delete tables and to add, update, and remove rows.
---

# Embedded API - Lookup tables

Use the endpoints below to manage [lookup tables](/en/features/lookup-tables) programmatically.

## Rate limits

Lookup table resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List rows: [/api/managed\_users/:managed\_user\_id /lookup\_tables/:lookup\_table\_id/rows](/en/oem/oem-api/lookup-tables#list-rows) | 1,000 requests per minute |
| All | All other [Lookup tables](/en/oem/oem-api/lookup-tables.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables](/en/oem/oem-api/lookup-tables#list-lookup-tables) | List tables. |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/lookup](/en/oem/oem-api/lookup-tables#lookup-row) | Look up a row. |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows](/en/oem/oem-api/lookup-tables#list-rows) | List rows. |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/oem/oem-api/lookup-tables#get-row) | Get a row. |
| POST | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows](/en/oem/oem-api/lookup-tables#add-row) | Add a row. |
| POST | [/api/managed\_users/:managed\_user\_id/lookup\_tables](#lut-create) | Create a new lookup table. |
| POST | [/api/managed\_users/:managed\_user\_id/lookup\_tables/batch\_delete](#lut-delete) | Delete lookup tables in batch. |
| PUT | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/oem/oem-api/lookup-tables#update-row) | Update a row. |
| DELETE | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/oem/oem-api/lookup-tables#delete-row) | Delete a row. |

## List lookup tables

Returns a list of lookup tables belonging to a customer. Workato includes the `project_id` of the project to which the lookup table belongs in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables
```

</api-code>

### URL Parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Query Parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** | Page number. Defaults to 1. |
| per\_page | **integer** | Page size. Defaults to 100 (maximum is 100). |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
  "result": [
    {
      "id": 1315,
      "name": "lookup_table4",
      "schema": "[{\"control_type\":\"text\",\"label\":\"code\",\"name\":\"col1\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"name\",\"name\":\"col2\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"col3\",\"name\":\"col3\",\"type\":\"string\",\"sticky\":false},{\"control_type\":\"text\",\"label\":\"col4\",\"name\":\"col4\",\"type\":\"string\",\"sticky\":false},{\"control_type\":\"text\",\"label\":\"col5\",\"name\":\"col5\",\"type\":\"string\",\"sticky\":false}]",
      "created_at": "2022-05-20T11:54:26.934-07:00",
      "updated_at": "2022-05-20T11:54:26.934-07:00",
      "project_id": "523144"
    }
  ]
}
```

## Look up a row

Finds the first row matching the given criteria in the lookup table. Returns a 404 when the lookup fails.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/lookup
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| lookup\_table\_id | **integer** _required_ | Lookup table id |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| by`[<col name>]` | **string** _required_ | Lookup criteria. Format the column name as follows: `by[<col name>]`. To match by multiple columns, provide multiple parameters. Refer to the sample request for more details. |

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows/:row_id?by[code]=:by_code_value \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

### Response

```json
{
  "id": 942,
  "data": {
    "code": "US",
    "name": "United States",
    "col3": null,
    "col4": null,
    "col5": null
  },
  "created_at": "2022-05-20T11:50:32.986-07:00",
  "updated_at": "2022-05-20T11:50:40.986-07:00"
}
```

## List rows

Returns a lists of rows from the lookup table. Supports filtering and pagination.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| lookup\_table\_id | **integer** _required_ | Lookup table id |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** | Page number. Defaults to 1. |
| per\_page | **integer** | Page size. Defaults to 500 (maximum is 1000). |
| by`[<col name>]` | **string** | Filter criteria. The column name should be provided as follows: `by[<col name>]`. To match by multiple columns, provide multiple parameters. Refer to the sample request for more details. When not supplied, all rows are returned. |

### Sample request

#### Request 1: list rows

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

#### Request 2: filter and list rows

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows?by[code]=:by_code_value \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

### Response

#### Response 1: list rows

```json
{
       "result": [
            {
              "id": 941,
              "data": {
                "code": "IND",
                "name": "India",
                "col3": null,
                "col4": null,
                "col5": null
              },
              "created_at": "2022-06-15T11:50:32.986-07:00",
              "updated_at": "2022-06-15T11:50:40.986-07:00"
            },
            {
              "id": 942,
              "data": {
                "code": "US",
                "name": "United States",
                "col3": null,
                "col4": null,
                "col5": null
              },
              "created_at": "2022-05-20T11:50:32.986-07:00",
              "updated_at": "2022-05-20T11:50:40.986-07:00"
            }
      ]
}
```

#### Response 2: filter and list rows

```json
{
       "result": [
            {
              "id": 942,
              "data": {
                "code": "US",
                "name": "United States",
                "col3": null,
                "col4": null,
                "col5": null
              },
              "created_at": "2022-05-20T11:50:32.986-07:00",
              "updated_at": "2022-05-20T11:50:40.986-07:00"
            }
      ]
}
```

## Get a row

Get a row from a lookup table.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows/:row_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| lookup\_table\_id | **integer** _required_ | Lookup table id |
| row\_id | **integer** _required_ | Row id |

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows/:row_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

### Response

```json
{
  "id": 942,
  "data": {
    "code": "US",
    "name": "United States",
    "col3": null,
    "col4": null,
    "col5": null
  },
  "created_at": "2022-05-20T11:50:32.986-07:00",
  "updated_at": "2022-05-20T11:50:40.986-07:00"
}
```

## Add a row

Add a row to the lookup table.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| lookup\_table\_id | **integer** _required_ | Lookup table id |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| data | **Hash** _required_ | The hash contains the data for the new row. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{ "data": { "name": ":name", "code": ":code" }}'
```

</api-code>

### Response

```json
{
  "id": 942,
  "data": {
    "code": "USA",
    "name": "United States",
    "col3": null,
    "col4": null,
    "col5": null
  },
  "created_at": "2022-05-20T11:50:32.986-07:00",
  "updated_at": "2022-05-20T11:50:32.986-07:00"
}
```

## Create a new lookup table

Create a new lookup table. Depending on your requirements, you can choose to make the lookup table available for general access across your workspace or limit its scope to a specific project.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Provide a name for your new lookup table. |
| project\_id | **integer** _optional_ | Specify a `project_id` to scope the lookup table to a specific project. If you do not provide a `project_id`, the lookup table's scope is global. Use the [list projects](/en/oem/oem-api/project-properties#list-projects) API to obtain a list of projects in your workspace. |
| schema | **hash** _required_ | Determine the structure of your lookup table by supplying a schema and specifying a name for each column in your table, for example: `[{ "label": "Name" }]`. Lookup tables support a maximum of ten columns. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "lookup_table": {
            "name": ":name",
            "project_id": :project_id,
            "schema": [{ "label": ":label_1" }, { "label": ":label_2" }]
            }
          }'
```

</api-code>

#### Response

```json
{
    "id": 2372,
    "name": "Contacts",
    "schema": "[{\"control_type\":\"text\",\"label\":\"ID\",\"name\":\"col1\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"Name\",\"name\":\"col2\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"CSM\",\"name\":\"col3\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"Email\",\"name\":\"col4\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"Phone number\",\"name\":\"col5\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"Priority\",\"name\":\"col6\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"Tier\",\"name\":\"col7\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"Notes\",\"name\":\"col8\",\"type\":\"string\",\"sticky\":true},{\"control_type\":\"text\",\"label\":\"Created at\",\"name\":\"col9\",\"type\":\"string\",\"sticky\":false},{\"control_type\":\"text\",\"label\":\"Updated at\",\"name\":\"col10\",\"type\":\"string\",\"sticky\":false}]",
    "project_id": 4321,
    "created_at": "2023-09-11T11:31:35.335-07:00",
    "updated_at": "2023-09-11T11:31:35.335-07:00"
}
```

## Delete lookup tables in batch

Use this endpoint to delete lookup tables in batch.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/batch_delete
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| ids | **hash** _required_ | Include the ID(s) of the lookup table(s) you plan to delete. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/batch_delete \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{ "ids": [":id_1", ":id_2", ":id_3"] }'
```

</api-code>

#### Response

```json
{
    "data": {"deleted": [1234, 1235, 1236] },
    "errors": []
}
```

## Update a row

Updates a row in the lookup table.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows/:row_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| lookup\_table\_id | **integer** _required_ | Lookup table id |
| row\_id | **integer** _required_ | Row id |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| data | **Hash** _required_ | The hash containing the data for the updated row. Only the columns provided are updated. |

#### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows/:row_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{ "data": { "code": ":code" }}'
```

</api-code>

### Response

```json
{
  "id": 942,
  "data": {
    "code": "US",
    "name": "United States",
    "col3": null,
    "col4": null,
    "col5": null
  },
  "created_at": "2022-05-20T11:50:32.986-07:00",
  "updated_at": "2022-05-20T11:50:40.986-07:00"
}
```

## Delete a row

Delete a row from the lookup table

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows/:row_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| lookup\_table\_id | **integer** _required_ | Lookup table id |
| row\_id | **integer** _required_ | Row id |

#### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/lookup_tables/:lookup_table_id/rows/:row_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

### Response

```json
{
  "success": true
}
```

---
