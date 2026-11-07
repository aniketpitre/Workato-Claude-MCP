---
url: 'https://docs.workato.com/en/connectors/outlook/new-updated-contact-trigger.md'
description: >-
  The New/updated contact trigger in the Outlook connector picks up new or
  updated contacts in the Outlook contact folder you monitor.
---

# Outlook - New/updated contact trigger

This trigger picks up new or updated contacts in your Outlook contact folder.

## Input

| Field | Description |
| --- | --- |
| Shared contacts mailbox | Provide the email address of the shared mailbox to fetch shared contacts. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows the default contacts from your Outlook account. |
| Contact folder | Select the contact folder to monitor for new contacts, limited to 200 folders. If not selected, root folder is monitored. |
| When first started, this recipe should pick up events from | When you start a recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records added one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Select how frequently to check for new/updated contacts. It defaults to five minutes if left blank. The minimum value allowed is five minutes. |

## Output

| Field | Description |
| --- | --- |
| First name | The contact's first name. |
| Surname | The contact's surname. |
| Middle name | The contact's middle name. |
| Mobile phone | The contact's mobile phone number. |
| Office location | The location of the contact's office. |
| Personal notes | The user's notes about the contact. |
| Profession | The contact's profession. |
| Company name | The name of the contact's company. |
| Department | The contact's department. |
| Job title | The contact’s job title. |
| Manager | The name of the contact's manager. |
| Title | The contact's title. |
| Nick name | The contact's nickname. |
| Spouse name | The name of the contact's spouse/partner. |
| Yomi company name | The phonetic Japanese company name of the contact. |
| Yomi given name | The phonetic Japanese given name (first name) of the contact. |
| Yomi surname | The phonetic Japanese surname (last name) of the contact. |
| Assistant name | The name of the contact's assistant. |
| Birthday | The contact's birthday. |
| File as | The name the contact is filed under. |
| Generation | The contact's generation. |
| Initials | The contact's initials. |
| Other address | The other addresses for the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Home address | The home address of the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Business address | The business address of the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Business home page | The business home page of the contact. |
| Email addresses | The email addresses of the contact. Each item in the list includes the contact's email address and name. |
| Business phones | The contact's business phone numbers. |
| Home phones | The contact's home phone numbers. |
| Children | The names of the contact's children. |
| Categories | The categories associated with the contact. |
| IM addresses | The contact's instant messaging (IM) addresses. |
| ID | The unique identifier for the contact. |
| Change key | The change key for the contact. |
| Display name | The display name of the contact. |
| Created date time | The date and time the contact was created. |
| Last modified date time | The date and time the contact was last modified. |
| Parent folder ID | The ID of the parent folder. |

---
