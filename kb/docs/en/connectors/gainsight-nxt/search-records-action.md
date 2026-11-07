---
url: 'https://docs.workato.com/en/connectors/gainsight-nxt/search-records-action.md'
description: >-
  The Search records action fetches one or more records that match specific
  criteria in Gainsight NXT.
---

# Gainsight NXT - Search records action

The **Search records** action fetches one or more records that match specific criteria in `Gainsight NXT`. Records can be sorted and paginated. This action returns a maximum of 1000 records.

## Input

| Input field | Description |
| --- | --- |
| Object name | Use the drop-down menu to select the object to search. Options include **Company** and **Person**. |
| Object fields | Select the fields you plan to use in your recipe. |
| Filter conditions | Enter conditions that return only records matching specific criteria. Each condition requires an object field, alias, operator, and value. The expression defines the operator between conditions, for example, `A OR B` or `A AND B`. |
| Order by | Enter the fields to sort the results by, in ascending or descending order. |
| Limit | Enter the number of records to return. The maximum value is 1000. The default value is 100. |
| Offset | Enter the record number from which the remaining records are fetched. For example, if 60 records match the criteria and you enter an offset of 10, records 10 through 60 are returned. The default value is 0. |

## Output

Output fields are dynamically generated based on the object name you select. Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/gainsight-nxt/get-record-details-action.md
description: >-
  The Get record details action retrieves the details of a record in Gainsight
  NXT.
---

# Gainsight NXT - Get record details action

The **Get record details** action retrieves the details of a record in `Gainsight NXT`.

## Input

| Input field | Description |
| --- | --- |
| Object name | Use the drop-down menu to select the object. Options include **Company** and **Person**. |
| Gainsight NXT ID | The Gainsight NXT ID (GSID) of the record you plan to retrieve. |

## Output

Output fields are dynamically generated based on the object name you select. Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for a complete list of output fields.

---
