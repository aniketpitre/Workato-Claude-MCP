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
