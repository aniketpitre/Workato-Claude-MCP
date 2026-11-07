---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/triggers/new-updated-contacts-batch.md
description: >-
  The New/updated contacts batch trigger checks for new or updated contacts in
  Zoho CRM once every polling interval.
---

# Zoho CRM - New/updated contacts trigger (batch)

The **New/updated contacts** batch trigger checks for new or updated contacts in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |
| Batch size | Specify the number of records to be returned in each job. Minimum is 1 and maximum is 200. Defaults to 200. |

## Output

| Output field | Description |
| --- | --- |
| Range | The range of records in the batch. |
| First record ID | The unique identifier of the first record in the batch. |
| Last record ID | The unique identifier of the last record in the batch. |
| Contacts | The list of contacts in the batch. |
| Contact Owner | The user to whom the contact is assigned. |
| Name (Contact Owner) | The name of the contact owner. |
| ID (Contact Owner) | The unique identifier of the contact owner. |
| Email (Contact Owner) | The email address of the contact owner. |
| Lead Source | The source from which the contact is created. |
| First Name | The first name of the contact. |
| Last Name | The last name of the contact. |
| Account Name | The name of the related account. |
| Name (Account Name) | The account name. |
| ID (Account Name) | The unique identifier of the account. |
| Email | The primary email address of the contact. |
| Title | The job position of the contact. |
| Department | The department of the contact. |
| Phone | The office phone number of the contact. |
| Home Phone | The home phone number of the contact. |
| Other Phone | An alternative phone number of the contact. |
| Fax | The fax number of the contact. |
| Mobile | The mobile number of the contact. |
| Date of Birth | The birthday of the contact. |
| Assistant | The name of the contact's assistant. |
| Asst Phone | The phone number of the contact's assistant. |
| Created By | The user who created the contact. |
| Name (Created By) | The name of the user who created the contact. |
| ID (Created By) | The unique identifier of the creator. |
| Email (Created By) | The email address of the creator. |
| Modified By | The user who last modified the contact. |
| Name (Modified By) | The name of the user who last modified the contact. |
| ID (Modified By) | The unique identifier of the modifier. |
| Email (Modified By) | The email address of the modifier. |
| Created Time | The timestamp when the contact was created. |
| Modified Time | The timestamp when the contact was modified. |
| Full Name | The full name of the contact. |
| Mailing Street | The primary street address of the contact. |
| Other Street | An alternative street address of the contact. |
| Mailing City | The primary city of the contact. |
| Other City | An alternative city of the contact. |
| Mailing State | The primary state or province of the contact. |
| Other State | An alternative state or province of the contact. |
| Mailing Zip | The primary postal code of the contact. |
| Other Zip | An alternative postal code of the contact. |
| Mailing Country | The primary country of the contact. |
| Other Country | An alternative country of the contact. |
| Description | Additional details about the contact. |
| Email Opt Out | Indicates if the contact has opted out of emails. |
| Skype ID | The Skype ID of the contact. |
| Salutation | The salutation of the contact. |
| Secondary Email | The secondary email address of the contact. |
| Last Activity Time | The timestamp of the last activity on the contact. |
| Twitter | The Twitter handle of the contact. |
| Contact Image | The image associated with the contact record. |
| Reporting To | The person to whom the contact reports. |
| Name (Reporting To) | The name of the person they report to. |
| ID (Reporting To) | The unique identifier of the person they report to. |
| Unsubscribed Mode | The method used to unsubscribe. |
| Unsubscribed Time | The timestamp when the contact unsubscribed. |
| Record Id | The unique identifier of the record. |
| Change Log Time | The timestamp of the last change. |
| Locked | Indicates if the record is locked. |
| Last Enriched Time | The timestamp when the contact was last enriched. |
| Enrich Status | The enrichment status of the contact. |
| Most Recent Visit | The timestamp of the most recent visit. |
| First Page Visited | The first page visited by the contact. |
| Average Time Spent (Minutes) | The average time spent on the site. |
| Number of Chats | The total number of chats with the contact. |
| Referrer | The referrer source for the contact. |
| Visitor Score | The engagement score of the contact. |
| First Visit | The timestamp of the first visit. |
| Days Visited | The number of days visited. |
| Record Status | The status of the record. |
