---
url: 'https://docs.workato.com/en/connectors/wrike/new-folder-trigger-real.md'
description: >-
  The New/updated folder trigger in the Wrike connector monitors folders that
  are created or updated in Wrike in real time.
---

# Wrike - New/updated folder trigger (real-time)

The **New/updated folder** trigger monitors folders created or updated in Wrike in real-time.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Select the start date and time to retrieve trigger events. If left blank, the trigger retrieves events created or updated one hour ago. You can't change this value after you run or test the recipe. |
| Fields to retrieve | Select additional fields to include in the output. If left blank, the trigger retrieves all custom fields and the following default fields: `metadata`, `hasAttachments`, `attachmentCount`, `description`, `briefDescription`, `customColumnIds`, `superParentIds`, and `customItemTypeId`. If **None** is selected, no additional fields are retrieved. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier for the folder. |
| Account ID | Unique identifier for the Wrike account associated with the folder. |
| Title | Name of the folder. |
| Created date | Timestamp indicating when the folder was created. |
| Updated date | Timestamp indicating when the folder was last updated. |
| Description | Folder description, if applicable. |
| List of users who share folder | Users who have access to the folder. |
| Parent folder | Folder that directly contains this folder. |
| Child folder | List of subfolders within this folder. |
| Super parent folder | Highest-level parent folder(s) in the hierarchy. |
| Custom field IDs | Identifiers of custom fields associated with the folder. |
| Brief description | Shortened version of the folder description. |
| Scope | Access scope of the folder. |
| Has attachments | Indicates whether the folder contains attachments. |
| Permalink | Direct URL to the folder in Wrike. |
| Workflow ID | Identifier for the workflow associated with the folder. |
| Metadata | Additional metadata associated with the folder. |
| Attachment count | Number of attachments in the folder. |
| Custom status | Current custom status of the folder, if applicable. |
| Project | Project details associated with the folder, if applicable. |
| Custom item type ID | Identifier for the custom item type. |
| Custom fields | List of custom field values assigned to the folder. |

---
