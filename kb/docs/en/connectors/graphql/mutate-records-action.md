---
url: 'https://docs.workato.com/en/connectors/graphql/mutate-records-action.md'
description: >-
  The Mutate records action in the GraphQL connector lets you create, update, or
  delete records using mutation arguments, fields, and sub-queries.
---

# GraphQL - Mutate records action

This action can be used to create, delete, or update records.

## Input

At a minimum, the top-level **Mutation** must be selected. This determines the operation to perform.

Depending on the mutation, additional input fields may be provided for:

- Mutation arguments
- Fields to retrieve
- Sub-queries

Each sub-query may have the following input fields:

- Query arguments
- Fields to retrieve
- Sub-queries

The sub-query pattern may continue recursively.

![Input fields](/assets/mutate-records-action-input.CL9PsYG2.png) _Example input fields for the GraphQL mutate records action_

_Mutation arguments_ are used to filter the data returned by the mutation. In the preceding example, you can enter the **Name** mutation argument in the **Input** section to create a record with a specific name.

_Fields to retrieve_ are used to determine which fields are returned by the mutation. For example, if you want to get the creation date, you can select the `Date created` field in the **Fields to retrieve** section. All fields are retrieved if this is left blank.

Note that you may need to select **Show optional fields** in order to see **Fields to retrieve**.

_Sub-queries_ are used to get related records. For example, if you want to get the current pets related to a record, you can select the `Current pets` sub-query.

This allows you to build a mutation that matches your needs.

## Output

The output fields are determined by the mutation, fields, and sub-queries selected in the input fields.

![Example output fields for the GraphQL mutate records action](/assets/mutate-records-action-output.Phha2ure.png) _Example output fields for the GraphQL mutate records action_

---
