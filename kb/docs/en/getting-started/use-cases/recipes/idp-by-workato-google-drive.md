---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/recipes/idp-by-workato-google-drive.md
description: >-
  Create a recipe that searches a Google Drive folder for Google Slides
  presentations, creates a PDF export for intelligent document processing, and
  records extracted data in Google Sheets.
---

# Extract Google Slides data with IDP by Workato

This use case guides you through connecting [Google Drive](/en/connectors/google-drive) and [IDP by Workato](/en/connectors/idp-by-workato) to create a powerful automation.

This recipe searches a Google Drive folder for Google Slides presentations, creates a PDF export for intelligent document processing, and records extracted data in Google Sheets.

## What does this recipe do?

This recipe enables you to extract matching content from Google Slides files stored in your Google Drive using IDP by Workato.

```mermaid
flowchart TD
  subgraph M[" "]
    direction TB
    subgraph D[&nbsp Scheduler by Workato New recurring event trigger &nbsp]
        direction RL
        x(setup) --- xx(Trigger)
    end
    subgraph H[Google Drive Search files action]
        xxx(Action) --- E(setup)
    end
    subgraph Y[Repeat for each loop]
        ww(Condition) --- V(setup)
    end
    subgraph J[Google Drive Export file action]
        www(Action) --- C(setup)
    end
    subgraph R[&nbsp IDP by Workato Process a document action &nbsp]
        AA(Action) --- CC(setup)
    end
    subgraph S[&nbsp Google Sheets Add row action &nbsp]
        AAA(Action) --- EEE(setup)
    end
  end
  A([Create recipe]) -- Configure your recipe --> M --> B([Automated workflow])
  D --> H
  H --> Y
  Y --> J
  J --> R
  R --> S
  classDef default fill:#fff,stroke:#67eadd,stroke-width:2px;
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class x,xx,xxx,ww,www,E,AA,EE,AAA,EEE,A,B,C,CC,V WorkatoTeal
  class D,H,R,S,Y,J SubgraphDash
  class M, default
```

## Create your recipe

Complete the following steps to create a recipe that extracts information you specify from Google Slides and records it in Google Sheets:

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create a connection for Google Drive:
   
   > **WORKATO UTILITY CONNECTORS DON'T REQUIRE SETUP**
   > 
   > The [Scheduler by Workato](/en/features/scheduler) and IDP by Workato connectors don’t require connection setup.
   
   Create a Google Drive connection.
   
   ### Create a Google Drive connection
   
   The Google Drive connector supports the following authentication types:
   
   - [OAuth 2.0 authentication](#oauth2-authentication)
   - [Service account](#service-account-authentication)
   
   #### OAuth 2.0 authentication
   
   OAuth 2.0 authentication requires specific permissions and scopes.
   
   View Google Drive OAuth 2.0 connection setup steps.
   
   #### Minimum and default scopes
   
   Workato requests the following scopes by default in addition to the scopes you select:
   
   - `drive`: See, edit, create, and delete all your Google Drive files
   - `drive.readonly`: See and download all your Google Drive files
   
   Additionally, your Google account must have the `Edit` permission for all files and folders that you plan to use in Workato recipes.
   
   #### Connect to Google Drive using OAuth 2.0
   
   Complete the following steps to set up an OAuth 2.0 connection to in Workato:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select **Google Drive** as your connection on the **New Connection** page.
      
   3. Enter a name for your connection in the **Connection name** field.
      
      ![Connection setup](/assets/google-drive-connection-setup.o_esWDm7.png)_Google Drive connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
      
   6. Optional. Expand the **Advanced settings** section and use the **Requested permissions** drop-down menu to specify OAuth scopes to request for your connection.
      
   7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
      
   8. Click **Sign in with Google**.
      
   9. Click **Allow** to authorize Workato to access your Google Drive.
      
   
   #### Service account authentication
   
   Service account authentication requires a Google service account and an enabled Google Workspace API.
   
   View service account connection setup steps.
   
   A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.
   
   Service accounts provide the following benefits:
   
   - **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
   - **Dedicated permissions:** Service accounts can only access projects that you share with them.
   - **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.
   
   Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.
   
   ##### Set up a Google service account
   
   Complete the following steps to set up a Google service account:
   
   1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
      
   2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
      
      ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
      
   3. Click the **Email** of the service account you intend to use.
      
      ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
      
   4. Copy the service account's **Email** and save it to configure your connection later.
      
      ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
      
   5. Go to the **KEYS** tab.
      
   6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
      
   7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
      
   
   ##### Connect to Google Drive using service account authentication
   
   Service account authentication requires the following prerequisites:
   
   - [Create a service account and generate a private key](#service-account-setup)
   - [Enable the Google Workspace API](https://support.google.com/googleapi/answer/6158841)
   
   Complete the following steps to set up a service account connection to Google Drive in Workato:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for `Google Drive` and select it as your app.
      
   3. Enter a name for your connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu to select **Service account**.
      
   6. Enter the service account's email address in the **GCP project service account email** field.
      
      ![Retrieve your GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Retrieve your GCP Project service account email_
      
   7. Enter the **Private key**. Retrieve the private key from the downloadable JSON. Include both `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----\n`.
      
   8. Optional. Enter the **User email** of the account to impersonate. If left blank, Workato accesses the service account's Drive.
      
      User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Drive. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Drive. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
      
   9. Optional. Expand the **Advanced settings** section and use the **Requested permissions** drop-down menu to specify OAuth scopes to request for your connection.
      
   10. Click **Sign in with Google**.
       
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Use the **Location** drop-down menu to select the project where you plan to store the recipe.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Run on a schedule**. This creates a new recipe with the Scheduler by Workato [New recurring event trigger](/en/features/scheduler/triggers/new-recurring-event). This trigger doesn't require a connection.
   
9. Set up your Scheduler by Workato New recurring event trigger.
   
   ### Set up Scheduler by Workato New recurring event trigger
   
   This trigger sets the interval for how frequently the recipe runs. The Scheduler by Workato trigger doesn't require connection setup.
   
   1. Click the trigger in the recipe editor.
      
      ![Click the trigger](/assets/click-trigger.Cxrovggz.png)_Click the trigger_
      
   2. Use the **Time unit** drop-down menu to select **Weeks**.
      
      - Available options include **Minutes**, **Hours**, **Days**, **Weeks**, **Months**, or **Custom schedule**.
   3. Enter `1` in the **Trigger every** field to run the recipe weekly.
      
   4. Choose the days the recipe should run in the **Days of the week** field. For example, select **Monday**.
      
   5. Specify the time for the recipe to run in the **Trigger at** field. For example, enter `12:00 AM`.
      
   6. Optional. Select the timezone in the **Timezone** field. The default is **America/Los\_Angeles** if left blank.
      
   7. Optional. Set the start date and time in the **Start after** field, or leave it blank to activate the trigger immediately after you start the recipe. You can't change this value after you run or test the recipe.
      
      ![Configure the trigger](/assets/trigger-config.pNyPMahZ.png)_Configure the trigger_
      
   8. Click **Save**.
      
   
10. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
11. Set up your Google Drive Search files or folders (Batch) action.
    
    ### Set up the Google Drive Search files or folders action
    
    This step searches a Google Drive folder you specify for Google Slides files.
    
    1. Search for `Google Drive` and select it as your app.
       
    2. Select the **Search files or folders (Batch)** action.
       
    3. Use the **Files or folders** drop-down menu to select **Files**.
       
       ![Set up the Search files or folders (Batch) action](/assets/google-drive-search-files-folders.Dybv46S8.png)_**Search files or folders** (Batch) action_
       
    4. Set **Folder** to **Select folder** and use the drop-down menu to select the folder you plan to search for files.
       
    5. Optional. Enter a name in the **Name** field to fetch files or folders that contain partial matches.
       
    6. Go to the **Query** field and enter the following value to filter your search to Google Slides files:
       
       ```
       mimeType='application/vnd.google-apps.presentation'
       ```
       
    7. Click **Save**.
       
    
12. Click **\+ Add step** and select **Repeat for each**.
    
13. Set up your Repeat for each step.
    
    ### Set up the Repeat for each step
    
    This step iterates through each Google Slides file in the folder you select.
    
    1. Map the Google Drive (Step 2) datapill to the **Input list** field.
       
       ![Set up the Repeat for each step](/assets/repeat-for-each.DW3y1h5e.png)_Set up the Repeat for each step_
       
    2. Use the **Repeat mode** drop-down menu to select **One item at a time**.
       
    3. Use the **Clear step output** drop-down menu to select **No**.
       
    4. Click **Save**.
       
    
14. Click **\+ Add step** and select **Action in app**.
    
15. Set up your Google Drive Export file action.
    
    ### Set up the Google Drive Export file action
    
    This step exports the Google Slides file as a PDF. IDP by Workato doesn't support Google Slides document types.
    
    1. Search for `Google Drive` and select it as your app.
       
    2. Select the **Export file** action.
       
    3. Use the **File** drop-down menu to select **Use file ID**.
       
       ![Set up the Google Drive Export file action](/assets/export-file-action.Dd9QSPXq.png)_Set up the Google Drive **Export file** action_
       
    4. Map the Foreach (Step 3) datapill to the **File** value field.
       
    5. Set **MIME type** to **Select MIME type** and use the value drop-down menu to select **PDF**.
       
    6. Click **Save**.
       
    
16. Click **\+ Add step** and select **Action in app**.
    
17. Set up your Process a document using IDP by Workato action.
    
    ### Set up the Process a document using IDP by Workato action
    
    This step processes the exported PDF for fields you identify.
    
    1. Search for `IDP by Workato` and select it as your app.
       
    2. Select the **Process a document using IDP by Workato** action.
       
    3. Map the Google Drive (Step 4) datapill to the **File contents** field.
       
       ![Set up the Process a document using IDP by Workato action](/assets/idp-process-document.C4NLYLvu.png)_Set up the **Process a document using IDP by Workato** action_
       
    4. Set **File type** to **Select from list** and use the value drop-down menu to select **PDF**.
       
    5. Use the **Document type** drop-down menu to select **Documents**.
       
    6. Use the **IDP version** drop-down menu to select **OCR augmented LLM extraction**.
       
    7. Copy the following JSON schema and paste it into the **Fields to identify** section:
       
       ```json
       [
         {
           "name": "FileName",
           "type": "string",
           "optional": false,
           "description": "Project Name",
           "control_type": "text",
           "label": "Project name"
         },
         {
           "name": "ProductManager",
           "type": "string",
           "optional": true,
           "description": "Product Manager",
           "control_type": "text",
           "label": "Product manager"
         },
         {
           "name": "PrintFileDeliveryDate",
           "type": "string",
           "optional": true,
           "description": "Print File Delivery Date",
           "control_type": "text",
           "label": "Print file delivery date"
         },
         {
           "name": "ProductFeatureName",
           "type": "string",
           "optional": false,
           "description": "Presentation feature or topic",
           "control_type": "text",
           "label": "Brand range"
         },
         {
           "name": "FeatureOverview",
           "type": "string",
           "optional": true,
           "control_type": "text",
           "label": "Feature overview",
           "description": "Summary or overview section title"
         },
         {
           "name": "Marketswherelaunched",
           "type": "string",
           "optional": true,
           "description": "Markets Where Launched",
           "control_type": "text",
           "label": "Markets where launched"
         }
       ]
       ```
       
    8. Click **Save**.
       
    
18. Click **\+ Add step** and select **Action in app**.
    
19. Set up your Google Sheets Add row in a sheet action.
    
    ### Set up the Google Sheets Add row in a sheet action
    
    This step adds the content identified in the IDP by Workato processing step to a new row in a Google sheet you select.
    
    1. Search for `Google Sheets` and select it as your app.
       
    2. Select the **Add row** action.
       
    3. Use the **Google Drive** drop-down menu to select the drive you plan to use.
       
       ![Set up the Add row action](/assets/google-sheet-add-row.Cu_XuRWe.png)_Set up the Add row action_
       
    4. Use the **Spreadsheet** drop-down menu to select the spreadsheet where you plan to add the new row.
       
    5. Use the **Sheet** drop-down menu to select the sheet where you plan to add the new row.
       
    6. Expand the **Columns** section.
       
    7. Map the File name (Step 5) datapill to the **ProjectName** field.
       
    8. Map the Product manager (Step 5) datapill to the **ProductManager** field.
       
    9. Map the Print file delivery date (Step 5) datapill to the **PrintFileDeliveryDate** field.
       
    10. Map the Product feature name (Step 5) datapill to the **ProductFeatureName** field.
        
    11. Map the Feature overview (Step 5) datapill to the **FeatureOverview** field.
        
    12. Map the Markets where launched (Step 5) datapill to the **Marketswherelaunched** field.
        
        ![Map the datapills to the corresponding fields](/assets/map-idp-extracted-content.D3dDsBEq.gif)_Map the datapills to the corresponding fields_
        
    13. Click **Save**.
        
    

Your **Extract Google Slides data with IDP by Workato** recipe is ready to test and implement.
