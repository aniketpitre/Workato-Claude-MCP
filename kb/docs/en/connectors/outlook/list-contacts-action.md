---
url: 'https://docs.workato.com/en/connectors/outlook/list-contacts-action.md'
description: >-
  The List contacts action in the Outlook connector lets you retrieve contacts
  from a specific folder in batches, with paging beyond the first 200.
---

# Outlook - List contacts action (batch)

Use this action to retrieve contacts from a specific contact folder in Outlook. This action retrieves the first 200 contacts. Configure the page token to retrieve additional contacts.

## Input

| Field | Description |
| --- | --- |
| Shared contacts mailbox | Provide the email address of the shared mailbox to fetch shared contacts. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows the default contacts from your Outlook account. |
| Contact folder path | Specify the contact folder path where you plan to list contacts. For example, `Parentfoldername/subfoldername`. |
| Max results | Enter a value for maximum results returned. Defaults to 200. |
| Page token | Specify the next page link. This value is available in the output of the Search contacts action. |

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
| Yomi given name | The contact's phonetic Japanese given name (first name). |
| Yomi surname | The contact's phonetic Japanese surname (last name). |
| Assistant name | The name of the contact's assistant. |
| Birthday | The contact's birthday. |
| File as | The name the contact is filed under. |
| Generation | The contact's generation. |
| Initials | The contact's initials. |
| Other address | The additional addresses of the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Home address | The home address of the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Business address | The business address of the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Business home page | The business home page of the contact. |
| Email addresses | The email addresses of the contact. |
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
| Parent folder ID | Provide the ID of the parent folder. |

---
