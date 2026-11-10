---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-mysql-source.md
description: >-
  Configure MySQL as a data pipeline source to extract table records and sync
  them with your destination.
---

# Configure MySQL as a data pipeline source

Set up MySQL as a data pipeline source to extract and sync table records into your destination. Use this guide to set up a connection, configure your pipeline, add objects, and review known limitations.

## MySQL features supported

The following features are supported when you use MySQL as a pipeline source:

- **On-prem connectivity**: Connect to MySQL through an on-prem group. Cloud connections aren't supported for data pipelines.
- **Table-level object selection**: Select individual MySQL tables to sync as objects in your pipeline.
- **Schema drift detection and handling**: Detect and apply schema changes automatically with **Auto-sync new fields**, or keep the schema fixed with **Block new fields**.
- **Configurable sync frequency**: Schedule syncs on a time-based interval or with a cron expression. The minimum supported interval is 15 minutes.

## MySQL prerequisites

Connecting MySQL as a data pipeline source requires:

- A MySQL instance reachable from your on-prem agent host
- A MySQL user account granted `SELECT` permission on the tables you plan to sync. Refer to [Permissions required to connect](#permissions-required-to-connect) for setup steps.
- The host, port, database name, username, and password for your MySQL instance

### Permissions required to connect

At a minimum, the database user account must have the `SELECT` permission on the database you plan to sync.

Create a dedicated user for Workato and grant it read-only access to the target database. The following example grants `SELECT` on a database named `HR_PROD` to a new user `workato`:

```sql
CREATE USER 'workato' IDENTIFIED BY 'password';
GRANT SELECT ON `HR_PROD`.* TO 'workato';
```

## Supported connection types

MySQL data pipelines support username and password authentication through an on-prem group. You must have a MySQL username and password to connect.

> **CLOUD CONNECTIONS NOT SUPPORTED**
> 
> Cloud connections aren't supported as a data pipeline source for MySQL. You must select an on-prem group in the **Connection type** field.

## Connect to MySQL

Complete the following steps to connect to MySQL:

Connect to MySQL

1. Select **Create > Connection** or press C twice.
   
2. Search for `MySQL` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select an on-prem group in the **Connection type** field.
   
   Don't select **Cloud**. Cloud connections aren't supported for MySQL as a data pipeline source and prevent objects from loading.
   
6. Enter the hostname of your MySQL instance in the **Host** field.
   
7. Enter the port number in the **Port** field. The default MySQL port is `3306`.
   
8. Enter your MySQL username in the **Username** field.
   
9. Enter your MySQL password in the **Password** field.
   
10. Enter the name of the database to sync in the **Database** field.
    
11. Optional. Expand **Advanced settings** to configure the following:
    
    1. Toggle **Use improved datetime handling** to enable enhanced handling of `date`, `datetime`, and `timestamp` data types. Defaults to true.
       
    2. Set the **Database timezone** field to the local timezone of your database. Default is UTC.
       
12. Select **Connect** to verify and save the connection.
    

## Configure the pipeline

Complete the following steps to configure MySQL as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from MySQL.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **MySQL**.
   
7. Choose the MySQL connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Click **Add object** to open the **Add new objects** panel.
   
   ![Add objects](/assets/add-objects-mysql.BORTkxs0.png)_Add objects_
   
9. Search or browse the list of available MySQL objects, select the objects to sync, and click **Add**.
   
10. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields.
    
12. Click **Add object** again to add more objects. Repeat this step to include additional MySQL objects in your pipeline.
    
13. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
14. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from MySQL to the destination.
    
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
       
    

## Supported MySQL objects

MySQL data pipelines sync data from tables in your connected database.

## MySQL limitations

The following limitations apply when you use MySQL as a data pipeline source:

### Minimum sync frequency

The minimum supported sync interval is 15 minutes.
