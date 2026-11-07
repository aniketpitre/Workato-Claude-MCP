---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/create-record-action.md
description: The Create record action creates an object in Pipedrive.
---

# Pipedrive - Create record action

The **Create record** action creates an object in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to create. |
| Name | Enter the name of the object. |
| Is deal probability enabled | Specify whether deal probability is enabled. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify details for the new object.

## Output

The **Create record** action's output fields vary based on your selected **Object** type. The following output table uses a **Pipeline** object as an example:

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
