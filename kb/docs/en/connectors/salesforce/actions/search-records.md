---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/search-records.md'
description: >-
  This action retrieves a list of Salesforce records that match the search
  criteria you provide.
---

# Salesforce - Search records action (batch)

This action retrieves a list of Salesforce records that match the search criteria you provide. Each job can retrieve up to 2,000 records.

> **ACTION TIMEOUT**
> 
> Some Salesforce fields are indexed, which allows queries on them to run faster and more efficiently. This action may fail due to a timeout if you search by unindexed fields, such as custom objects. Refer to the Salesforce [Improve Performance of SOQL Queries using a Custom Index](https://help.salesforce.com/apex/HTViewSolution?id=000006007&language=en_US) guide to improve the performance of search. Use the [Search records using SOQL](/en/connectors/salesforce/actions/search-records-soql) action for advanced search.

## Input

| Input fields | Description |
| --- | --- |
| Search for | Select the type of Salesforce object to search for. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| Limit | Enter the maximum number of records to return each job. The maximum value for this field is 2,000. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

The output of this action varies based on your selected **Object** and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/search-records-soql.md
description: >-
  This action retrieves a CSV stream of Salesforce records that match the SOQL
  query you provide.
---

# Salesforce - Search records in bulk using SOQL query action

This action retrieves a CSV stream of Salesforce records that match the SOQL query you provide. This action uses the Salesforce bulk API.

> **POLLING BEHAVIOR**
> 
> Recipes that contain an action with polling must be in a running state for asynchronous polling to function as expected.

Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information about SOQL or the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

> **API VERSIONS**
> 
> This action exists in both API v1.0 and API v2.0 versions. Workato recommends using the bulk API v2.0 for optimal performance. This version reduces the impact on Salesforce API quotas by batching records more efficiently.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| SOQL query | Provide a valid SOQL query excluding the LIMIT param. Enclose clauses with parentheses for logical operators. |
| Include deleted records? | Select whether to include deleted records in the results. Defaults to `No`. |
| Include header line? | Select whether to include the header line in the CSV results. |
| Retain failed job logs on Salesforce interface? | Select whether to persist failed job logs in Salesforce. Defaults to `No`. |
| Wait for Salesforce to process all CSV rows? (Advanced configuration) | Select whether to run the action synchronously. Select `Yes` to wait until Salesforce processes all rows in the CSV file before starting the next action. Select `No` to start the next action after the CSV file is uploaded to Salesforce. Bulk operations are asynchronous by default. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Job ID | The Salesforce ID of the job. |
| All records successfully processed? | Specifies whether all CSV rows across Salesforce bulk jobs were processed successfully. |
| CSV results | The retrieved records as a CSV stream. You can write the CSV stream to a file using a file connector, such as [Box](/en/connectors/box) or [SFTP](/en/connectors/sftp). You can also parse it as a list of data in Workato using the [Parse CSV](/en/connectors/csv-by-workato/parse-csv-action) action in the CSV tools by Workato utility connector. |
| Number of records processed | The total number of CSV rows processed in Salesforce, excluding the header row. |
| Number of records failed | The total number of CSV rows that encountered issues and were not processed in Salesforce. |
| Number of retried records | The total number of CSV rows that retried processing in Salesforce. This field is relevant for the [Retry objects bulk job in Salesforce from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action. |
| Processing time | The amount of time spent processing records. |

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/search-records-soql-batch.md
description: >-
  This action retrieves a list of Salesforce records that match the SOQL query
  you provide.
---

# Salesforce - Search records using SOQL query (batch)

This action retrieves a list of Salesforce records that match the SOQL query you provide. Each job can retrieve up to 2,000 records. The maximum length of the SOQL query is 16,000 characters. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information about SOQL.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| SOQL query | Provide a valid SOQL query excluding the LIMIT param. Enclose clauses with parentheses for logical operators. Returned records include deleted records by default. You can use `IsDeleted = false` to exclude them. |
| Output schema | Click **Use SOQL** to describe all fields in your response using SOQL, or click **add fields manually** to fill out the **Add new field** modal and configure the **Name**, **Hint**, **Label**, **Data type**, whether the parameter is **Optional**, and where the parameter should **Nest under**. |
| Limit | Enter the maximum number of records to return each job. The default value for this field is 150 and the maximum is 2,000. Workato omits the limit clause when aggregate functions are used. |
| Offset | Enter a number of rows to skip before returning query results. The maximum offset is 2,000 rows. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Done | Indicates whether this response contains the end of the retrieved record list. |
| Total size | The total number of matching records retrieved. |
| Records | An object containing records that match the provided SOQL query. `List index` is the position of the current record in the list. `List size` is the total number of records retrieved. |

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/search-records-soql-where.md
description: >-
  This action retrieves a CSV stream of Salesforce records that match the SOQL
  WHERE clause you provide.
---

# Salesforce - Search records using SOQL query WHERE clause action (batch)

This action retrieves a CSV stream of Salesforce records that match the SOQL WHERE clause you provide. Each job can retrieve up to 2,000 records. Refer to the [SOQL](/en/connectors/salesforce/salesforce-soql) guide for more information about SOQL.

> **SELECT CLAUSE IN SOQL**
> 
> SOQL queries don't support the `SELECT *` operation often used in SQL queries. You must specify specific fields to retrieve in the SELECT clause.

## Input

| Input fields | Description |
| --- | --- |
| Search for | Select the type of Salesforce object to search for. |
| SOQL WHERE clause | Enter a SOQL query to filter records by. For example: `StageName = 'Closed Lost' AND IsClosed = false` |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| Limit | Enter the maximum number of records to return each job. The default value for this field is 150 and the maximum is 2,000. |
| Offset | Enter a number of rows to skip before returning query results. The maximum offset is 2,000 rows. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

The output of this action varies based on your selected **Search for** object and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.

---
