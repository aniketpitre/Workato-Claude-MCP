---
url: 'https://docs.workato.com/en/connectors/veeva-vault/search-records-action.md'
description: >-
  The Search records action searches records, such as products, in Veeva Vault
  using a VQL query.
---

# Veeva Vault - Search records action

The **Search records** action searches records, such as products, in Veeva Vault. The action uses a Vault Query Language (VQL) query to run the search.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Vault object. For example, **Product**. This list is populated dynamically from your Vault. |
| Fields to retrieve | Select one or more fields to include in the VQL `SELECT`. Defaults to `id, name__v` when left blank. |
| WHERE clause | Enter a VQL `WHERE` clause, without the `WHERE` keyword. |
| ORDER BY clause | Enter a VQL `ORDER BY` clause, without the `ORDER BY` keyword. |
| Page size | Number of records per page. Defaults to `200`, with a maximum of `1000`. |
| Page token | To fetch the next or previous page, map the `Next page token` or `Previous page token` from a prior call. All other inputs are ignored when provided. |

## Output

| Output field | Description |
| --- | --- |
| Total records | The total number of records matching the query. |
| Records on this page | The number of records returned on this page. |
| Page size | The page size used for this query. |
| Next page token | Map this into **Page token** on a subsequent call to fetch the next page. |
| Previous page token | Map this into **Page token** on a subsequent call to fetch the previous page. |
| Records | An array of records for the selected object. Output fields are dynamically generated based on the object you select. Refer to the [Veeva Vault](https://developer.veevavault.com/api/26.1/) documentation for more information. |

---
