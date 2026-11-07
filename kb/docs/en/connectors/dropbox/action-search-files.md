---
url: 'https://docs.workato.com/en/connectors/dropbox/action-search-files.md'
description: >-
  The Search files action in the Dropbox connector lets you retrieve files whose
  names contain your keywords, including partial matches.
---

# Dropbox - Search files action

Retrieves a list of files whose name contains the search keywords. Partial matches are also returned.

## Input

| Field name | Description |
| --- | --- |
| Search keywords | Separate keywords with spaces. Search will return files containing all entered keywords in name. |
| Folder | Search is performed on this folder as well as its sub-folders. Leave blank to search all folders. |

## Output

| Field name | Description |
| --- | --- |
| ID | File ID. |
| Name | File name. |
| Path | File path. |
| Is directory | Whether this is a directory/folder. |
| Rev | A unique identifier for the current revision of the file. |
| Bytes | File size in bytes. |
| Size | File size in string format. |
| Modified | Date/time the file was last modified. |
| Client modified time | This is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not. |

---
