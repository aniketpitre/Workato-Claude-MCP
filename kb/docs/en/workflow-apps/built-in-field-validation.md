---
url: 'https://docs.workato.com/en/workflow-apps/built-in-field-validation.md'
description: >-
  Learn how Workflow apps use built-in client-side validation to check email,
  URL, phone, and number fields as users enter data.
---

# Built-in field validation

![Invalid email error](/assets/email-validation.CRVyB_I8.png)_Built-in email validation_

Workflow apps includes built-in client-side field validation for specific page components. Built-in client-side validation ensures data accuracy, prevents errors, and enhances workflow efficiency. It guides the end-users of your apps to enter data correctly and aids compliance efforts. This ultimately enables you to create more reliable and streamlined business processes.

Workato recommends that you configure your recipes to perform additional validation in business-critical fields. Because data table entries can be edited directly in columns, they are not eligible for client-side validations.

## How it works

Workflow apps offers built-in client-side field validation for specific [page components](/en/workflow-apps/page-components). This feature enables you to ensure that users enter email addresses, phone numbers, and more in the correct format.

To see how Workato handles client-side built-in validations while building your page, click **Preview** to [preview your page](/en/workflow-apps/pages-preview).

### Compatible components

The following components have built-in field validation:

- Email
- URL
- Phone numbers
- Number

## Examples

The following examples demonstrate the error messages Workato displays when user input is invalid.

**Phone component in page editor**

No setup is required for components that offer built-in validation.

![Phone component in page editor](/assets/phone-field-setup.CA8JEEuh.png)_Phone component in page editor_

**Error message**

When user input does not match the format of the component, Workato displays the following error message. Similar messages are displayed for URL, email, and number components.

![Invalid format](/assets/phone-number-validation.BLhKjj79.png)_Error message: Invalid phone number_

**Other examples**

The following example shows the error message that Workato displays when users attempt to provide alphabetical characters as input in **Number** components.

![Invalid format- numbers](/assets/number-validation.DClI4PFC.png)_Error message: Value is not a number_

> **FURTHER READING**
> 
> Refer to our [custom field validation](/en/workflow-apps/custom-field-validation) guide to learn how to enforce custom field validation.

---
