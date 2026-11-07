---
url: 'https://docs.workato.com/en/getting-started/build-first-recipe.md'
description: >-
  Build your first Workato recipe step by step and learn how triggers and
  actions connect your apps to automate a workflow.
---

# Create your first recipe

Build your first recipe with this video guide

[Video](https://www.youtube.com/embed/H4MMLklNpPU)

Recipes are automated workflows that connect your apps. Each recipe contains a trigger and one or more actions. When you start a recipe, it waits for a triggering event to run the actions.

The following steps guide you through building a recipe that closes a case in Salesforce whenever an issue with the same name is closed in Jira.

## Create a new recipe

Complete the following steps to create a new recipe:

1. Sign in to your Workato account.
   
2. Go to the **Projects** page.
   
   ![The Projects page](/assets/projects-page.CgXt349P.png)_The **Projects** page_
   
3. Select an existing project or use one of the following methods to create a new one:
   
   - Click **Create > Project**
   - Press C+P
4. Enter a **Project name**.
   
   ![Enter project name](/assets/create-project-name.DJ9CcZ8d.png)_Enter a project name_
   
5. Click **Build a recipe**.
   
6. Click **Create project**.
   
7. Enter `My first recipe` in the **Recipe name** field.
   
8. Ensure **Trigger from an app** is selected as the recipe starting point, then click **Start building**. ![Set up your recipe view](/assets/setup-recipe-view.CZAMrgKO.png) _The **Set up your recipe** menu_
   

## Connect to Jira

Complete the following steps to connect to Jira:

1. Search for and select **Jira** in the **Choose an app** search box.
   
2. Select the **Updated issue** trigger.
   
3. Enter a descriptive and unique name for the connection in the **Connection name** field.
   
4. Select **API token** in the **Auth type** field.
   
5. Enter the URL of your Jira account in the **Host name** field.
   
6. Enter your Jira account email in the **Email** field.
   
7. Enter your Atlassian API token in the **API token** field.
   
   How can I create an Atlassian API token?
   
   To create a new API token in Atlassian, complete the following steps:
   
   1. Go to **Account settings > Security**.
      
   2. Click [Create and manage API tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
      
   3. Click **Create API token**.
      
   4. Enter a name for your token in the **Name** field, and then click **Create**.
      
   5. Click **Copy** to retrieve your new API token.
      
   
8. Click **Connect**. ![Jira connection parameters](/assets/jira-connection-parameters.4DikqXJw.png)
   

## Set up the trigger

The following trigger activates whenever an issue is closed in Jira. When you start the recipe, it checks for matching events from the previous seven days.

Complete the following steps to set up the trigger:

1. Switch the **When first started, this recipe should pick up events from** field to [formula mode](/en/formulas/formula-mode) and enter `7.days.ago`.
   
2. Click the **Set trigger condition** toggle.
   
3. Locate the Jira Name (Step 1) datapill in the **Recipe data** menu under **Updated issue (Step 1 output) > Fields > Status** and map it to the **Trigger data** field.
   
   ![Search for and drag the datapill](/assets/datapill.Dc-cFEw0.png)_Locate the Name (Step 1) datapill_
   
4. Select **contains** in the **Condition** field.
   
5. Enter `Closed` in the **Value** field. ![Trigger fields](/assets/trigger-fields.BOpB93WZ.png)_Completed **Updated issue** trigger fields_
   

## Connect to Salesforce

Complete the following steps to connect to Salesforce:

1. Click **\+ Add step**, and then select **Action in app**. ![Add step](/assets/add-step.BCmLKGCG.png)_The **Add step** button_
   
2. Search for and select **Salesforce** in the **Choose an app** search box.
   
3. Select the **Search records (batch)** action.
   
4. Enter a descriptive and unique name for the connection in the **Connection name** field.
   
5. Select **OAuth 2.0** in the **Auth type** field.
   
6. Click **Connect** to open the Salesforce sign-in dialog. ![Salesforce connection parameters](/assets/salesforce-connection-parameters.DVy0sB6T.png) _Completed Salesforce connection fields and the **Connect** button_
   
7. Sign in to your Salesforce account.
   

## Set up the action

The following action searches for cases in Salesforce with the same case name as the Jira issue.

Complete the following steps to set up the action:

1. Select **Case** in the **Search for** field.
   
2. Enter `150` in the **Limit** field to restrict the number of records the action returns.
   
3. Locate the Jira Summary (Step 1) datapill in the **Recipe data** menu under **Updated issue (Step 1 output) > Fields > Parent > Fields** and map it to the **Subject** field.
   
   ![Action fields](/assets/action-fields.BkwLthlF.png)_Completed **Search for Cases** fields_
   

## Set up the conditional statement

The following [IF condition](/en/features/if-conditions) checks if the matching Salesforce case from the previous step is open. If it is, the recipe closes the case.

Complete the following steps to set up the conditional statement:

1. Click **\+ Add step**, and then select **IF condition**. ![Add step](/assets/add-step-three.Byw11Jzu.png)_The **Add step** button_
   
2. Locate the Salesforce Status (Step 2) datapill in the **Recipe data** menu under **Search Cases (Step 2 output) > Cases** and map it to **Data field**.
   
3. Select **does not equal** in the **Condition** field.
   
4. Enter `Closed` in the **Value** field. ![Conditional step](/assets/if-condition-updated.CSa6YI_H.png) _Completed IF condition fields_
   
5. Click **Select an app and action**.
   
   ![Select an app and action](/assets/select-an-app-and-action.EU24iwcG.png)
   
6. Search for and select **Salesforce** in the **Choose an app** search box.
   
7. Select the **Update record** action.
   
8. Select **Case** in the **Object** field.
   
9. Locate the Salesforce Case ID (Step 2) datapill in the **Recipe data** menu under **Search Cases (Step 2 output) > Cases** and map it to the **Case ID** field.
   
10. Select **Closed** in the **Status** field. ![Conditional step fields](/assets/if-condition-fields.DPTC-0aW.png)_Completed **Update case** fields_
    

## Save and start your recipe

Complete the following steps to save and start your recipe:

1. Click **Save**, then **Exit**.
   
2. Click **Start recipe**. Your completed recipe should resemble the following screenshot: ![Example recipe](/assets/example-recipe.8_n9QnAb.png)_Example recipe_
   

> **NEXT STEPS**
> 
> - Explore the [community library](https://app.workato.com/browse/recipes) to find ready-to-use recipes built by other users.
> - Learn about other types of triggers and actions in [Recipe design](/en/recipes/building-recipes#learn-more-about-recipe-components).

---
