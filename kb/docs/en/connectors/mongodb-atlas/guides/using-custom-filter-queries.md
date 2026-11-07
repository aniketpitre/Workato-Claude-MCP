---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/guides/using-custom-filter-queries.md
description: >-
  Use custom filter queries to filter documents in MongoDB Atlas delete, search,
  and update actions with Extended JSON and BSON types.
---

# Using Custom Filter Queries In MongoDB Actions

Using the **Custom filter query** field, you can filter the documents used in MongoDB actions in your recipes.

* * *

## Supported Actions

Custom filter queries are supported for the following MongoDB actions:

- [Delete documents](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Search documents](/en/connectors/mongodb-atlas/actions/search-documents)
- [Update documents](/en/connectors/mongodb-atlas/actions/update-documents)

* * *

## How it works

Using MongoDB's [Extended JSON](https://docs.mongodb.com/manual/reference/mongodb-extended-json/#example), you can construct queries that return a subset of documents from a collection.

Custom filter queries support:

- [Using BSON types](#using-bson-types)
- [Using JSON types](#using-json-types)
- [Using query operators](#using-query-operators)

### Using BSON Types

Custom filter queries accept [BSON types](https://docs.mongodb.com/manual/reference/bson-types/), with some [limitations](#limitations).

For example: This query would return documents with an `ObjectId` (`oid`) value of `5d505646cf6d4fe581014ab2`:

```json
{
   "_id":{
      "$oid":"5d505646cf6d4fe581014ab2"
   }
}
```

### Using JSON Types

Custom filter queries also accept [JSON data types](https://en.wikipedia.org/wiki/JSON#Data_types) such as `string`, `boolean`, `number`, etc.

For example: The following query returns documents where the document's `manager_id` value is a `string` type:

```json
{
   "manager_id":"string"
}
```

### Using Query Operators

You can also use [query operators](https://docs.mongodb.com/manual/reference/operator/query/#query-selectors) to perform comparison and logic operations. **Note**: There are some [limitations](#limitations) on the operators that are currently supported.

For example: We'll use this query to search for documents in an `employees` collection:

```json
{
   "manager_id":{
      "$oid":"5d505646cf6d4fe581014ab2"
   },
   "sales_closed":{
      "$gt":{
         "$numberDecimal":"1000000"
      }
   },
   "date_hired":{
      "$gt":{
         "$date":"2020-12-31T00:00:00.000Z"
      }
   }
}
```

The above query searches for documents - or employees - that:

- Have a `manager_id` value of `5d505646cf6d4fe581014ab2`)
- Have a total `sales_closed` value greater than `$1,000,000`, and
- Were hired after `2020-12-31` (December 31, 2020)

* * *

## Limitations

- **Only the following [BSON types](https://docs.mongodb.com/manual/reference/bson-types/) are currently supported:**
  - `Decimal128`, synonymous with `$numberDecimal`
  - `ObjectId`, synonymous with `$oid`
  - `Date`, synonymous with `$date`
- The [`$where`](https://docs.mongodb.com/manual/reference/operator/query/where/#-where) query operator isn't currently supported

* * *

## Resources

- [MongoDB Extended JSON](https://docs.mongodb.com/manual/reference/mongodb-extended-json/#example)
- [MongoDB Query Selectors](https://docs.mongodb.com/manual/reference/operator/query/#query-selectors)
- [MongoDB BSON Data Types](https://docs.mongodb.com/manual/reference/bson-types/)
