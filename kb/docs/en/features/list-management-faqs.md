---
url: 'https://docs.workato.com/en/features/list-management-faqs.md'
description: >-
  Answers to common questions about working with lists in Workato, including
  mapping list datapills, processing batches, and reading CSV files.
---

# Lists FAQs

Get answers to frequently asked questions (FAQs) about working with lists in Workato.

Why can't I select or map a list datapill into an input field?

Some input fields don't allow you to select list datapills directly from the datatree. To map a list datapill into these fields, switch the input to [formula mode](/en/formulas/formula-mode). Formula mode lets you reference lists and objects that aren't selectable in text mode.

![Mapping list datapills in formula mode](/assets/list-datapills-formula-mode.BlIrRMyz.gif)_Mapping list datapills in formula mode_

How are lists used in integrations with Workato?

Lists, also called arrays, let you handle structured data across applications. For example, you may need to process a list of order line items, contacts, or products in a recipe. Workato provides tools to manipulate individual list items or process entire batches.

How do I set up a recipe that reads a list from a CSV file?

You can use the **New CSV file in folder** trigger from the Box connector to read a CSV file and parse it into a list of rows. Column headers become variables you can use in your recipe. Refer to [How to use list datapills](/en/features/list-management#how-to-use-list-datapills) for an example with a sample file.

What are the ways to map list datapills into actions?

You can map list datapills into actions in three ways:

- Use the datapill directly in an action without list processing. This method only uses the first item in the list.
- Use an action that accepts a list as input, such as Salesforce bulk insert.
- Add a **Repeat** step to loop through the list and process each item.

Learn more in [How to use list datapills](/en/features/list-management#how-to-use-list-datapills).

Why does only the first item get used when I map a list datapill directly?

When you map a list datapill into an action that doesn't support list input, the action only uses the first item. To process all items, use a **Repeat** step or an action that accepts list input. Refer to [Direct use without list processing](/en/features/list-management#direct-use-without-list-processing) for more information.

Which actions support list input?

Some actions, like Salesforce bulk insert or NetSuite batch actions, contain a **Source list** input that accepts list datapills. These actions automatically process the entire list. Refer to [Actions that accept list inputs](/en/features/list-management#list-batch-action) for more information.

When should I use a Repeat step?

Use a **Repeat** step when an action doesn't support list input. The **Repeat** step loops through each item in the list so you can process them one at a time. Refer to [Using the repeat step for explicit list processing](/en/features/list-management#list-repeat-action) for more information.

How can I avoid incorrect values when using a Repeat step?

If you use variables inside a loop, set **Clear step output** to **Yes**. Otherwise, values from earlier iterations may persist unexpectedly. See [Clear step output](/en/features/list-management#clear-step-output) for guidance.

How can I manage lists using the Variables by Workato connector?

The [Variables by Workato](/en/features/variables) connector supports advanced list operations, including the following actions:

- [Create list](/en/features/variables#create-list)
- [Add item to list](/en/features/variables#add-item-to-list)
- [Add item to list (batch)](/en/features/variables#add-item-to-list-batch)
- [Clear all items from list](/en/features/variables#clear-all-items-from-list)

This is the recommended approach for managing lists in new recipes.

Why can't I find the Lists by Workato connector when building a recipe?

The **Lists by Workato** connector is deprecated. You can no longer select it when building new recipes, and it won't receive bug fixes or improvements.

Existing recipes using this connector still work, but we recommend migrating to the [Variables by Workato](/en/features/variables) connector for improved list management and long-term support.

Refer to [Lists by Workato](/en/features/lists-by-workato) for the deprecated connector documentation.

---
