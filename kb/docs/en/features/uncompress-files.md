---
url: 'https://docs.workato.com/en/features/uncompress-files.md'
description: >-
  Use the Uncompress a file action from File tools by Workato to extract .zip,
  .tar.gz, and .gz files from any connected app.
---

# File tools by Workato - Uncompress a file action

The **Uncompress a file** action extracts files with .zip, .tar.gz, or .gz extensions. You can use source files from any app, such as [Amazon S3](/en/connectors/s3), [Dropbox](/en/connectors/dropbox), and [Salesforce](/en/connectors/salesforce).

![Uncompress file](/assets/uncompress-file-action.dDS3ORWW.png)_Uncompress a file action_

## Input

| Field | Description |
| --- | --- |
| Compression format | Specify the file's compression format. Choose **Zip** for .zip files or **Gzip** for .gzip and .tar.gz files. The default is **Zip**. |
| Password | Provide the password if the archive is encrypted. This input field is only displayed if **Zip** is selected. |
| Archive format | Specify the file's archive format. Choose **None** for .gzip files or **Tar** for .tar.gz files. This input field is only displayed if **Gzip** is selected. |
| File contents | Specify the source file to extract. |
| File name encoding | Specify the encoding of the file names in the archive. Defaults to **Auto** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| File list | The list of files that were extracted. |
| File name (file list) | The name of the file. |
| File contents (file list) | The content of the file. |
| File size (file list) | The size of the file in bytes. |
| File directory (file list) | The directory path of each extracted file. Files originally located in the root folder are represented by `.` |

## Example: Uncompress a zip file

This recipe unzips a zip file and extracts the file contents.

![Uncompress file from S3](/assets/uncompress-file-recipe.BXrqHP0M.png)_Uncompress file from S3_

Complete the following steps to create this recipe:

1. Create a recipe using the Amazon S3 [New file](/en/connectors/s3/trigger-new-file) trigger.
   
2. Set a trigger condition that instructs the recipe to only process the new Amazon S3 file if it's a zip file.
   
3. Download the zip file using the Amazon S3 [Download file](/en/connectors/s3/action-download-file) action.
   
4. Map the Amazon S3 File content (Step 2) datapill to the **File contents** input field in the **Uncompress a file** action. ![Uncompress file input config](/assets/uncompress-file-recipe-input-config.Dm_4xUdi.png)
   
5. Add a **Repeat for each** step that processes every uncompressed file using the File list (Step 3) datapill from the **Uncompress a file** action.
   
6. Add an **IF condition** to only process extracted files ending in `.csv`.
   
7. Use the [Parse CSV](/en/features/handling-csv-files#csv-by-workato) action to parse the file contents if the IF condition is true.
   
8. Use the NetSuite [Upsert records in bulk](/en/connectors/netsuite/netsuite-upsert-batch-action) to bulk upsert the CSV file records into NetSuite.
   

The steps in the **Repeat for each** loop are repeated until all CSV files extracted from the zip file are processed.

---
