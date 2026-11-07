---
url: >-
  https://docs.workato.com/en/connectors/smartsuite/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action enables you to retrieve details of a
  specific record in SmartSuite.
---

# SmartSuite - Get record details by ID action

The **Get record details by ID** action enables you to retrieve details of a specific record in SmartSuite.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve. Fields load dynamically based on the object you select. |

For example, if you select **Table**, the input schema is the following:

| Input field | Description |
| --- | --- |
| Solution ID | Provide the SmartSuite solution ID. |
| Table ID | Provide the SmartSuite table ID. |
| Other params | Provide the expected other parameters for the structure that are added in the output. |

## Output

The output fields are determined by the object selected in the input.

For example, if you select **Table**, the output schema is the following:

| Output field | Description |
| --- | --- |
| Table ID | The ID of the table. |
| Table name | The name of the table. |
| Table icon | The icon of the table. |
| Solution ID | The ID of the solution. |
| Slug | The slug value of the table. |
| Status | The status of the table. |
| Primary field | The primary field of the table. |
| Order | The order of the table. |
| Show all reports members | The details of the reporting members. |
| Field permissions | The details of the field permissions. |
| Record term | The term of the record. |
| Record avatar field slug | The avatar field slug of the record. |
| Hidden | Indicates if this field is hidden. |
| Structure | The structure value of the table. |
| Slug | The slug value of the field. |
| Label | The label of the field. |
| Field type | The type of the field. |
| Params | The parameters of the fields. |
| Structure layout | The structure layout of the table. |
| Mode | The mode of the structure layout. |
| Hidden fields | The hidden fields in the table. |
| Hidden fields in conditions | The conditions of the hidden fields. |
| Single column | The single column value of the table. |

Refer to the [SmartSuite documentation](https://developers.smartsuite.com/docs/solution-data/tables/get-table) for more information.
