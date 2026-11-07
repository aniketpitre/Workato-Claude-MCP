---
url: 'https://docs.workato.com/en/wel/stdlib.md'
description: >-
  The 245 built-in functions in WEL, spanning 16 categories - strings, lists,
  maps, temporal, numeric, crypto, encoding, escaping, and conversion.
---

# WEL standard library

The standard library is the set of functions built into WEL (Workato Expression Language). It ships with the language, so there is nothing to install, import, or connect. Every function is available in every expression.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Quick reference

WEL organizes functions into the following categories:

| Category | Description |
| --- | --- |
| [String](/en/wel/stdlib/string) | Check, clean, extract, and replace text. |
| [List](/en/wel/stdlib/list) | Map, filter, sort, group, join, and aggregate. |
| [Map](/en/wel/stdlib/map) | Read, merge, and reshape key-value data. |
| [Deep map](/en/wel/stdlib/deep-map) | Collect or transform values at any depth in a nested structure. |
| [Temporal](/en/wel/stdlib/temporal) | Read, calculate with, and move between dates, times, and durations. |
| [Numeric](/en/wel/stdlib/numeric) | Round numbers and test numeric types. |
| [Formatting](/en/wel/stdlib/formatting) | Render values as display strings. |
| [Conversion](/en/wel/stdlib/conversion) | Construct a value of a given type. |
| [Common](/en/wel/stdlib/common) | Measure length, test presence, and inspect type. |
| [JSON](/en/wel/stdlib/json) | Parse, serialize, and query JSON. |
| [Encoding](/en/wel/stdlib/encoding) | Convert between text and bytes in a named encoding. |
| [Escape](/en/wel/stdlib/escape) | Escape a value for CSV, HTML, SOQL, and other formats. |
| [Unicode](/en/wel/stdlib/unicode) | Handle grapheme clusters, normalization, and Japanese text. |
| [Binary](/en/wel/stdlib/binary) | Work with raw byte data. |
| [Crypto](/en/wel/stdlib/crypto) | Hash, sign, and encrypt using HMAC, JWT, PBKDF2, and AES. |
| [Random](/en/wel/stdlib/random) | Generate UUIDs and random values. |

## Call a function

Call a function directly, or pipe a value into it with `>>`:

```text
upper(_.status)
_.status >> upper
```

`_` is the **input variable** that contains the data your expression receives. `_.status` reads the `status` field of the input. Refer to [Input variables](/en/wel/language/expressions#input-variable) for details.

The piped value fills the function's first argument. Write any other arguments normally:

```text
_.order_id >> starts_with?('SO-')
```

The pipe form reads left to right, which makes it the better choice when you chain several steps:

```text
_.email >> trim >> lower
```

Refer to [Operators](/en/wel/language/operators) for the full pipeline family.

## Types are strict

WEL doesn't coerce arguments to make a call succeed. Passing a number where a function expects a `String` raises `E100` rather than silently converting it. Use a [conversion function](/en/wel/stdlib/conversion) to make the intended type explicit.

This is deliberate. Silent coercion is the most common cause of a transformation running without an error but producing the wrong result.

The exceptions are string interpolation, which converts automatically, and two [Transform data action](/en/wel/workato-expression-language-connector) flags that configure specific coercions.

## Related

- [Data types](/en/wel/language/data-types): The 16 WEL data types and how each represents a value.
- [Operators](/en/wel/language/operators): More information about the pipeline family of operators.
- [Cookbook](/en/wel/cookbook): Examples of common integration problems.
- [Error codes](/en/wel/errors): Troubleshoot job failures.

---
