---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/search-records-batch.md
description: >-
  The Search records batch action allows searching by specifying attribute
  values directly.
---

# Oracle Fusion Cloud - Search records action

The **Search records** batch action finds records by specific attribute values.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to search for. |
| Search operation | Select the operator for combined expressions. Options include **And** and **OR**. **And** returns records matching all specified attributes. **Or** returns records matching at least one specified attribute. |
| Limit | Specify the number of resources to return. The minimum is 1, and the maximum is 500. Defaults to 100. |
| Offset | Define the starting position of the resource collection. Default value is 0. |
| Expand | Select the child and grandchild objects to include in the output. |
| Order by | This parameter orders a resource collection based on the specified attributes. The parameter value is a comma-separated string of attribute names, each optionally followed by a colon and `asc` or `desc`. Specify `asc` for ascending and `desc` for descending. The default value is `asc`. e.g. field1:asc,field2:desc |
| Search by | Expand this field to specify how you plan to search for a record. |

## Output

Returns a list of records that match the search criteria, including record details, the total number of matches, quota and offset values, and an indicator showing whether more records are available in a separate job.
