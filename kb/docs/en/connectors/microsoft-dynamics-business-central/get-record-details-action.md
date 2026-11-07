---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-business-central/get-record-details-action.md
description: >-
  Retrieve the details of a specific record through its ID in Microsoft Dynamics
  Business Central.
---

# Microsoft Dynamics Business Central - Get record details by ID action

Use the **Get record details by ID** action to retrieve the complete details of a specific record in Microsoft Dynamics Business Central using its unique identifier. This action supports retrieving various entity types such as Items, Customers, Vendors, Sales Orders, Purchase Orders, and other business entities.

## Input

| Input field | Description |
| --- | --- |
| Entity name | Select the entity type to retrieve from the drop-down menu. Examples include Item, Customer, Vendor, Sales Order, Purchase Order, and more. |
| ID | The unique identifier of the record to retrieve. |
| Company ID | Enter the Company ID where the record exists. If provided, this overrides the Company ID from the connection settings. Leave blank to use the Company ID specified in the connection. |
| Journal ID | The unique identifier of the journal that contains the journal line. Required for Journal Line entity. |

## Output

| Output field | Description |
| --- | --- |
| Record data | The complete record data, including all fields returned by Business Central. The structure depends on the entity type selected and includes all properties defined in your Business Central instance. |
| ETag | The entity tag (ETag) for the record. Use this ETag when updating the record to ensure data consistency. |
| ID | The unique identifier of the retrieved record. |
