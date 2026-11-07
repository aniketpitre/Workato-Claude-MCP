---
url: 'https://docs.workato.com/en/connectors/files-dot-com/search-records-action.md'
description: The Search records action searches for a record in Files.com.
---

# Files.com - Search records action

The **Search records** action searches for a record in Files.com.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to search for records of, such as `File/Folder`. |
| Path | Enter the path to the folder to search for records. |
| Search | Enter a name to search folders or files by. Results include the closest matches and aren't real-time. Results are truncated at 1,000 matches. |
| Search custom metadata key | Enter a custom metadata key to search for. Enter `*` to return results for any metadata key. |
| Search all | Select `Yes` to search the entire site. Select `No` to only search a section on the site. |
| Type | Select the type of object to return. For example, `File` and `Folder`. |
| Modified at datetime | Select a date to only return records modified after this time. You can only use this input field with the **Type** input field. |
| Preview size | Select the preview size for the returned record. Options include, `Small`, `Large`, `Extra large`, and `PDF`. The default is `Small`. |
| With previews | Select whether to include file preview information in the response. |
| With priority color | Select whether to include file priority color information in the response. |
| Sort by | Enter a fields and direction to sort the returned records by. Options include, `path`, `size`, `modified_at_datetime`, and `provided_modified_at`. |
| Per page | Enter the number of records to return on each page. |
| Page | Enter the index of the page to return from the results list. |

## Output

The following are the most common output fields. Refer to the [Files.com](https://developers.files.com/) documentation for a complete list of output fields.

| Output field | Description |
| --- | --- |
| Path | The path where the returned record is located. For example: `folder/file.txt`. |
| Created by ID | The ID of the user that created the record. |
| Display name | The name of the returned record that is displayed. |
| Type | The type of returned record. |
| Size | The size of the returned record. |
| Created at | The time that the record was created. |

---
