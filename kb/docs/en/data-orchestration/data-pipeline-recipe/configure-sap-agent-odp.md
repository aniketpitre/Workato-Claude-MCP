---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-sap-agent-odp.md
description: >-
  Extract data from SAP Operational Data Provisioning (ODP) data sources into
  data pipelines using the SAP Data Agent.
---

# Configure SAP ODP

The SAP ODP integration enables you to extract data from SAP Operational Data Provisioning (ODP) data sources into data pipelines using the SAP Data Agent.

This integration uses an asynchronous, package-based extraction method to securely and efficiently handle large datasets.

## Overview

SAP Data Agent uses ODP through OData services to transfer data from SAP to Workato. SAP Data Agent follows the guidelines in [SAP Note 3255746](https://me.sap.com/notes/3255746/E) for extracting data from SAP ODP data sources.

The following occurs when a pipeline runs:

- Workato sends an extraction request to SAP.
- The SAP ODP framework collects the required data and stores it in temporary packages.
- Workato retrieves the packages sequentially.
- The SAP ODP framework deletes temporary data after completion.

You can monitor extraction in SAP using transaction code `ODQMON`.

### Supported ODP contexts

SAP ODP supports data sources from the following ODP contexts:

- ABAP Core Data Services (`ABAP_CDS`)
- DataSources/Extractors (`SAPI`)
- HANA Information Views (`HANA`)
- SAP NetWeaver Business Warehouse (`BW`)

### Supported extraction modes

SAP ODP supports the following extraction modes:

- **Full**: Extracts all available records from the data source on every run.
- **Delta**: Performs an initial load, then extracts only new or changed records on later runs.

Refer to [Select the sync mode](#select-the-sync-mode) for more information.

### Binary field values

SAP displays some binary (`RAW`) field values in hexadecimal format. The corresponding values loaded into the destination are Base64-encoded. This is expected behavior.

## Set up SAP Data Agent

You must install and configure the SAP Data Agent on the SAP application server before creating a data pipeline.

SAP Data Agent installs as an ABAP transport in the SAP system. It exposes OData services under the `/WKTO/` namespace and enables secure, package-based data extraction.

### Supported SAP systems

The following SAP systems support SAP ODP:

| SAP system | Database | NetWeaver version | ABAP version |
| --- | --- | --- | --- |
| SAP ECC | Any | `7.5 EHP8 and above` | 7.5 and above |
| SAP S/4HANA | SAP HANA | `1610 and above` | 7.5 and above |
| SAP BW | Any | `7.5 EHP8 and above` | 7.5 and above |
| SAP BW/4HANA | SAP HANA | `2.0 SPS07 and above` | 7.5 and above |

### Create an SAP user account

You must create a dedicated SAP Communication user (SAP user type C) with the required authorization. Data pipelines support only basic authentication.

You must provide the username and password of this user when you [create the SAP OData connection](#create-the-sap-odata-connection) in Workato.

Assign the [required SAP role and authorization objects](#roles-and-authorization-objects) before testing connectivity.

### Install SAP Data Agent

You must install SAP Data Agent by importing the ABAP transport request into the SAP system.

> **TRANSPORT REQUEST REQUIRED**
> 
> Contact your Workato Account Executive or Customer Success Manager to obtain the ABAP transport request package.

Complete the following steps to install the SAP Data Agent:

1. Import the SAP transport request provided by Workato.
   
2. Assign the required SAP authorizations and roles to the user.
   
3. Activate SICF (SAP Internet Communication Framework transaction) services under the `/WKTO/` namespace.
   
4. Maintain the local alias for services in transaction `/IWFND/MAINT_SERVICE`.
   

Import the uninstall transport request provided by Workato into the SAP system to uninstall the SAP Data Agent. Workato provides separate uninstall transport requests for SAP BW/4HANA and non-BW/4HANA systems.

### Configure SAP role for ODP

Assign the required role and authorizations to the SAP user used for SAP Data Agent. This role grants access to the required OData services, background job processing, and ODP data sources for data extraction.

1. Go to transaction code `PFCG`.
   
2. Open role `/WKTO/ODP`, or create a custom role that includes the required authorization objects.
   
3. Go to the **Authorizations** tab and select **Change Authorization Data**.
   
4. Ensure the role includes the following authorization objects and field values:
   
   Summary of authorization included in the role
   
   <dl><dt>S_SERVICE</dt><dd>Authorizes access to SAP Data Agent OData services.</dd><dt>S_BTCH_JOB</dt><dd>Authorizes release and execution of background jobs used during extraction.</dd><dt>S_BTCH_ADM</dt><dd>Controls background job administration permissions.</dd><dt>S_RO_OSOA</dt><dd>Controls access to ODP data sources.</dd></dl>
   
   Authorization Field Values for S\_SERVICE Object
   
   <dt>Required for SAP Data Agent OData Services</dt>
   
   <dd><dl class="horizontal-dl"><dt>Program, transaction or Function</dt><dd>*</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Type of check Flag and Authorization</dt><dd>*</dd></dl></dd>
   
   Authorization Field Values for S\_BTCH\_JOB Object
   
   <dt>Required for Background Job Execution</dt>
   
   <dd><dl class="horizontal-dl"><dt>Job Operations</dt><dd>RELE</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Summary of jobs for a group</dt><dd>' '</dd></dl></dd>
   
   Authorization Field Values for S\_BTCH\_ADM Object
   
   <dt>Required for Background Job Administration</dt>
   
   <dd><dl class="horizontal-dl"><dt>Background Administrator ID</dt><dd>Y</dd></dl></dd>
   
   Authorization Field Values for S\_RO\_OSOA Object
   
   <dt>Required for ODP Data Source Access</dt>
   
   <dd><dl class="horizontal-dl"><dt>Activity</dt><dd>03</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Data Source (OSOA/OSOD)</dt><dd>*</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Application Component of a Data Source</dt><dd>*</dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>Subobject for Data Source</dt><dd>*</dd></dl></dd>
   
5. Generate the authorization profile and save the role.
   
6. Assign the role to the SAP user used for SAP Data Agent.
   

SAP users who configure data sources and monitor extraction in SAP also require the following authorizations to run SAP Data Agent transactions:

Authorization Field Values for configuration and monitoring

<dt>S_TCODE</dt>

<dd><dl class="horizontal-dl"><dt>Transaction code</dt><dd><ul><li>/WKTO/ADV_LOG</li><li>/WKTO/CONFIG</li><li>/WKTO/ODP_CONFIG</li><li>/WKTO/ODP_SUBS</li><li>ODQMON</li></ul></dd></dl></dd>

<dt>S_TABU_CLI</dt>

<dd><dl class="horizontal-dl"><dt>Indicator for cross-client maintenance</dt><dd>' '</dd></dl></dd>

<dt>S_TABU_DIS</dt>

<dd><dl class="horizontal-dl"><dt>Activity</dt><dd>02, 03</dd><dt>Table Authorization Group</dt><dd>&amp;NC&amp;</dd></dl></dd>

<dt>S_TRANSLAT</dt>

<dd><dl class="horizontal-dl"><dt>Activity</dt><dd>02</dd><dt>Target language</dt><dd>EN</dd></dl></dd>

## Expose an ODP data source as an OData service

You must expose each ODP data source through an OData service before the pipeline can extract it. You create the service in the SAP Gateway Service Builder (transaction `SEGW`), then register it in SAP Data Agent.

Record the following values as you complete this section. You must enter them in [`/WKTO/ODP_CONFIG`](#configure-the-data-source-in-sap-data-agent):

- ODP name
- Service name
- Entity name
- Delta entity name and terminate delta entity name, if the data source supports delta extraction
- Service URL

The examples in this section use the `0TCTAPPL_TEXT` data source.

### Create a Service Builder project

Complete the following steps to create a project in the SAP Gateway Service Builder:

1. Go to transaction code `SEGW`.
   
2. Click **Create Project**.
   
3. Enter a name for the project in the **Project** field and a description in the **Description** field. For example, `ZSAP_0TCTAPPL_TEXT` and `ODP for 0TCTAPPL_TEXT`.
   
4. Use the **Project Type** drop-down menu to select **Service with SAP Annotations**.
   
5. Use the **Generation Strategy** drop-down menu to select **Standard**.
   
6. Enter the package in the **Package** field, then save the project.
   
   ![Create new project](/assets/create-new-project-sap.BBxmeR-J.png)_Create new project_
   

### Redefine the data model for ODP extraction

Complete the following steps to assign the ODP data source to the project:

1. Right-click **Data Model** in the project tree and select **Redefine > ODP Extraction**.
   
   ![Redefine the service](/assets/redefine-service.BPzvK8g_.png)_Redefine the service_
   
2. Enter `NONE` in the **RFC Destination** field.
   
3. Use the **ODP Context** drop-down menu to select the context of the data source. For example, **DataSources Without ESH Modeling**.
   
4. Enter the data source name in the **ODP Name** field and click **Add ODP**. Record this value as the ODP name. For example, `0TCTAPPL_TEXT`.
   
   ![Add ODP](/assets/add-odp.CdGQjdYX.png)_Add ODP_
   
5. Click **Next**.
   
6. Review the transport, OData service, and service registration attributes. Record the value in the **Service Name** field. For example, `ZSAP_0TCTAPPL_TEXT_2_SRV`.
   
   ![Review attributes](/assets/review-attributes.CU29ib-z.png)_Review attributes_
   
7. Click **Next**.
   
8. Select the entity type and its properties. Record the entity type name as the entity name. For example, `EntityOf0TCTAPPL_TEXT`.
   
9. Click **Finish**.
   
10. Check the project and confirm that SAP reports no errors.
    

If the data source supports delta extraction, find the delta entity name and terminate delta entity name under **Function Imports** in the project.

Entity names are case-sensitive. Record them exactly as SAP displays them.

### Generate runtime objects

Complete the following steps to generate the required classes for the project:

1. Select the project and click **Generate Runtime Objects**.
   
2. Review the model provider class, data provider class, and service registration names in the **Model and Service Definition** dialog.
   
   ![Generate required classes](/assets/generate-required-classes.DonkoZAJ.png)_Generate required classes_
   
3. Confirm the dialog. SAP generates the runtime objects and registers the service and model.
   

### Register the service

Complete the following steps to register the service in the SAP Gateway hub:

1. Expand **Service Maintenance** in the project tree and select **GATEWAYLOCAL**.
   
2. Click **Register > Register Service**.
   
3. Confirm that the **Registration Status** shows green.
   
   ![Service registration with green registration status](/assets/service-registration-status.CNTdBUcx.png)_Service registration with green registration status_
   

### Test the service

Complete the following steps to test the service and retrieve its URL:

1. Go to transaction code `/IWFND/MAINT_SERVICE`.
   
2. Select the service and click **SAP Gateway Client**.
   
3. Click **Execute** and confirm that the response returns status code `200`.
   
4. Record the path in the **Request URI** field as the service URL. For example, `/sap/opu/odata/SAP/ZSAP_0TCTAPPL_TEXT_2_SRV`.
   

## Configure the data source in SAP Data Agent

You must register each ODP data source in SAP Data Agent. This configuration maps the data source to the OData service and entities that the pipeline uses for extraction.

Go to transaction code `/WKTO/ODP_CONFIG` and maintain the following fields for each data source:

| Field | Description |
| --- | --- |
| Data source name | The technical name of the ODP data source. For example, `0TCTAPPL_TEXT`. |
| Service name | The OData service name created by the **Redefine > ODP Extraction** wizard. |
| Context | The ODP context of the data source, such as `SAPI`, `ABAP_CDS`, `HANA`, or `BW`. |
| URL | The relative OData path of the service. |
| Entity name | The primary entity name used for data extraction. |
| Delta entity name | The entity name used for delta changes. Find it under **Function Imports** in the Service Builder project. |
| Terminate delta entity name | The entity name used to terminate or reset delta extraction. Find it under **Function Imports** in the Service Builder project. |
| Long description | A description of the data source. Enter this value for non-`SAPI` data sources only. |
| Max page | The maximum number of records returned in each extraction response. We recommend `50,000` for overall throughput. |

Entity names are case-sensitive and must match the values configured in the service exactly.

## Establish OData connectivity between Workato and SAP

You must configure connectivity between Workato and the SAP system before creating a data pipeline.

SAP Data Agent exposes OData services that Workato uses for authentication, extraction, and cleanup operations.

### Connect to SAP on-premise systems

Deploy a Workato on-prem agent (OPA) if your SAP system doesn't expose OData services to the public internet. The on-prem agent establishes a secure outbound connection from your network to Workato and enables access to internal SAP OData services.

Complete the following steps to connect to SAP on-premise systems:

1. Install and register a Workato on-prem agent in your workspace.
   
2. Ensure the SAP system exposes the required OData services under the `/WKTO/` namespace.
   
3. Verify network connectivity between the on-prem agent host and the SAP application server.
   

### Connect without an on-prem agent

Whitelist [Workato IP addresses](/en/security/ip-allowlists) on the SAP HTTPS port to allow inbound traffic from Workato. You can find the HTTPS port in transaction `SMICM` or SAP Web Dispatcher. Ensure the SAP OData service endpoint remains externally accessible over HTTPS.

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

After you install SAP Data Agent, expose your data sources, and establish connectivity, create a data pipeline to extract data from ODP data sources.

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
   
4. Use the **Source interface** drop-down menu to select **SAP ODP2**.
   
5. Enter the ODP context in the **ODP2 context** field. The context determines which objects are available for extraction.
   
   ![Configure SAP ODP2 context](/assets/configure-sap-odp2-context.2NCpIm7D.png)_Configure SAP ODP2 context_
   
6. Click **Add object** to select the ODP data source to extract.
   
7. Enter at least three uppercase characters of the data source name in the search field. Data source names are case-sensitive and use uppercase letters.
   
   ![Add new objects](/assets/add-objects-sap.CEZ8IHjX.png)_Add new objects_
   
8. Select the data sources from the search results. Each result shows the data source description, service name, delta type, and ODP name. For example, `Purchasing Data (Header Level) [Service = ZODP_02_HDR_1_SRV] [Delta = ABR] (2LIS_02_HDR)`.
   
   ![Select data sources](/assets/select-sources-sap.sIbwcd3m.png)_Select data sources_
   
9. Click **Add** to confirm the selection.
   

### Select the sync mode

Complete the following steps to configure the sync mode for each object:

1. Click the settings icon for the object in the **Objects** section.
   
2. Use the **Sync mode** drop-down menu to select **Full sync** or **Incremental sync**.
   
   ![Configure sync mode](/assets/configure-sync-mode-sap.CNoYHB3S.png)_Configure sync mode_
   
3. Optional. Enter an SAP filter expression in the **Data filter condition** field to filter the source data. For example, `BUKRS = '1000'`.
   
4. Click **Save**.
   

The sync modes behave in the following ways:

- **Full sync**: Extracts all available records from the data source, regardless of previous syncs or existing delta subscriptions. Use this mode when you need a complete snapshot of the source data or plan to reload the entire dataset.
- **Incremental sync**: Performs a delta initialization on the first run to establish the extraction pointer and retrieve the initial dataset, depending on the delta capability of the data source. Later runs extract only the records that changed after the last successful incremental sync.

> **ONE SERVICE PER INCREMENTAL PIPELINE**
> 
> You can use an ODP service for incremental sync in only one pipeline. Create a separate ODP service in SAP for each pipeline if you plan to use the same data source in multiple incremental pipelines. This restriction doesn't apply to full sync. Refer to [Pipeline can't run because the service is in use by another pipeline](/en/data-orchestration/data-pipeline-recipe/configure-sap-table-reader-troubleshooting#odp-service-in-use-by-another-pipeline) for more information.

#### Data sources based on setup tables

Data sources based on setup tables, mainly `2LIS*` data sources, behave differently during full and incremental extraction:

- Full and initial loads read data from setup tables. SAP fills setup tables from application tables, usually as a one-time activity.
- Setup tables don't refresh automatically. New or updated records don't appear in full or initial loads unless you reload the setup tables.
- The initial load activates the delta mechanism. Later delta loads read only new or changed records from the delta queue and don't rely on setup tables.

You may miss delta records generated after the setup table load if you terminate an existing incremental pipeline and start a new extraction from scratch. Continue using the same pipeline and avoid terminating or restarting the extraction to capture all delta records.

### Define the schema

The pipeline automatically fetches the schema for each selected object after you add the data sources. Review and customize the schema to ensure the destination matches the source:

1. Expand any object to view the list of available fields.
   
2. Keep all fields selected to extract all data, or deselect specific fields to exclude them from extraction and schema replication.
   
3. Optional. Configure field-level data protection for each non-key field:
   
   - **Replicate as is (default)**: Data values at the source are replicated identically to the destination.
   - **Hash**: Hash sensitive data values in the column before syncing to your destination.
4. Click **Add object** again to add more objects using the same flow. You can repeat this step to include multiple data sources in your pipeline.
   
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
   
   Re-sync operations don't count toward the concurrency limit. Each re-sync consumes a separate work process in SAP. Adjust concurrency carefully to avoid excessive load on the SAP system.
   
2. Set the **Frequency**.
   
   Frequency defines how often the pipeline runs, such as every few minutes, hourly, or daily. Select a frequency that balances data freshness with SAP system performance and stability.
   
   ![Configure frequency](/assets/configure-frequency.BlbzJx4B.png)_Configure frequency_
   
   Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from SAP ODP to the destination.
   
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

After the pipeline finishes extracting data, the SAP ODP framework cleans up the temporary data staged in SAP.

![Completed sync](/assets/completed-sync-sap.BrWCO2qs.png)_Completed sync_

The sync mode determines how the pipeline loads data into the destination:

- **Full sync**: The pipeline replaces existing data in the destination with the latest extracted dataset.
- **Incremental sync**: The pipeline adds newly extracted records to the existing data in the destination.

You can monitor extraction requests in SAP using transaction code `ODQMON`.
