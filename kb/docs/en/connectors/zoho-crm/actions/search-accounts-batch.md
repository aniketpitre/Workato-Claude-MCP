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
