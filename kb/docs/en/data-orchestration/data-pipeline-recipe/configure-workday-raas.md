---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-workday-raas.md
description: >-
  Configure Workday RaaS as a data pipeline source to extract custom report data
  from your tenant and sync it to your destination.
---

# Configure Workday RaaS as a data pipeline source

Set up Workday RaaS to extract custom report data from your Workday tenant and sync to your destination. Use this guide to register a custom report as a pipeline object, configure incremental sync through report prompts, and understand known limitations.

## Workday RaaS features supported

The following features are supported when you use Workday RaaS as a pipeline source:

- **Authentication**: Inherits the Workday connection authentication type. OAuth 2.0 is required to work with custom objects and Workday Query Language (WQL). Refer to [Supported connection types](#supported-connection-types) for more information.
- **Object selection**: Register Workday custom reports as pipeline objects by providing the report URL. Refer to [Configure the pipeline](#configure-the-pipeline) for more information.
- **Full refresh and incremental sync**: Supports full refresh and incremental sync modes. Incremental sync uses date prompts configured on the custom report. Refer to [Sync modes](#sync-modes) for more information.
- **Field-level selection**: Include or exclude individual report columns from the sync after you register the report as a pipeline object.
- **Schema drift detection and handling**: Detect and apply schema changes automatically with **Auto-sync new fields**, or keep the schema fixed with **Block new fields**.
- **Configurable sync frequency**: Schedule syncs on a time-based interval or with a cron expression. The minimum supported interval is 15 minutes.

## Workday RaaS prerequisites

Complete the following requirements before you configure Workday RaaS as a data pipeline source:

- A configured Workday data pipeline source connection. Refer to the [Connect to Workday](#connect-to-workday) section for connection setup steps.
- An **Advanced** type custom report in your Workday tenant that is enabled as a web service. Only Advanced custom reports can be exposed through RaaS.
- The Integration System User (ISU) configured on your Workday connection must have permission to run the custom report and access the data sources the report uses.
- For incremental sync, the custom report must include two date prompts (a start date prompt and an end date prompt) and corresponding filter conditions on a date field. Refer to [Configure date prompts and filters](#configure-date-prompts-and-filters) for setup steps.

## Supported connection types

Workday pipelines support cloud and on-prem connections, with OAuth 2.0 or basic authentication.

### Connection type

Workato reaches your Workday tenant through one of the following routes:

- **Cloud**: Connect directly from Workato's cloud to your Workday tenant.
- **On-prem group**: Connect through an on-prem group when network or security policy requires it.

### Authentication type

The authentication type determines whether the pipeline can access custom objects and Workday Query Language (WQL) data, and how the connection authenticates against your tenant.

- **OAuth 2.0**: Authenticate through a registered API client for integrations in Workday using a non-expiring refresh token. OAuth 2.0 is required to work with custom objects and WQL.
- **Basic authentication**: Authenticate with the ISU login name and password. Custom objects and WQL aren't available with this type.

## Connect to Workday

Complete the following steps to connect Workday as a data pipeline source. Select the tab that matches the authentication type you plan to use.

Connect to Workday

**OAuth 2.0**

1. Select **Create > Connection** or press C twice.
   
2. Search for `Workday` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Configure your Workday connection](/assets/configure-workday-connection-oauth.CBpiqpm9.png)_Configure your Workday connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**.
   
6. Select **OAuth 2.0** in the **Authentication type** field. This method is required to work with custom objects and to query data using Workday Query Language (WQL) with the Workday REST API.
   
7. Enter your Workday tenant ID in the **Tenant ID** field. Your tenant ID is the value that appears in the URL when you log in to Workday. For example, in `https://impl.workday.com/sample_company/d/home.htmld`, the tenant ID is `sample_company`.
   
8. Enter your Workday WSDL URL in the **WSDL URL** field. For example, `https://wd2-impl-services1.workday.com/ccx/service/`.
   
9. Enter the client ID from your Workday API client settings in the **Client ID** field.
   
10. Enter the client secret from your Workday API client settings in the **Client secret** field.
    
11. Enter your non-expiring refresh token in the **Refresh token** field. Refer to [Generate a non-expiring refresh token](/en/connectors/workday#register-api-client) for steps.
    
12. Enter the authorization endpoint from your Workday API client settings in the **Authorization endpoint** field.
    
13. Enter the token endpoint from your Workday API client settings in the **Token endpoint** field.
    
14. Use the **Workday tenant timezone** drop-down menu to select the timezone configured in your Workday tenant. Workday returns data effective from the current day in PST by default. Selecting a timezone ensures retrieved data is consistent with your tenant.
    
15. Optional. Expand **Advanced settings** to configure the **Advanced XML payload for multiple ID values**.
    
    Workato wraps each value in fields with multiple values within its own container by default when constructing the XML from your input.
    
    For example:
    
    ```
    <languages><language>english</language></languages><languages><language>chinese</language></languages>
    ```
    
    Workato unwraps these values and presents them in a single container if you set the value to **Yes**:
    
    ```
    <languages><language>english</language><language>chinese</language></languages>
    ```
    
    Consider enabling this when you encounter invalid payload errors.
    
16. Use the **Workday web services version** drop-down menu to select the API version you plan to use. Defaults to `45.1`. Refer to [API version](/en/connectors/workday#api-version) for the supported version list and version support policy.
    
17. Select **Connect** to verify and save the connection.
    

**Basic authentication**

1. Select **Create > Connection** or press C twice.
   
2. Search for `Workday` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Configure your Workday connection](/assets/configure-workday-connection-basic.DZeY_AC0.png)_Configure your Workday connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**.
   
6. Use the **Authentication type** drop-down menu to select **Basic**.
   
7. Enter your Workday tenant ID in the **Tenant ID** field.
   
8. Enter your Workday WSDL URL in the **WSDL URL** field.
   
9. Enter the ISU login name in the **Login name** field.
   
10. Enter the ISU password in the **Password** field.
    
11. Use the **Workday tenant timezone** drop-down menu to select the timezone configured in your Workday tenant.
    
12. Optional. Expand **Advanced settings** to configure the **Advanced XML payload for multiple ID values**.
    
    Workato wraps each value in fields with multiple values within its own container by default when constructing the XML from your input.
    
    For example:
    
    ```
    <languages><language>english</language></languages><languages><language>chinese</language></languages>
    ```
    
    Workato unwraps these values and presents them in a single container if you set the value to **Yes**:
    
    ```
    <languages><language>english</language><language>chinese</language></languages>
    ```
    
    Consider enabling this setting if you encounter invalid payload errors.
    
13. Use the **Workday web services version** drop-down menu to select the API version you plan to use. Defaults to `45.1`.
    
14. Select **Connect** to verify and save the connection.
    

## Configure date prompts and filters

Configure two date prompts and two filter conditions on your custom report to support incremental sync.

> **INCREMENTAL SYNC IS OPTIONAL**
> 
> Workday RaaS pipelines use full refresh by default. Incremental sync is an optional feature you can use to fetch data in chunks rather than reloading the entire report on every run. It's most useful for large reports where a full refresh on each sync isn't practical. You design the report prompts and filters that drive the date range. Skip this section if you only plan to use full refresh.

### How incremental sync works

Workday custom reports accept parameters through prompts. Each prompt is a named slot the report exposes through its web service URL. Filter conditions reference these prompts to limit the records the report returns. Incremental sync uses two prompts on the same date field to define a date range, paired with two filter conditions that apply the range.

Workato passes the following values on each incremental sync run:

- **Prompt #1** receives the timestamp of the last successful sync, or the historical start date on the first run.
- **Prompt #2** receives the current timestamp at the start of the sync run.

The XML alias you set on each prompt is the parameter name Workato sends in the report URL. You must enter the same alias values in the **Start date prompt** and **End date prompt** fields when you register the report as a pipeline object in Workato.

Set the **Comparison Type** on both filter conditions to **Prompt the user for the value and ignore the filter condition if the value is blank**. This setting lets the report return all records when prompt values aren't provided, which supports full refresh sync without removing the filters.

### Configure the report

Complete the following steps in Workday. Edit an existing custom report or create a new one. The configuration is the same in both cases.

1. Open the custom report. If you're editing an existing report, select **Actions > Custom Report > Edit**. If you're creating a new report, complete the report creation flow in Workday and continue with the next step once you're on the **Edit Custom Report** screen.
   
2. Confirm that **Report Type** is set to **Advanced** and that **Enable As Web Service** is selected.
   
3. Select the **Columns** tab and confirm that the date field you plan to filter on, such as `Last Functionally Updated`, is included as a column. Add the column if it isn't present.
   
   ![Add column](/assets/add-column-workday.BanyVD9-.png)_Add column_
   
4. Select the **Prompts** tab and locate the **Prompt Defaults** table.
   
5. Add a prompt for the start of the incremental date range:
   
   1. Select the **+** icon to add a new row to the **Prompt Defaults** table.
      
   2. Select the date field, such as `Last Functionally Updated`, in the **Field** column.
      
   3. Use the **Prompt Qualifier** drop-down menu to select **Prompt #1**.
      
   4. Enter an XML alias, such as `Updated_From_f`, in the **Label For Prompt XML Alias** column. Record this value. You must enter the same alias in the Workato **Start date prompt** field.
      
   5. Use the **Default Type** drop-down menu to select **No default value**.
      
6. Add a prompt for the end of the incremental date range:
   
   1. Select the **+** icon to add another row to the **Prompt Defaults** table.
      
   2. Select the same date field in the **Field** column.
      
   3. Use the **Prompt Qualifier** drop-down menu to select **Prompt #2**.
      
   4. Enter an XML alias, such as `Updated_From_t`, in the **Label For Prompt XML Alias** column. Record this value. You must enter the same alias in the Workato **End date prompt** field.
      
   5. Use the **Default Type** drop-down menu to select **No default value**.
      
      ![Configure date prompts](/assets/configure-date-prompts.BqTTaLgD.png)_Configure date prompts_
      
7. Select the **Filter** tab and locate the **Filter on Instances** table.
   
8. Add a filter condition for the start of the date range:
   
   1. Select the **+** icon to add a new filter condition.
      
   2. Select the date field, such as `Last Functionally Updated`, in the **Field** column.
      
   3. Use the **Operator** drop-down menu to select **greater than or equal to**.
      
   4. Use the **Comparison Type** drop-down menu to select **Prompt the user for the value and ignore the filter condition if the value is blank**.
      
   5. Use the **Comparison Value** drop-down menu to select **Prompt #1**.
      
9. Add a filter condition for the end of the date range:
   
   1. Select the **+** icon to add another filter condition.
      
   2. Select the same date field in the **Field** column.
      
   3. Use the **Operator** drop-down menu to select **less than or equal to**.
      
   4. Use the **Comparison Type** drop-down menu to select **Prompt the user for the value and ignore the filter condition if the value is blank**.
      
   5. Use the **Comparison Value** drop-down menu to select **Prompt #2**.
      
      ![Configure filters](/assets/configure-filters.DOPZFG-1.png)_Configure filters_
      
10. Select **OK** to save the report.
    

> **REPORT URL**
> 
> Locate the base report URL after you save the report. Select **Actions > Web Service > View URLs**, then copy the JSON endpoint URL. Strip any query parameters from the URL before you paste it into Workato. You must enter this URL when you register the report as a pipeline object in Workato. Refer to [Configure the pipeline](#configure-the-pipeline).

## Configure the pipeline

Complete the following steps to configure Workday RaaS as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from Workday RaaS.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Workday RaaS**.
   
7. Choose the Workday RaaS connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Click **Add object** to open the **New object** panel and start on the **Configure report** step.
   
9. Enter the base report URL in the **Report URL** field. Paste the URL without query parameters. For example:
   
   ```text
   https://{domain}/ccx/service/customreport2/{tenant}/{owner}/{report_name}
   ```
   
   ![Configure report](/assets/raas-configure-report.Dn3N0oB3.png)_Configure report_
   
10. Optional. Enter a destination table name in the **Object name** field. Workato derives the name from the report URL if you leave this field blank. Use lowercase characters and underscores only.
    
11. Click **Fetch schema** to retrieve the report column list from Workday and continue to the **Review schema** step.
    
12. Review the discovered columns. Each column from the custom report appears in the schema list with its data type. Deselect any column you don't want to include in the sync.
    
13. Use the **Primary key** drop-down menu to select up to five columns to use as the primary key for the destination table. Select columns that uniquely identify each record and don't change between syncs, such as `Employee ID`. Avoid selecting columns that change frequently, such as timestamps, because Workato treats each changed value as a new row in the destination.
    
14. Optional. Select **\+ Add prompt** under **Additional prompts** to pass fixed values to other report prompts. Enter the prompt name and the static value to send on every sync run. Skip this step if your report doesn't have additional prompts to configure.
    
15. Optional. Select **Enable incremental sync** and enter the XML alias values you recorded when you configured the custom report in Workday. Refer to [Configure date prompts and filters](#configure-date-prompts-and-filters) if you haven't configured the report yet.
    
    - Enter the start date prompt XML alias, such as `Updated_From_f`, in the **Start date prompt** field.
    - Enter the end date prompt XML alias, such as `Updated_From_t`, in the **End date prompt** field.
    
    Both prompts are required when **Enable incremental sync** is selected. Workato displays a configuration error and disables the **Review object** button if either field is blank.
    
    ![Enable incremental sync](/assets/enable-incremental-sync.D0cISmwj.png)_Enable incremental sync and enter prompt aliases_
    
16. Click **Review object** to continue to the **Review object** step.
    
    ![Review object](/assets/review-object.VzkxX5JK.png)_Review object_
    
17. Confirm the report settings on the **Review object** step. The summary includes the report URL, the primary key, the object name, and the start and end date prompt aliases when incremental sync is configured. Click **Back** to revise any setting, or click **Finish** to register the report as a pipeline object.
    
18. Review and customize the schema for each selected object. When you select an object, the pipeline automatically fetches its schema to ensure the destination matches the source.
    
    ![Review schema](/assets/review-schema.aHN25p5R.png)_Review schema_
    
    Expand any object to view its fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
19. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields.
    
20. Click **Add object** again to add more reports. Repeat the preceding steps to include additional Workday custom reports in your pipeline.
    
21. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
22. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Workday RaaS to the destination.
    
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
       
    

Workato uses full refresh when **Enable incremental sync** is unchecked on the **Review schema** step.

## Sync modes

Workday RaaS pipelines support full refresh and incremental sync. The sync mode is set per object on the **Review schema** step of the **New object** panel.

### Full refresh

A full refresh sync runs the report without start and end date prompt values on every pipeline run. Use full refresh when you need a complete snapshot of the report on each sync, or when the report doesn't include date prompts.

Reports with a primary key merge into the existing destination table, so records deleted in Workday stay in the table. Reports without a primary key overwrite the destination table on every run.

Workato uses full refresh when **Enable incremental sync** is unchecked on the **Review schema** step.

### Incremental sync

An incremental sync runs the report with a date range and fetches only records updated within that range. Workato passes the following values to the date prompts you configured on the report:

- **Start date prompt**: The timestamp of the last successful sync run. On the first run, Workato uses the historical start date set in the **When first started, this pipeline should pick up records from** field on the pipeline frequency configuration, or fetches all records if that field is blank.
- **End date prompt**: The current date and time at the start of the sync run.

Incremental sync requires the following configuration:

- The custom report must include two date prompts and two matching filter conditions. Refer to [Configure date prompts and filters](#configure-date-prompts-and-filters) for setup steps.
- **Enable incremental sync** must be selected on the **Review schema** step.
- Both the **Start date prompt** and **End date prompt** fields must contain the XML aliases that match the prompts on the custom report.

If you enable incremental sync but the report doesn't include matching filter conditions, the report returns all records on every run instead of filtering by the date range.

## Schema and data type handling

Workato fetches the report schema from Workday when you register the report as an object. Each report column becomes a column in the destination table. Workato detects the data type for each column from the report schema. Date and timestamp columns appear with a calendar icon in the schema list.

After you register the report as a pipeline object, you can include or exclude individual columns from the sync in the pipeline's source trigger. Deselect a column's checkbox to remove it from the destination table.

## Workday RaaS limitations

The following limitations apply when you use Workday RaaS as a data pipeline source.

### Advanced report type required

Only Advanced custom reports can be enabled as web services and registered as pipeline objects. Simple type reports aren't supported.

### Report size limit

Workday enforces a 2 GB size limit for advanced custom reports that are enabled as web services. Refer to [Workday's documentation on custom reports for integrations](https://doc.workday.com/r/3DMnG~27o049IYFWETFtTQ/sGhnezv85Vfp9LabNN~EWw) for more information.

### Incremental sync requires report configuration

Incremental sync depends on date prompts and matching filter conditions configured on the custom report in Workday. Workato uses full refresh when **Enable incremental sync** is unchecked. When **Enable incremental sync** is checked but the report doesn't include matching filter conditions, the report returns all records on every run instead of filtering by the date range.

### Minimum sync frequency

The minimum supported sync interval is 15 minutes.
