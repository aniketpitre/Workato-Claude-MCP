---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/metadata-filters.md
description: >-
  Use metadata filters for List documents (advanced filters) and Search
  documents (advanced filters) batch actions.
---

# Metadata filters

Use metadata filters for **[List documents (advanced filters)](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/list-documents-advanced-filters)** and **[Search documents (advanced filters)](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/search-documents-advanced-filters)** batch actions.

Filter metadata with a **data\_filters** JSON object to retrieve data that dedicated fields can't express, such as matching against a list of values, OR groups of conditions, or combining several conditions at once.

## When to use advanced filters

The standard **[Search documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/search-documents)** and **[List documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/list-documents)** actions use static filtering for dedicated fields like content type, Created after, Created before, Updated after, Updated before, and a key-value Metadata filters list.

**List documents (advanced filters)** and **Search documents (advanced filters)** use `data_filters` to enable dynamic, advanced filtering when static filtering can't parse data.

> **DON'T MIX FILTERING STYLES ON THE SAME FIELD**
> 
> Static filtering and `data_filters` write to the same query. Targeting one field with both filtering types is unsupported. For example, don't use Created after and `data_filters: {"created_at": ...}`.

## How to use advanced filters

Use the following examples to determine how advanced filtering can be applied to your workflow:

### Exact match

The following example returns only documents whose `status` metadata equals `active`. Use this example when a field equals a single value.

```json
{ "status": "active" }
```

### Match multiple values (OR)

The following example returns any value that matches the list you provide. Use this example when you need to check whether a value appears inside an array.

```json
{ "owner": ["abby", "jaime"] }
```

This returns documents owned by `abby` or `jaime`.

### OR groups

The following example returns documents that match any whole condition in the list you provide, rather than values for a single field. Use this example when you need to combine conditions with OR on different fields:

```json
{ "or": [ { "category": "finance" }, { "category": "legal" } ] }
```

This returns documents where `category` equals `finance` or `legal`.

#### OR group where each branch has more than one condition

Use the following example when there's more than one condition on a branch. Each object inside `or` can combine keys with `AND`, so you can OR together two different multi-field conditions:

```json
{
  "or": [
    { "category": "finance", "region": "US" },
    { "category": "legal", "region": "EU" }
  ]
}
```

Returns `(category = finance AND region = US)` OR `(category = legal AND region = EU)`.

#### OR group combined with a top-level AND condition

Use the following example when a top-level key next to `or` applies to every result to combine it with AND to the matching OR branch:

```json
{
  "status": "active",
  "or": [
    { "owner": "abby" },
    { "owner": "jaime" }
  ]
}
```

Returns documents with an `active` status and the owner is `abby` or `jaime`.

### Date range

The following example returns documents that fall within the range you provide. Use this example when you need to filter `created_at` or `updated_at` before, after, or between dates.

```json
{ "created_at": { "start": "2024-01-01", "end": "2024-12-31" } }
```

This returns documents where `created_at` falls between January 1, 2024 and December 31, 2024. Both `start` and `end` are optional. Dates use ISO 8601 format, either `YYYY-MM-DD` or a full timestamp. This range shape applies only to `created_at` and `updated_at`. Refer to [Field operators](#field-operators) to compare values on other fields.

Provide only `start` and omit `end` to retrieve documents from this date onward. For example:

```json
{ "updated_at": { "start": "2024-06-01" } }
```

Provide only `end` and omit `start` to retrieve documents before the date you provide. For example:

```json
{ "created_at": { "end": "2024-06-30" } }
```

### Field operators

Provide a field with an object containing one or more of the following operators instead of a plain value:

| Operator | Meaning | Accepts | Resulting query |
| --- | --- | --- | --- |
| `ne` | Not equals, or excludes | A single value, or a list to exclude several values at once | `must_not` term or terms match on the field |
| `gt` | Strictly greater than | Number or date string | Exclusive lower-bound range |
| `gte` | Greater than or equal to | Number or date string | Inclusive lower-bound range |
| `lt` | Strictly less than | Number or date string | Exclusive upper-bound range |
| `lte` | Less than or equal to | Number or date string | Inclusive upper-bound range |
| `like` | Partial or wildcard match | A string containing `*` for any characters, `?` for a single character, or both | Wildcard match against the exact stored value |

Use these operators when you need to exclude values, compare values, or match part of a value. Operators work in all metadata fields, not only `created_at` and `updated_at`.

Listing more than one operator on the same field chains the operators together using AND. For example, `gte` with `lt` produces a half-open range:

```json
{ "page_count": { "gte": 10, "lt": 100 } }
```

This returns documents where `page_count` is 10 or greater and less than 100. The lower bound is included and the upper bound is excluded.

#### Exclude a value

The following example returns documents whose `author` metadata is anything other than `bot`.

```json
{ "author": { "ne": "bot" } }
```

Provide a list to exclude several values at once. For example:

```json
{ "status": { "ne": ["spam", "deleted"] } }
```

This returns documents where `status` equals neither `spam` nor `deleted`.

#### Numeric range

The following example returns documents with a `page_count` that falls between 10 and 100. Use this example when you need an inclusive range on a field that holds numbers.

```json
{ "page_count": { "gte": 10, "lte": 100 } }
```

Use `gt` and `lt` when you need to exclude the bounds. For example:

```json
{ "page_count": { "gt": 10, "lt": 100 } }
```

This returns documents where `page_count` is greater than 10 and less than 100.

#### Partial match

The following example returns documents with a `title` that contains `quarterly` anywhere in the value. Use this example when you need to match part of a value rather than the whole value.

```json
{ "title": { "like": "*quarterly*" } }
```

> **TEST RANGE OPERATORS AGAINST REAL DATA**
> 
> `gt`, `gte`, `lt`, and `lte` build a native OpenSearch range query against the raw `metadata.<field>` value rather than the `.keyword` subfield. These operators behave as true numeric or date comparisons only when the underlying field is indexed with a numeric or date type. The filter model doesn't validate or coerce types. Test range operators against real data for your connector and datasource before you rely on them in production.

Empty or missing operator values, such as `""`, `null`, or `[]`, are ignored rather than returning an error. This aligns with the behavior in the other building blocks.

### AND across keys

The following example returns documents that match every key you provide. Use this example when you need to apply more than one condition at the same time. Listing more than one key ANDs the keys together automatically.

```json
{ "lang": "en", "status": "published" }
```

This returns documents where `lang` equals `en` and `status` equals `published`.

### Combine filters

You can combine the previous building blocks in one object. Combined keys AND together.

```json
{
  "status": "active",
  "owner": ["abby", "jaime"],
  "created_at": { "start": "2024-01-01", "end": "2024-12-31" }
}
```

This returns documents where `status` equals `active`, `owner` is `abby` or `jaime`, and `created_at` falls in 2024.

### List containment on an array-valued metadata field

Use the following example when you need an exact-match filter in a document metadata field array:

```json
{ "participant_email": "sam@example.com" }
```

This returns every document where `sam@example.com` appears among the values in the `participant_email` array.

### Narrow a bulk operation

Use the following example when you need to identify stale, unpublished documents:

```json

{
  "status": "draft",
  "updated_at": { "end": "2024-01-01" }
}
```

Returns a list of documents in `draft` status that were last updated before `2024-01-01`.

## Other data types

Exact match, the OR-list, `ne`, and `like` don't use integer, boolean, or numeric types. The Knowledge base by Workato stores and matches every metadata value as text.

- Exact match and the OR-list both check for an exact text match. A filter like `{"count": 5}` checks whether the stored text equals `5`. It doesn't perform numeric comparison.
- `like` matches wildcards against the exact stored value as text.
- The `{start, end}` range shape applies only to `created_at` and `updated_at`. Use [Field operators](#field-operators) to compare values on other fields.

You can list both values with an OR-list to match documents where `priority` is `4` or `5`:

```json
{ "priority": ["4", "5"] }
```

Alternatively, use `gte` when the field is numerically mapped:

```json
{ "priority": { "gte": 4 } }
```
