---
url: 'https://docs.workato.com/en/formulas/number-formulas.md'
description: >-
  Learn how to use Workato number formulas for integers and decimals, including
  arithmetic operations and how result types are returned.
---

# Number formulas

In Ruby, Fixnum refers to integers, such as 9, 10, and 11, while Float refers to decimals, such as 1.75 and 2.5. Workato supports a variety of Fixnum and Float formulas.

Formulas in Workato are allowlisted Ruby methods. Syntax and functionality for these formulas are generally unchanged. Most formulas return an error and stop the job if the formula operates on nulls (expressed as `nil` in Ruby), except for `present?`, `presence`, and `blank?`.

You can refer to the Ruby documentation for [Fixnum (integers)](http://ruby-doc.org/core-2.3.3/Fixnum.html) and [Float (decimals)](http://ruby-doc.org/core-2.3.3/Float.html) for more information. However, only allowlisted Ruby methods are supported. Contact your Customer Success Manager to request new formulas for the allowlist.

## Arithmetic operations

In the cases of arithmetic operations, whether the values are of integer types or decimal (float) types are important. Formulas stick to the types given as input, and the returned result will be of the most precise type.

For example:

- If integer values are provided, an integer value will be returned.
- If float values are provided, a float value will be returned.
- If both float and integer values are provided, a float value will be returned, as that is more precise.

### The add (+) operator

This operator allows the addition of operands on either side. This section talks about number arithmetic. Refer to [Date arithmetic](/en/formulas/date-formulas#date-arithmetic) for more information on date-specific arithmetic.

#### Sample usage

| Formula | Result | Type |
| --- | --- | --- |
| 4 + 7 | 11 | Fixnum |
| 4.0 + 7 | 11.0 | Float |
| 4.0 + 7.0 | 11.0 | Float |

* * *

### The subtract (-) operator

This operator subtracts the right hand operand from the left hand operand. This section talks about number arithmetic. Refer to [Date arithmetic](/en/formulas/date-formulas#date-arithmetic) for more information on date-specific arithmetic.

#### Sample usage

| Formula | Result | Type |
| --- | --- | --- |
| 4 - 7 | \-3 | Fixnum |
| 4.0 - 7 | \-3.0 | Float |
| 4.0 - 7.0 | \-3.0 | Float |

* * *

### The multiply (\*) operator

This operator multiplies the operands on either side.

#### Sample usage

| Formula | Result | Type |
| --- | --- | --- |
| 4 \* 7 | 28 | Fixnum |
| 4.0 \* 7 | 28.0 | Float |
| 4.0 \* 7.0 | 28.0 | Float |

* * *

### The divide (/) operator

Divides left hand operand by right hand operand.

#### Sample usage

| Formula | Result | Type |
| --- | --- | --- |
| 4 / 7 | 0 | Fixnum |
| 4.0 / 7 | 0.571428... | Float |
| 7 / 4 | 1 | Fixnum |
| 7 / 4.0 | 1.75 | Float |
| 7.0 / 4 | 1.75 | Float |
| 7.0 / 4.0 | 1.75 | Float |

* * *

### The exponential (\*\*) operator

Left hand operand to the power of the right hand operand.

#### Sample usage

| Formula | Result | Type |
| --- | --- | --- |
| 5\*\*3 | 125 | Fixnum |
| 4\*\*1.5 | 8.0 | Float |
| 4.0\*\*2 | 16.0 | Float |
| 3\*\*-1 | "1/3" | Rational |
| 8\*\*(3\*\*-1) | 2.0 | Float |
| 7\*\*-1.6 | 0.044447... | Float |

* * *

### The modulo (%) operator

Divides left hand operand by right hand operand and returns the remainder.

#### Sample usage

| Formula | Result | Type |
| --- | --- | --- |
| 4 % 7 | 4 | Fixnum |
| 4.0 % 7 | 4.0 | Float |
| 4 % 7.0 | 4.0 | Float |
| 7 % 4 | 3 | Fixnum |
| 7.0 % 4.0 | 3.0 | Float |

* * *

## Other number formulas

### `abs`

Returns the absolute (positive) value of a number.

#### Syntax

number.abs

- number - An input integer or float.

#### Sample usage

| Formula | Result |
| --- | --- |
| 45.abs | 45 |
| \-45.abs | 45 |
| 45.67.abs | 45.67 |
| \-45.67.abs | 45.67 |

* * *

### `round`

Rounds off a numerical value. This formula returns a value with a specified number of decimal places.

#### Syntax

number.round(offset)

- number - An input integer or float.
- offset - (optional) The number of decimal places to return, you can provide negative values. If not specified, this formula will return the number with no decimal places.

#### Sample usage

| Formula | Result |
| --- | --- |
| 1234.567.round | 1235 |
| 1234.567.round(2) | 1234.57 |
| 1234.567.round(-2) | 1230 |

* * *

## Conditionals

### `blank?`

Checks whether the input is considered blank according to Ruby conventions. This includes:

- Null values
- Empty inputs
- False booleans
- Strings containing only whitespace
- Non-value numbers, sometimes referred to as NaN (not a number). This is an undefined value or value that cannot be represented. For example, the result of division by zero, or a missing value.

#### Syntax

Input.blank?

- Input - An input datapill. It can be a string, number, date, datetime, boolean, array, or object datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Any Value".blank? | false |
| 123.blank? | false |
| 0.blank? | false |
| "".blank? | true |
| ' '.blank? | true |
| nil.blank? | true |
| false.blank? | true |
| true.blank? | false |
| \[\].blank? | true |
| {}.blank? | true |

#### How it works

If the input is considered blank according to Ruby conventions, the formula returns true. For any other data, it returns false.

#### See also

- [presence](/en/formulas/number-formulas#presence): Returns the data if it exists, returns nil if it does not.
- [present?](/en/formulas/number-formulas#present): Returns true if there is a valid input.

* * *

### `even?`

Checks the integer input and returns true if it is an even number.

#### Syntax

integer.even?

- integer - An input integer.

#### Sample usage

| Formula | Result |
| --- | --- |
| 123.even? | false |
| 1234.even? | true |

#### See also

- [odd?](/en/formulas/number-formulas#odd): Checks the integer input and returns true if it is an odd number.

* * *

### `odd?`

Checks the integer input and returns true if it is an odd number.

#### Syntax

integer.odd?

- integer - An input integer.

#### Sample usage

| Formula | Result |
| --- | --- |
| 123.odd? | true |
| 1234.odd? | false |

#### See also

- [even?](/en/formulas/number-formulas#even): Checks the integer input and returns true if it is an even number.

* * *

### `present?`

This formula will check the input and if there is a value present, it will return true. If the input is nil, boolean false, an empty string, or an empty list, the formula will return false.

#### Syntax

Input.present?

- Input - An input datapill. It can be a string, number, date, or list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Any Value".present? | true |
| 123.present? | true |
| 0.present? | true |
| "2017-04-02T12:30:00.000000-07:00".present? | true |
| nil.present? | false |
| "".present? | false |
| \[\].present? | false |

#### How it works

If the input is null, an empty string or an empty list, the formula will return false. For any other data, it returns true.

> **Evaluating a list with nil values**
> 
> - Only an empty list will return false.
> 
> \[\].present? returns false.
> 
> - A list with nil and empty string will return true.
> 
> \[nil,""\].present? returns true.

#### See also

- [presence](/en/formulas/number-formulas#presence): Returns the data if it exists, returns nil if it does not.
- [blank?](/en/formulas/number-formulas#blank): Returns nil if the data does not exist or if the string consist of only white spaces.

* * *

### `presence`

Returns the data if it exists, returns nil if it does not.

#### Syntax

Input.presence

- Input - An input datapill. It can be a string, number, date, or datetime datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| nil.presence | nil |
| "".presence | nil |
| "Any Value".presence | "Any Value" |
| 45.0.presence | 45.0 |
| 0.presence | 0 |

#### How it works

If the input is null or an empty string, the formula will return nil. For any other data, it returns the original input data.

#### See also

- [blank?](/en/formulas/number-formulas#blank): Returns nil if the data does not exist or if the string consist of only white spaces.
- [present?](/en/formulas/number-formulas#present): Returns true if there is a valid input.

* * *

## Conversions

### `ceil`

Rounds the input number to the next greater integer or float. You can specify the precision of the decimal digits.

#### Syntax

number.ceil(precision)

- number - An input integer or float.
- precision - (optional) The number of decimal places to return, you can provide negative values. If not specified, this formula will return the number with no decimal places.

#### Sample usage

| Formula | Result |
| --- | --- |
| 1234.567.ceil | 1235 |
| \-1234.567.ceil | \-1234 |
| 1234.567.ceil(2) | 1234.57 |
| 1234.567.ceil(-2) | 1300 |

* * *

### `floor`

Rounds the input number to the next smaller integer or float. You can specify the precision of the decimal digits.

#### Syntax

number.floor(precision)

- number - An input integer or float.
- precision - (optional) The number of decimal places to return, you can provide negative values. If not specified, this formula will return the number with no decimal places.

#### Sample usage

| Formula | Result |
| --- | --- |
| 1234.567.floor | 1234 |
| \-1234.567.floor | \-1235 |
| 1234.567.floor(2) | 1234.56 |
| 1234.567.floor(-2) | 1200 |

* * *

### `to_f`

Converts data to a float (number) datatype.

#### Syntax

Input.to\_f

- Input - An number input data. You can use a string datatype or a integer datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| 45.to\_f | 45.0 |
| \-45.to\_f | \-45.0 |
| "45.67".to\_f | 45.67 |
| "Workato".to\_f | 0 |

#### How it works

This formula checks whether the input contains any numbers, if no numbers are found, it returns 0. If the number does not have a decimal point, `.0` will be added the number.

#### See also

- [to\_i](/en/formulas/number-formulas#to-i): Convert data to an integer (whole number) datatype.

* * *

### `to_i`

Converts data to an integer (whole number) datatype.

#### Syntax

Input.to\_i

- Input - An number input data. You can use a string datatype or a float datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| 45.43.to\_i | 45 |
| \-45.43.to\_i | \-45 |
| "123".to\_i | 123 |
| "Workato".to\_i | 0 |

#### How it works

This formula checks whether the input contains any numbers, if no numbers are found, it returns 0. If the number has a decimal point, everything after the decimal will be omitted.

> **Check for integers**
> 
> You can use this formula to check if a string contains an integer. If the input does not contain any numbers, the formula will return `0`.

#### See also

- [to\_f](/en/formulas/number-formulas#to-f): Converts data to a float (number) datatype.

* * *

### `to_s`

Converts data to a string (text) datatype.

#### Syntax

Input.to\_s

- Input - Any input data. You can use number, array, object, or datetime datatypes.

#### Sample usage

| Formula | Result |
| --- | --- |
| \-45.67.to\_s | "-45.67" |
| "123".to\_s | "123" |
| \[1,2,3\].to\_s | "\[1,2,3\]" |
| {key: "Workato"}.to\_s | "{:key=>"Workato"}"" |
| "2020-06-05T17:13:27.000000-07:00".to\_s | "2020-06-05T17:13:27.000000-07:00" |
| "2020-06-05T17:13:27.000000-07:00".to\_s(:short) | "05 Jun 17:13" |
| "2020-06-05T17:13:27.000000-07:00".to\_s(:long) | "June 05, 2020 17:13" |

#### How it works

This formula returns a string representation of the input data.

> **Quicktip: Output is a string datatype.**
> 
> A string representation of a list cannot be used in a [**repeat step**](/en/recipes/steps#repeat-step).

#### See also

- [to\_f](/en/formulas/number-formulas#to-f): Converts data to a float (number) datatype.
- [to\_i](/en/formulas/number-formulas#to-i): Converts data to an integer (whole number) datatype.

* * *

### `to_currency`

Formats integers/numbers to a currency-style.

#### Syntax

Input.to\_currency

- Input - Any input string.

#### Sample usage

| Formula | Description | Result |
| --- | --- | --- |
| "345.60".to\_currency | Adds default currency symbol "$" | "$345.60" |

#### Advanced sample usage

Learn more about advance usage for the to\_currency formula. A comma-separated combination of these may be used to achieve the desired currency format. For example:

```ruby
"12345.678".to_currency(delimiter: ".", format: "%n %u", precision: 2, separator: ",", unit: "€")
```

| Formula | Description | Result |
| --- | --- | --- |
| "345.60".to\_currency(unit: "€") | Changes the default currency unit | "€345.60" |
| "345.60".to\_currency(format: "%n %u") | Changes the position of the number relative to the unit (where the number is represented by `%n` and the currency unit is represented by `%u`). Accepts 0 or 1 spaces in between. Defaults to `"%u%n"`. | "345.60 $" |
| "-345.60".to\_currency(negative\_format: "(%u%n)") | Specifies the format when the number is negative (where the number is represented by `%n` and the currency unit is represented by `%u`). | "($345.60)" |
| "345.678".to\_currency | Precision defaults to 2 decimal places | "$345.68" |
| "345.678".to\_currency(precision: 3) | Change the precision by specifying the number of decimal places | "$345.678" |
| "345.678".to\_currency(separator: ",") | Specify the **decimal separator** as ".", "," or " ". Defaults to ".". | "$345,68" |
| "12345.678".to\_currency(delimiter: ".") | Specify the **thousands separator** as ",", "." or " ". Defaults to ",". | ""$12.345.68" |

* * *

### `to_phone`

Converts string or number to a formatted phone number (user-defined).

#### Syntax

Input.to\_phone

- Input - Any input string or number.

#### Sample usage

| Formula | Result |
| --- | --- |
| "5551234".to\_phone | 555-1234 |
| 1235551234.to\_phone | 123-555-1234 |
| 1235551234.to\_phone(area\_code: true) | (123) 555-1234 |
| 1235551234.to\_phone(delimiter: " ") | 123 555 1234 |
| 1235551234.to\_phone(area\_code: true, extension: 555) | (123) 555-1234 x 555 |
| 1235551234.to\_phone(country\_code: 1) | +1-123-555-1234 |
| "123a456".to\_phone | 123a456 |

---
