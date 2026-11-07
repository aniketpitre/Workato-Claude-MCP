---
url: 'https://docs.workato.com/en/connectors/onedrive/list-permissions-action.md'
description: >-
  The List permissions batch action in the OneDrive connector lists the
  permissions assigned to a file or folder in Microsoft OneDrive.
---

# OneDrive - List permissions action (batch)

The **List permissions** batch action lists permissions for a file or folder in Microsoft OneDrive.

## Input

| Input field | Description |
| --- | --- |
| File/folder ID | Provide the ID of the file or folder to retrieve permissions. For example, `01G65C3RKY7QJD67NCMVAYKVFGW3KBGK75`. |

## Output

| Output fields | Description |
| --- | --- |
| Value | Provides an array of permissions for the file or folder. Each permission includes the ID, assigned roles, and the users or groups granted access. Specifies the sharing link (URL) and indicates if the permission is inherited from a parent folder or resource. |

---
