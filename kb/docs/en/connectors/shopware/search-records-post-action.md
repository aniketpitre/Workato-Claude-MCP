---
url: 'https://docs.workato.com/en/connectors/shopware/search-records-post-action.md'
description: >-
  The Search records action enables you to retrieve a list of records that
  matches your search criteria in Shopware.
---

# Shopware - Search records (POST) action

The **Search records** action enables you to retrieve a list of records that matches your search criteria in Shopware. This action uses the `POST` HTTP method to retrieve a list of records. Use this action when passing large search queries.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve a list of records for. Fields load dynamically based on the object you select. |
| Filter | Filter query to apply to search results. |
| Sort | Specify the order in which the search results must be sorted. |
| Associations | An array of filter queries to filter fields of an object that support associations. |
| Fields | Specify the fields to return in the search result. |

## Output

The output schema depends on the selected object. Use the output fields to map datapills to downstream steps.

For example, if you select the **Order** object, the output includes the following:

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the order. |
| Active | Indicates whether the order is active or not. |
| Customer number | The unique number of customer who placed the order. |
| Company | The company that placed the order. |
| Email | The email address of the company/customer that placed the order. |

---
