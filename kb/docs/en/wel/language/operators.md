---
url: 'https://docs.workato.com/en/wel/language/operators.md'
description: >-
  WEL operators for arithmetic, comparison, logic, concatenation, the pipeline
  operator, and the two fallback operators, with their precedence.
---

# Operators

Operators combine values into new values. Most, like arithmetic and comparison operators, work the same way they do in other languages. Two operators are specific to WEL:

- [The pipeline](#pipeline): `>>` turns a multi-step transformation into a single line that reads top to bottom.
- [The fallbacks](#fallbacks): `|` and `|?` supply a default value instead of a nested conditional.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

## Precedence

The following table lists operators by precedence. Operators higher in the table run before ones lower in it, regardless of where each appears in the expression. Parentheses (`()`) override precedence order. Wrap part of an expression in parentheses to evaluate it first.

| Precedence | Operators | Meaning |
| --- | --- | --- |
| 1 | `.` `()` | Field access, function call |
| 2 | `!` `not` `-` | Unary prefix |
| 3 | `^` | Power |
| 4 | `*` `/` `%` | Multiply, divide, modulo |
| 5 | `+` `-` | Add, subtract |
| 6 | `++` `>>` `|` `|?` | Concatenate, pipe, fallback, try-fallback |
| 7 | `==` `!=` `<` `>` `<=` `>=` `in` | Comparison and containment |
| 8 | `and` | Logical and |
| 9 | `or` | Logical or |

## Arithmetic

`+` `-` `*` `/` `%` `^` work on `Integer`, `Float`, and `Decimal`.

| Operation | Formula | Result |
| --- | --- | --- |
| `+`: Add | `1 + 2.5` | `3.5` |
| `-`: Subtract | `5 - 2` | `3` |
| `*`: Multiply | `4 * 3` | `12` |
| `/`: Divide | `10 / 3` | `3` |
| `%`: Modulo (remainder) | `10 % 3` | `1` |
| `^`: Power (exponent) | `2 ^ 10` | `1024` |

A negative exponent raises an `E211` error when the base is `Integer` or `Decimal`, since the exact result isn't representable in either type. Use `Float` as the base to resolve the error.

> **INTEGER DIVISION TRUNCATES**
> 
> Dividing two `Integer` values truncates the result. Make one side a `Float` or a `Decimal` for a fractional result, and use a `Decimal` for money. For example:
> 
> | Formula | Result |
> | --- | --- |
> | `10 / 3` | `3` |
> | `10.0 / 3` | `3.3333333333333335` |

Dividing by zero raises `E200` rather than producing infinity.

`Decimal` and `Float` can't mix. Refer to [Data types](/en/wel/language/data-types) for which types support arithmetic.

### Dates and durations

Operators also work on temporal data types. Add an `Integer` to a `PlainDate` to add days, subtract two dates to return the number of days between them, and subtract two instants to return a `Duration`. Use [advance\_date](/en/wel/stdlib/temporal) or [add\_months](/en/wel/stdlib/temporal) instead for calendar arithmetic where the answer depends on month lengths.

| Operation | Formula | Result |
| --- | --- | --- |
| `+`: Add days to a date | `PlainDate('2026-03-15') + 10` | `2026-03-25` |
| `-`: Subtract two dates (day count) | `PlainDate('2026-03-15') - PlainDate('2026-01-01')` | `73` |
| `+`: Add a duration to an instant | `DateTime('2026-01-01T10:00:00Z') + Duration('PT2H')` | `2026-01-01T12:00:00Z` |
| `-`: Subtract two instants (duration) | `DateTime('2026-03-01T00:00:00Z') - DateTime('2026-01-01T00:00:00Z')` | `PT1416H` |

## Concatenation

`++` joins two values of the same type.

| Operation | Formula | Result |
| --- | --- | --- |
| `++`: Join two strings | `'SO-' ++ '1001'` | `SO-1001` |
| `++`: Join two lists | `[1, 2] ++ [3]` | `[1, 2, 3]` |

Mixing types raises `E101`. `'x' ++ 1` is an error, not `x1`. Convert with `String(...)`, or use an [f-string](/en/wel/language/strings), which converts as it interpolates.

## Pipeline operator

`>>` passes the value on its left as the first argument to the function on its right.

| Operation | Formula | Result |
| --- | --- | --- |
| `>>`: Pipe a value into a function | `'acme' >> upper` | `ACME` |

Pipelines read left to right, in the order the steps run. In the following examples `lower` runs first, then `trim`, then `upper`:

```wel
_.email >> lower >> trim >> upper
```

Nested calls can achieve the same result as pipelines, but they force you to read the transformation inside-out:

```wel
upper(trim(lower(_.email)))
```

This is especially important with lambdas, where nesting quickly becomes unreadable:

**Nested call**

```wel
take(reverse(sort_by(filter_by(_.orders, o ~> o.status == 'open'), o ~> o.total)), 3)
```

**Pipeline call**

```wel
_.orders
  >> filter_by(o ~> o.status == 'open')
  >> sort_by(o ~> o.total)
  >> reverse
  >> take(3)
```

## Fallbacks

The fallback operators solve different problems:

### Null value fallback

`|` handles null values.

| Operation | Formula | Result |
| --- | --- | --- |
| `|`: Use a default value when null | `null | 'default'` | `default` |

[presence](/en/wel/stdlib/common#presence-function) reports every kind of absence as `null` so one fallback operator (`|` ) catches them all, including empty strings, whitespace-only strings, empty lists, and empty maps.

```wel
presence(_.display_name) | 'Unknown'
```

### Error fallback

`|?` catches errors.

| Operation | Formula | Result |
| --- | --- | --- |
| `|?`: Use a default value when the expression raises a catchable error | `1 / 0 |? 'error'` | `error` |

Reading a field that doesn't exist raises `E104` rather than producing `null`, so `|` _doesn't_ catch it, but `|?` does:

```wel
_.customer.nickname |? 'none'
```

Refer to [Error codes](/en/wel/errors) for which errors are catchable.

> **A FALLBACK IS A DECISION, NOT A FIX**
> 
> `|? 0` on a currency field means a malformed amount silently becomes zero, and the job reports success. That is sometimes right and sometimes an invoice that quietly goes out wrong.
> 
> Use a fallback when the absence is expected and the default is genuinely correct. Let the error propagate when it isn't. A failed job is visible, and a wrong number isn't.

## Comparison

`==` `!=` `<` `>` `<=` `>=` compare two values.

| Operation | Formula | Result |
| --- | --- | --- |
| `==`: Equal | `1 == 1.0` | `true` |
| `!=`: Not equal | `1 != 2` | `true` |
| `<`: Less than | `1 < 2` | `true` |
| `>`: Greater than | `2 > 1` | `true` |
| `<=`: Less than or equal | `2 <= 2` | `true` |
| `>=`: Greater than or equal | `2 >= 3` | `false` |

`==` and `!=` use the following rules to compare values:

| Behavior | Example |
| --- | --- |
| Numbers and strings don't equate. | `1 == '1'` returns `false`. |
| `Integer` compares across type with `Float` and `Decimal`. `Float` and `Decimal` don't mix. | `1 == 1.0` and `1 == Decimal('1')` return `true`. `1.5 == Decimal('1.5')` raises `E103`. |
| Comparison examines value, not construction. | `[1, 2] == range(1, 2)` returns `true`. `{a: 1} == from_entries([{key: 'a', value: 1}])` returns `true`. |
| Strings that [normalize](/en/wel/stdlib/unicode#unicode-normalize) differently aren't equal. | `é` stored as one character and `e` followed by a combining accent render identically but aren't equal. Use [unicode\_compare](/en/wel/stdlib/unicode) to compare text from different systems. |
| String comparison is case-sensitive. | `'A' == 'a'` returns `false`. |

Ordering a number against a string with `<`, `>`, `<=`, or `>=` raises `E101`. `==` and `!=` find numbers and strings unequal without raising an error.

## Containment

`in` tests whether a value is an element of a list.

| Operation | Formula | Result |
| --- | --- | --- |
| `in`: Test list membership | `2 in [1, 2, 3]` | `true` |

`in` is list-only. Use one of the following alternatives for other types:

- **Substring**: Use [contains?](/en/wel/stdlib/string). `'WID' in 'WID-1'` raises `E101`.
- **Map key**: Use [has\_key?](/en/wel/stdlib/map). `'a' in {a: 1}` raises `E101`.

## Logic

`and`, `or`, and `not` are spelled as words.

| Operation | Formula | Result |
| --- | --- | --- |
| `and`: Logical and | `5 > 3 and 2 < 1` | `false` |
| `or`: Logical or | `5 > 3 or 2 < 1` | `true` |
| `not`: Logical negation | `not true` | `false` |

`and`, `or`, and `not` require `Bool` (or `Null` or `Skip`) operands. A non-`Bool` operand, such as `1 and 2`, raises a type mismatch rather than coercing the value to a truth value.

## Conditionals

`if ... then ... else ...` is an expression. It produces a value, so it can go anywhere a value can.

| Operation | Formula | Result |
| --- | --- | --- |
| `if...then...else`: Conditional expression | `if 5 > 3 then 'yes' else 'no'` | `yes` |

The following example shows a conditional inside a map:

```wel
{
  tier: if _.total > 1000 then 'gold' else 'standard'
}
```

## Related

- [Data types](/en/wel/language/data-types): Which operators apply to which types.
- [Strings and formatting](/en/wel/language/strings): More information about f-strings and interpolation.
- [Standard library](/en/wel/stdlib): The functions you pipe into.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E101`, `E103`, `E104`, and `E200`.

---
