---
url: 'https://docs.workato.com/en/workbot-for-teams/proactive-messaging.md'
description: >-
  Send proactive Workbot messages to Microsoft Teams users without prior
  interaction to notify them of events from apps like Salesforce.
---

# Proactive messaging

Workbot for Microsoft Teams can send a message to any user without any prior interaction. This allows you to create workflows that trigger on events outside of Microsoft Teams, for example, a new opportunity from Salesforce.

> **ENTERPRISE WORKBOT REQUIRED**
> 
> This flow requires an [Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot) connection with [Application permissions](/en/workbot-for-teams/application-permissions), specifically `AppCatalog.Read.All` and `TeamsAppInstallation.ReadWriteAndConsentSelfForUser.All`. A standard OAuth 2.0 Delegated connection can only install Workbot into the signed-in user's own personal scope. It can't install Workbot for other users or retrieve the conversation ID needed to message them, and the **Post message** step fails with an `Application id not found` error.

![Post message with user ID](/assets/post-message-with-user-id.BlMLi3hS.png)_Posting a message with the ID (Step 2) datapill obtained from the output of a preceding get user info action_

## How to proactively send a message to a user

To send proactive messages to a user, you must use a **Get user info by User Principal Name** action followed by a **Post message** (or **Post simple message**) action.

| No. | Step | Description |
| --- | --- | --- |
| 1 | Get user ID | Use the action **Get user by User Principal Name** to obtain the user **ID**. ![](/assets/get-user-info-by-user-principal-name.CuFNy6z1.png) |
| 2 | Set user ID as message recipient | Next, use a Post message or Post simple message action with the ID (Step 2) datapill in the **Message recipient** field. ![](/assets/post-message-with-user-id.BlMLi3hS.png) |

## How it works

To proactively send messages to a user, Workbot is installed to a user in personal scope. From this installation event, Workato retrieves and caches the **conversation ID** between the user and Workbot. Subsequently, Workbot is then able to send direct messages to the user using this **conversation ID**.

## Limitations

The very first proactive message sent to a user can take significantly longer than subsequent messages due to the installation of Workbot followed by the subsequent retrieval of the **Conversation ID**. However, once Workato caches the conversation IDs of new bot users, subsequent proactive messages can be posted normally.

> **Proactively messaging first-time users inside a loop**
> 
> Be careful when sending users their very first proactive message from inside a loop as it can take as long as 10s per user. We recommend sending no more than 10 maiden messages (to new users) at a time.

---
