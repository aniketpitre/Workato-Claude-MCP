---
url: 'https://docs.workato.com/en/connectors/netsuite/netsuite-add-object-action.md'
description: >-
  The Add standard object and add custom object actions in the NetSuite SOAP
  connector let you create new standard or custom records in NetSuite.
---

# NetSuite SOAP - Add standard object and add custom object actions

The **add standard object** and **add custom object** actions are similar; we describe them here together.

## Configure the add object action

1. Select the object you plan to create.
   
   Let's create a sales order.
   
2. The recipe retrieves the fields of your selected NetSuite object.
   
   ![Unconfigured NetSuite add object action](/assets/unconfigured-netsuite-add-action.D4arHlEm.png)_NetSuite add object action - unconfigured. Select the object to create._
   
3. Select and map the specific fields you plan to write to when creating the new NetSuite record.
   
   ![Unconfigured NetSuite add object action](/assets/netsuite-add-action-fields-selector.DzeOPsWB.png)_Select the specific fields you plan to write to_
   
4. Some NetSuite fields display their internal API names instead of their labels in NetSuite.
   
   For example, **Entity ID** refers to the customer/vendor where to attach a transaction document, while **Internal ID** refers to the NetSuite ID of any object.
   

If you can't find the field you're looking for, check with your NetSuite admin or with us!

---
