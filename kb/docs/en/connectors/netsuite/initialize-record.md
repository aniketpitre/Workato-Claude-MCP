---
url: 'https://docs.workato.com/en/connectors/netsuite/initialize-record.md'
description: >-
  The Initialize record action creates a new NetSuite record that is pre-filled
  with data from a related record
---

# NetSuite SOAP - Initialize record action

The **Initialize record** action creates a new NetSuite record with data from a related record. You can use this action to create records like Cash Sales or Item Fulfillments based on existing transactions. This action retrieves all relevant fields and line items from the source record, removing the need for additional lookups or manual field mapping.

## Input

| Input field | Description |
| --- | --- |
| Record | Specify the NetSuite record type to initialize. Options include: Assembly Build, Assembly Unbuild, Cash Sale, Credit Memo, Customer Payment, Customer Refund, Estimate, Invoice, Item Fulfillment, Item Receipt, Return Authorization, Vendor Bill, Vendor Credit, Vendor Payment, Work Order Close, Work Order Completion, Work Order Issue |
| Reference record | Select the related record type to use as a reference. Options vary based on the selected record: **Assembly Build**: Assembly Item, Sales Order, Work Order; **Assembly Unbuild**: Assembly Build, Assembly Item; **Cash Sale**: Customer, Estimate, Opportunity, Sales Order; **Credit Memo**: Cash Sale, Invoice, Sales Order; **Customer Payment**: Credit Memo, Invoice, Sales Order; **Customer Refund**: Credit Memo, Customer Payment; **Estimate**: Customer, Opportunity; **Invoice**: Estimate, Opportunity, Sales Order; **Item Fulfillment**: Sales Order, Transfer Order; **Item Receipt**: Purchase Order, Transfer Order, Return Authorization; **Return Authorization**: Cash Sale, Invoice, Sales Order; **Vendor Bill**: Purchase Order; **Vendor Credit**: Purchase Order, Vendor Bill; **Vendor Payment**: Vendor Bill, Vendor Credit; **Work Order Close**: Work Order; **Work Order Completion**: Work Order; **Work Order Issue**: Work Order |
| Reference record ID | Provide the internal ID of the reference record in NetSuite. |

## Output

The output schema is dynamically generated based on the selected record type. It includes the fields relevant to the initialized record.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/troubleshooting/troubleshoot-netsuite-connection.md
description: >-
  Use this guide to troubleshoot errors that occur when establishing a NetSuite
  connection in Workato.
---

# Troubleshoot NetSuite connection errors

Use this guide to troubleshoot errors that occur when establishing a NetSuite connection in Workato.

## Error establishing connection when Subsidiaries feature isn't enabled

You may receive a connection error if your NetSuite account doesn't have the Subsidiaries feature enabled. This error can occur even if your account has only one legal entity.

To resolve this issue:

- Enable the subsidiaries feature in NetSuite.
- Grant the integration user access to the correct subsidiary if the feature is already enabled.

Ensure the integration user has the following NetSuite permissions:

- SOAP Web Services
- Set Up Company
- User Access Tokens
- Log in using OAuth 2.0 Access Tokens

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/troubleshooting/troubleshoot-netsuite-runtime.md
description: >-
  Use this guide to troubleshoot errors that occur at runtime when you use the
  Netsuite connector in Workato.
---

# Troubleshoot NetSuite runtime errors

Use this guide to troubleshoot errors that occur at runtime when you use the NetSuite connector in Workato.

## Search returns no results when using the status field

You may receive a result of `0` when using the **Status** field in a NetSuite search, even though the field contains values.

This happens when you use the status label displayed in the output (for example, `Pending Billing/Partially Fulfilled`) as the input value. NetSuite requires you to use the corresponding enum value instead, such as `_salesOrderBilled`).

In this example, the following output displays the status as `Billed`:

![Search output](/assets/output.t8glNk35.png)_Output displays status value_

To return results, use the enum `_salesOrderBilled_` in the search input:

![Enum value used in input](/assets/search-sales.CntYQMoU.png)_Enum value used in input_

This issue occurs because the **Status** field requires an enum value, but the search uses the display value shown in the output. These values differ, so the search returns no results.

Use the correct enum value in the **Status** field to retrieve records. Refer to [NetSuite's list of enum values](https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2019_2/schema/enum/transactionstatus.html?mode=package) for more information.

## Custom field doesn't appear in Workato

This error occurs when you create a custom field in your NetSuite instance and it doesn't display in Workato. To resolve this issue:

1. Refresh the schema.
   
2. Click **Show optional fields** and check if the custom field is present.
   
3. Ensure that the custom field is linked to the object in NetSuite.
   
4. Verify that the custom field is not set to **Hidden** or **Disabled** in the NetSuite **Display** tab.

---
