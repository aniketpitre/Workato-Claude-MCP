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
