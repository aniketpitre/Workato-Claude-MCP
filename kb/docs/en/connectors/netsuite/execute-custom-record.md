---
url: 'https://docs.workato.com/en/connectors/netsuite/execute-custom-record.md'
description: >-
  The Execute saved search for custom record action in the NetSuite SOAP
  connector lets you retrieve custom records from a saved search, with optional
  filters.
---

# NetSuite SOAP - Execute saved search for custom record action

The **Execute saved search for custom record** action retrieves custom records from NetSuite based on a saved search, with optional filters to refine the results.

![Execute saved search for custom record action](/assets/execute-saved-custom.B9wwUlqa.png)_Execute saved search for custom record action_

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select the type of NetSuite custom record for which you plan to retrieve saved searches. |
| Saved search | Select a saved search from the list or enter the **Saved search ID** if it’s not listed. Ensure the saved search is set up correctly in NetSuite. |
| Object list | Select the specific custom records you plan to retrieve. You must select **Internal IDs** of the records to retrieve their data. |
| Fields | Select the custom record fields to include in the output. The selected fields appear in the output datatree. All fields are returned if left blank, but selecting specific fields is recommended for performance. You must include **Internal IDs** in the **Object list**. |
| Results list page size | Specify the number of records to retrieve per page. The default is 25 records per page. The minimum value is 5, and the maximum is 200. If the number of records exceeds the page size, use the **Search ID** and **Page number** fields to retrieve the remaining records. |
| Search ID | Provide the **Search ID** from a previous search to retrieve subsequent pages of results. When **Search ID** is specified, other search criteria are ignored. |
| Page number | Enter the page number to retrieve if the search returns more than one page. Use this field with **Search ID** to paginate through results. |
| Search settings | Configure additional operators to refine your search. For example, you can filter string fields using `Contains` or integer fields using `Equal to`. Each operator applies to all fields of that type. |

## Output

| Output field | Description |
| --- | --- |
| Search ID | The unique identifier for the search results. |
| Page number | The current page number of the results being retrieved. |
| Total pages | The total number of pages in the search result. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-get-standard-objects-action.md
description: >-
  The Get all standard objects action in the NetSuite SOAP connector returns the
  entire list of records for a selected standard record type in your NetSuite
  app.
---

# NetSuite SOAP - Get all standard objects action

The **get all standard objects** action returns the entire list of records of the selected record type in your NetSuite app.

1. Specify in the recipe exactly what standard object category you want to retrieve.
   
   The output of this action is list that contains all records in your NetSuite instance.
   
2. In downstream actions, filter this list of records using the `.where` methods in formula mode. See [List and hash formulas](/en/formulas/array-list-formulas#where) for details.
   
   ![Get all standard objects](/assets/get-all-standard-objects.9v9w9zA3.png)_Configuring the get all standard objects action_
   

If you can't find the object you're looking for, check with your NetSuite admin or with us!

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-get-case-comments-action.md
description: >-
  The Get case comments action in the NetSuite SOAP connector retrieves the case
  comments of a specific case in NetSuite by its case ID.
---

# NetSuite SOAP - Get case comments action

The action `Get case comments` allows you to retrieve the case comments of a specific case in NetSuite by its case ID.

![Get case comments](/assets/case-comments.BLPUZFfg.png)

## Input

- Case ID
  
- The Netsuite case's ID
  
- Results list page size
  
- The number of records to return. The maximum is 200 and the default is 25.
  
- Search ID
  
- Returned from a previous "Get case comments" action
  
- Page number
  
- Used in conjunction with Search ID to page through results
  

## Output

- Search ID
  
- Used in a downstream "Get case comments" action to page through results
  
- Page number
  
- Used in a downstream "Get case comments" action to page through results
  
- Total pages
  
- Total pages of results in the search
  
- Messages
  
- An array of cases
  

## Page through results to retrieve all case comments

Using the `foreach` loop in Workato, you can easily page through all case comments and back them up into a database for storage.

Check out [this sample recipe](https://www.workato.com/recipes/1084569?st=517170) for more details.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-search-standard-object-action.md
description: >-
  The Search standard objects action in the NetSuite SOAP connector returns a
  list of records that match your search criteria, or an empty array if none
  match.
---

# NetSuite SOAP - Search standard objects action

The **search standard objects** action returns a list of records that match the search criteria. If there are no matching records, the action returns an empty array.

> **UNSUPPORTED RECORDS**
> 
> [Certain records are not supported](/en/connectors/netsuite/netsuite-unsupported-records) in the action because of API limitations.

## Configure the search objects action

1. To search standard objects, specify in the recipe the category of the object, and the object itself.
   
   The following displays an unconfigured search standard object action.
   
   ![Unconfigured NetSuite search action](/assets/unconfigured-search-action.GBag_D2W.png)_Unconfigured search standard object action. Select the category and specific object to search._
   
2. Regardless of category, you can search for any standard objects either by its **internal ID** or its **external ID**.
   
   Because IDs are unique, the search retrieves at most one (1) record if you search by IDs.
   
   ![NetSuite search objects via internal or external ID](/assets/search-via-internal-external-id.BdaE6F5E.png)_Ability to search NetSuite record by unique internal ID or external ID_
   
   > **FIELD NAME MISMATCH**
   > 
   > Some NetSuite fields display internal API names instead of their labels in NetSuite.
   > 
   > For example, **entity ID** refers to the customer/vendor where to attach a transaction document, while **internal ID** refers to the NetSuite ID of any object.
   
3. You can search by most categories.
   
   Depending on the object category you select, you can search by additional fields specific to that category.
   
   ![NetSuite search action picklist](/assets/search-objects-action-list.BT9HsfjY.png)_Available categories to search_
   

> **FIELD SELECTION**
> 
> You can perform a search for an object with all fields selected in the drop-down menu. If certain fields are missing in the response, it's likely that the fields are not queryable in NetSuite. We recommend leaving the fields unselected in the drop-down menu to allow for all fields to populate in the response. ![NetSuite field selection menu](/assets/field-selection.BQZVdJCz.png)_NetSuite drop-down menu_

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-search-custom-object-action.md
description: >-
  The Search custom objects action in the NetSuite SOAP connector returns a list
  of records that match your search criteria, or an empty array if none match.
---

# NetSuite SOAP - Search custom objects action

The **search custom objects** action returns a list of records that match the search criteria. If there are no matching records, the action returns an empty array.

> **Unsupported records**
> 
> [Certain records are not supported](/en/connectors/netsuite/netsuite-unsupported-records) in the action because of API limitations.

## Configure the search objects action

1. To search custom objects, specify in the recipe the category of the object, and the object itself.
   
   The following displays an unconfigured search custom object action.
   
   ![Unconfigured search custom object action](/assets/unconfigured-search-custom-object-action.GNZNjXYJ.png)_Unconfigured search custom object action. Select the specific object to search_
   
2. Regardless of category, you can search for any custom objects either by its **internal ID** or its **external ID**.
   
   Because IDs are unique, the search retrieves at most one (1) record if you search by IDs.
   
   ![NetSuite search objects via internal or external ID](/assets/search-via-internal-external-id.BdaE6F5E.png)_Ability to search NetSuite record by unique internal ID or external ID_
   
   > **Field name mismatch**
   > 
   > Some NetSuite fields display internal API names instead of their labels in NetSuite.
   > 
   > For example, **entity ID** refers to the customer/vendor where to attach a transaction document, while **internal ID** refers to the NetSuite ID of any object.
   
3. You can search by most categories.
   
   Depending on the object category you select, you can search by additional fields specific to that category.
   
   ![NetSuite search action picklist](/assets/search-objects-action-list.BT9HsfjY.png)_Available categories to search_
   

If you can't find the field you're looking for, check with your NetSuite admin or with us!

---

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

---
