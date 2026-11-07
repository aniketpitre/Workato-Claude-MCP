---
url: 'https://docs.workato.com/en/workbot-for-teams/guides/tabs.md'
description: >-
  Reference for deprecated Enterprise Workbot Personal tabs in Microsoft Teams;
  the new Teams client does not support these Adaptive Cards tabs.
---

# Tabs

You can create rich, dynamic, and interactive tabs for your Enterprise Workbot. Tabs are rendered using Adaptive Cards, making them fully customizable. Bots can have multiple tabs, and they will appear in the order in which they are defined in the app manifest.

![Tab example](/assets/tab-example.Dd4bmgpx.png)

Tabs rendered using Adaptive Cards are only available as Personal tabs. Tabs are only available to Enterprise Workbots.

> **DEPRECATION NOTICE: MICROSOFT ADAPTIVE CARDS TABS**
> 
> Microsoft is rolling out a new Microsoft Teams client that [does not support](https://learn.microsoft.com/en-us/microsoftteams/platform/resources/teams-updates#timelines-and-rollout) the use of Adaptive Cards in Microsoft Teams tabs. **Workbot Tabs will not be displayed in the new Microsoft Teams client.**
> 
> Microsoft has not provided any comparable replacement for this functionality. We recommend either putting your onboarding content into custom help messages, or implementing your own [web-based tab](https://learn.microsoft.com/en-us/microsoftteams/platform/tabs/what-are-tabs) (outside of Workato).
> 
> Please see Microsoft [new Teams client release schedule](https://learn.microsoft.com/en-us/microsoftteams/new-teams-desktop-admin) to see when the new client will be automatically enabled for your account.
> 
> This functionality has been deprecated and we don't allow the creation of new tabs on the Workato platform.

## Setup Requirements

To set up a tab, you'll need an [Enterprise Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot).

* * *

## Step 1: Adding tab(s) to the app manifest

1. Go to [https://dev.teams.microsoft.com/apps](https://dev.teams.microsoft.com/apps).
   
2. Find your enterprise Workbot, click on the horizontal ellipsis and choose **Download app package**.
   
3. Unzip the contents of the package into a specified location and open the `manifest.json` file in a text editor (e.g. Atom, SublimeText, etc).
   
4. \[Optional\] Install a JSON formatter to your text editor (for example, [pretty-json](https://atom.io/packages/pretty-json)) to view and edit `manifest.json` file easily.
   
5. Increment `version`, e.g. if originally the version was `1.0.0`, update it to `1.0.1`.
   
6. Add your tab under `staticTabs`. Specify one-word `entityId` that will be used in the **Tab opened** trigger during [recipe setup](#step-3), e.g.:
   
   ```
   {
            "entityId": "PendingPTORequests",
            "name": "Pending PTO requests",
            "contentBotId": "{your_bot_id}",
            "scopes": [
               "personal"
             ]
   }
   ```
   
   > **NOTE**
   > 
   > Your tab(s) should be on the same level as the `conversations` and `about` tabs; your bot ID can be found under `botId`.
   
7. Save the file, and zip the manifest along with the rest of the contents of the package. There should be 3 files in total; `color.png`, `manifest.json`, `outline.png`.
   
   > **NOTE**
   > 
   > Tabs will be rendered in the order they appear in, from left to right.
   

* * *

## Step 2: Updating your enterprise Workbot

1. Go to [https://admin.teams.microsoft.com/policies/manage-apps](https://admin.teams.microsoft.com/policies/manage-apps).
   
2. Search for your enterprise Workbot and click on its name.
   
3. Under **New version**, click on **Upload file**.
   
4. Select the new zip file containing the updated `manifest.json` file.
   
   > **NOTE**
   > 
   > If done right, it should say that the app was successfully updated.
   > 
   > It can take some time for the updated app to appear in Microsoft Teams clients.
   

* * *

## Step 3: Create a tab recipe

Complete the following steps to create a tab recipe:

> **NOTE**
> 
> Each tab will require its own recipe to trigger.

1. Create a new recipe and choose the **Tab opened** trigger.
   
2. Enter the `entityId` - this should be exactly the same as the one in the [manifest](#step-1).
   
3. \[Optional\] Add actions from other apps, so that the **Show tab with Adaptive Cards** action downstream may use it.
   
4. Add the **Show tab with Adaptive Cards** action and add one or more cards.
   
5. Save & start the recipe.
   

* * *

## Step 4: View the tab(s) in Microsoft Teams

1. Log off and close the Microsoft Teams client.
   
2. Run Microsoft Teams and open a DM with your enterprise Workbot.
   
   > **NOTE**
   > 
   > You should see your tab(s) near the top.
   
3. Click on it and it should render the cards as defined in your recipe.

---
