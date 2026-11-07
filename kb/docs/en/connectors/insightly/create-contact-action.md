---
url: 'https://docs.workato.com/en/connectors/insightly/create-contact-action.md'
description: >-
  The Create contact action in the Insightly connector lets you create a new
  contact with name, organization, email, phone, and address details.
---

# Insightly - Create contact action

This action creates a new contact in your Insightly instance.

## Input

| Field | Description |
| --- | --- |
| First name | The first name of the contact. |
| Last name | The last name of the contact. |
| Salutation | The salutation of the contact. |
| Organization | The organization of the contact. |
| Role | The role of the contact. |
| Tags | The tags of the contact. |
| Tags source list | The source list from which the contact tags are derived. This field accepts a [list datapill](/en/features/list-management#list-batch-action) as input. |
| Tag name | The name of the tag assigned to the contact. |
| Background | The background of the contact. |
| Visible to | The visibility of the contact. |
| Visible user IDs | The visible user IDs of the contact. |
| Work email | The work email of the contact. |
| Personal email | The personal email of the contact. |
| Other email | The other email of the contact. |
| Work phone | The work phone of the contact. |
| Mobile | The mobile phone of the contact. |
| Home phone | The home phone of the contact. |
| Website | The website of the contact. |
| Addresses | The addresses of the contact. |
| Addresses source list | The source list from which the addresses of the contact are derived. This field accepts a [list datapill](/en/features/list-management#list-batch-action) as input. |
| Address type | The type of address (for example, work, home, postal, or other). |
| Street | The street part of the contact's address. |
| City | The city of the contact's address. |
| State | The state of the contact's address. |
| Post code | The postal code of the contact's address. |
| Country | The country of the contact's address. |

## Output

The output of this action is a datatree that contains information about the [contact](https://api.insightly.com/v3.1/Help#!/Contacts/GetEntities) created.

---
