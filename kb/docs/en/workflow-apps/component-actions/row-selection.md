---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/row-selection.md'
description: >-
  Configure a Run recipe action that retrieves or updates data in an external
  app when a user selects a table row in a Workflow app.
---

# Action on table row selection

The **Run recipe** action enables you to retrieve or modify data in a third-party application and return it to your Workflow app dynamically when a table row is selected in an app. This allows you to sync data between external systems and your Workflow app in real-time.

## Configure a Run recipe action on table row selection

Configuring a **Run recipe** action on table row selection involves the following steps:

1. [Enable action on table row selection](#action-enable)
2. [Configure a recipe to retrieve or modify data in an external app](#recipe-configure)
3. [Connect the recipe to page components](#output-surface)

## Enable action on table row selection

Complete the following steps to enable a **Recipe run** action on table row selection:

1. Create a new Workflow app or select an existing one.
   
2. Select a **table** component and go to the **Action** panel. The action's **Trigger** event is pre-selected as `Row is active`.
   
3. Use the **Action** drop-down menu to select `Run recipe`.
   
4. Use the **Recipe** drop-down menu to click **Create recipe**. This opens the **Set up your recipe** page in a new tab.
   
   ![Action setup](/assets/action-setup.CxgQ59nV.png)_Action on table row selection setup_
   

## Configure a recipe to retrieve or modify data in an external app

1. Enter a unique **Name** for this recipe.
   
2. Use the **Location** drop-down menu to ensure the recipe is in the same folder as your app page.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the New component event trigger
   
   Complete the following steps to modify the trigger:
   
   1. Select the **New component event** trigger.
      
   2. Go to the **Setup** tab.
      
      The setup tab displays recipe input and output parameters which can be used to receive data from and return data to your page.
      
   3. Go to **Input parameters** and click **Add input parameters**.
      
   4. Define the page data to use in your recipe. You must provide the **Name**, **Data type**, and **Optional** status for each input parameter. **Label** and **Hint** are optional.
      
      ![Configure input parameters](/assets/input-parameters-recipe.CyksOhTq.png)_Configure input parameters_
      
   5. Go to **Output schema** and click **Add field**.
      
   6. Define the recipe output you plan to return to your page. You must provide the **Name**, **Data type**, and **Optional** status for each output parameter. **Label** and **Hint** are optional.
      
      ![Configure output schema](/assets/output-schema-modal.h4Q0CG_x.png)_Configure the output schema_
      
   
5. Configure an action in an app
   
   Complete the following steps to configure one or more **Action in an app** steps to retrieve or modify data from an external system:
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Search for and select the app you plan to use. A list of available actions for the app displays.
      
   3. Select the action you plan to use.
      
   4. Select the connection type you plan to use for the component event recipe.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connections#create-connections).
      
   6. Configure the action based on your requirements.
      
   7. Map in input parameters to the action as necessary. For example, you can user input, such as an `Account name` to search for accounts in an external system and return relevant data to your page.
      
   8. Add additional steps as required.
      
   
6. Modify the Return data to component action
   
   Complete the following steps to return recipe data to your app:
   
   1. Select the **Return data to component** action.
      
   2. Use the **Consider this action as successful?** drop-down to define whether the action completed successfully.
      
   3. Go to the output section and map in recipe data to the provided output fields. This output matches the output fields defined in the **New component event** trigger.
      
      ![Return data to component](/assets/return-data.Ba2Wfv2X.png)_Return data to component_
      
   4. Click **Save** and **Exit**.
      
   

## Connect the recipe to page components

Complete the following steps to map page data into the recipe and surface recipe output back to page components:

1. Return to the page editor and select a **table** component.
   
2. Create and map a variable into a page component
   
   1. Go to the **Design** panel and select **\+ Add variable**.
      
   2. Enter the variable **Name**, **Data type**, and **Default value** as required. Variable data types must match the data type specified in the trigger output parameters. Refer to [Create a variable](/en/workflow-apps/component-actions/variables#create) for more information.
      
      ![Add variable](/assets/variable-generic.DjllmcJ4.png)_Add a variable_
      
   3. Create additional variables as required.
      
   4. Select a component where you plan to display the variable, such as a **text block**, and go to the **Content** panel.
      
   5. Use the **Page data** modal to map in a variable.
      
      ![Map a variable](/assets/variable-map-generic.DNXItnc6.png)_Map a variable_
      
   
3. Define recipe input parameters
   
   1. Select a **table** component.
      
   2. Go to the **Action** panel.
      
   3. Go to **Recipe input parameters**.
      
   4. Use the **Page data** modal to map in page component data. For example, you can map in user input, such as an `Account name` to use it to search for account data in an external system.
      
      ![Recipe input parameters](/assets/recipe-input-parameters.lEKNlS86.png)_Define recipe input parameters_
      
   
4. Use recipe output to set variable values
   
   1. Select a **table** component.
      
   2. Go to the **Action** panel.
      
   3. Go to **Recipe output to set value** and click **\+ Add item**.
      
   4. Use the **Recipe output** drop-down menu to select recipe output.
      
   5. Use the **Set value for** drop-down menu to select a page component or variable to set the value for. Refer to [Populate a variable using recipe output](/en/workflow-apps/component-actions/variables#populate) to for more information.
      
      ![Recipe output](/assets/output-generic.CxlgVCHK.png)_Populate variable values with recipe output_
      
   
5. Click **Save**.

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/component-actions/file-value-change.md
description: >-
  Configure a Run recipe action that retrieves or updates data in an external
  app when a user uploads or downloads a file in a Workflow app.
---

# Action on file download/upload

The **Run recipe** action retrieves, modifies, or saves data in a third-party application and returns data to your Workflow app when a file is uploaded or downloaded in your app, keeping external systems and your Workflow app in sync in real time.

The **Value changed** trigger works with the **Upload** and **Download** modes of the **file** component. Refer to the [File component properties](/en/workflow-apps/page-components#file) for more information.

## Configure a Run recipe action on file value change

Configuring a **Run recipe** action on file value change involves the following steps:

1. [Enable action on file value change](#action-enable)
2. [Configure a recipe to process the uploaded or downloaded file](#recipe-configure)
3. [Connect the recipe to page components](#output-surface)

### Enable action on file value change

Complete the following steps to enable a **Recipe run** action on file value change:

1. Create a new Workflow app or select an existing one.
   
2. Select a **file** component and go to the **Action** panel. The action's **Trigger** event is pre-selected as `Value changed`.
   
3. Use the **Action** drop-down menu to select `Run recipe`.
   
4. Use the **Recipe** drop-down menu to click **Create recipe**. This opens the **Set up your recipe** page in a new tab.
   
   ![Action setup](/assets/action-setup.CxgQ59nV.png)_Action on file value change setup_
   

### Configure a recipe to process the uploaded or downloaded file

1. Enter a unique **Name** for this recipe.
   
2. Use the **Location** drop-down menu to ensure the recipe is in the same folder as your app page.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the New component event trigger
   
   1. Select the **New component event** trigger.
      
   2. Go to the **Setup** tab.
      
      The setup tab displays the recipe's input and output parameters. Use them to receive data, such as files, from your page and return data back to it.
      
   3. Go to **Input parameters** and click **Add input parameters**.
      
   4. Define the file to pass to your recipe. You must provide the **Name**, **Data type**, and **Optional** status for each input parameter. You can also provide an optional **Label** and **Hint**.
      
      Select `File` as the **Data type** to pass a file uploaded to your app to the recipe.
      
      ![Configure input parameters](/assets/input-parameters-recipe.CyksOhTq.png)_Configure input parameters_
      
   5. Go to **Output schema** and click **Add field**.
      
   6. Define the recipe output if you plan to return data to your page. You must provide the **Name**, **Data type**, and **Optional** status for each output parameter. You can also provide an optional **Label** and **Hint**.
      
      Select `File` as the **Data type** to return a file to your app.
      
      ![Configure output schema](/assets/output-schema-modal.h4Q0CG_x.png)_Configure the output schema_
      
   
5. Configure an action in an app
   
   Complete the following steps to configure one or more **Action in an app** steps to process the uploaded file. For example, you can save it to a data table, upload it to FileStorage, or process it in your recipe.
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Search for and select the app you plan to use. A list of available actions for the app displays.
      
   3. Select the action you plan to use, such as a file upload, download, or attachment action in a document storage or content management system.
      
   4. Select the connection type you plan to use for the component event recipe.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connections#connection-basics).
      
   6. Configure the action based on your requirements.
      
   7. Map input parameters to the action as necessary. For example, map the File name (Step 1) or File contents (Step 1) datapills into the action's input fields to save or process the file.
      
   8. Add additional steps as required.
      
   
6. Modify the Return data to component action
   
   Complete the following steps to return recipe data to your app:
   
   1. Select the **Return data to component** action.
      
   2. Use the **Consider this action as successful?** drop-down to define whether the action completed successfully.
      
   3. Go to the output section and map in recipe data to the provided output fields. This output matches the output fields defined in the **New component event** trigger.
      
      ![Return data to component](/assets/return-data.Ba2Wfv2X.png)_Return data to component_
      
   4. Click **Save** and **Exit**.
      
   

### Connect the recipe to page components

Complete the following steps to map page data into the recipe and surface recipe output back to page components:

1. Return to the page editor and select a **file** component.
   
2. Define recipe input parameters
   
   1. Select a **file** component.
      
   2. Go to the **Action** panel.
      
   3. Go to **Recipe input parameters**.
      
   4. Use the **Page data** modal to map in `File` to process in your recipe.
      
      ![Recipe input parameters](/assets/recipe-input-parameters-file.CqN4IQIX.png)_Define recipe input parameters_
      
   
3. Use recipe output to set values
   
   1. Select a **file** component.
      
   2. Go to the **Action** panel.
      
   3. Go to **Recipe output to set value** and click **\+ Add item**.
      
   4. Use the **Recipe output** drop-down menu to select recipe output.
      
   5. Use the **Set value for** drop-down menu to select a page component or variable to set the value for.
      
      ![Recipe output](/assets/output-generic.CxlgVCHK.png)_Populate variable values with recipe output_
      
   
4. Click **Save**.

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/component-actions/reset-components.md
description: >-
  Configure Reset/reload components actions to clear or refresh page components
  in a Workflow app after users submit data.
---

# Reset/reload components

You can configure your page to reset or reload page components as required. For example, you can configure your application to clear all values after a user submits data so that the app can be used again.

## How it works

**Reset/reload components** actions can be configured to clear the entire page or only specific components. This action can be set up as a follow-up action for components configured with another primary action or as the primary action for button components.

The following diagram explains how follow-up actions work in conjunction with **Run recipe** actions.

```mermaid
flowchart TD
  subgraph M[" "]
    direction TB
    subgraph D[&nbsp Recipe &nbsp]
        direction LR
        x(Real-time<br>trigger runs) --> xx(Retrieves or updates<br>data in external systems)
        xx --> xxx(Returns data to<br>component)
    end
    subgraph R[&nbsp Workflow app &nbsp]
        direction LR
        a(Recipe output<br>populates components)
    end
  end
  A([UI event]) --> M --> B([App page updated])
  B --> C([Reset button clicked]) -.- E([Page component<br>values reset])
  D -.-> R

  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef WorkatoPink fill:#f3c1c2,stroke:#f3c1c2,stroke-width:1px;
  class x,xx,xxx,a,A,C WorkatoTeal
  class D,R SubgraphDash
  class B,E WorkatoPink
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class M SubgraphLight
```

## Compatible components

The following table describes reset/reload actions, trigger events, and compatible components:

| Component | Trigger event | Action description |
| --- | --- | --- |
| Page | Follow up action | Reset/reload components after a primary action completes. |
| Button | Button click (primary action), Follow up action | Configure a button to reset/reload components as its primary action or reset/reload components after another primary action completes. |
| Single-select and multi-select drop-down components | Follow up action | Reset/reload components after a primary action completes. |
| Table | Follow up action | Reset/reload components after a primary action completes. |
| File | Follow up action | Reset/reload components after a primary action completes. |

## Reset/reload components

Complete the following steps to configure a follow-up action that resets/reloads component values:

1. Select a component configured with a **Run recipe** action, such as a **drop-down**, **table**, or **button**.
   
2. Go to the **Action** panel.
   
3. Use the **Follow up action** drop-down to select `Reset/reload components`.
   
4. Use the **Components** field to select one or more component values to reset or reload.
   
   ![Reset/reload component](/assets/follow-up-generic.3OsaXm0y.png)_Reset/reload a component_
   
5. Click **Save**.

---
