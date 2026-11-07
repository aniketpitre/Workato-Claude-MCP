---
url: 'https://docs.workato.com/en/insights/operators.md'
description: >-
  An operator is a symbol that specifies the action performed on one or more
  operands. Insights supports numerous operators in calculated columns.
---

# Operators

An operator is a symbol that specifies the action performed on one or more operands. Insights dashboard support the following types of operators in [calculated columns](/en/insights/custom-columns):

- [Arithmetic operators](#arithmetic-operators)
- [Comparison operators](#comparison-operators)
- [Logical operators](#logical-operators)

> **NULL OPERANDS**
> 
> Insights uses the following logic for operations that include `NULL` values:
> 
> - If the formula contains a `NULL` value, the result returned in the calculated column is also a `NULL` value.
> 
> For example, if one of the rows in the Quantity column is `NULL`, then the result in the calculated column for that row is also `NULL`:
> 
> **Column expression** (required):
> 
> \= {{Unit price}}`*`{{Quantity}}

## Arithmetic operators

Arithmetic operators are used to perform mathematical operations on number data types in queries. Insights supports the following arithmetic operators in calculated columns:

| Operator | Description |
| --- | --- |
| [\+ (add)](#add) | Addition |
| [\- (subtract)](#subtract) | Subtraction |
| [\* (multiply)](#multiply) | Multiplication |
| [/ (divide)](#divide) | Division |
| [% (modulus)](#modulus) | Returns the integer remainder of a division |

### \+ (add)

Adds one number to another.

- **Applicable data types**: `BIGINT`, `DOUBLE`

#### Example

This example adds an item's tax to an item's price:

**Column expression** (required):

\= {{Item price}}`+`{{Tax amount}}

### \- (subtract)

Subtracts one number from another.

- **Applicable data types**: `BIGINT`, `DOUBLE`

#### Example

This example subtracts the claim amount from the amount in a wallet:

**Column expression** (required):

\= {{Wallet amount}}`-`{{Claim amount}}

### \* (multiply)

Multiplies one operand by another.

- **Applicable data types**: `BIGINT`, `DOUBLE`

#### Example

This example multiplies the price of an item by the item quantity:

**Column expression** (required):

\= {{Item price}}`*`{{Quantity}}

### / (divide)

Divides one number (the numerator) by another (the denominator):

- **Applicable data types**: `BIGINT`, `DOUBLE`

> **DIVISION WITH 0 (ZERO)**
> 
> Insights uses the following logic for division operations that include 0:
> 
> - If the numerator is `0`, `0` is returned. For example, `0/row_count = 0`.
> - If the denominator is `0`, `0` is returned. For example, `time_taken/0 = 0`.
> - If the denominator is `null`, `null` is returned. For example, `time_taken/null = null`.

#### Example

This example divides the task count by the job count:

**Column expression** (required):

\= {{Task count}}`/`{{Job count}}

### % (modulus)

Returns the integer remainder of a division. For example, `23 % 7 = 2`, because the remainder of `23` divided by `7` is `2`.

- **Applicable data types**: `BIGINT`, `DOUBLE`

#### Example

This example returns the remainder from a division:

**Column expression** (required):

\= `(`{{Order month}}`-1) % 4 + 1`

## Comparison operators

Comparison operators are used to compare the value of one operand to another operand in queries. Insights supports the following types of comparison operators in calculated columns:

| Operator | Description |
| --- | --- |
| [\= (equal)](#equal) | Equal to |
| [!= (not equal to)](#not-equal-to) | Not equal to |
| [\> (greater than)](#greater-than) | Greater than |
| [\>= (greater than or equal to)](#greater-than-equal-to) | Greater than or equal to |
| [< (less than)](#less-than) | Less than |
| [<= (less than or equal to)](#less-than-equal-to) | Less than or equal to |

### \= (equal)

Returns `TRUE` if the two operands are equal, and `FALSE` otherwise.

- **Applicable data types**: `DATE`, `TIMESTAMP`, `BIGINT`, `DOUBLE`, `BOOLEAN`, `VARCHAR`

#### Example

This example evaluates whether the ID equals the recipe ID:

**Column expression** (required):

\= {{ID}}`=`{{Recipe ID}}

### != (not equal to)

Returns `TRUE` if the two operands are not equal, and `FALSE` otherwise.

- **Applicable data types**: `DATE`, `TIMESTAMP`, `BIGINT`, `DOUBLE`, `BOOLEAN`, `VARCHAR`

#### Example

This example evaluates whether the start date doesn't equal the end date.

**Column expression** (required):

\= {{Start date}}`!=`{{End date}}

### \> (greater than)

Returns `TRUE` if the left operand is greater (or later, for datetime values) than the right operand, and `FALSE` otherwise.

- **Applicable data types**: `DATE`, `TIMESTAMP`, `BIGINT`, `DOUBLE`

#### Example

This example evaluates whether the job count is greater than 1000:

**Column expression** (required):

\= {{job\_count}}`> 1000`

### \>= (greater than or equal to)

Returns `TRUE` if the left operand is greater (or later for datetime values) than or equal to the right operand, and `FALSE` otherwise.

- **Applicable data types**: `DATE`, `TIMESTAMP`, `BIGINT`, `DOUBLE`

#### Example

This example evaluates whether the job count is greater than or equal to 1000:

**Column expression** (required):

\= {{job\_count}}`>= 1000`

### < (less than)

Returns `TRUE` if the left operand is less (or earlier for datetime values) than the right operand, and `FALSE` otherwise.

- **Applicable data types**: `DATE`, `TIMESTAMP`, `BIGINT`, `DOUBLE`

#### Example

This example evaluates whether the submission date was before the deadline date:

**Column expression** (required):

\= {{submission\_date}}`<` {{deadline}}

### <= (less than or equal to)

Returns `TRUE` if the left operand is less (or earlier for datetime values) than or equal to the right operand, and `FALSE` otherwise.

- **Applicable data types**: `DATE`, `TIMESTAMP`, `BIGINT`, `DOUBLE`

#### Example

This example evaluates whether the submission date was on or before the deadline date:

**Column expression** (required):

\= {{submission\_date}}`<=` {{deadline}}

## Logical operators

Logical operators are used to combine or manipulate conditions in queries. Insights supports the following logical operators in calculated columns:

| Operator | Description |
| --- | --- |
| [AND](#and) | `TRUE` if both boolean operands are `TRUE`. |
| [OR](#or) | `TRUE` if one boolean operand is `TRUE`. |

### AND

Returns `TRUE` if both the left and right operands are `TRUE`, and `FALSE` otherwise.

- **Applicable data types**: `BOOLEAN`

#### Example

This example evaluates whether both `is_completed` and `is_success` are `TRUE`:

**Column expression** (required):

\= {{is\_completed}}`AND` {{is\_success}}

### OR

Returns `TRUE` if the left, right, or both operands are `TRUE`, and `FALSE` otherwise.

- **Applicable data types**: `BOOLEAN`

#### Example

This example evaluates whether `is_in_progress`, `is_complete`, or both are `TRUE`:

**Column expression** (required):

\= {{is\_in\_progress}}`OR`{{is\_complete}}

---
