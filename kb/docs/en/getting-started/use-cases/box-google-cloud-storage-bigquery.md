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
