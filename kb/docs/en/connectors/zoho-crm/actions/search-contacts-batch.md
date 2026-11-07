---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/search-contacts-batch.md
description: >-
  The Search contacts batch action returns records that match the given search
  criteria.
---

# Zoho CRM - Search contacts action (batch)

The **Search contacts** batch action returns records that match the given search criteria.

- Search input must be at least 2 characters. Partial matching is used for all fields.
- Search supports up to 5 fields maximum.
- At least one search field is required.

## Input

| Input field | Description |
| --- | --- |
| Contact email | Enter the email address to search. |
| First name | Enter the first name to search. |
| Last name | Enter the last name to search. |
| Account name | Enter the account name to search. |
| Title | Enter the job position to search. |
| Lead source | Enter the lead source to search. |
| Vendor name | Enter the vendor name to search. |
| Campaign name | Enter the campaign name to search. |
| Department | Enter the department to search. |
| Phone | Enter the phone number to search. |
| Twitter | Enter the Twitter handle to search. |
| Description | Enter description text to search. |
| Fax | Enter the fax number to search. |
| Mobile | Enter the mobile number to search. |
| Reports to | Enter the name of the person the contact reports to. |

## Output

| Output field | Description |
| --- | --- |
| Contacts | The list of contacts matching the search criteria. |
| Contact ID (Contacts) | The unique identifier of the contact. |
| SM owner ID (Contacts) | The ID of the user who owns the contact. |
| Contact owner (Contacts) | The user to whom the contact is assigned. |
| Account ID (Contacts) | The unique identifier of the related account. |
| Vendor ID (Contacts) | The unique identifier of the related vendor. |
| Campaign ID (Contacts) | The unique identifier of the related campaign. |
| Skype ID (Contacts) | The Skype ID of the contact. |
| Email (Contacts) | The primary email address of the contact. |
| Date of birth (Contacts) | The birthday of the contact. |
| Email opt out (Contacts) | Indicates if the contact has opted out of emails. |
| Last activity time (Contacts) | The timestamp of the last activity on the contact. |
| Assistant phone (Contacts) | The phone number of the contact's assistant. |
| Visitor score (Contacts) | The engagement score of the contact. |
| Assistant (Contacts) | The name of the contact's assistant. |
| Other phone (Contacts) | An alternative phone number of the contact. |
| Secondary email (Contacts) | The secondary email address of the contact. |
| Other zip (Contacts) | An alternative postal code of the contact. |
| Other street (Contacts) | An alternative street address of the contact. |
| Other city (Contacts) | An alternative city of the contact. |
| Other state (Contacts) | An alternative state or province of the contact. |
| Other country (Contacts) | An alternative country of the contact. |
| Mailing street (Contacts) | The primary street address of the contact. |
| Mailing city (Contacts) | The primary city of the contact. |
| Mailing state (Contacts) | The primary state or province of the contact. |
| Mailing zip (Contacts) | The primary postal code of the contact. |
| Mailing country (Contacts) | The primary country of the contact. |
| Home phone (Contacts) | The home phone number of the contact. |
| SM creator ID (Contacts) | The ID of the user who created the contact. |
| Created by (Contacts) | The user who created the contact. |
| Modified by ID (Contacts) | The ID of the user who last modified the contact. |
| Modified by (Contacts) | The user who last modified the contact. |
| Add to QuickBooks (Contacts) | Indicates if the contact is added to QuickBooks. |
| Created time (Contacts) | The timestamp when the contact was created. |
| Modified time (Contacts) | The timestamp when the contact was modified. |
| First name (Contacts) | The first name of the contact. |
| Last name (Contacts) | The last name of the contact. |
| Account name (Contacts) | The name of the related account. |
| Title (Contacts) | The job position of the contact. |
| Lead source (Contacts) | The source from which the contact is created. |
| Vendor name (Contacts) | The name of the related vendor. |
| Campaign name (Contacts) | The name of the related campaign. |
| Department (Contacts) | The department of the contact. |
| Phone (Contacts) | The office phone number of the contact. |
| Twitter (Contacts) | The Twitter handle of the contact. |
| Description (Contacts) | Additional details about the contact. |
| Fax (Contacts) | The fax number of the contact. |
| Mobile (Contacts) | The mobile number of the contact. |
| Reports to (Contacts) | The person to whom the contact reports. |
| Currency symbol (Contacts) | The currency symbol for monetary values. |
| Process flow (Contacts) | The process flow associated with the contact. |
| Approved (Contacts) | Indicates if the contact has been approved. |
| Editable (Contacts) | Indicates if the contact record is editable. |
| Approval (Contacts) | The approval details for the contact. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the contact can be approved. |
| Reject (Approval) | Indicates if the contact can be rejected. |
| Resubmit (Approval) | Indicates if the contact can be resubmitted. |
