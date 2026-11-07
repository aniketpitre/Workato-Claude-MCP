---
url: 'https://docs.workato.com/en/connectors/surveymonkey.md'
description: >-
  The SurveyMonkey connector lets you automate survey workflows: send survey
  invites and trigger recipes on completed survey responses.
---

# SurveyMonkey

[SurveyMonkey](https://www.surveymonkey.com) is a widely used online forms and survey software that allows users to easily design and send surveys and forms, as well as analyze the results.

## API version

The SurveyMonkey connector uses [SurveyMonkey REST API V3](https://developer.surveymonkey.com/api/v3/#getting-started).

## Supported editions and versions

The SurveyMonkey connector works with all SurveyMonkey plans. However, the [Extract data](https://www.surveymonkey.com/pricing/details/) capability is required to retrieve survey responses from SurveyMonkey when you use the **Completed survey response** trigger or the **Send survey invite via email and wait for response** action.

## How to connect to SurveyMonkey on Workato

The SurveyMonkey connector uses [OAuth2 authentication](https://developer.surveymonkey.com/api/v3/#authentication) to authenticate with SurveyMonkey.

Complete the following steps to connect to SurveyMonkey in Workato:

1. Provide a **Connection name** that identifies which SurveyMonkey account Workato is connected to.
   
2. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
3. Use the **Datacenter** drop-down menu to select the data center that hosts your SurveyMonkey account. Defaults to **United States**. You must use a [custom OAuth profile](/en/custom-oauth-profiles) to connect to a data center outside of the United States.
   
4. Optional. Use the **Custom OAuth profile** drop-down menu to select a [custom OAuth profile](/en/custom-oauth-profiles) for your connection. All requests to the app use the profile you specify here.
   
5. Click **Connect** to open the SurveyMonkey authorization window.
   
6. Sign in to SurveyMonkey with your account credentials. We recommend you use an admin account to avoid permission roadblocks.
   
7. Read the terms of service and click **Authorize** to complete the connection setup.
   
   > **VIEW ANSWERS REQUIREMENT**
   > 
   > Select `view answers along with responses` during authorization if you plan to use the `Completed survey response` trigger or the `Send survey invite via email and wait for response` action.
   
   ![Authorization grant](/assets/authorization_grant.mzHGoRrt.png)_Authorize Workato to access your SurveyMonkey account._
   

## How to unlink Workato on SurveyMonkey

If you ever need to change your selections in the authorization page, you might have to unlink the current app in SurveyMonkey. Head over to your `accounts` page, where you will see the currently linked applications. Simply select `Unlink` to remove the connection.

![SurveyMonkey linked accounts](/assets/linked_accounts.BJ9qKTyn.png)

---
