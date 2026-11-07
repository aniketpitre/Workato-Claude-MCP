---
url: 'https://docs.workato.com/en/connectors/box/action-file-folder-shared-link.md'
description: >-
  The Create file shared link action generates a direct shared link to a file in
  Box.
---

# Box - Create file shared link action

The **Create file shared link** action generates a direct link to a file in Box. You can control access levels and apply a password if your Box subscription supports it.

## Input

| Input field | Description |
| --- | --- |
| File ID | Enter the ID of the file for which you plan to create a shared link. |
| Access | Select the access level for the shared link. Options include `Open`, `Company`, `Collaborators`, or `Default`. |
| Password | Enter a password for the shared link. This requires a Premium Box subscription. |

## Output

| Output field | Description |
| --- | --- |
| ID | ID of the file. |
| Name | Name of the file. |
| Type | Type of object, such as `file`. |
| Description | Description of the file. |
| Size | Size of the file. |
| Shared link | Shared link details for the file. |
| Created at | Timestamp when the file was created. |
| Modified at | Timestamp when the file was last modified. |
| Trashed at | Timestamp when the file was moved to trash. |
| Purged at | Timestamp when the file was permanently deleted. |
| Content created at | Timestamp when the file content was created. |
| Content modified at | Timestamp when the file content was last modified. |
| Sequence ID | Position of the file in the folder hierarchy. |
| Etag | Entity tag identifying the version of the file. |
| Sha 1 | SHA-1 hash value of the file. |
| Parent | Parent folder details. |
| Path | Path of the file. |
| Path collection | Collection of all folder paths containing the file. |
| Created by | User who created the file. |
| Modified by | User who last modified the file. |
| Owned by | User who owns the file. |
| Item status | Status of the file, such as `active`. |

---
