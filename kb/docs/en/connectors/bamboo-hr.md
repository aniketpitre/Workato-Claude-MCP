---
url: 'https://docs.workato.com/en/connectors/bamboo-hr.md'
description: >-
  The BambooHR connector lets you automate HR workflows: create, update, and
  list employees, manage time off requests, run reports, and trigger on changes.
---

# BambooHR

[BambooHR](https://www.bamboohr.com/) is a HR software solution for collecting, maintaining, and analyzing your people data.

Review a BambooHR, QuickBooks Online, and Okta example recipe

Complete the following steps to create a recipe that monitors BambooHR for new employees. When activity is detected, it creates a new employee in QuickBooks Online and a new user in Okta.

This use case is intended to serve as an example. Recipe modifications such as trigger and action configuration and conditional logic may require adjustments if you plan to include this recipe in your own workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for [BambooHR](/en/connectors/bamboo-hr#how-to-connect-to-bamboo-hr-on-workato), [QuickBooks Online](/en/connectors/quickbooks#how-to-connect-to-quickbooks-on-workato), and [Okta](/en/connectors/okta#how-to-connect-to-okta).
   
4. Click **Create > Recipe** or press C+R.
   
5. Enter a name for your recipe in the **Name** field.
   
6. Use the **Location** drop-down menu to select the project where you plan to store the recipe.
   
7. Click **Start building**.
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Search for `BambooHR` and select it as your app.
    
11. Select the **New employee** trigger.
    
    ![Select trigger](/assets/new-employee.BOiRXLzt.png)_Select New employee as your trigger_
    
12. Use the calendar modal to select the date from which your recipe should begin to monitor events in the **When first started, this recipe should pick up events from** field. The trigger checks for new events every five minutes by default. Leave this field empty to fetch events from the last hour. You can't change this value after you run or test the recipe.
    
    Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
    
    ![Setup trigger](/assets/bamboohr-trigger.BeDP3TFk.png)_Set up your trigger_
    
13. Click **Save**.
    
14. Click **\+ Add step** and select **Action in app**.
    
15. Search for `QuickBooks Online` and select it as your app.
    
    ![Choose an app](/assets/choose.D9PsArpP.png)_Choose QuickBooks Online as your app_
    
16. Select **Create employee** as your action.
    
    ![Select action](/assets/create-employee.C77tRhnw.png)_Select Create employee as your action_
    
17. Map the BambooHR Mobile phone (Step 1) datapill into the **Phone** field and the BambooHR Work email (Step 1) datapill into the **Email** field.
    
    ![Set up QuickBooks action](/assets/setup-quickbooks-action.DVKQ5K7H.gif)_Map the datapills for your action_
    
18. Map the BambooHR First name (Step 1) datapill into the **Given name** field, map the BambooHR Last name (Step 1) datapill into the **Family name** field, and then map the BambooHR Display name (Step 1) datapill into the **Display name** field.
    
    ![Map name datapills](/assets/name-datapills.Bhal2anh.png)_Map the datapills for your action_
    
19. Map the BambooHR Employee number (Step 1) datapill into the **Employee number** field.
    
    ![Map employee number datapill](/assets/employee-number.BT7s-601.png)_Map the Employee number datapill_
    
20. Click **Save**.
    
21. Click **\+ Add step** and select **Action in app**.
    
22. Search for `Okta` and select it as your app.
    
23. Select the **Create user** action.
    
    ![Select action](/assets/create-user.C7vofcns.png)_Select Create user as your action_
    
24. Map the BambooHR First name (Step 1) into the **First name** field and the BambooHR Last name (Step 1) datapill into the **Last name** field.
    
    ![Map datapills](/assets/okta-name-datapills.BspVX5ap.png)_Map the datapills for your action_
    
25. Map the BambooHR Work email (Step 1) datapill into the **Primary email ID** field and the BambooHR Work email (Step 1) datapill into the **Username** field. The **Username** field must contain an email address.
    
    ![Map datapills](/assets/okta-emails.CufheKIC.png)_Map the datapills for your action_
    
26. Map the BambooHR Employee number (Step 1) datapill into the **Employee number** field.
    
27. Click **Save**.
    

Your BambooHR, QuickBooks Online, and Okta recipe is ready to test and implement.

## API version

The BambooHR connector uses the [Bamboo REST API v1](https://documentation.bamboohr.com/docs/getting-started).

## Connection setup

The BambooHR connector supports the following authentication types:

- [API token](#api-token)
- [OAuth 2.0](#oauth2)

### API token

Use API token authentication to connect to BambooHR with a static key generated in the BambooHR portal.

#### Generate an API key in BambooHR

Complete the following steps to generate an API key before you connect in Workato:

1. Sign in to the [BambooHR](https://app.bamboohr.com/login/) portal.
   
2. Go to **My Account > API Keys**.
   
   ![Go to BambooHR API Keys](/assets/find-api-keys.xegBwE4f.png)_Navigate to BambooHR API Keys_
   
3. Create a new API key by selecting **Add New Key**.
   
4. Provide a descriptive name for this new API Key, for example, `workato_user`.
   
5. Save the generated API key in a secure location.
   
   > **API KEY ONLY VISIBLE IN THIS STEP**
   > 
   > You can't retrieve this key after this step.
   
   Refer to the [BambooHR documentation](https://documentation.bamboohr.com/docs#authentication) for more information.
   

#### Connect to BambooHR with API token authentication

Complete the following steps to set up an API token connection to BambooHR in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `BambooHR` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![BambooHR API token connection](/assets/connect-to-bamboo-hr.BuDzV5cT.png)_Set up an API token connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **API Token**.
   
6. Enter the API token you generated in [Generate an API key in BambooHR](#api-token-setup) in the **API token** field.
   
7. Enter your BambooHR subdomain in the **Sub-domain** field. This is most often your company name.
   
8. Click **Connect**.
   

### OAuth 2.0

Use OAuth 2.0 to connect to BambooHR without managing a static key. You authorize the connection through BambooHR when you connect.

#### Connect to BambooHR with OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to BambooHR in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `BambooHR` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![BambooHR OAuth 2.0 connection](/assets/oauth-2.JOCMWC8O.png)_Set up an OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth2.0**.
   
6. Enter your BambooHR subdomain in the **Sub-domain** field. This is most often your company name.
   
7. Click **Connect**.
   
8. Sign in to BambooHR when prompted and authorize access to complete the connection.

---
