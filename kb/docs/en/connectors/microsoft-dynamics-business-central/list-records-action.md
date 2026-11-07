---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/list-records-action.md
description: >-
  Retrieve a list of records for a specific entity type in Microsoft Dynamics
  Business Central.
---

# Microsoft Dynamics Business Central - List records action

Use the **List records** action to retrieve a list of records for a specific entity type in Microsoft Dynamics Business Central. This action returns all available records for the selected entity type, such as Items, Customers, Vendors, Sales Orders, Purchase Orders, Companies, or Environments.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to list from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, Company, Environment, and more. |
| Company ID | Enter the Company ID to list records from. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |

## Output

| Output field | Description |
| --- | --- |
| Objects | An array of records for the selected entity type. Each record includes all entity-specific fields as defined in your Business Central instance, the entity tag (ETag) for each record for most entity types, and the unique identifier (ID) of each record. |
