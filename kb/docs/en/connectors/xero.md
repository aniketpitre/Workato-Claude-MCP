---
url: 'https://docs.workato.com/en/connectors/xero.md'
description: >-
  The Xero connector lets you automate accounting workflows: create, update, and
  search invoices, contacts, and payments, and trigger on new or updated
  records.
---

# Xero

[Xero](https://www.xero.com/us/) is a cloud-based accounting software designed for small- to medium-sized businesses. You can use Xero to manage invoicing, bank reconciliation, and bookkeeping.

Workato enables you to synchronize data between Xero and other apps within your organization. For example, you can sync Xero contact data into your CRM app as customer data, Xero sales data into your point-of-sales app, or Xero inventory data into your ERP app.

## API version

The Xero connector uses the [Xero Accounting API](https://developer.xero.com/documentation/api/api-overview). Review the Xero Accounting API documentation to fully understand the integration possibilities with Workato recipes.

## How to connect to Xero in Workato

Complete the following steps to connect to Xero in Workato:

1. Enter a unique **Connection name** to identify the Xero instance you plan to connect with Workato.
   
2. Select `Yes` if your Xero account is enabled for **Payroll**. Payroll connectivity is available only for AU and US editions.
   
3. Provide the exact **Tenant name** for the connection. This field is case-sensitive.
   
4. Specify the required **Decimal precision** for line item calculations. This field defaults to 2 if left blank.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
6. Click **Connect** to sign in to your Xero account and complete the setup process.
   
   ![Xero login](/assets/xero-login.HXP2RUNj.png)_Xero login_
   

How to find different IDs in Xero

Each record in Xero has a unique identifier called a Xero ID. You can obtain these IDs using two primary methods:

### Retrieving IDs directly from Xero

To retrieve an ID, navigate to the specific item's page in Xero and locate the ID at the end of the URL. This method suits scenarios requiring a consistent ID, typically during testing. For example:

![Contact ID](/assets/contact-id-updated.whkZgQcc.png)_**Contact ID** in the contact page URL_

In this instance, the **Contact ID** (`46145141-500e-4a15-b2e1-2752708fdd52`) appears at the end of a contact's page URL in Xero. You can also find other IDs, such as the **Manual journal ID**, at the end of its page URL.

### Using Workato actions to obtain IDs

You can also use Workato actions such as **Search**, **Create**, or **Update** to obtain Xero IDs. When Workato interacts with a Xero record, it retrieves the record's ID in the API response. The following examples demonstrate this method:

- Contact ID
  
- Obtain the unique identifier for each contact in Xero using triggers and actions such as [New/updated contact](/en/connectors/xero/new-contact), [Search contacts](/en/connectors/xero/search-contacts), and [Upsert contact](/en/connectors/xero/upsert-contact). For example, you can search for contacts by name or email and use the output datapill for the Contact ID.
  
  ![Search for contacts](/assets/upsert-contact-example.Bg_jGPlw.png)_Search for contacts by name or email_
  
- Manual journal ID
  
- Obtain the unique identifier for each manual journal in Xero using actions such as [Create manual journal](/en/connectors/xero/create-manual-journal), [Search manual journals](/en/connectors/xero/search-manual-journals), and [Update manual journal](/en/connectors/xero/update-manual-journal).
  
  ![Manual Journal ID](/assets/manual-journal-example.CislJjM1.png)_Search for manual journal ID_
  
- Payment ID
  
- Retrieve the unique identifier for each payment using actions such as [Create prepayment](/en/connectors/xero/create-prepayment) and [Search payments](/en/connectors/xero/search-payments).
  
  ![Payment](/assets/search-payment-example.BT-3CIJf.png)_Search for payment ID_
  
- Employee ID
  
- Obtain the unique identifier for each employee using triggers and actions such as [New/updated employee](/en/connectors/xero/new-employee) and [Create employee](/en/connectors/xero/create-employee-us).
  
- Account ID
  
- Retrieve the unique identifier for each account using triggers and actions such as [New/updated payment](/en/connectors/xero/new-payment), [Create invoice payment](/en/connectors/xero/create-invoice-payment), and [Get payment](/en/connectors/xero/get-payment). Alternatively, switch to **Account code** found in **Xero settings > Chart of accounts**.

---
