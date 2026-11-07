---
url: 'https://docs.workato.com/en/features/variables.md'
description: >-
  Variables by Workato lets you declare mutable, typed datapills that hold and
  update values within the scope of a single recipe job.
---

# Variables by Workato

Workato variable is a user-declared [datapill](/en/recipes/data-pills-and-mapping) that contains a data value. These user-declared variables are different from a standard datapill in that your declared variables are mutable - the value of the variable can be changed within a recipe.

The lifetime of a variable is for the duration of a single job (job scope) - there is no persistence, and no mechanism can access this across different jobs.

Workato variables are typed. In order to use variables, you will first have to declare it using the [create variable](#create-variable) action. To update the variable, use [update variables](#update-variables) action.

### Example

If you want to find a particular entry within a report - the entry with the _largest ARR_.

1. Create a variable called `ARR`.
2. Run the [for each](/en/recipes/steps#repeat-step) action, and update `ARR` whenever it finds a higher value.
3. Subsequently, use the `ARR` value to call up that specific entry.

![Iterate through the report for highest ARR](/assets/run-through-list-for-highest-arr.zy1sQvvB.png)_Iterate through the report for highest ARR_

### Connection setup

No connection setup is required. Simply select **App** > **Variables by Workato** to get started.

![Variables by Workato](/assets/variables-by-workato.CKNrk9JJ.png)_Variables by Workato_

## Create variable

This action creates variables in the specified data type. You should configure each variable to match the data type that it will be used for (for example, `integer`, `string`).

![Create variable](/assets/create-variable-action.CQXy5tOZ.png)![Create variable dialog](/assets/create-variable-action-dialog.Ci-Tl4jo.png)_Create variable dialog box_

Multiple variables can be created in this step by clicking on **Add variable**![Create multiple variables](/assets/create-multiple-variables.DFuduNo_.png)_Creating multiple variables_

| Input field | Description |
| --- | --- |
| Label | The name of the variable. |
| Data type | The [data type](/en/recipes/data-pills-and-mapping#data-types) of the variable. |
| Default value | The default value of the variable. Leave this blank to set the default value as `nil`. |

## Update variables

This action updates existing variables. You can only update variables previously created with the [Create variable](#create-variable) action. Otherwise, this action cannot be used.

![Update variables](/assets/update-variables-action.CzodQnT7.png)_Update variable_

| Input field | Description |
| --- | --- |
| Variable name | Select the variable(s) to update. |
| Input mode | Choose **Structured** to update field inputs individually or **Raw** for a single complete payload input. Only applies to variables with the **Object** data type because primitive variables (strings, numbers, booleans) are single values with no separate fields to structure. |
| `Variable` | The new value of the variable. |

> **Note**
> 
> This action does not generate a datapill. To use this variable in another action, use the Variable datapill in the **Create variable** step.

### Reset the value of a variable

You can set a `nil` value to variables in Update variable action to remove an existing value of a variable. This has to be done in the formula mode.

## Create list

This action create a list with custom schema. You can create an empty list or create a list with existing items.

![Create list](/assets/create-list-action.BCx_G7VB.png)_Create list_

| Input field | Description |
| --- | --- |
| List name | The name of the list. |
| List item schema | Define the properties of each item on this list. |
| Items | (Optional) Provide a list datapill to populate the list. You can [add more items](#add-item-to-list) afterwards. |

### Define list item schema

The list item schema will show up as a list of usable variables in the output datatree. These variables can be mapped unto subsequent recipe steps. Use **Add field** to define a new field.

![Add new field](/assets/add-new-field.Dz5PRlDR.png)_Add new field_

| Input field | Description |
| --- | --- |
| Name | The name of the new field. |
| Data type | The data type of the new field. |
| Optional | Select if this new field is mandatory. |
| Hint | A description of this new field. |

### Navigate list items

To iterate through items in a list, use the List index datapill from the **Create variable list** action output and a method that supports pagination, such as a **Repeat while** loop. Refer to the [Repeat while loops](/en/recipes/loops) documentation for more information.

## Add item to list

This action appends a new item entry to an existing list. You can only update lists created with **Variables by Workato**.

> **Add items in batches**
> 
> If you have a list datapill, [add them to the list in batches](#add-item-to-list-batch).

Some item fields are mandatory. Check that you have valid inputs for the required fields before using this action.

![Add item to list](/assets/add-item-to-list-action.BLj6rHn7.png)_Add item to list_

| Input field | Description |
| --- | --- |
| List name | Select the list to add your new entry. |
| Insert location | Select the location of the new entry. |
| List item | Define the values of the new entry. |

> **Note**
> 
> This action does not generate a datapill. To use this list in another action, use the datapills in the [Create list](#create-list) step.
> 
> Refer to [List management](/en/features/list-management) for more information.

## Add item to list (Batch)

This action appends multiple items to an existing list. You can only update lists created with **Variables by Workato**.

Some item fields are mandatory. Check that you have valid inputs for the required fields before using this action.

![Add item to list](/assets/add-item-to-list-batch-action.Cx2B3ap4.png)_Add item to list_

| Input field | Description |
| --- | --- |
| List name | Select the list to add your new entry. |
| Insert location | Select the location of the new entry. |
| List items | Provide a list datapill. Define how each list item is mapped. |

> **Note**
> 
> This action does not generate a datapill. To use this list in another action, use the datapills in the [Create list](#create-list) step.
> 
> Refer to [List management](/en/features/list-management) for more information.

## Clear all items from list

This action removes all entries in an existing list. This action should be used after the **Create list** and **Add items to list** action. You can only clear lists created with **Variables by Workato**.

| Input field | Description |
| --- | --- |
| List name | Select the list to clear all entries from. |

---
