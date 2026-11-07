---
url: 'https://docs.workato.com/en/connectors/bigquery.md'
description: >-
  The Google BigQuery connector allows you to automate actions on datasets in
  your Google BigQuery instance, such as inserting rows or performing queries on
  existing datasets.
---

# Google BigQuery

[Google BigQuery](https://cloud.google.com/bigquery/) is a serverless, highly scalable, and cost-effective cloud data warehouse with an in-memory BI Engine and machine learning built-in.

The Google BigQuery connector allows you to automate actions on datasets in your Google BigQuery instance, such as inserting rows or performing queries on existing datasets. You can also trigger recipes from new rows in dataset events.

> **FEATURE AVAILABILITY**
> 
> The Google BigQuery connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google BigQuery connector uses the [Google BigQuery API v2](https://cloud.google.com/bigquery/docs/reference/rest).

## How to connect to Google BigQuery

The Google BigQuery connector supports the following authentication methods:

- OAuth 2.0
- Service Account

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

![Configuring Google BigQuery connection](/assets/connection.CJrEIfny.png)

Complete the following steps to establish a connection to Google BigQuery in Workato:

1. Search for `Google BigQuery` and select it as your app.
   
2. Enter a unique name for your connection in the **Connection name** field that identifies which Google BigQuery instance it is connected to.
   
3. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
4. Use the **Authentication type** drop-down menu to select `OAuth 2.0` or `Service account`.
   
5. Complete the following steps if your **Authentication type** is `Service account`:
   
   1. Enter the email address of your service account in the **GCP Project service account email** field.
      
   2. Enter the private key of your service account in the **Private key** field.
      
   3. Expand the **Advanced settings** section and select scopes to request your connection.
      
6. Click **Sign in with Google**.
   
7. Click **Allow** when prompted to authorize Workato to access your Google account.
   

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

#### Set up a Google service account

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
   
   ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use.
   
   ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later.
   
   ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

Enable the Google BigQuery API, then return to Workato to finish setting up your connection.

#### Service account permissions

To use all triggers and actions in the Google BigQuery connector, you must give your service account the **BigQuery Admin** IAM role or a custom role with the following permissions:

- bigquery.datasets.get
- bigquery.jobs.create
- bigquery.jobs.get
- bigquery.jobs.list
- bigquery.jobs.listAll
- bigquery.tables.create
- bigquery.tables.get
- bigquery.tables.getData
- bigquery.tables.list
- bigquery.tables.update
- bigquery.tables.updateData

> **TIP**
> 
> If you would like to only **insert** data with this connection on Workato, you may:  
> 
> - Use the `BigQuery Data Editor` role.  
>   
> - Add the bigquery.jobs.create permission.  
>   
> 
> If you would like to only **select** data with this connection on Workato, you may:
> 
> - Use the `BigQuery Data Viewer` role.  
>   
> - Add the bigquery.jobs.create permission.  
>   

![Google BigQuery custom role with 11 assigned permissions](/assets/service-custom-permissions.C-q8i4or.png)

Refer to Google's documentation on [creating custom roles](https://cloud.google.com/iam/docs/creating-custom-roles) and [Google BigQuery permissions](https://cloud.google.com/bigquery/docs/access-control#bq-permissions) for more information.

> **SERVICE ACCOUNTS AND CUSTOM ROLES**
> 
> If you're using a custom role for your service account, the project ID must be supplied directly in Workato. Otherwise, the **Select project** drop-down menu in **Setup** won't load, and you'll need to provide the project ID manually.

## Rate limits on Google BigQuery

[Google BigQuery's rate limits](https://cloud.google.com/bigquery/quotas#standard_tables) on tables indicate that `bulk` insert operations on tables can only be performed 1000 times a day. Use the `Insert row` and `Insert rows` actions to bypass these quotas.

## Using the Google BigQuery connector

After establishing a connection with the Google BigQuery connector, most actions require additional parameter inputs.

| Field | Description |
| --- | --- |
| Project | The project to bill for the query. |
| Dataset | The dataset from which the action or trigger pulls possible tables. |
| Table | The table inside the dataset. |
| Location | The geographical location where the job should be run. |

### Single row versus batch of rows

The Google BigQuery connector can read or write to your database either as a single row or in batches. When using batch read actions or triggers, you must provide the a batch size. The batch size can be any number between 1 and 50000, with a maximum batch size of 50000.

![Batch trigger inputs](/assets/batch_trigger_input.Cr5kd4QL.png)_Batch trigger inputs_

The output of single and batch triggers and actions also differ. For example, a single trigger that processes rows one at a time returns an output datatree that allows you to map data from that single row.

![Single row output](/assets/single_row_trigger_output.CVQN9MCC.png)_Single row output_

A batch trigger that processes rows in batches returns this data as an array of rows. The Rows datapill indicates that the output is a list containing data for each row in that batch.

![Batch trigger output](/assets/batch_trigger_output.DfmG1IK4.png)_Batch trigger output_

You must handle the output of batch triggers or actions differently. In cases where downstream batch actions accept **Rows source list** input fields, you can map the Rows datapill to process the entire array.

### WHERE condition

The **WHERE condition** input field allows you to filter and identify rows to act on. You can configure this field to:

- Filter rows to be picked up in triggers
- Filter rows in the **Select rows** action
- Filter rows to be deleted in the **Delete rows** action

Each request will use this clause as a `WHERE` statement. This should follow basic SQL syntax. Refer to the [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) for a full list of rules for writing SQL statements compatible with Google BigQuery.

#### Simple statements

Knowing the column's data types in Google BigQuery is important to build working queries. When comparing string values, you must enclose values in single quotes (`''`), and the columns used must exist in the table. When comparing integer values, the supplied value should not be enclosed in single quotes.

A simple `WHERE` condition to filter rows based on values in a single column looks like this:

```sql
string_column = 'USD' and integer_column = 1111
```

If used in a **Select rows** action, this `WHERE` condition will return all rows that have the value 'USD' in the `currency` column. Just remember to wrap datapills with single quotes in your inputs.

![Using datapills in WHERE condition](/assets/use_datapill_in_where.cxd4cfU6.png)_Using datapills in `WHERE` condition_

#### Complex statements

Your `WHERE` condition can also contain subqueries. The following query can be used on the `users` table.

```sql
id in (select distinct(user_id) from zendesk.tickets where priority = 2)
```

When used in a **Delete rows** action, this query deletes all rows in the `users` table where at least one associated row in the `tickets` table has a value of `2` in the `priority` column.

### Defining your output fields

Some Google BigQuery actions and triggers allow you to define the expected output columns of a query. This input field is available in the following triggers and actions:

- Scheduled query trigger
- Get query job output
- Select rows using custom SQL

Define your output fields in the output schema designer using our CSV uploader. In these cases, run a sample query in the Google BigQuery console and export a CSV.

Upload this CSV into the schema wizard, and Workato automatically generates all fields.

---
