---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-sap-agent-ohd.md
description: >-
  Extract data from SAP BW Open Hub Destinations into data pipelines using the
  SAP Data Agent.
---

# Configure SAP BW OHD

The SAP BW OHD integration enables you to extract data from SAP BW Open Hub Destinations (OHD) into data pipelines using the SAP Data Agent.

This integration uses an asynchronous, package-based extraction method to securely and efficiently handle large datasets.

## Overview

SAP Data Agent – BW OHD uses the SAP Data Agent to transfer Open Hub Destination data from SAP to Workato.

The following occurs when a pipeline runs:

1. Workato sends an extraction request to SAP.
2. SAP Data Agent collects data from the Open Hub Destination and stores it in temporary packages.
3. Workato retrieves the packages sequentially.
4. SAP Data Agent deletes temporary data after completion.

You can monitor logs in SAP using transaction code `SLG1`.

SAP Data Agent processes extraction requests asynchronously. It stages data temporarily in SAP and transfers it to Workato in controlled packages to handle large datasets efficiently.

### Supported Open Hub Destination types

SAP Data Agent – BW OHD supports Open Hub Destinations with the following destination type:

- Database table

SAP Data Agent – BW OHD doesn't support Open Hub Destinations with the following destination types:

- File
- Third-party tool

### Supported objects

SAP Data Agent – BW OHD supports Open Hub Destinations sourced from the following object types:

- DataSource
- DataStore object (advanced)
- DataStore object (classic)
- InfoObject
- InfoCube
- MultiProvider
- Semantically Partitioned Object
- Query

## Set up SAP Data Agent

You must install and configure the SAP Data Agent on the SAP application server before creating a data pipeline.

SAP Data Agent installs as an ABAP transport in the SAP system. It exposes OData services under the `/WKTO/` namespace and enables secure, package-based data extraction.

### Supported SAP systems

The following SAP systems support SAP Data Agent – BW OHD:

| SAP system | Database | NetWeaver version | ABAP version |
| --- | --- | --- | --- |
| SAP ECC | Any | `7.4 EHP7 and above` | 7.4 and above |
| SAP S/4HANA | SAP HANA | `1610 and above` | 7.5 and above |
| SAP BW | Any | `7.4 EHP7 and above` | 7.4 and above |
| SAP BW/4HANA | SAP HANA | `2.0 SPS07 and above` | 7.5 and above |

> **BW OPEN HUB LICENSE**
> 
> SAP ECC requires the BW Open Hub license as an additional license. SAP HANA-based systems include the license with the installation. Contact your SAP partner to confirm your license coverage.

### Create an SAP user account

You must create a dedicated SAP Communication user (type C) with the required authorization. Data pipelines support only basic authentication.

Provide the SAP username and password of the SAP Communication user.

Assign the [required SAP role and authorization objects](#roles-and-authorization-objects) before testing connectivity.

### Install SAP Data Agent

You must install SAP Data Agent by importing the ABAP transport request into the SAP system.

> **TRANSPORT REQUEST REQUIRED**
> 
> Contact your Workato Account Executive or Customer Success Manager to obtain the ABAP transport request package.

The installation activates required OData services, assigns runtime components, and enables extraction under the `/WKTO/` namespace.

Complete the following steps to install the SAP Data Agent:

1. Import the SAP transport request provided by Workato.
   
2. Assign the required SAP authorizations and roles to the user.
   
3. Activate SICF (SAP Internet Communication Framework transaction) services under the `/WKTO/` namespace.
   
4. Maintain the local alias for services in transaction `/IWFND/MAINT_SERVICE`.
   
5. Maintain required parameters in transaction `/WKTO/CONFIG`:
   
   - Maintain `CSV_SEP` to set the CSV separator. Use `|` (pipe). Enter only the separator character.
   - Maintain `BW_MSTR_CLEANUP` to set the number of days before pipeline cleanup in the internal master table. Use `7` as the recommended value.
   - Maintain `FILEPATH` to set the `AL11` path for storing export files. For example, `D:\WORKATO\EXPORT\`.

To uninstall SAP Data Agent, import the uninstall transport request provided by Workato into the SAP system.

### Configure SAP role for BW OHD

Assign the required role and authorizations to the SAP user used for SAP Data Agent.

This role grants access to the required OData services and file-level permissions for data extraction.

1. Go to transaction code `PFCG`.
   
2. Open role `/WKTO/BWOHD`, or create a custom role that includes the required authorization objects.
   
3. Go to the **Authorizations** tab and select **Change Authorization Data**.
   
4. Ensure the role includes the following authorization objects and field values:
   
   Summary of authorization included in the role
   
   <dl><dt>S_SERVICE</dt><dd>Authorizes access to SAP Data Agent BW OHD OData services under the <code>/WKTO/</code> namespace.</dd><dt>S_DATASET</dt><dd>Controls access to physical files on the SAP application server.</dd></dl>
   
   Authorization Field Values for S\_SERVICE Object
   
   <dt>Required for SAP Data Agent BW OHD OData Services</dt>
   
   <dd><dl class="horizontal-dl"><dt>Program, transaction or Function</dt><dd>SRV_NAME</dd><dt>Values:</dt><dd><ul><li>2EBD022B6AD68064044A4209FE6283 (/WKTO/DA_BWOH_SRV)</li><li>3296492449AF2A0CA265701D1572AA (/WKTO/DA_BWOH_SRV_0001)</li></ul></dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Type of check Flag (SRV_TYPE)</dt><dd>HT</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Program Name with Search Help</dt><dd>/WKTO/CL_DA_BWOH_DPC_EXT======CP</dd></dl></dd>
   
   Authorization Field Values for S\_DATASET Object
   
   <dt>Required for File-Level Access</dt>
   
   <dd><dl class="horizontal-dl"><dt>Activity</dt><dd>*</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Physical file name</dt><dd>*</dd></dl></dd>
   
5. Generate the authorization profile and save the role.
   
6. Assign the role to the SAP user used for SAP Data Agent.
   

## Expose SAP BW objects as an Open Hub Destination

You must expose your SAP BW data through an Open Hub Destination before the pipeline can extract it. Two objects are required to expose data through Open Hub:

- **Open Hub Destination (OHD)**: Defines the target (database table) and the field mapping from the source InfoProvider.
- **Data Transfer Process (DTP)**: Moves data from the source InfoProvider into the Open Hub Destination, and supports full or delta loads.

> **PREREQUISITES**
> 
> Before you begin, ensure you have completed the following tasks:
> 
> - Obtain authorization for transaction `RSA1` (BW Modeling) and Open Hub objects.
> - Activate and load the source InfoProvider (DSO, ADSO, or InfoCube) with data.

### Create the Open Hub Destination

Complete the following steps to create the Open Hub Destination:

1. Log on to the BW system and run transaction `RSA1`.
   
2. Go to the InfoArea that contains the source InfoProvider you plan to expose in the **Modeling** tree.
   
   ![BW Modeling tree in RSA1](/assets/bw-modeling-tree.CWkloq5t.png)_BW Modeling tree in RSA1_
   
3. Create a new Open Hub Destination in the InfoArea.
   
4. Enter a technical name and description for the Open Hub Destination. For example, `OHD_PUR`.
   
5. Select the source InfoProvider (DSO, ADSO, or InfoCube), InfoObject, or DataSource that holds the data to expose.
   
6. Use the **Destination Type** field to select **Database Table**. SAP generates a transparent table, such as `/BIC/OHOHD_PUR`, for direct downstream SQL access.
   
   ![Open Hub Destination definition with database table destination type](/assets/ohd-definition.BwnGK3tf.png)_Open Hub Destination definition with database table destination type_
   
7. Save the Open Hub Destination. BW proposes field names based on the source structure.
   

### Map fields

Complete the following steps to map the source fields to the target table:

1. Review the auto-proposed mapping between source InfoObjects and target fields on the **Field Definition** tab.
   
2. Adjust data types, lengths, or field names as required by the receiving system.
   
3. Optional. Exclude fields that the target system doesn't need, such as technical BW fields.
   
4. Activate the Open Hub Destination after you confirm the mapping.
   
   ![Field definition tab with confirmed mapping](/assets/field-definition-tab.CSDspsGg.png)_Field definition tab with confirmed mapping_
   

### Create the Data Transfer Process

Complete the following steps to create the Data Transfer Process:

1. Right-click the Open Hub Destination you created and select **Create Data Transfer Process**.
   
2. Use the **Extraction Mode** field on the **Extraction** tab to choose the DTP type:
   
   - **Full** extracts the entire dataset every run. Use this type for initial loads or small static datasets.
   - **Delta** extracts only new or changed records after the last run. Use this type for recurring, incremental loads.
3. Set filters on the **Extraction** tab if you plan to expose only a subset of data, such as a specific fiscal year, plant, or sales organization.
   
4. Activate the DTP.
   
   ![Data Transfer Process configuration](/assets/data-process-configuration.BrfinJeB.png)_Data Transfer Process configuration_
   

> **DTP TYPE AND SYNC MODE**
> 
> The DTP type determines the [sync mode](#select-the-sync-mode) you select when you configure the pipeline. Select **Full sync** for a Full DTP and **Incremental sync** for a Delta DTP.

### Execute and validate the DTP

Complete the following steps to execute and validate the Data Transfer Process:

1. Execute the DTP manually for the first run, or schedule it through a process chain for recurring loads.
   
2. Monitor the execution in the DTP monitor and confirm the record count matches expectations.
   
3. Validate the output and check the contents of the generated database table.
   
   ![DTP monitor showing completed execution](/assets/dtp-monitor.CgaxBihK.png)_DTP monitor showing completed execution_
   

## Establish OData connectivity between Workato and SAP

You must configure connectivity between Workato and the SAP system before creating a data pipeline.

SAP Data Agent exposes OData services that Workato uses for authentication, extraction, and cleanup operations.

### Connect to SAP on-premise systems

Deploy a Workato on-prem agent (OPA) if your SAP system doesn't expose OData services to the public internet.

The on-prem agent establishes a secure outbound connection from your network to Workato and enables access to internal SAP OData services.

Complete the following steps to connect to SAP on-premise systems:

1. Install and register a Workato on-prem agent in your workspace.
   
2. Ensure the SAP system exposes the required OData services under the `/WKTO/` namespace.
   
3. Verify network connectivity between the on-prem agent host and the SAP application server.
   

### Connect without an on-prem agent

Whitelist [Workato IP addresses](/en/security/ip-allowlists) on the SAP HTTPS port to allow inbound traffic from Workato. You can find the HTTPS port in transaction `SMICM` or SAP Web Dispatcher.

Ensure the SAP OData service endpoint remains externally accessible over HTTPS.

### Configure the development environment (on-prem agent)

In development environments, you may disable certificate validation in the on-prem agent configuration to troubleshoot connectivity issues.

Edit the `config.yml` file in the OPA `conf` directory:

```yaml
http:
  trustAll: true
  verifyHost: false
```

Refer to the [On-prem agent HTTP profile](/en/on-prem/agents/connection/profile#http-profile) documentation for more information about HTTP profile configuration options.

Use this configuration only in non-production environments.

## Create and configure a data pipeline

After you install SAP Data Agent and establish connectivity, create a data pipeline to extract data from an Open Hub Destination.

### Create the SAP OData connection

Complete the following steps to create the SAP OData connection:

1. Select **Create > Connection** or press C twice.
   
2. Search for `SAP OData` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Create an SAP OData connection](/assets/choose-sap-odata-connection.BuVvt83e.png)_Create an SAP OData connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Complete the following fields in Workato to establish the SAP OData connection:
   
   | Field | Description |
   | --- | --- |
   | Connection type | Select the connection type based on your SAP deployment. Choose **On-premise** (through Secure Gateway) if your SAP instance runs on a network that doesn't allow direct external connections. Ensure you have an active on-prem agent before attempting to connect. Choose **Cloud** if SAP exposes OData services publicly. Requests are sent directly from Workato servers. |
   | Authentication type | Select **Basic**. Data pipelines support only basic authentication. |
   | OData version | Select **OData V2**. |
   | Username | Enter the username of the SAP Communication user (type C). |
   | Password | Enter the corresponding password. |
   | Host URL | Enter `https://<hostname>/sap/opu/odata/` as the base path of the SAP OData services. |
   | Service | Enter `WKTO/DA_CM_SRV` as the OData service name configured in SAP. |
   | SAP Client | Enter the SAP client used for login. For example, if your service URL is `https://<hostname>/sap/opu/odata/WKTO/DA_CM_SRV?sap-client=800`, enter `800`. This field applies only to on-prem SAP systems. |
   
6. Click **Connect** to validate the credentials and connection configuration.
   

Verify the following if the connection fails:

- SAP credentials
- Host URL format
- Service name
- Network accessibility

Common errors include `401 Unauthorized` and `Host unreachable`.

### Create a data pipeline

Complete the following steps to create a new data pipeline:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   

### Configure the SAP source

Complete the following steps to configure SAP as the source application:

1. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from the source application.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app-sap.BXSnHFYp.png)_Configure the Extract new/updated records from source app trigger_
   
2. Select **SAP OData** as the source application.
   
3. Choose the SAP OData connection to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
   ![Choose the SAP OData connection](/assets/choose-sap-connection.CjB45JFm.png)_Choose the SAP OData connection_
   
4. Click **Add object** to select the Open Hub Destination to extract.
   
   ![Add object](/assets/add-object-sap.DTKocWsM.png)_Add object_
   
5. Enter at least three uppercase characters of the Open Hub Destination name in the search field.
   
   Open Hub Destination names are case-sensitive and use uppercase letters.
   
6. Select the Open Hub Destinations from the search results.
   
   ![Select Open Hub Destinations](/assets/select-ohd.Ch-BNRvN.png)_Select Open Hub Destinations_
   
7. Click **Add** to confirm the selection.
   

### Select the sync mode

The sync mode you select must match the extraction behavior of the data source that feeds the Open Hub Destination in the source system.

Open the settings for the object in the objects section and select the sync mode:

- Select **Full sync** if the data source provides a full dataset during each extraction.
- Select **Incremental sync** if the data source provides only delta (new or changed) records.

![Configure the sync mode](/assets/configure-ohd-mode.CeWxfkrG.png)_Configure the sync mode_

> **SYNC MODE ALIGNMENT**
> 
> You are responsible for ensuring that the configured sync mode aligns with the extraction logic of the data source in the source system.

### Define the schema

After you add the Open Hub Destination, the pipeline automatically fetches the schema for each selected object. Review and customize the schema to ensure the destination matches the source:

1. Expand any object to view the list of available fields.
   
2. Keep all fields selected to extract all data, or deselect specific fields to exclude them from extraction and schema replication.
   
3. Optional. Configure field-level data protection for each non-key field:
   
   - **Replicate as is (default)**: Data values at the source are replicated identically to the destination.
   - **Hash**: Hash sensitive data values in the column before syncing to your destination.
4. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple Open Hub Destinations in your pipeline.
   
5. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
   
   - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
   - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
   
   Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
   

### Configure advanced settings

Configure pipeline-level settings to control execution behavior and SAP system impact:

1. Adjust the **Concurrency** configuration.
   
   ![Adjust the concurrency configuration](/assets/adjust-concurrency-configuration.D90fq1uo.png)_Adjust the concurrency configuration_
   
   Concurrency defines how many pipeline jobs run simultaneously:
   
   - Higher values allow parallel executions and increase throughput.
   - Lower values reduce load on the SAP system and help prevent table locks or performance issues.
   
   Adjust concurrency carefully to avoid excessive load on the SAP system.
   
2. Set the **Frequency**.
   
   ![Configure frequency](/assets/configure-frequency.BlbzJx4B.png)_Configure frequency_
   
   Frequency defines how often the pipeline runs, such as every few minutes, hourly, or daily. Select a frequency that balances data freshness with SAP system performance and stability.
   
   Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from SAP BW OHD to the destination.
   
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
      
   

### Configure the destination

After you configure the SAP source and advanced settings, select the destination for your data.

1. Click the **Load data to target table in destination app** action. This action defines how the pipeline replicates data in the destination.
   
   ![Configure destination](/assets/configure-destination.BA1kdQI-.png)_Configure destination_
   
2. Select the destination application.
   
3. Select an existing destination connection, or click **\+ New connection** to create one.
   
4. Click **Save**.
   

Refer to the following guides for destination-specific configuration details:

- [Configure Snowflake](/en/data-orchestration/data-pipeline-recipe/connect-to-snowflake)
- [Configure Databricks](/en/data-orchestration/data-pipeline-recipe/connect-to-databricks)
- [Configure SQL Server](/en/data-orchestration/data-pipeline-recipe/connect-to-sql-server)
- [Configure Google BigQuery](/en/data-orchestration/data-pipeline-recipe/connect-to-bigquery)

### Start the pipeline

Click **Start pipeline** to begin data extraction.

![Start pipeline](/assets/start-sap-pipeline.fKcgQazj.png)_Start pipeline_

Workato sends extraction requests to SAP Data Agent, retrieves data in packages, and loads the data into the destination.

### Review sync completion

After the pipeline finishes extracting data, SAP Data Agent performs post-extraction cleanup to protect system performance and data security.

![Completed sync](/assets/completed-sync-sap.BrWCO2qs.png)_Completed sync_

The following occurs:

- Workato loads the extracted data into the destination and makes it available for downstream processing.
- SAP Data Agent sets a checkpoint for the last extracted request. Future pipeline runs retrieve only new data generated after the last successful run.
- SAP Data Agent clears pipeline execution data and temporary information based on the `BW_MSTR_CLEANUP` parameter value.

The sync mode determines how the pipeline loads data into the destination:

- **Full sync**: The pipeline replaces existing data in the destination with the latest extracted dataset.
- **Incremental sync**: The pipeline adds newly extracted records to the existing data in the destination.

This cleanup process ensures efficient resource usage and prevents residual staging data from accumulating in SAP.
