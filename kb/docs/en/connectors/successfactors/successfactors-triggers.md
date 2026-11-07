---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-triggers.md
description: >-
  Explore SAP SuccessFactors connector triggers in Workato, including the New or
  updated object polling trigger that runs when an object is created or updated.
---

# SAP SuccessFactors - Triggers

## New or updated object

This [polling trigger](/en/recipes/triggers#polling-triggers) runs the recipe when you create or update a specific SuccessFactors object, such as a user.

- Trigger poll interval
  
- Enter a value to instruct the recipe how frequently to check for new events. If you leave this blank, the recipe defaults to checking every 10 minutes.
  
  This is an optional field.
  
- Object
  
- Select a SuccessFactor object from the drop-down list. Because many objects have identical names, the list includes the object's internal names.
  
- Object unique key
  
- Select the ID that the recipe uses to identify the monitored object.
  
- When first started, this recipe should pick up events from
  
- Specify the date and time for the trigger to start monitoring for events, using the format `MM/DD/YYYY HH:MM am/pm`.
  
  If you leave this field empty, the default condition is one hour: the recipe retrieves records that were created or updated one hour ago.
  
  You cannot change this value after you run or test the recipe.
  
  This is an optional field. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
  
- Output fields
  
- By default, Workato will fetch all available fields in the selected record. You may use this input to filter for only the output fields you need.
  
  This is an optional field.
  
- Query
  
- Enter the OData query filters.
  
  See [SAP documentation](https://help.sap.com/doc/7efdca36492e47c7b20ab92c4ca6323c/2211/en-US/SF_EC_OData_API_REF.pdf#page=36) to learn more about filtering with the OData v2 API.
  
  This is an optional field.
  
- From date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from “from date” to the effective end date. You must not use “from date” together with “as of date”.
  
  This is an optional field.
  
- To date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from the effective start date to the “to date”. You must not use “to date” together with “as of date”.
  
  This is an optional field.
  
- As of date
  
- Pick a date or enter it in MM/DD/YYYY format. You must not use "as of date" together with “from date” or “to date”.
  
  This is an optional field.
  
- Set trigger condition
  
- Set a [Trigger condition](/en/recipes/triggers.html#trigger-conditions) to define additional rules for trigger events to run a recipe.
  
  This is an optional field.
  

## New or updated objects in batch

This [batch trigger](/en/recipes/triggers#batch-triggers) retrieves a list of records created or updated after the last time the recipe was triggered.

- Trigger poll interval
  
- Enter a value to instruct the recipe how frequently to check for new events. If you leave this blank, the recipe defaults to checking every 10 minutes.
  
  This is an optional field.
  
- Object
  
- Select a SuccessFactor object from the drop-down list. Because many objects have identical names, the list includes the object's internal names.
  
- Object unique key
  
- Select the ID that the recipe uses to identify the monitored object.
  
- When first started, this recipe should pick up events from
  
- Specify the date and time for the trigger to start monitoring for events, using the format `MM/DD/YYYY HH:MM am/pm`.
  
  If you leave this field empty, the default condition is one hour: the recipe retrieves records that were created or updated one hour ago.
  
  You cannot change this value after you run or test the recipe.
  
  This is an optional field. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
  
- Batch size
  
- Specifies the maximum number of records per trigger event. Minimum is 1, maximum is 500, default is 500.
  
  This is an optional field.
  
- Output fields
  
- By default, Workato will fetch all available fields in the selected record. You may use this input to filter for only the output fields you need.
  
  This is an optional field.
  
- Query
  
- Enter the OData query filters.
  
  See [SAP documentation](https://help.sap.com/doc/7efdca36492e47c7b20ab92c4ca6323c/2211/en-US/SF_EC_OData_API_REF.pdf#page=36) to learn more about filtering with the OData v2 API.
  
  This is an optional field.
  
- From date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from “from date” to the effective end date. You must not use “from date” together with “as of date”.
  
  This is an optional field.
  
- To date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from the effective start date to the “to date”. You must not use “to date” together with “as of date”.
  
  This is an optional field.
  
- As of date
  
- Pick a date or enter it in MM/DD/YYYY format. You must not use "as of date" together with “from date” or “to date”.
  
  This is an optional field.
  
- Set trigger condition
  
- Set a [Trigger condition](/en/recipes/triggers.html#trigger-conditions) to define additional rules for trigger events to run a recipe.
  
  This is an optional field.
