---
url: 'https://docs.workato.com/en/connectors/zoho-desk/delete-record-action.md'
description: The Delete record action enables you to delete a record in Zoho Desk.
---

# Zoho Desk - Delete record action

The **Delete record** action enables you to delete a record in Zoho Desk.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object to create the record. Fields load dynamically based on the object you select. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates if the record was deleted successfully. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-desk/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action enables you to retrieve details of a
  specific record in Zoho Desk.
---

# Zoho Desk - Get record details by ID action

The **Get record details by ID** action enables you to retrieve details of a specific record in Zoho Desk.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object to create the record. Fields load dynamically based on the object you select. |

For example, if the selected object is **Contact**, the input schema is as follows:

| Input fields | Description |
| --- | --- |
| Contact ID | Enter the ID of the contact. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

For example, if the selected object is **Contact**, the output schema is as follows:

| Output field | Description |
| --- | --- |
| First name | First name of the contact. |
| Last name | Last name of the contact. |
| Email | Email ID of the contact. |
| Account name | Account name to which the contact is linked. |
| Phone | Phone number of the contact. |
| Mobile | Mobile number of the contact. |
| Title | Title of the contact. |
| Contact owner | ID of the user who creates the contact. |
| Type | Type of the contact. |
| Street | Street address of the contact. |
| City | City of residence of the contact. |
| State | State of residence of the contact. |
| Zip | Zip code of the contact. |
| Country | Country of residence of the contact. |
| Description | Description of the contact. |
| Twitter | Twitter ID of the contact. |
| Facebook | Facebook ID of the contact. |
| Secondary email | Secondary email ID of the contact. |
| Custom fields | User-defined fields related to contact. |
| Contact ID | ID of the contact. |
| Created time | Timestamp when the record was created. |
| Modified time | Timestamp when the record was last modified. |
| Photo URL | Photo URL of the contact. |
| Web URL | Web URL of the contact. |
| Is end user | Indicates if the contact is an end user. |
| Account ID | Account ID of the contact. |
| Account count | Account count of the contact. |
| Layout ID | Layout ID of the contact. |
| Is anonymous | Indicates if the contact is anonymous. |
| Is spam | Indicates if the contact is spam. |

Refer to the Zoho Desk [Documentation](https://desk.zoho.com/support/APIDocument.do#Contacts#Contacts_GetContact) for more information.

---
