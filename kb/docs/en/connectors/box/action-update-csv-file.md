---
url: 'https://docs.workato.com/en/connectors/box/action-update-csv-file.md'
description: >-
  The Update CSV file action updates or appends data to an existing CSV file in
  Box.
---

# Box - Update CSV file in box action

The **Update CSV file in box** action updates an existing CSV file in Box. The file size after appending must not exceed **50 MB**.

## Input

| Input field | Description |
| --- | --- |
| File | Select the CSV file you plan to update. |
| Column delimiter | Define the character used to separate column values. Defaults to **comma**. |
| File encoding type | Select the encoding format for the file. Defaults to **UTF-8**. |
| Append | Choose whether to append or overwrite the existing file. |
| Column headers | Enter column names, each on a new line. By default, the action retrieves headers from the existing CSV file. |

## Output

| Output field | Description |
| --- | --- |
| File version | Details of the current file version. |
| ID | ID of the file. |
| Name | Name of the file. |
| Type | Object type. |
| Description | File description. |
| Size | File size. |
| Shared link | Shared link details. |
| Created at | Timestamp when the file was created. |
| Modified at | Timestamp when the file was last modified. |
| Trashed at | Timestamp when the file was moved to trash. |
| Purged at | Timestamp when the file was permanently deleted. |
| Content created at | Timestamp when the file content was created. |
| Content modified at | Timestamp when the file content was last modified. |
| Sequence ID | Position of the file in the folder hierarchy. |
| Etag | Entity tag for the file version. |
| Sha 1 | SHA-1 hash of the file. |
| Parent | Parent folder details. |
| Path | File path. |
| Path collection | Collection of folder paths for the file. |
| Created by | User who created the file. |
| Modified by | User who last modified the file. |
| Owned by | File owner. |
| Item status | Status of the file. |

---
