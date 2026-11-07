---
url: 'https://docs.workato.com/en/connectors/gcp-biglake-iceberg.md'
description: >-
  The GCP BigLake Iceberg connector integrates with Apache Iceberg tables
  managed by the BigLake Metastore on Google Cloud.
---

# GCP BigLake Iceberg

The GCP BigLake Iceberg connector integrates with Apache Iceberg tables managed by the BigLake Metastore on Google Cloud. It manages tables directly through the [BigLake API](https://cloud.google.com/bigquery/docs/reference/biglake/rest) and loads or queries data through the BigQuery Jobs API, automatically handling long-running jobs with built-in polling.

## Install GCP BigLake Iceberg from the community library

Complete the following steps to install the GCP BigLake Iceberg connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The GCP BigLake Iceberg connector uses custom authentication with a Google Cloud service account and a JWT bearer token.

### Minimum and default scopes

Grant your Google Cloud service account the following minimum permissions:

- `biglake.tables.create`
- `biglake.tables.get`
- `biglake.tables.list`
- `bigquery.jobs.create`
- storage read/write access on your warehouse bucket.

Refer to the Google Cloud [Service accounts](https://cloud.google.com/iam/docs/service-accounts) documentation for more information about service accounts.

### GCP BigLake Iceberg set up

Complete the following steps to create a Google Cloud service account to establish a connection to GCP BigLake Iceberg in Workato:

1. Create a service account in your Google Cloud project and download its JSON key file. Refer to the Google Cloud [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete) documentation for detailed steps.
   
2. Grant the service account the permissions listed in [Minimum and default scopes](#scopes).
   
3. Enable the BigLake API (`biglake.googleapis.com`) and the BigQuery API (`bigquery.googleapis.com`) in your project. Refer to the Google Cloud [Enable and disable APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) documentation for complete steps.
   

### Connect to GCP BigLake Iceberg using custom authentication

Complete the following steps to connect to GCP BigLake Iceberg in Workato:

1. Click **Create > Connection**.
   
2. Search for and select GCP BigLake Iceberg as your connection.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Provide the email of the service account you created in the **Service account email** field, for example `name@project.iam.gserviceaccount.com`.
   
6. Copy and paste the private key from the downloaded service account JSON key file, including the `BEGIN`/`END` lines, into the **Private key** field.
   
7. Provide the default Google Cloud project ID billed for requests in the **Project ID** field, for example `my-gcp-project`.
   
8. Optionally, provide the default region for BigLake catalogs and BigQuery jobs in the **Default location** field, for example `us-central1` or `US`. You can override this value per action.
   
9. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/create-table-action.md
description: >-
  The Create table action registers a new table in a GCP BigLake Iceberg
  database.
---

# GCP BigLake Iceberg - Create table action

The **Create table** action registers a new table in a GCP BigLake Iceberg database. Point the metadata location at the table metadata JSON in Cloud Storage for GCP BigLake Iceberg tables.

## Input

| Input field | Description |
| --- | --- |
| Project ID | Enter the ID of the project you plan to create the table in. Defaults to the connection project ID. |
| Location | Enter the region of the catalog, such as `us-central1`. Defaults to the connection location. |
| Catalog ID | Enter the catalog that contains the database. |
| Database ID | Enter the database that contains the table. |
| Table ID | Enter the ID for the new table. |
| Storage location URI | Enter the Cloud Storage location of the table data, such as `gs://bucket/warehouse/db/table`. |
| Iceberg metadata location | Enter the Cloud Storage path to the Iceberg metadata JSON, such as `gs://bucket/warehouse/db/table/metadata/v1.metadata.json`. Optional. |

## Output

| Output field | Description |
| --- | --- |
| Table name | The full resource name of the table. |
| Type | The table type, such as `HIVE`. |
| ETag | The checksum used for concurrency control. |
| Create time | The timestamp when the table was created. |
| Update time | The timestamp when the table was last updated. |
| Delete time | The timestamp when the table was soft-deleted, if applicable. |
| Expire time | The timestamp when the table is permanently deleted, if applicable. |
| Hive options | An object containing the table type, storage descriptor, including the location URI, input/output format, and serialization library, and parameters such as table type and Iceberg metadata location. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/get-table-definitions-action.md
description: >-
  The Get table definitions action retrieves the definition of a table
  registered in GCP BigLake Iceberg.
---

# GCP BigLake Iceberg - Get table definitions action

The **Get table definitions** action retrieves the definition of a table registered in GCP BigLake Iceberg.

## Input

| Input field | Description |
| --- | --- |
| Catalog ID | Enter the BigLake Metastore catalog that contains the database. |
| Database ID | Enter the database that contains the table. |
| Table ID | Enter the table you plan to retrieve. |
| Project ID | Enter the project you plan to retrieve tables from. Defaults to the connection project ID. |
| Location | Enter the region of the catalog. Defaults to the connection location. |

## Output

| Output field | Description |
| --- | --- |
| Table name | The full resource name of the table. |
| Type | The table type, such as `HIVE`. |
| ETag | The checksum used for concurrency control. |
| Create time | The timestamp when the table was created. |
| Update time | The timestamp when the table was last updated. |
| Delete time | The timestamp when the table was soft-deleted, if applicable. |
| Expire time | The timestamp when the table is permanently deleted, if applicable. |
| Hive options | An object containing the table type, storage descriptor, including location URI, input/output format, and serialization library, and parameters such as table type and Iceberg metadata location. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/list-tables-action.md
description: >-
  The List tables action lists all tables in the specified GCP BigLake Iceberg
  database.
---

# GCP BigLake Iceberg - List tables action

The **List tables** action lists all tables in the specified GCP BigLake Iceberg database.

## Input

| Input field | Description |
| --- | --- |
| Catalog ID | Enter the ID of the BigLake Metastore catalog that contains the database. |
| Database ID | Enter the database whose tables you plan to list. |
| Project ID | Enter the ID of the project that contains the database. Defaults to the connection project ID. |
| Location | Enter the region of the catalog. Defaults to the connection location. |
| View | Select the level of detail to return, such as `BASIC` or `FULL`. Defaults to `BASIC`. |
| Page size | Enter the maximum number of tables to return (1-1000). |
| Page token | Enter the token from a previous response to fetch the next page. |

## Output

| Output field | Description |
| --- | --- |
| Tables | A list of tables. Each table includes its name, type, ETag, timestamps, and Hive options such as the storage descriptor and parameters. |
| Next page token | Token to fetch the next page of results, if more tables are available. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/import-data-action.md
description: >-
  The Import data action loads data from Cloud Storage files into a GCP BigLake
  Iceberg table using a BigQuery LOAD DATA job.
---

# GCP BigLake Iceberg - Import data action

The **Import data** action loads data from Cloud Storage files into a GCP BigLake Iceberg table using a BigQuery LOAD DATA job. This is a long-running action that polls until the job completes.

## Input

| Input field | Description |
| --- | --- |
| Dataset ID | Enter the BigQuery dataset containing the destination table. |
| Table ID | Enter the ID of the destination Iceberg table. |
| Source URIs | Enter Cloud Storage URIs of the source files, such as `gs://bucket/data/*.csv`. |
| Source format | Select the format of the source files, such as `CSV`, `PARQUET`, or `AVRO`. |
| Project ID | Enter the ID of the destination project. Defaults to the connection project ID. |
| Location | Enter the BigQuery job location. Defaults to the connection location. |
| Field delimiter | Enter the delimiter between columns in CSV files, such as `,` or `;`. Defaults to `,`. |
| Skip leading rows | Enter the number of CSV header rows to skip. |

## Output

| Output field | Description |
| --- | --- |
| Kind | The resource type, such as `bigquery#job`. |
| ETag | The checksum used for concurrency control. |
| Job ID | The fully qualified ID of the BigQuery job. |
| Self link | The URL used to access the job resource. |
| User email | The email of the user who ran the job. |
| Principal subject | The authenticated principal that submitted the job. |
| Job reference | An object containing the project ID, job ID, and location of the job. |
| Status | An object containing the job state and, if the job failed, the error result. |
| Statistics | An object containing job timing and processing statistics, such as creation time, start and end time, bytes processed, and slot usage. |
| Configuration | An object describing the job type and the load configuration used to run the job. |
| Job creation reason | An object containing the code that explains why the job was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gcp-biglake-iceberg/query-data-action.md
description: >-
  The Query data action runs a SQL query against GCP BigLake Iceberg tables
  using a BigQuery query job.
---

# GCP BigLake Iceberg - Query data action

The **Query data** action runs a SQL query against GCP BigLake Iceberg tables using a BigQuery query job. This is a long-running action that polls until the job completes and returns rows.

## Input

| Input field | Description |
| --- | --- |
| SQL query | Enter the GoogleSQL query you plan to use. |
| Project ID | Enter the ID of the project you plan to query. Defaults to the connection project ID. |
| Location | Enter the job location. Defaults to the connection location. |
| Max results | Enter the maximum number of rows to return. |

## Output

| Output field | Description |
| --- | --- |
| Kind | The resource type, such as `bigquery#getQueryResultsResponse`. |
| ETag | The checksum used for concurrency control. |
| Schema | An object listing the field names, types, modes, and descriptions for the returned rows. |
| Rows | An array of result rows. Each row contains a list of cell values in the same order as the schema fields. |
| Total rows | The total number of rows in the query result. |
| Job complete | Whether the query job has completed. |
| Cache hit | Whether the query results were fetched from the query cache. |
| Total bytes processed | The total number of bytes processed for the query. |
| Job reference | An object containing the project ID, job ID, and location of the job. |

---
