---
url: 'https://docs.workato.com/en/formulas/conditions.md'
description: >-
  Learn how to add conditional logic to Workato formulas using Ruby ternary
  syntax to handle missing values and unexpected data.
---

# Add conditions to formulas

It is also important to create recipes that are resilient against unexpected scenarios. For example, your trigger data might contain missing values or contain a data of another datatype.

You can use conditional logic to prepare your recipes for these situations.

## Conditionals

You can conditionally execute formulas using Ruby's ternary syntax (popular shortcut for if-else statements). Ternary syntax are of the form:

```
condition ? expression1 : expression2
```

### Behavior

#### `condition`

A boolean expression that evaluates to `true` or `false`.

#### `expression1`

Returns this expression if `condition` is `true`.

#### `expression2`

Returns this expression if `condition` is `false`.

## Example: Using first name or full name

In the following example, we conditionally pass in either the Full name (Step 1) or First name (Step 1) into the Message input field.

![Ternary syntax](data:image/png;base64,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)_Checks if Full name (Step 1) is present. Outputs Full name (Step 1) if present, or First name (Step 1) if not present._

Here is a detailed explanation of what the ternary formula does:

1. Full name (Step 1)`.present?` will check if the Full name (Step 1) pill has a value . If it has a value, it evaluates to `true`. If it has no value, it evaluates to `false`.
2. The second `?` in the formula separates the condition to evaluate from the expressions to return. Note, the first `?` is part of the [`.present?` formula](/en/formulas/string-formulas#present) whilst the second `?` is separated with a space character and is part of the ternary syntax.
3. If there is a value in the Full name (Step 1) pill when the job is ran, the value for Full name (Step 1) will mapped to the **Message** input.
4. If there is no value in the Full name (Step 1) pill when the job is ran, the value for First name (Step 1) will be mapped to the **Message** input. Of course, if there's also no value in this First name (Step 1) pill, the job will fail at this step if **Message** is a required input field.

For more information on Ruby's ternary syntax, check out this [article](http://www.w3resource.com/ruby/ruby-ternary-operator.php).

## Example: Skip field if empty

When updating records, you want to preserve existing data while changing only the updated fields. In this situation, can you use the `skip` formula to instruct the Workato action to leave this field untouched.

This example attempts use an updated Salesforce record to update a lead in Marketo. It checks if the Salesforce Company (Step 1) is present. If yes, it will output the Salesforce Company (Step 1) into Marketo. Otherwise, the Marketo record is left untouched.

![Skip syntax](/assets/skip-formula.Dy0bSf6o.png)_Checks if Company (Step 1) is present. Outputs Company (Step 1) if present, otherwise, leaves this field untouched_

> **How to avoid passing any values**
> 
> The [skip formula](/en/formulas/other-formulas#skip) will avoid passing any data to the input field.

## Safe navigation operator

Checks if the input is not `nil` or undefined. If true, it performs a specified operation on the input data. Otherwise, it returns a `nil` value.

### Syntax

Input&.operation

- Input - An input datapill. It can be any datatype.
- operation - If the input is not `nil`, this formula is applied to the input data. This formula must be compatible with the input datatype.

### How it works

The safe navigation operator (`&.`) checks if the input data is not `nil` or undefined. If the input data exists, it performs the operation specified by the operation argument. Otherwise, it returns `nil`. This operator enables you to write simpler expressions to handle `nil` values.

#### Example: Converting dates safely

You can use the safe navigation operator when you're working with a datapill that might contain `nil` values.

For example, applying the `to_date` formula directly to the Created Date (Step 1) datapill would cause a `NoMethodError` if the datapill value is `nil`. The safe navigation operator enables you to handle these cases without complex ternary expressions.

```ruby
# Instead of: created_date.present? ? created_date.to_date(format:"MM/DD/YYYY") : nil
created_date&.to_date(format:"MM/DD/YYYY")
```

![Using safe navigation operator](data:image/png;base64,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)_Using the safe navigation operator_

### Example: Safe hash retrieval

You can also use the safe navigation operator when you have a nested hash structure, such as a customer record with optional address information.

**With safe navigation**:

```ruby
# This returns nil instead of an error if any key is missing
customer["address"]&.[]("billing")&.[]("zip_code")
```

**Without safe navigation**:

```ruby
# This could fail if "address" or "billing" doesn't exist
customer["address"]["billing"]["zip_code"]
```

The safe navigation operator prevents errors by returning `nil` if any key is missing. This approach allows you to retrieve nested hash values without worrying about `NoMethodError` exceptions.

---
