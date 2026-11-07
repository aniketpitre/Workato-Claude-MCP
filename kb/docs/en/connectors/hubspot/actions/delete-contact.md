---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/delete-contact.md'
description: >-
  The Delete contact action in the HubSpot connector deletes a contact matching
  the given contact ID or email from your HubSpot portal.
---

# HubSpot - Delete contact action

The **Delete contact** action deletes a contact that matches the given contact ID or email from your HubSpot portal. If a contact with the same email address interacts with the portal again (through a form submission, for example), the contact is added back into the user interface.

> **WARNING**
> 
> Take extra precaution when using this action as deleted objects may be deleted permanently. We suggest that all delete actions be committed manually and under supervision.

## Input

| Input field | Description |
| --- | --- |
| Identification method | Contact email | Deletes the contact that corresponds to the email. |
| Contact VID | Deletes the contact that corresponds to the VID. |

## Output

This action doesn't return any output fields.

---
