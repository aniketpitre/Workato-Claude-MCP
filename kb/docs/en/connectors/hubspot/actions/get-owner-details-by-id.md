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
