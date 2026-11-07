---
url: 'https://docs.workato.com/en/connectors/zoho-crm/triggers/new-updated-case.md'
description: >-
  The New/updated case trigger checks for new or updated cases in Zoho CRM once
  every polling interval.
---

# Zoho CRM - New/updated case trigger

The **New/updated case** trigger checks for new or updated cases in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the case. |
| Case number | The case identification number. |
| Case owner | The user to whom the case is assigned. |
| SM owner ID | The ID of the user who owns the case. |
| Deal name | The name of the related deal. |
| Deal ID | The unique identifier of the related deal. |
| SM creator ID | The ID of the user who created the case. |
| Phone | The phone number of the customer. |
| Email | The email address of the customer. |
| Created by | The user who created the case. |
| Description | Complete details about the case. |
| Internal comments | Follow-up notes about the case. |
| Add comment | Follow-up notes about the solution. |
| Number of comments | The total number of comments on the case. |
| Related to | The name of the contact who submitted the case. |
| Who ID | The unique identifier of the related contact. |
| Subject | The title of the case. |
| Case origin | The source from which the case has been generated. |
| Modified by (ID) | The ID of the user who last modified the case. |
| Modified by | The user who last modified the case. |
| Stage (deprecated) | The deprecated stage field. |
| Solution | The solution provided for the case. |
| Reported by | The name of the person who reported the case. |
| Status | The status of the case. |
| Priority | The priority of the case. |
| Type | The type of problem. |
| Case reason | The reason for the case. |
| Product ID | The unique identifier of the related product. |
| Product name | The name of the related product. |
| Account ID | The unique identifier of the related account. |
| Account name | The name of the related account. |
| Currency symbol | The currency symbol for monetary values. |
| Process flow | The process flow associated with the case. |
| Approved | Indicates if the case has been approved. |
| Editable | Indicates if the case record is editable. |
| Approval | The approval details for the case. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the case can be approved. |
| Reject (Approval) | Indicates if the case can be rejected. |
| Resubmit (Approval) | Indicates if the case can be resubmitted. |
| Created time | The timestamp when the case was created. |
| Modified time | The timestamp when the case was modified. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/triggers/new-updated-contact.md
description: >-
  The New/updated contact trigger checks for new or updated contacts in Zoho CRM
  once every polling interval.
---

# Zoho CRM - New/updated contact trigger

The **New/updated contact** trigger checks for new or updated contacts in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| Contact ID | The unique identifier of the contact. |
| SM owner ID | The ID of the user who owns the contact. |
| Contact owner | The user to whom the contact is assigned. |
| Account ID | The unique identifier of the related account. |
| Vendor ID | The unique identifier of the related vendor. |
| Campaign ID | The unique identifier of the related campaign. |
| Skype ID | The Skype ID of the contact. |
| Email | The primary email address of the contact. |
| Date of birth | The birthday of the contact. |
| Email opt out | Indicates if the contact has opted out of emails. |
| Last activity time | The timestamp of the last activity on the contact. |
| Assistant phone | The phone number of the contact's assistant. |
| Visitor score | The engagement score of the contact. |
| Assistant | The name of the contact's assistant. |
| Other phone | An alternative phone number of the contact. |
| Secondary email | The secondary email address of the contact. |
| Other zip | An alternative postal code of the contact. |
| Other street | An alternative street address of the contact. |
| Other city | An alternative city of the contact. |
| Other state | An alternative state or province of the contact. |
| Other country | An alternative country of the contact. |
| Mailing street | The primary street address of the contact. |
| Mailing city | The primary city of the contact. |
| Mailing state | The primary state or province of the contact. |
| Mailing zip | The primary postal code of the contact. |
| Mailing country | The primary country of the contact. |
| Home phone | The home phone number of the contact. |
| SM creator ID | The ID of the user who created the contact. |
| Created by | The user who created the contact. |
| Modified by ID | The ID of the user who last modified the contact. |
| Modified by | The user who last modified the contact. |
| Add to QuickBooks | Indicates if the contact is added to QuickBooks. |
| Created time | The timestamp when the contact was created. |
| Modified time | The timestamp when the contact was modified. |
| First name | The first name of the contact. |
| Last name | The last name of the contact. |
| Account name | The name of the related account. |
| Title | The job position of the contact. |
| Lead source | The source from which the contact is created. |
| Vendor name | The name of the related vendor. |
| Campaign name | The name of the related campaign. |
| Department | The department of the contact. |
| Phone | The office phone number of the contact. |
| Twitter | The Twitter handle of the contact. |
| Description | Additional details about the contact. |
| Fax | The fax number of the contact. |
| Mobile | The mobile number of the contact. |
| Reports to | The person to whom the contact reports. |
| Currency symbol | The currency symbol for monetary values. |
| Process flow | The process flow associated with the contact. |
| Approved | Indicates if the contact has been approved. |
| Editable | Indicates if the contact record is editable. |
| Approval | The approval details for the contact. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the contact can be approved. |
| Reject (Approval) | Indicates if the contact can be rejected. |
| Resubmit (Approval) | Indicates if the contact can be resubmitted. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/triggers/new-updated-custom-object.md
description: >-
  The New/updated custom object trigger checks for new or updated custom objects
  in Zoho CRM once every polling interval.
---

# Zoho CRM - New/updated custom object trigger

The **New/updated custom object** trigger checks for new or updated custom objects in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| Module name | Select the custom module to monitor for new or updated objects. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

Output fields are dynamically generated based on the selected module.

---
