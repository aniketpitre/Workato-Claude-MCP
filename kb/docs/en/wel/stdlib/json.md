---
url: 'https://docs.workato.com/en/wel/stdlib/json.md'
description: >-
  Use WEL JSON functions to parse JSON strings into WEL values, serialize WEL
  values back to JSON text, and query a structure with JSONPath.
---

# JSON functions

JSON functions convert between JSON text and WEL values, and query a structure by path.

Ordinary recipe data rarely needs JSON functions. Input fields already arrive as WEL values, and the [Transform data](/en/wel/workato-expression-language-connector) action serializes the result. Use these when JSON appears inside a field, such as a webhook that delivers its body as a string, a database column holding a JSON document, or a payload you must hand to a destination as text.

## Convert

The following functions convert between JSON text and WEL values:

### `parse_json`

Parses a JSON string into a WEL value.

```text
parse_json(text, options)
```

| Parameter | Description |
| --- | --- |
| text | The JSON string to parse. Non-string data types raise `E100`. Malformed JSON text raises `E209`. A JSON object with a repeated key, such as `{"a":1,"a":2}`, raises `E223` rather than silently keeping the last occurrence. Nesting between 129 levels and 256 levels raises `E222`. Nesting beyond 256 levels raises `E211` instead. |
| options | Optional map to control how the JSON parses. `numbers`: How to represent JSON numbers. Pass `'decimal'` to parse fractional numbers as `Decimal` rather than `Float`. An unrecognized option key raises `E225` rather than being ignored. |

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
> A JSON number with a fraction becomes a `Float`, so `149.50` parses to `149.5` and the scale is gone. Pass `{numbers: 'decimal'}` so it becomes an exact `Decimal` instead when the field is a currency amount. Refer to [Data types](/en/wel/language/data-types) for why `Decimal` matters for money.

### `to_json`

Serializes a WEL value to a JSON string.

WEL doesn't implicitly convert a `List` or `Map` to a string, because an accidental stringified collection is one of the hardest transformation bugs to spot downstream. Call this function or another explicit serializer to turn one into text instead.

```text
to_json(value, options)
```

| Parameter | Description |
| --- | --- |
| value | The value to serialize. An infinite float, or a top-level `Skip` value, raises `E210`. A lambda value raises `E107`. |
| options | Optional map of serialization settings. `spacing`: Whitespace to use between tokens.; `indent`: Indentation for `pretty` output.; `pretty`: Format the output across multiple lines.; `format_binary`: How to render `Binary` values. Accepts `'base64'`, `'base64url'`, or `'hex'`.; `format_datetime`: How to render `DateTime` values.; `format_date`: How to render `PlainDate` values.; `number_format`: How to render numbers. `'js_safe'` stringifies an integer outside the range a JSON number can represent exactly in JavaScript, instead of writing it as a bare number. An unrecognized option key raises `E225`. |

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

Queries a value using the subset of RFC 9535 JSONPath that WEL supports. Returns a `List` of matching nodes, or an empty list when nothing matches.

Supported selectors:

| Selector | Syntax | Meaning |
| --- | --- | --- |
| Root | `$` | The `value` passed in. `$` alone always matches, even when `value` is `null`. |
| Child | `.key`, `['key']` | A named field of a `Map`. Use the bracket form, `['key']`, when the key contains a character `.key` can't express, such as a space or a dot. |
| Index | `[0]`, `[-1]` | The element at a position in a `List`. A negative index counts from the end, so `[-1]` selects the last element. |
| Wildcard | `[*]`, `.*` | Every element of a `List`, or every value of a `Map`, with no filtering by position or key. |
| Recursive descent | `..key`, `..*` | Every match for `key`, or every value with `..*`, at any depth of nesting. |
| Slice | `[start:end:step]` | A range of a `List` from `start` up to but not including `end`, moving by `step` elements at a time. Omit `start` to default to the start of the list, omit `end` to default to the end of the list, or omit `step` to default to `1`. |

Filters, unions, and function extensions are real RFC 9535 features, however WEL doesn't support them, so they raise `E220`. Use [deep\_collect\_by](/en/wel/stdlib/deep-map) or [filter\_by](/en/wel/stdlib/list) instead. An invalid selector raises `E219`.

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

### `json_pointer`

Resolves one value using an [RFC 6901](https://www.rfc-editor.org/rfc/rfc6901) JSON pointer, such as `/a/b/0`. Unlike `json_path`, a pointer addresses exactly one location, so the result is the value itself rather than a `List`.

```text
json_pointer(value, pointer)
```

| Parameter | Description |
| --- | --- |
| value | The structure to query. |
| pointer | An RFC 6901 pointer as a `String`. Each token addresses a key when `value` is a `Map` (with no Unicode normalization applied), or an index when `value` is a `List`. A non-empty pointer must start with `/`. An empty string returns `value` unchanged, including `null` or `Skip`. Non-string data types raise `E100`. URI fragments (`#/a`), relative pointers, wildcards, and percent-decoding raise catchable `E229`. A pointer that's syntactically valid but can't be resolved raises `E230`. |

Within a token, `~1` decodes to `/` and `~0` decodes to `~`, so a key containing either character needs the escaped form. A `~` followed by anything else is invalid syntax and raises `E229`.

WEL raises `E230` for an out-of-range list index, a leading zero in an index, or the `-` append token, since `json_pointer` only resolves a value that already exists.

Both `E229` and `E230` are catchable, so `json_pointer(data, '/optional/value') |? null` supplies a fallback when the path may not exist.

Look up a nested field by pointer

**Formula**

```text
json_pointer(parse_json('{"a":{"b":1}}'), '/a/b')
```

**Output**

```text
1
```

## Related

- [Deep map functions](/en/wel/stdlib/deep-map): Collect values by predicate, including filters `json_path` doesn't support.
- [Map functions](/en/wel/stdlib/map): Information about `pluck`, `except`, and `flatten_map`.
- [Data types](/en/wel/language/data-types): Why `Decimal` matters when parsing money.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E100`, `E107`, `E209`, `E210`, `E211`, `E218`, `E219`, `E220`, `E222`, `E223`, `E229`, and `E230`.

---
