---
url: 'https://docs.workato.com/en/connectors/greenhouse/create-attachment-v3.md'
description: >-
  The Create attachment (v3) action creates an attachment for an application in
  Greenhouse using the v3 API.
---

# Greenhouse - Create attachment (v3) action

The **Create attachment (v3)** action creates an attachment for an application in Greenhouse using the v3 API.

This action is available for OAuth 2.0 connections only.

## Input

| Input field | Description |
| --- | --- |
| Application ID | Provide the ID of the application to attach the file to. |
| Filename | Enter the name of the file. |
| Attachment type | Select the type of attachment to create. |
| File content | Enter the raw file content. Use this field or provide a file URL. |
| File URL | Enter the URL of the file. Use this field or provide file content. |
| Visibility | Select a visibility setting for the attachment. |

## Output

| Output field | Description |
| --- | --- |
| Attachment ID | ID of the created attachment. |
| Created at | Timestamp when the attachment was created. |
| Updated at | Timestamp when the attachment was last updated. |
| Application ID | ID of the associated application. |
| Candidate ID | ID of the associated candidate. |
| Type | Type of the attachment. |
| Filename | Name of the file. |
| URL | URL of the uploaded file. |
| Content type | MIME type of the file. |
| Visibility | Visibility setting of the attachment. |

---
