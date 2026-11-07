---
url: 'https://docs.workato.com/en/connectors/freshbooks/list-records-action.md'
description: >-
  The List records action enables you to retrieve a list of records in
  FreshBooks.
---

# FreshBooks - List records action

The **List records** action enables you to retrieve a list of records in FreshBooks.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to list records for. Fields load dynamically based on the object you select. |
| Account ID | Select the FreshBooks account ID to retrieve the list of records. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if you select the **Item** object, the output schema is as follows:

| Output field | Description |
| --- | --- |
| Items | An array of item objects returned from FreshBooks. |
| Page | Current page number in the paginated results. |
| Pages | Total number of pages available. |
| Per page | Number of items returned per page. |
| Total | Total number of items available across all pages. |

---
