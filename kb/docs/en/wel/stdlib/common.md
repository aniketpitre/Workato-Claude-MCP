---
url: 'https://docs.workato.com/en/wel/stdlib/common.md'
description: >-
  WEL common functions for measuring length, testing whether a value is present,
  providing a fallback when it isn't, and inspecting a value's type.
---

# Common functions

Common functions work on values of any type. Almost every transformation needs to know whether a usable value is present and what type it's holding, and these functions answer both. They are the backbone of writing expressions that survive imperfect inbound data.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Measure

The following function measures the size of a value, in the unit appropriate to its type:

### `length`

Returns the length of a `String` in code points, the number of elements in a `List`, or the number of keys in a `Map`.

`length` counts code points, not bytes, for a string. Some emoji and accented letters are made of several code points combined into a single user-perceived character (grapheme cluster). Refer to [Unicode functions](/en/wel/stdlib/unicode) for grapheme clusters.

```text
length(value)
```

| Parameter | Description |
| --- | --- |
| value | A `String`, `List`, or `Map`. |

Count code points in a string

The following example counts each code point in the string:

**Formula**

```text
length('hello')
```

**Output**

```text
5
```

Count elements in a list

The following example counts each element in the list:

**Formula**

```text
length(['a', 'b'])
```

**Output**

```text
2
```

Count keys in a map

The following example counts each key in the map:

**Formula**

```text
length({a: 1, b: 2, c: 3})
```

**Output**

```text
3
```

## Test for a usable value

The following functions test whether a value is actually usable, not just non-null:

### `present?`

Returns `true` when a value is actually usable: not `null`, not empty, not whitespace-only, and not `NaN` or `Infinity`. Works on every data type.

`false` returns as `true` because it's a meaningful value in a pipeline, not an absence. This differs from Ruby's `blank?`.

```text
present?(value)
```

| Parameter | Description |
| --- | --- |
| value | Any value except a `Regex`, which raises `E100`. |

A non-empty string is present

The following example tests a non-empty string:

**Formula**

```text
present?('SO-1001')
```

**Output**

```text
true
```

A whitespace-only string isn't present

The following example tests a whitespace-only string:

**Formula**

```text
present?('   ')
```

**Output**

```text
false
```

Null isn't present

The following example tests a `null` value:

**Formula**

```text
present?(null)
```

**Output**

```text
false
```

An empty list isn't present

The following example tests an empty list:

**Formula**

```text
present?([])
```

**Output**

```text
false
```

False is present

The following example tests a boolean `false` value, which is meaningful data, not an absence:

**Formula**

```text
present?(false)
```

**Output**

```text
true
```

### `presence`

Returns the value when it's present, and `null` when it isn't.

`presence` is the companion to `present?`, and the two are for different jobs. `present?` gives you a `Boolean` to branch on. `presence` normalizes every kind of absence: empty string, whitespace-only string, empty list or map, `NaN`, `Infinity`, down to a single `null`. This lets the fallback operator `|` catch all of them at once:

```text
presence(_.nickname) | 'none'
```

Without `presence`, a field containing `' '` isn't `null`, so `|` would pass the whitespace straight through.

```text
presence(value)
```

| Parameter | Description |
| --- | --- |
| value | Any value except a `Regex`, which raises `E100`. |

A usable value passes through unchanged

The following example passes a usable value through unchanged:

**Formula**

```text
presence('SO-1001')
```

**Output**

```text
SO-1001
```

A whitespace-only string normalizes to null

The following example normalizes a whitespace-only string to `null`:

**Formula**

```text
presence('   ')
```

**Output**

```text
null
```

### Use case: Pick the first name that is actually filled in

A CRM export supplies a display name that is sometimes blank and a legal name that is sometimes missing. Chain `presence` with `|` to fall through to the first usable one:

**Input**

```json
{
  "contacts": [
    {"id": "C-1", "display_name": "  ", "legal_name": "Kalani Park"},
    {"id": "C-2", "display_name": "Noam", "legal_name": "Noam Gupta"},
    {"id": "C-3", "display_name": null, "legal_name": null}
  ]
}
```

**Formula**

```text
_.contacts >> map_by(c ~> {
  id: c.id,
  name: presence(c.display_name) | presence(c.legal_name) | 'Unknown'
})
```

**Output**

```json
[
  {"id": "C-1", "name": "Kalani Park"},
  {"id": "C-2", "name": "Noam"},
  {"id": "C-3", "name": "Unknown"}
]
```

`C-1` falls through because `' '` is blank rather than missing, exactly the case a plain `null` check would let slip through to the destination.

## Inspect a type

The following function reports which of the 16 WEL types a value actually is:

### `type_of`

Returns the name of a value's type as a `String`.

Most useful for writing condition lambdas, which decide which leaves of a payload a rule should apply to, and for diagnosing a transformation that is failing on unexpected input.

```text
type_of(value)
```

| Parameter | Description |
| --- | --- |
| value | Any value. |

A string

The following example returns the type of a string:

**Formula**

```text
type_of('SO-1001')
```

**Output**

```text
String
```

An integer

The following example returns the type of an integer:

**Formula**

```text
type_of(42)
```

**Output**

```text
Integer
```

A decimal

The following example returns the type of a decimal:

**Formula**

```text
type_of(Decimal('1.50'))
```

**Output**

```text
Decimal
```

A list

The following example returns the type of a list:

**Formula**

```text
type_of([1])
```

**Output**

```text
List
```

A map

The following example returns the type of a map:

**Formula**

```text
type_of({a: 1})
```

**Output**

```text
Map
```

Null

The following example returns the type of a `null` value:

**Formula**

```text
type_of(null)
```

**Output**

```text
Null
```

> **TYPE\_OF REPORTS WHAT YOU ACTUALLY HAVE**
> 
> `type_of(42)` is `Integer` and `type_of(Decimal('1.50'))` is `Decimal`, even though both look like numbers. Check the type when arithmetic produces a result you didn't expect. It's the recommended way to determine why. Refer to [Data types](/en/wel/language/data-types) for what each WEL type represents.

## Related

- [Data types](/en/wel/language/data-types): The 16 WEL data types and when to use each one.
- [Operators](/en/wel/language/operators): More information about the fallback operator `|`.
- [Deep map functions](/en/wel/stdlib/deep-map): Use `type_of` inside condition lambdas.
- [Unicode functions](/en/wel/stdlib/unicode): Count text the way a reader sees it.

---
