---
url: 'https://docs.workato.com/en/connectors/xero/add-person-contact.md'
description: >-
  The Add person(s) to contact action in the Xero connector lets you add up to
  five individuals to a contact record, appending or replacing the list.
---

# Xero - Add person(s) to contact action

The **Add person(s) to contact** action allows you to add up to five individuals to a contact's record in Xero. You can either append these new entries to the existing list or replace the current list with the new one.

![Search items action](/assets/add-person-contact.DHHA7Qcz.png)_Xero - Add person(s) to contact action_

## Input

| Input field | Description |
| --- | --- |
| Contact ID | Input the unique identifier (ID) of the Xero contact you plan to add persons to. |
| Replace all | Select `Yes` to replace the existing list of contact persons with new entries or `No` to add to the current list. |
| Contact persons source list | Provide a list datapill containing the details of the contact persons. [Learn more about list input](/en/features/list-management#list-batch-action). |
| First name | Enter the first name of each contact person. |
| Last name | Enter the last name of each contact person. |
| Email address | Provide the email address of each contact person. |
| Include in emails | Specify whether to include a specific contact's email address in the email distribution when sending invoices, receipts, or other documents through the Xero platform. Select `Yes` to include or `No` to exclude. |

## Output

| Output field | Description |
| --- | --- |
| Contact ID | The unique identifier for the contact within Xero. |
| Contact number | The contact number assigned in Xero. |
| Contact status | The status of the contact. |
| Account number | The account number associated with the contact. |
| Contact name | The full name of the contact. |
| First name | The first name of the contact. |
| Last name | The last name of the contact. |
| Email address | The email address of the contact. |
| Skype user name | The Skype username associated with the contact. |
| Is supplier | Indicates if the contact is marked as a supplier. |
| Is customer | Indicates if the contact is marked as a customer. |
| Updated date | The date when the contact's information was last updated. |
| Bank account number | The bank account number related to the contact. |
| Tax number | The tax identification number for the contact. |
| Accounts receivable tax type | The tax type used for the contact's accounts receivable. |
| Accounts payable tax type | The tax type used for the contact's accounts payable. |
| Street address | The street address details for the contact. |
| Postal address | The postal address details for the contact. |
| Default phone details | The default phone information for the contact. |
| DDI phone details | Direct dial-in phone information for the contact. |
| Mobile phone details | The contact's mobile phone information. |
| Fax phone details | Fax phone information for the contact. |
| Batch payments | Details for batch payments associated with the contact. |
| Website | The URL of the contact's website. |
| Default currency | The default currency for transactions with the contact. See [ISO 4217 Currency Codes](http://www.xe.com/iso4217.php) for more information. |
| Balances | A summary of the financial balances associated with the contact. |
| Xero network key | The contact's Xero network key, used for secure transactions. |
| Sales default account code | The default account code for sales transactions. |
| Purchases default account code | The default account code for purchase transactions. |
| Payment terms | Payment terms set for the contact. |

---
