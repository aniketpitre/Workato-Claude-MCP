---
url: 'https://docs.workato.com/en/connectors/egnyte/get-event-details-action.md'
description: >-
  The Get event details action in the Egnyte connector lets you fetch the
  details of an Egnyte event using its object URI.
---

# Egnyte - Get event details action

The **Get event details** action allows you to fetch the details of an Egnyte event.

![Get event details action](/assets/get-event-details-action.CVkg4NqI.png)_Get event details action_

## Input

| Input field | Description |
| --- | --- |
| Event object URI | The unique address for the event object. You can find this value in the trigger output `object detail` parameter. For example `https://example.egnyte.com/pubapi/v1/fs/Shared/Egnyte%20Reports` |

## Output

| Output field | Description |
| --- | --- |
| Name | The name of the event. For example: `Egnyte Reports`. |
| Last modified | The timestamp when the event was last modified. |
| Uploaded | The timestamp when the item was uploaded. For example: `2024-02-26T23:06:36.538000+00:00`. |
| Count | The count of items within the folder. For example: `7`. |
| Offset | The offset used for pagination. |
| Path | The path to the event folder or file. For example: `/Shared/Egnyte Reports`. |
| Folder ID | The ID of the folder. For example: `c5fb09ef-6232-4b42-ab28-0f9da5449110`. |
| Total count | The total count of items within the folder. For example: `11`. |
| Parent ID | The ID of the parent folder. For example: `890acb4a-7039-422a-b282-de8211b82447`. |
| Is folder | Indicates if the item is a folder or not. Values are `true` or `false`. |
| Public links | The type of public links allowed. For example: `files_folders`. |
| Restrict move delete | Indicates if moving or deleting is restricted or not. Values are `true` or `false`. |
| Allow links | Indicates if linking is allowed or not. Values are `true` or `false`. |
| Folders | A nested object detailing subfolders, including subfolder names, last modified dates, uploaded timestamps, path, folder ID, and parent ID. |

---
