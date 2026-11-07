---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/search-vendors-batch.md
description: >-
  The Search vendors batch action returns records that match the given search
  criteria.
---

# Zoho CRM - Search vendors action (batch)

The **Search vendors** batch action returns records that match the given search criteria.

- Search input must be at least 2 characters. Partial matching is used for all fields.
- Search supports up to 5 fields maximum.
- At least one search field is required.

## Input

| Input field | Description |
| --- | --- |
| Vendor name | Enter the name of the vendor to search. |
| Phone | Enter the phone number to search. |
| Email | Enter the email address to search. |
| Website | Enter the website URL to search. |
| GL account | Enter the general ledger account to search. |
| Category | Enter the category to search. |
| Description | Enter description text to search. |

## Output

| Output field | Description |
| --- | --- |
| Vendors | The list of vendors matching the search criteria. |
| Vendor ID (Vendors) | The unique identifier of the vendor. |
| SM owner ID (Vendors) | The ID of the user who owns the vendor. |
| Vendor owner (Vendors) | The user to whom the vendor is assigned. |
| Street (Vendors) | The street address of the vendor. |
| City (Vendors) | The city of the vendor. |
| State (Vendors) | The state or province of the vendor. |
| Country (Vendors) | The country of the vendor. |
| Zip code (Vendors) | The postal code of the vendor. |
| SM creator ID (Vendors) | The ID of the user who created the vendor. |
| Created by (Vendors) | The user who created the vendor. |
| Modified by ID (Vendors) | The ID of the user who last modified the vendor. |
| Modified by (Vendors) | The user who last modified the vendor. |
| Created time (Vendors) | The timestamp when the vendor was created. |
| Modified time (Vendors) | The timestamp when the vendor was modified. |
| Record image (Vendors) | The image associated with the vendor record. |
| Vendor name (Vendors) | The name of the vendor. |
| Phone (Vendors) | The phone number of the vendor. |
| Email (Vendors) | The email address of the vendor. |
| Website (Vendors) | The website URL of the vendor. |
| GL account (Vendors) | The general ledger account. |
| Category (Vendors) | The category of the vendor. |
| Description (Vendors) | Additional details about the vendor. |
| Currency symbol (Vendors) | The currency symbol for monetary values. |
| Process flow (Vendors) | The process flow associated with the vendor. |
| Approved (Vendors) | Indicates if the vendor has been approved. |
| Editable (Vendors) | Indicates if the vendor record is editable. |
| Approval (Vendors) | The approval details for the vendor. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the vendor can be approved. |
| Reject (Approval) | Indicates if the vendor can be rejected. |
| Resubmit (Approval) | Indicates if the vendor can be resubmitted. |
