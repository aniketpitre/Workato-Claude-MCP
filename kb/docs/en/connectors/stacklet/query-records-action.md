---
url: 'https://docs.workato.com/en/connectors/stacklet/query-records-action.md'
description: The Query records action queries your records in Stacklet.
---

# Stacklet - Query records action

The **Query records** action queries your records in Stacklet.

## Input

The input fields load dynamically based on the object you select. For example, if you select **Accounts**, the following input fields are available.

| Input field | Description |
| --- | --- |
| Query | Select the records to retrieve with the query. |
| Filter element | Select either **Single** or **Multiple** filter elements to use in the query. |
| First | Enter a number to determine the first `n` results of the query response. |
| After | Enter a number to return query results with records appear after a specific point in the dataset. |
| Last | Enter a number to determine the last `n` results of the query response. |
| Before | Enter a number to query records that appear before a specific point in the data set. |
| Order | Enter a value to determine the order of the query results. |
| Sub queries | Select sub queries to retrieve in your query. |

## Output

The output fields load dynamically based on the object you select. For example, if you select **Accounts**, the following output is available.

| Output field | Description |
| --- | --- |
| Edges | Edges of the query results, including **Cursor** and **Node** values. |

---
