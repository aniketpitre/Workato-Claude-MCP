---
url: 'https://docs.workato.com/en/connectors/onedrive/delete-file-folder-action.md'
description: >-
  The Delete file or folder action in the OneDrive connector moves a specified
  file or folder to the recycle bin in Microsoft OneDrive.
---

# OneDrive - Delete file or folder action

The **Delete file or folder** action moves the specified file or folder to the recycle bin in Microsoft OneDrive without permanently deleting it. To delete a file or folder from a shared folder, enter the ID of the shared folder in the **Drive ID** field.

## Input

| Input fields | Description |
| --- | --- |
| Drive ID | Provide the drive ID from which you plan to delete the file or folder. The **Drive ID** appears in the CID parameter of the OneDrive URL. For example, in `https://onedrive.live.com/?id=244DDFC44A57%21103&cid=24C9A8FC44A57` `24C9A8FC44A57` is the drive ID. |
| Delete file or folder? | Specify whether to delete a file or folder. |
| File or folder path | Provide the file or folder path of the resource you plan to delete. For example, `test.xlsx` or `folder-one/folder-two`. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the file or folder was successfully deleted. |

---
