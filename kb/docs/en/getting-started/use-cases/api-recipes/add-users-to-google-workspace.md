---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/api-recipes/add-users-to-google-workspace.md
description: >-
  Create an API recipe enables you to add users to your Google Workspace
  programmatically or when a new employee is detected in BambooHR.
---

# Add users to Google Workspace

This use case provides step-by-step instructions to create an API recipe and a custom endpoint that adds users to Google Workspace programmatically or when a new employee is detected in BambooHR. This allows you to automate user provisioning from your CLI (command line interface) or HR system rather than manually logging into Google Admin console to add each new hire or batches of new hires.

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. API recipe modifications such as API trigger configuration, action configuration, and conditional logic may require adjustments for your specific setup.

## What does this API recipe do?

This API recipe enables you to add users to your Google Workspace programmatically or when a new employee is detected in BambooHR.

```mermaid
flowchart TD
  subgraph M[" "]
    direction TB
    subgraph D[&nbsp New API request trigger &nbsp]
        direction LR
        x(Trigger) --- xx(Request and <br/> response setup)
    end
    subgraph H[Monitor action]
        xxx(Monitor action for error)
    end
    subgraph R[&nbsp Google Workspace add user action &nbsp]
        AA(Action) --- EE(setup)
    end
  end
  subgraph N[" "]
    direction LR
    subgraph DD[Create a new <br/> API collection: <br/> <strong> Platform > API platform > <br/> Collections </strong>]
    direction LR
    end
    subgraph HH[Create a new endpoint <br/> and configure <br/> the endpoint path <br/> and method. <br/> For example: <br/> <strong>POST</strong>, <strong>GET</strong>, <strong>PUT</strong>, <strong>DELETE</strong>]
        direction LR
    end
  end
  subgraph O[" "]
    direction TB
    subgraph DDD[Create a new <br/> recipe with a <br/> BambooHR <strong>New employee </strong> <br/> trigger.]
    direction LR
    end
    subgraph HHH[Add an HTTP <strong>Send request</strong> action <br/> that uses the endpoint <br/> you created.]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[Add users to Google <br/> Workspace programmatically <br/> with a curl command <br/> in your CLI]
    end
  end
  A([Create recipe]) -- Configure your API recipe --> M -- Create an endpoint --> N
  N -- Create an HTTP connector <br/> recipe to use your endpoint <br/> with BambooHR --> O
  N -- Add users directly from your CLI --> Q
  O --> B([API recipe workflow])
  Q --> BB([API endpoint workflow])
  D --> H
  H --> R
  DD --> HH
  DDD --> HHH

  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue2 fill:#5159f6,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef WorkatoPurple fill:#fff,stroke:#a99ff5,stroke-width:2px,color:#000;
  classDef WorkatoPurple2 fill:#d5d0fe,stroke:#d5d0fe,stroke-width:2px,color:#000;
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px;
  class x,xx,xxx,E,AA,EE,A,BB,DD,HH WorkatoTeal
  class D,H,R SubgraphDash
  class Q WorkatoBlue
  class O WorkatoPurple
  class HHH,DDD,B WorkatoPurple2
  class RR,BB WorkatoBlue2
    classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class t1,setup1,setup2,setup3,setup4,setup5,Action1,Action2,Action3,x,xx,CreateRecipe,Workflow WorkatoTeal
  class Scheduler,SFTP,CSV,Quickbase SubgraphDash
  class M,N SubgraphLight
```

## Create your API recipe

Complete the following steps to create an API recipe that adds new employees to Google Workspace:

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create a connection for Google Workspace.
   
   ### Create a connection for Google Workspace
   
   This step creates a connection between Workato and your Google Workspace account. The Google Workspace connector supports the following authentication methods:
   
   - [OAuth 2.0](#oauth-2-0-authentication)
   - [Service account](#service-account-authentication)
   
   #### OAuth 2.0 authentication
   
   Complete the following steps to connect to Google Workspace using OAuth 2.0 authentication:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select **Google Workspace** as your connection.
      
   3. Provide a name for your connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
      
   6. Optional. Expand the **Advanced settings** section and select OAuth 2.0 scopes to request for your connection.
      
      Workato requests the following scopes by default in addition to the scopes you select:
      
      | Description | Scope requested |
      | --- | --- |
      | View and manage the provisioning of users on your domain | `admin.directory.user` |
      | View and manage organization units on your domain | `admin.directory.orgunit` |
      | View and manage the provisioning of domains for your customers | `admin.directory.domain` |
      | View and manage the provisioning of user schemas on your domain | `admin.directory.userschema` |
      | View and manage the provisioning of groups on your domain | `admin.directory.group` |
      | View and manage group subscriptions on your domain | `admin.directory.group.member` |
      | View and manage data transfers between users in your organization | `admin.datatransfer` |
      | Manage your mobile devices by performing administrative tasks | `admin.directory.device.mobile.action` |
      | View audit reports for your Google Workspace domain | `admin.reports.audit.readonly` |
      | View usage reports for your Google Workspace domain | `admin.reports.usage.readonly` |
      | Manage delegated admin roles for your domain | `admin.directory.rolemanagement` |
      | Manage data access permissions for users on your domain | `admin.directory.user.security` |
      
      Refer to the [Google Directory API scopes](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing) or [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes) guide for more information about scopes.
      
   7. Click **Sign in with Google**.
      
      ![Connect to Google Workspace](/assets/setup-1.CAQwtw4I.png)_Connect to Google Workspace_
      
   8. Sign in with your Google account. Your Google account must have admin privileges to make organization-wide changes in Google Workspace.
      
   9. Click **Allow** to enable Workato to access your Google account.
      
      ![Enable Workato to access your Google account](/assets/oauth-scopes.qLH22Y9E.png)_Enable Workato to access your Google account_
      
   
   #### Service account authentication
   
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
      
   
4. Select the project where you plan to create the API request recipe.
   
5. Click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
6. Enter a name for your recipe in the **Name** field.
   
7. Use the **Location** drop-down menu to select the project where you plan to store the recipe.
   
8. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
9. Click **Pick a starting point** and select **Trigger from an app**. The API request trigger doesn't require you to establish a connection.
   
10. Click **Select an app and trigger event**.
    
11. Set up your New API request trigger.
    
    ### New API request trigger setup
    
    This step creates an API request and response that enables your recipe to process and respond to your API request.
    
    1. Search for `API platform by Workato` and select it as your app.
       
    2. Select the **New API request** trigger.
       
       ![New API request trigger](/assets/new-api-request.pwrb55D9.png)_**New API request** trigger_
       
    3. Complete the following steps to configure your request schema:
       
       1. Go to the **Request schema** section and click **\+ Add Field**.
          
       2. Enter `Users` in the **Name** and **Label** fields.
          
       3. Use the **Data type** drop-down menu to select **Object**.
          
       4. Use the **Optional** drop-down menu to select **No**.
          
       5. Click **Save**.
          
          ![Users object](/assets/users-object.OgbAdi0A.png)_Users object_
          
       6. Enter `username` in the **Name** and **Label** fields.
          
       7. Use the **Data type** drop-down menu to select **String**.
          
       8. Use the **Optional** drop-down menu to select **No**.
          
          ![Username request schema](/assets/username-request-field-nested.BRgNES-E.png)_Username Request schema_
          
       9. Use the **Nest under** drop-down menu to select **Users**.
          
       10. Click **Save**.
           
       11. Return to the **Request schema** section and click **\+ Add Field**.
           
       12. Enter `firstname` in the **Name** and **Label** fields.
           
       13. Use the **Data type** drop-down menu to select **String**.
           
       14. Use the **Optional** drop-down menu to select **No**.
           
       15. Use the **Nest under** drop-down menu to select **Users**.
           
       16. Click **Save**.
           
       17. Return to the **Request schema** section and click **\+ Add Field**.
           
       18. Enter `lastname` in the **Name** and **Label** fields.
           
       19. Use the **Data type** drop-down menu to select **String**.
           
       20. Use the **Optional** drop-down menu to select **No**.
           
       21. Use the **Nest under** drop-down menu to select **Users**.
           
       22. Click **Save**.
           
           ![Configured Request schema](/assets/nested-request-schema.BmBDKW5c.png)_Configured **Request schema**_
           
    4. Complete the following steps to configure your request responses:
       
       1. Go to the **Responses** section and click **Add response**.
          
          ![Add response](/assets/add-response.BAEut3XI.png)_Click **Add response**_
          
       2. Enter `Return result` in the **Name** field.
          
       3. Use the **HTTPS status code standard response** drop-down menu to select `200 - OK`.
          
       4. Go to the **Response schema** section and click **add fields manually**.
          
       5. Enter `result` in the **Name** and **Label** fields.
          
       6. Use the **Data type** drop-down menu to select **String**.
          
       7. Use the **Optional** drop-down menu to select **No**.
          
       8. Click **Save**.
          
          ![Configure 200 - OK response](/assets/200-response.BCLGsEMA.png)_Configured `200 - OK` response_
          
       9. Click **Add response** again.
          
       10. Enter `Error output` in the **Name** field.
           
       11. Use the **HTTPS status code standard response** drop-down menu to select `400 - Bad Request`.
           
       12. Go to the **Response schema** section and click **add fields manually**.
           
       13. Enter `result` in the **Name** and **Label** fields.
           
       14. Use the **Data type** drop-down menu to select **String**.
           
       15. Use the **Optional** drop-down menu to select **No**.
           
       16. Click **Save**.
           
           ![Configure 400 - Bad Request response](/assets/400-response.X9e5H8fD.png)_Configured `400 - Bad Request` response_
           
    
12. Click **\+ Add step** and select **Handle errors**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Handle errors**_
    
    How does the Handle errors control statement work?
    
    The [Handle errors control statement](/en/recipes/steps#handle-errors-step) allows you to monitor your recipe for errors in actions, similar to the try/catch concept in programming languages. You have the opportunity to perform the following actions if an error occurs:
    
    - Retry the sequence of actions again, in case it was a temporary error such as network issues.
      
    - Take remedial actions, such as notifying users of the error through email or error messages in the app, or to carry out a rollback. For example, you can reverse the job by deleting any created or half-created records.
      
    
    This control statement consists of two blocks: the **Monitor** block and the **Error** block. Place the actions that you plan to monitor for errors within the **Monitor** block. If all actions are successful, Workato ignores the **Error** block. However, if any action in the **Monitor** block results in an error, the actions within the **Error** block are executed.
    
    ```mermaid
    graph TD
        A(Monitor action for errors) ---> B((Error found?))
        B --> C{Yes}
        B --> D{No}
        C --> E(Define how to <br/> handle the error)
        D --> F(Continue processing <br/> the recipe)
       classDef default fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
    ```
    
13. Set up your Google Workspace add user action.
    
    ### Set up your Google Workspace add user action
    
    This step adds a user to Google Workspace. Note that this step is nested within the **Monitor** block.
    
    1. Search for and select Google Workspace as the app to monitor.
       
    2. Select **Add record** as your action.
       
    3. Use the **Object** drop-down menu to select **Users**.
       
    4. Expand the **Name** field and map the lastname (Step 1) datapill to the **Surname** field.
       
    5. Map the firstname (Step 1) datapill to the **First name** field.
       
    6. Enter the user's email address in the **Primary email** field.
       
       ![Add user action](/assets/add-user-action.CSI1nxGY.png)_Add user action_
       
    7. Click **Save**.
       
    
14. Configure your ERROR FOUND? block.
    
    This step tells your recipe how to respond if it receives an error when it executes the **Add user** action.
    
    Complete the following steps to configure your **ERROR FOUND?** block:
    
    1. Go to the **ERROR FOUND?** block and confirm that the **Yes** branch shows **DO NOT RETRY**. This option is usually set by default.
       
       ![Error found block](/assets/error-found-block.B-zgqhof.png)_**ERROR FOUND?** block_
       
    2. Go to the **Yes** branch and click **Select and app and action**.
       
    3. Search for and select API platform by Workato as your app.
       
    4. Select **Respond to API request** as your action.
       
    5. Use the **Response** drop-down menu to select **error out**.
       
    6. Expand the **Response body** section.
       
    7. Map the Error message (Step 4) datapill to the **Result** field.
       
       ![Map the Error message datapill to the Result field](/assets/error-response.CtahBRpB.png)_Map the Error message (Step 4) datapill to the **Result** field_
       
    8. Go to the **No** branch and click the **\+ Add step** button.
       
    9. Search for and select API platform by Workato as your app.
       
    10. Select **Respond to API request** as your action.
        
    11. Use the **Response** drop-down menu to select **Return result**.
        
    

## Create an API collection and API endpoint

This section provides steps on how to create a new API collection and API endpoint.

Complete the following steps to create an API collection:

1. Create an API collection.
   
   ### Create an API collection
   
   This section provides steps on how to create a new API collection where you can store your Google Workspace API endpoint.
   
   1. Go to **Platform > API platform**.
      
   2. Click the **API collections** tab.
      
   3. Click **\+ Create new collection**.
      
   4. Ensure that **API recipe collection** is selected and then click **Next**.
      
   5. Ensure that **Use existing recipes** is selected.
      
   6. Use the **Recipe folder** drop-down menu to select the folder where you plan to store the API collection.
      
   7. Deselect all endpoints.
      
   8. Enter a name in the **Collection name** field.
      
   9. Enter a version number for your collection. For example: `v1`.
      
   10. Optional. Provide a description for the collection in the **Description** field.
       
   11. Click **Create collection**.
       
       ![Set collection details](/assets/set-collection-details.Dd-H23_w.png)_Click **Create collection**_
       
   
2. Create a new endpoint.
   
   ### Create an endpoint
   
   This step creates a new endpoint based on your API request recipe and stores it in your API collection.
   
   1. Go to **Platform > API platform**.
      
   2. Click the **API collections** tab.
      
   3. Select the API collection you created in the preceding steps.
      
   4. Click **Create new endpoint**.
      
   5. Use the **Recipe** drop-down menu to select the API request recipe you created in the preceding steps.
      
   6. Use the **HTTP method** drop-down menu to select **POST**.
      
   7. Enter a name for your endpoint in the **Endpoint name** field.
      
   8. Define a path for your endpoint in the **Endpoint path** field. For example: `add-google-workspace-user-v1`. Don't include a slash `\` in your endpoint path. This is automatically appended after you create the endpoint.
      
   9. Optional. Provide a description in the **Endpoint description** field.
      
   10. Optional. Set a timeout value in the **Request timeout** field. The default value is `30` seconds and the maximum value is `240` seconds.
       
   11. Click **Add endpoint**.
       
       ![Create an endpoint](/assets/create-google-workspace-endpoint.B1QPCnl_.png)_Create an endpoint_
       
   

## Add users from a CLI

You can use your endpoint to add users directly from your CLI.

How does a curl command work?

Your curl command can be broken down to the following items:

- `-X POST`: Uses the POST HTTP method
- `https://apim.workato.com/<your-workspace-name>/<your-endpoint-name>`: Your API endpoint URL. You must replace `<your-workspace-name>` and `<your-endpoint-name>` your actual workspace and endpoint names.
- `-H "Content-Type: application/json"`: Specifies JSON format.
- `-H "API-Token: <your-api-token>"`: Authentication header. You must replace `<your-api-token>` with your actual API token. -`-d '{"username": "janderson", "firstname": "Jade", "lastname": "Anderson"}'`: The request body with the three required fields from your request schema: `username`, `firstname`, and `lastname`.

The actual base URL and authentication method depend on how your Workato API collection is configured. You can find the exact URL and authentication details in your API collection settings under **Platform > API platform > API collections**.

```shell
curl -X POST https://apim.workato.com/<your-workspace-name>/<your-endpoint-name>\
  -H "Content-Type: application/json" \
  -H "API-Token: <your-api-token>" \
  -d '{
    "users": [
      {"username": "janderson", "firstname": "Jade", "lastname": "Anderson"},
      {"username": "jhernandez", "firstname": "Josh", "lastname": "Hernandez"},
      {"username": "ssingh", "firstname": "Sanjeev", "lastname": "Singh"},
      {"username": "etan", "firstname": "Emily", "lastname": "Tan"},
      {"username": "amiller", "firstname": "Alex", "lastname": "Miller"}
    ]
  }'
```

Complete the following steps to use your API endpoint to add users to Google Workspace programmatically from your CLI:

1. Open your preferred CLI, such as Cursor or VSCode.
   
2. Run the following command, updating `<your-workspace-name>`, `<your-endpoint-name>`, and `<your-api-token>` to match your configuration:
   
   ![Run the command in your CLI](/assets/cli-curl-command.uA7XREh7.gif)_Run the command in your CLI_
   

## Add users through a BambooHR trigger

Complete the following steps to add users to Google Workspace when a new employee is detected in BambooHR:

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create a connection for BambooHR. The HTTP connector doesn't require connection setup.
   
   Create a BambooHR connection.
   
   ### Create a BambooHR connection
   
   This step creates a connection between BambooHR and your Workato account. Refer to [BambooHR](/en/connectors/bamboo-hr#how-to-connect-to-bamboo-hr-on-workato) for more information.
   
   Complete the following steps to set up your BambooHR connection:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `BambooHR` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![BambooHR connection setup](/assets/connect-to-bamboo-hr.BuDzV5cT.png)_BambooHR connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter your API token in the **API token** field. Refer to the [How to create an API key in BambooHR](/en/connectors/bamboo-hr#how-to-create-an-api-key-on-bamboo-hr) section for more information.
      
   6. Enter your subdomain in the **Sub-domain** field. For example, enter `acme` if your subdomain is `https://acme.bamboohr.com/`.
      
   7. Click **Connect**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
5. Enter a name for your recipe in the **Name** field.
   
6. Use the **Location** drop-down menu to select the project where you plan to store the recipe.
   
7. Click **Start building**.
   
8. Click **Pick a starting point** and select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your BambooHR New employee trigger.
    
    ### Set up your BambooHR New employee trigger
    
    This step creates a trigger that runs when a new employee is detected in BambooHR.
    
    Complete the following steps to set up your trigger:
    
    1. Search for and select `BambooHR` as your app.
       
    2. Select the **New/updated employee** trigger.
       
       ![Select trigger](/assets/new-employee.BOiRXLzt.png)_Select New employee as your trigger_
       
    3. Go to the **When first started, this recipe should pick up events from** field and use the calendar modal to select the date from which your recipe begins to monitor events. The trigger checks for new events every five minutes by default. Leave this field empty to fetch events from the last hour. You can't change this value after you run or test the recipe.
       
       Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
       
       ![Setup trigger](/assets/bamboohr-trigger.BeDP3TFk.png)_Set up your trigger_
       
    4. Click **Save**.
       
    
11. Click **\+ Add step** and select **Action in app**.
    
12. Set up your HTTP action.
    
    ### Set up your HTTP action
    
    This step sets up your HTTP action to map your request to the API endpoint and the response from the API endpoint.
    
    1. Search for `HTTP` and select it as your app.
       
       ![Choose an app](/assets/choose.D9PsArpP.png)_Choose an app_
       
    2. Select the **Send request** action.
       
    3. Provide a name for your request in the **Request name** field.
       
    4. Use the **Method** drop-down menu to select **Post**.
       
    5. Paste the endpoint URL you created in the preceding steps into the **Request URL** field.
       
    6. Go to the **Request headers** section and click **Add header**.
       
    7. Enter **API Token** in the **Header name** field and paste your endpoint API token in the **Value** field.
       
    8. Use the **Request content type** drop-down menu to select **JSON request body**.
       
    9. Click **Use JSON**.
       
    10. Paste the following code into the **JSON sample** field:
        
        ```json
        {
          "users": [
            {
              "username": "",
              "firstname": "",
              "lastname": ""
            }
          ]
        }
        ```
        
        ![Request schema](/assets/request-schema.Cg1UH-BN.png)_Request schema_
        
    11. Click **Next**.
        
    12. Review the data to ensure accuracy and then click **Generate schema**.
        
    13. Go to the **Request body** section.
        
    14. Map the BambooHR Work email (Step 1) datapill to the **Username** field.
        
    15. Map the BambooHR First name (Step 1) datapill to the **Firstname** field.
        
    16. Map the BambooHR Last name (Step 1) datapill to the **Lastname** field.
        
    17. Go to the **Response** section and ensure that **Response content type** is set to **JSON**.
        
    18. Go to the **Response schema** section and click **Use JSON**.
        
    19. Paste the following code into the **JSON sample** field:
        
        ```json
        {
          "result": "User added successfully",
          "username": "",
          "firstname": "",
          "lastname": ""
        }
        ```
        
        ![Response schema](/assets/response-schema.BgDX47GT.png)_Response schema_
        
    20. Click **Next**.
        
    21. Review the data to ensure accuracy and then click **Generate schema**.
        
    22. Click **Save**.
