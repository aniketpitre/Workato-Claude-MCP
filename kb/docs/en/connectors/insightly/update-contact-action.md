---
url: 'https://docs.workato.com/en/connectors/insightly/update-contact-action.md'
description: >-
  The Update contact action in the Insightly connector lets you update an
  existing contact by ID, including name, email, phone, and address.
---

# Insightly - Update contact action

This action updates a contact in your Insightly instance.

## Input

| Input field | Description |
| --- | --- |
| Contact ID | The ID of the contact to be updated. |
| First name | The first name of the contact. |
| Last name | The last name of the contact. |
| Salutation | The salutation of the contact. |
| Organization | The organization of the contact. |
| Role | The role of the contact. |
| Tags | The tags of the contact. |
| Tags source list | The source list from which the contact tags are derived. This field accepts a [list datapill](/en/features/list-management#list-batch-action) as input. |
| Tag name | The name of the tag assigned to the contact. |
| Background | Background information or notes about the contact. |
| Visible to | Specifies who can see this contact (for example everyone, owner, or individuals) |
| Visible user IDs | The IDs of users who can see this contact. |
| Work email | The work email address of the contact. |
| Personal email | The personal email address of the contact. |
| Other email | Any other email addresses associated with the contact. |
| Work phone | The work phone number of the contact. |
| Mobile | The mobile phone number of the contact. |
| Home phone | The home phone number of the contact. |
| Website | The website associated with the contact. |
| Addresses | The addresses of the contact. |
| Addresses source list | The source list from which the addresses of the contact are derived. This field accepts a [list datapill](/en/features/list-management#list-batch-action) as input. |
| Address type | The type of address (for example, work, home, postal, or other). |
| Street | The street part of the contact's address. |
| City | The city part of the contact's address. |
| State | The state part of the contact's address. |
| Post code | The postal code part of the contact's address. |
| Country | The country part of the contact's address. |

## Output

The output of this action is a datatree that contains information about the updated [contact](https://api.insightly.com/v3.1/Help#!/Contacts/GetEntities).

---

---
url: >-
  https://docs.workato.com/en/connectors/insightly/add-note-to-opportunity-action.md
description: >-
  The Add note to opportunity action in the Insightly connector lets you attach
  a note with a title and body to an opportunity.
---

# Insightly - Add note to opportunity action

This action adds a note to an opportunity in your Insightly instance.

## Input

| Input field | Description |
| --- | --- |
| Title | The title of the note. |
| Body | The body of the note. |
| Opportunity name | The name of the opportunity. |

## Output

The output of this action is a datatree that contains information about the note added to the [opportunity](https://api.insightly.com/v3.1/Help#!/Opportunities/GetEntities).

---
