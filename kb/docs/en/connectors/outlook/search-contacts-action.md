---
url: 'https://docs.workato.com/en/connectors/outlook/search-contacts-action.md'
description: >-
  The Search contacts action in the Outlook connector lets you find contacts in
  a folder that match your criteria, returning 200 per batch.
---

# Outlook - Search contacts action (batch)

Use this action to search for contacts from the selected Outlook contact folder that match the search criteria. This action retrieves the first 200 contacts. Use the page token to retrieve additional contacts.

## Input

| Field | Description |
| --- | --- |
| Shared contacts mailbox | Provide the email address of the shared mailbox to search shared contacts. For example. `support@example.onmicrosoft.com`. If left blank, Workato shows the default contact folder from your Outlook account. |
| Contact folder path | Specify contact folder path. For example, `Parentfoldername/subfoldername`. |
| Search by | Search for specific Outlook contacts by specifying search by fields. Only contacts matching all specified fields will be retrieved. Available search fields are listed in the [search fields](#search-fields) table. |
| Search query | Search by providing OData based filters. If provided, this will override any search details provided in the **Search by** field. [Learn more](https://learn.microsoft.com/en-us/graph/query-parameters?tabs=http#filter-parameter). |
| Max results | Enter a value for maximum results returned. Defaults to 200. |
| Page token | Specify the next page link. This value is available in the output of Search contacts and List contacts actions. |

### Search by fields table

| Field | Description |
| --- | --- |
| First name | Provide the contact's first name. |
| Surname | Provide the contact's surname. |
| Middle name | Provide the contact's middle name. |
| Mobile phone | Provide the contact's mobile phone number. |
| Office location | Provide the location of the contact's office. |
| Personal notes | Provide the user's notes about the contact. |
| Profession | Provide the contact's profession. |
| Company name | Provide the name of the contact's company. |
| Department | Provide the contact's department. |
| Job title | Provide the contact’s job title. |
| Manager | Provide the name of the contact's manager. |
| Title | Provide the contact's title. |
| Nick name | Provide the contact's nickname. |
| Spouse name | Provide the name of the contact's spouse/partner. |
| Yomi company name | Provide the phonetic Japanese company name of the contact. |
| Yomi given name | Provide the phonetic Japanese given name (first name) of the contact. |
| Yomi surname | Provide the phonetic Japanese surname (last name) of the contact. |
| Assistant name | Provide the name of the contact's assistant. |
| Birthday | Provide the contact's birthday. |
| File as | Provide the name the contact is filed under. |
| Generation | Provide the contact's generation. |
| Initials | Provide the contact's initials. |
| Other address | Provide the other addresses for the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Home address | Provide the home address of the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Business address | Provide the business address of the contact. This object includes the contact's city, country or region, postal code, state, and street. |
| Business home page | Provide the business home page of the contact. |
| Email address | Provide the email address of the contact. |
| Created date time | Provide the date and time the contact was created. |
| Last modified date time | Provide the date and time the contact was last modified. |
| Parent folder ID | Provide the ID of the parent folder. |

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
| Other address | The additional addresses for the contact. This object includes the contact's city, country or region, postal code, state, and street. |
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
| Parent folder ID | The ID of the parent folder. |

---
