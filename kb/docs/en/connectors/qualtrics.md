---
url: 'https://docs.workato.com/en/connectors/qualtrics.md'
description: >-
  The Qualtrics connector enables you to manage surveys, distributions, mailing
  lists, and response data using the Qualtrics API v3.
---

# Qualtrics

[Qualtrics](https://www.qualtrics.com/) is an experience management platform that enables organizations to collect, analyze, and act on customer, employee, product, and brand experience data. Qualtrics provides tools for creating surveys, gathering feedback, and generating insights to drive business decisions.

## Prerequisites

Complete the following steps before establishing a Qualtrics connection in Workato:

- [Get your data center ID](#get-your-datacenter-id)
- [Generate an API token](#generate-an-api-token)

### Get your data center ID

Complete the following steps to obtain your data center ID:

1. Sign in to your Qualtrics account.
   
2. Identify your data center ID from your application URL. For example, if your URL is `https://partner.co1.qualtrics.com`, your data center ID is `co1`. Refer to the Qualtrics [Base URL and data center IDs](https://api.qualtrics.com/1aea264443797-base-url-and-datacenter-i-ds) documentation for more information.
   

### Generate an API token

Complete the following steps to generate an API token:

1. Sign in to Qualtrics.
   
2. Go to **Account Settings > Qualtrics IDs**.
   
3. Generate an API token. Refer to the Qualtrics [API key authentication](https://api.qualtrics.com/2b4ffbd8af74e-api-key-authentication) documentation for more information about API tokens.
   

## How to connect to Qualtrics

Complete the following steps to connect Workato to Qualtrics:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Qualtrics** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your **Data center ID**. For example, `co1`.
   
6. Enter your **Username**.
   
7. Enter your **API token**.
   
8. Click **Connect** to establish the connection.
   
   ![Qualtrics connection](/assets/connection.D7Ot3tOI.png)_Create a Qualtrics connection_

---

---
url: >-
  https://docs.workato.com/en/connectors/qualtrics/new-survey-response-trigger.md
description: >-
  Monitor for new survey responses in real time using Qualtrics webhooks.
  Triggers immediately when a respondent completes a survey.
---

# Qualtrics - New survey response trigger

The **New survey response** trigger monitors for new survey responses in real time using Qualtrics webhooks. When a respondent completes a survey, the trigger fires immediately and provides response information.

## Input

| Input field | Description |
| --- | --- |
| Survey | Select the survey to monitor from the drop-down menu, or toggle to provide a custom Survey ID. |

## Output

| Output field | Description |
| --- | --- |
| Topic | The webhook topic that triggered the event, identifying the survey and event type. |
| Status | The completion status of the survey response. For example, `Complete`. |
| Survey ID | The unique identifier of the survey. |
| Response ID | The unique identifier of the response. Use this ID with the **Get response details** action to retrieve complete response data. |
| Recipient ID | The identifier of the recipient who completed the survey. |
| Response event context | Additional context information about the response event. |
| Distribution ID | The identifier of the distribution through which the survey was sent. |
| Completed date | The date and time when the survey response was completed. |
| Brand ID | The identifier of the Qualtrics brand associated with the survey. |

---
