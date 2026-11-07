---
url: 'https://docs.workato.com/en/getting-started/use-cases/docusign-box-slack.md'
description: >-
  Build a recipe that invites DocuSign signees to collaborate in Box and
  notifies your team in Slack when a document is signed.
---

# Invite DocuSign signees to collaborate in Box and notify your team in Slack recipe

This use case guides you through connecting [DocuSign](/en/connectors/docusign), [Box](/en/connectors/box), and [Slack](/en/connectors/slack) to Workato to create a multi-application automation.

## What does this recipe do?

This recipe monitors DocuSign for newly signed documents. It checks if the email address of the individual who signed the document includes your company's email domain name, for example: `@acme.com`. If the email address does not contain your company's email domain name, the recipe creates a folder in Box, adds the user as a collaborator to the folder, and then creates a shared link to the folder. The recipe then sends an email to the user with the shared link and posts a message in Slack notifying you and your team that the user has been invited to collaborate.

```mermaid
flowchart TD
  subgraph M[" "]
    direction TB
    subgraph D[&nbsp DocuSign New signed document &nbsp]
        direction RL
        ax(setup) --- aa(Trigger)
    classDef default fill:#b3e0e1,stroke:#51c2b9,stroke-width:1px;
    end
    subgraph S[Box Create folder action]
        L(Action) --- EW(setup)
    classDef default fill:#b3e0e1,stroke:#51c2b9,stroke-width:1px;
    end
    subgraph SS[&nbsp Box Add user as collaborator action &nbsp]
        LL(Action) --- EX(setup)
    classDef default fill:#b3e0e1,stroke:#51c2b9,stroke-width:1px;
    end
    subgraph SSS[&nbsp Box Create shared link action &nbsp]
        LLL(Action) --- EY(setup)
    classDef default fill:#b3e0e1,stroke:#51c2b9,stroke-width:1px;
    end
    subgraph R[Send email]
        RR(Action) --- EZ(setup)
    classDef default fill:#b3e0e1,stroke:#51c2b9,stroke-width:1px;
    end
    subgraph H[Slack post]
        AA(Action) --- EE(setup)
    classDef default fill:#b3e0e1,stroke:#51c2b9,stroke-width:1px;
    end
  end
  A([Create recipe]) -- Configure your recipe --> M --> B([Automated workflow])
  D --> S
  S --> SS
  SS --> SSS
  SSS --> R
  R --> H
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class D,S,SS,SSS,R,H SubgraphDash
  class A,B,ax,aa,WX,WW,WWW,L,EW,LL,EX,LLL,EY,RR,EZ,AAA,AA,EE WorkatoTeal
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class M SubgraphLight
```

## Create your recipe

Complete the following steps to create a recipe that monitors DocuSign for newly signed documents, uses conditional logic to determine if the user is an employee at your company and then creates a new folder, adds the user as a collaborator to the folder, creates a shared folder link, emails the folder link to the new user, and posts a Slack message:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for DocuSign, Box, and Slack:
   
   Create a DocuSign connection.
   
   ### Create a DocuSign connection
   
   This step creates a connection between Workato and your DocuSign account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `DocuSign` on the **New connection** page.
      
   3. Provide a name for your connection in the **Name** field.
      
      ![Connect to DocuSign](/assets/connect.CStONNx7.png)_Connect to DocuSign_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Demo** drop-down menu to select whether the account you plan to use is a demo account.
      
   6. Enter your DocuSign account ID in the **Account ID** field. To find your account ID: sign in to DocuSign > click **Settings > Apps and Keys > API Account ID**.
      
   7. Enter your connect key in the **Connect key** field.
      
   8. Click **Connect**.
      
   
   Create a Box connection.
   
   ### Create a Box connection
   
   This step creates a connection between Workato and your Box account.
   
   The Box connector supports both authorization code grant and [client credentials](/en/connectors/box#client-credentials) authentication.
   
   Complete the following steps to set up your Box connection using authorization code grant authentication:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Box` on the **New connection** page.
      
   3. Provide a name that identifies which Box instance Workato is connected to in the **Connection name** field.
      
      ![Box Connection 1](/assets/box_connection_1.OJ4XKoIg.png)_Create your connection_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store this connection.
      
   5. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
      
   6. Optional. Expand **Advanced settings** to select **Requested permissions (Oauth scopes)** options.
      
      You can select from the following scopes:
      
      - Read files and folders
      - Read and write files and folders
      - Manage app users
      - Manage managed users
      - Manage groups
      - Manage webhooks
      - Manage enterprise properties
      - Manage retention policies
      - Global content manager
      - Admin can make calls on behalf of users
      - Manage signature requests
      - Manage Box Relay
   7. Click **Connect**. This opens the Box sign in dialog.
      
   8. Enter your Box account email address and password.
      
      ![Box Connection 2](/assets/box_connection_2.DakkUsWJ.png)_Log in to Box_
      
   9. Click **Authorize**.
      
   10. Review the requested permissions and click **Grant access to Box**.
       
       ![Grant access to Box](/assets/grant-access.CygYC_9w.png)_Grant access to Box_
       
   
   Create a Slack connection.
   
   ### Create a Slack connection
   
   This step creates a connection between Workato and your Slack account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Slack` on the **New connection** page.
      
   3. Enter a name for your connection in the **Connection name** field.
      
      ![Slack connection setup](/assets/connect.CHSRBplW.png)_Slack connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Optional. Configure **Advanced** and **Custom OAuth profile** settings if required for your account type.
      
   6. Click **Connect**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your DocuSign New document event trigger.
    
    ### Set up DocuSign New document event trigger
    
    This step monitors your DocuSign files for newly signed documents and triggers your recipe when a new signing event is detected.
    
    1. Search for `DocuSign` and select it as your app.
       
    2. Select the **New document event in DocuSign** trigger.
       
       ![Set up your recipe](/assets/docusign-trigger-setup.LKCCgiOO.png)_Select the New document event in DocuSign trigger_
       
    3. Use the calendar modal to select the date from which your recipe should begin to monitor events in the **When first started, this recipe should pick up events from** field. The trigger checks for new events every five minutes by default. Leave this field empty to fetch events from the last hour. You can't change this value after you run or test the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
       
    4. Use the **Event** drop-down menu to select **Signed** as the event you plan to monitor. This field defaults to **All** if you do not make a selection.
       
    5. Click **Save**.
       
    
11. Click **\+ Add step** and select **IF condition**.
    
    ![Add IF condition](/assets/docusign-if-condition.BkUFZV0Q.png)_Select IF condition_
    
12. Set up your doesn't contain Email IF condition.
    
    ### Set up doesn't contain Email IF condition
    
    This step creates an IF condition that instructs your recipe on how to behavior if an email address isn't found.
    
    1. Map the DocuSign Email (Step 1) datapill into the **Data field**.
       
    2. Use the **Condition** drop-down menu to select `doesn't contain`.
       
    3. Enter the value you plan to use for your IF condition in the **Value** field. For example, this use case checks if the email address in the **Data field** contains your company's email domain name in the **Value** field.
       
       ![Set up IF condition](/assets/docusign-if-condition.CXKLZbcI.gif)_Set up IF condition_
       
    4. Click **Save**.
       
    
13. Click **\+ Add step** for the **No** condition and select **Add action in app**.
    
14. Set up your Box Create folder action.
    
    ### Set up Box Create folder action
    
    This step creates a new folder where you plan to store the signed document.
    
    1. Search for Box and select it as your app.
       
       ![Choose Box as your app](/assets/choose.Cxg5AxoL.png)_Choose Box as your app_
       
    2. Select the **Create folder** action.
       
       ![Select action](/assets/create-folder.tBzylQ6J.png)_Select the Create folder action_
       
    3. Map the DocuSign Name (Step 1) datapill into the **New folder name** field.
       
       ![Set up Create folder action](/assets/box-create-folder-action.Bw6kJ5J3.gif)_Set up the Create folder action_
       
    4. Select the parent folder in which you plan to add your new folder in the **Parent folder** field.
       
    5. Click **Save**.
       
    
15. Click **\+ Add step** under your first Box action and select **Add action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
16. Set up your Box Create collaboration action.
    
    ### Set up Box Create collaboration action
    
    This step configures collaborator access to the newly signed document.
    
    1. Search for Box and select it as your app.
       
    2. Select the **Create collaboration** action.
       
       ![Select action](/assets/create-collaboration.CGFrp9K2.png)_Select the Create collaboration action_
       
    3. Click the **Show** button under **Item**.
       
    4. Map the Box Type (Step 3) datapill into the **Type** field.
       
    5. Map the Box ID (Step 3) datapill into the **File or folder ID** field.
       
       ![Item setup](/assets/collaborators-item-setup.Ck91cSCm.png)_Map your datapills into the Item section_
       
    6. Expand the **Accessible by** section.
       
    7. Enter the email address of the user in the **Email ID of collaborator** field.
       
    8. Use the **Role** drop-down menu to select the role you plan to provide for the collaborator.
       
       ![Select role](/assets/select-role.dqOh5awD.png)_Select a role for the collaborator_
       
    9. Click **Save**.
       
    
17. Click **\+ Add step** under your second Box action and select **Add action in app**.
    
18. Set up your Box Create shared link action.
    
    ### Set up Box Create shared link action
    
    This step creates a shareable link that enables you to share the signed document.
    
    1. Search for Box and select it as your app.
       
    2. Select the **Create folder shared link** action.
       
    3. Map the Box ID (Step 3) datapill into the **Folder ID** field.
       
       ![Folder ID](/assets/create-shared-folder-link.swOAInv1.png)_Map the Folder ID datapill_
       
    4. Use the **Access** drop-down menu to select **Collaborators**.
       
    5. Click **Save**.
       
    
19. Click **\+ Add step** and select **Add action in app**.
    
20. Set up your Email by Workato action.
    
    ### Set up Email by Workato action
    
    This step creates an email with a subject and message and sends it to the email addresses that you add.
    
    1. Search for Email by Workato and select it as your app. This app does not require connection configuration.
       
       ![Email by Workato app](/assets/choose.6AqK7Iz4.png)_Select Email by Workato as your app_
       
    2. Select the **Send email** action.
       
    3. Map the DocuSign Email (Step 1) datapill into the **To** field. This is the email address that receives the email you send.
       
       ![Email setup](/assets/email-setup.DIyjHBjB.png)_Map the DocuSign Email (Step 1) datapill into the To field_
       
    4. Enter a message subject in the **Subject** field. For example, `Invitation to collaborate`.
       
    5. Optional. Use the **Email type** drop-down menu to select the format of the email message. This field defaults to HTML.
       
    6. Enter a message for the body of your email in the **Message** field.
       
    7. Click **Save**.
       
    
21. Click **\+ Add step** and select **Add action in app**.
    
22. Set up your Slack Post message action.
    
    ### Set up Slack Post message action
    
    This step creates a Slack post with the text, attachment title, attachment link, and collaborator name that you provide.
    
    1. Search for Slack and select it as your app.
       
       ![Select Slack](/assets/choose.CBFE7k6j.png)_Select Slack as your app_
       
    2. Select the **Post message** action.
       
    3. Use the **Channel** drop-down menu to select the Slack channel in which you plan to post your message.
       
    4. Enter a message for the post in the **Basic text** field. You can also map the DocuSign Name (Step 1) datapill into this field if you plan to include the new collaborator's name in the message automatically.
       
    5. Enter an attachment title for the Slack post in the **Attachment title** field.
       
    6. Map the Box URL (Step 5) datapill into the **Attachment title link** field. Attachment titles are clickable and direct users to the URL you provide when clicked.
       
       ![Set up Slack action](/assets/slack-action-setup.DcCxoXSD.png)_Map the Box URL (Step 5) datapill into the Attachment title link field_
       
    7. Enter text for the attachment in the **Attachment text** field. You can map the DocuSign Name (Step 1) and Email (Step 1) datapills into this field if you plan to include specific details about the new collaborator.
       
    8. Click **Save**.
       
    

Your **Invite DocuSign signees to collaborate in Box and notify your team in Slack** recipe is ready to test and implement.

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/box-google-cloud-storage-bigquery.md
description: >-
  Build a recipe that watches a Box folder for new CSV files and loads their
  data into Google BigQuery through Google Cloud Storage.
---

# Load Box CSV data to Google BigQuery with Google Cloud Storage recipe

This use case guides you through connecting [Box](/en/connectors/box), [Google Cloud Storage](/en/connectors/google_cloud_storage), and [Google BigQuery](/en/connectors/bigquery) to create a powerful automation.

## What does this recipe do?

This recipe monitors a Box folder for new CSV files, downloads each file’s contents, uploads the content to Google Cloud Storage, and then loads the data into a Google BigQuery table.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB
    subgraph BoxTrigger[&nbsp Box New event in folder trigger &nbsp]
      Trigger(Trigger) --- setup1(setup)
    end
    subgraph BoxAction[&nbsp Box Download file action &nbsp]
      Action1(Action) --- setup2(setup)
    end
    subgraph GoogleCloudStorage[&nbsp Google Cloud Storage Upload object action &nbsp]
      Action2(Action) --- setup3(setup)
    end
    subgraph GoogleBigQuery[&nbsp Google BigQuery Load data from Google Cloud Storage into BigQuery action &nbsp]
      Action3(Action) --- setup4(setup)
    end
  end
  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  BoxTrigger --> BoxAction --> GoogleCloudStorage -->  GoogleBigQuery
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class CreateRecipe,Trigger,setup1,Action1,setup2,Action2,setup3,Action3,setup4,Workflow WorkatoTeal
  class BoxTrigger,BoxAction,GoogleCloudStorage,GoogleBigQuery SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## How can I use this recipe?

This recipe provides a versatile approach for handling CSV data, facilitating automated workflows between Box, Google Cloud Storage, and Google BigQuery. Consider the following usage examples for different departmental needs:

- **Track marketing campaigns**: Simplify campaign performance data collection and analysis. By storing CSV files with metrics in Box, you can integrate your data with Google BigQuery to create detailed reports and dashboards.
- **Manage sales leads**: Automatically transfer sales leads or customer data from CSV files saved in Box. This provides sales teams with the latest data in Google BigQuery and improves sales tracking and performance monitoring.
- **Monitor operational KPIs**: Automate the upload of operational logs or supply chain data from Box to Google BigQuery. This helps operations managers monitor key performance indicators and identify areas for process improvement without manual data entry.

## Create your recipe

Complete the following steps to create a recipe that monitors a Box folder for new CSV files, downloads each file’s contents, uploads the content to Google Cloud Storage, and then loads the data into a Google BigQuery table:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Box, Google Cloud Storage, and Google BigQuery:
   
   Create a Box connection.
   
   ### Create a Box connection
   
   This step creates a connection between Workato and your Box account.
   
   The Box connector supports both authorization code grant and [client credentials](/en/connectors/box#client-credentials) authentication.
   
   Complete the following steps to set up your Box connection using authorization code grant authentication:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Box` on the **New connection** page.
      
   3. Provide a name that identifies which Box instance Workato is connected to in the **Connection name** field.
      
      ![Box Connection 1](/assets/box_connection_1.OJ4XKoIg.png)_Create your connection_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store this connection.
      
   5. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
      
   6. Optional. Expand **Advanced settings** to select **Requested permissions (Oauth scopes)** options.
      
      You can select from the following scopes:
      
      - Read files and folders
      - Read and write files and folders
      - Manage app users
      - Manage managed users
      - Manage groups
      - Manage webhooks
      - Manage enterprise properties
      - Manage retention policies
      - Global content manager
      - Admin can make calls on behalf of users
      - Manage signature requests
      - Manage Box Relay
   7. Click **Connect**. This opens the Box sign in dialog.
      
   8. Enter your Box account email address and password.
      
      ![Box Connection 2](/assets/box_connection_2.DakkUsWJ.png)_Log in to Box_
      
   9. Click **Authorize**.
      
   10. Review the requested permissions and click **Grant access to Box**.
       
       ![Grant access to Box](/assets/grant-access.CygYC_9w.png)_Grant access to Box_
       
   
   Create a Google Cloud Storage connection.
   
   ### Create a Google Cloud Storage connection
   
   This step creates a connection between Workato and your Google Cloud Storage account.
   
   You must have a [service account](/en/connectors/google_cloud_storage#create-a-service-account) to create a Google Cloud Storage connection in Workato.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Google Cloud Storage` on the **New connection** page.
      
   3. Provide a name that identifies which Google Cloud Storage instance Workato is connected to in the **Connection name** field.
      
      ![Connect to Google Cloud Storage](/assets/connect.DN7RNrmu.png)_Connect to Google Cloud Storage_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store this connection.
      
   5. Enter a valid Google Cloud Platform project ID in the **Project identifier** field. You can find the project ID in the [Google Cloud Console](https://console.cloud.google.com) by clicking **Select a project** in the navigation menu.
      
   6. Enter the email address of the service account in the **GCS Project service account email** field.
      
   7. Provide the private key from the downloaded JSON file in the **Private key** field. You must copy the private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----`.
      
   8. Optional. Enter a comma-separated list of buckets the connection can access in the **Restrict to bucket** field. For example, `bucket-1,bucket2`.
      
   9. Optional. Expand **Advanced settings** and use the **Requested permissions (OAuth scopes)** drop-down menu to select the permissions to request for this connection.
      
   10. Click **Sign in with Google**.
       
   
   Create a Google BigQuery connection.
   
   ### Create a Google BigQuery connection
   
   This step creates a connection between Workato and your Google BigQuery account.
   
   The Google BigQuery connector supports both OAuth 2.0 and [service account](/en/connectors/bigquery#service-account) authentication.
   
   Complete the following steps to set up your Google BigQuery connection using OAuth 2.0 authentication:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Google BigQuery` on the **New connection** page.
      
   3. Provide a name that identifies which Google BigQuery instance Workato is connected to in the **Connection name** field.
      
      ![Connect to Google BigQuery](/assets/connect.C6fPJsKo.png)_Connect to Google BigQuery_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store this connection.
      
   5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
      
   6. Click **Sign in with Google**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your Box New event in folder trigger.
    
    ### Set up Box New event in folder trigger
    
    This trigger monitors Box for newly uploaded CSV files and activates the recipe only when the file name ends with a `.csv` extension.
    
    1. Search for `Box` and select it as your app.
       
       ![Choose Box as your app](/assets/choose.Cxg5AxoL.png)_Choose Box as your app_
       
    2. Select the **New event in folder** trigger.
       
       ![Select the New event in folder trigger](/assets/new-event-in-folder.lop7ld8R.png)_Select the New event in folder trigger_
       
    3. Select the Box connection you created in the preceding steps.
       
    4. Use the **Folder** drop-down menu to select the folder you plan to monitor for events.
       
    5. Use the **Events to monitor** drop-down menu to select **File uploaded**.
       
    6. Click the **Set trigger condition** toggle.
       
    7. Map the Box Name (Step 1) datapill (nested under the File/folder source (Step 1) object) to the **Trigger data** field.
       
       ![Configure the trigger condition](/assets/trigger-condition.0aTOrIOR.gif)_Configure the trigger condition_
       
    8. Use the **Condition** drop-down menu to select **ends with**.
       
    9. Enter `.csv` in the **Value** field.
       
    10. Click **Save**.
        
    
11. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
12. Set up your Box Download file action.
    
    ### Set up Box Download file action
    
    This step downloads the contents of the CSV file uploaded to Box.
    
    1. Search for Box and select it as your app.
       
       ![Choose Box as your app](/assets/choose.Cxg5AxoL.png)_Choose Box as your app_
       
    2. Select the **Download file** action.
       
       ![Select the Download file action](/assets/download-file.Bnj-oajA.png)_Select the Download file action_
       
    3. Map the Box ID (Step 1) datapill (nested under the File/folder source (Step 1) object) to the **File ID** field.
       
       ![Map the file ID](/assets/map-file-id.DIVERtS2.gif)_Map the file ID_
       
    4. Optional. Specify the **Chunk size** and unit (for example, B, KB, MB) for file transfer. The default is 10MB, with a minimum of 32KB and a maximum of 10MB. Larger chunk sizes improve throughput but may exceed API quotas.
       
    5. Click **Save**.
       
    
13. Click **\+ Add step** and select **Action in app**.
    
14. Set up your Google Cloud Storage Upload object action.
    
    ### Set up Google Cloud Storage Upload object action
    
    This step uploads the Box CSV file contents to a bucket in Google Cloud Storage using file streaming.
    
    1. Search for `Google Cloud Storage` and select it as your app.
       
       ![Choose Google Cloud Storage](/assets/choose.WirhtABx.png)_Choose Google Cloud Storage_
       
    2. Select the **Upload object** action.
       
       ![Select the Upload object action](/assets/upload-object.U3-HHRZy.png)_Select the Upload object action_
       
    3. Select the Google Cloud Storage connection you created in the preceding steps.
       
    4. Use the **Bucket name** drop-down menu to select the bucket where you plan to upload the Box CSV file contents.
       
    5. Enter a name for the object in the **Name** field, map the Job ID (Properties) datapill, and append `.csv` to specify the file extension.
       
       ![Configure the object name](/assets/name.D79pO_ZK.png)_Configure the object name_
       
       The Job ID (Properties) datapill is a [default property](/en/recipes/data-pills-and-mapping#default-datapills). Mapping it to the name helps identify which [job](/en/recipes/jobs) processed the object.
       
    6. Map the Box File content (Step 2) datapill to the **Object content** field.
       
    7. Click **Save**.
       
    
15. Click **\+ Add step** and select **Action in app**.
    
16. Set up your Google BigQuery Load data from Google Cloud Storage into BigQuery action.
    
    ### Set up Google BigQuery Load data from Google Cloud Storage into BigQuery action
    
    This step loads the CSV file content data from Google Cloud Storage to a table in Google BigQuery.
    
    1. Search for `Google BigQuery` and select it as your app.
       
       ![Choose Google BigQuery](/assets/choose.CWGoJfIE.png)_Choose Google BigQuery_
       
    2. Select the **Load data from Google Cloud Storage into BigQuery** action.
       
       ![Select the Load data from Google Cloud Storage into BigQuery action](/assets/load-data-from-gcs-into-bigquery.wFgazTb5.png)_Select the Load data from Google Cloud Storage into BigQuery action_
       
    3. Select the Google BigQuery connection you created in the preceding steps.
       
    4. Use the **Project** drop-down menu to select the project to be billed for the query.
       
    5. Use the **Dataset** drop-down menu to select the dataset that contains the table where you plan to load the CSV file data.
       
    6. Use the **Table** drop-down menu to select the table where you plan to load the CSV file data.
       
    7. Locate the **Source URI** field and perform the following actions:
       
       1. Enter `gs://`.
          
       2. Map the Google Cloud Storage Bucket (Step 3) datapill.
          
       3. Enter `/`.
          
       4. Map the Google Cloud Storage Name (Step 3) datapill.
          
          ![Configure the Source URI](/assets/source-uri.DUeqRmBD.png)_Configure the Source URI_
          
    8. Use the **Source format** drop-down menu to select **CSV**.
       
    9. Use the **Autodetect** drop-down menu to select **Yes**. This field enables Google BigQuery to automatically infer the schema and options of the data being loaded into the table.
       
    10. Use the **Alter table columns when required?** drop-down menu to choose **Allow field addition** and **Allow field relaxation**. These options enable you to add new optional fields to your schema and change existing required fields to optional.
        
    11. Use the **Create disposition** drop-down menu to select **Create if needed**. This options tells Google BigQuery to create the table if it doesn't already exist.
        
    12. Click **Save**.
        
    

Your **Load Box CSV data to Google BigQuery with Google Cloud Storage** recipe is ready to test and implement.

Example recipe configuration.

![Box, Google Cloud Storage, and Google BigQuery recipe](/assets/recipe.CkdHplsI.png)_**Load Box CSV data to Google BigQuery with Google Cloud Storage** recipe_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/gmail-filestorage-slack.md
description: >-
  Create a recipe that extracts image attachments from Gmail, stores them in
  Workato FileStorage, generates a public link, and posts it in Slack.
---

# Share image attachments from email in Slack using a public link recipe

This use case guides you through connecting [Gmail](/en/connectors/gmail), [Workato FileStorage](/en/features/workato-filestorage), and [Slack](/en/connectors/slack) to create a powerful automation.

## What does this recipe do?

This recipe extracts image attachments from Gmail, stores them in Workato FileStorage, generates a public link, and posts it in Slack. You can use this recipe to share submitted images, reports, or visuals without manually uploading them.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB

    subgraph Gmail[&nbsp Gmail New email trigger &nbsp]
      t1(Trigger) --- setup1(setup)
    end

    subgraph DownloadAttachment[&nbsp Gmail Download attachment action &nbsp]
      Action1(Action) --- setup2(setup)
    end

    subgraph CreateFile[&nbsp Workato FileStorage Create file action &nbsp]
      Action2(Action) --- setup3(setup)
    end

    subgraph GenerateLink[&nbsp Workato FileStorage Generate action &nbsp]
      Action3(Action) --- setup4(setup)
    end

    subgraph Slack[&nbsp Workbot for Slack Post message action &nbsp]
      Action4(Action) --- setup5(setup)
    end

  end

  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  Gmail --> DownloadAttachment --> CreateFile --> GenerateLink --> Slack
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class Gmail,DownloadAttachment,CreateFile,GenerateLink,Slack SubgraphDash
  class t1,setup1,setup2,setup3,setup4,setup5,Action1,Action2,Action3,Action4,CreateRecipe,Workflow WorkatoTeal
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## Create your recipe

Complete the following steps to create your recipe:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Gmail and Slack:
   
   > **WORKATO UTILITY CONNECTORS DON'T REQUIRE SETUP**
   > 
   > The Workato FileStorage connector doesn't require connection setup.
   
   Create a Gmail connection.
   
   ### Create a Gmail connection
   
   This step creates a connection between Workato and your Gmail account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Gmail` on the **New connection** page.
      
   3. Enter a name for your connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Select **OAuth 2.0** as the **Authentication type**.
      
   6. Optional. Click **Advanced settings** and select additional **OAuth 2.0 scopes**. If left blank, the following scopes are requested:
      
      - **See your primary Google Account email address**
      - **See and edit your email labels**
      - **Send email on your behalf**
      - **View your email messages and settings**
      - **Read, compose, and send emails from your Gmail account**
   7. Click **Sign in with Google** and sign in to your Google account to complete the setup.
      
   
   Create a Slack connection.
   
   ### Create a Slack connection
   
   This step creates a connection between Workato and your Slack account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Slack` on the **New connection** page.
      
   3. Enter a name for your connection in the **Connection name** field.
      
      ![Slack connection setup](/assets/connect.CHSRBplW.png)_Slack connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Optional. Configure **Advanced** and **Custom OAuth profile** settings if required for your account type.
      
   6. Click **Connect**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your Gmail New email trigger.
    
    ### Set up Gmail New email trigger
    
    This trigger checks Gmail for new emails at an interval you specify.
    
    1. Search for `Gmail` and select it as your app. The **New email** trigger is selected automatically.
       
       ![Choose Gmail](/assets/choose.uNvzK7c8.png)_Choose Gmail_
       
    2. Optional. Configure the **Trigger poll interval** field to specify how frequently to check for new events.
       
    3. Optional. Configure the **When first started, this recipe should pick up events from** field to specify the date to retrieve emails from.
       
    
11. Click **\+ Add step** and select **IF condition**.
    
12. Set up your IF condition.
    
    ### Set up email attachments IF condition
    
    This IF condition checks if the email contains attachments.
    
    1. Switch **Data field** to [formula mode](/en/formulas/formula-mode) and map the Gmail Attachments (Step 1) datapill.
       
    2. Set **Condition** to **is present**.
       
       ![Check if the email contains attachments](/assets/check-attachments-presence.BsEOhWIi.png)_Check if the email contains attachments_
       
    
13. Go to the **Yes** path and click **\+ Add step** > **Repeat for each**.
    
14. Set up your email attachments Repeat for each loop.
    
    ### Set up an email attachments Repeat for each loop
    
    This loop iterates through all the attachments in the email to ensure that all attachments are processed.
    
    1. Map the Gmail Attachments (Step 1) list datapill to the **Input list** field.
       
    2. Ensure **Repeat mode** is set to **One item at a time**.
       
       ![Iterate through attachments list](/assets/iterate-attachments.CMYW2OVf.png)_Iterate through attachments list_
       
    
15. Click **\+ Add step** and select **IF condition**.
    
16. Set up your image attachment IF condition.
    
    ### Set up your image attachment IF condition
    
    This IF condition filters only image attachments.
    
    1. Map the Gmail Mime type (Step 1) datapill to **Data field**.
       
    2. Set **Condition** to **contains**.
       
    3. Enter `image/` in the **Value** field.
       
       ![Check the image's MIME type](/assets/check-mime-type.C2wmc3rf.png)_Check the image's MIME type_
       
    
17. Click **Select an app and action**.
    
18. Set up your Gmail Download attachment action.
    
    ### Set up Gmail Download attachment action
    
    This step downloads the image attachment's content.
    
    1. Search for `Gmail` and select it as your app.
       
       ![Choose Gmail](/assets/choose.uNvzK7c8.png)_Choose Gmail_
       
    2. Select the **Download attachment** action.
       
       ![Select the Download attachment action](/assets/download-attachment.LVn8nAbA.png)_Select the Download attachment action_
       
    3. Map the Gmail ID (Step 1) datapill to the **Email ID** field.
       
    4. Map the Gmail Attachment ID (Step 1) datapill to the **Attachment ID** field.
       
       ![Configure the Download attachment action](/assets/download-attachment-config.DojsxjUn.png)_Configure the Download attachment action_
       
    
19. Click **\+ Add step** and select **Action in app**.
    
20. Set up your Workato FileStorage Create file action.
    
    ### Set up your Workato FileStorage Create file action
    
    This step stores the downloaded image in Workato FileStorage.
    
    1. Search for `Workato FileStorage` and select it as your app.
       
       ![Choose Workato FileStorage](/assets/choose.B5LNcTYp.png)_Choose Workato FileStorage_
       
    2. Select the **Create file** action.
       
       ![Select the Create file action](/assets/create-file.BrE7Ppjs.png)_Select the Create file action_
       
    3. Map the Foreach Filename (Step 3) datapill to the **File name** field.
       
    4. Specify the location of where to create the file in the **File path** field.
       
    5. Map the Gmail Content bytes (Step 5) datapill to the **File contents** field.
       
       ![Select the Create file action](/assets/create-file-config.BglagYeq.png)_Select the Create file action_
       
    
21. Click **\+ Add step** and select **Action in app**.
    
22. Set up your Workato FileStorage Generate shareable file link action.
    
    ### Set up Workato FileStorage Generate shareable file link action
    
    This step generates a public download link for the image.
    
    1. Search for `Workato FileStorage` and select it as your app.
       
       ![Choose Workato FileStorage](/assets/choose.B5LNcTYp.png)_Choose Workato FileStorage_
       
    2. Select the **Generate shareable file link** action.
       
       ![Select the Generate shareable file link action](/assets/generate-shareable-file-link.CWZj6nx0.png)_Select the Generate shareable file link action_
       
    3. Set the **Scope** field to **Download**.
       
    4. Map the Workato FileStorage File path (Step 6) datapill to the **File path** field.
       
       ![Configure the Generate shareable file link action](/assets/generate-shareable-link-config.BL9LV3RV.png)_Configure the Generate shareable file link action_
       
    
23. Click **\+ Add step** and select **Action in app**.
    
24. Set up your Slack Post message action.
    
    ### Set up Slack Post message action
    
    This step posts the image link in Slack, which users can click to download the attachment.
    
    1. Search for `Slack` and select it as your app.
       
       ![Choose Slack](/assets/choose.CBFE7k6j.png)_Choose Slack_
       
    2. Select the **Post message** action.
       
       ![Select the Post message action](/assets/post-message-action.UsCOyv3h.png)_Select the Post message action_
       
    3. Use the **Channel** drop-down menu to specify where to post the message.
       
    4. Enter a message in the **Basic text** field. For example, `*New attachment*`.
       
    5. Map the Workato FileStorage File name (Step 6) datapill to the **Attachment title** field.
       
    6. Map the Workato FileStorage Shareable link (Step 7) datapill to the **Attachment title link** field.
       
    7. Optional. Enter text in the **Attachment text** field. This text appears under the attachment link.
       
       ![Configure the Post message action](/assets/post-message-config.D6L_Imep.png)_Configure the Post message action_
       
    
    ![Outcome](/assets/slack-post.BDySz-BU.png)_Outcome_
    
25. Click **Save**.
    

Your **Share image attachments from email in Slack using a public link** recipe is ready to test and implement.

Example recipe configuration.

![Share image attachments from email in Slack using a public link recipe](/assets/recipe.CiWdu7g4.png)_**Share image attachments from email in Slack using a public link** recipe_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/quickbase-oracle-ebs-slack.md
description: >-
  Build a recipe that connects Quickbase, Oracle EBS, and Slack to sync
  employees and notify your team of each new record.
---

# Sync Quickbase employees to Oracle EBS and notify your team in Slack recipe

This use case guides you through connecting [Quickbase](/en/connectors/quickbase), [Oracle EBS](/en/connectors/oracle-ebs), and [Slack](/en/connectors/slack) to Workato to create a powerful automation.

## What does this recipe do?

This recipe syncs employees from Quickbase to Oracle E-Business Suite (EBS) and then posts a notification in Slack.

```mermaid
flowchart TD
  subgraph M[" "]
    direction TB
    subgraph D[&nbsp Quickbase New record trigger &nbsp]
        direction RL
        s1(setup) --- t1(Trigger)
    end
    subgraph S[&nbsp Oracle EBS Create employee action &nbsp]
        L(Action) --- EW(setup)
    end
    subgraph H[&nbsp Slack post &nbsp]
        AA(Action) --- EE(setup)
    end
  end
  A([Create recipe]) -- Configure your recipe --> M --> B([Automated workflow])
  D --> S
  S --> H
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class s1,t1,L,EW,AA,EE,A,B WorkatoTeal
  class D,S,H SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class M SubgraphLight
```

## Create your recipe

Complete the following steps to create a recipe that syncs employees from Quickbase to Oracle EBS and then posts a notification in Slack.

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Quickbase, Oracle EBS, and Slack:
   
   Create a Quickbase connection.
   
   ### Create a Quickbase connection
   
   This step creates a connection between Workato and your Quickbase account.
   
   Workato supports the following authentication methods for connecting to Quickbase:
   
   - [Create a Quickbase connection](#create-a-quickbase-connection)
   - [User-token authentication](#user-token-authentication)
   - [Username and password authentication](#username-and-password-authentication)
   
   ### User-token authentication
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Quickbase` on the **New connection** page.
      
   3. Provide a unique **Connection name** that identifies the Quickbase instance to which it is connected.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter your **Quickbase subdomain**. This is most often your company name.
      
   6. Use the **User-token authentication?** drop-down menu to select **Yes**.
      
   7. Provide your **User token**. Refer to the [Generate a user token](/en/connectors/quickbase#generate-user-token) section for more information.
      
   8. Click **Connect**.
      
   
   ### Username and password authentication
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Quickbase` on the **New connection** page.
      
   3. Provide a unique **Connection name** that identifies the Quickbase instance you plan to use.
      
      ![Quickbase connection setup](/assets/connect.byecfmaJ.gif)_Set up your Quickbase connection with a username and password_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter your **Quickbase subdomain**. This is most often your company name.
      
   6. Use the **User-token authentication?** drop-down menu to select **No**.
      
   7. Provide your Quickbase **username** and **password**.
      
   8. Click **Connect**.
      
   
   Create an Oracle EBS connection.
   
   ### Create an Oracle EBS connection
   
   This step creates a connection between Workato and your Oracle EBS account.
   
   Ensure that you complete the [prerequisite steps](/en/connectors/oracle-ebs#prerequisites) before you begin to set up your connection.
   
   Complete the following steps to set up your connection:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Oracle E-Business Suite` on the **New connection** page.
      
   3. Enter a name for your connection in the **Connection name** field.
      
      ![Oracle recipe](/assets/connect.CA53ZLWk.png)_Set up your Oracle E-Business Suite connection_
      
   4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
      
   5. Use the **Connection type** drop-down menu to specify whether this is a cloud or on-prem connection. If you're connecting to an on-premise Oracle E-Business Suite instance, select the appropriate on-prem group from the drop-down menu.
      
   6. Enter the base URL for your Oracle SOA Gateway REST services in the **Instance URL** field. For example, `https://oracleebs.mycompany.com:8000/`.
      
   7. Enter your Oracle SOA Gateway REST services username in the **Username** field.
      
   8. Enter your password in the **Password** field.
      
   9. Click **Connect**.
      
   
   Create a Slack connection.
   
   ### Create a Slack connection
   
   This step creates a connection between Workato and your Slack account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Slack` on the **New connection** page.
      
   3. Enter a name for your connection in the **Connection name** field.
      
      ![Slack connection setup](/assets/connect.CHSRBplW.png)_Slack connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Optional. Configure **Advanced** and **Custom OAuth profile** settings if required for your account type.
      
   6. Click **Connect**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your Quickbase New record trigger.
    
    ### Set up Quickbase New record trigger
    
    This trigger monitors your Quickbase account for new records.
    
    1. Search for `Quickbase` and select it as your app.
       
       ![Select Quickbase](/assets/choose.DjEADCNF.png)_Select Quickbase as your app_
       
    2. Select the **New record** trigger.
       
       ![Select your trigger](/assets/new-record.DAW_13Xs.png)_Select the New record trigger_
       
    3. Use the **Application** drop-down menu to select the application you plan to monitor for new records.
       
       ![Set up your trigger](/assets/configure-new-record-trigger.CsT7UsTm.png)_Set up your New record trigger_
       
    4. Use the **Table** drop-down menu to select the table item you plan to monitor. For example, `Employees`.
       
    5. Use the calendar modal to select the date from which your recipe should begin to monitor events in the **When first started, this recipe should pick up events from** field. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
       
    6. Click **Save**.
       
    
11. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
12. Set up your Oracle EBS Create employee action.
    
    ### Set up Oracle EBS Create employee action
    
    This step creates an employee record in your Oracle EBS account.
    
    1. Search for `Oracle E-Business Suite` and select it as your app.
       
       ![Choose an app](/assets/choose.DD4oJZD6.png)_Choose Oracle EBS as your app_
       
    2. Select the **Execute operation** action.
       
       ![Select action](/assets/execute-operation.DS-_D1Km.png)_Select the Execute operation action_
       
    3. Provide a **Service name** for your action. For example, `employee`.
       
       ![Select action](/assets/service-operation-name.B1GSUlam.png)_Provide a service and operation name_
       
    4. Provide an **Operation name** for your action. For example, `Create employee`.
       
    5. Expand **Operation request header** and select the language code you plan to use for your action.
       
    6. Expand **Operation input** and provide the **First name**, **Last name**, and **Email address**. ![Select action](/assets/oebs-operation-input.CrM30EWH.png)_Provide values for your operation input_
       
    7. Click **Save**.
       
    
13. Click **\+ Add step** and select **Add action in app**.
    
14. Set up your Slack Post message action.
    
    ### Set up Slack Post message action
    
    This step posts a Slack message to the channel you specify with the new employee's details.
    
    1. Search for `Slack` and select it as your app.
       
       ![Select Slack](/assets/choose.CBFE7k6j.png)_Select Slack as your app_
       
    2. Select the **Post message** action.
       
    3. Use the **Channel** drop-down menu to select the Slack channel where you plan to post your message.
       
       ![Set up Slack](/assets/oracle-slack.CzSrpGRD.png)_Set up your Slack action_
       
    4. Enter a message for the post in the **Basic text** field. You can also map the Quickbase Name (Step 1) datapill into this field if you plan to automatically include the new employee's name.
       
    5. Enter an attachment title for the Slack post in the **Attachment title** field.
       
    6. Map the Quickbase File URL (Step 1) datapill into the **Attachment title link** field. Attachment titles are clickable and direct users to the URL you provide when clicked.
       
    7. Enter text for the attachment in the **Attachment text** field. You can map the Quickbase Name (Step 1) and Role (Step 1) datapills into this field if you plan to include specific details about the new employee.
       
    8. Click **Save**.
       
    

Your **Sync Quickbase employees to Oracle EBS and notify your team in Slack** recipe is ready to test and implement.

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/greenhouse-sap-successfactors-odata.md
description: >-
  Build a recipe that connects Greenhouse and SAP SuccessFactors OData to create
  user accounts in real time when new hires are added.
---

# Sync Greenhouse new hires to SAP SuccessFactors recipe

This use case guides you through connecting [Greenhouse](/en/connectors/greenhouse) and [SAP SuccessFactors OData](/en/connectors/successfactors/successfactors) to create a powerful automation.

## What does this recipe do?

This recipe monitors Greenhouse for new hires and creates new user accounts in SAP SuccessFactors in real time.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB

    subgraph NewEvent[Greenhouse New event trigger]
      t1(Trigger) --- setup1(setup) --- w(webhook)
    end

    subgraph GetCandidate[&nbsp Greenhouse Get object by ID action: Candidate &nbsp]
      Action1(Action) --- setup2(setup)
    end

    subgraph GetJob[&nbsp Greenhouse Get object by ID action: Job &nbsp]
      Action2(Action) --- setup3(setup)
    end

    subgraph CreateRecord[&nbsp SAP SuccessFactors OData Create record action: User &nbsp]
      Action4(Action) --- setup5(setup)
    end
  end

  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  NewEvent --> GetCandidate --> GetJob --> CreateRecord
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class t1,w,setup1,setup2,setup3,setup4,setup5,Action1,Action2,Action3,Action4,CreateRecipe,Workflow WorkatoTeal
  class NewEvent,GetCandidate,GetJob,CreateRecord SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## Create your recipe

Complete the following steps to create a recipe that monitors Greenhouse for new hires and creates new user accounts in SAP SuccessFactors in real time:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Greenhouse and SAP SuccessFactors OData:
   
   Create a Greenhouse connection.
   
   ### Create a Greenhouse connection
   
   This step creates a connection between Workato and your Greenhouse account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Greenhouse` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Greenhouse connection setup](/assets/connect.BsUiOD6n.png)_Greenhouse connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter your API key in the **API key** field.
      
      Complete the following steps in Greenhouse to create your API key if you haven't already:
      
      1. Go to **Configure > Dev Center > API Credential Management**.
         
      2. Click **Create new API key**.
         
      3. Use the **API type** drop-down menu to select **Harvest**.
         
      4. Search for and select `Workato` in the **Partner** field.
         
      5. Enter a description for your API key in the **Description** field.
         
      6. Click **Manage permissions**.
         
      7. Click **Copy** to copy the API key.
         
      8. Click **I have stored the API key**.
         
      9. Keep the default permissions selected, or choose additional ones relevant to your use case in the **Manage permissions** section.
         
      10. Click **Save**.
          
   6. Enter the user email the API key is generated from in the **User email** field.
      
   7. Use the **Environment** drop-down menu to specify the environment instance you are connecting to. The default is **Production** if left blank.
      
   8. Click **Connect**.
      
   
   Create a SAP SuccessFactors OData connection.
   
   ### Create a SAP SuccessFactors OData connection
   
   This step creates a connection between Workato and your SAP SuccessFactors OData account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `SAP SuccessFactors OData` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![SAP SuccessFactors OData connection setup](/assets/connect._eQqEDPa.png)_SAP SuccessFactors OData connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Connection type** drop-down menu to select the connection method you plan to use. You can select your [on-prem group](/en/on-prem/groups) name or select **Cloud** to use a direct connection.
      
   6. Use the **Authentication type** drop-down menu to select your authentication method. Options include **Basic** and **OAuth 2.0**.
      
   7. Enter the company ID in the **Company ID** field. The company ID is located in **Show version information** under the profile drop-down menu and in the URL after `company=`.
      
   8. Enter your SAP SuccessFactors user ID in the **User ID** field.
      
   9. Provide your authentication information.
      
      **Basic authentication**
      
      1. Enter your password in the **Password** field.
         
      
      **OAuth 2.0**
      
      1. Enter the OAuth client ID in the **Client ID** field.
         
      2. Enter the X.509 private key used to sign the SAML assertion in the **Private key** field.
         
         The private key can be from a self-signed X.509 certificate or one generated by SAP SuccessFactors. It is a base64-encoded string enclosed between `-----BEGIN ENCRYPTED PRIVATE KEY-----` and `-----END ENCRYPTED PRIVATE KEY-----`. Enter only the encoded string, excluding the beginning and ending lines, to avoid an error.
         
   10. Use the **Environment** drop-down menu to select your corresponding SAP SuccessFactors environment. Refer to the [List of SAP SuccessFactors API Servers](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/af2b8d5437494b12be88fe374eba75b6.html) for more information on the mapping between your API endpoint and SAP SuccessFactors environment.
       
   11. Optional. Enter the application interface key in the **Application interface key** field. The default is Workato's application interface key if left blank.
       
   12. Optional. Select the API server standard UTC time zone in the **API server timezone** field.
       
   13. Click **Connect**.
       
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your Greenhouse New event trigger.
    
    ### Set up Greenhouse New event trigger
    
    This trigger monitors Greenhouse for new hires in real-time. You must set up a webhook in Greenhouse to complete the setup for this trigger.
    
    1. Search for `Greenhouse` and select it as your app.
       
       ![Choose Greenhouse](/assets/choose.COciOsmA.png)_Choose Greenhouse_
       
    2. Select the **New event** trigger.
       
       ![Select the New event real-time trigger](/assets/new-event.BZy9c_ho.png)_Select the New event real-time trigger_
       
    3. Select the Greenhouse connection you created in the preceding steps.
       
    4. Use the **Event category** drop-down menu to select **Candidate**.
       
    5. Use the **Event** drop-down menu to select **Candidate hired**.
       
    6. Use a random string generator to create a secret key that is at least 32 characters long, and enter it in the **Secret key** field. Store this key in a secure location, as it is required to configure the webhook in Greenhouse.
       
       ![New candidate hired configuration](/assets/new-candidate-hired.VmiJH6YX.png)_New candidate hired configuration_
       
    7. Copy the webhook endpoint URL provided in the help section of the recipe editor. This value is also required to configure the webhook in Greenhouse.
       
       ![Copy the webhook endpoint URL](/assets/endpoint-url.BDWlwQsk.png)_Copy the webhook endpoint URL_
       
    8. Click **Save**.
       
    
11. Sign in to your Greenhouse instance to create a webhook that corresponds to the **New event** trigger.
    
    What is a webhook?
    
    ### Greenhouse webhook example
    
    A webhook is a notification sent by an application to a target URL in real-time when a specified event occurs. You can choose which events trigger these notifications.
    
    You must create a webhook in Greenhouse that sends data to Workato whenever a candidate is marked as hired for this recipe.
    
    ```mermaid
    flowchart TD
        A(Candidate marked as hired in Greenhouse) -- The trigger activates --> B(Send webhook notification)
        B --> C(Workato receives notification)
        C --> D(Process candidate data)
      classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
    classDef WorkatoPink fill:#f3c1c2,stroke:#f3c1c2,stroke-width:1px;
    ```
    
    Set up your Greenhouse webhook.
    
    ### Set up a Greenhouse webhook
    
    This webhook sends a notification to your Workato recipe each time a candidate is marked as hired in Greenhouse.
    
    1. Go to **Configure > Dev Center > Webhooks > Webhooks**. The **Create a new webhook** page appears.
       
    2. Provide a name for your webhook in the **Name this webhook** field.
       
    3. Use the **When** drop-down menu to select **Candidate hired**. This field specifies the Greenhouse event that triggers the webhook.
       
    4. Paste the webhook endpoint URL from Workato into the **Endpoint URL** field.
       
    5. Enter the secret key you created when configuring the trigger in the **Secret key** field.
       
    6. Click **Create webhook**.
       
    
12. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
13. Set up your Greenhouse Get object by ID action (Candidate).
    
    ### Set up Greenhouse Get object by ID action (Candidate)
    
    This step retrieves information about the candidate using the candidate ID.
    
    1. Search for `Greenhouse` and select it as your app.
       
       ![Choose Greenhouse](/assets/choose.COciOsmA.png)_Choose Greenhouse_
       
    2. Select the **Get object by ID** action.
       
       ![Select the Get object by ID action](/assets/get-object-by-id.C0P2RjCI.png)_Select the Get object by ID action_
       
    3. Use the **Object** drop-down menu to select **Candidate**.
       
    4. Map the Greenhouse ID (Step 1) datapill (nested under the `Candidate` object) to the **Candidate ID** field.
       
       ![Map the candidate ID datapill](/assets/map-candidate-id.DJ2Uokdc.gif)_Map the candidate ID (Step 1) datapill_
       
    5. Click **Save**.
       
    
14. Click **\+ Add step** and select **Action in app**.
    
15. Set up your Greenhouse Get object by ID action (Job).
    
    ### Set up Greenhouse Get object by ID action (Job)
    
    This step retrieves information about the job using the job ID.
    
    1. Search for `Greenhouse` and select it as your app.
       
       ![Choose Greenhouse](/assets/choose.COciOsmA.png)_Choose Greenhouse_
       
    2. Select the **Get object by ID** action.
       
       ![Select the Get object by ID action](/assets/get-object-by-id.C0P2RjCI.png)_Select the Get object by ID action_
       
    3. Use the **Object** drop-down menu to select **Job**.
       
    4. Map the Greenhouse ID (Step 1) datapill (nested under the `Jobs` array) to the **Job ID** field.
       
       ![Map the job ID datapill](/assets/map-job-id.BUrDrJj1.gif)_Map the job ID (Step 1) datapill_
       
    5. Click **Save**.
       
    
16. Click **\+ Add step** and select **Action in app**.
    
17. Set up your SAP SuccessFactors OData Create record action.
    
    ### Set up SAP SuccessFactors OData Create record action
    
    This step creates a user in SAP SuccessFactors based on the hired candidate's information in Greenhouse. Refer to the [SAP SuccessFactors API reference documentation](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/e13d5de2c3844adca3d1161f78fc638c.html?version=2411) for more information.
    
    1. Search for `SAP SuccessFactors OData` and select it as your app.
       
       ![Choose SAP SuccessFactors OData](/assets/choose.C6hN6W34.png)_Choose SAP SuccessFactors OData_
       
    2. Select the **Create record** action.
       
       ![Select the Create record action](/assets/create-record.B5MLD3Z5.png)_Select the Create record action_
       
    3. Use the **Object** drop-down menu to select **User**.
       
    4. Enter `t` in the **Status** field. This indicates that the user has an active status.
       
    5. Map the Greenhouse Candidate ID (Step 2) datapill to the **User ID** field. You can adjust the mapping based on your specific workflow requirements.
       
    6. Map the Greenhouse First name (Step 3) datapill to the **First name** field.
       
    7. Map the Greenhouse Last name (Step 3) datapill to the **Last name** field.
       
    8. Optional. Map additional fields based on your specific use case or the available data from Greenhouse. In this example, the following fields are mapped:
       
       - **Cell phone**: Map the Greenhouse Value (Step 2) datapill (nested under the `Phone numbers` array).
       - **Department**: Map the Greenhouse Name (Step 3) datapill (nested under the `Departments` array).
       - **Email**: Map the Greenhouse Value (Step 2) datapill (nested under the `Email addresses` array), or construct it using [formula mode](/en/formulas/formula-mode).
       
       ![Construct the email using formula mode](/assets/email.CRDWZSIz.png)_Construct the email using formula mode_
       
       - **Location**: Map the Greenhouse Name (Step 3) datapill (nested under `Offices > Location`).
       
       If these optional fields are currently hidden in the step, click **Show optional fields** and search for the relevant fields you plan to map.
       
       ![Create user configuration](/assets/create-user-config.DGEd0tGw.png)_Create user configuration_
       
    9. Click **Save**.
       
    

Your **Sync Greenhouse new hires to SAP SuccessFactors** recipe is ready to test and implement.

Example recipe configuration.

![Greenhouse and SAP SuccessFactors OData recipe](/assets/recipe.CYTYSWtR.png)_**Sync Greenhouse new hires to SAP SuccessFactors** recipe_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/workday-python-google-drive.md
description: >-
  Build a recipe that exports Workday workers to CSV using Python snippets by
  Workato and uploads the file to Google Drive.
---

# Export Workday workers to CSV with Python and upload to Google Drive recipe

This use case guides you through connecting [Workday](/en/connectors/workday), [Python snippets by Workato](/en/connectors/python), and [Google Drive](/en/connectors/google-drive) to create a powerful automation.

## What does this recipe do?

This recipe performs a daily search for workers in Workday, converts the output data from JSON to CSV format using Python, and uploads the resulting CSV file to Google Drive.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB
    subgraph Scheduler[&nbsp Scheduler by Workato New recurring event trigger &nbsp]
      Trigger(Trigger) --- setup1(setup)
    end
    subgraph Workday[&nbsp Workday Search business object batch action &nbsp]
      Action1(Action) --- setup2(setup)
    end
    subgraph Python[&nbsp Python snippets by Workato Execute code action &nbsp]
      Action2(Action) --- setup3(setup)
    end
    subgraph GoogleDrive[&nbsp Google Drive Upload file action &nbsp]
      Action3(Action) --- setup4(setup)
    end
  end
  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  Scheduler --> Workday --> Python -->  GoogleDrive
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class CreateRecipe,Trigger,setup1,Action1,setup2,Action2,setup3,Action3,setup4,Workflow WorkatoTeal
  class Scheduler,Workday,Python,GoogleDrive SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## Create your recipe

Complete the following steps to create a recipe that searches for workers in Workday, converts the output JSON data into CSV format using Python, and uploads the CSV file to Google Drive:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Workday and Google Drive:
   
   > **WORKATO UTILITY CONNECTORS DON'T REQUIRE SETUP**
   > 
   > The Python snippets by Workato connector does not require connection setup.
   
   Create a Workday connection.
   
   ### Create a Workday connection
   
   This step creates a connection between Workato and your Workday account.
   
   #### Before connecting to Workday
   
   Before integrating with Workday using third-party services like Workato, we recommend using an [Integration System User (ISU)](/en/connectors/workday#register-integration-system-user-isu-in-workday). Using an ISU ensures that all integration operations are logged under a designated user, separate from regular workflow processes. This is essential as changes to a regular worker’s security profile or their termination could disrupt integrations reliant on their account. For enhanced security, limit each ISU to a single integration system, such as Workato.
   
   Additionally, if your integration involves **custom objects** in Workday, you must register a Workday [API client](/en/connectors/workday#register-a-new-api-client-for-integrations). This step is required as the Workday REST API requires authentication through an OAuth client setup.
   
   #### Authentication requirements
   
   The Workday connector supports both OAuth 2.0 and basic authentication methods. However, OAuth 2.0 authentication is required for working with the Workday REST API and custom objects. We recommend that you avoid using the deprecated **Hybrid** authentication method.
   
   #### Connection setup using OAuth 2.0 authentication
   
   Complete the following steps to configure your Workday connection in Workato using OAuth 2.0 authentication:
   
   1. Enter a unique **Connection name** to identify your Workday account in Workato.
      
      ![Workday connection](/assets/workday-connection-setup-oauth.rU2iQ_Y6.png)_Label your connection_
      
   2. Choose **OAuth 2.0** as the **Authentication type**. This method is required for working with custom objects and for querying data using Workday Query Language (WQL) with the Workday REST API.
      
   3. Select the **Workday web services version** appropriate for your Workday tenant. We recommend choosing the newest version available for access to the latest features and updates.
      
   4. Locate and enter your **Tenant ID** from the URL when logged into Workday. For example, in `https://impl.workday.com/sample_company/d/home.htmld`, the tenant ID is `sample_company`.
      
   5. Provide the **WSDL URL** associated with your Workday services.
      
   6. Enter the **Client ID** and **Client Secret** from your API client settings.
      
   7. Optional. Input your **Refresh token** if you are using an API client for integrations.
      
   8. Enter your **Authorization endpoint** and **Token endpoint** from your API Client settings to complete the OAuth flow.
      
   9. Select the **Workday tenant timezone** that matches your Workday tenant's settings. By default, Workday uses Pacific Standard Time (PST).
      
   10. Optional. Click **Advanced settings** to configure the **Advanced XML payload for multiple ID values** field.
       
       Workato wraps each value in fields with multiple values within individual containers when constructing the XML from your input by default.
       
       For example:
       
       ```xml
       <languages><language>english</language></languages><languages><language>chinese</language></languages>
       ```
       
       Set the value to **Yes** to allow Workato to unwrap and present the values in a single container:
       
       ```xml
       <languages><language>english</language><language>chinese</language></languages>
       ```
       
       Consider setting this field to **Yes** if you encounter invalid payload errors.
       
   11. Review the information you entered to ensure it's correct.
       
   12. Click **Connect** to initiate the authorization process and complete the connection setup.
       
   
   #### Connection setup using basic authentication
   
   Complete the following steps to set up your Workday connection in Workato with basic authentication:
   
   1. Enter a unique **Connection name** to identify your Workday account in Workato.
      
      ![Workday connection](/assets/workday-connection-setup-basic-updated.B1rcozBp.png)_Label your connection_
      
   2. Select **Basic** as the **Authentication type**. This method uses your Workday username and password for integration.
      
   3. Select the **Workday web services version** appropriate for your Workday tenant. We recommend choosing the newest version available to access the latest features and updates.
      
   4. Locate and enter your **Tenant ID** from the URL when logged into Workday. For example, if your URL is `https://impl.workday.com/sample_company/d/home.htmld`, the tenant ID is `sample_company`.
      
   5. Provide the **WSDL URL** associated with your Workday services.
      
   6. Input your Workday **Login name** and **Password**.
      
   7. Select your **Workday tenant timezone** that matches your Workday tenant's settings. By default, Workday uses Pacific Standard Time (PST).
      
   8. Click **Advanced settings** to configure the **Advanced XML payload for multiple ID values** field. By default, fields with multiple values are wrapped within a container. Set this option to `yes` to unwrap the values.
      
   9. Review the information you entered to ensure it's correct.
      
   10. Click **Connect** to initiate the authorization process and complete the connection setup.
       
   
   Create a Google Drive connection.
   
   ### Create a Google Drive connection
   
   This step creates a connection between Workato and your Google Drive account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Google Drive` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Google Drive connection setup](/assets/connect.KZWFdVHS.png)_Google Drive_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu to select your authentication method. Options include **OAuth 2.0** and **Service account**.
      
   6. Optional. Expand **Advanced settings** to select permissions to request for the connection. By default, Workato requests the following permission:
      
      - See, edit, create, and delete all of your Google Drive files
   7. Optional. Use the **Custom OAuth profile** drop-down menu to select the custom OAuth profile you plan to use for this connection.
      
   8. Click **Sign in with Google**.
      
   9. Select the account you plan to use to connect to Workato.
      
   10. Review the requested permissions and click **Allow**.
       
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Run on a schedule**. This creates a new recipe with the Scheduler by Workato [New recurring event trigger](/en/features/scheduler/triggers/new-recurring-event). This trigger doesn't require a connection.
   
9. Set up your Scheduler by Workato New recurring event trigger.
   
   ### Set up Scheduler by Workato New recurring event trigger
   
   This trigger sets the interval for how frequently the recipe runs. The Scheduler by Workato trigger doesn't require connection setup.
   
   1. Click the trigger in the recipe editor.
      
      ![Click the trigger](/assets/click-trigger.Cxrovggz.png)_Click the trigger_
      
   2. Use the **Time unit** drop-down menu to select **Days**.
      
      - Available options include **Minutes**, **Hours**, **Days**, **Weeks**, **Months**, or **Custom schedule**.
   3. Enter `1` in the **Trigger every** field to run the recipe daily.
      
   4. Specify the time for the recipe to run in the **Trigger at** field. For example, enter `12:00 AM`.
      
   5. Optional. Select the timezone in the **Timezone** field. If left blank, the default is **America/Los\_Angeles**.
      
   6. Optional. Set the start date and time in the **Start after** field, or leave it blank to activate the trigger immediately after you start the recipe. You can't change this value after you run or test the recipe.
      
      ![Configure the trigger](/assets/trigger-config.B92l8JBt.png)_Configure the trigger_
      
   7. Click **Save**.
      
   
10. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
11. Set up your Workday Search business object batch action.
    
    ### Set up Workday Search business object batch action
    
    This step searches for workers in batches in Workday.
    
    1. Search for `Workday` and select it as your app.
       
       ![Choose Workday](/assets/choose.BYvxSHpz.png)_Choose Workday_
       
    2. Select the **Search business object (batch)** action.
       
       ![Select the Search business object action](/assets/search-business-object.BKn2ughN.png)_Select the Search business object action_
       
    3. Select the Workday connection you created in the preceding steps.
       
    4. Use the **Business object** drop-down menu to select **Workers**.
       
       ![Search for workers in Workday](/assets/business-object.DOU0WYdX.png)_Search for workers in Workday_
       
    5. Click **Save**.
       
    
12. Click **\+ Add step** and select **Action in app**.
    
13. Set up your Python snippets by Workato Execute code action.
    
    ### Set up Python snippets by Workato Execute code action
    
    This step takes the Search workers in Workday step output, which is in JSON format, and converts the output to CSV format using Python.
    
    1. Search for `Python snippets by Workato` and select it as your app. The **Execute code** action is selected automatically, as it is the only available action for this connector.
       
       ![Choose Python](/assets/choose.CYdjmB5Y.png)_Choose Python_
       
    2. Enter `Convert JSON to CSV` in the **Name** field to specify what this step does. This updates the action title in the recipe editor.
       
       ![Specify the step purpose](/assets/convert-json-to-csv.D6tZRxkm.png)_Specify the step purpose_
       
    3. Go to **Input fields** and click **Add field** to open the **Add new field** dialog.
       
       ![Add input field](/assets/add-input-field.B1FD4FOd.gif)_Add input field_
       
    4. Enter `JSON` in the **Label** field.
       
    5. Click **Add field**.
       
    6. Switch the **JSON** field to [formula mode](/en/formulas/formula-mode) and map the Workday Data (Step 2) list datapill. Mapping this list datapill requires the field to be in formula mode.
       
    7. Go to **Output fields** and click **Add field** to open the **Add new field** dialog.
       
    8. Enter `csv` in the **Label** field.
       
    9. Click **Add field**. This adds the **csv** field to the output schema:
       
       ![Add the CSV output field](/assets/csv-output-field.P7Qwagin.png)_Add the CSV output field_
       
    10. Clear the content in the **Code** field.
        
    11. Copy and paste the following Python code into the **Code** field:
        
        ```python
        # Import required libraries
        import pandas as pd
        import base64
        import io
        
        def main(input):
          # Normalize the JSON data to flatten nested structures into a flat table format
          normalized_json = pd.json_normalize(input['JSON'])
        
          # Remove the 'Worker_' prefix from all column names for cleaner headers
          normalized_json.columns = normalized_json.columns.str.replace('Worker_', '')
        
          # Drop any columns that contain 'Compensation_' in their name to exclude compensation data
          normalized_json = normalized_json[normalized_json.columns.drop(list(normalized_json.filter(regex='Compensation_')))]
        
          # Convert the modified DataFrame to CSV format as a string without the index column
          csv = normalized_json.to_csv(path_or_buf=None, index=False)
        
          # Return the CSV data as a dictionary output
          return { 'csv': csv }
        ```
        
        This code takes a JSON input, normalizes it into a flat table format, removes `Worker_` from the column names, excludes any columns containing `Compensation_`, and converts the resulting data into a CSV format. The code then returns the CSV content as a string.
        
    12. Click **Save**.
        
    
14. Click **\+ Add step** and select **Action in app**.
    
15. Set up your Google Drive Upload file action.
    
    ### Set up Google Drive Upload file action
    
    This step uploads the CSV output from the previous step to a folder you specify in Google Drive.
    
    1. Search for `Google Drive` and select it as your app.
       
       ![Choose Google Drive](/assets/choose.D8wbhGha.png)_Choose Google Drive_
       
    2. Select the **Upload file** action.
       
       ![Select the Upload file action](/assets/upload-file.D24b4T3I.png)_Select the Upload file action_
       
    3. Map the Python snippets by Workato Csv (Step 3) datapill to the **File contents** field.
       
       ![Map the Csv datapill](/assets/file-contents.BvAemKcZ.png)_Map the Csv (Step 3) datapill_
       
    4. Switch the **File name** field to [formula mode](/en/formulas/formula-mode) and enter the following:
       
       ```plaintext
       "Workday-flattened-#{today}.csv"
       ```
       
       This formula creates the name for the CSV file in the following format: `Workday-flattened-YYYY-MM-DD`.
       
       ![Configure the file name](/assets/file-name.BLbA5yoE.png)_Configure the file name_
       
    5. Use the **Parent folder** drop-down menu to select the folder where you plan to upload this file. This example selects a folder named **Workday-workers-flattened** as the parent folder.
       
    6. Click **Show optional fields** and select **Upload file MIME type**.
       
    7. Click **Apply changes** to show this field.
       
    8. Enter `text/csv` in the **Upload file MIME type** field.
       
       ![Specify the file type](/assets/upload-file-mime-type.BwDstDf7.png)_Specify the file type_
       
    9. Click **Save**.
       
    

Your **Export Workday workers to CSV with Python and upload to Google Drive** recipe is ready to test and implement.

Example recipe configuration.

![Workday, Python snippets by Workato, and Google Drive recipe](/assets/recipe.Dhg1wREg.png)_**Export Workday workers to CSV with Python and upload to Google Drive** recipe_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/greenhouse-box-servicenow-workbot.md
description: >-
  Create a recipe that automates offer letter generation, review, delivery, and
  initiates the onboarding process for new hires.
---

# Sync Greenhouse offer letter to Box and create onboarding request in ServiceNow recipe

This use case guides you through connecting [Greenhouse](/en/connectors/greenhouse), [Box](/en/connectors/box), [ServiceNow](/en/connectors/servicenow) and [Workbot for Slack](/en/workbot/workbot) to create a powerful automation.

## What does this recipe do?

This recipe monitors Greenhouse for new offers. When a new offer is created, Workbot for Slack sends a reminder to generate and send the offer letter to the candidate. Clicking **Generate and send** triggers a ServiceNow request for the IT team to start the candidate's onboarding process. It also creates a sign request in Box, sending the offer letter to a final copy reader for review and then to the candidate. Lastly, a ServiceNow requested item is generated to indicate the Box sign request has been initiated.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB
    subgraph GreenhouseTrigger[&nbsp Greenhouse New event trigger &nbsp]
      Trigger(Trigger) --- setup1(setup)
    end
    subgraph GetJob[&nbsp Greenhouse Get job by ID action &nbsp]
      Action1(Action) --- setup2(setup)
    end
    subgraph GetApplication[&nbsp Greenhouse Get application by ID action &nbsp]
      Action2(Action) --- setup3(setup)
    end
    subgraph GetCandidate[&nbsp Greenhouse Get candidate by ID action &nbsp]
      Action3(Action) --- setup4(setup)
    end
    subgraph Workbot[&nbsp Workbot for Slack Post message action &nbsp]
      Action4(Action) --- setup5(setup)
    end
    subgraph Request[&nbsp ServiceNow Create request action &nbsp]
      Action5(Action) --- setup6(setup)
    end
    subgraph SignRequest[&nbsp Box Create sign request action &nbsp]
      Action6(Action) --- setup7(setup)
    end
    subgraph RequestedItem[&nbsp ServiceNow Create requested item action &nbsp]
      Action7(Action) --- setup8(setup)
    end
  end
  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  GreenhouseTrigger --> GetJob --> GetApplication -->  GetCandidate --> Workbot --> Request --> SignRequest --> RequestedItem
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class CreateRecipe,Trigger,setup1,Action1,setup2,Action2,setup3,Action3,setup4,Action4,setup5,Action5,setup6,Action6,setup7,Action7,setup8,Workflow WorkatoTeal
  class GreenhouseTrigger,GetJob,GetApplication,GetCandidate,Workbot,Request,SignRequest,RequestedItem SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## Prerequisites

Before you begin, ensure you have the following:

- A Greenhouse [custom offer field](https://support.greenhouse.io/hc/en-us/articles/360024551831-Add-a-custom-offer-field) named **Annual salary**.
  
- A Box account with a Starter plan or higher. This is required to use sign templates.
  
- A Box sign template that includes the following [template tag](https://support.box.com/hc/en-us/articles/4404085855251-Creating-templates-using-tags) IDs:
  
  - `jobTitle`
  - `annualSalary`
  - `startDate`

These elements match the examples in this guide and will help you recreate the recipe step-by-step. However, you can modify them to fit your specific use case as needed.

## Create your recipe

Complete the following steps to create a recipe that automates offer letter generation, review, and delivery before initiating the onboarding process for new hires:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Greenhouse, Box, ServiceNow, and Workbot for Slack:
   
   Create a Greenhouse connection.
   
   ### Create a Greenhouse connection
   
   This step creates a connection between Workato and your Greenhouse account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Greenhouse` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Greenhouse connection setup](/assets/connect.BsUiOD6n.png)_Greenhouse connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter your API key in the **API key** field.
      
      Complete the following steps in Greenhouse to create your API key if you haven't already:
      
      1. Go to **Configure > Dev Center > API Credential Management**.
         
      2. Click **Create new API key**.
         
      3. Use the **API type** drop-down menu to select **Harvest**.
         
      4. Search for and select `Workato` in the **Partner** field.
         
      5. Enter a description for your API key in the **Description** field.
         
      6. Click **Manage permissions**.
         
      7. Click **Copy** to copy the API key.
         
      8. Click **I have stored the API key**.
         
      9. Keep the default permissions selected, or choose additional ones relevant to your use case in the **Manage permissions** section.
         
      10. Click **Save**.
          
   6. Enter the user email the API key is generated from in the **User email** field.
      
   7. Use the **Environment** drop-down menu to specify the environment instance you are connecting to. The default is **Production** if left blank.
      
   8. Click **Connect**.
      
   
   Create a Box connection.
   
   ### Create a Box connection
   
   This step creates a connection between Workato and your Box account.
   
   The Box connector supports both authorization code grant and [client credentials](/en/connectors/box#client-credentials) authentication.
   
   Complete the following steps to set up your Box connection using authorization code grant authentication:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Box` on the **New connection** page.
      
   3. Provide a name that identifies which Box instance Workato is connected to in the **Connection name** field.
      
      ![Box Connection 1](/assets/box_connection_1.OJ4XKoIg.png)_Create your connection_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store this connection.
      
   5. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
      
   6. Optional. Expand **Advanced settings** to select **Requested permissions (Oauth scopes)** options.
      
      You can select from the following scopes:
      
      - Read files and folders
      - Read and write files and folders
      - Manage app users
      - Manage managed users
      - Manage groups
      - Manage webhooks
      - Manage enterprise properties
      - Manage retention policies
      - Global content manager
      - Admin can make calls on behalf of users
      - Manage signature requests
      - Manage Box Relay
   7. Click **Connect**. This opens the Box sign in dialog.
      
   8. Enter your Box account email address and password.
      
      ![Box Connection 2](/assets/box_connection_2.DakkUsWJ.png)_Log in to Box_
      
   9. Click **Authorize**.
      
   10. Review the requested permissions and click **Grant access to Box**.
       
       ![Grant access to Box](/assets/grant-access.CygYC_9w.png)_Grant access to Box_
       
   
   Create a ServiceNow connection.
   
   ### Create a ServiceNow connection
   
   This step creates a connection between Workato and your ServiceNow account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `ServiceNow` on the **New connection** page.
      
   3. Enter a name for your ServiceNow connection in the **Connection name** field.
      
      ![ServiceNow connection setup](/assets/connect.LDELMjfR.png)_ServiceNow connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu to select **Username/Password**.
      
   6. Enter your ServiceNow **Instance name**. For example, if your ServiceNow URL is `https://acme.service-now.com`, the instance name is `acme`.
      
   7. Enter your ServiceNow username in the **Username** field.
      
   8. Enter your ServiceNow password in the **Password** field.
      
   9. Click **Connect**.
      
   
   The ServiceNow connector also supports [OAuth 2.0](/en/connectors/servicenow#oauth-2-0) and [Password grant](/en/connectors/servicenow#password-grant) authentication methods.
   
   Create a Workbot for Slack connection.
   
   ### Create a Workbot for Slack connection
   
   This step creates a connection between Workato and your Workbot for Slack account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Workbot for Slack` on the **New connection** page.
      
   3. Provide a name for your connection in the **Name** field.
      
      ![Workbot for Slack connection setup](/assets/connect.DudoV0Fs.png)_Workbot for Slack connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Optional. Select the NLU provider you plan to use, such as DialogFlow or Amazon Lex NLU. You must connect to the NLU provider for it to appear in the drop-down menu.
      
   6. Optional. Click **Advanced** to configure **Slash commands verification tokens**, **custom help** content, your **Slack app status** (classic or not), and your **Custom OAuth profile**.
      
   7. Click **Connect**, sign in to your Slack workspace when prompted, and click **Continue** to verify the connection.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your Greenhouse New event trigger.
    
    ### Set up Greenhouse New event trigger
    
    This trigger monitors new offers created in Greenhouse.
    
    1. Search for `Greenhouse` and select it as your app.
       
       ![Choose Greenhouse](/assets/choose.COciOsmA.png)_Choose Greenhouse_
       
    2. Select the **New event** trigger.
       
       ![Select the New event real-time trigger](/assets/new-event.BZy9c_ho.png)_Select the New event real-time trigger_
       
    3. Use the **Event category** drop-down menu to select **Offer**.
       
    4. Use the **Event** drop-down menu to select **Offer created**.
       
    5. Use a random string generator to create a secret key that's at least 32 characters long, and enter it in the **Secret key** field. Store this key in a secure location, as it's required to configure the webhook in Greenhouse.
       
       ![New offer created configuration](/assets/offer-created.BVPMH_iE.png)_New offer created configuration_
       
    6. Copy the webhook endpoint URL provided in the help section of the recipe editor. This value is also required to configure the webhook in Greenhouse.
       
       ![Copy the webhook endpoint URL](/assets/endpoint-url.BDWlwQsk.png)_Copy the webhook endpoint URL_
       
    7. Click **Save**.
       
    
11. Sign in to your Greenhouse instance to create a webhook that corresponds to the New event trigger.
    
    What is a webhook?
    
    ### Greenhouse webhook example
    
    A webhook is a notification sent by an application to a target URL in real-time when a specified event occurs. You can choose which events trigger these notifications.
    
    This use case requires a webhook in Greenhouse that sends data to Workato whenever an offer is created.
    
    ```mermaid
    flowchart TD
        A(Offer created in Greenhouse) -- The trigger activates --> B(Send webhook notification)
        B --> C(Workato receives notification)
        C --> D(Process offer data)
      classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
    classDef WorkatoPink fill:#f3c1c2,stroke:#f3c1c2,stroke-width:1px;
    ```
    
    Set up your Greenhouse webhook.
    
    ### Set up a Greenhouse webhook
    
    This webhook sends a notification to your Workato recipe each time an offer is created in Greenhouse.
    
    1. Go to **Configure > Dev Center > Webhooks > Webhooks**. The **Create a new webhook** page appears.
       
    2. Provide a name for your webhook in the **Name this webhook** field.
       
    3. Use the **When** drop-down menu to select **Offer created**. This field specifies the Greenhouse event that triggers the webhook.
       
    4. Paste the webhook endpoint URL from Workato into the **Endpoint URL** field.
       
    5. Enter the secret key you created when configuring the trigger in the **Secret key** field.
       
    6. Click **Create webhook**.
       
    
12. Click **\+ Add step**, then select **Handle errors**.
    
    ![Add an error handling step](/assets/handle-errors-standard.D9k1lANk.png)_Add an error handling step_
    
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
    
13. Click **Select an app and action**.
    
14. Set up your Greenhouse Get object (job) by ID action.
    
    ### Set up Greenhouse Get object (job) by ID action
    
    This step retrieves details about the job from Greenhouse.
    
    1. Search for `Greenhouse` and select it as your app.
       
       ![Choose Greenhouse](/assets/choose.COciOsmA.png)_Choose Greenhouse_
       
    2. Select the **Get object by ID** action.
       
       ![Select the Get object by ID action](/assets/get-object-by-id.C0P2RjCI.png)_Select the Get object by ID action_
       
    3. Use the **Object** drop-down menu to select **Job**.
       
    4. Map the Greenhouse Job ID (Step 1) datapill to the **Job ID** field.
       
       ![Configure the Get job by ID action](/assets/get-job-by-id-config.jlLjAuWA.png)_Configure the Get job by ID action_
       
    
15. Click **\+ Add step** and select **Action in app**.
    
16. Set up your Greenhouse Get object (application) by ID action.
    
    ### Set up Greenhouse Get object (application) by ID action
    
    This step retrieves details about the application from Greenhouse.
    
    1. Search for `Greenhouse` and select it as your app.
       
       ![Choose Greenhouse](/assets/choose.COciOsmA.png)_Choose Greenhouse_
       
    2. Select the **Get object by ID** action.
       
       ![Select the Get object by ID action](/assets/get-object-by-id.C0P2RjCI.png)_Select the Get object by ID action_
       
    3. Use the **Object** drop-down menu to select **Application**.
       
    4. Map the Greenhouse Application ID (Step 1) datapill to the **Application ID** field.
       
       ![Configure the Get application by ID action](/assets/get-application-by-id-config.DjL41dgi.png)_Configure the Get application by ID action_
       
    
17. Click **\+ Add step** and select **Action in app**.
    
18. Set up your Greenhouse Get object (candidate) by ID action.
    
    ### Set up Greenhouse Get object (candidate) by ID action
    
    This step retrieves details about the candidate from Greenhouse.
    
    1. Search for `Greenhouse` and select it as your app.
       
       ![Choose Greenhouse](/assets/choose.COciOsmA.png)_Choose Greenhouse_
       
    2. Select the **Get object by ID** action.
       
       ![Select the Get object by ID action](/assets/get-object-by-id.C0P2RjCI.png)_Select the Get object by ID action_
       
    3. Use the **Object** drop-down menu to select **Candidate**.
       
    4. Map the Greenhouse Candidate ID (Step 1) datapill to the **Candidate ID** field.
       
       ![Configure the Get candidate by ID action](/assets/get-candidate-by-id-config.BHn9Yb-M.png)_Configure the Get candidate by ID action_
       
    
19. Click the **•••** (ellipsis) next to the placeholder step (step 7) in the recipe editor and select **Delete**.
    
20. Click **\+ Add step** and select **Stop job**.
    
    How does the Stop control statement work?
    
    The [Stop control statement](/en/recipes/steps#stop-step) stops a single job from being processed further. Stop control statements are usually used in cases when there is an error in the business logic and further job processing is not required.
    
    The Stop statement can be configured to mark the job as failed or successful.
    
    ```mermaid
    flowchart TD
        B(Was an error found?)
        B -->|Yes| C(The job is stopped)
        B ---->|No| E(The recipe continues processing)
        classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
    ```
    
21. Set up your Stop control statement.
    
    ### Set up your Stop control statement
    
    This step stops and marks the job as failed if the recipe fails to retrieve details from Greenhouse.
    
    1. Use the **In job report, mark stopped job as** drop-down menu to select **Failed**.
       
    2. Enter the following text in the **Reason for failure** field:
       
       ```plaintext
       Failed to get details from Greenhouse.
       ```
       
       ![Configure the stop job step](/assets/stop-job-1-config.BtFf8rd_.png)_Configure the stop job step_
       
    
22. Click **\+ Add step** and select **Action in app**.
    
23. Set up your Workbot for Slack Post message action.
    
    ### Set up Workbot for Slack Post message action
    
    This step configures Workbot to post a reminder message in a designated Slack channel whenever a new offer is created in Greenhouse. The message includes the details about the candidate's full name, position, annual salary, start date, and a button. Clicking the button prompts the recipe to continue executing the actions that follow the **Post message** action.
    
    1. Search for `Workbot for Slack` and select it as your app.
       
       ![Choose Workbot for Slack](/assets/choose.6f8uKzDW.png)_Choose Workbot for Slack_
       
    2. Select the **Post message** action.
       
       ![Select the Post message action](/assets/post-message.CrJukgY-.png)_Select the Post message action_
       
    3. Use the **Reply channel** drop-down menu to select the Slack channel where Workbot will post the message.
       
    4. Locate the **Message** field and click **Add block to message**.
       
    5. Use the **Type** drop-down menu to select **Section with button (new version)**
       
    6. Enter the following text in the **Section text** field:
       
       ```plaintext
       Hi there :wave:
       It's time to send the offer letter to {FIRST_NAME} :tada:
       ```
       
       Replace `{FIRST_NAME}` with the Greenhouse First name (Step 5) datapill.
       
    7. Enter `Generate and send` in the **Button title** field.
       
    8. Ensure that **Continue recipe** is selected in the **Action to take on button-click** field.
       
    9. Use the **Button style** drop-down menu to select **Primary**.
       
    10. Locate the **Attachment fields** section and click **Add field**.
        
        Click **Show optional fields**, search for `Attachment fields`, select the **Title** and **Value** checkboxes, and then click **Apply changes** if the **Attachment fields** section isn't visible.
        
        ![Show attachment fields](/assets/show-attachment-fields.Cp0Dp586.png)_Show attachment fields_
        
    11. Enter `Full Name` in the **Title** field.
        
    12. Map the Greenhouse First name (Step 5) and Last name (Step 5) datapills to the **Value** field. Make sure to enter a space between the two datapills.
        
    13. Click **\+ Add field**.
        
    14. Enter `Position` in the **Title** field.
        
    15. Map the Greenhouse Job name (Step 3) datapill to the **Value** field.
        
    16. Click **\+ Add field**.
        
    17. Enter `Annual Salary` in the **Title** field.
        
    18. Switch the **Value** field to [formula mode](/en/formulas/formula-mode) and enter the following formula:
        
        ```ruby
        "$"+{ANNUAL_SALARY_VALUE}.reverse.scan(/\d{3}|.+/).join(",").reverse
        ```
        
        Replace `{ANNUAL_SALARY_VALUE}` with the Greenhouse Value (Step 1) datapill. The Value (Step 1) datapill is nested under the Annual salary object.
        
    19. Click **\+ Add field**.
        
    20. Enter `Start Date` in the **Title** field.
        
    21. Switch the **Value** field to [formula mode](/en/formulas/formula-mode) and enter the following formula:
        
        ```ruby
        {START_DATE}.strftime("%d %B %Y")
        ```
        
        Replace `{START_DATE}` with the Greenhouse Start date (Step 1) datapill.
        
    
    The following screenshot displays how the message appears in Slack:
    
    ![Example of how the message appears in Slack](/assets/message.Dy2iOfUl.png)_Example of how the message appears in Slack_
    
24. Click **\+ Add step** and select **Handle errors**.
    
25. Locate step 10 and click **Select an app and action**.
    
26. Set up your ServiceNow Create record (request) action.
    
    ### Set up ServiceNow Create record (request) action
    
    This step creates a new ServiceNow request for IT to initiate the onboarding process for the candidate.
    
    1. Search for `ServiceNow` and select it as your app.
       
       ![Choose ServiceNow](/assets/choose.CvUk6DVe.png)_Choose ServiceNow_
       
    2. Select the **Create record** action.
       
       ![Select the Create record action](/assets/create-record.CZqverB7.png)_Select the Create record action_
       
    3. Use the **Table** drop-down menu to select **Request**.
       
    4. Enter the following in the **Special instructions** field:
       
       ```plaintext
       This ticket is for IT to kickstart the onboarding process for {FIRST_NAME} {LAST_NAME}.
       ```
       
       Replace `{FIRST_NAME}` and `{LAST_NAME}` with the Greenhouse First name (Step 5) and Last name (Step 5) datapills.
       
    5. Switch the **Description** field to [formula mode](/en/formulas/formula-mode) and enter the following:
       
       ```plaintext
       "Details -" + "\n"
       "Full name -" + {FIRST_NAME} + " " + {LAST_NAME} + "\n"
       "Position - " + {JOB_NAME} + "\n" +
       "Annual Salary - " + "$" + {ANNUAL_SALARY_VALUE}.reverse.scan(/\d{3}|.+/).join(",").reverse + "\n" +
       "Start date - " + {START_DATE}.strftime("%d %B %Y") + "\n" +
       "IT, please onboard the new employee!"
       ```
       
       Replace the following placeholders with their corresponding datapill from Greenhouse:
       
       - `{FIRST_NAME}`: First name (Step 5)
       - `{LAST_NAME}`: Last name (Step 5)
       - `{JOB_NAME}`: Job name (Step 3)
       - `{ANNUAL_SALARY_VALUE}`: Value (Step 1) (from the Annual salary object)
       - `{START_DATE}`: Start date (Step 1)
    6. Enter the following in the **Short description** field:
       
       ```plaintext
       Onboard New Employee - {FIRST_NAME} {LAST_NAME}
       ```
       
       Replace `{FIRST_NAME}` and `{LAST_NAME}` with the Greenhouse First name (Step 5) and Last name (Step 5) datapills.
       
       ![Configure the new record values fields](/assets/new-record-values.BCwS27bq.png)_Configure the new record values fields_
       
    
27. Click **\+ Add step** and select **Action in app**.
    
28. Set up your Box Create sign request action.
    
    ### Set up Box Create sign request action
    
    This step creates and sends a Box sign request using an existing sign template. This step maps the data (job title, annual salary, and start date) from Greenhouse if your sign template uses prefill tags.
    
    1. Search for `Box` and select it as your app.
       
       ![Choose Box](/assets/choose.Cxg5AxoL.png)_Choose Box_
       
    2. Select the **Create sign request** action.
       
       ![Select the Create sign request action](/assets/create-sign-request.BzUYJERJ.png)_Select the Create sign request action_
       
    3. Enter the following in the **Name** field:
       
       ```plaintext
       Offer Sending for {FIRST_NAME} {LAST_NAME}
       ```
       
       Replace `{FIRST_NAME}` and `{LAST_NAME}` with the Greenhouse First name (Step 5) and Last name (Step 5) datapills.
       
    4. Select the sign template you plan to use from the **Sign template** drop-down menu.
       
    5. Expand the **Signers** section and click **Add Signer**.
       
    6. Use the **Role** drop-down menu to select **Final copy reader**.
       
    7. Enter the final copy reader's email in the **Email** field.
       
    8. Enter `1` in the **Order** field.
       
    9. Click **\+ Add Signer** to add a second signer.
       
    10. Use the **Role** drop-down menu to select **Signer**.
        
    11. Enter the signer's email in the **Email** field.
        
    12. Enter `2` in the **Order** field.
        
    13. Use the **Destination folder** drop-down menu to select the destination folder for the finalized, signed document and signing log.
        
    14. Locate the **Prefill tags** section and click **Add item**.
        
        If the **Prefill tags** section isn't visible, click **Show optional fields**, search for `Prefill tags`, select the **Document tag ID**, **Text value**, and **Date value** checkboxes, and then click **Apply changes**.
        
    15. Enter `jobTitle` in the **Document tag ID** field.
        
    16. Map the Greenhouse Job name (Step 3) datapill to the **Text value** field.
        
    17. Click **\+ Add item** to add a second prefill tag.
        
    18. Enter `annualSalary` in the **Document tag ID** field.
        
    19. Switch the **Text value** field to [formula mode](/en/formulas/formula-mode) and enter the following:
        
        ```ruby
        {ANNUAL_SALARY_VALUE}.reverse.scan(/\d{3}|.+/).join(",").reverse
        ```
        
        Replace `{ANNUAL_SALARY_VALUE}` with the Greenhouse Value (Step 1) datapill. The Value (Step 1) datapill is nested under the Annual salary object.
        
        ![Configure the text field](/assets/annual-salary.DrJCB7b-.gif)_Configure the text field_
        
    20. Click **\+ Add item** to add a third prefill tag.
        
    21. Enter `startDate` in the **Document tag ID** field.
        
    22. Map the Greenhouse Start date (Step 1) datapill to the **Date value** field.
        
    
29. Click **\+ Add step** and select **Action in app**.
    
30. Set up your ServiceNow Create record (requested item) action.
    
    ### Set up ServiceNow Create record (requested item) action
    
    This step creates a requested item in ServiceNow noting that a Box sign request was initiated.
    
    1. Search for `ServiceNow` and select it as your app.
       
       ![Choose ServiceNow](/assets/choose.CvUk6DVe.png)_Choose ServiceNow_
       
    2. Select the **Create record** action.
       
       ![Select the Create record action](/assets/create-record.CZqverB7.png)_Select the Create record action_
       
    3. Use the **Table** drop-down menu to select **Requested item**.
       
    4. Locate the **New record values** section.
       
       Click **Show optional fields**, select the **Request**, **Description**, and **Short description** checkboxes, and then click **Apply changes** if the **New record values** section isn't visible.
       
    5. Map the ServiceNow Number (Step 10) datapill to the **Request** field.
       
    6. Switch the **Description** field to [formula mode](/en/formulas/formula-mode) and enter the following:
       
       ```ruby
       "Box sign request initiated" + "\n" +
       "Sign ID - " + {ID}
       "Signers - " + {SIGNERS}.pluck('email')
       ```
       
       Replace `{ID}` and `{SIGNERS}` with the Box ID (Step 11) and Signers (Step 11) datapills.
       
    7. Enter `Box sign request initiated` in the **Short description** field.
       
       ![Configure the Create requested item action](/assets/create-requested-item-config.DDtgRVnw.png)_Configure the Create requested item action_
       
    
31. Click the **•••** (ellipsis) next to the placeholder step (step 14) in the recipe editor and select **Delete**.
    
32. Click **\+ Add step** and select **Stop job**.
    
33. Set up your second Stop control statement.
    
    ### Set up your second Stop control statement
    
    This step stops and marks the job as failed if the recipe fails to retrieve details from Greenhouse.
    
    1. Use the **In job report, mark stopped job as** drop-down menu to select **Failed**.
       
    2. Enter the following text in the **Reason for failure** field:
       
       ```plaintext
       Something went wrong when creating records in ServiceNow or sending the Box sign request.
       ```
       
       ![Configure the stop job step](/assets/stop-job-2-config.RRfrOAiN.png)_Configure the stop job step_
       
    
34. Click **Save**.
    

Your **Sync Greenhouse offer letter to Box and create onboarding request in ServiceNow** recipe is ready to test and implement.

Example recipe configuration.

![Greenhouse, Box, ServiceNow, and Workbot for Slack recipe](/assets/recipe.ClcnCG6D.png)_**Sync Greenhouse offer letter to Box and create onboarding request in ServiceNow** recipe_

---
