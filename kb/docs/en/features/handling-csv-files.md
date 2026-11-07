---
url: 'https://docs.workato.com/en/features/handling-csv-files.md'
description: >-
  Learn how to process CSV files in Workato recipes using CSV tools by Workato
  or connector-specific triggers and actions to parse tabular data.
---

# Handle CSVs

A comma-separated values (CSV) file is a text file that stores tabular data in plain text. It is human-readable and widely supported across systems.

Many applications import or export data in CSV format. Workato recipes can process CSV data using built-in actions or connector-specific features. Use [CSV tools by Workato](#csv-by-workato) to parse raw CSV content into structured datapills or to generate CSV-formatted strings from arrays. Some connectors, such as Box or SFTP, also parse CSV content through their triggers or actions.

## CSV tools by Workato

[CSV tools by Workato](/en/connectors/csv-by-workato) allows you to parse raw CSV content into structured datapills or generate CSV-formatted strings from arrays. These built-in actions work with any file source, such as Box, Google Drive, or Dropbox, and don't depend on connector-specific parsing capabilities.

## Use cases

Automate CSV data processing to streamline file transfers, data synchronization, and reporting across your business applications. You can export employee records, update databases, or move data between cloud platforms with automated workflows to ensure accuracy and efficiency. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can optimize CSV processing:

- [Export Workday workers to CSV](/en/getting-started/use-cases/workday-python-google-drive) with Python and upload the file to Google Drive.
- [Update Quickbase records](/en/getting-started/use-cases/sftp-csv-by-workato-quickbase) from SFTP CSV files.
- [Load Box CSV data](/en/getting-started/use-cases/box-google-cloud-storage-bigquery) to Google BigQuery with Google Cloud Storage.
- [Upload a CSV file](/en/getting-started/use-cases/active-directory-csv-sftp) with Active Directory entries to an SFTP server.

## Parse CSV files with an external parser

Some connectors provide built-in support to parse CSV content. For example, the [Box connector](/en/connectors/box) can detect and parse CSV content through file triggers.

### Example usage

This recipe uses the Box [New CSV file in folder](/en/connectors/box/trigger-new-csv) trigger to detect a new CSV file in Box. The trigger reads the file, parses its contents, and generates an array of rows based on the defined **Field names**. These fields, such as `Manufacturer`, `Item Code`, and `Taxable`, appear as datapills in the recipe.

The recipe uses a [Repeat step](/en/recipes/repeat-for-each) to loop through each row and create inventory items in NetSuite.

![Recipe that processes a CSV file from Box and creates inventory items in NetSuite](/assets/define-expected-csv-columns.COLCFGdZ.png)_Recipe that processes a CSV file from Box and creates inventory items in NetSuite. View the [example recipe](https://www.workato.com/recipes/485023)._

The Box trigger processes all new files in the folder as CSVs. If the folder contains files with different headers, use filters or folder naming conventions to avoid recipe errors.

---
