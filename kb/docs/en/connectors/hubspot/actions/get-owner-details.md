---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/get-owner-details.md'
description: >-
  The Get owner details action in the HubSpot connector retrieves a list of
  owners from your HubSpot account.
---

# HubSpot - Get owner details action

The **Get owner details** action retrieves a list of owners from HubSpot.

## Input

| Input field | Description |
| --- | --- |
| Email | Filter results by the owner's email address. |
| Include inactive | Specify whether to include archived (inactive) owners in the results. The default is `false`. |
| Limit | Specify the maximum number of results to return per page. The default is `500`. |
| Next page token | Map the Next page token datapill to retrieve the next page of results. |

## Output

This action returns a list of owners matching the input criteria, along with a paging object used for pagination.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/get-owner-details-by-id.md
description: >-
  The Get owner details by ID action in the HubSpot connector retrieves owners
  that match the ID you provide, with an option to include archived owners.
---

# HubSpot - Get owner details by ID action

The **Get owner details by ID** action retrieves all owners in a HubSpot account that match the ID you provide. You can select whether to retrieve archived owners in the results.

HubSpot uses owners to [assign](https://knowledge.hubspot.com/crm-setup/how-to-set-an-owner) specific users to contacts, companies, deals, tickets, or engagements. Any HubSpot user with access to contacts can be assigned as an owner, and multiple owners can be assigned to an object by creating a [custom property](https://knowledge.hubspot.com/crm-setup/manage-your-properties#create-custom-properties).

## Input

| Input field | Description |
| --- | --- |
| ID | Provide the ID of the owner to retrieve details for. |
| Archived | Select **Yes** to return only results that have been archived. Default is **No**. |

## Output

If the request is successful, Workato returns information about the owner that matches the ID provided. You can use these datapills in subsequent recipe steps. See the HubSpot [API Reference](https://legacydocs.hubspot.com/docs/methods/owners/get_an_owner) to view available fields.

---

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

---
