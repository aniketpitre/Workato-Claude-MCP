---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-oracle-fusion.md
description: >-
  Configure Oracle Fusion Cloud as a data pipeline source to extract data in
  bulk through BICC and sync it to your destination.
---

# Configure Oracle Fusion Cloud as your data pipeline source

Set up Oracle Fusion Cloud as a data pipeline source to extract and sync records into your destination. This guide covers connection setup, pipeline configuration, and key behavior when using Oracle Fusion Cloud as a source.

## Oracle Fusion Cloud prerequisites

Ensure you have the following configuration before creating the connection:

- Access to an Oracle Fusion Cloud instance
- Valid Oracle Fusion Cloud user credentials
- Required permissions to access the objects used in the pipeline

## Sync overview

The Oracle Fusion Cloud connector uses [Oracle Business Intelligence Cloud Connector](https://docs.oracle.com/en/cloud/saas/applications-common/26b/biacc/overview-of-business-intelligence-cloud-connector.html) (BICC) to extract data in bulk from Oracle Fusion Cloud applications. BICC enables the connector to retrieve business intelligence and other data from your Oracle Fusion Cloud instance and load it into your designated destination.

## Oracle Fusion Cloud features supported

The following features are supported when using Oracle Fusion Cloud as a data pipeline source:

- Extract data from Oracle Fusion Cloud modules
- Support for full and incremental sync (where supported)
- Field-level selection for object extraction
- Schema drift detection and handling
- Field-level data masking

## API version

The Oracle Fusion Cloud connector uses the [ERP Integrations REST API v11.13.18.05](https://docs.oracle.com/en/cloud/saas/applications-common/24a/farca/api-set-id-sets-set-id-sets-11.13.18.05.html) and [Oracle UCM Web Services](https://docs.oracle.com/cd/E14571_01/doc.1111/e10807/web_services002.htm) (SOAP) for DTU (Data Transfer Utility) downloads.

## How to connect

Complete the following steps to create an Oracle Fusion Cloud connection:

Connect to Oracle Fusion Cloud

The Oracle Fusion Cloud connector supports the following authentication methods:

- [Basic](#basic)
- [JWT token](#jwt-token)

### Basic

Complete the following steps to connect to Oracle Fusion Cloud using basic authentication:

1. Sign in to Workato.
   
2. Select the project where you plan to store the connection.
   
3. Select **Create > Connection** or press C twice.
   
4. Search for `Oracle Fusion Cloud` and select it as your app.
   
5. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Oracle Fusion Cloud (basic authentication)](/assets/basic.C_sNovQ1.png)_Connect to Oracle Fusion Cloud (basic authentication)_
   
6. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
7. Use the **Auth type** drop-down menu to select **Basic**.
   
8. Enter the username for your Oracle Fusion Cloud account in the **Username** field.
   
9. Enter the password for your Oracle Fusion Cloud account in the **Password** field.
   
10. Enter the subdomain of your specific Oracle Fusion Cloud instance in the **Subdomain** field. For example, `servername.fa.us2.oraclecloud.com`.
    
11. Click **Connect**.
    

### JWT token

The following items are required to connect to Oracle Fusion Cloud using JWT token authentication:

- [Generate a X.509 key pair](#generate-a-x-509-key-pair)
- [Retrieve the certificate fingerprint](#retrieve-the-certificate-fingerprint)
- [Configure token-based authentication in Oracle Fusion Cloud](#configure-token-based-authentication-in-oracle-fusion-cloud)
- [Complete setup in Workato](#complete-setup-in-workato)

You can also refer to the Oracle [Configure JWT Authentication Provider](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fusionapps/HCM/JWT_API_Authentication_OBE/html/index.html#GenerateaX.509KeyPair) tutorial for more information about this process.

#### Generate a X.509 key pair

X.509 key pairs are used to establish secure communication by verifying the authenticity of the public certificate.

Complete the following steps to generate a X.509 key pair:

> **ENVIRONMENT REQUIREMENT**
> 
> These steps use `openssl`.
> 
> - Mac and Linux include OpenSSL by default
> - Windows doesn't include OpenSSL by default. Install OpenSSL or run these commands using tools such as Git Bash or WSL (Windows Subsystem for Linux).

1. Open a new terminal window.
   
2. Run the following command to generate a private key:
   
   ```shell
   openssl genrsa -out private.key 2048
   ```
   
   This command creates a 2048-bit RSA private key and saves it to `private.key`.
   
3. Run the following command to generate an X.509 certificate containing the public key:
   
   ```shell
   openssl req -new -x509 -key private.key -out publickey.cer -days 365
   ```
   
   This command generates a self-signed X.509 certificate (`publickey.cer`) valid for 365 days.
   
4. Open the `private.key` file in a text editor and copy the contents, starting from `-----BEGIN RSA PRIVATE KEY-----` and ending with `-----END RSA PRIVATE KEY-----`.
   
   Store this key securely for later use in [complete setup in Workato](#complete-setup-in-workato).
   

#### Retrieve the certificate fingerprint

The certificate fingerprint is a unique identifier used to verify the authenticity of a certificate.

Complete the following steps to retrieve the certificate fingerprint:

> **ENVIRONMENT REQUIREMENT**
> 
> These steps use `openssl`.
> 
> - Mac and Linux include OpenSSL by default
> - Windows doesn't include OpenSSL by default. Install OpenSSL or run these commands using tools such as Git Bash or WSL (Windows Subsystem for Linux).

1. Run the following `openssl` command to generate the x5t value from the `publickey.cer` file:
   
   ```shell
   openssl x509 -sha1 -in publickey.cer -noout -fingerprint
   ```
   
   The fingerprint output is in hexadecimal format:
   
   ```plaintext
   Fingerprint=00:6D:6F:4A:5F:36:71:10:24:F8:F0:FD:33:89:6D:C5:EB:92:00:0F
   ```
   
2. Convert the fingerprint to base64 format. Replace the string with your actual certificate fingerprint:
   
   ```shell
   echo "00:6D:6F:4A:5F:36:71:10:24:F8:F0:FD:33:89:6D:C5:EB:92:00:0F" | xxd -r -p | base64
   ```
   
   The fingerprint output is in base64 format:
   
   ```plaintext
   AG1vSl82cRAk+PD9M4ltxeuSAA8=
   ```
   
3. Copy the base64-encoded certificate fingerprint and store it securely. This value is required to [complete setup in Workato](#complete-setup-in-workato).
   
   Remove any trailing `=` when you store the fingerprint.
   

#### Configure token-based authentication in Oracle Fusion Cloud

Complete the following steps to configure token-based authentication in Oracle Fusion Cloud:

1. Sign in to Oracle Fusion Cloud.
   
2. Click the **☰ Navigator** icon to expand the sidebar and go to **Tools > Security**.
   
3. Click **API Authentication**.
   
4. Click **\+ Create Oracle API Authentication Provider**.
   
5. Click **Edit**.
   
6. Enter the name of the calling provider in the **Trusted Issuer** field. For example, `Workato`.
   
7. Select the **JWT** checkbox as the **Token Type**.
   
   ![Configure token-based authentication in Oracle Fusion Cloud](/assets/jwt-config.DQfXPdwp.png)_Configure token-based authentication in Oracle Fusion Cloud_
   
8. Click **Save and Close**.
   
9. Click **Inbound API Authentication Public Certificates**.
   
10. Click **\+ Add New Certificate**.
    
11. Enter a name in the **Certificate Alias** field.
    
12. Click **Choose File** and select the public certificate (`publickey.cer`) generated in the [Generate a X.509 key pair](#generate-a-x-509-key-pair) step.
    
13. Click **Save**.
    

#### Complete setup in Workato

Complete the following steps to connect to Oracle Fusion Cloud using JWT token authentication:

1. Sign in to Workato.
   
2. Select the project where you plan to store the connection.
   
3. Select **Create > Connection** or press C twice.
   
4. Search for `Oracle Fusion Cloud` and select it as your app.
   
5. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Oracle Fusion Cloud (JWT token authentication)](/assets/jwt-token.BfN6UZkC.png)_Connect to Oracle Fusion Cloud (JWT token authentication)_
   
6. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
7. Use the **Auth type** drop-down menu to select **JWT token**.
   
8. Enter the [trusted issuer name](#configure-token-based-authentication-in-oracle-fusion-cloud) for your Oracle API authentication in the **Issuer** field.
   
9. Enter the username for your Oracle Fusion Cloud account in the **Username** field.
   
10. Enter the [private key](#generate-a-x-509-key-pair) associated with your public certificate in the **Private key** field.
    
11. Enter your [base64-encoded certificate fingerprint](#retrieve-the-certificate-fingerprint) in the **Certificate fingerprint** field.
    
12. Enter the subdomain for your Oracle Fusion Cloud instance in the **Subdomain** field. For example, `servername.fa.us2.oraclecloud.com`.
    
13. Click **Connect**.
    

## Configure the pipeline

Complete the following steps to configure Oracle Fusion Cloud as your data pipeline source in Workato:

1. Return to your Workato account.
   
2. Select **Create > Data pipeline** or press C+I.
   
3. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
5. Click **Start building**.
   
6. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app-oracle.BUuhzejr.png)_Configure the Extract new/updated records from source app trigger_
   
7. Use the **Your Connected Source Apps** drop-down menu to select **Oracle Fusion Cloud**.
   
8. Choose the Oracle Fusion Cloud connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose a Oracle Fusion Cloud connection](/assets/choose-oracle-fusion-connection.K_uALRU2.png)_Choose a Oracle Fusion Cloud connection_
   
9. Click **Add object** to open the object modal.
   
   ![Add object](/assets/add-oracle-fusion-object.D-T0ZcIS.png)_Add object_
   
10. Search or browse the list of available Oracle Fusion Cloud tables and select the tables you plan to sync.
    
11. Click **Add**.
    
12. Review and customize the schema for each table you select. The pipeline automatically fetches schemas for each to ensure the destination matches the source.
    
    ![Expand object](/assets/expand-object-oracle.Br2pJtZq.png)_Expand object_
    
    You can expand a table to view its fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from extraction and schema replication.
    
13. Configure sync settings for each table:
    
    1. Click the **Settings** (gear) icon next to the table.
       
       ![Configure sync settings](/assets/click-settings-icon.Bi0q8G5n.png)_Configure sync settings_
       
    2. Select a **Sync mode**:
       
       **Incremental**
       
       1. Select **Incremental** to sync only new and updated records.
          
       2. Select a **Change tracking column** for incremental syncs. This column detects new and updated records.
          
          ![Configure sync settings](/assets/configure-sync-settings.BYz_qWjn.png)_Configure sync settings_
          
          The selected tracking column is required for incremental syncs and can't be deselected.
          
          The following occurs if the table doesn't contain a valid timestamp or change tracking column:
          
          - Incremental sync isn't available
          - The pipeline defaults to **Full sync**
          - The **Change tracking column** field is disabled
          - The pipeline reloads all records on each run
       3. Click **Save**.
          
       
       **Full sync**
       
       1. Select **Full Sync** to reload all records on each run. The **Change tracking column** field doesn't appear for full sync.
          
          ![Configure sync settings](/assets/configure-sync-settings-full.l25F3Z52.png)_Configure sync settings_
          
       2. Click **Save**.
          
       
    3. Review the impact of sync configuration changes.
       
       > **FULL RE-SYNC BEHAVIOR**
       > 
       > Changing the **Sync mode** or **Change tracking column** triggers a full re-sync of the affected table on the next pipeline run.
       > 
       > During a full re-sync, the pipeline reloads all records for that table. This process may increase runtime and reprocess existing data in the destination.
       
14. Click **Add object** again to add additional tables using the same flow.
    
15. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
16. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Oracle Fusion Cloud to the destination.
    
    **Time-based schedule**
    
    1. Select the **Time unit**, such as **Minutes**, **Hours**, or **Days**.
       
    2. Specify the sync interval in the **Trigger every** field.
       
       For example, the pipeline syncs every 6 hours if you select **Hours** as the **Time unit** and enter `6` in the **Trigger every** field.
       
       The minimum interval you can set is 15 minutes.
       
    3. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts records. The pipeline picks up all available records from the source if you leave this field blank.
       
       You can't change this value after you run the pipeline.
       
    4. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-destinations#configure‒how‒data‒is‒loaded‒in‒the‒workato‒data‒pipeline).
       
    
    **Cron-based scheduling**
    
    1. Use the **Time unit** drop-down menu to select **Custom schedule**.
       
    2. Enter an expression in the **Cron expression** field using the format:
       
       ```text
       [minute] [hour] [day of month] [month] [day of week]
       ```
       
       The minimum interval for cron schedules is 15 minutes.
       
       For example, enter the following expression to sync every day at 8:00 AM UTC:
       
       ```text
       0 8 * * *
       ```
       
    3. Optional. Select a **Timezone** for the cron expression. Leave blank to use `Etc/UTC`.
       
    4. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts records. The pipeline picks up all available records from the source if you leave this field blank.
       
       You can't change this value after you run the pipeline.
       
    5. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-destinations#configure‒how‒data‒is‒loaded‒in‒the‒workato‒data‒pipeline).
       
    

## Supported Oracle Fusion Cloud objects

The Oracle Fusion Cloud connector supports a wide range of business objects across multiple modules, including:

- Financials
- Procurement
- Supply chain
- Order management
- Human capital management

The available objects depend on:

- Enabled Oracle Fusion Cloud modules
- User permissions and roles
