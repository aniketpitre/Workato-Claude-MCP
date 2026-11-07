---
url: 'https://docs.workato.com/en/features/filestorage/filestorage-connector.md'
description: >-
  Store, manage, and process files within Workato recipes using the FileStorage
  connector, with triggers and actions for files and directories.
---

# Workato FileStorage connector

The FileStorage connector enables you to store, manage, and process files directly within Workato recipes.

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Triggers

The **Workato FileStorage** connector allows you to work with files stored using the following recipe triggers:

- [New CSV file (batch)](/en/features/filestorage/new-csv-file-trigger)
- [New lines in CSV file (batch)](/en/features/filestorage/new-csv-lines-in-file-trigger)
- [New file](/en/features/filestorage/new-file-trigger)

## Actions

The **Workato FileStorage** connector allows you to work with the file storage entity using the following recipe actions:

- [Append to file](/en/features/filestorage/append-to-file-action)
- [Create directory](/en/features/filestorage/create-directory-action)
- [Create file](/en/features/filestorage/create-file-action)
- [Delete directory](/en/features/filestorage/delete-directory-action)
- [Delete file](/en/features/filestorage/delete-file-action)
- [Generate shareable file link](/en/features/filestorage/generate-shareable-link-action)
- [Get file contents](/en/features/filestorage/get-file-contents-action)
- [Rename/move file](/en/features/filestorage/rename-move-file-action)
- [Search files](/en/features/filestorage/search-files-action)

## Working with CSV files

If you choose to [create a file](/en/features/filestorage/create-file-action) or [append to a file](/en/features/filestorage/append-to-file-action) and the data needs to be formatted as a CSV file, then it must have the column data types (schema) defined. The schema can be automatically inferred or you can set it explicitly. If the column schema is defined explicitly, then Workato parses the entirety of the incoming CSV data to determine if the provided column schema matches exactly with the data present in the CSV file.

If there are mismatches, Workato either relaxes the column schema to accommodate the new data in the same column, or returns an error, depending on how the action is configured.

This means that the newly created file and any content appended to it conforms to the stored column schema, ensuring that the file is stored in a schema-safe way.

By ensuring schema-safe CSV files, Workato enables you to maintain workflows such as the following:

1. Store a CSV file in FileStorage as a schema-safe source of truth.
2. Aggregate a stream of CSV data to an existing large CSV file while ensuring column schema conformance.
3. Use triggers to batch out the file's data into smaller chunks that can be consumed by applications downstream.

Example use cases include the following:

- Fetch and download a CSV file from a partner SFTP server and store it in FileStorage with the data contents and the explicitly set column schema. In a separate recipe, using the [New CSV file](/en/features/filestorage/new-csv-file-trigger) trigger, the data is batched out and loaded into a database table. Because the CSV file conforms to the provided column schema, Workato prevents any data type mismatch errors while loading the data into the columns in the database table.
- Every day, process new leads from Hubspot and append them to a CSV file with a defined column schema. Using the [New lines in CSV file](/en/features/filestorage/new-csv-lines-in-file-trigger) trigger, this newly appended lead data is fetched and loaded in batches to Salesforce CRM lead objects safely, without any data type mismatch errors.

### Set schema

When you explicitly set the schema for incoming CSV columns, you instruct FileStorage to parse the entire file and ensure the data types match the schema you define. If they don't match the schema, FileStorage raises an error at run time. This prevents errors later, such as when data is replicated to a data warehouse through ELT/ETL.

### Auto-infer schema

Optionally, Workato can auto-infer the data types of incoming CSV columns. When you select **Auto infer** in the [Create file](/en/features/filestorage/create-file-action) or [Append to file](/en/features/filestorage/append-to-file-action) actions, Workato automatically selects and stores the appropriate schema for the data. For example, if a column contains only integers, Workato assigns that column the integer data type.

#### Schema relaxation

If you configure Workato to auto-infer the schema for created or appended data, and Workato encounters a data type mismatch in a column, Workato "relaxes" the schema. This means that Workato adjusts the data type for the column to accommodate the changes. For example, if Workato assigns a column the integer data type but encounters a string in the column during an append job, Workato adjusts the column's data type to string to prevent errors at load time.

However, if you explicitly set the schema for created or appended data, and Workato encounters a data type mismatch in a column, Workato raises an error and the job fails.

---
