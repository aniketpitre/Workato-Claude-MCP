---
url: 'https://docs.workato.com/en/connectors/zoho-desk/update-record-action.md'
description: >-
  The Update record action enables you to update the details of a specific
  record in Zoho Desk.
---

# Zoho Desk - Update record action

The **Update record** action enables you to update the details of a specific record in Zoho Desk.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create the record. Fields load dynamically based on the object you select. |

For example, if the selected object is **Contact**, the input schema will be below.

| Input fields | Description |
| --- | --- |
| Contact ID | Provide the unique ID of the contact. |
| First name | Enter the first name of the contact. |
| Last name | Enter the last name of the contact. |
| Email | Enter the email ID of the contact. |
| Account name | Select the account name to which the contact is linked. |
| Phone | Enter the phone number of the contact. |
| Mobile | Enter the mobile number of the contact. |
| Title | Enter the title of the contact. |
| Contact owner | Enter the ID of the user who created the contact. |
| Type | Select the type of contact. |
| Street | Enter the street address of the contact. |
| City | Enter the city of residence of the contact. |
| State | Enter the state of residence of the contact. |
| Zip | Enter the zip code of the contact. |
| Country | Enter the country of residence of the contact. |
| Description | Enter the description of the contact. |
| Twitter | Enter the Twitter ID of the contact. |
| Facebook | Enter the Facebook ID of the contact. |
| Secondary email | Enter the secondary email ID of the contact. |
| Custom fields | Enter any user-defined fields related to the contact. |
| Account | Enter the account name to which the contact is linked. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

For example, if the selected object is **Contact**, the output schema will be shown below.

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

Refer to the Zoho Desk [Documentation](https://desk.zoho.com/support/APIDocument.do#Contacts#Contacts_Updateacontact) for more details on schema.

---
