---
url: 'https://docs.workato.com/en/recipes/design-time-errors/empty-actions.md'
description: >-
  Learn how to identify and fix action and field errors in Workato recipes,
  including empty actions, missing input fields, and invalid datapills.
---

# Action and fields errors

Ensure all actions and triggers in your Workato recipe are fully configured and contain all necessary data. Errors can occur due to several reasons:

- [Empty actions](/en/recipes/design-time-errors/empty-actions#empty-actions)
- [Missing input fields](/en/recipes/design-time-errors/empty-actions#missing-input-fields)
- [Unavailable fields](/en/recipes/design-time-errors/empty-actions#unavailable-fields)
- [Invalid datapills](/en/recipes/design-time-errors/empty-actions#invalid-datapills)

This section provides guidance on identifying and resolving these common errors.

## Empty actions

Empty actions in a recipe can prevent the recipe from starting properly. Each action must have all necessary fields filled out to start correctly. Leaving an action empty means it does not have the required configuration or data to execute its function. These issues typically occur due to incomplete configuration, missing required fields, or changes to previous steps that leave subsequent actions with missing data.

![Empty action](/assets/empty-action.nT1apEOH.png)_Empty action_

To resolve issues related to empty actions, review all actions in your recipe and ensure all fields are filled out.

## Missing input fields

Triggers and actions require configuration to function correctly in a recipe. For example, to update a record in Salesforce, you must provide the ID of the record. If the recipe detects a required input field without values or datapills, it raises a design-time error and does not start until the input field is filled with a value or datapill.

Complete the following steps to identify and fix missing input fields:

1. Locate the error notifications that highlight the missing fields in the step details section.
   
   ![Required field error](/assets/input-field-error.BJ7gbgiM.png)_Required field error_
   
2. Enter the necessary values or datapills for each required field.
   
3. Resolve the specific error to cross the item off your checklist.
   
   ![Fix missing field](/assets/fix-input-field.wVrpNwrq.png)_Fix missing field_
   

## Unavailable fields

You may receive a design-time error if your recipe uses data fields that aren't available in your app. This can happen if a field in your app is deleted or renamed.

Complete the following steps to resolve unavailable fields:

1. Identify the missing fields by reviewing the error notification in your recipe.
   
   ![Review error notification](/assets/unavailable-field.DiKI3UJL.png)_Review error notification_
   
2. Add the missing fields to your app and [refresh the schema](/en/recipes/editor#refresh-schema) in Workato. Remove or replace fields that are no longer required in your recipe.
   
3. Verify that all fields in your recipe are valid and correctly configured.
   

## Invalid datapills

Mapping datapills from a certain step and later deleting or skipping that step can introduce errors. These changes can disrupt the following steps and prevent the recipe from starting. Datapills can become invalid when their source is missing. For example, if the trigger or action that provides the datapill is changed, or if the field is deleted from the app, the datapill becomes invalid and turns red.

In the following example, design-time errors due to invalid datapills occur when the Salesforce trigger is changed from **New/updated record** to **Deleted record**.

![Replace invalid datapills](/assets/replace-invalid-datapills.JJ9iAVW-.png)_Replace invalid datapills_

---
