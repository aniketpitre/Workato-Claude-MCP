---
url: 'https://docs.workato.com/en/connectors/telegram/get-file-action.md'
description: >-
  Get a Telegram file's size and server path before fetching its contents with
  the Download file action.
---

# Telegram - Get file action

The **Get file** action retrieves metadata about a file stored on the servers in Telegram.

> **CHAIN INTO DOWNLOAD FILE**
> 
> This action returns file metadata, including the file path, which is valid for at least one hour. Use the output of this action as input for the [Download file](/en/connectors/telegram/download-file-action) action to fetch the file's actual bytes and keep the API token on the server side.

## Input

| Input field | Description |
| --- | --- |
| File ID | Enter the file identifier to get information about. |

## Output

| Output field | Description |
| --- | --- |
| File ID | The file identifier, usable to download or reuse the file. |
| File unique ID | The file identifier that's the same over time and for different bots. Can't be used to download or reuse the file. |
| File size | The file size, if known. Measured in bytes. |
| File path | The file's path on Telegram's servers. Use this with the [Download file](/en/connectors/telegram/download-file-action) action. |

---
