---
url: 'https://docs.workato.com/en/connectors/mural.md'
description: >-
  Connect Mural to Workato to automate visual collaboration workflows for your
  remote and hybrid teams.
---

# Mural

[Mural](https://www.mural.co/) is a digital workspace for visual collaboration that empowers teams to brainstorm, plan, and collaborate in a structured and creative way. It provides an individual canvas where users can add, create, and edit your content. This connector enables businesses to operate seamlessly in remote and hybrid environments, enhancing team productivity and communication.

## Prerequisites

Ensure that you have an active account with appropriate permissions to access APIs before using the Mural connector in Workato. Refer to the [Register an application in Mural](#register-application) section to create an account if you don't already have one.

### Register an application in Mural

Complete the following steps to register an app in your Mural account.

1. Log in to your [Mural](http://app.mural.co/) account.
   
2. Click your profile picture in the top right corner.
   
3. Navigate to the **Create and Manage apps**. ![Mural Dashboard](/assets/mural-create-app.C-eepbjz.jpg)_Create an app in Mural_
   
4. Click **New App** on the My Apps page. ![Mural Account Settings](/assets/mural-new-app.BmmkhwUH.png)_Mural new App_
   
5. Enter your application name in the **App name** field.
   
6. Enter your Redirect URL provided by Workato for OAuth. Refer to the [Workato Redirect URL guide](/en/developing-connectors/registering-new-client#callback-url) for more information.
   
7. Click **Save** and **Continue**.
   
8. Select the required **API Scopes**, including `mural.read`, `mural.write`, and more. Refer to [Mural OAuth Scopes](https://developers.mural.co/public/docs/scopes) for more information.
   
9. Click **Save** and **Continue**.
   
10. Copy the **Client ID** and **Client Secret**. Store them in a secure location, and click **Save** to complete the app registration.
    

Refer to the Mural [Sign up for a Mural account](https://support.mural.co/s/article/sign-up-for-a-mural-account) guide for additional information about account registration.

## Connection setup

Mural connector supports Oauth2 authentication to connect to Mural. Complete the following steps establish a connection to Mural in Workato.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Mural** as your connection on the New Connection page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID** and **Client Secret** for your Mural account. Refer to the [Register an app in Mural](#register-application) step for more information.
   
6. Select the necessary [OAuth scopes](https://developers.mural.co/public/docs/scopes) required for your integration. If no scopes are selected, the minimum set of required scopes are automatically applied.
   
7. Click **Connect**.
   
   ![Mural connection setup](/assets/mural-connection-setup.DGucELJ9.png)_Mural connection setup_

---
