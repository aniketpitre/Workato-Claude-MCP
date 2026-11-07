---
url: 'https://docs.workato.com/en/recipes/repeat-for-each.md'
description: >-
  Learn how the Repeat for each loop in Workato runs nested recipe actions once
  for every item in a list datapill.
---

# Repeat for each loop

A **Repeat for each** loop executes actions inside a block of steps for each item in a given list. The actions you select to repeat must use data output from the Repeat for each loop's datatree to ensure that every item in the list is processed. Actions nested under a Repeat for each block are carried out for all items in the list.

For example, a **Repeat for each** block allows you to create a loop that processes each item in a list of invoice line items.

**Repeat for each** is a type of [Repeat control statement](/en/recipes/steps#repeat-step).

To insert a Repeat for each loop into a recipe, click the **+** (plus) button in the recipe editor to add a new step and select **Repeat for each**.

![Select Repeat for each](/assets/repeat-for-each-block-add-step.kWmC0qrR.png) _Select Repeat for each_

Workato adds a block of steps to the recipe where you can configure the app and action to take for each item in a list.

![Repeat for each block](/assets/repeat-for-each-block.BJ-wjvx_.png) _Repeat for each block_

## Example: Repeat for each loop

The following example demonstrates how to use the Repeat for each loop to sync Salesforce accounts using the batch trigger to Zendesk as organizations.

![Repeat for each loop example scenario](/assets/foreach_example_scenario.BACP8mVA.png)_Use the Repeat for each loop to iterate through a list of Salesforce accounts. [Example recipe](https://www.workato.com/recipes/480695)_

In this example, the trigger returns a list of Salesforce accounts. Since Zendesk does not support batch actions, each Salesforce account must be added one at a time from Salesforce to Zendesk.

The list datapill must be passed into the Repeat for each block. When the input list field is selected, only list type datapills are usable in the datatree, as shown in the following image. List datapills can be identified through their stack icon.

![Map list datapill into the Repeat for each block](/assets/map-list-pill-into-repeat-step.YHVikose.png)_Mapping a list datapill into the Repeat for each block's input list field. [Example recipe](https://www.workato.com/recipes/480695)_

> **CLEAR STEP OUTPUT**
> 
> When using a **Repeat for each** loop, set **Clear step output** to **Yes** to process data from each iteration independently. This setting is crucial when using **IF** conditions within the loop because it prevents previous iterations from affecting the current one.
> 
> Refer to the [List management documentation](/en/features/list-management#clear-step-output) for more information.

Datapills from the Repeat for each output datatree must be mapped to ensure that values from each list item are used when the action is repeated. For example, if the trigger fetches two Salesforce accounts, using datapills from the Repeat for each datatree ensures that the **Create organization** action creates a Zendesk organization with the data from the first Salesforce account on its first iteration, then with the data from the second Salesforce account on its second iteration.

![Use datapills from the Repeat for each block](/assets/use-datapills-from-repeat-step.Vt9Ad_ru.png)_Use datapills from the Repeat for each block's datatree. This ensures values from the list being iterated through are used. [Example recipe](https://www.workato.com/recipes/480695)_

The following image displays the mapping from the Repeat for each datatree.

![Repeat for each step example](/assets/foreach_example.BWvE3or_.png)_Datapills are mapped from the Repeat for step's datatree. [Example recipe](https://www.workato.com/recipes/480695)_

For further Repeat for each loop examples and more information about list processing, refer to the [list management](/en/features/list-management) documentation.

## Repeat for each in batches

[Video](https://www.youtube.com/embed/zc0Roqa-7b0)

Occasionally, the rate at which an upstream app or system transmits the data is faster than the rate at which a downstream app or system can receive it. You can use the **Repeat for each in batches** feature to process data by configuring the batch size. Large data sets are automatically parsed into smaller batches for transfer. Each item in the data set is only processed once.

For example, you can use the Repeat for each in batches feature to [create a batch of Salesforce leads](/en/connectors/salesforce/batch-operations#create-records-in-batches) from a list of leads in a CSV.

### How to use

Complete the following steps to use the Repeat for each in batches feature:

1. Sign in to your Workato account.
   
2. Go to **Projects**.
   
3. Click **Create > Recipe** or press C+R to create a new recipe, or click an existing recipe and select **Edit recipe**.
   
4. Click the **+** (plus) button to add a new step.
   
5. Select **Repeat for each**.
   
   ![Select Repeat for each](/assets/repeat-for-each-block-add-step.kWmC0qrR.png) _Select Repeat for each_
   
   Workato adds a block of steps to the recipe and automatically selects the **Set up list to repeat steps for each item** step.
   
   ![Set up list to repeat steps for each item in the Repeat for each block](/assets/repeat-for-each-block-select-list.DoAT3uhi.png) _Set up list to repeat steps for each item in the Repeat for each block_
   
6. Enter an input list datapill in the **Input list** field.
   
   ![Input list](/assets/repeat_step_inputlist.Dhfpag9b.png) _Input list_
   
7. Select `Batch of items` from the **Repeat mode** drop-down menu.
   
   ![Repeat mode drop-down menu](/assets/repeat_step_invoke.qKcKhVgD.png) _Repeat mode drop-down menu_
   
8. Set the **Batch size** field. This defaults to `100` when the batch size is not specified or if the number specified is less than 1. Note that a datapill can also be entered as a batch size.
   
   ![Set batch size](/assets/repeat_step_batchsize.BEALxnYp.png) _Set batch size_
   
9. You can see this reflected in the **For each** statement with the **Batch** tag.
   
   ![Repeat for each loop batch size](/assets/repeat_step_loop.Ca48jKUd.png) _Repeat for each loop batch size_
   
   Refer to [an example recipe](https://www.workato.com/recipes/1106794?st=d3a7e3) for more information.

---
