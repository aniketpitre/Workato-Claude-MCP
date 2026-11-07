---
url: 'https://docs.workato.com/en/connectors/intacct/troubleshoot-intacct-runtime.md'
description: >-
  Use this guide to troubleshoot errors that occur at runtime when you use the
  Intacct connector in Workato.
---

# Troubleshoot Intacct runtime errors

Use this guide to troubleshoot errors that occur at runtime when you use the Intacct connector in Workato.

## Custom fields don't display in the recipe

Custom fields created for a **Sales Order** or **Sales Invoice** may not appear when you create or convert sales transactions in a recipe.

Ensure that the custom field is associated with an **Order Entry Transaction Detail** object to resolve the issue.

![order entry transaction detail object](/assets/custom-field.BsmtcDj7.png)_Associate the custom field with the order entry transaction detail object_

This association allows the recipe to use the custom field as an optional field.

![The custom field appears as an optional field in the recipe](/assets/optional-field.BYxLUvES.png)_The custom field appears as an optional field in the recipe_

---
