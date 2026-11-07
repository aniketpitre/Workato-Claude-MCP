---
url: 'https://docs.workato.com/en/connectors/sage-intacct.md'
description: >-
  The Sage Intacct (Custom) connector lets you automate accounting workflows:
  create, update, search, and delete records like AP bills, AR payments, and
  orders.
---

# Sage Intacct (Custom)

[Sage Intacct](https://www.sage.com/en-us/sage-business-cloud/intacct/) is an accounting and financial management software that offers consolidation of information across business units, real-time analysis of financial operations, and compliance and auditing services.

## Sage Intacct connectors

Workato provides two connectors for Sage Intacct:

- The platform connector, available by default.
- The [community connector](https://app.workato.com/custom_adapters/3119/details?community=true) for Sage Intacct, which you must install from the [community library](/en/community-library).

Each connector supports a different set of object types for triggers and actions.

**Community connector**

The community connector supports triggers and actions for the following objects:

**Triggers:**

- Accounts payable
- Contracts
- Customers
- Invoices
- Purchasing transactions
- Vendors

**Actions:**

- Accounts
- Accounts payable and receivable
- Attachments
- Contracts
- Custom fields
- Customers
- Employees
- Invoices
- Items
- Journal, statistical journal, order, and bank feed entries
- Locations
- MEA allocations
- Price lists
- Projects
- Purchase orders
- Purchasing transactions
- Tasks
- Timesheets
- Vendors

**Platform connector**

The platform connector supports triggers and actions for the following objects:

**Triggers:**

- Accounts payable and receivable
- Contacts
- Contracts
- Expenses
- General ledger accounts
- Invoices
- Items
- Objects
- Projects
- Project tasks
- Purchase orders
- Vendors

**Actions:**

- Vendors

## Prerequisites

To establish the Intacct integration workflow on Workato, you must establish a connection between Workato and your Intacct instance. Refer to the [Sage Intacct platform connector documentation](/en/connectors/intacct#how-to-connect-to-sage-intacct-on-workato) for more information.

## How to connect to Sage Intacct (Custom)

Workato supports OAuth (Client credentials) authentication to connect to Sage Intacct (Custom). Complete the following steps to establish a connection with the Sage Intacct custom connector on Workato.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Sage Intacct (Custom)** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Sage Intacct connection](/assets/connection.1GFY_okX.png)_Sage Intacct connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Provide the **Company ID** of your Sage Intacct instance.
   
6. Provide the **Login username** and **Login password** of your Sage Intacct instance.
   
7. Provide the **Sender ID** and **Sender password**. You can find these values in the **Web Services Authorizations** section.
   
8. Provide the **Location ID** for an entity. If left blank, Workato retrieves all entities.
   
9. Click **Connect** to establish the connection.

---
