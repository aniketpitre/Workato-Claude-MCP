---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/search-records-action.md
description: >-
  The Search records action retrieves a list of records for an object in
  Pipedrive.
---

# Pipedrive - Search records action

The **Search records** action retrieves a list of records for an object in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |
| Limit | Enter the maximum number of records to return. |
| Cursor | Provide the `next_cursor` value to retrieve the next page of results. Defaults to the first page if left blank. |
| Sort by | Select the object to use to sort results. |
| Sort direction | Select whether to sort records in ascending or descending order. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify details for the new object.

## Output

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the object. |
| Name | The name of the object. |
| Order number | The sequence number of the object. |
| Is deleted | Indicates whether the object was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this pipeline. |
| Add time | A timestamp indicating when this object was created. |
| Update time | A timestamp indicating when this object was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |

> **VARIABLE OUTPUT**
> 
> The **Search records** action's output fields vary based on your selected **Object** type.
