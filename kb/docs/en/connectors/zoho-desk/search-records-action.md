---
url: 'https://docs.workato.com/en/connectors/zoho-desk/search-records-action.md'
description: >-
  The Search records action enables you to retrieve a list of records that match
  your search criteria in Zoho Desk.
---

# Zoho Desk - Search records action

The **Search records** action enables you to retrieve a list of records that match your search criteria in Zoho Desk.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create the record. Fields load dynamically based on the object you select. |

For example, if the selected object is **Contact**, the input schema will be below.

| Input fields | Description |
| --- | --- |
| Contact ID | Enter the ID of the contact. |
| Full name | Provide the full name of the contact. |
| First name | Provide the first name of the contact. |
| Last name | Provide the last name of the contact. |
| Email | Enter the Email ID of the contact. |
| Account name | Provide the account name to which the contact is linked. |
| Phone | Provide the phone number of the contact. |
| Mobile | Enter the mobile number of the contact. |
| Offset | Provide the index number, starting from which the records must be fetched. |
| Limit | Provide the number of records to fetch. The default is 10. |
| Search string | Specify the search string to search throughout the contact. |
| From | Provide the **From** time, which will be used to search for contacts based on their creation timestamp. |
| To | Provide the **To** time, which will be used to search for contacts based on their creation timestamp. |
| From | Provide the **From** time, which will be used to search for contacts based on their last modified timestamp. |
| To | Provide the **To** time, which will be used to search for contacts based on their last modified timestamp. |
| Sort by | Select the suitable attribute to sort the result set. |
| Custom fields | Provide the value to search records by user-defined fields. Use the format: `CustomFieldName:Value`. For example - `cf_phone:902*`. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

For example, if the selected object is **Contact**, the output schema will be shown below.

| Output field | Description |
| --- | --- |
| Contacts | The main object that contains the records. |
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

Refer to the Zoho Desk [Documentation](https://desk.zoho.com/support/APIDocument.do#Search#Search_SearchContacts) for more information.

---
