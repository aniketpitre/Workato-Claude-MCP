---
url: 'https://docs.workato.com/en/connectors/files-dot-com/create-record-action.md'
description: >-
  The Create record action creates a new record, including files and folders, in
  Files.com.
---

# Files.com - Create record action

The **Create record** action creates a new record, including files and folders, in Files.com.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the Files.com object you plan to create a new record of. |
| Path | Enter the path where you plan to create a record. For example: `folder/file.txt`. |
| Create parent directories | Select `Yes` or `No` to indicate if you plan to create parent directories if they do not exist. |
| Provided modified time | Enter a custom creation timestamp for the record. |

## Output

The following are the most common output fields. Refer to the [Files.com](https://developers.files.com/) documentation for a complete list of output fields.

| Output field | Description |
| --- | --- |
| Path | The path where the newly created record is located. |
| Created by ID | The ID of the user that created the new record. |
| Display name | The name of the new record that is displayed. |
| Type | The type of new record. |
| Size | The size of the new record. |
| Created at | The time that the new record was created. |

---
