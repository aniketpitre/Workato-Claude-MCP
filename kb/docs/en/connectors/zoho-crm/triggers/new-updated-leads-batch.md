---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/triggers/new-updated-leads-batch.md
description: >-
  The New/updated leads batch trigger checks for new or updated leads in Zoho
  CRM once every polling interval.
---

# Zoho CRM - New/updated leads trigger (batch)

The **New/updated leads** batch trigger checks for new or updated leads in Zoho CRM once every polling interval.

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
| Leads | The list of leads in the batch. |
| Lead Owner | The user to whom the lead is assigned. |
| Name (Lead Owner) | The name of the lead owner. |
| ID (Lead Owner) | The unique identifier of the lead owner. |
| Email (Lead Owner) | The email address of the lead owner. |
| Company | The name of the company where the lead is working. |
| First Name | The first name of the lead. |
| Last Name | The last name of the lead. |
| Title | The job position of the lead. |
| Email | The email address of the lead. |
| Phone | The phone number of the lead. |
| Fax | The fax number of the lead. |
| Mobile | The mobile number of the lead. |
| Website | The website of the lead. |
| Lead Source | The source from which the lead is generated. |
| Lead Status | The status of the lead. |
| Industry | The industry to which the lead belongs. |
| No. of Employees | The number of employees in the lead's company. |
| Annual Revenue | The annual revenue of the company. |
| Rating | The rating of the lead. |
| Created By | The user who created the lead. |
| Name (Created By) | The name of the user who created the lead. |
| ID (Created By) | The unique identifier of the creator. |
| Email (Created By) | The email address of the creator. |
| Modified By | The user who last modified the lead. |
| Name (Modified By) | The name of the user who last modified the lead. |
| ID (Modified By) | The unique identifier of the modifier. |
| Email (Modified By) | The email address of the modifier. |
| Created Time | The timestamp when the lead was created. |
| Modified Time | The timestamp when the lead was modified. |
| Full Name | The full name of the lead. |
| Street | The street address of the lead. |
| City | The city where the lead lives. |
| State | The state where the lead lives. |
| Zip Code | The postal code of the lead's address. |
| Country | The country of the lead. |
| Description | Additional details about the lead. |
| Skype ID | The Skype ID of the lead. |
| Email Opt Out | Indicates if the lead has opted out of emails. |
| Salutation | The salutation of the lead. |
| Secondary Email | The secondary email address of the lead. |
| Last Activity Time | The timestamp of the last activity on the lead. |
| Twitter | The Twitter handle of the lead. |
| Lead Image | The image associated with the lead record. |
| Converted Date Time | The date and time when the lead was converted. |
| Lead Conversion Time | The time taken to convert the lead. |
| Unsubscribed Mode | The method used to unsubscribe. |
| Unsubscribed Time | The timestamp when the lead unsubscribed. |
| Converted Account | The account created from the converted lead. |
| Name (Converted Account) | The name of the converted account. |
| ID (Converted Account) | The unique identifier of the converted account. |
| Converted Contact | The contact created from the converted lead. |
| Name (Converted Contact) | The name of the converted contact. |
| ID (Converted Contact) | The unique identifier of the converted contact. |
| Converted Deal | The deal created from the converted lead. |
| Name (Converted Deal) | The name of the converted deal. |
| ID (Converted Deal) | The unique identifier of the converted deal. |
| Record Id | The unique identifier of the record. |
| Change Log Time | The timestamp of the last change. |
| Is Converted | Indicates if the lead has been converted. |
| Locked | Indicates if the record is locked. |
| Last Enriched Time | The timestamp when the lead was last enriched. |
| Enrich Status | The enrichment status of the lead. |
| Most Recent Visit | The timestamp of the most recent visit. |
| First Page Visited | The first page visited by the lead. |
| Average Time Spent (Minutes) | The average time spent on the site. |
| Number of Chats | The total number of chats with the lead. |
| Referrer | The referrer source for the lead. |
| Visitor Score | The engagement score of the lead. |
| First Visit | The timestamp of the first visit. |
| Days Visited | The number of days visited. |
| Record Status | The status of the record. |
