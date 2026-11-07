---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/crm-app.md'
description: >-
  Build a Workflow app that uses Run recipe actions to view, create, update, and
  delete CRM accounts in Salesforce.
---

# Example use case: CRM app

This example demonstrates how to use **Run recipe** actions to create a front-end app for a third-party application, such as a CRM, and uses Salesforce as an example.

![Front-end CRM app](/assets/crm-app.BlAOJz9_.png)_Front-end app for Salesforce powered by **Run recipe** actions_

In this example, the end-users of the application are business users who need limited access to Salesforce. This app must deliver the following functionality:

- Provide a high-level overview of accounts
- Provide a detailed look into an account users specify
- Enable users to create, update, and delete accounts

The following table describes the recipes we plan to create to accomplish these goals:

| Recipe name and action | Description |
| --- | --- |
| On page load | Surface high-level data about all accounts from Salesforce and surfaces it in the application read-only mode on page load. |
| Get data for drop-down (accounts) | Get a list of accounts from Salesforce and surface them as options in a single-select drop-down component. |
| Get account details | Get detailed information about a specific account in Salesforce and surface it in the application. |
| Create/update/delete account | Create, update, or delete an account in Salesforce, depending on user input. |
| Update an opportunity | Update an opportunity in Salesforce based on user input. |

> **EXAMPLE USE CASE**
> 
> This guide uses a sales lead processing use case and is intended to serve as an example. Recipe modifications, such as trigger, action, and conditional logic configuration, may require additional customizations to suit your specific requirements.

## Prerequisites

You must have the following to complete the instructions in this guide:

- [A Salesforce connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato)
- Workflow apps with the [Run recipe](/en/workflow-apps/component-actions/run-recipe) and [Reset/reload components](/en/workflow-apps/component-actions/reset-components) actions enabled

## Action: On page load

To collect high-level information about Salesforce accounts, you must build a recipe that retrieves data from Salesforce and configure page components to surface the data in the Workflow app.

This involves the following steps:

1. [Enable action on page load](#action-enable)
2. [Configure a recipe to fetch data from Salesforce](#recipe-configure)
3. [Surface recipe data in page components](#output-surface)

### Enable action on page load

Complete the following steps to enable action on page load:

1. Go to the page editor.
   
2. Click the page canvas.
   
3. Go to the **Action** panel.
   
4. Use the **Action** drop-down menu to select `Run recipe`.
   
5. Use the **Recipe** drop-down menu to select **Create recipe**. This opens the **Set up your recipe** page in a new tab.
   

### Configure a recipe to fetch data from Salesforce

Customizing this recipe consists of modifying the trigger, adding additional recipe steps, and modifying the **Return data to component** action.

Complete the following steps to set up your recipe:

1. Go to the **Name** field and enter `Page load` as the recipe name.
   
2. Use the **Location** drop-down menu to ensure the recipe is in the same folder as your app page.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the New component or drop-down event trigger
   
   Complete the following steps to modify the trigger:
   
   1. Select the **New component or drop-down event** trigger.
      
   2. Go to the **Setup** tab.
      
   3. Go to **Output parameters** and click **\+ Add field**.
      
   4. Go to the **Name** field and provide a unique name for this parameter, such as `totalAccounts`.
      
   5. Go to the **Label** field and provide a unique name for this field, such as `Total accounts`.
      
   6. Go to the **Data type** field and select **Integer**.
      
   7. Go to the **Optional** field and select `No`. When `No`, this field is required.
      
   8. Optional. Go to the **Hint** field and provide a hint to help users fill out this field.
      
      Your configuration should look as follows:
      
      ![Configure output schema](/assets/output-schema.BkxGWCNI.png)_Configure the output schema_
      
   9. Create the following additional output fields:
      
      | Name | Label | Data type | Optional |
      | --- | --- | --- | --- |
      | TotalArr | Total arr | Number | No |
      | NewOpps | Total opps | Integer | No |
      | ChurnedAccs | Churned accounts | Integer | No |
      
   10. Click **Save**.
       
   
5. Configure a Search for records using SOQL query in Salesforce (Batch) action.
   
   _This action fetches the total number of accounts and populates the_ `totalAccounts` _output field._
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Search for and select **Salesforce** as your app.
      
   3. Select the **Search for records using SOQL query in Salesforce (Batch)** action.
      
   4. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   6. Go to the **SOQL query** field and type `SELECT COUNT() FROM Account`.
      
   7. Go to the **Output schema** field and click **Use SOQL**.
      
   8. Type the same SOQL query as above, `SELECT COUNT() FROM Account`.
      
   9. Click **Next** and **Generate schema**. Workato generates the output schema by default.
      
   
   Your configuration should look as follows:
   
   ![Search records using SOQL query](/assets/page-load-search-accounts.DwdBI_Dp.png)_Search for records using SOQL query in Salesforce action_
   
6. Configure a Search Opportunities using SOQL query WHERE clause in Salesforce (Batch) action.
   
   _This action fetches new opportunities and populates the_ `newOpps` _output field._
   
   1. Click **+** and select **Action in an app**.
      
   2. Search for and select **Salesforce** as your app.
      
   3. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   4. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   5. Select the **Search records using SOQL query WHERE clause (Batch)** action.
      
   6. Use the **Search for** drop-down menu to select `Opportunity`.
      
   7. Go to the **SOQL WHERE clause** field and type `CreatedDate = THIS_WEEK`.
      
   8. Use the **Fields to retrieve** drop-down menu to select `Opportunity ID`, `Name`, and `Created date`.
      
   
   Your configuration should look as follows:
   
   ![Search records using SOQL query](/assets/page-load-search-opps.lAIAmDb4.png)_Search Opportunities SOQL query WHERE clause action configuration_
   
7. Configure a Search Accounts using SOQL query WHERE clause in Salesforce (Batch) action
   
   _This action fetches the ARR from all accounts in Salesforce and its output populates the totalARR output field._
   
   1. Click **+** and select **Action in an app**.
      
   2. Search for and select **Salesforce** as your app.
      
   3. Select the **Search records using SOQL query WHERE clause (Batch)** action.
      
   4. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   6. Use the **Search for** drop-down menu to select `Account`.
      
   7. Go to the **SOQL WHERE clause** field and type `IsDeleted = false` .
      
   8. Use the **Fields to retrieve** drop-down menu to select `Annual revenue`, and `Account name`.
      
   
   Your configuration should look as follows:
   
   ![Search records using SOQL query WHERE clause](/assets/page-load-search-accounts-2.MvTSQDIu.png)_Search accounts using SOQL query WHERE clause action_
   
8. Create a variable
   
   _This action aggregates the total ARR from all accounts in Salesforce._
   
   1. Click **+** and select **Action in an app**.
      
   2. Search for and select **Variables by Workato** as your app.
      
   3. Select the **Create variable** action.
      
   4. Click **\+ Add variable** and click **Formula** to use formula mode to create your variable.
      
   5. Map in the Accounts (Step 4) datapill and type `.pluck("AnnualRevenue").compact.sum`.
      
   
   Your configuration should look as follows:
   
   ![Create variable action](/assets/recipe-variable-create.CXdA0GXs.png)_Create a variable to find the total ARR_
   
9. Configure a Search Accounts using SOQL query WHERE clause in Salesforce (Batch) action
   
   _This action fetches the total number of inactive accounts from Salesforce and populates the_ `churnedAccs` _output field._
   
   1. Click **+** and select **Action in an app**.
      
   2. Search for and select **Salesforce** as your app.
      
   3. Select the **Search records using SOQL query WHERE clause (Batch)** action.
      
   4. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   6. Use the **Search for** drop-down menu to select `Account`.
      
   7. Go to the **SOQL WHERE clause** field and type `Active__c = 'No'` .
      
   8. Use the **Fields to retrieve** drop-down menu to select `Account name`.
      
   
10. Modify the Return data to component action
    
    1. Select the **Return data to component** action.
       
    2. Go to the **Consider action as successful** field and select `Yes`.
       
    3. Go to the **Output** section and map datapills to the following fields:
       
       | Output field name | Datapill |
       | --- | --- |
       | Total accounts | Total size (Step 2) |
       | Total opps | List size (Step 3) |
       | Total arr | totalArr (Step 5) |
       | Churned accounts | List size (Step 6) |
       
       Your configuration should look as follows:
       
       ![Configure return to component action](/assets/page-load-output.DxM3FOKV.png)_Return values fetched from Salesforce to your page_
       
    4. Optional. Go to the **Successful toast message** field and provide a custom success message.
       
    
11. Click **Save** and **Exit**.
    
12. Click **Start recipe**.
    

Your completed recipe should look as follows:

![Completed recipe](/assets/page-load-recipe-complete.CP8nvseF.png)_Completed recipe_

### Surface recipe output in page components

Surfacing recipe data in your app involves creating variables, setting variable values, and mapping variables into page components.

Complete the following steps to surface recipe data in page components using the page editor:

1. Create variables
   
   Complete the following steps to create and configure the variables required to surface high-level account data in your app. These variables correspond to the output schema defined in the **Page load** recipe created in the previous step.
   
   1. Click the page canvas.
      
   2. Go to the **Design** panel.
      
   3. Click **\+ Add variable**.
      
   4. Go to the **Name** field and type a unique name for your variable, such as **ActiveAccounts**. This variable represents the total number of active accounts in Salesforce.
      
   5. Go to the **Data type** menu and select **integer** as the data type.
      
   6. Optional. Go to the **Default value** field and provide a default value for your variable, such as <null>.
      
   7. Click **Done**.
      
      Your configuration should look as follows:
      
      ![Variable details](/assets/page-load-variable-details.DF8ficaW.png)_Variable details_
      
   8. Create the following additional variables:
      
      | Name | Data type | Description |
      | --- | --- | --- |
      | TotalArr | Number | Total ARR for all accounts. |
      | NewOpps | Integer | Number of new opportunities across all accounts. |
      | ChurnedAccs | Integer | Total number of churned accounts. |
      
      **_Note: All variables must match the data type specified in the output schema of the corresponding recipe._**
      
   
2. Use recipe output to set variable values
   
   1. Click the page canvas.
      
   2. Go to the **Action** panel.
      
   3. Go to the **Recipe output to set value** section and use the **Recipe output** drop-down menu to select `Total accounts`.
      
   4. Use the **Set Value for** field to select the `totalAccounts` variable.
      
   5. Click **\+ Add item** and map the following recipe outputs and variables:
      
      | **Recipe output to set value field** | **Set value for field** |
      | --- | --- |
      | Total opps | newOpps |
      | Total arr | totalArr |
      | Churned accounts | churnedAccs |
      
   
3. Map variables into page components
   
   This example has separate **Text block** components to hold each variable, which are located in the account overview section of our app.
   
   Complete the following steps to map variables into page components:
   
   1. Click a text block component to select it.
      
   2. Go to the **Text field** and click it. The **Page data** modal appears.
      
   3. Go to **Variables** and select `totalAccounts`.
      
   4. Add a label to help identify your variable, such as `Active accounts`.
      
   5. Apply styling, such as Markdown and color, as appropriate.
      
      Your configuration should look as follows:
      
      ![Map variables](/assets/page-load-variable-map.BncWmzvy.png)_Map variables into page components_
      
   6. Repeat this process for all remaining variables.
      
   
4. Click **Save**.
   

## Action: Get data for drop-down (accounts)

This part of the setup involves building a recipe to fetch data from Salesforce and configuring page components to display that data in your app. It populates a drop-down component with a list of accounts from Salesforce, which users can select. Refer to our [Drop-downs with recipe data source](/en/workflow-apps/dropdown-recipe-data-source#how-to) documentation to learn how to enable this functionality in your app.

## Action: Get account details

1. [Enable action on drop-down menu selection](#action-selection-enable)
2. [Configure a recipe to fetch data from Salesforce](#recipe-account-configure)
3. [Surface recipe data in page components](#account-details-page-component-configure)

### Enable action on drop-down menu selection

Complete the following steps to enable action when users select an option from a drop-down menu:

1. Go to the page editor.
   
2. Click the **Select an account** drop-down component.
   
3. Go to the **Action** panel.
   
4. Use the **Action** drop-down menu to select `Run recipe`.
   
5. Use the **Recipe** drop-down menu to select **Create recipe**. This opens the **Set up your recipe** page in a new tab.
   

### Configure a recipe to fetch data about a specific account from Salesforce

Customizing this recipe consists of modifying the trigger, adding additional recipe steps, and modifying the **Return data to component** action.

Complete the following steps to set up your recipe:

1. Go to the **Name** field and enter `Get account details` as the recipe name.
   
2. Use the **Location** drop-down menu to ensure the recipe is in the same folder as your app page.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the trigger
   
   1. Select the **New component or drop-down event** trigger.
      
   2. Go to the **Setup** tab.
      
   3. Go to **Input parameters** and click **\+ Add field**.
      
   4. Go to the **Name** field and provide a unique name for this parameter, such as `account_id`.
      
   5. Go to the **Label** field and provide a unique name for this parameter, such as `Account ID`.
      
   6. Go to the **Data type** field and select **String**.
      
   7. Go to the **Optional** field and select `Yes`.
      
   8. Optional. Go to the **Hint** field and provide a hint to help users fill out this field.
      
      ![Configure an input parameter](/assets/account-details-input-parameter.C3BWTzCD.png)_Configure an input parameter_
      
   9. Go to **Output parameters** and click **\+ Add field**.
      
   10. Go to the **Name** field and provide a unique name for this parameter, such as `arr`.
       
   11. Go to the **Label** field and provide a unique name for this field, such as `Arr`.
       
   12. Go to the **Data type** field and select **Number**.
       
   13. Go to the **Optional** field and select `No`. When `No`, this field is required.
       
   
   Your configuration should look as follows:
   
   ![Configure an output parameter](/assets/account-details-output-parameter.DEQgZJ1g.png)_Configure an output parameter_
   
5. Configure a Get details of a specific Account in Salesforce action
   
   _This action fetches the ARR for a specific account in Salesforce and populates the_ `arr` _output field. You can modify it to get additional account details to surface in your app._
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Search for and select **Salesforce** as your app.
      
   3. Select the **Get details of specific Account in Salesforce** action.
      
   4. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   6. Use the **Object** drop-down menu to select `Account`.
      
   7. Map the Account ID (Step 1) datapill into the **Object ID** field.
      
   
   Your configuration should look as follows:
   
   ![Get details of a specific Account in Salesforce action](/assets/account-details-get.Cq75dy8X.png)_Get details of a specific Account in Salesforce action_
   
6. Modify the Return data to component action
   
   1. Select the **Return data to component** action.
      
   2. Go to the **Consider action as successful** field and select `Yes`.
      
   3. Go to the **Output** section and map the Annual Revenue (Step 2) datapill to the **Arr** field.
      
   4. Optional. Type a custom toast message into the **Successful toast message** field.
      
   
   Your configuration should look as follows:
   
   ![Configure a return data to component action](/assets/account-details-output.BVo5-82v.png)_Configure the **Return data to component** action_
   
7. Click **Save** and **Exit**.
   
8. Click **Start recipe**.
   

Your completed recipe should look as follows:

![Completed recipe](/assets/account-details-recipe-complete.QABmicTZ.png)_Completed recipe_

### Surface recipe output in page components

Surfacing recipe data in your app involves creating variables, setting variable values, and mapping variables into page components.

Complete the following steps to surface recipe data in page components using the page editor:

1. Create variables in the page editor
   
   Complete the following steps to create and configure the variable required to surface the ARR for a specific account in your app. This variable corresponds to the output field defined in the **Get account details** recipe created in the previous step and must have the same data type.
   
   1. Click the page canvas.
      
   2. Go to the **Design** panel.
      
   3. Click **\+ Add variable**.
      
   4. Go to the **Name** field and type a unique name for your variable, such as **arr**. This variable represents the ARR for a specific account in Salesforce.
      
   5. Go to the **Data type** menu and select **number** as the data type.
      
   6. Optional. Go to the **Default value** field and provide a default value for your variable, such as <null>.
      
   7. Click **Done**.
      
   
   Your configuration should look as follows:
   
   ![Configure a variable](/assets/account-details-recipe-variable.DA-msftC.png)_Configure a variable_
   
2. Configure recipe input parameters and use recipe output to set variable values
   
   1. Click the page canvas.
      
   2. Go to the **Action** panel.
      
   3. Go to the **Recipe input parameters** section and use the **Account ID** drop-down menu to select the Selected value (Select an account) datapill.
      
   4. Click the page canvas.
      
   5. Go to the **Action** panel.
      
   6. Go to the **Recipe output to set value** section.
      
   7. Use the **Recipe output** drop-down menu to select `Arr`.
      
   8. Use the **Set value for** drop-down menu to select `arr`.
      
   
   Your configuration should look as follows:
   
   ![Recipe input and output configuration](/assets/account-details-recipe-input-config.DDg3VBP7.png)_Recipe input and output configuration_
   
3. Map variables into page components
   
   This example is configured with a **Text block** component to hold the variable, which is located in the **Manage accounts** section of the app.
   
   Complete the following steps to map a variable into a page component:
   
   1. Click a text block component to select it.
      
   2. Go to the **Text field** and click it. The **Page data** modal appears.
      
   3. Go to **Variables** and select `arr`.
      
   4. Add a label to help identify your variable, such as `ARR`.
      
   5. Apply styling, such as Markdown and color, as appropriate.
      
   
   Your configuration should look as follows:
   
   ![Map the ARR variable](/assets/account-details-variable-map.BzazI-Vt.png)_Map the ARR variable_
   
4. Click **Save**.
   

## Action: Create, update, or delete an account

This portion of the app enables users to create, update, or delete an account in Salesforce.

This consists of the following steps:

1. [Enable action on button click](#button-action)
2. [Configure a recipe to create, update, or delete an account](#crud-configure)
3. [Surface recipe output in page components](#page-component-configure)

### Enable action on button click

The Manage CRM application page is configured with the following buttons, which enable users to perform actions in Salesforce:

- Update account
- Delete account
- Create account

![Buttons for updating, deleting, and creating an account](/assets/crud-portal.BXsh_BBV.png)_Buttons for updating, deleting, and creating an account_

Complete the following steps to enable action when users click a button:

1. Go to the page editor.
   
2. Click the **Update account** button.
   
3. Go to the **Action** panel.
   
4. Use the **Action** drop-down menu to select `Run recipe`.
   
5. Use the **Recipe** drop-down menu to select **Create recipe**. This opens the **Set up your recipe** page in a new tab.
   

### Configure a recipe to create, update, or delete an account

Customizing this recipe consists of modifying the trigger, adding additional actions, and returning data to your page components.

Complete the following steps to set up your recipe:

1. Go to the **Name** field and enter `Create, update, or delete account` as the recipe name.
   
2. Go to the **Location** drop-down menu and ensure the recipe is in the same folder as your app page.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the trigger
   
   Complete the following steps to modify the trigger:
   
   1. Select the **New component or drop-down event** trigger.
      
   2. Go to the **Setup** tab.
      
   3. Go to **Input parameters** and click **\+ Add field**.
      
   4. Go to the **Name** field and provide a unique name for this parameter, such as `action`.
      
   5. Go to the **Label** field and provide a unique name for this field, such as `Action`.
      
   6. Go to the **Data type** field and select **String**.
      
   7. Go to the **Optional** field and select `No`. When `No`, this field is required.
      
   8. Create the following additional input parameters:
      
      | Name | Label | Data type | Optional |
      | --- | --- | --- | --- |
      | accountID | Account ID | String | Yes |
      | accountName | Account name | String | Yes |
      | arr | ARR | Number | Yes |
      | details | Details | string | Yes |
      
   9. Go to **Output parameters** and click **\+ Add field**.
      
   10. Go to the **Name** field and provide a unique name for this parameter, `result`.
       
   11. Go to the **Label** field and provide a unique name for this field, such as `Result`.
       
   12. Go to the **Data type** field and select **String**.
       
   13. Go to the **Optional** field and select `No`. When `No`, this field is required.
       
   
   Your configuration should look as follows:
   
   ![Input and output parameter configuration](/assets/crud-input-parameters.Cqvpv8jV.png)_Input and output parameter configuration_
   
5. Configure conditional logic
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Click **Handle errors** to add a **Monitor** block to your recipe.
      
   3. Click **+** and select **IF condition**.
      
   4. Map the Action (Step 1) datapill into the **Data field** field.
      
   5. Use the **Condition** drop-down menu to select `equals`.
      
   6. Type `Delete` in the **Value** field.
      
   
6. Configure a Delete Account in Salesforce action
   
   1. Click **+** and select **Action in an app**.
      
   2. Search for and select **Salesforce** as your app.
      
   3. Select the **Delete Account in Salesforce** action.
      
   4. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   6. Use the **Object** drop-down menu to select `Account`.
      
   7. Map the Account ID (Step 1) datapill into the **Object ID** field.
      
   
   Your configuration should look as follows:
   
   ![Delete account in Salesforce action](/assets/crud-delete.C7odn7ui.png)_Delete an account in Salesforce action_
   
7. Configure conditional logic and an Update Account in Salesforce action
   
   1. Click **+** and select **ELSE IF Condition**.
      
   2. Map the Action (Step 1) datapill into the **Data field** field.
      
   3. Use the **Condition** drop-down menu to select `equals`.
      
   4. Type `Update` in the **Value** field.
      
   
8. Configure an Update account in Salesforce action
   
   1. Click **+** and select **Action in an app**.
      
   2. Search for and select **Salesforce** as your app.
      
   3. Select the **Update Account in Salesforce** action.
      
   4. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   6. Use the **Object** drop-down menu to select `Account`.
      
   7. Map the Account ID (Step 1) datapill into the **Object ID** field.
      
   8. Map the Details (Step 1) datapill into the **Account Description** field.
      
   9. Map the Account name (Step 1) datapill into the **Account Name** field.
      
   10. Map the ARR (Step 1) datapill into the **Annual Revenue** field.
       
   
   Your configuration should look as follows:
   
   ![Update account in Salesforce action](/assets/crud-update.CnuSzl76.png)_Update an account in Salesforce action_
   
9. Configure conditional logic and a Create Account in Salesforce action
   
   1. Click **+** and select **ELSE IF Condition**.
      
   2. Map the Action (Step 1) datapill into the **Data field** field.
      
   3. Use the **Condition** drop-down menu to select `equals`.
      
   4. Type `Create` in the **Value** field.
      
   
10. Configure a Create Account in Salesforce action
    
    1. Click **+** and select **Action in an app**.
       
    2. Search for and select **Salesforce** as your app.
       
    3. Select the **Create record** action.
       
    4. Select the connection type you plan to use for this action.
       
       ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
       
       - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
       - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
       
       **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
       
    5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
       
    6. Use the **Object** drop-down menu to select `Account`.
       
    7. Map the Account name (Step 1) datapill into the **Account Name** field.
       
    8. Map the Details (Step 1) datapill into the **Account Description** field.
       
    9. Map the ARR (Step 1) datapill into the **Annual Revenue** field.
       
    
    Your configuration should look as follows:
    
    ![Create account in Salesforce action](/assets/crud-create.CIWMMXky.png)_Create an account in Salesforce action_
    
11. Modify the Return data to component action and configure conditional logic
    
    This portion of the workflow sends either a successful toast message back to the application or an error message based on whether the action is executed successfully.
    
    1. Click **+** and select **ELSE**.
       
    2. Click **+** and select **Action in an app**.
       
    3. Search for and select **Workflow apps** as your app.
       
    4. Select the **Return data to component** action.
       
    5. Use the **Consider action as successful?** drop-down menu to select `No`.
       
    6. Type `Unsupported action` in the **Error message** field.
       
    7. Go to the **Error found?** section and click the **Do not retry** action. Use the **Retry actions in Monitor block** drop-down menu to select `Do not retry`.
       
    8. Click the **Select an app and action** step and search for and select **Workflow apps** as your app.
       
    9. Select the **Return data to component** action.
       
    10. Use the **Consider action as successful?** drop-down menu to select `No`.
        
    11. Type a custom error message in the **Error message** field, such as `Error occurred`.
        
    
12. Configure the Return data to component action
    
    1. Click the **Return data to component** action to select it.
       
    2. Use the **Consider action as successful?** drop-down menu to select `Yes`.
       
    3. Go to the **Output** section and type `Success!` in the **Result** field.
       
    4. Go to the **Successful toast message** field and map in the Action (Step 1) datapill.
       
    5. Type in `=== 'Delete' ? "Successfully deleted account" : "Done!"`
       
    
    Your configuration should look as follows:
    
    ![Configure the return data to component action](/assets/crud-output.BvkeM45j.png)_Configure the **Return data to component** action_
    
13. Click **Save** and **Exit**.
    
14. Click **Start recipe**.
    

Your completed recipe should look as follows:

![Completed recipe](/assets/crud-recipe-complete.Bg9SdUlA.png)_Complete recipe_

### Surface recipe output in page components

Surfacing recipe data in your app involves creating variables, setting variable values, and mapping variables into page components.

Complete the following steps to surface recipe data in page components using the page editor:

1. Configure the Update account button
   
   1. Select the **Update account** button.
      
   2. Go to the **Action** panel.
      
   3. Go to the **Recipe input parameters** section and set up input parameters for use in the **Create, update, or delete account** recipe created in the previous step.
      
   4. Type `Update` into the **Action** field.
      
   5. Map the Selected value (Select an account) page component datapill into the **Account ID** field.
      
   6. Map the Value (New account name) page component datapill into the **Account name** field.
      
   7. Map the Value (ARR) page component datapill into the **ARR** field.
      
   8. Map the Value (Details) page component datapill into the **Details** field.
      
   9. Leave the **Recipe output to set value** and **Follow up action** fields blank.
      
   
   Your configuration should look as follows:
   
   ![Update account button configuration](/assets/crud-update-button-config.CR4wnJnC.png)_Update account button configuration_
   
2. Configure the Delete account button
   
   1. Select the **Delete account** button.
      
   2. Go to the **Action** panel.
      
   3. Go to the **Recipe input parameters** section to set up input parameters for use in the **Create, update, or delete account** recipe created in the previous step.
      
   4. Type `Delete` into the **Action** field.
      
   5. Map the Selected value (Select an account) page component datapill into the **Account ID** field.
      
   6. Leave the **Recipe output to set value** and **Follow up action** fields blank.
      
   
   Your configuration should look as follows:
   
   ![Delete account button configuration](/assets/crud-delete-button-config.DoHn4Wlo.png)_Delete account button configuration_
   
3. Configure the Create account button
   
   1. Select the **Create account** button.
      
   2. Go to the **Action** panel.
      
   3. Go to the **Recipe input parameters** section to set up input parameters for use in the **Create, update, or delete account** recipe created in the previous step.
      
   4. Type `Create` into the **Action** field.
      
   5. Map the Value (Account name) page component datapill into the **Account name** field.
      
   6. Map the arr (Variable) page component datapill into the **ARR** field.
      
   7. Map the Value (Details) page component datapill into the **Details** field.
      
   8. Leave the **Recipe output to set value** and **Follow up action** fields blank.
      
   
   Your configuration should look as follows:
   
   ![Create account button configuration](/assets/crud-create-button-config.C9j-Jh3d.png)_Create account button configuration_
   
4. Click **Save**.
   

## Action: Update an opportunity

This portion of the app enables users to update an opportunity in Salesforce.

![Update an opportunity](/assets/table-portal.Dy_vcn-V.png)_Update an opportunity_

This consists of the following steps:

1. [Enable action on table row selection](#table-action)
2. [Configure a recipe to update an opportunity](#update-configure)
3. [Define input parameters and reload page components](#table-component-configure)

### Enable action on table row selection

The Manage CRM application page includes a table that lists all opportunities for the selected account.

Complete the following steps to enable action when users select a row in a table:

1. Go to the page editor.
   
2. Click the **Opportunities** table component.
   
3. Go to the **Action** panel.
   
4. Use the **Action** drop-down menu to select `Run recipe`.
   
5. Use the **Recipe** drop-down menu to select **Create recipe**. This opens the **Set up your recipe** page in a new tab.
   

### Configure a recipe to update an opportunity in Salesforce

Customizing this recipe consists of modifying the trigger, adding additional actions, and returning data to your page components.

Complete the following steps to set up your recipe:

1. Go to the **Name** field and enter `Update opportunity (on table row click)` as the recipe name.
   
2. Go to the **Location** drop-down menu and ensure the recipe is in the same folder as your app page.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the trigger
   
   Complete the following steps to modify the trigger:
   
   1. Select the **New component event** trigger.
      
   2. Go to the **Setup** tab.
      
   3. Go to **Input parameters** and click **\+ Add field**.
      
   4. Go to the **Name** field and provide a unique name for this parameter, such as `opp_id`.
      
   5. Go to the **Label** field and provide a unique name for this field, such as `Opportunity ID`.
      
   6. Go to the **Data type** field and select **String**.
      
   7. Go to the **Optional** field and select `No`. When `No`, this field is required.
      
   8. Create the following additional input parameters:
      
      | Name | Label | Data type | Optional |
      | --- | --- | --- | --- |
      | updated\_description | Updated description | String | Yes |
      | updated\_deal | Updated deal amount | Number | Yes |
      | updated\_stage | Updated stage | String | Yes |
      
   9. Go to **Output parameters** and click **\+ Add field**.
      
   10. Go to the **Name** field and provide a unique name for this parameter, such as `new_deal`.
       
   11. Go to the **Label** field and provide a unique name for this field, such as `New deal amount`.
       
   12. Go to the **Data type** field and select **Number**.
       
   13. Go to the **Optional** field and select `Yes`.
       
   14. Create the following additional output parameters:
       
       | Name | Label | Data type | Optional |
       | --- | --- | --- | --- |
       | new\_description | New description | String | Yes |
       | new\_stage | New stage | String | Yes |
       
   
   Your configuration should look as follows:
   
   ![Input and output parameter configuration](/assets/table-input-output-parameters.CkO7PXdq.png)_Input and output parameter configuration_
   
5. Configure conditional logic
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Click **Handle errors** to add a **Monitor** block to your recipe.
      
   3. Click **Select an app and action**.
      
   4. Search for and select **Salesforce** as your app.
      
   5. Select the **Update record in Salesforce** action.
      
   6. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   7. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   8. Use the **Object** drop-down menu to select `Opportunity`.
      
   9. Map the Opportunity ID (Step 1) datapill into the **Opportunity ID** field.
      
   10. Map the Updated deal (Step 1) datapill into the **Amount** field.
       
   11. Map the Updated description (Step 1) datapill into the **Description** field.
       
   12. Map the Updated stage (Step 1) datapill into the **Stage** field.
       
   
   Your configuration should look as follows:
   
   ![Delete account in Salesforce action](/assets/opportunity-update.kaGlo50R.png)_Update an opportunity in Salesforce action_
   
6. Modify the Return data to component action and configure error handling
   
   This portion of the workflow sends an error message to the application if the **Update opportunity in Salesforce** action fails.
   
   1. Go to the **Error found?** section and click the **Do not retry** action. Use the **Retry actions in Monitor block** drop-down menu to select `Do not retry`.
      
   2. Click **Select an app and action**.
      
   3. Search for and select **Workflow apps** as your app.
      
   4. Select the **Return data to component** action.
      
   5. Use the **Consider action as successful?** drop-down menu to select `No`.
      
   6. Type `Unable to update opportunity. Contact your portal admin to learn more.` in the **Error message** field.
      
   
7. Configure the Return data to component action
   
   1. Click the **Select an app and action** step and search for and select **Workflow apps** as your app.
      
   2. Select the **Return data to component** action in step 6.
      
   3. Use the **Consider action as successful?** drop-down menu to select `Yes`.
      
   
   Your configuration should look as follows:
   
   ![Configure the return data to component action](/assets/table-output.BmQ_U2-w.png)_Configure the **Return data to component** action_
   
8. Click **Save** and **Exit**.
   
9. Click **Start recipe**.
   

Your completed recipe should look as follows:

![Completed recipe](/assets/table-recipe-complete.c1KmFl9a.png)_Complete recipe_

### Define input parameters and reload page components

This part of the setup focuses on defining input parameters and setting up a follow-up action to reload page components. Since the table data is directly sourced from Salesforce, there is no need to map recipe outputs into page components or variables

Complete the following steps to reload page components using the page editor:

1. Configure recipe input parameters
   
   1. Select the **Opportunities** table.
      
   2. Go to the **Action** panel.
      
   3. Go to the **Recipe input parameters** section and map page data into the provided fields.
      
   4. Map the Opp ID (Opportunities table) into the **Opportunity ID** field.
      
   5. Map the Value (Updated description) into the **Updated description** field.
      
   6. Map the Value (Updated deal amount) into the **Updated deal amount** field.
      
   7. Map the Value (Updated stage) into the **Updated stage** field.
      
   
   You configuration should look as follows:
   
   ![Table row select configuration](/assets/table-config.of1o0VcV.png)_Table row selection configuration_
   
2. Reload the table component
   
   This step reloads the **Opportunities** table with updated user-provided data.
   
   1. Select the **Update opportunity** button.
      
   2. Go to the **Action** panel.
      
   3. Use the **Action** drop-down to select `Reset/reload components`.
      
   4. Use the **Components** field to select the component values to reload on button click, the `update opps` container and `Opportunities table`.
      
   5. Click **Save**.
      
   
   Your configuration should look as follows:
   
   ![Component reset](/assets/table-reset.boBVW9xn.png)_Reset table component_

---
