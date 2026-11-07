---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action retrieves the details of a specific record
  in Pipedrive.
---

# Pipedrive - Get record details by ID action

The **Get record details by ID** action retrieves the details of a specific record in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |
| ID | Enter the unique identifier for the object. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify the object to delete.

## Output

The **Get record details by ID** action's output fields vary based on your selected **Object** type. The following output table uses a **Pipeline** object as an example:

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the pipeline. |
| Name | The name of the pipeline. |
| Order number | The sequence number of the pipeline. |
| Is deleted | Indicates whether the pipeline was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this pipeline. |
| Add time | A timestamp indicating when this pipeline was created. |
| Update time | A timestamp indicating when this pipeline was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |

> **VARIABLE OUTPUT**
> 
> The **Get record details by ID** action's output fields vary based on your selected **Object** type.
