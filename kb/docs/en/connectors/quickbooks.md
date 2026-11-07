---
url: 'https://docs.workato.com/en/connectors/quickbooks.md'
description: >-
  The QuickBooks Online connector lets you automate accounting: create, update,
  and search invoices, bills, payments, and customers, and trigger on new
  records.
---

# QuickBooks Online

[QuickBooks Online](https://quickbooks.intuit.com/) is an easy-to-use accounting software package that enables businesses to manage business payments, bills, and payroll functions.

## API version

As of August 1, 2025, the QuickBooks Online connector uses the [QuickBooks Online Accounting API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account) version 75. This is the only supported version as QuickBooks no longer supports earlier versions.

## Supported editions and versions

The QuickBooks connector works with all QuickBooks Online versions, including:

- QuickBooks Self-Employed
- QuickBooks Simple Start
- QuickBooks Essentials
- QuickBooks Plus

However, Workato currently doesn't support QuickBooks Desktop/Enterprise versions.

## How to connect to QuickBooks on Workato

Complete the following steps to establish a connection to QuickBooks Online in Workato:

1. Provide a **Connection name** that identifies which QuickBooks instance Workato is connected to.
   
   ![QuickBooks online connection](/assets/QBO_connect1.D_Fk-JGJ.png)_QuickBooks online connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Sandbox** drop-down menu to specify whether the QuickBooks Online account is a sandbox account.
   
4. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
5. Click **Connect to QuickBooks** to open the QuickBooks sign in window.
   
   ![Connect to QuickBooks Online](/assets/QBO_connect2.DOeG2fRE.png)_Connect to QuickBooks Online_
   
6. Enter your QuickBooks Online account email address and password.
   
7. Click **Sign in** to complete the connection.
   

## QuickBooks triggers

The following triggers are currently available for the QuickBooks connector:

**NEW:** Account, Bank Deposit, Bill Payment, Credit Note, Customer, Employee, Estimate, Invoice, Item, Payment, Sales Receipt, Vendor

**NEW/UPDATED:** Account, Tax Code, Tax Rate

**UPDATED:** Bill, Credit Note, Customer, Employee, Estimate, Invoice, Item, Purchase, Vendor

**DELETED:** Item

## QuickBooks actions

### Deprecated actions

Some actions in this connector are deprecated. The recipe editor marks these actions with a `Deprecated` tag and prevents their use in new steps.

> **DEPRECATED ACTIONS ARE UNSUPPORTED**
> 
> Deprecated QuickBooks actions don't receive updates, fixes, or support from Workato and should be replaced.

Replacements for deprecated actions

Replace deprecated actions with the following supported actions, even if their names match:

| Deprecated action | Supported action |
| --- | --- |
| Add line to bill | Update bill |
| Add line to purchase | Update expense |
| Add line to purchase order | Update purchase order |
| Create bank deposit | Create bank deposit |
| Create bill with 1 line item | Create bill |
| Create bill with line items | Create bill |
| Create credit memo | Create credit memo |
| Create estimate with 1 line item | Create estimate |
| Create invoice with 1 line item | Create invoice |
| Create invoice with line items | Create invoice |
| Create payment with 1 line item | Create payment |
| Create purchase with 1 line item | Create expense |
| Create purchase order | Create purchase order |
| Create sales receipt with 1 line item | Create sales receipt |
| Create sales receipt with line items | Create sales receipt |
| Search customers | Search customers |
| Update bank deposit and line items | Update a bank deposit |
| Update bill and line items | Update bill |
| Update estimate header details | Update estimate |
| Update invoice header details | Update invoice |
| Update invoice and line items | Update invoice |
| Update sales receipt header details | Update sales receipt |
| Update sales receipt and lines items | Update sales receipt |

### Add Line to Invoice

#### Sales Item Detail vs. Discount Line Detail vs. Description only

##### Sales Item Detail

As the name suggests, user is required to key in some details regarding the sales item. This includes Item ID, Total Amount, Unit Price/Quantity and also the Description.

##### Discount Line Detail

##### Description Only

When user wants to include only the description of the items, choose this option. As such, "Description only" is a subset of "Sales Item Detail", if the user wants to include more details in the invoice, choose "Sales Item Detail".

#### Difference between Create with 1 line item and Create with Line items

##### Creating Transactional Objects with line items

Workato QuickBooks actions for creating Transactional objects (Invoice, Sales receipt, Bill, Credit Memo, etc) generally has two ways for populating them:

1. Creating first an invoice with a single line item (as mandatory by QuickBooks Online to have at least one line item), and use Add Line Item to X action for any further addition

or

2. Creating an invoice with line items. The line items detail will be pulled dynamically from a list datapill. You can learn more about it here.

**When do I use 'Create with 1 line item'?**

Creating a single invoice with only line items are great for Single sync ups, where details of the transactional items are minimal. Example of this is creating an invoice for an opportunity, or creating a Sales Receipt for donations. Subsequently, adding on line items to an invoice can be done in another recipe when new items are added for an existing invoice, giving you the flexibility of structuring your invoices.

In all other cases, you should use 'Create with line items' and simply place the list of items where required.

![QBO multiline](/assets/QBO_multiline.BClRRAf8.png)

A 'list' type datapill is marked with the list logo as can be seen above in red.

### Bank Deposit

Workato has several QuickBooks actions that are related to a Bank Deposit object:

- Create bank deposits
- Search bank deposits
- Update bank deposits

The available fields for a Bank Deposits are:

- Txn Date
  
  - Date of the transaction object
- Total amount
  
  - The total amount that the bank deposit should amount to. Note that this value cannot be negative.
- Cash back
  
  - Specify an account that should return a certain amount back to for this deposit
    - Account
    - Amount
    - Memo
- Deposit To Account Reference
  
  - Specify an account that this bank deposit should be targeted to. Note that you cannot specify Undeposited Funds as the Deposit To Account here.
  - Account
    - Account specified here must be of Bank or Other Current Asset Account type.
- Transaction tax detail
  
  - Tax Code
  - Total Tax
- Line
  
  - Line Source list
    - Specify a line item object here where data will be accessed from. The total number of line item created will equals to the size of the source list. To learn more about source list, see here
  - Description
    - For each of the line item, specify its Description
  - Amount
    - For each of the line items, specify its Amount
- Linked Transaction
  
  - If there are existing transactions that needs to be related, specify details here to record a deposit for an existing transaction.
  - Linked transaction source list
    - Specify a line item object here where data will be accessed from. The total number of line item created will equals to the size of the source list. To learn more about source list, see here
  - Transaction ID
  - Transaction Type
    - Possible types of transactions that can be linked to a Deposit include: `Transfer`, `Payment` (for Cash, CreditCard, and Check payment method types), `SalesReceipt`,`RefundReceipt`, `JournalEntry`.
  - Transaction Line ID
- Deposit Line Detail
  
  - Entity Name
    - Reference to a customer Display Name from which deposit was received
  - Type
    - Specify if it is a Customer or Vendor
  - Value
    - Reference to a customer ID from which deposit was received
- Class reference
  
  - Reference to the Class associated with the transaction
- Account Reference
  
  - Account where the funds are deposited
- Payment method reference
  
  - Payment method
- Check num
  
  - Check number for the deposit.
- Tax reference
  
  - Tax code
    - Sales/Purchase tax code associated with the Line. For Non US Companies only
  - Tax applicable on
- Private Note
  
- Currency Reference
  
  - Value
  - Name
- Transaction source
  
  - A field used internally to specify originating source of a credit card transaction.

### Exchange Rate

QuickBooks Online provides international trades to be done in multiple currencies. Workato adapts your business needs and supports all necessary changes needed to automate your business.

QuickBooks Online allows you to support multiple currencies. To do so, you may enable it in your Accounts and Settings section. Do note that enabling multiple currency may incur setting changes. Please consult your QuickBooks Online support.

![QBO currency](/assets/QBO_currency.DJTeVulc.png)

Exchange Rate field allows you to specify the exchange rate to your home currency from the specified currency. If no Currency is specified, the exchange rate will be defaulted to 1 in respect of the home currency.

For dependent transaction documents such as credit memo, the applied currency will depends on its parent transactions document, such as payment, or bank deposit.

An Example:

![QBO currency2](/assets/QBO_currency2.CjOmkesu.png)

The preceding example sets the exchange rate at `1.5239475`, meaning `1` unit of the home currency equals `1.5239475` units of the foreign currency.

## Different labels between profit and non-profit versions

If you are using the non-profit version of QuickBooks, do note that on Workato, certain terms may be labeled differently from what appears in your QuickBooks account. Refer to the table below to know which triggers and actions to use:

| For Profit | Non-Profit |
| --- | --- |
| Invoice | Pledge |
| Sales Receipt | Donations (Sales) |
| Expenses | Expenditure |
| Profit & Loss | Statement of Activity |
| Balance Sheet | Statement of Financial Positions |

For more information on non-profit organization in QuickBooks, refer to the [Learn QuickBooks Online terminology](https://quickbooks.intuit.com/learn-support/en-us/help-custom/L9tYm1JhO) article.

---

---
url: >-
  https://docs.workato.com/en/connectors/quickbooks/quickbooks-troubleshooting-runtime.md
description: >-
  Use this guide to troubleshoot errors that occur at runtime when you use the
  QuickBooks Online connector in Workato.
---

# Troubleshoot QuickBooks Online runtime errors

Use this guide to troubleshoot errors that occur at runtime when you use the QuickBooks Online connector in Workato.

## Create invoice not assigning invoice numbers

You may encounter an error where invoices created in Workato don't receive an invoice number. However, if you create an invoice manually in QuickBooks, the invoice number is assigned correctly. This issue occurs when **Customer Transaction** is enabled on the connected QuickBooks instance.

To resolve this issue in QuickBooks Online:

1. Go to **Settings > Account and Settings > Sales > Sales form content > Customer Transaction** in QuickBooks Online.
   
2. Click to turn **Customer Transaction** off. When off, QuickBooks assigns the invoice number on the next invoice created through the API.
   

## `Duplicate Name Exists Error` when creating a record

![QBO error2](/assets/QBO_error2.CTuZaAsz.png)

In QuickBooks, display names are used as unique identifiers for Customers (also known as Donors or Tenants), Employees, and Vendors.

As such, trying to create a record with the same display name as an existing Customer, Employee, or Vendor causes the following error: `Another tenant, vendor, or employee is already using this name. Please use a different name.`

![QBO error1](/assets/QBO_error1.BS6iIu0_.png)

To resolve this, add a prefix or suffix to the display name of the Customer, Employee, or Vendor.

![QBO error3](/assets/QBO_error3.DeHdOlfc.png)

Note that QuickBooks does not allow for certain special characters in the display name, including colon (:).

The following characters are accepted:

- Alpha-numeric (A-Z, a-z, 0-9)
- Comma (,)
- Dot or period (.)
- Question mark (?)
- At symbol (@)
- Ampersand (&)
- Exclamation point (!)
- Number/pound sign (#)
- Single quote (')
- Tilde (~)
- Asterisk (\*)
- Space ( )
- Underscore (\_)
- Minus sign/hyphen (-)
- Semi-colon (;)
- Plus sign (+)
- Brackets (())

## Account period closed, cannot update through API

You may encounter the `Error 6210: Account period closed, cannot update through API` error when a QuickBooks closing date prevents you from creating or updating transactions. To resolve this, remove the closed date in QuickBooks Online.

## `Malformed website address format` error

`QuickBooks fault: {"Error"=>[{"Message"=>"Malformed Web Site Address format", "Detail"=>"Web Site URL does not have correct format. Supplied value:example.com", "code"=>"2200", "element"=>"WebAddr"}], "type"=>"ValidationFault"}`

You may encounter this error when you are trying to create a record in QuickBooks Online and you have mapped a field that requires a website address. The QuickBooks API requires a well-formed web address in the form `http://example.com`. To resolve this, ensure your recipe starts with `http://` or `https://`.

---

---
url: >-
  https://docs.workato.com/en/connectors/quickbooks/quickbooks-troubleshooting-connection.md
description: >-
  Use this guide to troubleshoot errors that occur while creating a QuickBooks
  Online connection in Workato.
---

# Troubleshoot QuickBooks Online connection errors

Use this guide to troubleshoot errors that occur while creating a QuickBooks Online connection in Workato.

## `app_already_purchased` error while creating a connection

![QBO purchased](/assets/QBO_purchased.GW_BjjXm.png)

You may receive the `app_already_purchased` error when creating a QuickBooks Online connection if someone else is already connected to Workato using the company account you provided. QuickBooks only allows one active connection to Workato per company account. Contact the user listed in the error message to delete their Workato connection or use a different company account to resolve this error.

## `Object Not Found` error while accessing QuickBooks API

![QBO errorobjnotfound](/assets/QBO_errorobjnotfound.CZ8rmYNi.png)

You may receive the `Object Not Found` error when you try to get a QuickBooks object based on an ID that doesn't exist.

![QBO errorobjnotfound3](/assets/QBO_errorobjnotfound3.eKNUNNKq.png)

For example, in the preceding image, the recipe tries to get an item from QuickBooks based on its ID. Unfortunately, the object does not exist in the QuickBooks account.

You can find the object's ID in its QuickBooks Online URL. For example, in the following image, `ID=6` shows that 6 is the object's ID.

![QBO errorobjnotfound2](/assets/QBO_errorobjnotfound2.DG3-M8tc.png)

To resolve the issue using a fixed value, find the correct ID using the QuickBooks Online URL, then rerun the job. To resolve the issue using a datapill, ensure your recipe provides the action with the correct IDs, then rerun the job.

## `784:unexpected token` QuickBooks API server not responding

![QBO APIerror](/assets/QBO_APIerror.3DX9zF3v.png)

You may receive the `784:unexpected token` error when the QuickBooks API experiences an outage or other intermittent issues. To resolve the issue, monitor [Intuit's Status page](http://status.developer.intuit.com) and re-run the job when the API is operational.

## `403 forbidden` error

You may receive the `403 forbidden` error when there are connectivity issues with the QuickBooks Online app. To resolve the issue, go to your recipe's **Connections** tab, then **Disconnect** and reconnect to the app.

![QBO connect3](/assets/QBO_connect3.BM-_JzRu.png)

---
