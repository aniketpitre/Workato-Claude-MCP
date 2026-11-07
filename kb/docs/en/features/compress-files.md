---
url: 'https://docs.workato.com/en/features/compress-files.md'
description: >-
  Use the Compress files action in File tools by Workato to combine multiple
  files from any app into a single zip or gzip archive.
---

# File tools by Workato - Compress files action

The **Compress files** action allows you to compress multiple files into one zip or gzip file. You can use source files from any app, such as [Amazon S3](/en/connectors/s3), [Dropbox](/en/connectors/dropbox), and [Salesforce](/en/connectors/salesforce).

> **COMPATIBILITY**
> 
> Ensure all files have unique names, as this action doesn't support duplicates.

![Compress files](/assets/compress-files-action.B4u0C55z.png)

## Input

| Field | Description |
| --- | --- |
| Compression format | Specify the file's compression format. Options include **Zip** and **Gzip**. The default is **Zip**. |
| Archive format | Specify the file's archive format. Options include **None** and **Tar**. This input field is only displayed if you select **Gzip** as the compression format. |
| Password | Set a password if encryption is required. This input field is only displayed if you select **Zip** as the compression format. |
| Unicode encoding for filenames | Select **Yes** if you plan to compress files with non-English filenames that must be opened on Windows OS. The default is **No**. |
| File list | Add files to compress to this list. |
| File name | Enter the filename including the extension. For example, `jan_report.csv`. |
| File contents | Map a datapill containing the file contents to compress. |

## Output

| Field | Description |
| --- | --- |
| Compressed file contents | Contains the compressed file contents in the specified format. |

## Example: Compress all files in a folder

This recipe downloads files from Amazon S3 and Dropbox, compresses the downloaded files into a single zip file, and then sends the zip file as an email attachment.

![Compress files in SFTP directory](/assets/compress-files-static-list-recipe.B7Urc9ip.png)

---
