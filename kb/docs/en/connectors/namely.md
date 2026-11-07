---
url: 'https://docs.workato.com/en/connectors/namely.md'
description: >-
  The Namely connector lets you automate HR workflows: create, update, and
  search employee profiles, post updates, and trigger on new or updated
  employees.
---

# Namely

Namely offers a modern human resources management platform. Namely provides tools to streamline onboarding, automate tasks, store new hire forms, and collect eSignatures. Depending on your plan, you can also use Namely to manage payroll and benefits.

## API version

The Namely connector uses Namely's REST-based API. Refer to the [Namely API documentation](https://developers.namely.com/docs/namely-api/72f9086e4f0e7-introduction) for more information.

## Connection setup

The Namely connector supports OAuth 2.0 authentication.

Complete the following steps to connect to Namely in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Namely` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/connection-setup-updated.D3Nc3waz.png)_Namely connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the company account name you plan to connect to your Workato account in the **Company** field. You can find this name in your Namely URL. For example, if your URL is `http://acme.namely.com`, enter `acme` in this field.
   
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
7. Click **Connect**.
   
8. Click **Allow** when prompted to authorize Workato to access your Namely account.
   

## Namely and Google Sheets recipe example

This example recipe guides you through connecting [Namely](/en/connectors/namely) and [Google Sheets](/en/connectors/google-sheets) to Workato to create a simple yet powerful automation. This use case demonstrates how you can integrate these popular applications to enhance record-keeping, information-sharing, and efficiency within your team.

This recipe adds the employee name to a new row in Google Sheets when you create a new employee record in Namely. This automation triggers when a new employee record is detected in your connected Namely account.

Complete the following steps to create a recipe that adds employee names to new rows in Google Sheets when you add new employees in Namely:

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for [Namely](/en/connectors/namely#connection-setup) and [Google Sheets](/en/connectors/google-sheets#how-to-connect-to-google-sheets-on-workato).
   
4. Click **Create > Recipe** or press C+R.
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Search for `Namely` and select it as your app.
    
11. Select the **New employee profile** trigger.
    
    ![Namely new employee profile](/assets/new-employee-profile.EAuf6Xqr.png)_Select the New employee profile trigger_
    
12. Click **\+ Add step** and select **Action in app**.
    
13. Search for `Google Sheets` and select it as your app.
    
    ![Choose an app](/assets/choose.CuOTU1-J.png)_Choose Google Sheets as your app_
    
14. Select the **Add row** action.
    
15. Select the spreadsheet you plan to use in your recipe from the **Spreadsheet** drop-down menu.
    
16. Select the sheet in which you plan to add rows from the **Sheet** drop-down menu. The sheet you select must have at least one header row and one data row.
    
17. Click the **Columns Show** button, map the First name (Step 1) datapill into the **First name** field, and map the Last name (Step 1) datapill into the **Last name** field.
    
18. Map the Email (Step 1) datapill into the **Email** field and the Title (Step 1) datapill into the **Job title** field.
    
    ![Set up Google Sheets](/assets/google-sheets-setup.BSwi-DuX.gif)_Set up Google Sheets_
    
19. Click **Save**.
    
    Your recipe adds a new row containing the profile information you configured when a new employee profile is added to Namely.
    
    ![Google Sheets automation](/assets/google-sheets-automation.DDfsKg5w.png)_New employee information automatically added to Google Sheets_

---
