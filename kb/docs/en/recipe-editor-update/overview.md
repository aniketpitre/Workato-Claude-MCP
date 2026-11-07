---
url: 'https://docs.workato.com/en/recipe-editor-update/overview.md'
description: >-
  See how the Workato recipe editor improves recipe building, with sections on
  triggers, steps, actions, and data mapping.
---

# Workato recipe editor update

See how recipe building has improved with Workato's new recipe editor.

* * *

## Getting started

Main article: [Getting start with your first recipe](/en/getting-started)

* * *

## Workato concepts

Main article: [Workato concepts](/en/workato-concepts)

* * *

## Connecting Apps

Main article: [Connecting apps](/en/connections)

* * *

## Building recipes

This section covers the basic components of a recipe: triggers, steps, and actions. These components allow you to define the logic of a recipe - what to carry out under different conditions. This section also covers fields mapping, which delves into the details of how we map pills to define how data is moved from one app to another.

### Triggers

  
Trigger chapters

  
\- [Polling Triggers](/en/recipes/triggers.html#polling-triggers)  
\- [Real-time Triggers](/en/recipes/triggers.html#real-time-triggers)  
\- [Scheduled triggers](/en/recipes/triggers.html#scheduled-triggers)  
\- [Single trigger](/en/recipes/triggers.html#single-triggers)  
\- [Batch triggers](/en/recipes/triggers.html#batch-triggers)  
\- [When first started, this recipe should pick up events from](/en/recipes/triggers.html#since-from)  
\- [Trigger conditions](/en/recipes/triggers.html#trigger-conditions)  
  

### Steps

  
Recipe steps chapters

  
\- [Action step](/en/recipes/steps.html#action-step)  
\- [Conditional action step](/en/recipes/steps.html#conditional-action-step)  
\- [Repeat step](/en/recipes/steps.html#repeat-step)  
\- [Call recipe step](/en/recipes/steps.html#call-recipe-step)  
\- [Stop step](/en/recipes/steps.html#stop-step)  
\- [Action with error handler step](/en/recipes/steps.html#action-with-error-handler-step)  
  

### Actions

  
Recipe actions chapters

  
\- [Create action](/en/recipes/actions.html#create)  
\- [Update action](/en/recipes/actions.html#update)  
\- [Search action](/en/recipes/actions.html#search)  
\- [Get action](/en/recipes/actions.html#get)  
\- [Upsert action](/en/recipes/actions.html#upsert)  
\- [Delete action](/en/recipes/actions.html#delete)  
  

### IF conditions

  
IF condition chapters

  
\- [contains](/en/features/if-conditions.html#contains)  
\- [starts with](/en/features/if-conditions.html#starts-with)  
\- [ends with](/en/features/if-conditions.html#ends-with)  
\- [does not contain](/en/features/if-conditions.html#does-not-contain)  
\- [does not start with](/en/features/if-conditions.html#does-not-start-with)  
\- [does not end with](/en/features/if-conditions.html#does-not-end-with)  
\- [equals](/en/features/if-conditions.html#equals)  
\- [does not equal](/en/features/if-conditions.html#does-not-equal)  
\- [greater than](/en/features/if-conditions.html#greater-than)  
\- [less than](/en/features/if-conditions.html#less-than)  
\- [is true](/en/features/if-conditions.html#is-true)  
\- [is not true](/en/features/if-conditions.html#is-not-true)  
\- [is present](/en/features/if-conditions.html#is-present)  
\- [is not present](/en/features/if-conditions.html#is-not-present)  
  

### Datapills and mapping

  
Datapills and mapping chapters

  
\- [Data types](/en/recipes/data-pills-and-mapping.html#data-types)  
\- [Type conversions](/en/recipes/data-pills-and-mapping.html#type-conversions)  
\- [Preview data](/en/recipes/data-pills-and-mapping.html#preview-data)  
\- [Fields mapping](/en/recipes/data-pills-and-mapping.html#fields-mapping)  
  

## Best practices: Error handing

Main article: [Error handling best practices](/en/recipes/best-practices-error-handling)

## Version management

Main article: [Version management](/en/recipes/version-management)

* * *

## Running recipes

This section covers recipe management - what you need to know to handle testing, starting, and stopping a recipe. This section also covers jobs management - how to read your jobs report for troubleshooting and debugging, as well as how to customize your jobs report to get the most relevant data.

### Test, start, and stop recipe

  
Test, start, and stop recipe chapters

  
\- [Test mode](/en/recipes/start-and-stop.html#test-mode)  
\- [Start recipe](/en/recipes/start-and-stop.html#start-recipe)  
\- [Stop recipe](/en/recipes/start-and-stop.html#stop-recipe)  
  

### Jobs

  
Jobs chapters

  
\- [Jobs report](/en/recipes/jobs.html#jobs-report)  
\- [Job details](/en/recipes/jobs.html#job-details)  
  

### Tasks

Main article: [Tasks](/en/recipes/tasks)

### Rerun job

  
Rerun job chapters

  
\- [Cached trigger data](/en/recipes/rerun-job.html#cached-trigger-data-in-job-reruns)  
\- [Job rerun history](/en/recipes/rerun-job.html#job-rerun-history)  
  

### Read only mode

Main article: [Read only mode](/en/recipes/read-only-mode)

* * *

## Troubleshooting: Recipe design errors

  
Recipe design errors chapters

  
\- [Missing required fields](/en/recipes/recipe-design-time-errors.html#missing-required-input-fields-at-design-time)  
\- [Formula errors](/en/recipes/recipe-design-time-errors.html#design-time-formula-errors)  
\- [Invalid datapills](/en/recipes/recipe-design-time-errors.html#invalid-datapills)  
  

* * *

## Data types and formulas

  
Formula chapters

  
\- [Filter formula by data type](/en/formulas/formula-mode.html#filter-formulas-displayed-by-data-type)  
\- [Formula hints and syntax](/en/formulas/formula-mode.html#formula-hints-and-syntax)  
\- [Text mode vs Formula mode](/en/formulas/formula-mode.html#text-vs-formula-mode)  
\- [Ternary condition](/en/formulas/formula-mode.html#conditionals)  
\- [Safe Navigation Operator](/en/formulas/formula-mode.html#safe-navigation-operator)

---

---
url: >-
  https://docs.workato.com/en/workbot-for-teams/guides/creating-enterprise-workbot-app-studio.md
description: >-
  Create a Microsoft Teams Enterprise Workbot using Microsoft App Studio,
  retained for reference after Microsoft deprecated App Studio.
---

# Create an Enterprise Workbot using the Microsoft App Studio

To set up an Enterprise Bot, you need:

- **The following in Workato**:
  
  - **Access to:**
    - **Workbot.** If you don't see the **Platform > Workbot** option in your account, contact your Customer Success Manager.
    - **[Custom OAuth profiles](/en/custom-oauth-profiles).** If you don't see the **Tools > Custom OAuth Profiles** option in your account, contact your Customer Success Manager.
  - **Privileges that allow you to:**
    - Create and configure Workbots.
    - Create and configure connections.
    - Create and configure Custom OAuth Profiles.
- **One of the following roles in your Microsoft organization**:
  
  - Application administrator
  - Cloud application administrator
  - Global administrator
  - Privileged role administrator
  
  Check your role assignments in [Microsoft](https://portal.azure.com/) by navigating to **Users > You (select your name) > Assigned roles**.
  

> **MICROSOFT APP STUDIO IS DEPRECATED**
> 
> As of **January 1, 2022**, Microsoft has deprecated App Studio. To create Enterprise Workbots, use the [Microsoft Teams Developer Portal guide](/en/workbot-for-teams/guides/creating-enterprise-workbot). We're retaining this guide for reference only.

* * *

## Step 1: Create The Workbot In Workato

1. Sign in to your Workato account.
   
2. Go to **Platform > Workbot**.
   
3. Click the **Custom bot** tab, then **\+ New custom bot**.
   
4. In the **Application** field, select **Workbot for Microsoft Teams**.
   
5. In the **Name** field, enter a name for the bot.
   
6. Click **Create new app**.
   

Keep this page open - you'll need it to complete the setup for your bot.

* * *

## Step 2: Create A Microsoft Teams App

- [Step 2.1: Install Microsoft App Studio](#step-2-1)
- [Step 2.2: Create and configure an app](#step-2-2)
- [Step 2.3: Add a personal tab to your bot](#step-2-3)
- [Step 2.4: Obtain bot credentials](#step-2-4)

### Step 2.1: Install Microsoft App Studio

Complete the following steps to install Microsoft App Studio:

> **NOTE**
> 
> If you already have App Studio installed, skip to [the next step](#step-2-2).

1. Sign in to your Microsoft Teams account.
   
2. From the left navigation menu, click the ellipsis (`...`) and search for **App Studio.**
   
   ![](/assets/install-app-studio.CtSFGlsN.png)
3. Click and install App Studio.
   

### Step 2.2: Create And Configure An App

1. In App Studio, navigate to the **Manifest editor** tab.
   
2. Click **Create new app**.
   
   ![](/assets/create-new-app.XxoIvfJT.png)
3. On the page that displays, fill in the following:
   
   - **Short name**: A short name for your bot. For example: `OpsBot`
     
   - **Full name**: **Optional.** The full name of your bot. For example: `Opportunities Bot`
     
   - **App ID**: Click **Generate** to generate an App ID.
     
     > **SAVE THIS INFO!**
     > 
     > Keep the **App ID** handy - you'll need it to complete the bot setup in Workato.
     
   - **Package name**: Enter the package name in reverse domain format. For example: `com.workato.opsbot`
     
   - **Version**: Enter the version of your bot. The version will typically be `1.0.0` for a new bot.
     
   - **Short description**: Enter a short description of your bot.
     
   - **Full description**: Enter a long description of your bot. **Note**: Microsoft will reject the full description if it contains the same text as the **Short description**.
     
   - **Website**: Enter `https://www.workato.com`
     
   - **Privacy statement**: Enter `https://www.workato.com/legal/privacy-policy`
     
   - **Terms of use**: Enter `https://www.workato.com/legal/terms-of-service`
     
   - **Branding**: We recommend using your app's own icons, but the default Workbot icons can also be used. If using your own, verify that the icons meet Microsoft's size requirements.
     
     To use the default Workbot icons, right-click and save the following:
     
     - **Full color (192x192 pixels)**:
       
       ![](data:image/png;base64,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)
     - **Transparent outline (32x32 pixels**: The image looks blank, but it's there. Use `#108921` as the accent color.
       
       ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAolBMVEUAAAD///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8ELnaCAAAANXRSTlMA/DHme+rXBwPx0YqBKAzgzMKmj2FZUEI+NiwiFhL13bSwrHRpOsehk3BmVEvt7L24qZgbmY6ZNq4AAAFMSURBVBgZzcHXkqJAAAXQ293kJKCgJHPWyXP//9cWacotnSme5xz8LeUlwpDwlWsHA67kwsaAaMkAg3Y0MKgSHxhkqxhaZANw8MNs59TyYhz2C+uzwhP7azcJPjxTUFMS/8nt8d1y+Whvo9ekgg+UyZsCmrPmo6Cux2xNoE15Y74tqMUAbIukDy1hy6vQrNhZopWQXEFTbJ0BFII3LyWwc0l6DjobtiYApGBH+b7JllmjM2Ur/kKUsrOYUxMSnWrO1mjt0RNsFSv2LuhEI/ZmxkglWWmyF0BL2IunYShPippQBrQD78xXtlzrfby9ho0DbcM711r5k6mU0/PJxl1OUqh9amQzWVxPn4kiKUrcVYcgk+UsM9L4haQYvX1v8hCPmhFJ11oeje12M05DPIv88SQ/G8elNSc5z/Ebn6TrrYOsqPGr2TiXjYNn/wAOgUJRFP5gJAAAAABJRU5ErkJggg==)

### Step 2.3: Add a personal tab to tour bot

Complete the following steps to add a personal tab to your bot:

> **THIS STEP IS OPTIONAL**
> 
> Skip to the [next step](#step-2-4) if you don't want to add a personal tab to your bot.

1. Click **Capabilities > Tabs**.
   
2. Click **Add a personal tab.**
   
3. Fill in the following fields:
   
   - **Name**: Enter `Getting started`
   - **Entity ID**: Enter `gettingstarted`
   - **Content URL**: Enter `https://docs.workato.com/workbot-for-teams/getting-started.html`
   - **Website URL**: Enter `https://docs.workato.com/workbot-for-teams/getting-started.html`
4. Click **Save**.
   

The page should look like the following when you're finished:

![](/assets/personal-tab.nYFScd4I.png)

### Step 2.4: Obtain Bot Credentials

- [Step 2.4.1: Obtain Client ID](#step-2-4-1)
- [Step 2.4.2: Obtain Client Secret](#step-2-4-2)

#### Step 2.4.1: Obtain Client ID

1. In the left navigation bar, click **Capabilities > Bots**.
   
2. Click **Set up**.
   
3. Give your bot a name. For example: `OpsBot`
   
4. Under **Scopes**, select the following scopes:
   
   - Personal
   - Team
   - Group Chat

After the bot has been created, locate the **Bot ID** under the bot's name. The Bot ID will be used as your bot's Client ID, so keep it handy - you'll need it to complete the setup in Workato.

#### Step 2.4.2: Obtain Client Secret

Under **App passwords**, select **Generate new password.**

The password will be used as your bot's Client Secret, so keep it handy - you'll need it to complete the setup in Workato.

* * *

## Step 3: Configure Workato To Talk To The App

1. Navigate back to the Workato page from [Step 1](#step-1).
   
2. In the **Step 3** section, fill in the following fields:
   
   - **Bot ID**: The **Bot ID** you generated in the [previous section](#step-2-4-1).
   - **Client secret**: The **App password** you generated in the [previous section](#step-2-4-2).
   - **App ID**: The **App ID** you generated when you [created the app](#step-2-2).
3. Click **Save**.
   
4. Expand the **Step 4** section and copy the bot endpoint address. It should look something like this:
   
   ```
   https://app.workato.com/skype_webhooks/event?coak_id=42
   ```
   
   Keep this handy - you'll need it to complete the next step.
   

* * *

## Step 4: Configure The App To Talk To Workato

- [Step 4.1: Configure the bot's endpoint address](#step-4-1)
- [Step 4.2: Add Workato's domain to allowlist](#step-4-2)
- [Step 4.3: Download the bot manifest](#step-4-3)
- [Step 4.4: Upload the manifest to your app store](#step-4-4)
- [Step 4.5: Add the bot to a team or channel](#step-4-5)
- [Step 4.6: Configure authentication redirect URLs](#step-4-6)

### Step 4.1: Configure The Bot's Endpoint Address

1. Navigate back to Microsoft Teams App Studio.
   
2. Navigate to **Manifest editor > Your bot > Capabilities > Bot**.
   
3. In the **Messaging endpoint** section, paste the **bot endpoint address** from the [previous section](#step-3) into the **Bot endpoint address** field.
   
   ![](/assets/messaging-endpoint.DeMXoZS3.png)

### Step 4.2: Add Workato's Domain to the Allowlist

1. In the left navigation bar, navigate to **Finish > Domains and permissions**.
   
2. In the **Enter a valid domain** field, enter `*.workato.com`.
   
   ![](/assets/allowlist-domain-1.DVqJAqWE.png)
3. Click **Add**. The domain will be added to the **Additional valid domains** section.
   

### Step 4.3: Download The Bot Manifest

1. In the left navigation bar, navigate to **Finish > Test and distribute**.
   
2. **If there are any errors on the right side of the page, resolve them before proceeding.** If left unresolved, you may run into issues with installation or downloading your app package (a.k.a. manifest). These issues are typically related to fields in **Details** > **App details** or **Capabilities** > **Bots**.
   
   ![](/assets/test-distribute-issues.BjplDu0p.png)
   
   When resolved, proceed to the next step.
   
3. Click **Download**. Your app's manifest will be downloaded into your default download folder. Take note of the file's location - you'll need it to complete the next step.
   

### Step 4.4: Upload The Manifest To Your App Store

1. Open a new browser tab and browse to the [Microsoft Teams Admin Center](https://admin.teams.microsoft.com/policies/manage-apps).
   
2. In the left navigation bar, navigate to **Teams apps > Manage apps**.
   
   ![](/assets/teams-admin-center.Ci7NiM5V.png)
3. In the apps table, click **\+ Upload**.
   
4. Select and upload the manifest file you downloaded in the [previous section](#step-4-4). This will upload the bot to the Microsoft tenant app catalog.
   

### Step 4.5: Add The Bot To A Team/Channel

1. Navigate to your **Microsoft tenant app catalog**.
   
   ![](/assets/add-sideloaded-app.CHskDqb9.png)
2. Find and select your app in the **Build for <YOUR\_NAME>** section. If you don't see the app, sign out and back into Microsoft Teams again.
   
3. Click the arrow next to the **Add** button and select **Add to team**.
   
   ![](/assets/sideload-choose-team.BynENgcQ.png)
4. Enter a team or channel name.
   

### Step 4.6: Configure Authentication Redirect URLs

1. Navigate to your [Azure portal](http://portal.azure.com/).
   
2. In the search bar, enter `App Registration` and select the result.
   
3. On the page that displays, click on your bot.
   
   ![](/assets/app-registrations.C0NWTpfm.png)
4. From the left navigation bar, click **Authentication**.
   
5. Under **Platform configurations**, click **+Add a platform/Web**.
   
6. In the **Redirect URIs** section, add the following URIs:
   
   - `https://www.workato.com/auth/skype/callback`
   - `https://www.workato.com/users/auth/skype`
   - `https://www.workato.com/oauth/callback`
7. Click **Save**, located near the top of the page:
   
   ![](/assets/redirect-uris.sht9cwL0.png)

* * *

## Step 5: Establish A Workbot Connection

1. Open the browser tab with your Workato account.
   
2. Navigate to [**Connections**](https://app.workato.com/?fid=smart-connection).
   
3. Click **Create connection**.
   
4. Search for and click on **Workbot for Microsoft Teams** in the list of apps.
   
5. Fill in the following:
   
   - **Connection name**: Enter a name for the connection.
   - **Location**: Select a folder where the connection will be stored.
   - **Advanced settings**: In **API Scope(s)**, select the API scopes you want the bot to use. By default, `User.Read`, `User.Read.All`, and `Group.Read.All` will be requested.
   - **Custom OAuth profile**: Select the custom OAuth profile you want the bot to use.
   
   ![](/assets/app-connection-with-custom-oauth.BGjHH_JK.png)
6. Click **Connect**. You'll be prompted to authenticate yourself in Microsoft Teams.
   
7. Authenticate yourself and authorize the bot's permissions when prompted.
   

* * *

## Troubleshooting

If you encounter permissions issues during sideloading your app or authentication, check the following settings in the [Microsoft Teams admin center](https://admin.teams.microsoft.com/policies/manage-apps):

- [Org-wide app settings](#org-wide-app-settings)
- [Permission policies](#permission-policies)
- [Setup policies](#setup-policies)

### Org-Wide App Settings

1. Navigate to **Teams apps > Manage apps**.
   
2. Click **Org-wide app settings**.
   
3. Under **Third-party apps**, verify that **Allow third-party apps** is set to **On**.
   
4. Under **Custom apps**, verify that **Allow interaction with custom apps** is set to **On**.
   
   ![](/assets/org-wide-app-settings.vmIi5FRX.png)
5. Click **Save**.
   

### Permission Policies

1. Navigate to **Teams apps > Permission policies**.
   
2. Select your org-wide policy.
   
3. Under **Third-party apps**, verify that **Allow all apps** is set; alternatively, verify that your app has been allowed.
   
4. Under **Custom apps**, verify that **Allow all apps** is set; alternatively, verify that your app has been allowed.
   
   ![](/assets/permission-policies.C1qXJNW0.png)
5. Click **Save**.
   

### Setup Policies

1. Go to **Teams apps > Setup policies**.
   
2. Select your org-wide policy.
   
3. Verify that **Upload custom apps** is set to **On**.
   
   ![](/assets/setup-policies.BNiI6GJy.png)

---
