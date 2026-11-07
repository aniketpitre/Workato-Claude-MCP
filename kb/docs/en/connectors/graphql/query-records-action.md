---
url: 'https://docs.workato.com/en/connectors/graphql/query-records-action.md'
description: >-
  The Query records action in the GraphQL connector lets you get a single record
  or search for records using query arguments, fields, and sub-queries.
---

# GraphQL - Query records action

This action can be used to get a single record or to search for records that match specific criteria.

## Input

At a minimum, the top-level **Query** must be selected. This determines the type of record to retrieve.

Depending on the query, additional input fields may be provided for:

- Query arguments
- Fields to retrieve
- Sub-queries

Each sub-query may have the following input fields:

- Query arguments
- Fields to retrieve
- Sub-queries

The sub-query pattern may continue recursively.

![Input fields](/assets/query-records-action-input.C1Gq16TV.png) _Example input fields for the GraphQL query records action_

_Query arguments_ filter the records returned by the query. In the preceding example, if you want to get a single record by its ID, you can enter the **Id** query argument.

_Fields to retrieve_ are used to determine which fields are returned by the query. For example, if you want to get a record's ID, name, and when it was last updated, you can select the `Id`, `Name`, and `Last updated` fields in the **Fields to retrieve** section. All fields are retrieved if this is left blank.

Note that you may need to select **Show optional fields** in order to see **Fields to retrieve**.

_Sub-queries_ are used to get related records. For example, if you want to get the tags related to a record, you can select the `Tags` sub-query.

This allows you to build a query that matches your needs.

## Output

The output fields are determined by the queries, fields, and sub-queries selected in the input fields. To use them in downstream steps, map in the relevant datapill from the datatree.

![Example output fields for the GraphQL query records action](/assets/query-records-action-output.BaPunP4N.png) _Example output fields for the GraphQL query records action_

---
