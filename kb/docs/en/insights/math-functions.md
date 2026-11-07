---
url: 'https://docs.workato.com/en/insights/math-functions.md'
description: >-
  Use math functions in calculated columns to round and manipulate numerical
  values within Insights dashboards.
---

# Math functions

You can use the following math functions in [calculated columns](/en/insights/custom-columns) to round and manipulate numerical values within Insights dashboards.

> **ALIASES**
> 
> You can search for a function using its alias.
> 
> For example, if the function `floor` has the alias `round_down`:
> 
> - When you type `round_do`, Insights suggests the `floor` function.
> - When you type `round_down`, Insights rewrites it as `floor`.

> **NULL OPERANDS**
> 
> Insights uses the following logic for expressions that include `NULL` values:
> 
> - If the expression contains a `NULL` value, the result returned in the calculated column is also a `NULL` value.
> 
> For example, if one of the rows in the Date column is `NULL`, then the result in the calculated column for that row is also `NULL`:
> 
> **Column expression** (required):
> 
> \= `floor((month(`{{Date}}`) - 2 + 12) / 3 % 4) + 1`

## floor

Rounds the input number down to the nearest multiple of the step size. Defaults to integer rounding, where `step_size` = `1`.

The step size must be a non-zero positive number.

- **Return type**: `BIGINT`, `DOUBLE`
- **Alias**: `round_down`

```plaintext
floor(number, step_size)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `number` | `BIGINT`, `DOUBLE` | The input to round down. |
| `step_size` | `BIGINT`, `DOUBLE` | _Optional_. The interval for rounding. The number is rounded down to the nearest multiple of this value. The default is 1. |

### Example

This example calculates the fiscal year (FY) quarter for a month, where the FY starts in February.

**Column expression** (required):

\= `floor((month(`{{Date}}`) - 2 + 12) / 3 % 4) + 1`

If Date is `"04/28/2024"`, this expression returns `1`, indicating that April is in the first FY quarter.

More examples

| Formula | Result |
| --- | --- |
| `floor(3.67)` | `3` |
| `floor(3.32, 2)` | `2` |

## round

Rounds the input number. Defaults to integer rounding, where `decimal_places` = `0`.

The number of decimal places must be an integer. Positive values set decimal places while negatives round to the nearest 10, 100, and so on. For example, `-1` rounds to the nearest 10 and `-2` rounds to the nearest 100.

- **Return type**: `BIGINT`, `DOUBLE`

```plaintext
round(number, decimal_places)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `number` | `BIGINT`, `DOUBLE` | The input to round. |
| `decimal_places` | `BIGINT` | _Optional_. The number of decimal numbers. The default value is 0 decimal places. |

### Example

This example rounds the average cost to cents for financial reporting.

**Column expression** (required):

\= `round(`{{Average cost}}`, 2)`

If Average cost equals `123.5678`, this expression returns `123.57`.

More examples

| Formula | Result |
| --- | --- |
| `round(3.32)` | `3` |
| `round(3.67)` | `4` |
| `round(123.5678, -1)` | `120` |
| `round(167, -2)` | `200` |

## ceiling

Rounds the input number up to the nearest multiple of the step size. Defaults to integer rounding, where `step_size` = `1`.

The step size must be a non-zero positive number.

- **Return type**: `BIGINT`, `DOUBLE`
- **Alias**: `round_down`

```plaintext
ceiling(number, step_size)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `number` | `BIGINT`, `DOUBLE` | The input to round up. |
| `step_size` | `BIGINT`, `DOUBLE` | _Optional_. The interval for rounding. The number is rounded up to the nearest multiple of this value. The default is 1. |

### Example

This example calculates the minimum number of shipping containers required by rounding up the order volume.

**Column expression** (required):

\= `ceiling(`{{Units ordered}}`/100)`

If Units ordered equals `275` and each shipping container can hold `100` units, this expression returns `3`.

More examples

| Formula | Result |
| --- | --- |
| `ceiling(3.32)` | `4` |
| `ceiling(3.67)` | `4` |

---
