---
url: 'https://docs.workato.com/en/workflow-apps/page-properties.md'
description: >-
  Reference for Workflow apps component design properties, including editable,
  appearance, data, options, and rules, and which components support each.
---

# Component design properties

Customize page components using the properties panel. The properties panel provides options that enable you to create dynamic pages that change in response to user input. You must configure each property for each component on your page.

The following table provides a high-level overview of the different types of page properties and component compatibility. Each property has a unique set of configurable fields. Additionally, the set of available properties varies for each page component.

View our [page components](/en/workflow-apps/page-components) documentation for information on customizing properties for each type of page component.

| Property | Description | Compatible components |
| --- | --- | --- |
| Editable | Determine whether page components are editable, read-only, or editable only under the conditions you specify. The editability of components affects what other properties are customizable. | Data table, Linked tables, Text, Number, Choices, Data, Button, File upload |
| Appearance | Determine how components appear on the page. This includes deciding whether components are required, visible, assigning hints and placeholders to your components, and more. | Text, Number, Choices, Contact, Display, Data tables, Linked tables, Data, Buttons, File download, File upload |
| Data | Configure how your data tables appear on your pages. This includes choosing which columns appear on your page, filtering columns, and more. | Linked tables, View |
| Options | Configure how choices components appear on your page by determining the source for multiple choice (drop-down) components. | Drop-down |
| Rules | Set rules for these components. For example, you can determine whether users must fill out the field to submit the form. Additionally, you can create validation rules, including limiting user input, pattern matching, and setting accepted file types and maximum file sizes. | Text, Number, Choices, Contact, Date, File upload _Note: The specific type of rules you can configure varies by component type._ |

---
