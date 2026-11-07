---
url: >-
  https://docs.workato.com/en/connectors/gumroad/get-record-details-by-id-action.md
description: >-
  Retrieve the details of a Gumroad record, such as a sale or subscriber, by its
  unique ID.
---

# Gumroad - Get record details by ID action

The **Get record details by ID** action retrieves a record, such as a sale or subscriber, by its unique ID in Gumroad.

## Input

Input fields dynamically generate based on the **Object** you select.

| Input field | Description |
| --- | --- |
| Object | Select the object type. Options are **Sale** or **Subscriber**. |
| Sale ID | Select the sale to retrieve. Alternatively, enter the sale ID. The **Sale ID** field is only available when **Object** is **Sale**. |
| Subscriber ID | Enter the unique ID of the subscriber to retrieve. The **Subscriber ID** field is only available when **Object** is **Subscriber**. |

## Output

Output fields dynamically generate based on the **Object** you select. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields. The following fields are common to all objects:

| Output field | Description |
| --- | --- |
| ID | The unique ID of the record. |
| Email | The email address of the buyer or subscriber. |
| Product ID | The unique ID of the product. |
| Product name | The name of the product. |
| Created at | The date and time the record was created. |
| License key | The license key issued for the record. |
