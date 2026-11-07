---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-sap-agent.md
description: >-
  Configure SAP Table Reader to extract SAP table data into data pipelines
  through the SAP Data Agent using package-based extraction.
---

# Configure SAP Table Reader (SAP Data Agent)

The SAP Table Reader enables you to extract SAP table data into data pipelines using the SAP Data Agent.

This integration uses an asynchronous, package-based extraction method to securely and efficiently handle large datasets.

## Overview

SAP Table Reader uses the SAP Data Agent to transfer data from SAP to Workato.

The following occurs when a pipeline runs:

1. Workato sends an extraction request to SAP.
2. SAP Data Agent collects data and stores it in temporary packages.
3. Workato retrieves the packages sequentially.
4. SAP Data Agent deletes temporary data after completion.

You can monitor logs in SAP using transaction code `SLG1`.

SAP Data Agent processes extraction requests asynchronously. It stages data temporarily in SAP and transfers it to Workato in controlled packages to handle large datasets efficiently.

### Supported source types

SAP Table Reader supports the following source types:

- Transparent tables
- Pool tables
- Cluster tables
- Traditional database views
- CDS views without parameters

SAP Table Reader doesn't support the following:

- Consumption views
- AMDP (ABAP Managed Database Procedures)
- CDS views with parameters

## Set up SAP Data Agent

You must install and configure the SAP Data Agent on the SAP application server before creating a data pipeline.

SAP Data Agent installs as an ABAP transport in the SAP system. It exposes OData services under the `/WKTO/` namespace and enables secure, package-based data extraction.

### Supported SAP systems

The following SAP systems support SAP Data Agent – Table Reader:

| SAP system | Database | NetWeaver version | ABAP version |
| --- | --- | --- | --- |
| SAP ECC | Any | `7.4 EHP7 and above` | 7.4 and above |
| SAP S/4HANA | SAP HANA | `1610 and above` | 7.5 and above |
| SAP BW | Any | `7.4 EHP7 and above` | 7.4 and above |
| SAP BW/4HANA | SAP HANA | `2.0 SPS07 and above` | 7.5 and above |

### Create an SAP user account

You must create a dedicated SAP Communication user (type C) with the required authorization. Data pipelines support only basic authentication.

Provide the SAP username and password of the SAP Communication user.

Assign the [required SAP roles and authorization objects](#roles-and-authorization-objects) before testing connectivity.

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
   
   - Maintain `CSV_SEP` to set the CSV separator. Use `|` (pipe).
   - Maintain `MSTR_CLEANUP` to set the number of days before pipeline cleanup in the internal master table. Use `7` as the recommended value.
   - Maintain `FILEPATH` to set the `AL11` path for storing export files. For example, `D:\WORKATO\EXPORT\`.
6. Tune package size for large tables using transaction `/WKTO/PACK`. Very large tables require package size tuning. Refer to the [Troubleshooting](/en/data-orchestration/data-pipeline-recipe/configure-sap-table-reader-troubleshooting) guide for additional guidance.
   

### Configure SAP role for Table Reader

Assign the required role and authorizations to the SAP user used for SAP Data Agent.

This role grants access to required OData services, background job processing, and table-level permissions for data extraction.

1. Go to transaction code `PFCG`.
   
2. Open role `/WKTO/TABLE_READER`, or create a custom role that includes the required authorization objects.
   
3. Go to the **Authorizations** tab and select **Change Authorization Data**.
   
4. Ensure the role includes the following authorization objects and field values:
   
   Summary of authorization included in the role
   
   <dl><dt>S_SERVICE</dt><dd>Authorizes access to SAP Data Agent OData services under the <code>/WKTO/</code> namespace.</dd><dt>S_BTCH_ADM</dt><dd>Controls background job administration permissions.</dd><dt>S_BTCH_JOB</dt><dd>Authorizes release and execution of background jobs used during extraction.</dd><dt>S_TABU_DIS</dt><dd>Controls access to table authorization groups.</dd><dt>S_TABU_NAM</dt><dd>Controls access to specific table names.</dd></dl>
   
   Authorization Field Values for S\_SERVICE Object
   
   <dt>Required for SAP Data Agent OData Services</dt>
   
   <dd><dl class="horizontal-dl"><dt>Program, transaction or Function</dt><dd>SRV_NAME</dd><dt>Values:</dt><dd><ul><li>0AE2A6D56834889146773B86C3B4A4 (/WKTO/DA_CM_SRV)</li><li>9CB49C41E6503E8A3BF6A9CE025B88 (/WKTO/DA_LOG_SRV_0001)</li><li>B80B26B216EE837EDD71ECBCC2A106 (/WKTO/DA_TBL_SRV_0001)</li><li>BF83C9264549804E40E46A704B73A0 (/WKTO/DA_CM_SRV_0001)</li><li>C45237A6760D58CFA80609CAE052B9 (/WKTO/DA_TBL_SRV)</li><li>ECE235D66D4238FC5D4C2F97A16A4F (/WKTO/DA_LOG_SRV)</li></ul></dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Type of check Flag (SRV_TYPE)</dt><dd>HT</dd></dl></dd>
   
   Authorization Field Values for S\_BTCH\_ADM Object
   
   <dt>Required for Background Job Administration</dt>
   
   <dd><dl class="horizontal-dl"><dt>Background Administrator</dt><dd>N</dd></dl></dd>
   
   Authorization Field Values for S\_BTCH\_JOB Object
   
   <dt>Required for Background Job Execution</dt>
   
   <dd><dl class="horizontal-dl"><dt>Job Operations</dt><dd>RELE</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Summary of jobs for a group</dt><dd>' '</dd></dl></dd>
   
   Authorization Field Values for S\_TABU\_DIS Object
   
   <dt>Required for Table Access by Authorization Group</dt>
   
   <dd><dl class="horizontal-dl"><dt>Activity</dt><dd>02, 03</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Table Authorization Group</dt><dd>VA</dd></dl></dd>
   
   Authorization Field Values for S\_TABU\_NAM Object
   
   <dt>Required for Table-Level Access</dt>
   
   <dd><dl class="horizontal-dl"><dt>Activity</dt><dd>03</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Table Name</dt><dd>*</dd></dl></dd>
   
5. Generate the authorization profile and save the role.
   
6. Assign the role to the SAP user used for SAP Data Agent.
   

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

After you install SAP Data Agent and establish connectivity, create a data pipeline to extract SAP table data.

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
   
4. Click **Add object** to select the SAP table to extract.
   
   ![Add object](/assets/add-object-sap.DTKocWsM.png)_Add object_
   
5. Enter at least three uppercase characters of the SAP table name in the search field.
   
   SAP table names are case-sensitive and use uppercase letters.
   
6. Select the tables from the search results.
   
   ![Select SAP tables](/assets/select-sap-tables.CEH-GzZL.png)_Select SAP tables_
   
7. Click **Add** to confirm the selection.
   
   > **CDS VIEWS**
   > 
   > Search the SQL view name instead of the CDS view name for CDS views.
   

### Define the schema

After you add the SAP table, the pipeline automatically fetches the schema for each selected object. Review and customize the schema to ensure the destination matches the source:

1. Click **Get schema** to retrieve table metadata.
   
2. Expand any table to view the list of available fields.
   
3. Keep all fields selected to extract all data, or deselect specific fields to exclude them from extraction and schema replication.
   
4. Optional. Configure field-level data protection for each non-key field:
   
   - **Replicate as is (default)**: Data values at the source are replicated identically to the destination.
   - **Hash**: Hash sensitive data values in the column before syncing to your destination.
5. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple SAP tables in your pipeline.
   
6. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
   
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
   
   Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from SAP Table Reader to the destination.
   
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

### Start the pipeline

Click **Start pipeline** to begin data extraction.

![Start pipeline](/assets/start-sap-pipeline.fKcgQazj.png)_Start pipeline_

Workato sends extraction requests to SAP Data Agent, retrieves data in packages, and loads the data into the destination.

### Review sync completion

After the pipeline finishes extracting data, SAP Data Agent performs post-extraction cleanup to protect system performance and data security.

![Completed sync](/assets/completed-sync-sap.BrWCO2qs.png)_Completed sync_

The following occurs:

- Workato makes the full dataset available in the pipeline for downstream processing.
- Workato sends a final cleanup API call to SAP Data Agent.
- The SAP Data Agent flushes pipeline execution memory and deletes temporary staging tables in the SAP system.

This cleanup process ensures efficient resource usage and prevents residual staging data from accumulating in SAP.
