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
