---
url: 'https://docs.workato.com/en/connectors/salesforce/soql-faqs.md'
description: >-
  Answers to frequently asked questions about Salesforce SOQL in Workato,
  covering query syntax, WHERE clauses, and comparison operators.
---

# SOQL FAQs

Get answers to frequently asked questions about Salesforce SOQL.

What is Salesforce Object Query Language (SOQL)?

[SOQL](/en/connectors/salesforce/salesforce-soql#working-with-soql-in-salesforce) is a query language used to search Salesforce data for specific records. It's similar to SQL but is specifically designed for querying Salesforce data, allowing users to select, filter, and sort data stored in Salesforce objects.

What is the basic syntax of a SOQL query?

The [basic syntax](/en/connectors/salesforce/salesforce-soql#working-with-soql-in-salesforce) of a SOQL query involves a SELECT statement to specify the fields, a FROM statement to define the object, and an optional WHERE statement for filtering criteria and sorting.

How do I use the WHERE clause in SOQL?

In SOQL, the [WHERE clause](/en/connectors/salesforce/salesforce-soql#inputting-soql-where-conditions-syntax) is used to filter records based on specific conditions. The syntax follows a `fieldExpression` format, for example:

```shell
<fieldName> <comparisonOperator> <value>
```

What are the available SOQL comparison operators?

SOQL includes [comparison operators](/en/connectors/salesforce/salesforce-soql#comparison-operators) such as:

- `=`
- `!=`
- `<`
- `<=`
- `>`
- `>=`
- `LIKE`
- `IN`
- `NOT IN`
- `INCLUDES`
- `EXCLUDES`

Each operator is used to compare field values in different ways.

How can I use logical operators in SOQL?

[Logical operators](/en/connectors/salesforce/salesforce-soql#logical-operators) like `AND`, `OR`, and `NOT` can be used to join multiple field expressions in SOQL queries. These operators help combine multiple conditions in a WHERE clause.

What are other important SOQL clauses like LIMIT and OFFSET?

The [LIMIT clause](/en/connectors/salesforce/salesforce-soql#other-soql-clauses) restricts the number of records returned in a query, while [OFFSET](/en/connectors/salesforce/salesforce-soql#other-soql-clauses) skips a specified number of records before starting to return results. The maximum value for both clauses is 2,000.

How should I format dates and date-times in SOQL queries?

[Dates in SOQL](/en/connectors/salesforce/salesforce-soql#date-formats-and-date-literals) queries must be formatted as YYYY-MM-DD. For `dateTime` fields, formats such as `YYYY-MM-DDThh:mm:ss+hh:mm`, `YYYY-MM-DDThh:mm:ss-hh:mm`, and `YYYY-MM-DDThh:mm:ssZ` are used. Single quotes around date or `dateTime` values are not required.

How do I use SOQL in Salesforce triggers and actions?

SOQL can be used in Salesforce [triggers and actions](/en/connectors/salesforce/salesforce-soql#triggers-and-actions-that-use-soql) to set up queries based on fields provided in the Workato UI. It's commonly used in scheduled record search and record search actions in Workato.

How do I use a full SOQL query in Workato?

To use a [full SOQL query](/en/connectors/salesforce/salesforce-soql#querying-with-a-full-soql-query) in Workato, enter the complete SOQL query in the SOQL Query field when setting up a trigger or action, ensuring that it follows the correct syntax and format.

What is the maximum length of a SOQL query?

The [maximum length of a SOQL query](/en/connectors/salesforce/salesforce-soql#scheduled-records-search-using-soql-query) is 16,000 characters.

How can I handle the 2000 record quota in Salesforce actions?

You must implement pagination to manage the 2000 record quota in Salesforce actions. Pagination allows you to divide your data into manageable chunks. You can achieve this by using the [LIMIT and OFFSET fields](/en/connectors/salesforce/salesforce-soql#other-soql-clauses) inside a loop.

- Use `LIMIT` to define the number of records to retrieve in each batch.
- Use `OFFSET` to specify the starting point of each batch.

Refer to the Salesforce documentation on [pagination](https://developer.salesforce.com/blogs/2012/06/the-joys-of-soql-pagination) for more information.

How can I retrieve archived or deleted records from Salesforce using a SOQL query in Workato?

To retrieve archived or deleted records in Workato, set `IsDeleted = true` in the SOQL query:

```sql
SELECT IsDeleted, Name, Id FROM Contact WHERE IsDeleted = true
```

Ensure that the "Include deleted" option is set to "Yes."

![Retrieve archived or deleted records](/assets/salesforce-soql-retrieve-archive-deleted.CwaCHIGq.png)_Retrieve archived or deleted records_

---
