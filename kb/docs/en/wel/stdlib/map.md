---
url: 'https://docs.workato.com/en/wel/stdlib/map.md'
description: >-
  WEL map functions for reading keys and values, merging maps, picking and
  removing fields, and flattening nested objects into a single level.
---

# Map functions

A `Map` is a set of key-value pairs: the WEL type for a JSON object. Map functions read its keys and values, combine one map with another, remove fields, and convert between a map and a list so that list functions can operate on it.

Keys are `String` by default. Insertion order is preserved, so a map built in a deliberate order serializes in that order.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Call a map function

Call a function directly, or pipe a value into it with `>>`:

```text
keys(_.customer)
_.customer >> keys
```

Read a field with a period (`.`), or with brackets (`[]`) when the key is computed or isn't a bare identifier:

```text
_.customer.email
_.customer['email']
```

Reading a key that doesn't exist raises `E104`. Use `has_key?` to test first, or the try-fallback operator `|?` to supply a default:

```text
_.customer.nickname |? 'none'
```

## Read keys and values

The following functions read a map's keys and values without changing it:

### `keys`

Returns the keys as a list, in insertion order.

```text
keys(map)
```

| Parameter | Description |
| --- | --- |
| map | The map to read. |

Get the keys of a map

The following example returns the keys of a map, in insertion order:

**Formula**

```text
keys({sku: 'WID-1', qty: 3})
```

**Output**

```text
["sku", "qty"]
```

### `values`

Returns the values as a list, in insertion order. Values that are `Skip` are omitted.

```text
values(map)
```

| Parameter | Description |
| --- | --- |
| map | The map to read. |

Get the values of a map

The following example returns the values of a map, in insertion order:

**Formula**

```text
values({sku: 'WID-1', qty: 3})
```

**Output**

```text
["WID-1", 3]
```

### `has_key?`

Returns `true` if the key is present.

A test for the key isn't the same as a test for a value. A key present with a `null` value returns `true` here. Use `present?` instead to test for a usable value.

```text
has_key?(map, key)
```

| Parameter | Description |
| --- | --- |
| map | The map to test. |
| key | The key name, as a `String`. |

A present key returns true

The following example tests a key that is present in the map:

**Formula**

```text
has_key?({sku: 'WID-1'}, 'sku')
```

**Output**

```text
true
```

A missing key returns false

The following example tests a key that isn't present in the map:

**Formula**

```text
has_key?({sku: 'WID-1'}, 'qty')
```

**Output**

```text
false
```

## Choose fields

The following functions narrow a map to a smaller, safer set of fields:

### `pluck`

Returns a map containing only the named keys. Keys that aren't present are skipped rather than raising an error.

Use it to narrow a large inbound record to the fields a destination actually accepts.

```text
pluck(map, keys)
```

| Parameter | Description |
| --- | --- |
| map | The map to read from. |
| keys | A list of key names to keep. |

Keep only the named keys

The following example keeps only the named keys from the map:

**Formula**

```text
pluck({id: 1, secret: 'x', name: 'a'}, ['id', 'name'])
```

**Output**

```text
{id: 1, name: "a"}
```

A missing key is skipped rather than raising an error

The following example plucks a key that isn't present, which is skipped rather than raising an error:

**Formula**

```text
pluck({id: 1}, ['id', 'missing'])
```

**Output**

```text
{id: 1}
```

### `except`

Returns a map with the named keys removed.

`pluck` and `except` are opposites, and the choice between them matters for safety. `pluck` is an allowlist, so a new field appearing upstream is dropped by default. `except` is a denylist, so a new field is forwarded by default. Prefer `pluck` when leaking a newly added field is the concern.

```text
except(map, keys)
```

| Parameter | Description |
| --- | --- |
| map | The map to read from. |
| keys | A list of key names to remove. |

Remove the named keys

The following example removes the named keys from the map:

**Formula**

```text
except({id: 1, secret: 'x', name: 'a'}, ['secret'])
```

**Output**

```text
{id: 1, name: "a"}
```

### Use case: Drop sensitive fields before forwarding

An inbound user record carries credentials that shouldn't reach the destination system. Use `except` to drop the sensitive fields before forwarding the record:

**Input**

```json
{
  "user": {
    "id": "U-1",
    "email": "nur@example.com",
    "password": "hunter2",
    "ssn": "111-22-3333"
  }
}
```

**Formula**

```text
_.user >> except(['password', 'ssn'])
```

**Output**

```json
{"id": "U-1", "email": "nur@example.com"}
```

This use of `except` is the denylist form, and it's only safe while you know every field the source can send. `pluck(['id', 'email'])` is the safer expression of the same intent if the source may add fields.

## Combine maps

The following function combines two maps into one:

### `merge`

Combines two maps. The second wins when both define the same key.

```text
merge(first, second)
```

| Parameter | Description |
| --- | --- |
| first | The base map. |
| second | The map whose values take precedence. |

Merge two maps, second wins on conflict

The following example merges two maps, where the second map's value wins on a shared key:

**Formula**

```text
merge({sku: 'WID-1', qty: 1}, {qty: 5})
```

**Output**

```text
{sku: "WID-1", qty: 5}
```

### Use case: Apply overrides to a set of defaults

A set of defaults needs caller-supplied overrides applied on top, so anything supplied wins and anything omitted falls back. Use `merge` with the defaults first and the caller's values second:

**Input**

```json
{
  "overrides": {"currency": "EUR", "notify": true}
}
```

**Formula**

```text
merge(
  {currency: 'USD', locale: 'en-US', notify: false},
  _.overrides
)
```

**Output**

```json
{"currency": "EUR", "locale": "en-US", "notify": true}
```

`merge` combines one level. A nested map in the second argument replaces its counterpart outright rather than being merged into it.

## Convert between maps and lists

These four functions are how a map reaches the [list functions](/en/wel/stdlib/list). `entries` and `pairs` go one way. `from_entries` and `from_pairs` come back.

### `entries`

Converts a map to a list of `{key, value}` maps.

```text
entries(map)
```

| Parameter | Description |
| --- | --- |
| map | The map to convert. |

Convert a map to a list of key/value maps

The following example converts a map to a list of `{key, value}` maps:

**Formula**

```text
entries({sku: 'WID-1', qty: 3})
```

**Output**

```text
[{key: "sku", value: "WID-1"}, {key: "qty", value: 3}]
```

### `from_entries`

Converts a list of `{key, value}` maps back to a map. The inverse of `entries`.

```text
from_entries(list)
```

| Parameter | Description |
| --- | --- |
| list | A list of maps, each with a `key` and a `value`. |

Convert a list of key/value maps back to a map

The following example converts a list of `{key, value}` maps back to a map:

**Formula**

```text
from_entries([{key: 'sku', value: 'WID-1'}])
```

**Output**

```text
{sku: "WID-1"}
```

### `pairs`

Converts a map to a list of two-element `[key, value]` lists. Pairs whose value is `Skip` are omitted.

```text
pairs(map)
```

| Parameter | Description |
| --- | --- |
| map | The map to convert. |

Convert a map to a list of key/value pairs

The following example converts a map to a list of two-element `[key, value]` lists:

**Formula**

```text
pairs({sku: 'WID-1', qty: 3})
```

**Output**

```text
[["sku", "WID-1"], ["qty", 3]]
```

### `from_pairs`

Converts a list of two-element `[key, value]` lists back to a map. The inverse of `pairs`.

```text
from_pairs(list)
```

| Parameter | Description |
| --- | --- |
| list | A list of two-element lists. |

Convert a list of key/value pairs back to a map

The following example converts a list of two-element `[key, value]` lists back to a map:

**Formula**

```text
from_pairs([['sku', 'WID-1']])
```

**Output**

```text
{sku: "WID-1"}
```

> **FILTER A MAP WITHOUT CONVERTING IT**
> 
> [filter\_by](/en/wel/stdlib/list) accepts a map directly. The lambda receives two parameters, the key and the value, and the result is a map:
> 
> ```text
> {a: 1, b: 2} >> filter_by((k, v) ~> v > 1)
> ```

## Flatten nested maps

The following function collapses a nested map into a single level, joining the path into one key:

### `flatten_map`

Collapses nested maps into a single level, joining the path into one key.

The walk is depth-first in insertion order. Only maps are descended into. A list is treated as a leaf value and kept whole. An empty nested map is also a leaf.

Two nested keys can collapse onto the same flattened key. The last write wins and an `E229` warning is emitted when that happens, so the collision is visible in the job rather than silent.

```text
flatten_map(map, options)
```

| Parameter | Description |
| --- | --- |
| map | The map to flatten. |
| options | Optional map to control the flattening. `sep`: Key separator. Defaults to `.`., `max_depth`: How many levels to descend. Defaults to unlimited. |

An unrecognized option key raises `E222` rather than being ignored.

Flatten a nested map with the default separator

The following example flattens a nested map, joining the path with the default `.` separator:

**Formula**

```text
flatten_map({customer: {name: 'Nur', address: {city: 'London'}}})
```

**Output**

```text
{"customer.name": "Nur", "customer.address.city": "London"}
```

Flatten a nested map with a custom separator

The following example flattens a nested map using a custom separator:

**Formula**

```text
flatten_map({a: {b: 1}}, {sep: '_'})
```

**Output**

```text
{a_b: 1}
```

### Use case: Flatten a record for a CSV row

A CSV destination needs one column per field, but the source is nested two levels deep. Use map functions to flatten the record into a single level:

**Input**

```json
{
  "record": {
    "id": "C-1",
    "customer": {
      "name": "Nur",
      "address": {"city": "London", "postcode": "E1"}
    }
  }
}
```

**Formula**

```text
_.record >> flatten_map
```

**Output**

```json
{
  "id": "C-1",
  "customer.name": "Nur",
  "customer.address.city": "London",
  "customer.address.postcode": "E1"
}
```

The flattened keys are exactly the column headers the destination expects. Pass `{sep: '_'}` if the target doesn't accept dots in header names.

## Related

- [List functions](/en/wel/stdlib/list): What to do with `entries`, `pairs`, `keys`, and `values`.
- [Deep map functions](/en/wel/stdlib/deep-map): Reach through nesting rather than flattening it.
- [Data types](/en/wel/language/data-types): `Map`, `Skip`, and `null`.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E104`, `E222`, and `E229`.

---
