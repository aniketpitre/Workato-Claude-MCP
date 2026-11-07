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
