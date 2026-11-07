---
url: 'https://docs.workato.com/en/connectors/oracle-fusion-cloud/general-setup.md'
description: >-
  Set up the metadata-based Oracle Fusion Cloud connector in Workato, including
  object selection and mapping main and child object fields at design time.
---

# General setup

The Oracle Fusion Cloud connector is metadata-based. It retrieves input and output schemas for objects you select at design time.

## Object setup

When you choose an action or trigger, the first step is object selection. After selecting an object (such as Invoice or Receivable Credit Memo), the connector fetches all relevant input fields for that object.

![Object selection populates the fields in the action](/assets/input-fields.BMkIkUTe.png)_Object selection populates the fields in the action_

If you don't have access to the selected object resource in Oracle Fusion Cloud (for example, an HCM module object not enabled in your plan), a 403 Forbidden error appears.

![Error populating the fields of the specific object](/assets/input-fields-error.BXf6rjf2.png)_Error populating the fields of the specific object_

The populated fields include both main object properties and child object properties. For example, Invoices includes main attributes like Invoice number, Business unit, and Invoice amount, plus child objects like Invoice Lines, Invoice installments, and Attachments.

![Main attributes under Invoice](/assets/main-attributes.CUeaYS_x.png)_Main attributes under Invoice_

![Child objects under Invoice](/assets/child-attributes.DacZmJG8.png)_Child objects under Invoice_

Each child object accepts a list input, which is useful when passing data from upstream systems. For example, you can pass product line items from Salesforce to the Invoice Lines child object.

![Passing list datapill to child object](/assets/list-datapill.BvkStE1t.png)_Passing list datapill from Salesforce to the child object Invoice lines_

To input child objects manually instead of using a list, change the list to a fixed list and add items individually.

![Fixed list setup under child object](/assets/fixed-list.9QimpahR.png)_Fixed list setup under child object_

Child objects can contain additional nested objects, accessible using the same method. This allows you to add inputs at any depth for a record.

---
