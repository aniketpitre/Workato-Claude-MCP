---
url: 'https://docs.workato.com/en/connectors/sendgrid.md'
description: >-
  The SendGrid connector enables you to automate email workflows, sending
  marketing, transactional, and automated messages with high deliverability.
---

# SendGrid

[SendGrid](https://www.sendgrid.com) enables you to deliver emails for your business. You can use SendGrid to send marketing emails, automated messages, and transactional emails, ensuring high deliverability and effective customer engagement.

## API version

SendGrid's connector uses the Web API v3 for integration with Workato. For more information, see [SendGrid's API documentation](https://sendgrid.com/docs/API_Reference/index.html).

## Prerequisites

Ensure that your API key has the correct permissions before you connect to SendGrid in Workato:

1. Go to **Settings > API Keys** in your SendGrid account.
   
2. Click **Create API Key**.
   
3. Select **Restricted Access** under **API Key Permissions** and set `Mail Send` to **Full Access**.
   
   > **VERIFY ACCESS**
   > 
   > If a 403 error occurs after you assign permissions, switch the API key to **Full Access** to test whether missing permissions cause the issue. Revert to **Restricted access** with only the required scopes after verification to maintain security best practices.
   
4. Assign any additional required scopes based on your application's needs.
   
5. Use this API key in your [Workato connection setup](#connection-setup).
   

## Connection setup

Complete the following steps to set up a SendGrid connection in Workato:

1. Enter a unique **Connection name** to identify your SendGrid account in Workato.
   
   ![SendGrid connection setup](/assets/sendgrid-connection-setup.DMwgZLjL.png)_Name your connection_
   
2. Enter the **API Key** you configured in the [Prerequisites](#prerequisites) section.
   
3. Review all information you entered to ensure it is correct, including the connection name and API key.
   
4. Click **Connect** to establish a connection between Workato and your SendGrid account. This action redirects you to SendGrid for login and confirmation.

---
