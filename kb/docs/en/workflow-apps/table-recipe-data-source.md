---
url: 'https://docs.workato.com/en/workflow-apps/table-recipe-data-source.md'
description: >-
  Learn how to use recipes as a data source for Workflow apps table components
  to dynamically populate tables with data from other apps.
---

# Tables with recipe data source

Workflow apps enable you to use [recipes](/en/workato-concepts#recipes) as a data source for [table components](/en/workflow-apps/page-components#view). This allows you to dynamically populate tables with data from your other applications. This ensures data consistency and reduces manual effort.

You can create new recipes directly from the [page editor](/en/workflow-apps/pages-customize).

![Table with recipe data source](/assets/apps-portal-get-data-table.DyrxiQbe.png)_Table component populated by recipe data_

## Use cases

The following use cases provide examples of how you can use this feature to address your business objectives.

### Customer support

- **Scenario**: A customer support workflow requires updating customer account information, which is dynamically populated based on data from a CRM system.
- **Solution**: A recipe retrieves a list of customer accounts from Salesforce in real-time, ensuring that the table reflects the most up-to-date data. The employee can then update the account using a Workflow apps page. Submitting the page triggers an additional recipe that updates the account in the CRM.

### Sales lead processing

- **Scenario**: Sales representatives must review accounts and related opportunities as part of a lead processing workflow. They require details about opportunities such as the name, description, and amount. Opportunities are stored in a CRM such as Salesforce and change frequently.
  
- **Solution**: A recipe fetches the latest opportunities for a specific account from Salesforce and returns them to your app page in table format.
  

### HR onboarding

- **Scenario**: An HR team needs to assign new hires to various departments, which are stored in a database and frequently updated.
  
- **Solution**: A recipe fetches the latest list of departments from the database whenever the page loads, ensuring the HR team sees the most current options.
  

## Limitations

This feature has the following limitations:

- Pages can have a maximum of one table that uses a recipe as its data source. If your page includes additional tables, they must be configured to use data tables as the data source.
- Table component recipes have a maximum run time of 10 seconds.
- Long-running actions are not supported in table component recipes.
- Runtime user connections are not supported in table component recipes.
- Public (anonymous) pages don’t support recipes as a data source for table components.

## How to set up recipes as a data source

Configuring recipes as a data source for table components consists of the following steps:

1. [Set up your recipe](#recipe-setup)
2. [Configure page components](#page-configure)

> **EXAMPLE USE CASE**
> 
> This guide uses a sales lead processing use case and is intended to serve as an example. Recipe modifications such as trigger and action configuration may require additional customizations to suit your specific requirements.

### Configure your recipe

Complete the following steps to set up this functionality in your Workflow app:

1. Sign in to Workato and create a Workflow app or select one of your existing Workflow apps.
   
2. Create a new page or edit an existing page.
   
3. Add a **Table** component to your page and select **Recipe** as the data source.
   
   ![Select recipe as the data source](/assets/get-data-for-table.Bq9jFda9.png)_Select recipe as the data source_
   
4. If existing recipes in your Workflow apps project contain the **New component event (Drop-down)** trigger, Workato displays them here. Otherwise, click **Create recipe**.
   
5. Set up your recipe
   
   1. Go to the **Name** field and enter `Get opportunities for table`  as the recipe name.
      
   2. Go to the **Location** drop-down menu and ensure the recipe is in the same folder as your app page.
      
   3. Click **Start building**.
      
   
6. Modify the New load event trigger
   
   Complete the following steps to modify the **New load event** trigger:
   
   1. Select the **New load event** trigger.
      
   2. Go to the **Setup** tab.
      
   3. Go to **Input parameters** and click **\+ Add field**
      
   4. Go to the **Name** field and provide a unique name for this parameter, such as `account_id.`
      
   5. Go to the **Label** field and provide a unique name for this field, such as `Account ID`.
      
   6. Go to the **Data type** field and select **String**.
      
   7. Go to the **Optional** field and select `No`. When `No`, this field is required.
      
   8. Go to **Output parameters** and click **\+ Add field**.
      
   9. Go to the **Name** field and provide a unique name for this output parameter, `name`.
      
   10. Go to the **Label** field and provide a unique name for this field, such as `Name`.
       
   11. Go to the **Data type** field and select **String**.
       
   12. Go to the **Optional** field and select `No`. When `No`, this field is required.
       
   13. Create the following additional output parameters:
       
       | Name | Label | Data type | Optional |
       | --- | --- | --- | --- |
       | description | Description | String | Yes |
       | opp\_type | Opp type | String | Yes |
       | stage | Stage | String | Yes |
       | deal\_amount | Deal amount | Number | Yes |
       | probability | Probability | Number | Yes |
       | opp\_id | Opp ID | String | Yes |
       
   
   Your configuration should look as follows:
   
   ![Trigger configuration](/assets/recipe-table-trigger.BHVOfQos.png)_New Load event from a table trigger_
   
7. Configure a Search for Opportunities in Salesforce (Batch) action
   
   _This action fetches the opportunities and related details for an account you specify. The output populates the output fields specified in the New load event trigger._
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Search for and select **Salesforce** as your app and select the **Search for Opportunities in Salesforce (Batch)** action.
      
   3. Select the connection type you plan to use for this action.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to populate components with recipe data.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   4. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).
      
   5. Use the **Object** drop-down menu to select `Opportunities`
      
   6. Use the **Fields to retrieve** drop-down menu to select `Opportunity ID`, `Name`, `Description`, `Stage`, `Amount`, `Probability (%)`, and `Opportunity Type`.
      
   7. Map the Account ID (Step 1) datapill into the **Account ID** field.
      
   
   Your configuration should look as follows:
   
   ![Search for Opportunities in Salesforce (Batch) action](/assets/recipe-table-salesforce-search-action.DqdveyBl.png)_Search for Opportunities in Salesforce (Batch) action_
   
8. Modify the return data to drop-down action
   
   1. Select the **Return data to component** action.
      
   2. Go to the **Table data source options** field and map in the Opportunities (Step 2) datapill.
      
   3. Go to the **Table data** section and map datapills into the following fields:
      
      | Field | Datapill |
      | --- | --- |
      | Name | Name (Step 2) |
      | stage | Stage (Step 2) |
      | Deal amount | Amount (Step 2) |
      | Opp ID | Opportunity (Step 2) |
      | Description | Description (Step 2) |
      | Probability | Probability (Step 2) |
      | Opp type | Opportunity type (Step 2) |
      
   
   You configuration should look as follows:
   
   ![Return data to component action](/assets/recipe-table-return-action.CwRWKcrt.png)_Return data to component action_
   
9. Click **Save**.
   

Your completed recipe should look as follows:

![Completed Get data for table recipe](/assets/recipe-table-complete.B-mkG6vs.png)_Completed Get data for table recipe_

### Configure page components

Complete the following steps to configure your recipe as a data source for table components in the page editor:

1. Click the **Data table** component to select it.
   
2. Go to the **Properties panel**.
   
3. Use the **Recipe input parameters** section to set up an input parameter for use in the **Get data for table** recipe created in the previous step:
   
   - Map the Selected value (Select an account) page component datapill into the **Account ID** field.
4. Use the **Displayed columns** menu to select the columns you plan to display on your page.
   
5. Configure component visibility
   
   Complete the following steps to configure this component to be visible only after a user selects an account:
   
   1. Go to the **Appearance** section.
      
   2. Click **Conditional**.
      
   3. Map in the Selected label (Select an account) datapill to the **Data** field.
      
   4. Use the **Condition** drop-down menu to select `Is present`.
      
   
6. Type `Opportunities` into the **Title** field.
   
7. Enter `10` into the  **Max table height** field.
   
8. Click **Save**.
   

Your configuration should look as follows:

![Component configuration](/assets/page-editor-get-data-table.Dl_L1e7v.png)_Component configuration_

---
