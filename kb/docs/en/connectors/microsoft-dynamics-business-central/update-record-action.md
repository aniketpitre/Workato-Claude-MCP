---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/update-record-action.md
description: Update an existing record in Microsoft Dynamics Business Central.
---

# Microsoft Dynamics Business Central - Update record action

Use the **Update record** action to update an existing record in Microsoft Dynamics Business Central. This action supports updating various entity types such as Items, Customers, Vendors, Sales Orders, Purchase Orders, and other business entities available in your Business Central instance.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to update from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| ID | The unique identifier of the record to update. |
| ETag | The entity tag (ETag) of the record to update. The ETag ensures data consistency and prevents overwriting changes made by other users. |
| Company ID | Enter the Company ID where the record exists. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Record fields | Provide the fields to update. Only include the fields you plan to change. The available fields depend on the selected entity type and are dynamically generated based on your Business Central instance's metadata. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete updated record data, including all fields returned by Business Central. The structure depends on the entity type selected. |
| ETag | The new entity tag (ETag) for the updated record. Use this ETag for subsequent updates to ensure data consistency. |
| ID | The unique identifier of the updated record. |
