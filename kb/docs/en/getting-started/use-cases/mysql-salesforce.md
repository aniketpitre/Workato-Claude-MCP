---
url: 'https://docs.workato.com/en/getting-started/use-cases/mysql-salesforce.md'
description: >-
  Build a recipe that connects MySQL and Salesforce to sync and upsert records
  in batches, adaptable to contacts, accounts, leads, and more.
---

# Sync MySQL records to Salesforce in batches recipe

This use case guides you through connecting [MySQL](/en/connectors/mysql) and [Salesforce](/en/connectors/salesforce) to Workato to create a powerful automation.

## What does this recipe do?

This recipe syncs records from MySQL to Salesforce in batches. Specifically, this recipe demonstrates how to upsert contacts from MySQL to Salesforce. You can adapt this recipe for other Salesforce objects such as accounts, leads, opportunities, and more.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB
    subgraph MySQL[&nbsp MySQL New/updated rows batch trigger &nbsp]
      t1(Trigger) --- setup1[setup]
    end
    subgraph Salesforce[&nbsp Salesforce Upsert records in batches &nbsp]
      Action1(Action) --- setup2(setup)
    end
  end
  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  MySQL --> Salesforce
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class t1,setup1,setup2,Action1,CreateRecipe,Workflow WorkatoTeal
  class MySQL,Salesforce SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## How can I use this recipe?

This recipe can be applied in various ways to automate workflows, including but not limited to the following use cases:

- **User synchronization**: Seamlessly sync user records from MySQL to Salesforce, ensuring accurate and up-to-date information for all users.
- **Account management**: Automatically transfer customer data from MySQL to Salesforce as Accounts, maintaining consistency across platforms.
- **Opportunity tracking**: Sync opportunity details from MySQL to Salesforce, enabling sales teams to have access to the latest pipeline information.

## Create your recipe

Complete the following steps to create a recipe that syncs records from MySQL to Salesforce in batches.

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for MySQL and Salesforce:
   
   Create a MySQL connection.
   
   ### Create a MySQL connection
   
   This step creates a connection between Workato and your MySQL account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `MySQL` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![MySQL connection setup](/assets/connect.DHkSpWC1.png)_MySQL connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Connection type** drop-down menu to select the connection method you plan to use. You can select your [on-prem group](/en/on-prem/groups) name or select **Cloud** to use a direct connection.
      
   6. Enter the database host address in the **Host** field.
      
   7. Enter the port number your server runs on in the **Port** field. The default port number is `3306`.
      
   8. Enter the username to connect to MySQL in the **Username** field.
      
   9. Enter the password associated with your username in the **Password** field.
      
   10. Enter the name of the MySQL database you plan to connect to in the **Database** field.
       
   11. Optional. Expand **Advanced settings** to configure the following connection settings:
       
       1. Specify whether the MySQL connection should use improved datetime handling in the **Use improved datetime handling** field. The default is **Yes** for all new connections. This setting affects all actions that **insert rows** into MySQL.
          
       2. Select the local timezone of your database in the **Database timezone** field. When you provide a timezone for datetime values, Workato converts it to the specified timezone before insertion. The default is **UTC**.
          
          Refer to the [Improved datetime handling](/en/connectors/mysql#improved-datetime-handling) section for more information.
          
   12. Optional. Expand **SSL settings** to configure the following fields:
       
       1. Provide the X509 server certificate in `.pem` format in the **Server certificate** field.
          
       2. Provide the X509 client certificate in `.pem` format in the **SSL certificate** field.
          
       3. Provide the RSA client key in `.pem` format in the **SSL certificate key** field.
          
       4. Choose whether the client should trust any certificate chain in the **Trust all** field. Self-signed server certificates are supported.
          
       5. Choose whether to match the server certificate name with the domain name in the **Verify host** field.
          
   13. Click **Connect**.
       
   
   #### Permissions required to connect
   
   Your database user account must have at least `SELECT` permission for the database you plan to access.
   
   For example, to connect to a named database (`HR_PROD`) in a MySQL instance using a new database user `workato`, you can use the following queries:
   
   1. Create a new user dedicated to integration use cases with Workato:
      
      ```sql
      CREATE USER 'workato' IDENTIFIED BY 'password';
      ```
      
      This command creates a new user with login access to the MySQL instance. However, this user won't yet have access to any tables.
      
   2. Grant the user `SELECT` permission for all tables in `HR_PROD`:
      
      ```sql
      GRANT SELECT ON `HR_PROD`.* TO 'workato';
      ```
      
   3. Verify the user's permissions by running the following query:
      
      ```sql
      SHOW GRANTS FOR 'workato';
      ```
      
      The query returns the minimum permissions required to create a MySQL connection on Workato:
      
      ```sql
      +---------------------------------------------------------------------+
      | Grants for workato@%                                                |
      +---------------------------------------------------------------------+
      | GRANT USAGE ON *.* TO 'workato'@'%' IDENTIFIED BY PASSWORD <secret> |
      | GRANT SELECT ON `HR_PROD`.* TO 'workato'@'%'                        |
      +---------------------------------------------------------------------+
      2 rows in set (0.24 sec)
      ```
      
   
   Create a Salesforce connection.
   
   ### Create a Salesforce connection
   
   This step creates a connection between Workato and your Salesforce account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Salesforce` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Salesforce connection setup](/assets/connect.CnntY3nd.png)_Salesforce connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Auth type** drop-down menu to select the authentication method. The default is OAuth 2.0.
      
   6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
      
   7. Optional. Expand **Advanced settings** to configure advanced connection options.
      
   8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
      
      - This custom OAuth profile ensures that the connection is restricted to the same set of scopes you selected for all users with the profile, and the authentication flow uses the client app linked to the custom profile.
   9. Click **Connect**.
      
   10. Enter your Salesforce account credentials and click **Log In**.
       
       ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
       
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your MySQL New/updated rows batch trigger.
    
    ### Set up MySQL New/updated rows batch trigger
    
    This step detects new or updated rows in batches in your MySQL database.
    
    1. Search for `MySQL` and select it as your app.
       
       ![Choose an app](/assets/choose.Bq-Uns8g.png)_Choose MySQL as your app_
       
    2. Select the **New/updated rows** batch trigger.
       
       ![Select the New/updated rows batch trigger](/assets/new-updated-rows.BTUHuYVX.png)_Select the New/updated rows batch trigger_
       
    3. Select the MySQL connection you created in the preceding steps.
       
    4. Optional. Specify how frequently this trigger should check for new events in the **Trigger poll interval** field. This field defaults to five minutes if left blank.
       
    5. Select the table you plan to monitor for new or updated rows in the **Table** drop-down menu.
       
       This example monitors a table named `contacts` for new or updated rows.
       
       ![Select your MySQL table in the Table field](/assets/table.Du6YVOk4.png)_Select your MySQL table in the Table field_
       
    6. Select a unique key column to filter out duplicate rows in the **Unique key** field. This column should be unique and auto-incrementing to ensure that no trigger events are missed.
       
       This example uses a column named `id` as the unique key.
       
       ![Select your unique key](/assets/unique-key.DmonOGGT.png)_Select your unique key_
       
    7. Select a column to identify updated rows in the **Sort column**. Only timestamp columns can be used as a sort column.
       
       This example selects a column named `last_updated` for this field.
       
       ![Select the sort column](/assets/sort-column.9vWowHty.png)_Select the sort column_
       
       This MySQL column has the `TIMESTAMP` data type and is automatically updated with the current date and time whenever the row is modified. Refer to [MySQL's documentation on `TIMESTAMP` and `DATETIME`](https://dev.mysql.com/doc/refman/8.0/en/timestamp-initialization.html) for more information.
       
    8. Select the size of the returned events batch in the **Batch size** field. The minimum is `1` and the maximum is `100`. The default is `100`.
       
    9. Optional. Choose columns to be returned from the selected table in the **Output columns** field. Leave this field blank to return all columns.
       
    10. Optional. Specify a condition to filter new rows in the **WHERE condition** field.
        
    11. Click **Save**.
        
    
11. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Add action_
    
12. Set up your Salesforce Upsert records in batches action.
    
    ### Set up Salesforce Upsert records in batches action
    
    This step updates or inserts records in batches in Salesforce if there is a new or updated record in the MySQL table. This action upserts **Contact** records from MySQL into Salesforce in this use case.
    
    1. Search for `Salesforce` and select it as your app.
       
       ![Choose an app](/assets/choose.K4EwwvB5.png)_Choose Salesforce as your app_
       
    2. Select the **Upsert records in batches** action.
       
       ![Select the Upsert records in batches action](/assets/upsert-records-in-batches.DMwDFjLF.png)_Select the Upsert records in batches action_
       
    3. Select the Salesforce connection you created in the preceding steps.
       
    4. Select the Salesforce object you plan to upsert in the **Object** field.
       
       This example uses the **Contact** object.
       
       ![Select the Salesforce object to upsert](/assets/object.BQUWQYTz.png)_Select the Salesforce object to upsert_
       
    5. Optional. Enter the number of records to be processed in a batch in the **Batch size** field. The minimum is `1` and the maximum is `200`. The default is `200`.
       
    6. Select the external unique identifier to upsert your record in the **Primary key** field.
       
       This example uses a primary key named `MySQL ID`.
       
       ![Select your primary key](/assets/primary-key.DwG8xL9n.png)_Select your primary key_
       
       Refer to our Salesforce connector documentation to learn how to [create a primary key](/en/connectors/salesforce/batch-operations#create-a-primary-key).
       
    7. Optional. Use the **Relationship fields** drop-down menu to select relationship fields to include in the upsert. Refer to our [Salesforce object relationships](/en/connectors/salesforce/related-objects) documentation for more information.
       
    8. Expand **Contacts** to configure additional settings. The name of this field and the following fields vary depending on your selected object.
       
    9. Map the Rows (Step 1) list datapill to the **Contacts source list**. Learn more about [list input](/en/features/list-management#list-batch-action).
       
       ![Map the Rows datapill](/assets/contacts-source-list.DO8AtVJO.png)_Map the Rows (Step 1) datapill_
       
    10. Click **Show optional fields** to select the fields you plan to map from your MySQL table to Salesforce.
        
        ![Show optional fields](/assets/show-optional-fields.BdruvmBG.png)_Show optional fields_
        
        This example selects fields corresponding to the records in the `contacts` MySQL table:
        
        - Business Phone
        - Email
        - First Name
        - Last Name
        - Title
    11. Map the datapills corresponding to your MySQL table to the fields in the **Contact fields** section.
        
        ![Map the output datapills to the Contact fields section](/assets/map-contacts-fields.CMlkRbfT.gif)_Map the output datapills to the Contact fields section_
        
    12. Map the datapill associated with the MySQL column you selected as your **Unique key** (Step 1) to the field corresponding to your Salesforce **Primary key**.
        
        This example maps the id (Step 1) datapill to the **MySQL ID** field, which is the name of the primary key created in Salesforce.
        
        ![Map the id datapill](/assets/mysql-id.F2kukHyT.png)_Map the id (Step 1) datapill_
        
    13. Optional. Expand **Advanced configuration** to configure the following setting:
        
        - **Roll back records when errors occur?**: Choose whether the batch should roll back records if an object upsert fails. If the batch is larger than 200 records, only the affected batch is rolled back. We recommend using the default **No** setting.
    14. Click **Save**.
        
    

Your **Sync MySQL records to Salesforce in batches** recipe is ready to test and implement.

Example recipe configuration.

![MySQL and Salesforce recipe](/assets/recipe.CEJIKca0.png)_**Sync MySQL records to Salesforce in batches** recipe_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/salesforce-js-snippets-snowflake-email.md
description: >-
  Build a recipe that connects Salesforce, JavaScript snippets, Snowflake, and
  Email to validate contacts and upsert valid records.
---

# Validate Salesforce contact information with JavaScript and upsert to Snowflake recipe

This use case guides you through connecting [Salesforce](/en/connectors/salesforce), [JavaScript snippets by Workato](/en/connectors/javascript), [Snowflake](/en/connectors/snowflake), and [Email by Workato](/en/connectors/email-by-workato) to create a powerful automation.

## What does this recipe do?

This recipe retrieves new Salesforce contacts in batches, validates each phone number using JavaScript, and upserts the valid contacts into a Snowflake table. Contacts with invalid phone numbers are excluded from the upsert, and the recipe sends an email listing these invalid contacts.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB

    subgraph Salesforce[&nbsp Salesforce New records batch trigger &nbsp]
      t1(Trigger) --- setup1(setup)
    end

    subgraph JavaScript[&nbsp JavaScript snippets by Workato Execute code action &nbsp]
      Action1(Action) --- setup2(setup)
    end

    subgraph Snowflake[&nbsp Snowflake Replicate rows batch action &nbsp]
      Action2(Action) --- setup3(setup)
    end

    subgraph Email[&nbsp Email by Workato Send email action &nbsp]
      Action3(Action) --- setup5(setup)
    end
  end

  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  Salesforce --> JavaScript --> Snowflake --> Email

  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class t1,setup1,setup2,setup3,setup4,setup5,Action1,Action2,Action3,x,xx,CreateRecipe,Workflow WorkatoTeal
  class Salesforce,JavaScript,Snowflake,Email SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## Create your recipe

Complete the following steps to create a recipe that retrieves new Salesforce contacts in batches, validates each phone number using JavaScript, and inserts or updates rows in a Snowflake table:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Salesforce and Snowflake:
   
   > **WORKATO UTILITY CONNECTORS DON'T REQUIRE SETUP**
   > 
   > The JavaScript snippets by Workato and Email by Workato connectors do not require connection setup.
   
   Create a Salesforce connection.
   
   ### Create a Salesforce connection
   
   This step creates a connection between Workato and your Salesforce account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Salesforce` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Salesforce connection setup](/assets/connect.CnntY3nd.png)_Salesforce connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Auth type** drop-down menu to select the authentication method. The default is OAuth 2.0.
      
   6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
      
   7. Optional. Expand **Advanced settings** to configure advanced connection options.
      
   8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
      
      - This custom OAuth profile ensures that the connection is restricted to the same set of scopes you selected for all users with the profile, and the authentication flow uses the client app linked to the custom profile.
   9. Click **Connect**.
      
   10. Enter your Salesforce account credentials and click **Log In**.
       
       ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
       
   
   Create a Snowflake connection.
   
   ### Create a Snowflake connection
   
   This step creates a connection between Workato and your Snowflake account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Snowflake` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Snowflake connection setup](/assets/connect.C_-ABP8L.png)_Snowflake connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter your account identifier in the **Account identifier** field. Snowflake has multiple methods of identifying an account. Workato supports all methods:
      
      - Account name: `https://{org.name}-{account_name}`
      - Connection name: `https://{org.name}-{connectionname}`
      - Account locator: `https://{account.locator}.{region}.{cloud}`
      
      If you're using the account locator, note that `{region}` and `{cloud}` are only required for certain locations. For example:
      
      - If your account is hosted in AWS US West (Oregon), use `your-account-locator`.
      - If your account is hosted in AWS US East (Ohio), use `your-account-locator.us-east-2`.
      - If your account is hosted in Azure West Europe, use `your-account-locator.west-europe.azure`.
   6. Enter the full name of the warehouse where you plan to perform all operations for this connection in the **Warehouse** field. For example, `compute_wh`.
      
   7. Enter the database you plan to use in your recipe connection in the **Database name** field.
      
   8. Use the **Authentication type** drop-down menu to select your authentication type.
      
      - **Username/Password**: Enter your username and password if you select this option.
      - **OAuth 2.0**: Enter your Client ID and Client Secret if you select this option.
   9. Click **Connect**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your Salesforce New records batch trigger.
    
    ### Set up Salesforce New records batch trigger
    
    This trigger monitors Salesforce daily for new contact records and retrieves specific fields when new contacts are found.
    
    1. Search for `Salesforce` and select it as your app.
       
       ![Choose Salesforce](/assets/choose.K4EwwvB5.png)_Choose Salesforce_
       
    2. Select the **New records** trigger.
       
       ![Select the New records batch trigger](/assets/new-records.DelQsogP.png)_Select the New records batch trigger_
       
    3. Select the Salesforce connection you created in the preceding steps.
       
    4. Use the **Object** drop-down menu to select **Contact** as the Salesforce object you plan to monitor for new records.
       
    5. Optional. Use the **Fields to retrieve** drop-down menu to specify the fields you plan to retrieve. This example selects the following fields:
       
       - Contact ID
       - Account ID
       - Last Name
       - First Name
       - Business Phone
       - Email
       
       ![Specify the fields you plan to retrieve](/assets/fields-to-retrieve.BQ7ZjMbH.png)_Specify the fields you plan to retrieve_
       
    6. Enter the batch size in the **Batch size** field. The default is `100`, and the maximum is `2000` records per batch.
       
    7. Optional. Click **Show optional fields**, select **Trigger poll interval**, and click **Apply changes**.
       
       ![Configure the Trigger poll interval](/assets/trigger-poll-interval.DhYmd1U7.gif)_Configure the Trigger poll interval_
       
    8. Optional. Use the **Trigger poll interval** drop-down menu to specify how frequently this recipe should check for new contacts in Salesforce. This example selects **1 day**.
       
    9. Click **Save**.
       
    
11. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
12. Set up your JavaScript snippets by Workato Execute code action.
    
    ### Set up JavaScript snippets by Workato Execute code action
    
    This step validates contacts by checking if each record contains a valid phone number. This action returns the following output fields: `val_contacts` (list of valid contacts), `bad_contacts` (list of invalid contacts), and `log`. The log message varies based on whether all Salesforce contacts in the batch are valid or if any have invalid phone numbers.
    
    1. Search for `JavaScript snippets by Workato` and select it as your app.
       
       ![Choose JavaScript snippets by Workato](/assets/choose.WxJcqdMq.png)_Choose JavaScript snippets by Workato_
       
    2. Select the **Execute code** action.
       
       ![Select the Execute code action](/assets/execute-code.Dc4NApYy.png)_Select the Execute code action_
       
    3. Enter `Validate contacts` in the **Name** field. This changes the action name in the recipe editor.
       
       ![Configure the Name field](/assets/name.dKCyNrmx.png)_Configure the Name field_
       
    4. Go to **Input fields** and select **Add field**.
       
       1. Enter `contacts` in the **Name** field.
          
       2. Click **Add field**.
          
          ![Select the Execute code action](/assets/input-fields.e4lWvbzD.png)_Select the Execute code action_
          
    5. Switch the **Contacts** field to [formula mode](/en/formulas/formula-mode).
       
    6. Map the Salesforce Contacts (Step 1) list datapill to the **Contacts** field. You can't map this datapill unless the **Contacts** field is switched to formula mode.
       
       ![Map the Contacts datapill](/assets/map-contacts.B7p-FD3c.gif)_Map the Contacts (Step 1) datapill_
       
    7. Go to **Output fields** and create a placeholder field.
       
    8. Click **Edit schema**.
       
    9. Copy and paste the following JSON schema to replace the existing schema:
       
       ```json
       [
         {
           "name": "val_contacts",
           "type": "array",
           "of": "object",
           "label": "Val contacts",
           "properties": [
             {
               "properties": [
                 {
                   "control_type": "text",
                   "label": "Type",
                   "type": "string",
                   "name": "type"
                 },
                 {
                   "control_type": "text",
                   "label": "URL",
                   "type": "string",
                   "name": "url"
                 }
               ],
               "label": "Attributes",
               "type": "object",
               "name": "attributes"
             },
             {
               "control_type": "text",
               "label": "Account ID",
               "type": "string",
               "name": "AccountId"
             },
             {
               "control_type": "text",
               "label": "Phone",
               "type": "string",
               "name": "Phone"
             },
             {
               "control_type": "text",
               "label": "ID",
               "type": "string",
               "name": "Id"
             },
             {
               "control_type": "text",
               "label": "Email",
               "type": "string",
               "name": "Email"
             },
             {
               "control_type": "text",
               "label": "First name",
               "type": "string",
               "name": "FirstName"
             },
             {
               "control_type": "text",
               "label": "Last name",
               "type": "string",
               "name": "LastName"
             },
             {
               "control_type": "text",
               "label": "Valid",
               "render_input": {},
               "parse_output": {},
               "toggle_hint": "Select from option list",
               "toggle_field": {
                 "label": "Valid",
                 "control_type": "text",
                 "toggle_hint": "Use custom value",
                 "type": "boolean",
                 "name": "valid"
               },
               "type": "boolean",
               "name": "valid"
             }
           ]
         },
         {
           "name": "bad_contacts",
           "type": "array",
           "of": "object",
           "label": "Bad contacts",
           "properties": [
             {
               "properties": [
                 {
                   "control_type": "text",
                   "label": "Type",
                   "type": "string",
                   "name": "type"
                 },
                 {
                   "control_type": "text",
                   "label": "URL",
                   "type": "string",
                   "name": "url"
                 }
               ],
               "label": "Attributes",
               "type": "object",
               "name": "attributes"
             },
             {
               "control_type": "text",
               "label": "Account ID",
               "type": "string",
               "name": "AccountId"
             },
             {
               "control_type": "text",
               "label": "Phone",
               "type": "string",
               "name": "Phone"
             },
             {
               "control_type": "text",
               "label": "ID",
               "type": "string",
               "name": "Id"
             },
             {
               "control_type": "text",
               "label": "Email",
               "type": "string",
               "name": "Email"
             },
             {
               "control_type": "text",
               "label": "First name",
               "type": "string",
               "name": "FirstName"
             },
             {
               "control_type": "text",
               "label": "Last name",
               "type": "string",
               "name": "LastName"
             },
             {
               "control_type": "text",
               "label": "Valid",
               "render_input": {},
               "parse_output": {},
               "toggle_hint": "Select from option list",
               "toggle_field": {
                 "label": "Valid",
                 "control_type": "text",
                 "toggle_hint": "Use custom value",
                 "type": "boolean",
                 "name": "valid"
               },
               "type": "boolean",
               "name": "valid"
             }
           ]
         },
         {
           "control_type": "text",
           "label": "Log",
           "type": "string",
           "name": "log"
         }
       ]
       ```
       
    10. Click **Update** to apply the new JSON schema. You can scroll through the listings under **Output fields** to see the newly applied schema output:
        
        ![Output fields](/assets/output-fields.DB4_kMoa.gif)_Output fields_
        
        You can modify this schema based on the fields you plan to retrieve from Salesforce and upsert into Snowflake.
        
    11. Clear the contents of the **Code** field.
        
    12. Copy and paste the following JavaScript code into the **Code** field:
        
        ```javascript
        const _ = require("lodash");
        
        class ContactValidator {
          static validContact = (phone) => {
            return this.validPhoneNumber(phone);
          };
        
          static validPhoneNumber = (phone) => {
            let phone_regex = /^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$/;
            return phone ? phone_regex.test(phone) : false;
          };
        
          static validate = function(contacts) {
            const bad_contacts = [];
            const val_contacts = _.filter(contacts, (contact) => {
              let phone = _.get(contact, 'Phone');
              const isValid = this.validContact(phone);
              contact['valid'] = isValid;
        
              if (!isValid) {
                bad_contacts.push(contact); // Add invalid contact to the array
                return false;  // Don't include invalid contacts in val_contacts
              }
              return true;  // Include only valid contacts in val_contacts
            });
        
            // Create a log message based on the bad contacts
            const logMessage = bad_contacts.length > 0
              ? `The following contacts were not replicated due to invalid phone numbers: ${bad_contacts.map(c => `${c.FirstName} ${c.LastName} (${c.Phone})`).join(', ')}`
              : 'All contacts were valid and successfully replicated.';
        
            return { val_contacts, bad_contacts, log: logMessage };
          };
        }
        
        exports.main = ({ contacts }) => {
          return ContactValidator.validate(contacts);
        };
        ```
        
    13. Click **Save**.
        
    
13. Click **\+ Add step** and select **Action in app**.
    
14. Set up your Snowflake Replicate rows batch action.
    
    ### Set up Snowflake Replicate rows batch action
    
    This step inserts or updates the records from the valid contacts list into the Snowflake table.
    
    1. Search for `Snowflake` and select it as your app.
       
       ![Choose Snowflake](/assets/choose.IV_92BfS.png)_Choose Snowflake_
       
    2. Select the **Replicate rows** action.
       
       ![Select the Replicate rows batch action](/assets/replicate-rows.pqmE2raP.png)_Select the Replicate rows batch action_
       
    3. Select the Snowflake connection you created in the preceding steps.
       
    4. Use the **Table** drop-down menu to select the Snowflake table where you plan to replicate rows.
       
    5. Ensure that the **Rows** field is switched to [formula mode](/en/formulas/formula-mode) and map the JavaScript snippets by Workato Val contacts (Step 2) datapill.
       
       ![Map the Val contacts datapill](/assets/map-val-contacts.Cli8juQJ.gif)_Map the Val contacts (Step 2) datapill_
       
    6. Use the **Flatten columns** drop-down menu to select **Yes**.
       
    7. Enter `1` in the **Flatten level** field.
       
    8. Use the **Unique keys** drop-down menu to select one or more unique keys to identify duplicate rows. This example selects **ID** (contact ID) as the unique key.
       
       ![Select the unique key](/assets/unique-keys.DqZdOIpk.png)_Select the unique key_
       
    9. Optional. Use the **Exclude columns** drop-down menu to select the columns to exclude while replicating rows. This example selects **Attributes** and **Valid**.
       
       ![Select the columns to exclude from the upsert](/assets/exclude-columns.DLWzi3hT.png)_Select the columns to exclude from the upsert_
       
    10. Click **Save**.
        
    
15. Click **\+ Add step** and select **IF condition**.
    
    ![Add IF condition](/assets/if-condition-standard.DI59XkdU.png)_Click **Add step > IF condition**_
    
    How do IF conditions work?
    
    ### Snowflake and Salesforce IF condition example
    
    An [IF condition](/en/features/if-conditions) enables you to make decisions based on specific conditions. You can control your recipe workflow by executing different actions depending on whether a condition you specify is true or false.
    
    ```mermaid
    flowchart TD
        A([Replicate valid Salesforce contact rows to Snowflake]) --> B(Were there any invalid contacts?)
        B -->|Yes| C(Send an email detailing the contacts with invalid phone numbers)
        B ---->|No| E(No action required)

        classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
        classDef WorkatoPink fill:#f3c1c2,stroke:#f3c1c2,stroke-width:1px;
        class E WorkatoPink
    ```
    
16. Set up your JavaScript snippets by Workato and Salesforce IF condition.
    
    ### Set up a JavaScript snippets by Workato and Salesforce IF condition
    
    This step checks if the bad contacts list size is greater than zero. This means that the batch contains one or more contacts with invalid phone numbers if this condition is true.
    
    1. Switch **Data field** to formula mode.
       
    2. Map the JavaScript snippets by Workato Bad contacts (Step 2) datapill to **Data field**.
       
    3. Append the [`.length` formula](/en/formulas/array-list-formulas#length).
       
    4. Use the **Condition** drop-down menu to select **greater than**.
       
    5. Switch the **Value** field to formula mode and enter `0`.
       
       ![Configure the IF condition](/assets/if-condition.CkVAg5IY.png)_Configure the IF condition_
       
    6. Click **Save**.
       
    
17. Click **Select an app and action**.
    
18. Set up your Email by Workato Send email action.
    
    ### Set up Email by Workato Send email action
    
    Workato sends an email to a recipient you specify detailing which Salesforce contacts weren't replicated into Snowflake due to invalid phone numbers if the bad contacts list size is greater than zero.
    
    1. Search for `Email by Workato` and select it as your app.
       
       ![Choose Email by Workato](/assets/choose.6AqK7Iz4.png)_Choose Email by Workato_
       
    2. Select the **Send email** action.
       
       ![Select the Send email action](/assets/send-email.YYuGiZJJ.png)_Select the Send email action_
       
    3. Provide the recipient's email address in the **To** field.
       
    4. Enter a subject line in the **Subject** field. For example, `Salesforce Contacts Not Replicated into Snowflake Due to Invalid Data`
       
    5. Use the **Email type** drop-down menu to select **Text**.
       
    6. Map the JavaScript snippets by Workato Log (Step 2) datapill to the **Message** field.
       
       ![Configure the message](/assets/message.CD0630Vn.png)_Configure the message_
       
    7. Click **Save**.
       
    

Your **Validate Salesforce contact information with JavaScript and upsert to Snowflake** recipe is ready to test and implement.

Example recipe configuration.

![Salesforce, JavaScript snippets by Workato, Snowflake, and Email by Workato recipe](/assets/recipe.D-8dRGYA.png)_**Validate Salesforce contact information with JavaScript and upsert to Snowflake** recipe_

---
