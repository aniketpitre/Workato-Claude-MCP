---
url: 'https://docs.workato.com/en/connectors/hubspot/triggers/new-form-submission.md'
description: >-
  The New form submission trigger in the HubSpot connector notifies you when a
  new form is submitted, checking for new submissions every five minutes.
---

# HubSpot - New form submission trigger

The **New form submission** trigger notifies you when a new form is submitted in HubSpot. The trigger checks for new form submissions every five minutes after the recipe is started.

## Input

| Input field | Description |
| --- | --- |
| Form | Use the drop-down menu to choose **Select from list** or **Enter form ID** to select the form you plan to monitor for new submissions. Only the first 1000 records are displayed. |
| Unique field | Use the drop-down menu to choose **Select from list** or **Provide custom value**. The unique field ensures that you do not receive duplicate form submissions. |
| When first started, this recipe should pick up events from | Use the calendar and time menus to select the date and time at which the trigger should begin to fetch new form submissions. The trigger fetches form submissions created during the past hour if left blank. After you run or test the recipe, you cannot change the value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

This trigger returns a datatree that contains information about the form submission.

---
