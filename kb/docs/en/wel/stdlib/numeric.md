---
url: 'https://docs.workato.com/en/wel/stdlib/numeric.md'
description: >-
  Use WEL numeric functions to round to integers and decimal places, take
  absolute values, and test for finite, infinite, or NaN numbers.
---

# Numeric functions

Numeric functions round numbers and test numeric values. Rounding functions help prevent precision mismatches between systems, such as accounting totals that differ by fractions of a cent.

> **ROUND MONEY AS DECIMAL, NOT AS FLOAT**
> 
> `round_places` and `round_significant` take a `Decimal` rather than a `Float`. This is because a `Float` can't represent `0.1` exactly, so precision is already lost before rounding even begins.
> 
> Convert currency amounts to `Decimal` at the boundary, such as with `Decimal('12.50')`, and keep them as `Decimal` values throughout the transformation. Schema inference in the Transform Data action doesn't perform this conversion.

## Round to a whole number

The following functions round a number to the nearest, next, or previous integer.

### `round`

Rounds to the nearest integer.

```text
round(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to round. A non-number argument raises `E100`. An infinite float or a `Decimal` beyond the numeric size limit raises `E211`. |

Round up at the midpoint

The following example rounds a number up at the midpoint:

**Formula**

```text
round(3.5)
```

**Output**

```text
4
```

Round down below the midpoint

The following example rounds a number down when it's below the midpoint:

**Formula**

```text
round(2.4)
```

**Output**

```text
2
```

### `ceil`

Rounds up to the next integer.

```text
ceil(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to round up. |

Round up regardless of the decimal

The following example rounds the number up regardless of its decimal:

**Formula**

```text
ceil(3.2)
```

**Output**

```text
4
```

### `floor`

Rounds down to the previous integer.

```text
floor(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to round down. |

Round down regardless of the decimal

The following example rounds the number down regardless of its decimal:

**Formula**

```text
floor(3.9)
```

**Output**

```text
3
```

## Round to a precision

The following functions round a `Decimal` to a fixed number of decimal places or significant digits:

### `round_places`

Rounds and zero-pads a `Decimal` to a given number of decimal places.

```text
round_places(decimal, places, options)
```

| Parameter | Description |
| --- | --- |
| decimal | The `Decimal` to round. Non-decimal data types raise `E100`. |
| places | How many decimal places to keep. Negative values round to the left of the decimal point. A magnitude beyond 2,147,483,647 raises `E211`. Non-integer data types raise `E100`. |
| options | Optional map to control the rounding mode. `mode`: How to round when a value falls exactly between two results. `half_up` (the default): Rounds away from zero.; `half_even`: Rounds to the nearest even digit rather than rounding up, so totals don't drift upward over many rows. Use it when reconciling against a system that requires it, or when totals differ by cents.; `half_down`, `up`, `down`, `ceiling`, `floor`: Standard rounding directions.; `exact`: Raises catchable `E228` rather than rounding when the value doesn't fit in the requested places. Use `exact` when silently losing precision would be a bug. An unrecognized option key raises `E225` rather than being ignored. |

Default rounding (half up)

The following example rounds using the default half-up mode:

**Formula**

```text
round_places(Decimal('11.545'), 2)
```

**Output**

```text
11.55
```

Banker's rounding (half to even)

The following example rounds using banker's rounding, half to even:

**Formula**

```text
round_places(Decimal('11.545'), 2, {mode: 'half_even'})
```

**Output**

```text
11.54
```

Round using floor mode

The following example rounds using floor mode:

**Formula**

```text
round_places(Decimal('11.545'), 2, {mode: 'floor'})
```

**Output**

```text
11.54
```

### `round_significant`

Rounds a `Decimal` to a number of significant digits rather than decimal places, without padding.

```text
round_significant(decimal, digits, options)
```

| Parameter | Description |
| --- | --- |
| decimal | The `Decimal` to round. Non-decimal data types raise `E100`. |
| digits | How many significant digits to keep. Raises `E211` for values less than `1`. Non-integer data types raise `E100`. Zero stays zero regardless of `digits`. |
| options | Optional map with the same `mode` values as `round_places`. An unrecognized option key raises `E225`. |

Round to 3 significant digits

The following example rounds a number to 3 significant digits:

**Formula**

```text
round_significant(Decimal('1234.5'), 3)
```

**Output**

```text
1230
```

### Use case: Round each invoice line to cents

Unit prices arrive with three decimal places, but the destination accounting system accepts only two. Use `round_places` to round each invoice line to two decimal places:

**Input**

```json
{
  "lines": [
    {"sku": "WID-1", "unit_price": "12.335", "qty": 3},
    {"sku": "GAD-7", "unit_price": "99.005", "qty": 1}
  ]
}
```

**Formula**

```text
_.lines >> map_by(l ~> {
  sku: l.sku,
  total: round_places(Decimal(l.unit_price) * l.qty, 2)
})
```

**Output**

```json
[
  {"sku": "WID-1", "total": 37.01},
  {"sku": "GAD-7", "total": 99.01}
]
```

The prices stay `Decimal` from the start, so the multiplication is exact and only the final rounding loses anything. A `Float` reading first would round twice instead, applying the second rounding to an already-approximate number.

## Absolute value

The following function returns a number's magnitude, discarding its sign:

### `abs`

Returns the magnitude of a number, discarding its sign. Also accepts a `Duration`.

```text
abs(value)
```

| Parameter | Description |
| --- | --- |
| value | A `Number` or a `Duration`. Non-number, non-duration data types raise `E100`. Negating the most negative representable `Duration` overflows and raises `E211`. |

Absolute value of a negative number

The following example returns the absolute value of a negative number:

**Formula**

```text
abs(-42)
```

**Output**

```text
42
```

## Test a number

The following functions distinguish an ordinary number from the special `Float` values. A non-numeric argument raises `E100` rather than returning `false`.

### `finite?`

Returns `true` for an `Integer`, a `Decimal`, or a `Float` that is an ordinary number.

```text
finite?(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to test. |

An ordinary float is finite

The following example tests an ordinary float:

**Formula**

```text
finite?(1.0)
```

**Output**

```text
true
```

Infinity isn't finite

The following example tests positive infinity:

**Formula**

```text
finite?(Float('Infinity'))
```

**Output**

```text
false
```

### `infinite?`

Returns `true` if the value is positive or negative infinity.

```text
infinite?(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to test. |

Detect positive infinity

The following example tests positive infinity:

**Formula**

```text
infinite?(Float('Infinity'))
```

**Output**

```text
true
```

### `nan?`

Returns `true` if the value is the `Float` "not a number". `NaN` is outside WEL's value domain. Arithmetic raises `E200` instead of producing `NaN`. `Float('NaN')` raises `E102`.

```text
nan?(number)
```

| Parameter | Description |
| --- | --- |
| number | The number to test. |

An ordinary number isn't NaN

The following example tests an ordinary number:

**Formula**

```text
nan?(1.0)
```

**Output**

```text
false
```

> **THESE VALUES DON'T ARISE FROM DIVISION BY ZERO**
> 
> Dividing by zero raises `E200` rather than producing infinity, so a WEL expression doesn't silently generate one. `Infinity` can still arise from overflow, such as `1.0e308 * 10.0`. [present?](/en/wel/stdlib/common) treats `Infinity` as absent, so a [presence](/en/wel/stdlib/common) fallback catches it without an explicit check.

## Bit width

The following function measures how many bits an integer needs to represent:

### `int_bit_size`

Returns the number of bits needed to represent an integer in bit-complementary encoding.

```text
int_bit_size(integer)
```

| Parameter | Description |
| --- | --- |
| integer | The integer to measure. Non-integer data types raise `E100`. Both `0` and `-1` require 1 bit. |

Bits needed for 255

The following example measures the bits needed for 255:

**Formula**

```text
int_bit_size(255)
```

**Output**

```text
9
```

## Related

- [Conversion functions](/en/wel/stdlib/conversion): How to construct each data type.
- [Formatting functions](/en/wel/stdlib/formatting): Render a number for display.
- [Data types](/en/wel/language/data-types): Why `Decimal` and `Float` behave differently.
- [Common functions](/en/wel/stdlib/common): Information about `present?` and `presence`.
- [Temporal functions](/en/wel/stdlib/temporal): Information about `Duration`, which `abs` also accepts.

---
