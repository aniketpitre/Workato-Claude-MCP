---
url: 'https://docs.workato.com/en/connectors/box/action-rename-user.md'
description: >-
  The Rename other user's file or folder action renames a file or folder that
  belongs to another user in your Box organization. Admin privileges are
  required.
---

# Box - Rename other user's file or folder action

The **Rename other user's file or folder** action renames a file or folder owned by another user in your Box organization.

This action requires admin privileges and the following connection scopes:

- **Admin can make calls on behalf of users**
- **Global content manager**

Admins can rename files and folders of all managed users, including co-admins. Co-admins can rename only files and folders of managed users.

## Input

| Input field | Description |
| --- | --- |
| User ID | Enter the ID of the user who owns the file or folder. You can find this in the output of other Box triggers or actions. |
| File/folder ID | Enter the ID of the file or folder to rename. You can find this in the output of other Box triggers or at the end of the file/folder URL in Box. |
| Type | Select whether the item is a `file` or a `folder`. |
| New file/folder name | Enter the new name of the file or folder. |

## Output

| Output field | Description |
| --- | --- |
| Folder upload email | The upload email address of the folder, if applicable. |
| Item collection | The collection of items inside the folder, if applicable. |
| ID | Unique identifier of the file or folder. |
| Name | The name of the file or folder. |
| Type | Type of the object, such as `file` or `folder`. |
| Description | Description of the file or folder. |
| Size | Size of the file. |
| Shared link | Shared link details of the file or folder. |
| Created at | Timestamp when the item was created. |
| Modified at | Timestamp when the item was last modified. |
| Trashed at | Timestamp when the item was moved to trash. |
| Purged at | Timestamp when the item was permanently deleted. |
| Content created at | Timestamp when the content was created. |
| Content modified at | Timestamp when the content was last modified. |
| Sequence ID | Position of the item in the folder hierarchy. |
| Etag | Entity tag identifying the version of the item. |
| Sha 1 | SHA-1 hash of the file. |
| Parent | Parent folder details. |
| Path | Path of the file or folder. |
| Path collection | Collection of all parent paths containing the item. |
| Created by | User who created the item. |
| Modified by | User who last modified the item. |
| Owned by | User who owns the item. |
| Item status | Status of the item, such as `active`. |

---
