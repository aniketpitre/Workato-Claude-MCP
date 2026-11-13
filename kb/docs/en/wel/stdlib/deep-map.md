---
url: 'https://docs.workato.com/en/wel/stdlib/deep-map.md'
description: >-
  Use WEL deep map functions to collect values and transform leaf values
  anywhere inside a deeply nested API response, regardless of depth.
---

# Deep map functions

Deep map functions walk an entire structure, through every nested map and list, instead of operating on one level. Use them when the shape of an API response varies, when the target value could be at any depth, or when a rule must apply to every leaf regardless of where it sits.

## Use cases

Prefer an explicit path when the location of the value is known in advance. For example, `_.order.customer.email` says what it means, fails loudly when the shape changes, and can't pick up an unrelated `email` from somewhere else in the payload.

Use a deep function when:

- The depth genuinely varies between payloads.
- A rule applies to every value of a kind, such as trimming every string or encoding every `Binary`, regardless of position.
- The goal is to collect every occurrence of something, rather than one known field.

Use [json\_path](/en/wel/stdlib/json) instead for path queries with wildcards, indexing, or slices.

> **DEEP WALKS MATCH BROADLY**
> 
> `deep_collect(_, 'id')` returns _every_ `id` in the payload, including for the order, the customer, and each line item. Use a direct field access path instead, such as `_.order.id`, to return one ID.

## Collect values

Both collectors do a depth-first, pre-order walk through maps and lists. A matched value is collected _and_ descended into when it's itself a map or a list. Pass `shallow` as `true` to collect a matched container without descending into it.

### `deep_collect`

Collects every value whose map key matches the given name, at any depth. Returns an empty list when nothing matches.

```text
deep_collect(value, key, shallow)
```

| Parameter | Description |
| --- | --- |
| value | The structure to walk. |
| key | The key name to match, as a `String`. |
| shallow | Optional `Boolean`. A matched container is collected but not descended into when `true`. Defaults to `false`. |

Collect every id at any depth

The following example collects every `id` value at any depth:

**Formula**

```text
deep_collect({order: {id: 'SO-1', customer: {id: 'C-9'}}}, 'id')
```

**Output**

```text
["SO-1", "C-9"]
```

### `deep_collect_by`

Collects every value for which a predicate returns `true`. The predicate receives the key and the value, so it can match on either or both.

```text
deep_collect_by(value, predicate, shallow)
```

| Parameter | Description |
| --- | --- |
| value | The structure to walk. |
| predicate | A lambda taking `(key, value)` and returning a `Boolean`. A predicate that doesn't return a `Boolean` raises `E100`. A predicate that doesn't take exactly two parameters raises `E105`. |
| shallow | Optional `Boolean`. A matched container is collected but not descended into when `true`. Defaults to `false`. |

Collect values matching a key-and-value predicate

The following example collects values whose key is `Amount` and whose value exceeds 10:

**Formula**

```text
deep_collect_by({order: {Amount: 5}, items: [{Amount: 20}]}, (k, v) ~> k == 'Amount' and v > 10)
```

**Output**

```text
[20]
```

### Use case: Gather every email address in a payload

A CRM response carries addresses in several places, and the same one can appear twice. Use deep map functions to collect them all, then deduplicate:

**Input**

```json
{
  "primary": {"email": "nur@example.com"},
  "contacts": [
    {"email": "dana@example.com"},
    {"email": "nur@example.com"}
  ]
}
```

**Formula**

```text
deep_collect(_, 'email') >> unique
```

**Output**

```json
["nur@example.com", "dana@example.com"]
```

`deep_collect` reaches both the top-level map and the nested list without either path being named. `unique` keeps the first occurrence of each address.

## Transform leaves

The following function transforms every leaf value in a structure that matches a condition, regardless of depth:

### `deep_map_values_by`

Walks the whole structure and applies a transform to leaf values, returning a structure of the same shape.

An optional second lambda selects which leaves to transform. Values it rejects are left exactly as they are. This behavior makes a type-specific rule safe to apply across a payload of mixed types.

```text
deep_map_values_by(value, transform, condition)
```

| Parameter | Description |
| --- | --- |
| value | The structure to walk. |
| transform | A lambda returning the new value for each selected leaf. The function removes entries from the list or map where `transform` returns `Skip`. |
| condition | Optional lambda returning a `Boolean` for each leaf. Every leaf is transformed when omitted. |

Multiply every leaf value

The following example multiplies every leaf value in a nested structure:

**Formula**

```text
deep_map_values_by({a: 1, b: [2, 3]}, x ~> x * 10)
```

**Output**

```text
{a: 10, b: [20, 30]}
```

### Use case: Trim every string in an inbound payload

Whitespace from a source system can appear on any field at any depth. Use deep map functions to trim every field in one pass, leaving non-string values untouched:

**Input**

```json
{
  "customer": {
    "name": "  Nur  ",
    "tags": ["  vip  ", "new"]
  },
  "qty": 3
}
```

**Formula**

```text
deep_map_values_by(
  _,
  v ~> trim(v),
  v ~> type_of(v) == 'String'
)
```

**Output**

```json
{
  "customer": {"name": "Nur", "tags": ["vip", "new"]},
  "qty": 3
}
```

The condition lambda is what makes this safe. Without it, `trim` would run on `qty` and raise `E100`, because WEL doesn't coerce a number to a string to make the call succeed.

## Related

- [Map functions](/en/wel/stdlib/map): Single-level reading, merging, and `flatten_map`.
- [List functions](/en/wel/stdlib/list): What to do with a collected list.
- [JSON functions](/en/wel/stdlib/json): Use `json_path` for wildcards, indexing, and slices.
- [Common functions](/en/wel/stdlib/common): Use `type_of` to write condition lambdas.

---
