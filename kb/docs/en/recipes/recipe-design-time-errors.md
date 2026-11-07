---
url: 'https://docs.workato.com/en/recipes/recipe-design-time-errors.md'
description: >-
  Learn how to resolve recipe design-time errors in Workato, including missing
  required fields, formula syntax errors, and invalid datapills.
---

# Recipe design-time errors

Recipe design-time errors refer to errors which are caught while building a recipe. These errors typically show up when you select recipe test or recipe start, and prevent you from testing or starting the recipe until they are resolved. This is because recipes with design-time errors will definitely result in job errors if ran. We go through common design-time errors in this section.

![Recipe design-time errors show up when recipe is tested or started](/assets/design-time-errors-invalid-pills.ILskoxe4.png)_Recipe design-time errors show up when recipe is tested or started_

## Missing required input fields at design-time

Triggers and actions typically need configuration to be useful in a recipe. For example, to update a Zendesk organization, we need, at a minimum, the ID of the organization to update. Therefore, that's a required field in the recipe.

If the recipe detects that a required input field is lacking values or datapills, it will raise a design-time error and refuse to start until the input field has been filled with a value or a datapill.

You will be able to see the items needed to be fixed in the step details drawer.

![Missing required field](/assets/missing-required-field.Bc_9hvaV.png)_Recipe design error due to missing required input field_

Once you fix a specific error, the item will get crossed off your checklist.

![Fixed field](/assets/fixed-missing-field.DktRF1j7.png)_Fixed field_

## Design-time formula errors

Every input field (except for list input fields) can be toggled between text and formula mode. When in formula mode, errors in formula syntax will raise design-time errors.

Common design-time formula errors are:

- misspelled formulas (such as the above)
- lack of proper spacing between formulas and operators (for example, having 2 whitespaces instead of 1)
- formula syntax errors (for example, using curly braces `{ }` instead of square brackets `[ ]`)
- symbols in the wrong format (for example, when copying formulas and symbols from word processors like OpenOffice and Microsoft Word, these programs may format symbols like `"`, `'` and `{ }` differently and cause the Workato formula editor to not recognize these symbols)

## Invalid datapills

Datapills can become invalid when their source is missing, for example, if the trigger or action that the datapill comes from is changed, or if the field gets deleted from the app (for example, if the custom field `Customer subscription plan` in Salesforce object `Account` gets deleted in Salesforce, that datapill will become invalid for use in Workato). Invalid datapills will turn red.

In the following example, design-time errors due to invalid datapills are raised when the Salesforce trigger is changed.

![Salesforce trigger is changed from New/updated object to New object](/assets/design-time-errors-change-trigger.Dd8E7oGT.png)_Salesforce trigger is changed from New/updated object to New object_

To resolve issues with invalid datapills, you need to replace these pills with valid datapills or values.

## Unavailable fields

Sometimes you may receive a design-time error if the recipe uses data fields that aren't available in your app. You must either add the fields in your app and [refresh the schema](/en/recipes/editor#refresh-schema) in the recipe editor or remove the unavailable fields in your recipe.

![Field unavailable](/assets/field-unavailable.D4n4syt4.png)_Field unavailable_

## App connection errors

App connections can become invalid due to several reasons:

- app credentials were changed and the connection was not updated correspondingly in Workato
- connected user doesn't have the right set of permissions to read/write selected records
- permissions of the connected user was changed to a reduced scope

In such cases, reconnecting, or verifying that the connected user has permissions to read/write records used in the recipes should work to re-establish the connection.

---
