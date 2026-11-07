---
url: 'https://docs.workato.com/en/connectors/files-dot-com/get-record-action.md'
description: The Get record action retrieves a file or folder in Files.com.
---

# Files.com - Get record action

The **Get record** action retrieves a file or folder in Files.com.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to get the record of. |
| Path | Enter the path to the file or folder to retrieve. For example: `folder/file.txt`. |
| Preview size | Select the preview size for the record. Options include `Small`, `Large`, `Extra large`, and `PDF`. The default is `Small`. |
| With previews | Select whether to include file preview information in the response. |
| With priority color | Select whether to include file priority color information in the response. |

## Output

The following are the most common output fields. Refer to the [Files.com](https://developers.files.com/) documentation for a complete list of output fields.

| Output field | Description |
| --- | --- |
| Path | The path where the retrieved record is located. |
| Created by ID | The ID of the user that created the record. |
| Display name | The name of the retrieved record that is displayed. |
| Type | The type of retrieved record. |
| Size | The size of the retrieved record. |
| Created at | The time that the record was retrieved. |

---
