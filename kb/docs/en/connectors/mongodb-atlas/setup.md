---
url: 'https://docs.workato.com/en/connectors/mongodb-atlas/setup.md'
description: >-
  Set up and connect MongoDB Atlas in Workato, including the cluster URI,
  database name, and a database user with read and write permissions.
---

# Connecting MongoDB Atlas

In this guide, we'll show you how to connect your MongoDB Atlas database to your Workato workspace.

* * *

## Setup Requirements

To connect MongoDB Atlas, you'll need:

- [A MongoDB Atlas account](https://docs.atlas.mongodb.com/tutorial/create-atlas-account/) with a deployed active cluster.
  
- [A database user](https://docs.atlas.mongodb.com/connect-to-database-deployment/#database-user) with **read and write** privileges on the database you're connecting.
  
- Privileges that allow you to manage IP Access List entries in MongoDB Atlas. This is typically associated with the [Project Owner role](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner).
  

* * *

## Step 1: Add Workato's IP Addresses to allowlist

To ensure Workato can successfully connect to your MongoDB Atlas instance, you'll need to add our [IP addresses](/en/security/ip-allowlists) to the database's IP Access List.

Follow [these steps](https://docs.atlas.mongodb.com/security/ip-access-list/#add-ip-access-list-entries) until all of Workato's IP addresses have been added.

* * *

> **TIP**
> 
> To complete this step, you need privileges in MongoDB Atlas that allow you to manage IP Access List entries.

## Step 2: Retrieve Your MongoDB Atlas Cluster URI

Next, you'll retrieve the cluster URI for your MongoDB Atlas instance. You'll use this in the last step to complete the connection in Workato.

1. Log in to your MongoDB Atlas account.
   
2. In the cluster you want to connect, click the **Connect** button.
   
3. Click **Connect with the Mongo Shell.**
   
4. In the **Run your connection string in your command line** step, locate the cluster URI. This is highlighted in the image below:
   
   ![The cluster URI highlighted in the Mongo connection string](/assets/cluster_uri-copy_uri_from_connection_string.BbKYCkhl.png)
   
5. Copy the cluster URI. Keep this handy - you'll need it for the next step.
   

* * *

## Step 3: Complete The Setup In Workato

In Workato, fill in these fields. When finished, click **Connect** to complete the connection.

| Field | Required | Description |
| --- | --- | --- |
| **Connection name** | Required | The name of the connection. We recommend choosing a name that identifies which MongoDB Atlas cluster the connection uses. |
| **Cluster URI** | Required | Paste the cluster URI you retrieved in [Step 2.](#step-2-retrieve-your-mongodb-atlas-cluster-uri) This will be similar to `cluster0.6rk8t.mongodb.net`. |
| **Database name** | Required | The name of the database Worko will connect to in the Mongo cluster. |
| **Username** | Required | The name of the database user Workato will use to connect to the Mongo cluster. This user must have **read and write** permissions. |
| **Password** | Required | The password of the database user. |
| **Retry writes** | Optional | Automatically retry write operations if certain issues are encountered. Check out the [MongoDB docs](https://docs.mongodb.com/manual/core/retryable-writes/#behavior) to learn more. |
| **Retry reads** | Optional | Automatically retry read operations if network or server errors are encountered. Check out the [MongoDB docs](https://docs.mongodb.com/manual/core/retryable-reads/#behavior) to learn more. |
| **App name** | Optional | An optional custom app name. Check out the [MongoDB docs](https://docs.mongodb.com/manual/reference/connection-string/#mongodb-urioption-urioption.appName) to learn more. |
| **Replica set** | Optional | If connecting to a [replica set](https://docs.mongodb.com/manual/replication/#replication), enter the name of the replica set. |
| **Auth source** | Optional | The name of the database in the Mongo cluster Workato will use to authenticate the **database user**. The default is `admin`. |
| **Read concern** | Optional | Allows you to control the consistency and isolation properties of the data read from replica sets and replica set shards. Defaults to `majority`. Check out the [MongoDB docs](https://docs.mongodb.com/manual/reference/connection-string/#readconcern-options) to learn more. |

---

---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/delete-documents.md
description: >-
  The Delete documents action in the MongoDB Atlas connector deletes documents
  from a collection that match an optional custom filter query.
---

# MongoDB Atlas - Delete documents action

This action deletes documents from a [MongoDB](/en/connectors/mongodb-atlas) Collection that match an optional custom query.

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection to delete documents from. Note: Names are case-sensitive. |
| **Custom filter query** | A JSON query used to filter documents. Documents that match the query's criteria will be deleted. Refer to the [Custom Filter Queries for MongoDB guide](/connectors/mongodb-atlas/guides/using-custom-filter-queries.html) for more info. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were deleted. |
| **Documents deleted count** | The total number of deleted documents. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Using Custom Filter Queries](/en/connectors/mongodb-atlas/guides/using-custom-filter-queries)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)

---

---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/insert-documents.md
description: >-
  The Insert documents action in the MongoDB Atlas connector inserts new
  documents into a collection based on a defined schema and field mapping.
---

# MongoDB Atlas - Insert documents action

This action inserts a batch of documents with a fixed structure into a [MongoDB](/en/connectors/mongodb-atlas) Collection. When we say "fixed", we mean that you know all the possible fields a document can have.

**Note**: If any of the following are true, use the [Replicate documents](/en/connectors/mongodb-atlas/actions/replicate-documents) action instead:

- The documents' schema is flexible or unknown, or
- You want to update existing records

* * *

## Limitations

- [MongoDB limits the size of a single document to 16MB](https://docs.mongodb.com/manual/reference/limits/#mongodb-limit-BSON-Document-Size).

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection where documents will be inserted. Note: Names are case-sensitive. |
| **Document schema** | Defines the schema of the documents to be inserted. You can add fields manually or provide sample JSON using the **Schema generator**. **Note:** For `integer` and `decimal` data, there are a few [limitations](/connectors/mongodb-atlas/typing-fields-in-mongodb.html) to be aware of. |
| **Input document** | Defines the mapping between source data and the MongoDB documents to be inserted. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were inserted. |
| **Inserted IDs** | An array of `_id` values of the inserted documents. |
| **Number of documents inserted** | The total number of documents inserted into the collection. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Data Typing Limitations](/en/connectors/mongodb-atlas/guides/typing-fields-in-mongodb)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)

---

---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/replicate-documents.md
description: >-
  The Replicate documents action in the MongoDB Atlas connector inserts or
  updates documents in a collection, de-duping records by unique fields.
---

# MongoDB Atlas - Replicate documents action

This action inserts multiple documents into a [MongoDB](/en/connectors/mongodb-atlas) Collection. Additionally, this action allows you to update existing documents, thereby preventing duplicate documents in the collection.

**If you want to retain document histories**, use the [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents) instead. The Insert Documents Action doesn't perform de-duplication, meaning existing documents aren't updated, but inserted as new documents. This allows you to see how a document has changed over time.

* * *

## How it works

When Workato replicates documents into the target collection, it will use the **Unique fields** input to check for existing documents and update them. This is called de-duplication, or de-duping, and is used to prevent duplicate records.

To summarize:

- **If a document doesn't exist in the collection**, Workato will insert the document.
- **If a document does exist in the collection**, it will be overwritten with the incoming version of the document.

Let's look at an example using `unique_code` as the **Unique field**.

**Here's an existing document in our collection**:

This document has a `unique_code` value of `CHOSEN_1`.

```json
{
  "unique_code": "CHOSEN_1",
  "first_name": "Anakin",
  "last_name": "Skywalker",
  "friends": ["c3po", "r2d2"]
}
```

**And an incoming version of the document:**

Note that even though the `unique_code` value is still `CHOSEN_1`, the other field values are different from the existing document:

```json
{
  "unique_code": "CHOSEN_1",
  "first_name": "Darth",
  "last_name": "Vader",
  "master": "Palpatine"
}
```

**The document after replication**:

During replication, Workato searches for records with `unique_code: CHOSEN_1` and if there's a match, overwrites the existing record.

This is what the final document would look like for this example:

```json
{
  "unique_code": "CHOSEN_1",
  "first_name": "Darth",
  "last_name": "Vader",
  "master": "Palpatine"
}
```

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection where documents will be replicated. Note: Names are case-sensitive. |
| **Documents** | The documents to replicate into the collection. This field accepts a List datapill. |
| **Unique fields** | The field(s) that identify a document as unique. For example: A unique `customer_id` Workato uses these field(s) to de-dupe records. If a document already exists in the collection, the document will be updated. Otherwise, a new document will be inserted. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were replicated. |
| **Documents inserted** | The total number of documents inserted into the collection. |
| **Documents updated** | The total number of documents in the collection that were updated. |
| **Inserted IDs** | An array of `_id` values of documents that were inserted. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)

---

---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/search-documents.md
description: >-
  The Search documents action in the MongoDB Atlas connector retrieves documents
  from a collection, with optional custom filter query, quota, and offset.
---

# MongoDB Atlas - Search documents action

This action retrieves documents from a [MongoDB](/en/connectors/mongodb-atlas) Collection.

* * *

## Limitations

Up to 10,000 documents can be retrieved at a time.

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection to retrieve documents from. Note: Names are case-sensitive. |
| **Quota** | The maximum number of documents to retrieve from the collection. The default is 1,000; the maximum is 10,000. |
| **Offset** | The number of documents to skip. |
| **Custom filter query** | A JSON query used to filter documents. Documents that match the query's criteria will be selected. Refer to the [Custom Filter Queries for MongoDB guide](/connectors/mongodb-atlas/guides/using-custom-filter-queries.html) for more info. |
| **Document schema** | Defines the expected fields of retrieved documents. You can add fields manually or provide sample JSON using the **Schema generator**. **Note:** For `integer` and `decimal` data, there are a few [limitations](/connectors/mongodb-atlas/typing-fields-in-mongodb.html) to be aware of. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were retrieved. |
| **Documents** | A list of the retrieved documents. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Using Custom Filter Queries](/en/connectors/mongodb-atlas/guides/using-custom-filter-queries)
- [Data Typing Limitations](/en/connectors/mongodb-atlas/guides/typing-fields-in-mongodb)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)

---

---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/update-documents.md
description: >-
  The Update documents action in the MongoDB Atlas connector updates documents
  in a collection that match an optional custom filter query.
---

# MongoDB Atlas - Update documents action

This action updates documents in a [MongoDB](/en/connectors/mongodb-atlas) Collection that match an optional custom query.

* * *

## Limitations

Updates to `array` fields have a few limitations:

- Updates to `array` fields will replace values entirely
  
- Partial updates (appending and/or removing fields) to `array` fields isn't currently supported.
  
  To make partial updates, we recommend that you:
  
  1. Use the [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents) to obtain a copy of the field's existing values
     
  2. Manipulate the field
     
  3. Update the field using this action
     

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection to update documents in. Note: Names are case-sensitive. |
| **Document schema** | Defines the schema of the documents to be updated. You can add fields manually or provide sample JSON using the **Schema generator**. **Note:** For `integer` and `decimal` data, there are a few [limitations](/connectors/mongodb-atlas/typing-fields-in-mongodb.html) to be aware of. |
| **Custom filter query** | A JSON query used to filter documents. Documents that match the query's criteria will be updated. Refer to the [Custom Filter Queries for MongoDB guide](/connectors/mongodb-atlas/guides/using-custom-filter-queries.html) for more info. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were updated. |
| **Documents updated count** | The total number of updated documents. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Using Custom Filter Queries](/en/connectors/mongodb-atlas/guides/using-custom-filter-queries)
- [Data Typing Limitations](/en/connectors/mongodb-atlas/guides/typing-fields-in-mongodb)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)

---

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

---

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

---
