---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/variables.md'
description: >-
  Learn how variables store and reference recipe data in Workflow apps to build
  interactive experiences that respond to user actions.
---

# Variables

Variables are dynamic placeholders used to store, manipulate, and reference data as users interact with Workflow apps. They can be populated in real time with output from recipes and enable you to display and manage information from other applications directly within your Workflow app. This allows you to build interactive, data-driven experiences that respond instantly to user actions and live business data.

Using variables in your apps involves creating them in the page editor, populating them with recipe output, and mapping them into page components.

Variables support the following data types:

- String
- Number
- Integer
- Date
- Date and time
- Boolean

_All page components that accept text input also accept variables, with the exception of placeholder fields._

## Create a variable in the page editor

Complete the following steps to create and configure a variable:

1. Click the **Page**.
   
2. Go to the **Design** panel.
   
3. Click **\+ Add variable**.
   
4. Go to the **Name** field and type a unique name for your variable, such as **translated-text**.
   
5. Go to the **Data type** menu and select a data type.
   
6. Optional. Go to the **Default value** field and provide a default value for your variable, such as <null>.
   
7. Click **Done**.
   

Your configuration should look as follows:

![Create a variable](/assets/translate-variable-create.BMXKV-WQ.png)_Create a variable_

## Populate a variable using recipe output

Before you define a variable in the page editor, consider which event will trigger the recipe to run and return data to your variable. For example, you can trigger a **Run recipe** action based on a [button click](/en/workflow-apps/component-actions/button-click), [drop-down value change](/en/workflow-apps/component-actions/drop-down-change), [page load](/en/workflow-apps/component-actions/page-load), or when a [table row is selected](/en/workflow-apps/component-actions/row-selection).

Complete the following steps to define a variable using recipe output:

1. Go to the **Recipe output to set value > Recipe output** field and select **recipe-output-name**. This is the output field you defined in your recipe.
   
2. Go to the **Set value for** field and select **your-variable-name**.
   

Your configuration should look as follows:

![Recipe output configuration](/assets/translate-variable.CRbjdTzb.png)_Recipe output configuration_

## Delete a variable

Complete the following steps to delete a variable:

1. Click the **Page**.
   
2. Go to the **Design** panel.
   
3. Hover over the variable and click the **Delete** icon.
   
4. Click **Delete variable**.
   
   ![Delete a variable](/assets/variable-delete.2wD4laEr.png)_Delete a variable_

---
