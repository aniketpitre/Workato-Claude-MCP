---
url: 'https://docs.workato.com/en/connectors/greenhouse/upload-attachment-action.md'
description: >-
  The Upload attachment action in the Greenhouse connector lets you attach a
  file to a candidate or application identified by its Greenhouse ID.
---

# Greenhouse - Upload attachment action

This action uploads an attachment to a Greenhouse object identified by the unique Greenhouse ID.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Create attachment (v3)](/en/connectors/greenhouse/create-attachment-v3) action before this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Upload attachment ction](/assets/upload-attachment-action.DAnWWCmI.png)_Upload attachment action_

## Input

| Input field | Description |
| --- | --- |
| Object | The object type. The available objects are:- Candidate
- Application |
| Object ID | The ID of the object you want to update. |
| Attachment type | The type of attachment. |
| File content | The contents of the attachment. |
| File URL | The file URL. **Instead of uploading by file content, you can load the file by the file URL**. |
| Content type | The content type of the file. |

## Output

| Output field | Description |
| --- | --- |
| Filename | The filename. |
| Type | The attachment type. |
| URL | The file URL. |
| Content type | The content type. |

---
