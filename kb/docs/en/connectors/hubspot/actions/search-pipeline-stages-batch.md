---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/search-pipeline-stages-batch.md
description: >-
  The Search pipeline stages action in the HubSpot connector lets you search
  pipeline stages within your HubSpot account.
---

# HubSpot - Search pipeline stages action

The **Search pipeline stages** action allows you to search pipeline stages within HubSpot.

## Input

| Input field | Description |
| --- | --- |
| Object | Select a standard HubSpot object. Options include **Deal** and **Ticket**. |
| Pipeline ID | Provide the ID of the pipeline you plan to search for. |

## Output

This action returns a list of pipeline stages for the pipeline ID you provided.

| Output field | Description |
| --- | --- |
| Stages | A list of pipeline stages returned for the specified pipeline. |
| Label (stages) | The display name of the stage. |
| Display order (stages) | The position of the stage in the pipeline, starting from 0. |
| Metadata (stages) | Additional properties about the stage, including status and behavior. |
| Is closed (metadata) | Indicates whether the stage represents a closed status. |
| Probability (metadata) | The likelihood of success at this stage. Only available if **Deal** is the selected object. |
| Ticket state (metadata) | The state of the ticket at this stage. Only available if **Ticket** is the selected object. |
| ID (stages) | The unique identifier for the pipeline stage. |
| Created at (stages) | Timestamp indicating when the stage was created. |
| Updated at (stages) | Timestamp indicating when the stage was last modified. |
| Archived (stages) | Indicates whether the stage has been archived. |
| Write permissions (stages) | Indicates whether the authenticated user has write access to the stage. |
