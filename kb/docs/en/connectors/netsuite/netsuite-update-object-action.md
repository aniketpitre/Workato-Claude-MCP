---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-update-object-action.md
description: >-
  The Update standard object and update custom object actions in the NetSuite
  SOAP connector let you update existing standard or custom records in NetSuite.
---

# NetSuite SOAP - Update standard object and update custom object actions

The **update standard object** and **update custom object actions** are very similar.

## Functions of the update object actions

You can make a number of different updates:

- Overwrite
  
- Overwrite existing field values with new values.
  
  You cannot delete an existing value of a field and change it to a null or a blank value.
  
- Append
  
- Append new lines to records.
  
  For example, add additional line items to your sales order.
  
- Replace
  
- Replace all lines in records.
  
  For example, overwrite all existing line items in your sales order with a new set of line items.
  

### Configure your update action

1. First, specify the object to update using an internal ID or external ID. To update your NetSuite record, you must specify which record to update. You can use either the internal ID or the external ID to specify the record - all other fields with values passed into them overwrite the original existing value in the NetSuite record.

![Specify record to update by ID](/assets/specify-record-to-update-by-id.DrRLHVFu.png)_Specifying the NetSuite record to update with either internal ID or external ID_

2. Next, configure the action to carry out the type of update you want: overwrite existing values or append values

- Overwrite existing field values

To do this, simply select the fields to which you plan to write. Then, input the values or variables you plan to use to overwrite the fields. For example, we might have a Shopify e-commerce site set up, and we want to move all our sales orders made in Shopify into NetSuite for inventory and delivery management.

In the following recipe, we're moving all newly created sales orders and all updates to existing orders from Shopify into NetSuite. Whenever there's a new/updated Shopify order, we try to search for the corresponding NetSuite order. If it exists, we update that NetSuite order. If it doesn't exist, we create a NetSuite order.

![Shopify to NetSuite recipe](/assets/shopify-to-netsuite-recipe.B4AnF-vD.png)_Recipe that syncs Shopify sales orders into NetSuite._

In Step 3, which is the branch of the recipe we execute if we find a NetSuite order that corresponds to the incoming Shopify sales order, we pass in the internal ID of the NetSuite order we've found.

![Specify NetSuite record to update via internal ID](/assets/specify-record-to-update-via-internal-id.BaiogsdJ.png)_Specify NetSuite record to update via internal ID_

In this update action, we're taking the values of the note and email fields in the Shopify order, and updating the values of the memo and email fields in the corresponding NetSuite order.

![Update memo and email fields](/assets/netsuite-fields-to-update.BmqAJbJC.png)_Update memo and email fields_

When selecting the fields to update in the NetSuite connector, take note that some NetSuite fields are displayed with their internal API names instead of their labels in NetSuite. For example, entity ID refers to the customer/vendor to attach a transaction document to, while internal ID refers to the NetSuite ID of any object.

If you can't find the field you're looking for, check with your NetSuite admin or with us!

- Append new lines to object or replace all lines in the object

There are numerous NetSuite objects which contain one or more lists. For example, transaction objects, including sales orders, have lists of line items. When you update objects in NetSuite, most lists offer you the ability to append more elements to the list, or replace the existing list with a whole new list.

First, specify the object you plan to update, then the specific ID of the object to update. Do the same data mapping for the item list as usual.

![Specify NetSuite record to update via internal ID](/assets/append-new-lines-update-object-via-id.k_7j5znr.png)_Select object and record ID to update_

At the end of most NetSuite lists, the **Replace all** option displays. Select **True** to overwrite all existing list items, and select **False** to append new list items to the existing list of items.

![Specify NetSuite record to update via internal ID](/assets/append-new-lines-replace-all-false.D0RxnDYr.png)_Replace all picklist found at the end of NetSuite lists_

When selecting the fields to update in the NetSuite connector, take note that some NetSuite fields are displayed with their internal API names instead of their labels in NetSuite. For example, entity ID refers to the customer/vendor to attach a transaction document to, while internal ID refers to the NetSuite ID of any object.

If you can't find the field you're looking for, check with your NetSuite admin or with us!
