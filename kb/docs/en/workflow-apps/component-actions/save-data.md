---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/save-data.md'
description: >-
  Configure a Save data to table action on a button to save workflow request
  data to a Workflow app's primary data table.
---

# Save data to table action

Specific page components enable you to save workflow request data to your Workflow app's primary data table.

## Compatible components

| Component | Trigger event |
| --- | --- |
| Button | Button click |

## Configure a Save data to table action

Complete the following steps to configure a **Save data to table** action on button click:

1. Select a **Button** component.
   
2. Go to the **Action** panel. The **Trigger** event, `Button is clicked` is pre-selected.
   
3. Use the **Action** drop-down to select `Save data to table`.
   
4. Optional. Use **Additional data for table columns** to save extra data to the table row alongside the submitted page fields. Click **\+ Add column**, then map a page variable or static value to a data table column.
   
5. Use the **Redirect to** drop-down menu to choose where to redirect the user after saving data to the table.
   
6. Click **Save**.
   

> **LIMITATIONS**
> 
> The **Column** drop-down menu for **Additional data for table columns** only lists compatible data table columns. You can't map the same column more than once. If a mapped page variable has no value when the user submits, the column saves as empty and doesn't block submission. Static values must match the target column's data type, or the mapping shows a validation error.

Your configuration should look as follows:

![Save data to table](/assets/save-data.9IQE-LEg.png)_Save data to table on button click_

---
