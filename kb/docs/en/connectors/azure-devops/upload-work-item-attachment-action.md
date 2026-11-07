---
url: >-
  https://docs.workato.com/en/connectors/azure-devops/upload-work-item-attachment-action.md
description: The Upload work item attachment action uploads an attachment to Azure DevOps.
---

# Azure DevOps - Upload work item attachment action

The **Upload work item attachment** action uploads an attachment to Azure DevOps.

## Input

| Input field | Description |
| --- | --- |
| Project | Select the project where you plan to upload a work item. |
| Work item ID | Enter the ID of the work item you plan to upload. |
| File name | Enter the name of the file you plan to upload. Provide the file extension in the file name. |
| Content | Enter the content of the work item you plan to upload. This must be binary file content or a text file. Maximum size is 130MB. |
| Comments | Enter a description of the attachment. |
| Work item output fields | Enter a sample JSON to include work item custom fields. |

## Output

This action has a large number of output fields. Refer to the [Azure DevOps](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2) documentation for a complete list of output fields.
