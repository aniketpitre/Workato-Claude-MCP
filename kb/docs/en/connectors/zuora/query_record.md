---
url: 'https://docs.workato.com/en/connectors/zuora/query_record.md'
description: >-
  The Query record action in the Zuora connector lets you query records using
  Zuora Object Query Language, a SQL-like language for the SOAP API.
---

# Zuora - Query record action

## Query record action

This action queries records in Zuora using [Zuora Object Query Language](https://knowledgecenter.zuora.com/DC_Developers/BC_ZOQL). The Zuora Object Query Language (ZOQL) is a simple SQL-like query language used to construct query calls in the SOAP API.

Basic knowledge and experience with SQL is required to work with ZOQL

![Query record action](/assets/query_record_action.D-rK1gf1.png)_Query records_

### Input

| Field | Description |
| --- | --- |
| Object | Select the object type in Zuora you hope to query for. |
| ZOQL Query | A valid ZOQL query - `select field_names from object where filter_statements` |
| Batch size | The size of the query result to be returned. Maximum is 2000. |

### Output

| Field | Description |
| --- | --- |
| Array of records | An array of records where the attributes returned for each record change dynamically based on the object you have selected. |

### ZOQL details

- No Complex Queries Zuora does not support complex queries and joining for query().
  
- No Aggregate Functions Nested aggregate functions are not supported for query().
  
- No Wild Card Support You cannot use the asterisk wild card (\*) for field names with a query() call. You must explicitly specify a field name.
  
- No Order By Support ZOQL does not support sorting results in ascending or descending order.
  
- Conditions Allowed A maximum of 200 conditions are allowed in a WHERE clause of a query() call. For example, you can have up to 200 distinct AND or OR clauses.
  

Refer to the [ZOQL documentation](https://knowledgecenter.zuora.com/DC_Developers/BC_ZOQL) for more details.

---
