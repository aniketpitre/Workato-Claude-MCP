---
url: 'https://docs.workato.com/en/connectors/clickup.md'
description: >-
  The ClickUp connector enables you to automate project, task, and productivity
  workflows across documents, time tracking, and goals.
---

# ClickUp

[ClickUp](https://clickup.com/) is a cloud-based, all-in-one productivity platform designed to manage projects, tasks, and workflows, offering features like task management, document sharing, time tracking, goal setting, and automation. It aims to be a versatile tool for individuals and teams to organize, collaborate, and streamline their work processes.

## Prerequisites

To use the ClickUp API, you must authenticate every request. To allow others to use your app, implement the OAuth2 flow so each user has their own token for accessing their ClickUp resources. ClickUp uses the [authorization code](https://oauth.net/2/grant-types/authorization-code/) grant type.

### Generating OAuth credentials

Only Workspace owners or admins can create OAuth apps in ClickUp.

1. Log in to [ClickUp](https://app.clickup.com/login).
   
2. Select your avatar from the top right corner.
   
3. Click **Settings**.
   
4. Use the sidebar to select **Apps**.
   
5. Click **Create new app**.
   
6. Provide a name for the app.
   
7. Enter the Workato redirect URL: `https://www.workato.com/oauth/callback`
   
   Refer to [Workato callback URLs](/en/developing-connectors/registering-new-client#callback-url) for more information.
   
8. Retain the **Client ID** and **Secret** to establish a connection to ClickUp in Workato.
   

## How to connect to ClickUp on Workato

Complete the following steps to set up an connection to ClickUp:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **ClickUp** on the New connection page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down to select the project where you plan to store the connection.
   
5. Enter the **Client ID** and **Client Secret** generated in the previous step.
   
6. Click **Connect** to establish the connection. ![Connect to ClickUp](/assets/connection.DOrKxkmQ.png)_Connect to ClickUp_

---
