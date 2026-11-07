---
url: 'https://docs.workato.com/en/features/fixed-dynamic-lists.md'
description: >-
  Learn how to use fixed and dynamic lists as action inputs in Workato recipes
  to iterate through list datapills or add items one by one.
---

# Fixed and dynamic lists

## Using list datapills in actions

Some actions will accept a list as input for example, Salesforce bulk insert and bulk update actions, create journal entry actions for accounting apps, create sales order actions for ERP apps.

Actions that take lists as inputs will have a input field called Source list, which will only take in list pills. List datapills are indicated with a stack of lines as an icon. When these list input fields are selected, the data tree will offer only list pills.

![Example input source list](/assets/example-recipe-using-input-list.DTHxeX_g.png)_**Lines** object is mapped into the Salesforce Contacts input source list_

When actions offer a list as input, the input modes allowed are `Fixed list` and `Dynamic list`. Select the input mode by clicking on the ellipsis icon.

![Dynamic or fixed](/assets/dynamiclist.7vC05t3c.png)_Select the input mode_

## Dynamic lists

Use the 'Dynamic list' option when you want the action to dynamically iterate through all items in a list, reading the values in every row. For example, if you have a CSV file with 10 rows, Dynamic list will iterate through all the rows, using the data in each row to create 10 new records in Salesforce.

When this option is selected, the first field to map is the 'Source list' field, which only accepts a list datapill. Using the list datapill will read directly from the source application's list of objects. Thereafter, map the fields below using the pills nested within the list pill.

In the example below, the source list comes from a CSV file uploaded into Dropbox and will create Salesforce Opportunity records in bulk using the data in each line of the CSV file. It will loop through all CSV rows and read the column values from each row, such as Product code, Product description etc. Thus, each line in the CSV file will provide data per Opportunity record created in Salesforce.

![Example input source list](/assets/example-recipe-using-input-list.DTHxeX_g.png)_Rows list object is mapped into the Salesforce products input source list_

## Fixed lists

In contrast, use the 'Fixed list' option when you want to input a list with a fixed number of items, without dynamically iterating through another list. In this case, each item is added one by one.

![Dynamic or fixed](/assets/fixedlist.B-8jU5LD.png)_Select the input mode_

Use this input mode if the total number of items in the list and their contents should be the same across recipe jobs. When this option is selected, you need to add and map each item in the list one by one.

You can use static values from [Environment Properties](/en/features/account-properties) or [Lookup tables](/en/features/lookup-tables) to fill in the fixed list.

![Entering static values in a fixed list](/assets/item-fixed.DMjoLXhV.png)_Entering static values in a fixed list_

---
