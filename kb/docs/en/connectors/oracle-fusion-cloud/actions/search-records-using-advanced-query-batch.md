---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/search-records-using-advanced-query-batch.md
description: >-
  The Search records using advanced query batch action searches for records
  using flexible query options.
---

# Oracle Fusion Cloud - Search records using advanced query action (batch)

The **Search records using advanced query** batch action searches for records using flexible query options.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to search for. |
| Query | Define the WHERE clause, similar to SQL. For example, `InvoiceAmount>=10 and InvoiceAmount<=30 and Supplier!='NY'`. Refer to the [Oracle documentation](https://docs.oracle.com/en/cloud/saas/financials/22d/farfa/Collections.html#Collections-261C5653__concept-108-55605D77) for more information. |
| Fields | Specify which fields to return in the output to reduce response size. If you provide both **Fields** and **Expand**, only **Fields** applies. |
| Finder | Use a predefined finder query associated with the object. For example: `PrimaryKey;InvoiceId=3`. Refer to the [Oracle documentation](https://docs.oracle.com/en/cloud/saas/financials/22d/farfa/Collections.html#Collections-261C5653__concept-108-55605D77) for more information. |
| Limit | Specify the maximum number of records to return. The minimum is 1, and the maximum is 500. Defaults to 100. |
| Offset | Specify the starting position for results. Defaults to 0. |
| Expand | Select the child and grandchild objects to include in the output. |
| Order by | Sort results by specified fields. Use comma-separated format: `field1:asc,field2:desc`. Specify `asc` for ascending or `desc` for descending order. Defaults to ascending. For example: `amount:asc,date:desc` |

## Output

The output contains a list of records matching your search criteria. The specific fields vary based on the selected object. The response also includes the following pagination and metadata fields:

| Output field | Description |
| --- | --- |
| Count | Number of records returned in this response. |
| Total results | Total number of matching records. |
| Has more | Whether additional results are available. |
| Limit | Maximum records per page used in the request. |
| Offset | Starting position used in the request. |
| Links | Navigation links for pagination. |
| Hyperlink reference (Links) | URL for the navigation link. |
| Relation (Links) | Type of link relationship. |
| Name (Links) | Display name for the link. |
| Kind (Links) | Link category or type. |
