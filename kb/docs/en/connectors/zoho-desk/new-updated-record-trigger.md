---
url: 'https://docs.workato.com/en/connectors/zoho-desk/new-updated-record-trigger.md'
description: This trigger runs the recipe when there is a new/updated record in Zoho Desk.
---

# Zoho Desk - New/updated record trigger

The **New/updated record** trigger runs the recipe when there is a new/updated record in Zoho Desk.

## Input

| Input field | Description |
| --- | --- |
| Object | Enter the object to retrieve the details of a record. Fields load dynamically based on the object you select. |
| Trigger poll interval | Select the frequency at which trigger checks for new events, from the drop-down menu. Defaults to minutes if left blank. The minimum value allowed is 5 minutes. [Learn more](/en/recipes/polling-intervals) |
| When first started, this recipe should pick up events from | Select the date and time from the calendar. When you start a recipe for the first time, it picks up events from this specified date and time. It was processed 1 hour ago if left blank. Once a recipe has been run or tested, the value cannot be changed. |
| Set trigger condition | Define further guidelines added to a specific trigger that filter what type of trigger events should be selected for processing. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

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

Refer to the Zoho Desk [Documentation](https://desk.zoho.com/support/APIDocument.do#Search#Search_SearchContacts) for more details on schema.

---
