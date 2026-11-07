---
url: 'https://docs.workato.com/en/connectors/servicenow/updated-record-trigger.md'
description: >-
  The New/updated record trigger in the ServiceNow connector picks up records
  created or updated in the selected table once every poll interval.
---

# ServiceNow - New/updated record triggers

## New/updated record

This trigger picks up records that are created or updated in the selected table. Each record is processed as a separate job. It checks for new or updated records once every poll interval.

![New/updated record trigger](/assets/updated-record-trigger.CBerSwGh.png)_New/updated record trigger_

### Input

| Input field | Description |
| --- | --- |
| [From](#from) | Records created or updated after this time will be processed by the recipe. If left blank, the default time will be set to **one day** before the recipe is first started. |
| [Table](#table) | Select a table to pick up new or updated records from. |

### Output

The output datatree of this trigger contains the full set of columns from the selected table. All default and custom columns are supported. The output fields will be displayed only after a table is provided, either by selecting a table from the pick list or by providing the full table name.

![Output fields](/assets/extended-output-new.DQm_WzGb.png)_Output fields_

## New/updated record (real-time)

This trigger picks up records in the selected table as soon they are created or updated. Each record is processed as a separate job. It makes use of business rules to detect and trigger a new or updated record event to be processed.

**To use this trigger, the connected user must have sufficient access control to sys\_script table. Learn how to configure [access control for real time triggers](/en/connectors/servicenow#real-time-trigger).**

![New/updated record trigger](/assets/updated-record-trigger-real-time.BSmcHiQE.png)_New/updated record trigger_

### Input

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table to pick up new or updated records from. |
| Query | ServiceNow query to filter the records you want. Example: `active=true^stateIN1,3`. If your query contains the operator `VALCHANGES`, `CHANGESFROM`, `CHANGESTO`, you must select **Yes** to the **Disable polling?** input field. [Learn more](https://docs.servicenow.com/bundle/paris-platform-user-interface/page/use/common-ui-elements/reference/r_OpAvailableFiltersQueries.html). |
| When first started, this recipe should pick up events from | Records created or updated after this time will be processed by the recipe. If left blank, the default time will be set to **one day** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Disable polling? | Polling allows us to retrospectively pull records from a previous timestamp specified in the **When first started, this recipe should pick up events from** field. In cases where your Query contains `VALCHANGES`, `CHANGESFROM`, `CHANGESTO` operators, you **must** disable polling. In all other cases, polling is highly recommended. |

### Output

The output datatree of this trigger contains the full set of columns from the selected table. All default and custom columns are supported. The output fields will be displayed only after a table is provided, either by selecting a table from the pick list or by providing the full table name.

![Output fields](/assets/extended-output-new.DQm_WzGb.png)_Output fields_

## Input field definitions

### When first started, this recipe should pick up events from

This is a user-defined time that marks the earliest time that the trigger should pick up created or updated records. If left blank, the default time will be set to **one day** before the recipe is first started.

The **Updated (sys\_updated\_on)** column is used to determine the time that a record is created or updated. Only records with **Updated (sys\_updated\_on)** timestamp later than the time specified in **From** will be processed by the trigger.

![Updated (sys\_updated\_on) timestamp](/assets/sys-updated-on.Dq0CQP0P.png)_Updated (sys\_updated\_on) timestamp_

### Table

Select the table to process records from. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

Make sure that the user used in the connection has [sufficient access control](/en/connectors/servicenow#roles-and-permissions-required-to-connect) to the selected table.

---
