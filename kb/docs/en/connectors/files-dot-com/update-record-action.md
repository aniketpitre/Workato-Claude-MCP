---
url: 'https://docs.workato.com/en/connectors/files-dot-com/update-record-action.md'
description: The Update record action updates a record in Files.com.
---

# Files.com - Update record action

The **Update record** action updates a record in an Files.com.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to update, such as `File/Folder`. |
| Path | Enter the path to the folder to update. For example: `folder/file.txt` |
| Custom metadata | Enter custom metadata key-value pairs for the object. This field is limited to 32 keys, 256 characters in each key, and 1024 characters for each value. |
| Provided modified time | Select the time that the record was modified. |
| Priority color | Enter the priority color to update the record with. |

## Output

This action has additional output fields, however these are the most common fields. Refer to the [Files.com](https://developers.files.com/) documentation for a complete list of output fields.

| Output field | Description |
| --- | --- |
| Path | The path where the updated record is located. For example: `folder/file.txt`. |
| Created by ID | The ID of the user that created the record. |
| Display name | The name of the updated record that is displayed. |
| Type | The type of updated record. |
| Size | The size of the updated record. |
| Created at | The time that the record was created. |

---
