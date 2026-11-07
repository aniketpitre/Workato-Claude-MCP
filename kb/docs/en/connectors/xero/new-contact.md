---
url: 'https://docs.workato.com/en/connectors/xero/new-contact.md'
description: >-
  The New/updated contact trigger in the Xero connector fires when a contact is
  created or updated in your connected Xero organization.
---

# Xero - New/updated contact trigger

The **New/updated contact** trigger activates when a contact is created or updated.

![New/updated contact trigger](/assets/update-contact-trigger.rAew1mY8.png)_Xero - New/updated contact trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |
| Contact filter | Select to filter for customers or suppliers. |

## Output

| Output field | Description |
| --- | --- |
| Contact ID | The unique identifier for the contact within Xero. |
| Contact number | A unique number that identifies the contact, as assigned within Xero. |
| Contact status | The status of the contact. |
| Account number | The account number associated with the contact. |
| Contact name | The full name of the contact. |
| First name | The contact's first name. |
| Last name | The contact's last name. |
| Email address | The primary email address of the contact. |
| Skype user name | The Skype username linked to the contact. |
| Is supplier | Indicator if the contact is a supplier. |
| Is customer | Indicator if the contact is a customer. |
| Updated date | The date when the contact was last updated. |
| Bank account number | The bank account number related to the contact. |
| Tax number | The tax number associated with the contact. |
| Accounts receivable tax type | The default tax type for the contact's accounts receivable. |
| Accounts payable tax type | The default tax type for the contact's accounts payable. |
| Street address | Details about the street address. |
| Postal address | Details about the postal address. |
| Default phone details | The default phone details. |
| DDI phone details | The DDI phone details. |
| Mobile phone details | The mobile phone details. |
| Fax phone details | The fax phone details. |
| Batch payments | The batch payments details. |
| Contact persons | The contact persons details. |
| Website | The URL of the contact's website. |
| Default currency | The currency that the contact uses by default. |
| Balances | The balances related to the contact. |
| Xero network key | The unique key for the contact's Xero network. |
| Sales default account code | The default account code used for sales to this contact. |
| Purchases default account code | The default account code used for purchases from this contact. |
| Payment terms | The payment terms for the contact. |

---
