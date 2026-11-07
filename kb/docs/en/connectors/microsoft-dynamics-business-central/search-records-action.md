---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/search-records-action.md
description: >-
  Search for records matching specific criteria using OData query options in
  Microsoft Dynamics Business Central.
---

# Microsoft Dynamics Business Central - Search records action

Use the **Search records** action to search for records in Microsoft Dynamics Business Central that match your specified criteria. This action uses OData query options to filter, search, and sort results. You must provide at least one search criteria (Search query or Filter criteria).

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to search from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, Environment, and more. |
| Search query | A free-text search expression using OData `$search` syntax. The search query allows clients to request entities matching a free-text search expression. Refer to the [OData Search](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#search) documentation for syntax format. |
| Filter criteria | An OData filter expression to filter records. For example, `totalTaxAmount lt 96.5`. Refer to the [OData Filter](https://docs.microsoft.com/en-us/odata/concepts/queryoptions-overview#filter) documentation for filter syntax help. |
| Expand | Specify additional related objects to be returned in the output. For example, enter `purchaseOrderLines` to include purchase order lines in the results. |
| Order by | Sort the results by field in ascending or descending order. For example, `displayName asc` or `displayName desc`. |
| Limit | The maximum number of results to display per page. |
| Offset | Skip the number of records before starting to return results from the query. |
| Company ID | Enter a Company ID to search records in a specific company. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |

> **SEARCH CRITERIA REQUIRED**
> 
> You must provide at least one of the following to use this action:
> 
> - **Search query**
> - **Filter criteria**

## Output

| Output field | Description |
| --- | --- |
| Objects | An array of records that match your search criteria. Each record includes all entity-specific fields as defined in your Business Central instance, the entity tag (ETag) for each record, and the unique identifier (ID) of each record. |
