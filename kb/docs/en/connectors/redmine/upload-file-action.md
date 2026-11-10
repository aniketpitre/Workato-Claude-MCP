---
url: 'https://docs.workato.com/en/connectors/redmine/upload-file-action.md'
description: >-
  The Upload file action uploads a file to Redmine and returns a token you can
  use to attach the file to an issue.
---

# Redmine - Upload file action

The **Upload file** action uploads a file to Redmine and returns a token. The file isn't attached to an issue until you map the token into the **Uploads** input field of a [Create record](/en/connectors/redmine/create-record-action) or [Update record](/en/connectors/redmine/update-record-action) action.

Each token can be used once. To attach the same file to more than one issue, upload it again for each issue.

## Input

| Input field | Description |
| --- | --- |
| File content | Map the file content datapill from a previous step. |
| File name | Enter the name of the file, including its extension. For example, `image.png`. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the uploaded file. |
| Token | Token that identifies the uploaded file. Map this value into the **Token** field under **Uploads** to attach the file to an issue. |

---
