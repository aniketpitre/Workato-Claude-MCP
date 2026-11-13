---
url: 'https://docs.workato.com/en/wel/language/data-types.md'
description: >-
  The 16 WEL data types, including numbers, text, temporal types, collections,
  and the Skip marker, and how to choose the right one for each field.
---

# Data types

WEL has 16 data types. Use the right type when data enters or leaves an expression to ensure bad values don't cause a transformation to silently fail.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

Two rules govern how every type in WEL behaves:

- **WEL doesn't coerce by default**: Passing a number where a `String` is expected raises `E100` rather than converting it. Nothing is silently reinterpreted to make an expression succeed, except inside [string interpolation](/en/wel/language/strings#f-strings), which converts automatically, and one [Transform data](/en/wel/workato-expression-language-connector) flag that configures a specific coercion.
- **Collections don't become strings by accident**: A `List` or `Map` is only serialized by an explicit call such as [to\_json](/en/wel/stdlib/json#to-json).

Both rules exist because a transformation that fails is visible, and one that silently produces the wrong value isn't.

## Quick reference

WEL contains the following data types:

| Type | Description | Literal |
| --- | --- | --- |
| [Null](#null-and-skip) | The absence of a value | `null` |
| [Bool](/en/wel/stdlib/conversion#bool) | A boolean | `true`, `false` |
| [Integer](#integer) | A whole number, arbitrary precision up to 1024 bytes | `42` |
| [Float](#float) | A 64-bit IEEE 754 floating-point number | `3.14` |
| [Decimal](#decimal) | An exact decimal, arbitrary precision up to 1024 bytes | `Decimal('1.00')` |
| [String](#string) | UTF-8 text | `'hello'` |
| [Binary](#binary) | Raw bytes | `0x"48656C6C6F"` |
| [PlainDate](#plain-date) | A calendar date, no time, no zone | `PlainDate('2026-03-15')` |
| [DateTime](#datetime) | An exact instant, with an offset | `DateTime('2026-03-15T09:30:00Z')` |
| [PlainDateTime](#plain-date-time) | A date and time, no zone | `PlainDateTime('2026-03-15T09:30:00')` |
| [PlainTime](#plain-time) | A time of day, no date, no zone | `PlainTime('09:30:00')` |
| [Duration](#duration) | A length of time | `Duration('PT2H30M')` |
| [List](#list) | An ordered collection | `[1, 2, 3]` |
| [Map](#map) | A key-value collection | `{a: 1}` |
| [Skip](#null-and-skip) | A marker meaning "omit this" | `Skip` |
| [Lambda](/en/wel/language/expressions#lambdas) | An inline function | `x ~> x * 2` |

> **CHECK A VALUE'S TYPE**
> 
> Use [type\_of](/en/wel/stdlib/common#type-of) to check a value's type.

## Numbers

WEL has three numeric types, and the choice between them is the most consequential type decision in most integrations.

### `Integer`

An `Integer` is a whole number, with arbitrary precision up to a 1024-byte (8192-bit) magnitude, including intermediate values. Every magnitude up to 2466 decimal digits fits. A 2467-digit magnitude fits only if it doesn't exceed `2^8192 - 1`. There is no 64-bit ceiling and no silent loss above `2^53`. A literal or constant that exceeds the limit raises a non-catchable `E020` error. A value computed at runtime raises a catchable `E211` error.

No 64-bit ceiling

The result in the following example is past the point where a JavaScript number would lose precision. The result remains precise because the numbers are integers which have no 64-bit ceiling:

| Formula | Result |
| --- | --- |
| `9007199254740993 + 1` | `9007199254740994` |

This allows record identifiers from systems that issue large integer keys to arrive intact.

### `Float`

A `Float` is a binary floating-point number. Float arithmetic is fast, and appropriate for measurements, ratios, percentages, and scientific values. `Float` can't represent most decimal fractions exactly. Use `Decimal` in cases where fraction precision matters, such as when working with money.

Fraction imprecision

The following example shows the imprecision of floats when working with fractions:

| Formula | Result |
| --- | --- |
| `0.1 + 0.2` | `0.30000000000000004` |

This happens because floats store numbers in base 2, where most decimal fractions have no exact representation. The same rounding appears in any language that uses binary floating point.

### `Decimal`

`Decimal` provides exact decimal arithmetic at arbitrary precision up to a 1024-byte magnitude. Use it for cases where fraction precision matters, such as when working with money.

Decimals preserve scale

`Decimal` preserves scale, so results in the following examples retain their digit count rather than picking up extra digits or collapsing:

| Formula | Result |
| --- | --- |
| `Decimal('0.1') + Decimal('0.2')` | Returns `0.3` with no additional digits. |
| `Decimal('12.50') + Decimal('0.00')` | Returns `12.50` without collapsing to `12.5`. |

This lets currency keep its exact value all the way to a destination.

> **USE STRINGS FOR DECIMAL CONVERSIONS**
> 
> Pass the [Decimal()](/en/wel/stdlib/conversion#decimal) conversion a string such as `Decimal('19.99')`, not a float such as `Decimal(19.99)`. The float form parses `19.99` as a `Float` first, which passes an imprecise value to `Decimal`. The string form gives `Decimal` the digits `19.99` directly, with nothing lost.

### Mix numeric types

`Integer` can combine with both `Decimal` and `Float`. `Decimal` and `Float` can't directly mix:

| Formula | Result |
| --- | --- |
| `1 + Decimal('1')` | `2` |
| `1.5 + Decimal('1')` | Raises `E103` |

The restriction prevents a `Float` from silently making a result approximate. Raising `E103` forces the approximation to be explicit. Fix `E103` by converting the `Float` operand to a `Decimal`, not by demoting the `Decimal` operand to a `Float`.

> **SCHEMA INFERENCE DOESN'T PRODUCE DECIMALS**
> 
> Pasting sample JSON into the [Transform data](/en/wel/workato-expression-language-connector) action infers `12.50` as a `Float`. Set the type manually if fraction precision matters for your use case, such as when working with money.

## Text and bytes

The following two types hold text and raw byte data:

### `String`

A `String` is UTF-8 text, in single or double quotes (`'` or `"`).

Measure length by code points or grapheme clusters

The [length](/en/wel/stdlib/common#length) function counts code points, not user-perceived characters or bytes:

| Formula | Result |
| --- | --- |
| `length('👨‍👩‍👧')` | `5` |
| `grapheme_length('👨‍👩‍👧')` | `1` |

Some emoji and accented letters are made of several code points, even though a reader would see one character. Use [grapheme\_length](/en/wel/stdlib/unicode#grapheme-length) to count user-perceived characters (grapheme clusters).

Concatenate strings

Concatenation with [++](/en/wel/language/operators#concatenation) requires matching types on both sides:

| Formula | Result |
| --- | --- |
| `'a' ++ 'b'` | `ab` |
| `'x' ++ 1` | Raises `E101` |

Convert the element first with [String(...)](/en/wel/stdlib/conversion#string), or use an f-string, which converts as it interpolates:

```text
f"Order {_.id} has {_.count} items"
```

### `Binary`

`Binary` is raw bytes, written in hexadecimal format. For example: `0x"48656C6C6F"`.

> **BINARY STRING CONVERSION**
> 
> The [String()](/en/wel/stdlib/conversion#string) conversion rejects a `Binary` rather than selecting a representation for it. Use one of the following conversions instead:
> 
> - Use [encode\_base64](/en/wel/stdlib/binary#encode-base64) or [encode\_hex\_string](/en/wel/stdlib/binary#encode-hex-string) for a text-safe form.
> - Use [decode\_string](/en/wel/stdlib/encoding#decode-string) with a named character encoding to read hexadecimal as text.

## Dates and times

WEL has five temporal types. Use the type that fits your use case to avoid common date bugs.

### `DateTime`

A `DateTime` is an exact instant with a time zone or offset. Use it to record the specific time of an event, such as the time something was created, shipped, or logged. For example: `DateTime('2026-03-15T09:30:00Z')`.

### `PlainDate`

A `PlainDate` is a calendar date with no time and no zone. Use it for a calendar date that's the same for everyone looking at it, such as an invoice date, a birth date, or a contract start date. For example: `PlainDate('2026-03-15')`.

> **USE PLAINDATE TO IGNORE TIMEZONES**
> 
> The same point in time can have different dates across timezones. For example, `2026-03-15T00:00:00Z` is the 15th at 9am in Tokyo and the _14th_ at 5pm in Los Angeles.
> 
> A `PlainDate` has no timezone, so it reads as the same date for everyone. Storing an invoice date as a `DateTime` instead of a `PlainDate` is the most common source of off-by-one-day errors.

### `PlainTime`

A `PlainTime` is a time of day with no date and no zone. Use it for a time of day with no date attached, such as a store's opening time or a daily cutoff. For example: `PlainTime('09:30:00')`.

### `PlainDateTime`

A `PlainDateTime` is a date and time with no zone. Use it for a wall-clock reading before its time zone is known, such as a local time a source system sends with the zone supplied separately. For example: `PlainDateTime('2026-03-15T09:30:00')`.

### `Duration`

A `Duration` holds a fixed clock duration, not a calendar unit, written `Duration('PT2H30M')`. Use it for a length of time, such as an age, an elapsed interval between two events, or a timeout.

Clock durations vs calendar units

A calendar unit such as a day can vary in actual length across a daylight-saving change, so `Duration` only accepts a fixed clock length such as hours or minutes, not a calendar unit such as days. For example:

| Formula | Result |
| --- | --- |
| `Duration('PT72H')` | 3 days |
| `Duration('P3D')` | Raises `E020` |

Refer to the [Temporal functions](/en/wel/stdlib/temporal) documentation for more information.

## Collections

WEL has two collection types. A `List` contains ordered data and a `Map` contains key-value data.

### `List`

A `List` is an ordered collection that can contain elements of mixed type. Wrap the list in brackets and separate values with commas. For example: `[1, 2, 3]`.

Refer to the [List functions](/en/wel/stdlib/list) documentation for more information.

### `Map`

A `Map` is a key-value collection and the WEL type for JSON objects. Keys are `String`, and insertion order is preserved. Wrap the map in curly braces and separate pairs with commas. For example: `{a: 1, b: 2}`.

Refer to the [Map functions](/en/wel/stdlib/map) documentation for more information.

### Collections don't become strings

A `List` or `Map` doesn't become a `String` automatically:

| Formula | Result |
| --- | --- |
| `String([1, 2])` | Raises `E100` |

The restriction exists because an accidentally stringified collection, such as a whole array arriving in a destination field as `[object Object]` or a bracketed blob, is one of the hardest integration bugs to trace. Raising `E100` forces conversions to be explicit. Call [to\_json](/en/wel/stdlib/json#to-json) for JSON, [to\_wel](/en/wel/stdlib/formatting#to-wel) for a WEL literal, or [join\_to\_string](/en/wel/stdlib/formatting#join-to-string) for a delimited list, depending on what the destination expects.

## `Null` and `Skip`

`null` and `Skip` both describe an absence, but their behavior differs in many destination systems:

- `null`: The field has no value. The key is still emitted.
  
- `Skip`: Don't emit this at all. The key is left out of a map.
  

| Formula | Result |
| --- | --- |
| `{a: 1, b: Skip}` | `{a: 1}` |

This distinction is especially common in CRM update APIs. Sending `null` clears a field, while omitting the key with `Skip` leaves it untouched.

Filter and transform a list with map\_by

Returning [Skip](/en/wel/stdlib/conversion#skip) from a [map\_by](/en/wel/stdlib/list#map-by) lambda drops that element from the result. This means a single pass can filter and transform together:

| Formula | Result |
| --- | --- |
| `[1, -2, 3] >> map_by(n ~> if n > 0 then n else Skip)` | `[1, 3]` |

## Test for values

[present?](/en/wel/stdlib/common#present) is the general test, and it treats every kind of absence the same way:

| Formula | Result |
| --- | --- |
| `present?('SO-1001')` | `true` |
| `present?(' ')` | `false` |
| `present?(null)` | `false` |
| `present?([])` | `false` |
| `present?(false)` | `true` |

`present?(false)` returns `true`, because it's a real value a pipeline can carry deliberately, not a stand-in for missing data the way `null` or an empty string is.

[presence](/en/wel/stdlib/common#presence-function) reports every kind of absence as `null` so one [fallback operator](/en/wel/language/operators#null-value-fallback) (`|` ) catches them all, including empty strings, whitespace-only strings, empty lists, and empty maps.

## Convert between types

Each type has a constructor, such as [Integer(...)](/en/wel/stdlib/conversion#integer), [Decimal(...)](/en/wel/stdlib/conversion#decimal), or [PlainDate(...)](/en/wel/stdlib/conversion#plain-date). Constructors are strict, for example: `Integer('3 items')` raises `E102` rather than partially parsing.

The most reliable shape for a transformation is to convert every field at the start:

```text
{
  order_id: String(_.id),
  qty: Integer(_.qty),
  total: Decimal(_.total),
  ship_date: PlainDate(_.ship_date)
}
```

Refer to the [Conversion functions](/en/wel/stdlib/conversion) documentation for more information.

## Related

- [Standard library](/en/wel/stdlib): Information about every WEL function.
- [Conversion functions](/en/wel/stdlib/conversion): How to construct each data type.
- [Error codes](/en/wel/errors): Troubleshoot errors such as `E100`, `E101`, `E102`, and `E103`.
- [Transform data](/en/wel/workato-expression-language-connector): Declare data types in the Transform data action.

---
