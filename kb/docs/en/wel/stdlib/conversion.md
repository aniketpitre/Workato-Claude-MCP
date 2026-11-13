---
url: 'https://docs.workato.com/en/wel/stdlib/conversion.md'
description: >-
  Use WEL conversion functions to cast values to Integer, Decimal, Float,
  String, Bool, Binary, temporal types, and the Null and Skip sentinels.
---

# Conversion functions

Conversion functions construct values of specific types. Each function uses the name of the type it produces and starts with a capital letter. For example, `Decimal('19.99')` creates a `Decimal` value.

Conversion functions give you explicit control over a value's type where inbound data enters an expression, because inbound data usually arrives as strings. WEL doesn't convert an argument to make a call succeed, except for [string interpolation](/en/wel/language/strings#f-strings) and one [Transform data](/en/wel/workato-expression-language-connector) flag that configures mixed precision coercion. Explicit conversion at the boundary keeps downstream operations type-safe and predictable.

> **CONVERT ONCE, AT THE EDGE**
> 
> Convert each field to its intended type in one place at the start of the transformation. Use those typed values throughout the remaining expression. Scattered conversions through an expression make it hard to see which fields have been handled, and raise the chance that a number gets rounded twice.

## Numbers

WEL has three numeric constructors, one for each numeric type.

### `Integer`

Converts to an `Integer`. Accepts an existing `Integer` or a string of digits.

```text
Integer(value)
```

| Parameter | Description |
| --- | --- |
| value | An `Integer` or an integer string. An integer string can include underscores as separators, such as `Integer('1_000_000')`. A string that contains anything other than a valid integer raises `E102`. For example, `Integer('3 items')` raises an error instead of returning `3`. |

Convert an integer string

The following example converts an integer string:

**Formula**

```text
Integer('42')
```

**Output**

```text
42
```

Pass through an existing integer

The following example passes an existing `Integer` through unchanged:

**Formula**

```text
Integer(42)
```

**Output**

```text
42
```

### `Decimal`

Converts to a `Decimal`, an exact, arbitrary-precision number.

Use `Decimal` for money. Pass the value as a string, such as `Decimal('19.99')`, so the exact digits reach the constructor. `Decimal(19.99)` converts a `Float` that's already approximate, which discards the exactness `Decimal` exists to preserve.

`Decimal` also preserves scale, so `Decimal('12.50')` keeps its trailing zero through arithmetic and a total stays a currency amount rather than becoming `12.5`.

```text
Decimal(value)
```

| Parameter | Description |
| --- | --- |
| value | A number or a numeric string. A string that isn't a valid number, such as `Decimal('notanumber')`, raises `E020`. |

Convert a decimal string

The following example converts a decimal string:

**Formula**

```text
Decimal('19.99')
```

**Output**

```text
19.99
```

Convert an integer to a Decimal

The following example converts an integer to a `Decimal`:

**Formula**

```text
Decimal(5)
```

**Output**

```text
5
```

### `Float`

Converts to a `Float`, a binary floating-point number.

Appropriate for measurements, ratios, and scientific values, where approximate precision is acceptable. Not appropriate for money, because a `Float` can't represent most decimal fractions exactly. Refer to [Decimal](#decimal) for exact arithmetic instead.

```text
Float(value)
```

| Parameter | Description |
| --- | --- |
| value | A number or a numeric string. Enter `'inf'` and `'infinity'` for an infinite value. `'NaN'` and incomplete strings such as `'.5'` and `'5.'` raise `E102`. |

Convert a numeric string to a Float

The following example converts a numeric string to a `Float`:

**Formula**

```text
Float('3.14')
```

**Output**

```text
3.14
```

## Text and truth

The following constructors convert to `String`, `Bool`, and `Binary`:

### `String`

Converts a scalar value to a `String`, using the **data-plane** locale.

Rejects `Binary` and collections. A `List` or `Map` isn't turned into a string implicitly or by this function, and passing one raises `E100`. Use [to\_json](/en/wel/stdlib/json) or `to_wel` to serialize a collection deliberately. This restriction exists because a silently stringified collection is one of the hardest transformation bugs to notice downstream.

```text
String(value)
```

| Parameter | Description |
| --- | --- |
| value | A scalar value. |

Convert an integer to a string

The following example converts an integer to a string:

**Formula**

```text
String(42)
```

**Output**

```text
42
```

Convert a Decimal to a string

The following example converts a `Decimal` to a string:

**Formula**

```text
String(Decimal('19.99'))
```

**Output**

```text
19.99
```

### `Bool`

Converts a value to a `Boolean`. Accepts an existing `Boolean`, or the strings `'true'` and `'false'`.

`'yes'`, `'1'`, and `'Y'` aren't accepted because their meaning depends on the source system, and an unrecognized string raises `E102`. Map source-specific values to a `Boolean` explicitly:

```text
if _.flag == 'Y' then true else false
```

```text
Bool(value)
```

| Parameter | Description |
| --- | --- |
| value | A `Boolean`, or the string `'true'` or `'false'`. |

Convert the string 'true'

The following example converts the string `'true'` to a `Boolean`:

**Formula**

```text
Bool('true')
```

**Output**

```text
true
```

### `Binary`

Converts an ASCII string to `Binary` bytes. An existing `Binary` value passes through unchanged.

Use [encode\_string](/en/wel/stdlib/encoding), which takes an explicit encoding, for text that isn't ASCII.

```text
Binary(value)
```

| Parameter | Description |
| --- | --- |
| value | An ASCII string. Non-ASCII strings raise `E008`. Values that aren't a `String` or `Binary` and computed strings that become non-ASCII at runtime raise `E100`. |

Convert an ASCII string to bytes

The following example converts an ASCII string to `Binary` bytes:

**Formula**

```text
Binary('AB')
```

**Output**

```text
0x"4142"
```

## Dates and times

WEL distinguishes an exact instant from a calendar date or wall-clock time without a time zone. Choosing the correct type helps prevent date shifts across time zones. Refer to [Temporal functions](/en/wel/stdlib/temporal) for how to work with each type once it's constructed.

### `DateTime`

Converts to a `DateTime`, an exact instant with a time zone.

Use it to record an event happening, such as a creation timestamp, an event time, or an audit record.

```text
DateTime(value)
```

| Parameter | Description |
| --- | --- |
| value | A `DateTime`, an ISO 8601 string, or a map of components. A map of components defaults `hour` and `minute` to `0`. A `String` argument must carry an explicit offset or `Z`. An invalid string raises `E020`, and an unsupported type raises `E100`. A map component outside its valid range raises `E211`. |

Convert an ISO 8601 string with a zone

The following example converts an ISO 8601 string with a time zone:

**Formula**

```text
DateTime('2026-03-15T09:30:00Z')
```

**Output**

```text
2026-03-15T09:30:00Z
```

### `PlainDate`

Converts to a `PlainDate`, a calendar date with no time and no zone.

Use it for a date that is the same everywhere, such as an invoice date, a birth date, or a contract start. A `DateTime` stored in place of a `PlainDate` can shift a day when it crosses a zone boundary.

```text
PlainDate(value)
```

| Parameter | Description |
| --- | --- |
| value | An ISO 8601 date string, or a value carrying a date. An invalid date, such as a day that doesn't exist in the given month, raises `E020`. |

Convert an ISO 8601 date string

The following example converts an ISO 8601 date string:

**Formula**

```text
PlainDate('2026-03-15')
```

**Output**

```text
2026-03-15
```

### `PlainTime`

Converts to a `PlainTime`, a time of day with no date and no zone, such as a store opening time.

```text
PlainTime(value)
```

| Parameter | Description |
| --- | --- |
| value | A time-only string, or a map with `hour`, `minute`, and `second`. An invalid time, such as an out-of-range hour, raises `E020`. |

Convert an ISO 8601 time string

The following example converts an ISO 8601 time string:

**Formula**

```text
PlainTime('09:30:00')
```

**Output**

```text
09:30:00
```

### `PlainDateTime`

Converts to a `PlainDateTime`, a date and time with no zone.

`PlainDateTime` strips the zone from a `DateTime` argument rather than converting it, so the wall-clock reading is kept as-is.

```text
PlainDateTime(value)
```

| Parameter | Description |
| --- | --- |
| value | A map of components, an ISO 8601 string, or a `DateTime`. A `PlainDate` raises `E102` because it has no time component to supply. A map component outside its valid range raises `E211`. |

Convert an ISO 8601 date-time string

The following example converts an ISO 8601 date-time string:

**Formula**

```text
PlainDateTime('2026-03-15T09:30:00')
```

**Output**

```text
2026-03-15T09:30:00
```

### `Duration`

Converts to a `Duration`, a length of time written in ISO 8601 duration form. For example, `PT1H30M`.

```text
Duration(value)
```

| Parameter | Description |
| --- | --- |
| value | An ISO 8601 duration string, a value carrying a duration, or a map of components, such as `{hours: 1, minutes: 30}`. `Duration` normalizes negative component values and values above 60. The `month` and `year` components must be numbers. |

Convert an ISO 8601 duration string

The following example converts an ISO 8601 duration string:

**Formula**

```text
Duration('PT1H30M')
```

**Output**

```text
PT1H30M
```

## Sentinels

WEL uses the `Null()` constructor or the `Skip` sentinel value to represent an absence.

### `Null`

Returns `null`. Takes no arguments.

```text
Null()
```

Return null

The following example returns `null`:

**Formula**

```text
Null()
```

**Output**

```text
null
```

### `Skip`

`Skip` omits a field entirely instead of sending `null` for it. Refer to [Null and Skip](/en/wel/language/data-types#null-and-skip) for the full comparison, including how `Skip` filters a list inside `map_by`. Use `Skip` when a destination distinguishes an explicitly cleared field from an untouched one, which many CRM APIs do.

```text
Skip
```

### Use case: Convert an inbound payload at the boundary

Every field arrives as a string, including ones that logically aren't. Convert them once, at the top, so the rest of the transformation can work in real types:

**Input**

```json
{
  "id": 1001,
  "qty": "3",
  "total": "149.50",
  "shipped": "true",
  "ship_date": "2026-03-15"
}
```

**Formula**

```text
{
  order_id: String(_.id),
  qty: Integer(_.qty),
  total: Decimal(_.total),
  shipped: Bool(_.shipped),
  ship_date: PlainDate(_.ship_date)
}
```

**Output**

```json
{
  "order_id": "1001",
  "qty": 3,
  "total": 149.50,
  "shipped": true,
  "ship_date": "2026-03-15"
}
```

`total` keeps its trailing zero because `Decimal` preserves scale. `ship_date` is a `PlainDate`, so it can't drift a day when a later step applies a time zone.

## Related

- [Data types](/en/wel/language/data-types): The 16 WEL data types and when to use each one.
- [Numeric functions](/en/wel/stdlib/numeric): Round a `Decimal`.
- [Temporal functions](/en/wel/stdlib/temporal): Work with dates after conversion.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E008`, `E020`, `E100`, `E102`, and `E211`.

---
