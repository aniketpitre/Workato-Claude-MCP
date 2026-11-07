---
url: 'https://docs.workato.com/en/connectors/shopware/search-records-get-action.md'
description: >-
  The Search records action retrieves a list of records that matches your search
  criteria in Shopware.
---

# Shopware - Search records (GET) action

The **Search records** action retrieves a list of records that matches your search criteria in Shopware. This action uses the `GET` HTTP method to retrieve a list of records. Use this action when passing smaller search queries.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve a list of records for. Fields load dynamically based on the object you select. |
| Page | The page to return. |
| Limit | The maximum number of resources to return in a page. You can only enter positive numbers (excluding 0) in this field. |
| Query | The search query to filter results with. |

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
