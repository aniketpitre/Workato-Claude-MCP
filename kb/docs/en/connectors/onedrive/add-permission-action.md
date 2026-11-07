---
url: 'https://docs.workato.com/en/connectors/onedrive/add-permission-action.md'
description: >-
  The Add permission action in the OneDrive connector grants read or write
  access to a file or folder for specified recipients in Microsoft OneDrive.
---

# OneDrive - Add permission action

The **Add permission** action adds permission to a file or folder for specified recipients in Microsoft OneDrive.

## Input

| Input fields | Description |
| --- | --- |
| File/folder | Provide the file or folder ID. For example, `01G65C3RKY7QJD67NCMVAYKVFGW3KBGK75`. |
| Role | Specify the type of permission. Allowed values include `read` or `write`. |
| Recipients | Input a list datapill to provide an array of recipient email addresses. Only one of these values is required. |
| Message | A plain text formatted message that is included in the sharing invitation. The maximum length is `2000` characters. |
| Require sign in | Specifies whether the recipient of the invitation is required to sign-in to view the shared item. |
| Send invitation | Select `Yes` to send a sharing link to recipients. Choose `No` to grant permissions directly without notifications. |

## Output

| Output fields | Description |
| --- | --- |
| Roles | An array of roles granted. |
| Granted to identities | Information about the users to whom the permission is granted. |
| Granted to | Information about the user to whom the permission is granted. |
| Link | Information about the sharing link, including scope and type. |
| Invitation | Information about the invitation sent, including email and sign-in requirement. |

---
