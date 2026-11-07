---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-google-search-console.md
description: >-
  Set up Google Search Console as a data pipeline source to extract Search
  Analytics performance reports and site and sitemap data from the Google Search
  Console API and sync it to your destination.
---

# Configure Google Search Console as a data pipeline source

Set up Google Search Console as a data pipeline source to extract Search Analytics performance reports and site and sitemap data from the Google Search Console API and sync it to your destination.

Use this guide to review the features and prerequisites, connect Google Search Console as a data pipeline source, configure the pipeline, and understand the supported objects, sync modes, schema handling, sensitive data handling, and known limitations.

## Features supported

The following features are supported when you use Google Search Console as a pipeline source:

- **Cloud connectivity**: Connects to the Google Search Console API over HTTPS. An on-prem agent isn't required.
- **Automatic multi-property sync**: Every Search Console property your connection can access syncs automatically, including domain properties and URL-prefix properties. There's no property picker in Workato. Refer to [Every accessible property syncs automatically](#every-accessible-property-syncs-automatically) for more information.
- **Search type coverage**: Report objects sync the `web`, `image`, `video`, and `news` search types. Each report row includes a `search_type` column. Refer to [Synthetic columns](#synthetic-columns) for more information.
- **Object-level selection**: Choose from the supported Search Analytics reports and the site and sitemap tables. Refer to [Supported objects](#supported-objects) for the full list.
- **Incremental sync**: All report objects sync incrementally by constraining the report's date range. Refer to [Sync modes](#sync-modes) for more information.
- **Schema drift detection and handling**: Detect and apply schema changes automatically with **Auto-sync new fields**, or keep the schema fixed with **Block new fields**.
- **Field-level data protection**: Hash or replicate sensitive fields as is before the data reaches your destination.
- **Configurable sync frequency**: Schedule syncs on a time-based interval or with a cron expression. The minimum supported interval is 15 minutes.

## Prerequisites

Connecting Google Search Console as a data pipeline source requires:

- A Google account with access to at least one Search Console property as an owner, full user, or restricted user. Workato syncs every property this account can access. The connection fails if the account has no property at one of these levels. Refer to [Every accessible property syncs automatically](#every-accessible-property-syncs-automatically) for more information.
- A Google Cloud project with the Google Search Console API enabled, an OAuth 2.0 client for that project, and a [custom OAuth profile](/en/custom-oauth-profiles) built from that client's ID and secret. The connection form requires a custom OAuth profile. Refer to [Connect to Google Search Console](#connect-to-google-search-console) for setup steps.

> **REQUIRED PERMISSIONS**
> 
> Workato requests the `https://www.googleapis.com/auth/webmasters.readonly` scope. This read-only scope covers every supported object. Workato doesn't request the read and write `webmasters` scope.

## Supported connection types

Google Search Console data pipelines support OAuth 2.0 authentication:

- **OAuth 2.0**: Authorize Workato using a custom OAuth profile built from a Google Cloud OAuth app that you create. Refer to [Create a Google Cloud OAuth app](#create-a-google-cloud-oauth-app) for setup steps. Service account authentication isn't supported.

## Connect to Google Search Console

Complete the following steps to connect Google Search Console as a data pipeline source:

Connect to Google Search Console

### Create a Google Cloud OAuth app

You must create a Google Cloud OAuth app and a Workato custom OAuth profile before you connect Google Search Console as a data pipeline source.

1. Go to **Tools > Custom OAuth profiles** in Workato and click **\+ New custom profile**.
   
2. Use the **Application** drop-down menu to select **Google Search Console**.
   
3. Enter a name in the **Name** field. The name can contain spaces but no special characters, and it must be unique for your account.
   
4. Click **Create new app**. Keep the Workato tab open.
   
5. Sign in to your [Google Cloud Console](https://console.cloud.google.com/welcome/new) in a new tab and select or create a project.
   
6. Search for the **Google Search Console API** in the [API Library](https://console.cloud.google.com/apis/library/searchconsole.googleapis.com) and click **Enable**.
   
7. Go to **Google Auth platform > Clients** and click **Create client**.
   
8. Configure the **OAuth consent screen** if prompted, then select **Web application** as the **Application type**.
   
9. Enter `https://www.workato.com/oauth/callback` in the **Authorized redirect URIs** field, then click **Create**.
   
10. Copy the **Client ID** and **Client secret** and store them securely.
    
11. Return to the Workato tab and enter the values in the **Client ID** and **Client secret** fields.
    
12. Click **Save**, then click **Done**. Refer to [Custom OAuth profiles](/en/custom-oauth-profiles) for more information.
    

### Connect to Google Search Console with OAuth 2.0

1. Select **Create > Connection** or press C twice.
   
2. Search for `Google Search Console` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Custom OAuth profile** drop-down menu to select the [custom OAuth profile](#create-a-google-cloud-oauth-app) you created for Google Search Console. This field is required.
   
6. Select **Sign in with Google** to open Google's sign-in window.
   
7. Enter your credentials in the Google sign-in window to authenticate your account.
   
8. Review the permissions that Workato requests, then approve them to complete the connection. Workato displays a success message when the connection is established.
   

## Configure the pipeline

Complete the following steps to configure Google Search Console as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from Google Search Console.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Google Search Console**.
   
7. Choose the Google Search Console connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Click **Add object** to open the **Add new objects** panel.
   
9. Search or browse the list of available Google Search Console objects, select the objects you plan to sync, and click **Add**.
   
   > **FIXED OBJECT LIST**
   > 
   > You can only select from the objects listed in [Supported objects](#supported-objects). You can't define your own combination of dimensions and metrics.
   
10. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
11. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields. Refer to [Sensitive data handling](#sensitive-data-handling) for a list of fields that commonly contain PII.
    
12. Click **Add object** again to add more objects. Repeat this step to include additional Google Search Console objects in your pipeline.
    
13. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
14. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Google Search Console to the destination.
    
    **Time-based schedule**
    
    1. Select the **Time unit**, such as **Minutes**, **Hours**, or **Days**.
       
    2. Specify the sync interval in the **Trigger every** field.
       
       The pipeline syncs every 6 hours if you select **Hours** as the **Time unit** and enter `6` in the **Trigger every** field. The minimum interval you can set is 15 minutes.
       
       Workato recommends a 24-hour interval for Google Search Console, because Search Console finalizes each day's data once per day. Refer to [Incremental sync](#incremental-sync) for more information.
       
    3. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts report data. The pipeline starts the historical sync `1` year before today if you leave this field blank. The pipeline uses the date `2` years before today instead if you enter a start date more than `2` years before today. Refer to [Historical sync is limited to two years](#historical-sync-is-limited-to-two-years) for more information.
       
       This field doesn't apply to `Sites`, `Sitemaps`, and `Sitemap Contents`, which sync in full on every run.
       
       You can't change this value after you run the pipeline.
       
    4. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe#configure-how-data-is-loaded-in-the-workato-data-pipeline).
       
    
    **Cron-based scheduling**
    
    1. Use the **Time unit** drop-down menu to select **Custom schedule**.
       
    2. Enter an expression in the **Cron expression** field using the format:
       
       ```text
       [minute] [hour] [day of month] [month] [day of week]
       ```
       
       The minimum interval for cron schedules is 15 minutes. Enter the following expression to sync every day at 8:00 AM UTC:
       
       ```text
       0 8 * * *
       ```
       
       Workato recommends a daily cron schedule for Google Search Console, because Search Console finalizes each day's data once per day. Refer to [Incremental sync](#incremental-sync) for more information.
       
    3. Optional. Select a **Timezone** for the cron expression. Leave blank to use `Etc/UTC`.
       
    4. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts report data. The pipeline starts the historical sync `1` year before today if you leave this field blank. The pipeline uses the date `2` years before today instead if you enter a start date more than `2` years before today. Refer to [Historical sync is limited to two years](#historical-sync-is-limited-to-two-years) for more information.
       
       This field doesn't apply to `Sites`, `Sitemaps`, and `Sitemap Contents`, which sync in full on every run.
       
       You can't change this value after you run the pipeline.
       
    5. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe#configure-how-data-is-loaded-in-the-workato-data-pipeline).
       
    

## Supported objects

Google Search Console data pipelines sync data from the Google Search Console API. The following tables list the supported objects, grouped by category. Each object syncs as a separate table in your destination:

### Search Analytics reports

The following reports return the `clicks`, `impressions`, `ctr`, and `position` metrics. Every report groups by `date`, `country`, and `device`. `Page Report` adds the `page` dimension, the keyword reports add the `query` dimension, and `Keyword Page Report` adds both. Reports with `by Page` in the name aggregate results by page, and reports with `by Site` in the name aggregate results by property. Workato syncs each report for every search type and every accessible property.

| Object | Sync mode | Delete tracking |
| --- | --- | --- |
| `Site Report by Page` | Incremental | No |
| `Site Report by Site` | Incremental | No |
| `Page Report` | Incremental | No |
| `Keyword Site Report by Page` | Incremental | No |
| `Keyword Site Report by Site` | Incremental | No |
| `Keyword Page Report` | Incremental | No |

`Keyword Page Report` has the highest cardinality of the reports, because it groups by both `page` and `query`. It returns the most rows and consumes the most Google API quota. Refer to [Search Analytics quotas](#search-analytics-quotas) for more information.

### Property and sitemap data

The following tables sync configuration data about your Search Console properties and the sitemaps submitted to them. `Sitemap Contents` contains one row for each content type listed in a sitemap. Refer to [Every accessible property syncs automatically](#every-accessible-property-syncs-automatically) for the properties each object includes.

| Object | Sync mode | Delete tracking |
| --- | --- | --- |
| `Sites` | Full sync | Yes (destination-inferred) |
| `Sitemaps` | Full sync | Yes (destination-inferred) |
| `Sitemap Contents` | Full sync | No |

## Sync modes

Google Search Console data pipelines support full sync and incremental sync. Refer to the [Supported objects](#supported-objects) tables to see the sync mode for each object.

### Full sync

A full sync re-reads the complete record set for an object on every run and replaces the destination table. `Sites`, `Sitemaps`, and `Sitemap Contents` use full sync, because the Google Search Console API returns these resources as complete lists and offers no way to request only changed records.

### Incremental sync

Search Analytics reports aren't row-level records with a modified-time field. Each report is a query over Google's reporting data, so incremental sync constrains the query's date range instead of filtering by a per-record cursor:

- **Finalized data only**: Workato syncs only finalized Search Console data, and every sync stops `3` days before today. Each date syncs after it ages past that cutoff.
- **Rollback window**: Every recurring incremental sync also re-pulls the `7` days before the previous sync's cutoff date, because Google can revise recent values. Re-pulled rows update the existing rows in your destination instead of creating duplicates, so metric values for recent dates can change between runs. This window doesn't apply to the first, historical sync.
- **Historical sync**: The first sync extracts every date from the start date you configure through the cutoff date. Refer to [Historical sync is limited to two years](#historical-sync-is-limited-to-two-years) for how the start date is applied.

### Delete tracking

Report objects don't support delete tracking. They're aggregated metrics, and the Search Console API doesn't expose a deletion signal for them.

`Sites` and `Sitemaps` sync in full on every run. The destination compares each run against the previous one and marks records that no longer appear as deleted, because these are full-sync objects. The Search Console API itself exposes no deletion signal for them. Workato detects deletions on the next full sync, not at the time of deletion.

`Sitemap Contents` also syncs in full but doesn't support delete tracking.

## Schema and data type handling

The following considerations apply to schema and data types when you sync data from Google Search Console:

### Schema

Every object has a fixed schema defined by Workato. The schema doesn't vary between accounts or properties.

### Data types

Workato maps the following report columns:

- `date` syncs as a date column.
- `clicks` and `impressions` sync as whole numbers.
- `ctr` and `position` sync as decimals.
- `country`, `device`, `page`, and `query` sync as strings and can be empty in a row.

### Synthetic columns

Workato adds the following synthetic columns to destination tables:

| Column | Type | Purpose |
| --- | --- | --- |
| `_workato_id` | String | Report objects only. A primary key generated from the property URL, search type, and every dimension value in the row, because Search Console report rows don't include a natural identifier. A re-pulled row generates the same key, so it updates the existing row. |
| `site` | String | The property URL that the row belongs to, such as `sc-domain:example.com` for a Domain property or `https://www.example.com/` for a URL-prefix property. Added to report objects, `Sitemaps`, and `Sitemap Contents`, because a single pipeline syncs every property your connection can access. |
| `search_type` | String | Report objects only. The search type the row belongs to: `web`, `image`, `video`, or `news`. |

## Sensitive data handling

Google Search Console reports are aggregated, and Workato delivers the values Google returns without masking or filtering any field.

| Object | Sensitive fields |
| --- | --- |
| `Keyword Site Report by Page`, `Keyword Site Report by Site`, `Keyword Page Report` | `query` |
| `Page Report`, `Keyword Page Report` | `page` |

Use the **Hash** option in field-level data protection during pipeline configuration to protect PII before it reaches your destination. Refer to the [Configure the pipeline](#configure-the-pipeline) steps for more information.

## Limitations

The following limitations apply when you use Google Search Console as a data pipeline source:

### Every accessible property syncs automatically

Workato discovers and syncs every Search Console property that the connection's Google account can access. You can't limit a pipeline to specific properties in Workato. Remove the account's access to a property in Search Console to exclude it from syncing.

The permission level on each property determines what syncs:

- **Owner and full user**: All objects sync.
- **Restricted user**: Search Analytics reports and `Sites` sync. `Sitemaps` and `Sitemap Contents` don't include the property.
- **Unverified user**: The property is skipped, because this level has no data access.

### Historical sync is limited to two years

The historical sync starts `1` year before today if you leave the start date blank. A start date more than `2` years before today is replaced with the date `2` years before today. Dates outside the range that Search Console retains return no rows, without an error.

### Daily row ceiling

The Search Console API returns at most `50,000` rows per day, per search type, per property, sorted by clicks. The API drops the remaining rows without an error or other signal when a single day exceeds this limit, and Workato can't recover them. Google can also withhold additional rows when a report groups by `page` or `query`. Google doesn't offer a quota increase for this limit.

### Search Analytics quotas

Google limits Search Analytics queries to `1,200` queries per minute for each property and each Google user. Google also applies a load-based quota that wide date ranges and reports grouped by both `page` and `query` consume faster than other query types. Workato waits and retries on quota errors. Set a more recent start date to reduce quota use.

### Unsupported Search Console data

Google Search Console data pipelines don't sync the following data:

- URL Inspection data
- The `searchAppearance` dimension
- Hourly report data
- The `discover` and `googleNews` search types
- Custom combinations of dimensions and metrics

### Minimum sync frequency

The minimum supported sync interval is 15 minutes.
