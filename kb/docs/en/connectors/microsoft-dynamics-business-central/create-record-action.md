---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/create-record-action.md
description: >-
  Create a new record (for example, Item, Customer, Vendor) in Microsoft
  Dynamics Business Central.
---

# Microsoft Dynamics Business Central - Create record action

Use the **Create record** action to create a new record in Microsoft Dynamics Business Central. This action supports creating various entity types such as Items, Customers, Vendors, Sales Orders, Purchase Orders, and other business entities available in your Business Central instance.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to create from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| Company ID | Enter a Company ID to create the record in a specific company. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Record fields | Provide the data for creating the record. The available fields depend on the selected entity type and are dynamically generated based on your Business Central instance's metadata. |
| Display name (Record fields) | The display name of the record. |
| Number (Record fields) | The unique number identifier. |
| Type (Record fields) | The type or category of the record. |
| Status (Record fields) | The status of the record. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete record data that was created, including all fields returned by Business Central. The structure depends on the entity type selected. |
| ETag | The entity tag (ETag) for the created record. Use this ETag when updating the record to ensure data consistency. |
| ID | The unique identifier of the created record. |
