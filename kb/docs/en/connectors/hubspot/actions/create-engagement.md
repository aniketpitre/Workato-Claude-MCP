---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/create-engagement.md'
description: >-
  The Create engagement action in the HubSpot connector creates an engagement
  such as an email, call, meeting, task, or note on an object.
---

# HubSpot - Create engagement action

The **Create engagement** action creates an engagement, such as an email, call, meeting, task, or note, on an object in HubSpot. An engagement is useful for keeping your CRM records up-to-date with interactions that take place outside of HubSpot. Activity reporting in the CRM also uses this data.

## Input

| Input field | Description |
| --- | --- |
| Engagement | Active | Indicates whether the engagement is active. |
| Type | The type of engagement. The available values are **Email**, **Call**, **Meeting**, **Task**, and **Note**. |
| Timestamp | This timestamp is treated as the time that the engagement happened, and determines where the engagement appears in the timeline for any associated records. |
| Owner ID | Owner ID of the engagement. Task engagements use the ownerId to populate the Assigned to field. |
| Associations | Contact | Contact IDs to be associated with the engagement. You can associate engagements with objects to ensure they're displayed correctly in the UI. |
| Company | Company IDs to be associated with the engagement. You can associate engagements with objects to ensure they're displayed correctly in the UI. |
| Deal | Deal IDs to be associated with the engagement. You can associate engagements with objects to ensure they're displayed correctly in the UI. |
| Owner | Owner IDs to be associated with the engagement. You can associate engagements with objects to ensure they're displayed correctly in the UI. |
| Attachments | ID of items to be attached to the engagement. |

## Output

If the request is successful, Workato returns a record representing the newly created engagement. You can use these datapills in subsequent recipe steps. Refer to the HubSpot documentation to learn more about the available fields for [creating an engagement](https://legacydocs.hubspot.com/docs/methods/engagements/create_engagement).

---
