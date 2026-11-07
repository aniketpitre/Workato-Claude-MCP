---
url: 'https://docs.workato.com/en/troubleshooting/undefined-method-for-nilclass.md'
description: >-
  Troubleshoot the Undefined method for nil:NilClass error in Workato recipes
  that occurs when a formula runs on an empty datapill.
---

# Undefined method for nil:NILClass

Troubleshoot undefined method error under 3 min

[Video](https://www.youtube.com/embed/0I25iPuDd2Y)

You may encounter the following error when you use a formula on a datapill that doesn't contain a value:

```text
Undefined method for nil:NilClass
```

This error indicates that the datapill didn't contain a value at runtime.

![Example of Undefined method for nil:NILClass](/assets/undefined-method-for-nilclass.DZcLYAhV.png)_Example of Undefined method for nil:NILClass_

## Why it happens

This error occurs when the value of the datapill is `null` at runtime. The following scenarios can cause this error:

- A **Get** action returns records with missing fields.
- A **Search** action returns no results.
- A SQL query returns 0 rows.

For example, your datapill doesn't contain any value when step 2 has missing fields, which means that step 3 (Update lead in Marketo) applies a formula to an empty datapill.

![Example of Undefined method for nil:NILClass](/assets/undefined-method-for-nilclass-example.D7a7w72Q.png)_Example of Undefined method for nil:NILClass_

Since the `capitalize` formula doesn't apply to a datapill with no value, the job fails with the following error:

```text
Error calculating input for field 'company':
Formula received a nil value:
undefined method `capitalize' for nil:NilClass
```

## How to troubleshoot

Use the `&` safe navigation operator in your formula to prevent errors when the datapill is null. For example:

```text
[Datapill]&.capitalize
```

The operator checks if the datapill has a valid value:

- The operator applies the formula if the datapill contains a value.
- The operator skips the formula and returns `null` if the datapill is null.

This ensures the recipe continues without failure.

![Example of using the safe navigation operator](/assets/save-navigation-operator.WIfbGqw7.png)_Example of using the safe navigation operator with the `.capitalize` formula_

---
