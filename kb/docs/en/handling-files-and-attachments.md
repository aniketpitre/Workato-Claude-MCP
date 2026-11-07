---
url: 'https://docs.workato.com/en/handling-files-and-attachments.md'
description: >-
  Learn how Workato moves and parses files and attachments across FTP, file
  systems, APIs, and S3, handling both text and binary file formats.
---

# Handling files and attachments

Files and attachments are a key aspect of many integrations. Your recipes might involve data formats that are not found in the [standard datapill list](/en/recipes/data-pills-and-mapping#data-types). Workato enables you to move file and attachments of different formats across different access/transport mechanisms, such as FTP, file system, APIs, or S3.

For instance, you may need to upload a CSV file to Redshift or move attachments from Salesforce to Zendesk.

## Text files

Text files refers to files which can be opened with any text editor and is generally human-readable. Workato can act as the intermediary to move files from one app to another, as well as extract data from text files and parse it for use in Workato.

For instance, a recipe can retrieve CSV file content, parse, and make it available within the recipe. The data can further be used in transformations and loaded unto the target system.

Some examples of text files commonly worked with:

- Tabular data: [CSV](/en/features/handling-csv-files)
- Documents: txt, rtf
- Web standards: html, [JSON](/en/features/handling-json), [XML](/en/features/handling-xml), [SOAP](/en/features/handling-soap), [YAML](/en/features/handling-yaml)

## Binary files

Binary files refer to any file which is not human readable. Unlike text files where Workato parses the content to understand the structure of the data, Workato moves binary data without interpreting its content. For example, Workato cannot read and interpret an image file, but it can upload the entire file into Salesforce as an attachment.

Some examples of binary files commonly used:

- Images: jpg, png, gif, bmp, psd
- Documents: pdf, doc, docx, ppt, xls, odt

Refer to [Handling binary files](/en/features/handling-binary-files) for guidelines on working with binary files.

---
