---
url: 'https://docs.workato.com/en/wel/language/strings.md'
description: >-
  WEL string literals, f-string interpolation, and format specifications for
  controlling padding, alignment, and decimal places in output text.
---

# Strings and formatting

A transformation often needs to build a string out of data, such as a display name, a reference number, a message body, or a line for a report. WEL has f-strings for that, and they are usually a better choice than concatenation.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## String literals

Single and double quotes are equivalent.

| Formula | Result |
| --- | --- |
| `'single quotes'` | `single quotes` |
| `"double quotes"` | `double quotes` |

Pick whichever avoids escaping. A string containing an apostrophe is easiest in double quotes:

```text
"O'Brien"
```

Strings are UTF-8, and `length` counts code points rather than bytes. Refer to [Data types](/en/wel/language/data-types) for how WEL counts and stores text.

## Interpolation with f-strings

Prefixing a string with `f` evaluates and inserts any `{...}` inside it.

| Formula | Result |
| --- | --- |
| `f"Order {upper('so-1')} total {1 + 2}"` | `Order SO-1 total 3` |

Anything that produces a value can go inside the braces, including a field, a function call, arithmetic, or a whole pipeline:

```text
f"{capitalize(_.first_name)} {capitalize(_.last_name)} <{lower(trim(_.email))}>"
```

### Prefer f-strings over `++`

`++` requires matching types on both sides, so a message built from mixed data needs every piece converted first:

```text
'Order ' ++ String(_.id) ++ ' has ' ++ String(_.count) ++ ' items'
```

An f-string converts as it interpolates, and the result reads like the sentence it produces:

```text
f"Order {_.id} has {_.count} items"
```

Use `++` when you are deliberately joining two strings, or two lists.

## Format specifications

A colon (`:`) inside the braces adds a format specification, which controls width, alignment, and precision.

| Formula | Result |
| --- | --- |
| `f"{3.14159:.2f}"` | `3.14` |
| `f"{42:05d}"` | `00042` |
| `f"{'nur':>10}"` | `nur` |

The following table lists the common forms:

| Spec | Effect |
| --- | --- |
| `.Nf` | Fixed-point with N decimal places |
| `0Nd` | Integer padded to N digits with leading zeros |
| `>N` | Right-align in a field N wide |
| `<N` | Left-align in a field N wide |
| `^N` | Center in a field N wide |

An invalid specification raises `E016` at parse time, so a malformed format is caught before the expression ever runs.

> **FORMATTING ISN'T ROUNDING**
> 
> `f"{_.total:.2f}"` produces text with two decimal places. It doesn't round the underlying value, and the result is a `String`, which doesn't support arithmetic afterwards.
> 
> Round it first with [round\_places](/en/wel/stdlib/numeric), then format the result, to keep the rounded value available for later arithmetic.

## Padding and alignment

Format specifications cover most cases. For padding applied to a value rather than inside a template, use [`lpad` and `rpad`](/en/wel/stdlib/string):

```text
lpad(String(_.line_no), 5, '0')
```

Use [`grapheme_lpad` and `grapheme_rpad`](/en/wel/stdlib/unicode) instead for fixed-width output containing text outside ASCII. This ensures the columns line up for a reader rather than for a byte counter.

## Locale-aware formatting

Numbers, currency, and dates that a person reads should go through the locale rather than a hand-written pattern:

```text
f"{_.customer_name}: {to_local_currency(_.total)}"
```

`to_local_currency` and `to_local_string` use the **data-plane** locale configured on the Transform Data action, so the same expression is correct for a recipe set up for another region. Refer to [Formatting functions](/en/wel/stdlib/formatting) and the [Transform data](/en/wel/workato-expression-language-connector) action.

## Escaping

Escape a value as you insert it when the string is going into another format, such as a URL, a CSV field, a query, or HTML:

```text
f"SELECT Id FROM Account WHERE Name = '{escape_for_soql(_.name)}'"
```

The quotes form part of the query syntax. Escape only the value between them. Refer to [Escape functions](/en/wel/stdlib/escape) for escaping values safely into other formats.

## Related

- [String functions](/en/wel/stdlib/string): Check, clean, extract, and replace text.
- [Formatting functions](/en/wel/stdlib/formatting): Format dates, numbers, currency, and joined lists.
- [Escape functions](/en/wel/stdlib/escape): Embed a value safely inside another format.
- [Unicode functions](/en/wel/stdlib/unicode): Measure text the way a reader sees it.

---
