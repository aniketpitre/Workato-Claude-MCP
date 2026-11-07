---
url: 'https://docs.workato.com/en/connectors/sftp/change-permission-action.md'
description: >-
  The Change permission of a file action sets new access permissions for a file
  on the SFTP server.
---

# SFTP - Change permission of a file action

The **Change permission of a file** action updates access permissions for a specified file on an SFTP server. This action replaces the existing permissions with new values you provide.

## Input

| Input field | Description |
| --- | --- |
| File path | Provide the full path of the file, including the file name. For example: `/folder1/folder2/filename.csv`. |
| Apply permissions method | Choose how to apply file permissions. Options include **Custom permission** and **Select permission**. Defaults to **Select permission**. |
| Permission for Owner | Select one or more permissions for the file owner. Available options include **Read, Write & Execute (7)**, **Read & Write (6)**, **Read & Execute (5)**, **Read Only (4)**, **Write & Execute (3)**, **Write Only (2)**, **Execute Only (1)**, and **No Permission (0)**. This field appears when you select **Select permission** as the **Apply permissions method**. |
| Permission for Group | Select one or more permissions for the group. Available options include **Read, Write & Execute (7)**, **Read & Write (6)**, **Read & Execute (5)**, **Read Only (4)**, **Write & Execute (3)**, **Write Only (2)**, **Execute Only (1)**, and **No Permission (0)**. This field appears when you select **Select permission** as the **Apply permissions method**. |
| Permission for Others | Select one or more permissions for others. Available options include **Read, Write & Execute (7)**, **Read & Write (6)**, **Read & Execute (5)**, **Read Only (4)**, **Write & Execute (3)**, **Write Only (2)**, **Execute Only (1)**, and **No Permission (0)**. Defaults to **None**. This field appears when you select **Select permission** as the apply permissions method. |
| Permission code | Enter a 3-digit permission code. Defaults to `644`. This field appears when you select **Custom permission** as the **Apply permissions method**. |

## Output

| Output field | Description |
| --- | --- |
| File path | Returns the full path of the file. |
| Updated permission code | Returns the three-digit permission code applied to the file. |

---
