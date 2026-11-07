---
url: 'https://docs.workato.com/en/connectors/jira/export-new-issues-trigger.md'
description: >-
  The Export new issues in Jira trigger retrieves new issues from Jira on a
  schedule you specify.
---

# Jira - Export new issues in Jira trigger

The **Export new issues in Jira** trigger retrieves new issues from Jira on a schedule you specify.

Refer to the [ETL/ELT documentation](/en/features/etl-elt-guide#bulk-vs-batch) for more information about bulk triggers and ELT/ETL processes.

> **ISSUE ACCESS**
> 
> Workato only triggers jobs from issues that the connected Jira account has access to.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. Defaults to one hour ago if left blank. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| JQL where clause | Enter a JQL query to filter records by. For example: `project = "PRJ" AND status = "Done"`. This field only supports the following queries: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue`, `property`, and `cf[id]`. The `ORDER BY` clause isn't supported. Refer to the Jira documentation to learn more about [JQL](https://www.atlassian.com/software/jira/guides/jql/overview#what-is-jql). |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all navigable fields by default. |
| When exporting records to form the CSV, fetch them in batches of | Optional. Enter the number of issues to include in each batch. The default and maximum value is `100`. |
| Schedule settings | Configure the trigger schedule. Refer to the [scheduler trigger](/en/features/scheduler) to configure this section. |

## Output

| Output field | Description |
| --- | --- |
| CSV content | The results of the search as a CSV stream. You can write this datapill to a file using a file connector such as [Box](/en/connectors/box) or [SFTP](/en/connectors/sftp), or parse it using the **CSV tools by Workato** [Parse CSV](/en/connectors/csv-by-workato/parse-csv-action) action. |
| Object name | The type of object that was exported. |
| Object schema | Contains information about the schema of the object, including the fields specified in the **Fields to retrieve** input. |
| New From | The date and time the object was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/jira/export-new-updated-issues-trigger.md
description: >-
  This trigger retrieves new or updated issues from Jira on a schedule you
  specify.
---

# Jira - Export new/updated issues in Jira trigger (bulk)

The **Export new/updated issues in Jira (bulk)** trigger retrieves new or updated issues from Jira on a schedule you specify.

You can use this trigger with the [Get issue schema for Jira](/en/connectors/jira/actions#get-issue-schema) action to retrieve an issue's schema and replicate it to a database or data warehouse.

Refer to the [ETL/ELT documentation](/en/features/etl-elt-guide#bulk-vs-batch) for more information about bulk triggers and ELT/ETL processes.

> **ISSUE ACCESS**
> 
> Workato only triggers jobs from issues that the connected Jira account has access to.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. Defaults to one hour ago if left blank. You can't change this value after running or testing the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| JQL where clause | Enter a JQL query to filter records by. For example: `project = "PRJ" AND status = "Done"`. This field only supports the following queries: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue`, `property`, and `cf[id]`. The `ORDER BY` clause isn't supported. Refer to the Jira documentation to learn more about [JQL](https://www.atlassian.com/software/jira/guides/jql/overview#what-is-jql). |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all navigable fields by default. |
| When exporting records to form the CSV, fetch them in batches of | Optional. Enter the number of issues to include in each batch. The default and maximum value is `100`. |
| Schedule settings | Configure the trigger schedule. Refer to the [scheduler trigger](/en/features/scheduler) to configure this section. |

## Output

| Output field | Description |
| --- | --- |
| CSV content | The contents of the issue as a CSV stream. You can write this datapill to a file using a file connector such as [Box](/en/connectors/box) or [SFTP](/en/connectors/sftp), or parse it using the **CSV tools by Workato** [Parse CSV](/en/connectors/csv-by-workato/parse-csv-action) action. |
| Object name | The type of object that was created or updated. |
| Object schema | Contains information about the schema of the object, including the fields specified in the **Fields to retrieve** input. |
| New/updated from | The time and date the record was created or updated. |

---
