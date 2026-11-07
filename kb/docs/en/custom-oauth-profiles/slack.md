---
url: 'https://docs.workato.com/en/custom-oauth-profiles/slack.md'
description: >-
  Learn how custom OAuth profiles let your Slack apps use the Workato Slack
  connector while customizing branding, permissions, and bot identity.
---

# Custom OAuth profiles for Slack

## What are custom OAuth profiles?

Custom OAuth profiles allow your Slack apps to leverage the Workato Slack connector under the hood. You can fully customize your Slack app's identity, i.e.:

- Branding (bot name, bot logos, background color)
- Permissions

## When would I need custom OAuth profiles for Slack

1. You want multiple apps that each perform workspace orchestration as part of their automations, for example, creating/archiving conversations. For example, an EscalationBot could create a private conversation, invite crisis management team members, and archive it once the issue is resolved. At the same time, BirthdayBot could perform the same actions – create a private conversation, invite the party planners, and archive it once the birthday is over – but for vastly different purposes.
   
2. You want control over your app's branding & appearance
   
3. You want control over your bot's permissions. The minimum permissions for optimal use are listed in the table below.
   

| Token type | Scope | Reason |
| --- | --- | --- |
| Bot | None | No bot scopes required. |
| User | `channels:read` | Retrieves list of public conversations. |
| `channels:write` | Create/update public conversations. |
| `groups:read` | Retrieves list of private conversations. |
| `groups:write` | Create/update private conversations. |
| `im:read` | Retrieves list of direct message conversations. |
| `im:write` | Create/update direct message conversations. |
| `mpim:write` | Create/update multi-party group conversations. |
| `mpim:read` | Retrieves list of multi-party group conversations. |
| `chat:write` | Post messages as user. |
| `users:read` | Get user info. |
| `users:read.email` | Get user info by email. |

> **Migration to granular scopes**
> 
> Slack released [granular permissions](https://api.slack.com/docs/token-types#granular_bot) on 22 January 2020. You may have to migrate any pre-existing custom Slack apps you have connected to Workato. migration guide for more details.

## Setup requirements

To create a custom OAuth profile, you'll need access to [Custom OAuth profiles](https://app.workato.com/custom_oauth_keys) in Workato.

If you're using another data center, log in to the custom profile for the Workato Enterprise or Self-service (Workato Free, Workato Pro, or Developer Sandbox) data center.

### Workato Enterprise customers

- [EU Data Center Custom OAuth profile](https://app.eu.workato.com/custom_oauth_keys)
- [JP Data Center Custom OAuth profile](https://app.jp.workato.com/custom_oauth_keys)
- [SG Data Center Custom OAuth profile](https://app.sg.workato.com/custom_oauth_keys)
- [AU Data Center Custom OAuth profile](https://app.au.workato.com/custom_oauth_keys)
- [IL Data Center Custom OAuth profile](https://app.il.workato.com/custom_oauth_keys)
- [KR Data Center Custom OAuth profile](https://app.kr.workato.com/custom_oauth_keys)
- [UK Data Center Custom OAuth profile](https://app.uk.workato.com/custom_oauth_keys)

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- [Self-service Data Center Custom OAuth profile](https://app.trial.workato.com/oauth/callback)

> **I Don't See Custom OAuth Profiles in My Workspace**
> 
> Custom OAuth Profile is an added capability. Check with your Workato CSM to ensure that you have this capability enabled for your Workspace.

## Creating a custom OAuth profile

### Step 1: Choose Slack

1. Before getting started, \[sign in to your Slack workspace\[([https://slack.com/signin#/signin](https://slack.com/signin#/signin)) from your browser.
   
2. Navigate to **Tools > Custom OAuth profiles** in Workato.
   
3. Click **New custom profile**.
   
4. On the **New custom profile** page:
   
   - In Step 1, select **Slack**.
   - In Step 2, provide a name for your new app, then click **Create new app.** This will open a new tab that brings you to [https://api.slack.com/apps](https://api.slack.com/apps). Keep both the Workato tab and this new tab open - you'll need both to complete the remaining steps.

### Step 2: Create a new Slack app

1. In the new tab, select a workplace to develop the app in, then click **Next**.
   
2. Click **Create**.
   
3. In the "Welcome to your app's configurations" pop-up, click **Got It**.
   
4. Navigate to your app's **Basic Information** page. Scroll down to **App Credentials**, you will need the information here to complete the next step.
   

### Step 3: Configure Workato to talk to your Slack app

1. Head back to the Workato tab to complete Step 3.
   
2. In Step 3, fill in the following:
   
   - **Client ID**: Paste the **Client ID** value from Slack into this field.
   - **Client secret**: Paste the **Client secret** value from Slack into this field.
   - **Verification token**: Paste the **Verification Token** value from Slack into this field.
3. Click **Save** when you're finished.
   

### Step 4: Complete the connection in Workato

You're almost there! All that's left is to complete the connection in Workato.

1. In the open Workato tab, click **Done**. Go to any project folder to create a new Slack connection.
   
2. Provide a name for your Slack connection. In the **Custom OAuth profile** field, select the newly created OAuth profile. Click **Connect**.
   
3. In the permissions grant, click **Allow**.
   

* * *

---
