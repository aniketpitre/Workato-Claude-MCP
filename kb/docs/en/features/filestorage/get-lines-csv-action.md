---
url: 'https://docs.workato.com/en/features/filestorage/get-lines-csv-action.md'
description: >-
  Use the Get lines from CSV file batch action to retrieve up to 50,000 CSV
  lines from a file in Workato FileStorage.
---

# Workato FileStorage - Get lines from CSV file action (batch)

The **Get lines from CSV file** batch action allows you to retrieve a batch of lines from a CSV file in [Workato FileStorage](/en/features/workato-filestorage). This action returns 1,000 CSV lines by default and can fetch up to 50,000 records. Only files stored with a CSV column schema can be fetched.

![Get lines from CSV file in FileStorage action](/assets/filestorage-csv-lines.CWaWczT3.png) _Get lines from CSV file in FileStorage action_

## Input

| Input fields | Description |
| --- | --- |
| File path | Enter the full path of the CSV file. For example: `samplepath/path1/file1.csv`. The file must already exist, and only files with a CSV column schema can be fetched. |
| Batch size | Specify the number of lines to retrieve in a single fetch. This field defaults to 1,000 and can be increased to a maximum of 50,000 records. The number of records are auto-adjusted depending on size. |
| Batch offset | Specify the offset from which to start fetching records. The default offset is 0. Adjust the offset incrementally to fetch all records in manageable batches. |

## Output

| Output fields | Description |
| --- | --- |
| File name | The name of the CSV file. |
| File path | The complete path of the CSV file. |
| Batch size | The number of lines retrieved per fetch. |
| Batch offset | The offset value from which the batch starts. |

## Schema validation

This action validates the CSV data against the column schema set when you create or append the file, either through **Auto infer** or **Set schema**. It doesn't relax the schema when it reads the file. The action returns an error if the data includes values that don't match the schema.

To avoid validation errors, define the schema to cover all possible data types in each column. Set the column type to string when a column may contain mixed data types, such as numbers and special characters.

---
