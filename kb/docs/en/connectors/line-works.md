---
url: 'https://docs.workato.com/en/connectors/line-works.md'
description: >-
  The LINE WORKS connector enables you to automate business messaging and
  collaboration workflows, sending messages, managing channels, and searching
  directories.
---

# LINE WORKS

[LINE WORKS](https://line-works.com/en/blog/line-works/) is a professional communication and collaboration platform that helps organizations connect, share information, and plan schedules efficiently. With features like instant messaging, shared calendars, task management, and file sharing, it suits businesses of all sizes and industries.

Workato's LINE WORKS connector enables integrations and automations within LINE WORKS, allowing you to automate tasks such as sending messages, searching user directories, retrieving bot lists, and creating channels. It also supports triggers for events like message exchanges, postback actions, and member participation in chats.

## Prerequisites

Before using the LINE WORKS connector in Workato, ensure you have an active LINE WORKS administrator account with appropriate permissions to access APIs and permissions to use the Developer Console. Refer to LINE WORKS' [help documentation](https://help.worksmobile.com/en/service-introduction/start/registration/#i-1) for detailed steps on creating an account.

## Register an app in the LINE WORKS developer console

Register an app in the LINE WORKS Developer Console to enable integration with the Workato platform and automate tasks such as messaging, user management, and event handling.

1. Sign in to the [LINE WORKS Developer Console](https://auth.worksmobile.com/login/login?accessUrl=http%3A%2F%2Fdev.worksmobile.com%3A80%2Fconsole%2Fopenapi%2Fv2%2Fapp%2Flist%2Fview) using an administrator account.
   
2. Go to **API > Client App**.
   
3. Click **Add a Client App**.
   
4. Enter your app name, then click **Confirm** to proceed.
   
   ![Line works register app](/assets/line-works-register-app1.DX1SacEB.png)_LINE WORKS Register an application_
   
5. Complete the following steps to configure the app:
   
   1. Add a brief **Description** of the app’s purpose.
      
   2. Select the required **API Scopes** (e.g., bot.read, task.read). Refer to LINE WORKS' [OAuth Scopes](https://developers.worksmobile.com/jp/docs/auth-scope) documentation for more details on authorization scopes.
      
   3. Enter the **Redirect URL** provided by Workato for OAuth. Refer to the [Workato Redirect URL guide](/en/developing-connectors/registering-new-client#callback-url) to access your **Redirect URL**.
      
   4. Click **Add**.
      
   5. Click **Save** to complete the app's configuration. ![Line works register app](/assets/line-works-register-app2.DbSxYCZA.png)_LINE WORKS Register an application_
      
6. Copy the **Client ID** and **Client Secret** and store them in a secure location. For more details, refer to the [LINE WORKS Developer Documentation](https://developers.worksmobile.com/jp/docs/introduction/).
   

## Register a Bot in LINE WORKS

Configuring a bot in the LINE WORKS Developer Console is required to utilize this connector's triggers and actions.

Complete the following steps to configure a bot in the LINE WORKS Developer Console:

1. Sign in to the [LINE WORKS Developer Console](https://auth.worksmobile.com/login/login?accessUrl=http%3A%2F%2Fdev.worksmobile.com%3A80%2Fconsole%2Fopenapi%2Fv2%2Fapp%2Flist%2Fview) using an administrator account.
   
2. Go to **API > Bot**
   
3. Click **Register**.
   
4. Provide the **Bot Name**, a brief **Bot Description**, and complete the necessary fields.
   
   ![Line works register bot](/assets/line-works-register-app3.C-fe822I.png)_LINE WORKS Register a Bot_
   
5. Click **Save** to complete the bot's configuration.
   
6. Go to [Service > Bot](https://admin.worksmobile.com/service/bot).
   
7. Click **Add bot** to make the bot visible to members.
   
   ![Line works register bot](/assets/line-works-register-app4.Del5_Sqf.png)_LINE WORKS Register a Bot_
   
8. Locate the bot you registered in the previous steps and click **Add** in the **Add Bot** column to enable it for members.
   
9. Locate your bot and click its **Bot name** to open the **Bot info** pop-up. ![Line works register bot](/assets/line-works-register-app5.Br-RLH7J.png)_LINE WORKS Register a Bot_
   
10. Click **Edit**.
    
11. Click the **Visibility setting** toggle to make the bot public.
    
12. Click **Save** to complete the bot's configuration.
    
    Refer to the LINE WORKS' [Bot Documentation](https://developers.worksmobile.com/jp/docs/bot) for more details on bot configuration.
    

## How to connect to LINE WORKS

Workato supports Oauth2 authentication to connect to LINE WORKS. This authentication method requires the following value:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **LINE WORKS** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![LINE WORKS Connection](/assets/line-works-connection-setup.Bg4jP-Yz.png)_LINE WORKS Connection_
   
4. Enter the **Client ID** generated for your application in the LINE WORKS Developer Console.
   
5. Provide the **Client Secret** generated for your application in the LINE WORKS Console.
   
6. Select the necessary [OAuth scopes](https://developers.worksmobile.com/jp/docs/auth-scope) required for your integration. If no scopes are selected, the minimum set of required scopes will be automatically applied.
   
7. Click **Connect** to complete the connection.

---
