---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-sql-server-source.md
description: >-
  Configure SQL Server as a data pipeline source to extract table records
  through an on-prem agent and sync them incrementally with Change Tracking or
  Change Data Capture.
---

# Configure SQL Server as a data pipeline source

Set up SQL Server as a data pipeline source to extract and sync records into your destination. Use this guide to set up a connection, configure your pipeline, add objects, review sync behavior, and understand known limitations.

## SQL Server features supported

The following features are supported when you use SQL Server as a pipeline source:

| Feature | Details |
| --- | --- |
| On-prem connectivity | Connect to SQL Server through an on-prem group. Cloud connections aren't supported for data pipelines. |
| Full sync and incremental sync | Supports full sync and incremental sync modes. Incremental sync uses SQL Server Change Tracking or Change Data Capture (CDC). CDC is the default when both are enabled on a table. Refer to [Sync modes](#sync-modes) for more information. |
| Table-level object selection | Select individual SQL Server tables to sync as objects in your pipeline. Tables across multiple schemas in the connected database are supported. Refer to [Configure the pipeline](#configure-the-pipeline) for more information. |
| Schema drift detection and handling | Detect and apply schema changes automatically with **Auto-sync new fields**, or keep the schema fixed with **Block new fields**. |
| Configurable sync frequency | Schedule syncs on a time-based interval. The minimum supported interval is `15` minutes. |

## SQL Server prerequisites

Connecting SQL Server as a data pipeline source requires:

- A SQL Server instance reachable from your on-prem agent host
- An on-prem agent running version **30 or above**. Refer to the [on-prem agent documentation](/en/on-prem/agents/run) for setup steps.
- A SQL Server user with `SELECT` and `VIEW DEFINITION` permissions on the tables you plan to sync. Incremental sync requires additional permissions, such as `VIEW CHANGE TRACKING`. Refer to [Enable Change Tracking](#enable-change-tracking) or [Enable Change Data Capture](#enable-change-data-capture) for more information.
- A primary key on each table you plan to sync
- The host, port, database name, username, and password for your SQL Server instance
- Change Tracking or CDC enabled on your SQL Server database and on each table you plan to sync incrementally. Refer to [Enable Change Tracking](#enable-change-tracking) or [Enable Change Data Capture](#enable-change-data-capture) for setup steps.

## Enable Change Tracking

Incremental sync by Change Tracking uses SQL Server Change Tracking to detect row-level inserts, updates, and deletes. Your database administrator must enable it at both the database and table level before the pipeline can run incremental syncs with this method. Refer to the Microsoft [Enable and disable change tracking](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-tracking-sql-server) documentation for more information.

Enable Change Tracking at the database level:

```sql
ALTER DATABASE CURRENT SET CHANGE_TRACKING = ON (CHANGE_RETENTION = 7 DAYS, AUTO_CLEANUP = ON)
```

Set a data retention period longer than the longest time period a pipeline can be paused, including planned maintenance. Workato recommends a minimum retention of 3 days. Seven days provides a safe buffer if pipelines are paused or delayed. Incremental sync fails if a pipeline is paused longer than the retention period. Refer to [Change history retention](#change-history-retention) for more information.

Enable Change Tracking at the table level for each table you plan to sync:

```sql
ALTER TABLE [schema].[table_name] ENABLE CHANGE_TRACKING WITH (TRACK_COLUMNS_UPDATED = ON)
```

Repeat the table-level command for each table you plan to add as an object in your pipeline. `TRACK_COLUMNS_UPDATED = ON` is optional. It records which columns changed, which uses additional storage.

Grant the Workato user the `VIEW CHANGE TRACKING` permission on each table you plan to sync incrementally. Workato requires this permission to query the Change Tracking log:

```sql
GRANT VIEW CHANGE TRACKING ON OBJECT::[schema].[table_name] TO [workato_user]
```

Use `ON SCHEMA::[schema]` instead of `ON OBJECT::[schema].[table_name]` to grant the permission on every table in a schema.

## Enable Change Data Capture

Incremental sync by Change Data Capture (CDC) reads net changes from SQL Server CDC change tables. Refer to the Microsoft [Enable and disable change data capture](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-data-capture-sql-server) documentation for more information.

Ensure you meet the following requirements to use CDC:

- CDC is enabled at the database and table level by your database administrator
- SQL Server Agent is running
- You have SQL Server Enterprise, Standard, or Developer edition

> **UNSUPPORTED EDITIONS**
> 
> SQL Server Express and Web editions don't support CDC.

### Enable CDC at the database level

Run the following command to enable CDC on your database. This command requires the `sysadmin` role:

```sql
USE <your_database>;
EXEC sys.sp_cdc_enable_db;
```

### Enable CDC at the table level

Run the following command for each table you plan to sync. This command requires the `db_owner` role:

```sql
EXEC sys.sp_cdc_enable_table
    @source_schema = N'<schema>',
    @source_name   = N'<table_name>',
    @role_name     = NULL,
    @supports_net_changes = 1;
```

You must set `@supports_net_changes = 1`. Workato reads net changes, which collapse multiple changes to the same row into a single row with its final state. Net changes require a primary key or a unique index specified with `@index_name`, and Workato requires a primary key on every table you sync. Workato can't use CDC on tables enabled without net changes.

### Grant access to CDC change data

Run the following command to let the Workato user read CDC change data:

```sql
GRANT SELECT ON SCHEMA::cdc TO <workato_user>;
```

The table-level example sets `@role_name` to `NULL`, so no gating role restricts access to the change data. If you specify a gating role, add the Workato user to it:

```sql
ALTER ROLE <gating_role> ADD MEMBER <workato_user>;
```

### Verify that SQL Server Agent is running

Ensure that SQL Server Agent is running. CDC captures changes through a SQL Server Agent job, so the change tables stay empty until the agent runs. SQL Server Agent is disabled by default on Linux. Run the following commands to enable it and restart SQL Server:

```shell
sudo /opt/mssql/bin/mssql-conf set sqlagent.enabled true
sudo systemctl restart mssql-server
```

For a new SQL Server container, set the `MSSQL_AGENT_ENABLED=true` environment variable when you create the container instead.

Keep SQL Server Agent running while CDC is enabled. SQL Server can't truncate the transaction log past changes the capture job hasn't read, so the log can keep growing while the capture job is stopped.

### Confirm CDC is enabled

Run the following query to confirm CDC is enabled with net changes on a table:

```sql
SELECT capture_instance, supports_net_changes
FROM cdc.change_tables
WHERE OBJECT_SCHEMA_NAME(source_object_id) = '<schema>'
  AND OBJECT_NAME(source_object_id) = '<table_name>';
```

## Supported connection types

SQL Server pipelines support username and password authentication through an on-prem group. You must have a SQL Server username and password to connect.

> **CLOUD CONNECTIONS NOT SUPPORTED**
> 
> Cloud connections aren't supported as a data pipeline source for SQL Server. You must select an on-prem group in the **Connection type** field.

## Connect to SQL Server

Complete the following steps to connect SQL Server as a data pipeline source.

1. Select **Create > Connection** or press C twice.
   
2. Search for `SQL Server` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Configure your SQL Server connection](/assets/configure-sql-server-connection.BbLIrr-y.png)_Configure your SQL Server connection_
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Select an on-prem group in the **Connection type** field.
   
   Don't select **Cloud**. Cloud connections aren't supported for SQL Server as a data pipeline source and prevent objects from loading.
   
6. Enter the hostname of your SQL Server instance in the **Host** field.
   
7. Enter the port number in the **Port** field. The default SQL Server port is `1433`.
   
8. Enter your SQL Server username in the **Username** field.
   
9. Enter your SQL Server password in the **Password** field.
   
10. Enter the name of the database you plan to sync in the **Database** field.
    
11. Optional. Expand **Advanced settings** to configure the following:
    
    | Field | Description |
    | --- | --- |
    | Use improved datetime handling | Enable enhanced handling of `datetime`, `datetime2`, and `datetimeoffset` data types. Defaults to true. Refer to the [Improved datetime handling](/en/connectors/mssql/introduction#improved-datetime-handling) section for more information. |
    | Database timezone | Set the local timezone of your database. When timezones are provided for `datetime` and `datetime2` values, Workato converts them to this timezone before processing. Default is UTC. |
    
12. Optional. Expand **SSL settings** to configure certificate-based security for your connection:
    
    | Field | Description |
    | --- | --- |
    | Server certificate | Provide the X.509 server certificate in `.pem` format. |
    | SSL certificate | Provide the X.509 client certificate in `.pem` format. |
    | SSL certificate key | Provide the RSA client key in `.pem` format. |
    | Trust all | Forces the client to trust any certificate chain. Enables support for self-signed server certificates. |
    
13. Optional. Expand **Pooling settings** to configure connection pool behavior:
    
    | Field | Description |
    | --- | --- |
    | Minimum pool size | Enter the minimum number of connections the on-prem agent maintains in the pool, including idle and in-use connections. Default is `1`. |
    | Maximum pool size | Enter the maximum number of connections in the pool. When the pool reaches this quota and no idle connections are available, new connection attempts block until the timeout is reached. Default is `10`. |
    | Idle timeout | Enter the maximum time, in seconds, a connection can sit idle in the pool before removal. A value of `0` means connections aren't removed. Default is 600 seconds (10 minutes). |
    | Maximum lifetime | Enter the maximum lifetime, in seconds, of a connection in the pool. Connections that reach this quota are removed even if they were recently used. Default is 1800 seconds (30 minutes). |
    | Timeout | Enter the maximum time, in seconds, to wait for a connection from the pool. A value of `0` means no timeout. Default is 30 seconds. |
    
14. Optional. Expand **Additional properties for SQL Server connection** and select **Add parameter** to pass additional JDBC connection parameters.
    
15. Select **Connect** to verify and save the connection.
    

## Configure the pipeline

Complete the following steps to configure SQL Server as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from SQL Server.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **SQL Server**.
   
7. Choose the SQL Server connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Click **Add object** to open the **Add new objects** panel.
   
   ![Add objects](/assets/add-objects-sql-server.DlufU4YO.png)_Add objects_
   
9. Search or browse the list of available SQL Server objects, select the objects you plan to sync, and click **Add**.
   
10. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields.
    
12. Click **Add object** again to add more objects. Repeat this step to include additional SQL Server objects in your pipeline.
    
13. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
14. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from SQL Server to the destination.
    
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
       
    

## Supported SQL Server objects

SQL Server data pipelines sync data from tables in your connected database. Workato discovers available tables across all schemas in the connected database when you select **Add object** during pipeline configuration. You can add one or more tables as objects in your pipeline. Views aren't supported. Tables without Change Tracking or CDC enabled are still listed and can use full sync.

## Sync modes

SQL Server data pipelines support full sync and incremental sync. The sync mode is configured per object when you add it to your pipeline.

### Full sync

A full sync reads all rows from the source table on every pipeline run. Use full sync for tables where you need a complete snapshot of the data on each sync.

Each table merges into the existing destination table, so rows deleted in SQL Server stay in the table.

### Incremental sync

An incremental sync extracts only rows that changed since the last successful sync run. Workato supports the following incremental sync methods:

- **Change Data Capture (CDC)**: Available when CDC is enabled on the table with net changes. Workato reads net inserts, updates, and deletes from the table's CDC change tables. Refer to [Enable Change Data Capture](#enable-change-data-capture) for setup steps.
- **Change Tracking**: Available when Change Tracking is enabled on the database and table. Workato queries the Change Tracking log to detect row-level inserts, updates, and deletes. Refer to [Enable Change Tracking](#enable-change-tracking) for setup steps.

Workato uses CDC by default when a table has both CDC and Change Tracking enabled. You can change the incremental sync method for the object.

### Delete tracking

Incremental sync by CDC or Change Tracking reports deleted rows through the synthetic `_workato_is_deleted` column. Deleted rows keep key column values, so the destination can identify which rows were deleted. Full sync doesn't track deletes. Refer to [Full sync](#full-refresh) for more information.

## Identifier handling

Workato pipelines translate source column names into valid destination identifiers by applying the following rules:

- Column names are uppercased.
- Special characters such as `$`, spaces, or dashes are replaced with underscores (`_`).
- Identifiers are wrapped in square brackets to protect against reserved words.

For example, the source column `$Name$` becomes `[_NAME_]` in the destination table.

## SQL Server limitations

The following limitations apply when you use SQL Server as a data pipeline source:

### No objects displayed

If the pipeline doesn't display objects when you select **Add object**, check that you selected an on-prem group in the **Connection type** field. The pipeline can't discover tables over a cloud connection.

![No objects error](/assets/no-objects-error.DmLxbr8j.png)_No objects error_

### Change history retention

Incremental sync by Change Tracking or CDC depends on the change history SQL Server retains. If a pipeline is paused longer than the retention window, its saved cursor falls outside the retained history and the next run fails. You must [re-sync the object](/en/data-orchestration/sync-types#object-re-sync) to resume incremental sync.

CDC cleans up change data after three days by default. Run the following command to increase the CDC retention period if you expect long pauses. The `@retention` value is in minutes, and this example sets retention to seven days:

```sql
EXEC sys.sp_cdc_change_job @job_type = N'cleanup', @retention = 10080;
```

The new value applies the next time the cleanup job runs. Run `SELECT job_type, retention FROM msdb.dbo.cdc_jobs;` to confirm the setting.

Refer to [Enable Change Tracking](#enable-change-tracking) for the Change Tracking retention setting.

### Column changes after CDC is enabled

CDC doesn't capture columns added to a table after CDC was enabled on it, so those columns don't sync. Your database administrator must create a new capture instance for the table or disable and re-enable CDC to capture new columns. Run a full sync on the object to include the new columns. Workato uses the most recently created capture instance when a table has two capture instances.

Columns dropped after CDC is enabled appear as `NULL` values in later changes.

### Switching incremental sync methods

Change Tracking and CDC store different types of cursors, and neither method can resume from the other's cursor. The next run fails if you change the incremental sync method for an existing object. Run a full sync on the object to reinitialize the cursor.

### On-prem agent version requirement

Workato requires on-prem agent version **30 or above** to support SQL Server data pipelines. Earlier versions aren't supported. Workato recommends using the latest available version.

### Minimum sync frequency

The minimum supported sync interval is 15 minutes.
