---
url: 'https://docs.workato.com/en/connectors/freshbooks.md'
description: >-
  [FreshBooks](https://www.freshbooks.com/) is a cloud-based accounting software
  platform designed for small businesses and freelancers. It provides tools for
  invoicing, expense tracking, time tracking, project management, and financial
  reporting to help businesses manage their finances efficiently.
---

# FreshBooks

[FreshBooks](https://www.freshbooks.com/) is a cloud-based accounting software platform designed for small businesses and freelancers. It provides tools for invoicing, expense tracking, time tracking, project management, and financial reporting to help businesses manage their finances efficiently.

## Prerequisites

Before using the FreshBooks connector in Workato, ensure you have an active FreshBooks account with proper permissions and have set up OAuth 2.0 authentication.

- [Set up your FreshBooks account](#account-setup)
- [Create an application in the FreshBooks Developer Portal](#app-creation)
- [Configure OAuth 2.0 authentication scopes](#scopes)

### Set up your FreshBooks account

Ensure that you have an active FreshBooks account with administrative privileges. You can sign up at [FreshBooks.com](http://FreshBooks.com) if you don't have an account.

### Create an application in the FreshBooks Developer Portal

Complete the following steps to set up a developer application in FreshBooks and obtain OAuth 2.0 credentials:

1. Sign in to the [FreshBooks Developer Portal](https://my.freshbooks.com/developers) using your FreshBooks account credentials.
   
2. Select **My Apps**, then click **Create New App**.
   
3. Enter the **App Name** and **Redirect URI**. The [universal callback URL](/en/developing-connectors/registering-new-client#universal-callback-url) for Workato is `https://www.workato.com/oauth/callback`.
   
4. Click **Save** to register the app.
   
5. Copy the generated **Client ID** and **Client Secret** for use in your OAuth integration.
   

### Configure OAuth 2.0 authentication scopes

Configure the appropriate scopes for your application based on the data you need to access. Refer to the [FreshBooks API Scopes documentation](https://www.freshbooks.com/api/scopes) for a complete list of available scopes and their permissions.

## How to connect to FreshBooks

Complete the following steps to establish a connection to FreshBooks in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **FreshBooks** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field. ![FreshBooks connection](/assets/connection.BNIJDtTG.png)_FreshBooks connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID** and **Client Secret** for your FreshBooks developer application, which you obtained from the FreshBooks Developer Portal.
   
6. Click **Connect** to establish the connection.

---

---
url: >-
  https://docs.workato.com/en/connectors/freshbooks/new-updated-record-trigger.md
description: >-
  The New/updated record trigger runs the recipe when there is a new or updated
  record in FreshBooks.
---

# FreshBooks - New/updated record trigger

The **New/updated record** trigger runs the recipe when there is a new or updated record in FreshBooks.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to monitor from the drop-down menu. Fields load dynamically based on the object you select. |
| Account ID | Select the FreshBooks account ID to trigger the record. |
| Trigger poll interval | Select the frequently to check for new events from the drop-down menu. The minimum value allowed is 5 minutes. [Learn more](/en/recipes/polling-intervals). |
| When first started, this recipe should pick up events from | When you first start a recipe, it picks up events from this specified date and time. It processes new or updated records from 1 hour ago if left blank. Once a recipe has been run or tested, the value cannot be changed. |
| Set trigger condition | Defines further guidelines added to a specific trigger that filter what type of trigger events should be selected for processing. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if you select the **Payment** object, the output schema is as follows:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the payment. |
| Invoice ID | ID of the associated invoice. |
| Amount | Payment amount with amount and currency code. |
| Date | Date when the payment was made. |
| Type | Method of payment (Check, Credit, Cash). |
| Notes | Additional notes about the payment. |
| Gateway | Payment processor used. |
| From credit | Whether payment is from client credit. |
| Accounting System ID | Accounting system identifier. |
| Bulk Payment ID | Associated bulk payment ID. |
| Client ID | Associated client ID. |
| Credit ID | Associated credit ID. |
| Log ID | Payment log ID. |
| Note | Payment note. |
| Order ID | Associated order ID. |
| Overpayment ID | Associated overpayment ID. |
| Send client notification | Whether to send a notification to the client. |
| Transaction ID | Associated transaction ID. |
| Updated | Last update timestamp. |
| Visibility state | Visibility state of the payment. |

---
