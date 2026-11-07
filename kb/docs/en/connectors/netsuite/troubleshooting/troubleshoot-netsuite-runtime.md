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
