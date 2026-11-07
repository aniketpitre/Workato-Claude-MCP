---
url: 'https://docs.workato.com/en/connectors/x-twitter.md'
description: Connect X to Workato to automate workflows with your social media platform.
---

# X (Twitter)

X (formerly Twitter) provides a social media service for microblogging and social networking services. X enables you to share text messages, images, and videos in posts and like other users' content. The X connector allows you to automate workflows to search tweets and users and post your status.

## Connection setup

The X connector uses OAuth 1.0a authentication.

### X setup for OAuth 1.0a authentication

Complete the following steps to connect to X in Workato with OAuth 1.0a authentication:

#### Generate a consumer key and secret

Complete the following steps to generate a consumer key and secret in X:

1. Sign in to the [X Developer Console](https://console.x.com).
   
2. Click **Apps > Create App**.
   
3. Enter an **Application Name**.
   
4. Select an **Environment**.
   
5. Click **Create New Client Application**.
   
6. Copy and save the **Consumer Key** and **Secret Key** for use in Workato.
   
   > **SAVE YOUR CREDENTIALS**
   > 
   > The credentials only display once. If you lose them, you must generate new ones.
   

#### Generate an access token and secret

Complete the following steps to generate an access token and secret in X:

1. Sign in to the [X Developer Console](https://console.x.com).
   
2. Click **Apps**.
   
3. Click on the app you created in the preceding steps.
   
4. Under **OAuth 1.0 Keys**, click **Generate** for **Access Token**.
   
5. Copy and save the **Access Token** and **Access Token Secret** for use in Workato.
   
   > **SAVE YOUR CREDENTIALS**
   > 
   > The credentials only display once. If you lose them, you must generate new ones.
   

### Connect to X with OAuth 1.0a

Complete the following steps to connect to X in Workato:

1. Click **Create > Connection**.
   
2. Search for `X` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![X connection setup](/assets/x-connection-setup.C74ieFMu.png)_X connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Consumer key** and **Consumer secret**.
   
6. Enter the **Access token** and **Access token secret**.
   
7. Click **Connect**.

---
