---
url: 'https://docs.workato.com/en/connectors/egnyte/get-object-details-action.md'
description: >-
  The Get object details action in the Egnyte connector lets you fetch the
  details of a selected file or folder object in Egnyte.
---

# Egnyte - Get object details action

The **Get object details** action allows you to fetch the details of an Egnyte object.

![Get object details action](/assets/get-object-details-action.DCn8czzG.png)_Get object details action_

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plant to fetch. |

## Output

| Output field | Description |
| --- | --- |
| Uploaded | The timestamp when the file was uploaded. For example: `2024-02-26T23:06:36.891999+00:00`. |
| Checksum | The checksum of the file for verification. For example: `c79fba1f4bf041a5ed667a0606538f27649b9a5bc7e76039fedec4`. |
| Size | The size of the file in bytes. For example: `448`. |
| Path | The path to the file. For example: `/Shared/Egnyte Reports/Folder Size/test-file.csv`. |
| Name | The name of the file. For example: `test-file.csv`. |
| Locked | Indicates if the file is locked or not. Values are `true` or `false`. |
| Permission | The permission level of the file. For example: `Owner`. |
| Is folder | Indicates if the item is a folder or not. Values are `true` or `false`. |
| Entry ID | The ID of the file entry. For example: `13b63eae-77a7-43ff-8ad4-05314e35fe8d`. |
| Group ID | The ID of the group associated with the file. For example: `d871bf95-8c07-4c61-8ec9-4f65e92b9b96`. |
| Last modified | The timestamp when the file was last modified. For example: `2024-02-26T23:06:36.000000+00:00`. |
| Uploaded by | The user who uploaded the file. |
| Num versions | The number of versions of the file. For example: `7`. |
| Parent ID | The ID of the parent folder. For example: `8c880bab-e6b4-41cd-949f-758182f06cca`. |

---
