---
url: 'https://docs.workato.com/en/connectors/box/action-folder-shared-link.md'
description: >-
  The Create folder shared link action generates a direct shared link to a
  folder in Box.
---

# Box - Create folder shared link action

The **Create folder shared link** action generates a direct link to a folder in Box. You can control access levels and apply a password if your Box subscription supports it.

## Input

| Input field | Description |
| --- | --- |
| Folder ID | Enter the ID of the folder for which you plan to create a shared link. |
| Access | Select the access level for the shared link. Options include `Open`, `Company`, `Collaborators`, or `Default`. |
| Password | Enter a password for the shared link. This requires a Premium Box subscription. |

## Output

| Output field | Description |
| --- | --- |
| ID | ID of the folder. |
| Name | Name of the folder. |
| Type | Type of object, such as `folder`. |
| Description | Description of the folder. |
| Size | Size of the folder. |
| Shared link | Shared link details for the folder. |
| Created at | Timestamp when the folder was created. |
| Modified at | Timestamp when the folder was last modified. |
| Trashed at | Timestamp when the folder was moved to trash. |
| Purged at | Timestamp when the folder was permanently deleted. |
| Content created at | Timestamp when the folder content was created. |
| Content modified at | Timestamp when the folder content was last modified. |
| Sequence ID | Position of the folder in the hierarchy. |
| Etag | Entity tag identifying the version of the folder. |
| Sha 1 | SHA-1 hash value of the folder. |
| Parent | Parent folder details. |
| Path | Folder path. |
| Path collection | Collection of all folder paths containing the folder. |
| Created by | User who created the folder. |
| Modified by | User who last modified the folder. |
| Owned by | User who owns the folder. |
| Item status | Status of the folder, such as `active`. |

---
