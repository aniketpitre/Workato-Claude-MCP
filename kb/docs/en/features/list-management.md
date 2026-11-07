---
url: 'https://docs.workato.com/en/features/list-management.md'
description: >-
  Learn how to read, process, and write lists in Workato recipes, including how
  list datapills appear in the datatree and ways to map them.
---

# Lists

Workato enables you to read, process, and write lists across applications. You can work with list items individually or in batches.

This guide explains how to manage lists in Workato recipes. It covers how list data appears in your recipe's datatree, different ways to map and process list datapills, and tips for common use cases.

## List datapills

List datapills appear in the datatree with a lines icon:

![List datatree icon](/assets/list-datatree-icon.TO5jBk1j.png)_List icon in the datatree_

### Map list datapills using formula mode

Some input fields, such as those that expect a string or number, may not allow you to select list datapills in text mode. In these cases, switch the field to [formula mode](/en/formulas/formula-mode) to map list datapills.

![Mapping list datapills in formula mode](/assets/list-datapills-formula-mode.BlIrRMyz.gif)_Mapping list datapills in formula mode_

## How to use list datapills

You can map list datapills into actions using the following methods:

- [Direct use without list processing](#direct-use-without-list-processing)
- [Actions that accept list inputs](#list-batch-action)
- [Using the repeat step for explicit list processing](#list-repeat-action)

> **USING A SAMPLE CSV**
> 
> This section uses a sample CSV file with gardening supply inventory to demonstrate list behaviors in recipes. The file is read using a **New CSV file in folder** trigger and parsed into a list of three lines.
> 
> **View sample CSV**
> 
> ```csv
> Manufacturer,Model,Category,Item Name,Item Code,Description,Unit Cost,Unit Price,Taxable,Tax,Material,Color,Dimensions
> Sierra Gardening,MS-321,Gardening supplies,Pine wood potting bench,MS-321,Pine wood potting bench with durable construction and a stylish finish.,74.5,119.99,Yes,0.0875,Pine,White,30 inches
> Sierra Gardening,MS-322,Gardening supplies,Cherry wood potting bench,MS-322,Cherry wood potting bench with durable construction and a stylish finish.,74.5,119.99,Yes,0.0875,Cherry,Natural,30 inches
> Sierra Gardening,MS-323,Gardening supplies,Cedar wood potting bench,MS-323,Cedar wood potting bench with durable construction and a stylish finish.,74.5,119.99,Yes,0.0875,Cedar,Black,30 inches
> ```
> 
> You can upload this file to your Box folder to try out the examples in this guide.

### Direct use without list processing

Mapping datapills directly from a list uses only the first item.

For example, when you map a list datapill directly into the **Log message** action without list processing, the action retrieves only the first line from the CSV file.

![Example recipe using list datapills directly](/assets/example-recipe-using-list-pills-directly.CtI4yohF.png)_Recipe using list datapills directly in a Log message action. [Example recipe](https://www.workato.com/recipes/487919)_

In the job details page, the trigger output displays all three lines within the CSV file.

![CSV trigger output](/assets/csv-trigger-output.3nVOl7TU.png)_Trigger output details displaying lines within the CSV file_

However, the **Log message** output only displays the first line:

![Log message result](/assets/log-message-result.CkEkpZ6w.png)_Log message input displaying only the first line of data_

### Actions that accept list inputs

Some actions accept lists as input, including Salesforce bulk insert and update, journal entry creation in accounting apps, and sales order creation in ERP apps.

The following example imports new products from a Box CSV file into Salesforce using the **Bulk insert** action:

![Example recipe using list input](/assets/example-recipe-using-input-list.DTHxeX_g.png)_Example recipe using list input. [Example recipe](https://www.workato.com/recipes/549955)_

These actions include a **Source list** field that accepts only list datapills. When this input is selected, you can only select list datapills from the datatree. Map a list datapill, such as Rows, to this field.

The action processes the entire list. In this example, the three inventory items from the Box CSV file are created as Salesforce products.

The job output confirms the three products were created:

![Salesforce bulk insert via input list](/assets/job-output-sf-bulk-insert.HMCgS8fd.png)_Salesforce bulk insert via list input_

### Using the repeat step for explicit list processing

If an action doesn't support list input, you can use a **Repeat** step to run the action for each item in the list.

![Example recipe using repeat step](/assets/example-recipe-using-repeat-step.RJM2jJiU.png)_Recipe using repeat step to iterate through NetSuite list of inventory items. [Example recipe](https://www.workato.com/recipes/487921)_

To iterate through the **Rows** list, pass the Rows list datapill as input for the repeat step. The recipe runs the **Add inventory item** action three times, once for each CSV line.

![Repeat step input list](/assets/repeat-step-input-list.XfXJ8QiS.png)_Provide the list datapill as input for repeat step_

When using the Repeat step, the important thing to note is to retrieve datapills from the For each datatree.

![Mapping from foreach datatree](/assets/mapping-from-foreach-datatree.C-LkDhgv.png)_Mapping datapills from the Foreach datatree_

This ensures each **Add inventory item** step uses the next line in the CSV.

#### Common mistake when using the repeat step

Mapping datapills directly from the list datapill instead of from the **Repeat** step causes every iteration to use the first item's data. This results in duplicate records.

![Recipe with direct mapping from list](/assets/recipe-with-wrong-direct-mapping.BD50IeLP.png)_Example of a recipe with INCORRECT (direct) mapping from list instead of from the Repeat step. [Example recipe](https://www.workato.com/recipes/488273)_

## Manage lists with Variables by Workato

The [Variables by Workato](/en/features/variables) supports advanced list management using variables with custom schemas. You can create a list, define its structure, and dynamically add or clear items in recipes.

Supported list actions include:

- [Create list](/en/features/variables#create-list)
- [Add item to list](/en/features/variables#add-item-to-list)
- [Add item to list (batch)](/en/features/variables#add-item-to-list-batch)
- [Clear all items from list](/en/features/variables#clear-all-items-from-list)

> **LISTS BY WORKATO DEPRECATION NOTICE**
> 
> Workato has deprecated the [Lists by Workato](/en/features/lists-by-workato) connector. Although we continue to provide runtime support for active recipes using this connector, creating new recipes with it is no longer possible. Additionally, we will no longer fix bugs or enhance this connector in the future.
> 
> We recommend that you transition to the [Variables by Workato](/en/features/variables) connector, which offers enhanced list management with support for custom schemas and more dynamic control over list items. For fixed count loops, use **Repeat while** loops with the Index datapill to control loop execution.
> 
> Refer to [Lists by Workato](/en/features/lists-by-workato) for reference.

## Clear step output

You can configure the **Clear step output** field when using the **Repeat action** to repeat a step in your recipe.

![Clear step output field](/assets/clear-step-output.CR2Na0mS.png) _Clear step output field_

The **Clear step output** field is set to **No** by default. If you don't clear the step output when the condition is satisfied on the first iteration, the variable retains the value from the first iteration **even if later iterations don't satisfy the condition**. We recommend you change the **Clear step output** field value to **Yes** if you plan to:

- Use datapills from previous steps inside the loop that is nested in the condition.
  
- Use the result from the most recent iteration, which may differ from the result of your first iteration.
  

Consider the following example to determine how to set the **Clear step output** field in your recipe:

- Create a list of orders.
- For each order in the list:
  - If the order amount exceeds $1000:
    - Calculate the discount for the order.
  - If you apply a discount:
    - Update the variable `total_discount` with the discount amount.

If you keep the default **No** setting for **Clear step output**, and if the condition is satisfied in the first iteration, the `total_discount` variable retains the value from the first iteration.

**First iteration**:

- Order amount is $1500.
  - Workato calculates a discount of $150.
    - `total_discount` updates to $150.

**Second iteration**:

- Order amount is $1200.
  - Workato calculates a discount of $120.
    - `total_discount` **incorrectly** remains at $150.

In this scenario, the `total_discount` is inaccurate on the second iteration, retaining the value `$150` from the first iteration instead of applying the new discount amount of `$120`.

However, if you set **Clear step output** to **Yes**:

**First iteration**:

- Order amount is $1500.
  - Workato calculates a discount of $150.
    - `total_discount` updates to $150.

**Second iteration**:

- Order amount is $1200.
  - Workato calculates a discount of $120.
    - `total_discount` updates to $120.

---
