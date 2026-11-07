---
url: 'https://docs.workato.com/en/wel/stdlib/json.md'
description: >-
  WEL JSON functions for parsing JSON strings into WEL values, serializing WEL
  values back to JSON text, and querying a structure with JSONPath.
---

# JSON functions

JSON functions convert between JSON text and WEL values, and query a structure by path.

Ordinary recipe data rarely needs JSON functions. Input fields already arrive as WEL values, and the [Transform data](/en/wel/workato-expression-language-connector) action serializes the result. Use these when JSON appears inside a field, such as a webhook that delivers its body as a string, a database column holding a JSON document, or a payload you must hand to a destination as text.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Convert

The following functions convert between JSON text and WEL values:

### `parse_json`

Parses a JSON string into a WEL value.

```text
parse_json(text, options)
```

| Parameter | Description |
| --- | --- |
| text | The JSON string to parse. |
| options | Optional map to control how the JSON is parsed. `numbers`: How to represent JSON numbers., `decimal`: Parse fractional numbers as `Decimal` rather than `Float`. |

An unrecognized option key raises `E222` rather than being ignored.

Parse a JSON string into a WEL value

The following example parses a JSON string into a WEL value:

**Formula**

```text
parse_json('{"sku": "WID-1", "qty": 3}')
```

**Output**

```text
{sku: "WID-1", qty: 3}
```

> **PARSING MONEY LOSES PRECISION BY DEFAULT**
> 
> A JSON number with a fraction becomes a `Float`, so `149.50` parses to `149.5` and the scale is gone. Pass the `decimal` option so it becomes an exact `Decimal` instead when the field is a currency amount. Refer to [Data types](/en/wel/language/data-types) for why `Decimal` matters for money.

### `to_json`

Serializes a WEL value to a JSON string.

WEL doesn't implicitly convert a `List` or `Map` to a string, because an accidental stringified collection is one of the hardest transformation bugs to spot downstream. Call this function or another explicit serializer to turn one into text instead.

```text
to_json(value, options)
```

| Parameter | Description |
| --- | --- |
| value | The value to serialize. |
| options | Optional map of serialization settings. |

Serialize a WEL value to a JSON string

The following example serializes a WEL value to a JSON string:

**Formula**

```text
to_json({sku: 'WID-1', qty: 3})
```

**Output**

```text
{"sku":"WID-1","qty":3}
```

### Use case: Unpack a JSON string field

A webhook delivers its body as a single string field. Use JSON functions to parse it, then keep only the fields the destination accepts:

**Input**

```json
{
  "payload": "{\"order_id\":\"SO-1001\",\"total\":149.5,\"internal\":true}"
}
```

**Formula**

```text
parse_json(_.payload) >> pluck(['order_id', 'total'])
```

**Output**

```json
{"order_id": "SO-1001", "total": 149.5}
```

`pluck` is an allowlist, so `internal` is dropped and any field the source adds later is dropped too.

## Query by path

The following function queries a structure using a JSONPath expression, without parsing it into WEL values first:

### `json_path`

Queries a value using the subset of RFC 9535 JSONPath that WEL supports. Returns a `List` of matching nodes: an empty list when nothing matches, not `null`.

Supported selectors:

| Selector | Syntax | Meaning |
| --- | --- | --- |
| Root | `$` | The value passed in |
| Child | `.key`, `['key']` | A named field |
| Index | `[0]`, `[-1]` | Position in a list. Negative counts from the end |
| Wildcard | `[*]`, `.*` | Every element or every value |
| Recursive descent | `..key`, `..*` | Match at any depth |
| Slice | `[start:end:step]` | A range of a list |

Filters, unions, and function extensions are real RFC 9535 features that WEL doesn't currently support. They raise `E224`. Use [deep\_collect\_by](/en/wel/stdlib/deep-map) or [filter\_by](/en/wel/stdlib/list) instead. An invalid selector raises `E223`.

```text
json_path(value, path)
```

| Parameter | Description |
| --- | --- |
| value | The structure to query. |
| path | A JSONPath expression, as a `String`. |

Query a nested structure with a wildcard

The following example collects every price from a nested list using a wildcard:

**Formula**

```text
json_path({store: {book: [{price: 10}, {price: 20}]}}, '$.store.book[*].price')
```

**Output**

```text
[10, 20]
```

Query a value at any depth with recursive descent

The following example finds a key at any depth using recursive descent:

**Formula**

```text
json_path({a: {b: {c: 'x'}}}, '$..c')
```

**Output**

```text
["x"]
```

A path with no match returns an empty list

The following example returns an empty list when the path matches nothing:

**Formula**

```text
json_path({a: 1}, '$.missing')
```

**Output**

```text
[]
```

### Use case: Pull every SKU out of a nested response

An API returns orders, each with its own line items. Use a JSONPath expression to collect every SKU in one recursive path instead of walking each level individually:

**Input**

```json
{
  "orders": [
    {"line_items": [{"sku": "WID-1"}, {"sku": "GAD-7"}]},
    {"line_items": [{"sku": "BOX-2"}]}
  ]
}
```

**Formula**

```text
json_path(_, '$..line_items[*].sku')
```

**Output**

```json
["WID-1", "GAD-7", "BOX-2"]
```

The result is a list, so a payload with no orders yields `[]`. The following steps keep working rather than failing on a `null`.

## Related

- [Deep map functions](/en/wel/stdlib/deep-map): Collect values by predicate, including filters `json_path` doesn't support.
- [Map functions](/en/wel/stdlib/map): Information about `pluck`, `except`, and `flatten_map`.
- [Data types](/en/wel/language/data-types): Why `Decimal` matters when parsing money.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E222`, `E223`, and `E224`.

---
