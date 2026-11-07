---
url: 'https://docs.workato.com/en/connectors/graphql/custom-action.md'
description: >-
  The Custom action in the GraphQL connector lets you run any custom GraphQL
  query or mutation, including variables, fragments, directives, and aliases.
---

# GraphQL - Custom action

This action can be used to run any custom GraphQL operation.

This is useful if you have existing GraphQL queries or mutations that you want to reuse in your recipes.

It also allows you to use advanced features of GraphQL query language, such as:

- Variables
- Fragments
- Inline-fragments
- Directives
- Aliases
- Multi-operation documents

See the [GraphQL documentation](https://graphql.org/learn/queries/) for more information about these features.

## Input

At a minimum, the **GraphQL document** must be provided. It must be a valid GraphQL query or mutation.

In the following example, the GraphQL document is a simple query for the details of a record with a specific ID, which is hard-coded in the query:

![Simple custom query](/assets/custom-action-simple-query.BL6_K4-E.png) _Simple custom query_

Instead of hard-coding the ID, you can use recipe datapills to inject the ID.

The record ID is set by the Role ID (Step 2) datapill:

![Custom query with datapills](/assets/custom-action-query-with-datapills.DUJBT2iU.png) _Custom query with datapills_

Alternatively, you can also define a variable in your GraphQL document and let the user provide the value through an input field.

For example, you would enter the **Role ID** to provide the value for the `$role_id` variable:

![Custom query with variables](/assets/custom-action-query-with-variables.Bd8hlWnr.png) _Custom query with variables_

If the GraphQL document contains multiple queries, you must select the operation to run.

The following document contains the queries `RoleWithTags` and `RoleWithoutTags`, and the **Operation to perform** is set to `Role without tags`:

![Custom query with multiple queries](/assets/custom-action-multiple-queries.d08J6RzJ.png) _Custom query with multiple queries)_

## Output

The output fields are determined by the fields mentioned in the query. To use them in downstream steps, map in the relevant datapill from the datatree.

![Example output fields for the GraphQL custom action](/assets/custom-action-output.DxbaYCnP.png) _Example output fields for the GraphQL custom action_

---
