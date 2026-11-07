---
url: 'https://docs.workato.com/en/connectors/concur/concur-migration-guide.md'
description: >-
  Migrate SAP Concur recipes from deprecated v2 and v3 API actions to the new v4
  list, list item, and expense report actions in Workato.
---

# SAP Concur - API Migration guide

SAP Concur has deprecated the List v3 API, List item v3 API and Expense report v2 API, replacing them with List v4, List item v4 and Expense report v4 API. Some APIs like List v3 and List item v3 have been deprecated by Concur but no decommissioning date has been set. We recommend migrating to their v4 APIs as soon as possible.

For the Expense report v2 APIs, no deprecation or decommissioning date has been set by Concur. However we recommend moving over to the new actions to utilize the latest APIs from Concur.

Workato have since deprecated old actions utilizing these endpoints and published new endpoints that utilize new V4 APIs. This particular version upgrade on Concur introduced changes that prevent us from automatically upgrading the actions without user intervention. Below, we will cover how to migrate your actions.

Reach out to our support teams to get details on which actions you have that might be impacted.

## Migrating to new triggers/actions from deprecated actions

For any Concur recipes that utilize these actions, you will see a prominent `Deprecated` tag next to the action within the recipe editor. There are a total of 5 deprecated actions:

1. Get all lists
2. Get list items
3. Create list item
4. Delete list item
5. Get expense report details
6. New expense report
7. New expense report submission
8. New or updated expense report submission

![Deprecated actions](/assets/deprecated-actions.DEISPgeF.png)_Actions using legacy APIs will have the deprecated tag shown next to the action in the recipe editor_

To replace these actions, simply click on the deprecated action and the `Action` section in the input configuration to switch the action. Then, search for the action via its current name. **The only exception is `Get list items` which has been replaced with `Get All List items`**

![Switch actions 1](/assets/switch-action-1.B0aQ5lhJ.png)_You should see two actions with the same name - 1 with a deprecated tag that is currently selected and 1 that is new_

Read the guides below for the action you are migrating.

### Get all lists

The deprecated `Get all lists` action did not contain any inputs.

When switching to the new `Get all lists` action, you will now have 2 new fields for `page number` and `sort by`. Verify that this new action will produce the same number of records and if needed, build pagination to retrieve the desired number of lists.

Ensure that the output datapills for the Get All list actions are remapped properly to downstream actions.

### Get list items

The deprecated `Get list items` action contained inputs for `list ID` as well as inputs for different level codes. Take note of your existing mappings before changing the action.

When switching to the new `Get All List items` action, the previous input for `list ID` should be mapped to the corresponding new `List ID` input field. Level codes should be mapped to the `Short code or value` input field. In the V4 of the API, you may also filter by the value of the list item directly.

Ensure that the output datapills for the Get All list actions are mapped properly to downstream actions.

### Create list items

The deprecated `Create list item` action contained inputs for `List`, `Item name` as well as level code. Take note of your existing mappings before changing the action.

When switching to the new create list item action, you can now either select the list input from a drop-down or provide the list ID. To get the list ID, you may use the `Get all lists` action. Map `Item name` to `Value` and `Level 1 code` to `Short code`.

The new `Create list item` has inputs that you may map to downstream actions as needed.

### Delete list items

The deprecated `Delete list item` action for contains inputs for `List name/ID` and `Item name/ID`. Take note of your existing mappings before changing the action.

When switching to the new delete list item action, you can now either select a list and item from a drop-down or provide the ID. If you have used the list name or item name as a datapill, you will need to add another step before the action to get the list ID via the `Get all lists` action or get the list item ID via the `Get list items` and searching by value.

Both delete actions do not have any output.

### Get expense report details

The deprecated `Get expense report details` action for contains inputs for `Report ID`. Take note of your existing mappings before changing the action. The value for the user ID should be the unique ID of the Concur user who is the report owner which can be retrieved from the `Get All users` action.

### New expense report/New expense report submission/New or updated expense report submission

The deprecated triggers are all related to the Expense report v4 API. When swapping the triggers over, the output datapills may be different and you will be notified via warnings on the recipe editor for actions that require you to remap the output datapills.

---
