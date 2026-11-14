---
url: 'https://docs.workato.com/en/wel/stdlib/formatting.md'
description: >-
  Use WEL formatting functions to render dates, times, numbers, and currency as
  display strings, parse datetimes, join lists, and serialize values to WEL.
---

# Formatting functions

Formatting functions turn values into the strings a person or a destination system reads. They also parse strings back into values.

The distinction that matters here is between _formatting_ and _converting_. `format_date` produces text for display or for a system that demands a particular layout. It doesn't produce a date. The result is a `String`, which doesn't support arithmetic. Keep values in their original types until the final formatting step.

## Format dates and times

`format_date`, `format_datetime`, and `format_time` each take a [strftime](https://man7.org/linux/man-pages/man3/strftime.3.html) pattern or a named preset. An unrecognized preset name doesn't raise an error. These functions treat it as a literal strftime pattern and return it unchanged, because it contains no directives to substitute. A malformed strftime pattern raises `E016`. The following table lists the common directives:

| Directive | Meaning | Example |
| --- | --- | --- |
| `%Y` | Four-digit year | `2026` |
| `%m` | Two-digit month | `03` |
| `%d` | Two-digit day | `15` |
| `%b` | Abbreviated month name | `Mar` |
| `%H` | Hour, 24-hour clock | `09` |
| `%M` | Minute | `30` |
| `%S` | Second | `00` |

### `format_date`

Formats a `PlainDate`.

```wel
format_date(date, pattern)
```

| Parameter | Description |
| --- | --- |
| date | The `PlainDate` to format. |
| pattern | A strftime pattern or a named preset. |

Format a date as day/month/year

The following example formats a date using a day/month/year pattern:

**Formula**

```wel
format_date(PlainDate('2026-03-15'), '%d/%m/%Y')
```

**Output**

```text
15/03/2026
```

### `format_datetime`

Formats a `DateTime` or a `PlainDateTime`.

```wel
format_datetime(datetime, pattern)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` or `PlainDateTime` to format. |
| pattern | A strftime pattern or a named preset. |

Format a datetime with date and time

The following example formats a datetime showing both the date and time:

**Formula**

```wel
format_datetime(DateTime('2026-03-15T09:30:00Z'), '%Y-%m-%d %H:%M')
```

**Output**

```text
2026-03-15 09:30
```

### `format_time`

Formats a `PlainTime`.

```wel
format_time(time, pattern)
```

| Parameter | Description |
| --- | --- |
| time | The `PlainTime` to format. |
| pattern | A strftime pattern or a named preset. |

Format a time as hour and minute

The following example formats a time as hour and minute:

**Formula**

```wel
format_time(PlainTime('09:30:00'), '%H:%M')
```

**Output**

```text
09:30
```

## Standard timestamp formats

Prefer `to_rfc3339` and `to_rfc2822` over a hand-written pattern when a protocol calls for a standard layout. These functions preserve the required format without relying on a manually maintained pattern.

### `to_rfc3339`

Formats a `DateTime` as RFC 3339, the format most JSON APIs expect. This function drops fractional seconds.

Produces the same output as [`to_iso8601`](/en/wel/stdlib/temporal#to-iso8601) for a `DateTime`.

```wel
to_rfc3339(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to format. Offsets with nonzero seconds raise `E212`. |

Format a datetime as RFC 3339

The following example formats a datetime as RFC 3339:

**Formula**

```wel
to_rfc3339(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
2026-03-15T09:30:00Z
```

### `to_rfc2822`

Formats a `DateTime` as RFC 2822, the format used in email headers. This function drops fractional seconds.

Renders the day and month names in English regardless of locale.

```wel
to_rfc2822(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to format. Offsets with nonzero seconds raise `E212`. |

Format a datetime as RFC 2822

The following example formats a datetime as RFC 2822:

**Formula**

```wel
to_rfc2822(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
Sun, 15 Mar 2026 09:30:00 +0000
```

## Parse a datetime

The following functions parse a string into a temporal type, the inverse of formatting one:

### `parse_datetime`

Parses a string into a `DateTime`.

```wel
parse_datetime(text, options)
```

| Parameter | Description |
| --- | --- |
| text | The string to parse. |
| options | Optional map to control how the string is parsed. `format`: A strftime pattern describing the input., `default_tz`: Time zone to assume when the input carries none., `on_gap`: How to resolve a time that doesn't exist because a daylight-saving change skipped it., `on_fold`: How to resolve a time that occurs twice because a daylight-saving change repeated it. An unrecognized option key raises `E225`. An unknown `default_tz` zone name raises `E214`. An invalid `on_gap` or `on_fold` value raises `E225`. |

A date-only ISO string with no `format` option, such as `'2024-03-15'`, raises `E212`.

Parse an RFC 3339 datetime string

The following example parses a datetime string in RFC 3339 format:

**Formula**

```wel
parse_datetime('2026-03-15T09:30:00Z')
```

**Output**

```text
2026-03-15T09:30:00Z
```

Parse a datetime using a custom format

The following example parses a datetime string using a custom day/month/year format:

**Formula**

```wel
parse_datetime('15/03/2026', {format: '%d/%m/%Y'})
```

**Output**

```text
2026-03-15T00:00:00Z
```

> **A DATE-ONLY STRING BECOMES MIDNIGHT UTC**
> 
> The second row parses to `00:00:00Z`, because a `DateTime` must have a time and a zone and the input supplied neither. Use `PlainDate` instead if the value is a calendar date rather than an instant. A `PlainDate` can't shift a day when a later step applies a zone.
> 
> Use `default_tz` when the input has no zone but you know which one it came from. Without it, `on_gap` and `on_fold` decide what happens on the two days a year when a local time is ambiguous or doesn't exist.

### `parse_plain_datetime`

Parses a string into a `PlainDateTime`, with no zone attached.

```wel
parse_plain_datetime(text, options)
```

| Parameter | Description |
| --- | --- |
| text | The string to parse. A string carrying a UTC offset or zone designation raises `E102`, because a `PlainDateTime` has no zone to hold it. |
| options | Optional map with a `format` key. An unrecognized option key raises `E225`. |

Parse a plain datetime using a custom format

The following example parses a plain datetime string using a custom format:

**Formula**

```wel
parse_plain_datetime('2026-03-15 09:30', {format: '%Y-%m-%d %H:%M'})
```

**Output**

```text
2026-03-15T09:30:00
```

## Format numbers

Both of these use the **data-plane** locale, which is configured on the [Transform data](/en/wel/workato-expression-language-connector) action rather than passed as an argument. The same expression renders differently for different locales.

The following examples show the default locale, `en-US`.

### `to_local_string`

Formats a number using the locale's grouping and decimal separators.

```wel
to_local_string(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to format. |

Format a number using locale grouping

The following example formats a number using the locale's grouping and decimal separators:

**Formula**

```wel
to_local_string(1234567.891)
```

**Output**

```text
1,234,567.89
```

### `to_local_currency`

Formats a number as a currency amount, using the locale's currency symbol and conventions. Rounds to the currency's standard number of fractional digits, for example 2 for USD and EUR, 0 for JPY, and 3 for BHD, and places the negative sign where the locale convention puts it. Renders `Infinity` as literal text rather than a numeric-looking string.

```wel
to_local_currency(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to format. A non-number value raises `E100`. |

Format a number as a currency amount

The following example formats a number as a currency amount:

**Formula**

```wel
to_local_currency(1234.5)
```

**Output**

```text
$1,234.50
```

## Join a list into a string

The following functions join a list's elements into a single delimited string:

### `join_to_string`

Joins the elements of a list into one string, with an optional separator. Omitting the separator concatenates the elements directly.

```wel
join_to_string(list, separator)
```

| Parameter | Description |
| --- | --- |
| list | The list to join. A `List`, `Map`, or `Binary` element raises `E100`. |
| separator | Optional string placed between elements. |

Join list elements with a separator

The following example joins list elements with a comma separator:

**Formula**

```wel
join_to_string(['a', 'b', 'c'], ', ')
```

**Output**

```text
a, b, c
```

Join list elements with no separator

The following example joins list elements directly, with no separator:

**Formula**

```wel
join_to_string(['a', 'b'])
```

**Output**

```text
ab
```

### `join_to_local_string`

Joins the elements using the list separator from the **data-plane** locale, rather than one you supply.

```wel
join_to_local_string(list, separator)
```

| Parameter | Description |
| --- | --- |
| list | The list to join. A `List`, `Map`, or `Binary` element raises `E100`. |
| separator | Optional override for the locale's separator. |

Join list elements using the locale separator

The following example joins list elements using the data-plane locale's separator:

**Formula**

```wel
join_to_local_string(['a', 'b', 'c'])
```

**Output**

```text
a, b, c
```

## Serialize to WEL

The following function serializes a value to WEL's own literal syntax, for logging and debugging:

### `to_wel`

Serializes a value to a WEL literal that parses back to the same value.

`to_wel` is useful for logging and for debugging a transformation, because it shows exactly what a value is rather than an approximation of it. Use [to\_json](/en/wel/stdlib/json) for data leaving the recipe.

`to_wel` renders a constructed type as its constructor call, a `Binary` as a `0x"..."` literal, quotes a `Map` key only when it isn't a plain name, and serializes `Skip` as the literal `Skip`.

```wel
to_wel(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to serialize. Raises `E107` for a lambda. |

Serialize a map to a WEL literal

The following example serializes a map to a WEL literal:

**Formula**

```wel
to_wel({sku: 'WID-1', qty: 3})
```

**Output**

```wel
{sku: 'WID-1', qty: 3}
```

### Use case: Build an order confirmation line

An order confirmation line needs several values combined into one finished sentence. Format the values once, at the end, in an f-string:

**Input**

```json
{
  "id": "SO-1001",
  "ship_date": "2026-03-15",
  "total": 149.5
}
```

**Formula**

```wel
f"Order {_.id} ships {format_date(PlainDate(_.ship_date), '%d %b %Y')} for {to_local_currency(_.total)}"
```

**Output**

```json
"Order SO-1001 ships 15 Mar 2026 for $149.50"
```

The date is converted to a `PlainDate` before being formatted, so the day can't shift. The currency is left to the locale rather than hard-coded, so the same expression is correct for a recipe configured for another region.

## Related

- [Temporal functions](/en/wel/stdlib/temporal): Handle arithmetic and time zones before you format a value.
- [Conversion functions](/en/wel/stdlib/conversion): How to construct each data type.
- [Strings and formatting](/en/wel/language/strings): F-strings and format specifications.
- [Transform data](/en/wel/workato-expression-language-connector): Set the data-plane locale these functions use.

---
