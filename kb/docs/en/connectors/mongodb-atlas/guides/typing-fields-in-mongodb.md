---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/guides/typing-fields-in-mongodb.md
description: >-
  Understand data typing limitations in MongoDB Atlas insert and replicate
  actions, including how integers are stored as doubles, with workarounds.
---

# Data Typing Limitations In MongoDB

When using MongoDB actions, you may encounter unexpected behavior when it comes to typing inserted data. In this guide, we'll explain what's happening and provide you with some workarounds.

* * *

## Applicable Actions

This guide applies to the following actions:

- [Insert documents](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Replicate documents](/en/connectors/mongodb-atlas/actions/search-documents)

* * *

## Integers Inserted As Doubles

If using a JSON sample to generate a schema for insertion into a collection, you may notice `integer` values are translated to `number` types. When data is inserted into MongoDB, the `number` type will be transformed into a `double`.

The root cause is that JSON doesn't distinguish integers from floating point numbers. For example: `1` is equivalent to `1.0`

To ensure fields are loaded as `integers`, manually add the field using the **Add new field** option in the schema editor.

* * *

## Decimals Inserted As Doubles

The default behavior for MongoDB is to type decimal values like `123.45` as `double`.

If you want data to be typed as `Decimal128`, you'll need to modify the field in MongoDB after it's been inserted.

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)
