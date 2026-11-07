---
url: 'https://docs.workato.com/en/connectors/quickbase/search-records-action.md'
description: >-
  The Search records action in the Quickbase connector finds records in a
  specified table that match your query, with sorting and a result quota.
---

# Quickbase - Search records action (batch)

This action searches for records in a specified Quickbase table that match the search criteria.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | This is required if this application has been configured to require tokens for data access. You can obtain the token from the application's **Settings > App properties > Manage Application Token**. |
| Table | Select the table where you plan to create the record. You can either select the table from the drop-down, or provide the table ID. |
| Table field list | Select which columns in your Quickbase table to map to. Workato can support a maximum of 150 fields from a Quickbase table. If your table has more than 150 fields, select the fields you plan to use. These fields are dynamic and change based on the **Table** you select. |
| Query | Use Quickbase query to fetch only records that match your query. Query syntax is `{'fid'.operator.'matching_value'}`. For example, `{'7'.EX.'Test'}`. |
| Sort field | Select a field to use for sorting the records. If you don’t specify the sort field, the default order of the records on the report layout page is used. |
| Sort order | Select the order to sort the records, based on the selected Sort field. Defaults to ascending if left blank. |
| Limit | Enter the number of records you plan for this action to return. The minimum is 1 and the maximum is 1000. |

> **ADDITIONAL FIELDS**
> 
> Workato displays additional fields which you can use to filter records in your Quickbase table. The fields available are dynamic and change based on the table you select.

## Output

The output datatree contains a list of records. Each record contains information based on the selected fields.

| Field | Description |
| --- | --- |
| Records | A list of records that match the search criteria. |

---

---
url: >-
  https://docs.workato.com/en/connectors/quickbase/get-records-from-report-action.md
description: >-
  The Get records from a report action in the Quickbase connector retrieves
  records from a pre-built report, with sorting and a result quota.
---

# Quickbase - Get records from a report action (batch)

This action gets records from a pre-built report in your Quickbase.

## Input

| Field | Description |
| --- | --- |
| Application | Select an application in your Quickbase account. |
| Application token | This is required if this application has been configured to require tokens for data access. You can obtain the token from the application's **Settings > App properties > Manage Application Token**. |
| Table | Select the table where you plan to create the record. You can either select the table from the drop-down, or provide the table ID. |
| Report | Select a Quickbase report. Workato fetches records from this report. |
| Report field list | Workato can support a maximum of 150 fields from a Quickbase table. If your table has more than 150 fields, select the fields you plan to use in the Table field list. |
| Sort field | Select a field to use for sorting the records. |
| Sort order | Select the order to sort the records, based on the selected Sort field. Defaults to Ascending if left blank. |
| Limit | Enter the number of records you plan for this action to return. Minimum is 1 and maximum is 1000. |

## Output

The output datatree contains a list of records. Each record contains information based on the selected fields.

| Field | Description |
| --- | --- |
| Records | A list of records from the specified report. |

---
