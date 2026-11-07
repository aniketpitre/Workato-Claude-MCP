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
