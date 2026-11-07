---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/update-record-action.md
description: >-
  The Update record action enables you to update the details of a specific
  record in Pipedrive.
---

# Pipedrive - Update record action

The **Update record** action updates a record you specify in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to update. |
| ID | Enter the unique identifier of the pipeline object to update. |
| Name | Enter a name for the object. |
| Is deal probability enabled | Select whether to enable deal probability for the object. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify details for the new object.

## Output

The **Update record** action's output fields vary based on your selected **Object** type. The following output table uses a **Pipeline** object as an example:

| Output field | Description |
| --- | --- |
| ID | The pipeline's unique identifier. |
| Name | The name of the pipeline. |
| Order number | The sequence number of the pipeline. |
| Is deleted | Indicates whether the pipeline was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for the pipeline. |
| Add time | A timestamp indicating when this pipeline was created. |
| Update time | A timestamp indicating when this pipeline was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |

> **VARIABLE OUTPUT**
> 
> The **Update record** action's output fields vary based on your selected **Object** type.
