---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/get-contacts-associated-with-company-batch.md
description: >-
  The Get contacts associated with a company batch action in the HubSpot
  connector retrieves all contacts associated with a company by company ID.
---

# HubSpot - Get contacts associated with a company action (batch)

The **Get contacts associated with a company** batch action retrieves all contacts associated with a company in HubSpot in descending order when you provide the company ID.

## Input

| Input field | Description |
| --- | --- |
| Company ID | The ID of the company from which you plan to get associated contacts. You can find the company ID at the end of the URL of the company's page. |
| Count | Specify the number of contacts to return in the response. 20 contacts are returned if no limit is set. |
| Properties | Only contact properties you select are returned. Leave this field blank if you plan to retrieve all properties. |
| Property mode | Select the value and version history to retrieve the entire version history of the contact properties. |

## Output

If the request is successful, Workato returns a list of records that the company contact is associated with. You can use these datapills in subsequent recipe steps.

This action retrieves all contacts associated with a company in HubSpot in descending order when you provide the company ID. Additionally, you can select whether to retrieve the version history of fields and/or the list memberships of the contact.
