---
url: 'https://docs.workato.com/en/connectors/box/action-search-files.md'
description: >-
  The Search files or folders batch action in the Box connector searches for
  files or folders by name, description, or contents in Box.
---

# Box - Search files or folders action (batch)

The **Search files or folders** batch action searches for files or folders in Box by name, description, or contents.

Box may not return newly created files or folders immediately due to indexing delays. If your search does not return expected results, run the search again after some time. Refer to the Box [Search indexing](https://developer.box.com/guides/search/indexing/) guide for more information.

> **SEARCH RESULTS WITH % CHARACTER**
> 
> The **Search files or folders** action may return unrelated results when you search using the % character. This happens because Box performs a broad search across multiple fields, such as names, descriptions, and file contents, rather than performing an exact string match.
> 
> Set the **Type** field to match the item you plan to search for (**File** or **Folder**) and turn on **Exact match** in the action settings. This ensures that the search returns only items whose names match the text exactly, such as a folder named `Baz%Qux`.

## Input

| Input field | Description |
| --- | --- |
| Search text | Enter text to search against file name, description, or contents. Include the extension. For example, `File.csv`. |
| Type | Choose whether to search for `file` or `folder`. Defaults to `file`. |
| Starting folder | Select the folder to narrow the scope of the search. |
| File extensions | Enter a comma-separated list of file extensions to include. For example, `csv,txt,doc`. |
| Exact match | Choose whether to search using exact or partial match. Defaults to `No`. |
| Trash content | Decide whether to include items in the trash. Defaults to `Non trashed only`. |
| Limit | Define the maximum number of items to return per page. Defaults to `100`, maximum allowed is `200`. |
| Sort by | Select how to sort the search results. Defaults to `Relevance`. |
| Sort direction | Define the order of the results. Defaults to `Descending`. |

## Output

| Output field | Description |
| --- | --- |
| Files | A list of files or folders returned by the search. |
| ID | ID of the file or folder. |
| Name | Name of the file or folder. |
| Type | Type of the object, such as `file` or `folder`. |
| Description | Description of the file or folder. |
| Size | Size of the file. |
| Shared link | Shared link details. |
| Created at | Timestamp when the file or folder was created. |
| Modified at | Timestamp when the file or folder was last modified. |
| Trashed at | Timestamp when the file or folder was moved to trash. |
| Purged at | Timestamp when the file or folder was permanently deleted. |
| Content created at | Timestamp when the file content was created. |
| Content modified at | Timestamp when the file content was last modified. |
| Sequence ID | Position of this object in the folder hierarchy. |
| Etag | Entity tag identifying the version of the object. |
| Sha 1 | SHA-1 hash value of the file. |
| Parent | Parent folder details. |
| Path | File path. |
| Path collection | Collection of all folder paths containing the file. |
| Created by | User who created the file or folder. |
| Modified by | User who last modified the file or folder. |
| Owned by | User who owns the file or folder. |
| Item status | Status of the item, such as `active`. |
| List size | Number of items in the returned list. |
| List index | Index of the current item in the list. |

---
