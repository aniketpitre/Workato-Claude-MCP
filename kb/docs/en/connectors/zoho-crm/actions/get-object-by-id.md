---
url: 'https://docs.workato.com/en/connectors/zoho-crm/actions/get-object-by-id.md'
description: >-
  The Get object by ID action retrieves the details about an object using its
  ID.
---

# Zoho CRM - Get object by ID action

The **Get object by ID** action retrieves the details about an object using its ID.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type. |
| Object ID | Enter the unique identifier of the object. |

## Output

Output fields are dynamically generated based on the selected object.

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/relate-member-to-campaign.md
description: >-
  The Relate a member to a campaign action relates a lead or contact to a
  campaign in Zoho CRM.
---

# Zoho CRM - Relate a member to a campaign action

The **Relate a member to a campaign** action relates a lead or contact to a campaign in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Member ID | Enter the lead or contact ID. The action does nothing if the member is already a campaign member. |
| Campaign ID | Enter the unique identifier of the campaign. |
| Member type | Specify the type of member: `Leads` or `Contacts`. |
| Member status | Specify the status of the member in the campaign. |

## Output

| Output field | Description |
| --- | --- |
| Added member IDs | The list of member IDs that were added. |
| Updated member IDs | The list of member IDs that were updated. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/search-accounts-batch.md
description: >-
  The Search accounts batch action returns records that match the given search
  criteria.
---

# Zoho CRM - Search accounts action (batch)

The **Search accounts** batch action returns records that match the given search criteria.

- Search input must be at least 2 characters. Partial matching is used for all fields.
- Search supports up to 5 fields maximum.
- At least one search field is required.

## Input

| Input field | Description |
| --- | --- |
| Account name | Enter the company name to search. |
| Account number | Enter the reference number for the account. |
| Ownership | Enter the type of ownership to search. |
| Account type | Enter the type of account to search. |
| Rating | Enter the rating to search. |
| Phone | Enter the phone number to search. |
| Account site | Enter the account location name to search. |
| Fax | Enter the fax number to search. |
| Ticker symbol | Enter the ticker symbol to search. |
| Website | Enter the website URL to search. |
| Description | Enter description text to search. |

## Output

| Output field | Description |
| --- | --- |
| Accounts | The list of accounts matching the search criteria. |
| Account ID (Accounts) | The unique identifier of the account. |
| SM owner ID (Accounts) | The ID of the user who owns the account. |
| Account owner (Accounts) | The user to whom the account is assigned. |
| Parent ID (Accounts) | The unique identifier of the parent account. |
| Account name (Accounts) | The company name. |
| Parent account (Accounts) | The parent company name. |
| Employees (Accounts) | The number of employees in the account's company. |
| Industry (Accounts) | The type of industry of the company. |
| SM creator ID (Accounts) | The ID of the user who created the account. |
| Created by (Accounts) | The user who created the account. |
| Modified by ID (Accounts) | The ID of the user who last modified the account. |
| Modified by (Accounts) | The user who last modified the account. |
| Billing street (Accounts) | The billing street address. |
| Billing city (Accounts) | The billing city. |
| Billing state (Accounts) | The billing state or province. |
| Billing code (Accounts) | The billing postal code. |
| Billing country (Accounts) | The billing country. |
| Shipping street (Accounts) | The shipping street address. |
| Shipping state (Accounts) | The shipping state or province. |
| Shipping code (Accounts) | The shipping postal code. |
| Shipping country (Accounts) | The shipping country. |
| Created time (Accounts) | The timestamp when the account was created. |
| Modified time (Accounts) | The timestamp when the account was modified. |
| SIC code (Accounts) | The Standard Industrial Classification (SIC) code. |
| Annual revenue (Accounts) | The annual revenue of the account. |
| Last activity time (Accounts) | The timestamp of the last activity on the account. |
| Account number (Accounts) | The reference number for the account. |
| Ownership (Accounts) | The type of ownership of the company. |
| Account type (Accounts) | The type of account. |
| Rating (Accounts) | The rating of the account. |
| Phone (Accounts) | The phone number of the account. |
| Account site (Accounts) | The name of the account's location. |
| Fax (Accounts) | The fax number of the account. |
| Ticker symbol (Accounts) | The ticker symbol of the company. |
| Website (Accounts) | The URL of the company's website. |
| Description (Accounts) | Additional details about the account. |
| Currency symbol (Accounts) | The currency symbol for monetary values. |
| Process flow (Accounts) | The process flow associated with the account. |
| Approved (Accounts) | Indicates if the account has been approved. |
| Editable (Accounts) | Indicates if the account record is editable. |
| Approval (Accounts) | The approval details for the account. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the account can be approved. |
| Reject (Approval) | Indicates if the account can be rejected. |
| Resubmit (Approval) | Indicates if the account can be resubmitted. |
| Associated contacts (Accounts) | The contacts associated with this account. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/search-campaigns-batch.md
description: >-
  The Search campaigns batch action returns records that match the given search
  criteria.
---

# Zoho CRM - Search campaigns action (batch)

The **Search campaigns** batch action returns records that match the given search criteria.

- Search input must be at least 2 characters. Partial matching is used for all fields.
- Search supports up to 5 fields maximum.
- At least one search field is required.

## Input

| Input field | Description |
| --- | --- |
| Campaign name | Enter the name of the campaign to search. |

## Output

| Output field | Description |
| --- | --- |
| Campaigns | The list of campaigns matching the search criteria. |
| Campaign owner (Campaigns) | The user to whom the campaign is assigned. |
| Campaign ID (Campaigns) | The unique identifier of the campaign. |
| Campaign name (Campaigns) | The name of the campaign. |
| Type (Campaigns) | The type of the campaign. |
| Status (Campaigns) | The status of the campaign. |
| Start date (Campaigns) | The date on which the campaign starts. |
| End date (Campaigns) | The date on which the campaign ends. |
| Expected revenue (Campaigns) | The revenue expected after launching the campaign. |
| Actual cost (Campaigns) | The actual amount spent on the campaign. |
| Budgeted cost (Campaigns) | The planned amount to be spent on the campaign. |
| Expected response (Campaigns) | The campaign turnout percentage. |
| Number sent (Campaigns) | The number of leads or contacts who received details. |
| Description (Campaigns) | Additional details about the campaign. |
| Currency symbol (Campaigns) | The currency symbol for monetary values. |
| Process flow (Campaigns) | The process flow associated with the campaign. |
| Approved (Campaigns) | Indicates if the campaign has been approved. |
| Editable (Campaigns) | Indicates if the campaign record is editable. |
| Approval (Campaigns) | The approval details for the campaign. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the campaign can be approved. |
| Reject (Approval) | Indicates if the campaign can be rejected. |
| Resubmit (Approval) | Indicates if the campaign can be resubmitted. |
| SM owner ID (Campaigns) | The ID of the user who owns the campaign. |
| SM creator ID (Campaigns) | The ID of the user who created the campaign. |
| Created by (Campaigns) | The user who created the campaign. |
| Modified by (ID) (Campaigns) | The ID of the user who last modified the campaign. |
| Modified by (Campaigns) | The user who last modified the campaign. |
| Created time (Campaigns) | The timestamp when the campaign was created. |
| Modified time (Campaigns) | The timestamp when the campaign was modified. |
| Survey Department (Campaigns) | The department responsible for the survey. |
| Survey Type (Campaigns) | The type of survey associated with the campaign. |
| Survey (Campaigns) | The survey name or identifier. |
| Survey URL (Campaigns) | The URL for the survey. |
| Department ID (Campaigns) | The unique identifier for the department. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/search-custom-objects.md
description: >-
  The Search custom objects action returns records that match the given search
  criteria.
---

# Zoho CRM - Search custom objects action

The **Search custom objects** action returns records that match the given search criteria.

- Search input must be at least 2 characters. Partial matching is used for all fields.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the custom module to search within. |
| Operand | Enter the value to search for. |
| Operator | Select the comparison operator for the search. |
| Search by | Select the field to search by. |

Additional fields appear based on the module you select.

## Output

Output fields are dynamically generated based on the selected module.

---
