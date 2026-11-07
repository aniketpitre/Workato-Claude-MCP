---
url: 'https://docs.workato.com/en/airo/build/recipes.md'
description: >-
  Describe a use case in plain language and AIRO builds or modifies the recipe
  in the editor.
---

# Build recipes with AIRO

You can build and modify any recipe type with AIRO directly in the recipe editor, including skills, API recipes, recipe functions, and knowledge base recipes. Start by describing your automation in plain language, and AIRO configures the steps, connections, and field mappings from there. You can track what AIRO changed and restore any recorded state.

## Write your prompt

Write a prompt that includes the apps involved, the trigger condition, and the expected outcome. The more specific you are, the more accurately AIRO configures the recipe.

Open a new or existing recipe in the recipe editor and use the AIRO chat panel, or start from the AIRO chat on the homepage. If you start from the homepage, AIRO asks you to select a project to store the recipe before building.

![AIRO chat panel with a prompt typed in the message field](/assets/describe-your-automation.nl1Xm0Ps.gif)_Type your automation description in the AIRO chat panel_

### Example prompts

The following examples show what makes an effective AIRO prompt.

**Salesforce lead → Slack**

In this example, the goal is to notify a Slack channel when a new lead is created in Salesforce.

|  | Prompt | Why it works (or doesn't) |
| --- | --- | --- |
| **Vague** | "Lead notification." | No apps, no trigger, no action. AIRO asks follow-up questions to fill in the gaps. |
| **Better** | "Send a Slack message when a new Salesforce lead is created." | Names the apps and the trigger, but doesn't specify the condition, the channel, or what to include in the message. |
| **Recommended** | "When a new Lead is created in Salesforce with the status 'Open - Not Contacted', send a Slack message to the #sales-leads channel with the lead's name, company, email, and source." | Names the apps, the trigger condition, the destination channel, and the exact fields to include. AIRO has everything it needs to configure the recipe accurately. |

**ServiceNow incident → Jira + Slack**

In this example, the goal is to create a Jira issue and notify a Slack channel when a P1 incident is created in ServiceNow.

|  | Prompt | Why it works (or doesn't) |
| --- | --- | --- |
| **Vague** | "P1 incident alert." | No apps, no trigger, no action. AIRO asks follow-up questions to fill in the gaps. |
| **Better** | "When a P1 incident is created in ServiceNow, notify the on-call channel in Slack." | Names the trigger and one destination, but doesn't include the Jira action or specify the exact channel name. |
| **Recommended** | "When a P1 incident is created in ServiceNow, create a Jira issue in the 'Incidents' project and notify the #on-call channel in Slack." | Names both destination apps, the trigger condition, the exact Jira project, and the exact Slack channel. AIRO has everything it needs to configure both actions accurately. |

**Salesforce opportunity → Slack**

In this example, the goal is to notify a Slack channel when a high-value opportunity closes in Salesforce.

|  | Prompt | Why it works (or doesn't) |
| --- | --- | --- |
| **Vague** | "Closed won alert." | No apps, no trigger, no threshold. AIRO asks follow-up questions to fill in the gaps. |
| **Better** | "When a Salesforce opportunity is closed won, send a Slack message to #big-wins." | Names the apps and the trigger, but doesn't specify the amount threshold or what to include in the message. |
| **Recommended** | "When an Opportunity in Salesforce moves to 'Closed Won' and the amount is greater than $50,000, send a Slack message to #big-wins with the opportunity name, amount, account name, and close date." | Names the apps, the trigger condition, the amount threshold, the destination channel, and the exact fields to include. AIRO has everything it needs to configure the recipe accurately. |

## Connect your apps

Connect your apps so AIRO can access your account data and configure the recipe accurately. AIRO supports both platform connectors and custom connectors installed in your workspace.

![AIRO connection panel listing apps that require a connection](/assets/select-connections.CruSmaI6.png)_AIRO lists the apps that need a connection before building_

If you click **Skip**, AIRO still creates the recipe but some field mappings may be incomplete or use placeholder text instead of datapills.

Select an existing connection or create a new one for each app listed. After selecting connections for each app, click **Use these connections** to proceed.

![The Use these connections button in the AIRO connection panel](/assets/use-these-connections.DNJ7e8YN.png)_Click **Use these connections** to confirm your selections and proceed_

## While AIRO builds

AIRO configures each step directly in the editor based on your description. While AIRO is working, the canvas is hidden and the chat is locked. When AIRO finishes, it posts a summary in the chat and reveals the canvas.

![AIRO chat panel showing a progress indicator while the recipe builds](/assets/while-airo-builds.BhE8_CPW.gif)_AIRO configures the recipe while the canvas is hidden_

## Track what AIRO changed

Each time AIRO makes a change, the following appear in the chat:

- **Recipe state** marker: Shows everything that changed between that recorded state and the current recipe, including steps AIRO configured and any edits you made manually.
- **View update details** button: Shows only what AIRO changed in that specific update. The button appears each time AIRO makes a change and is replaced when AIRO makes another change.

![AIRO chat showing a Recipe state marker and View update details button](/assets/view-update-details.BIs_p3mu.png)_Click **View update details** to see what AIRO changed in that specific update_

To return the recipe to any recorded state, click **Restore** in the chat or in the top-right corner of either diff screen. You can go to an earlier or later state, and AIRO asks you to confirm before restoring the recipe. All changes made after the selected state are discarded, including any you made manually.

> **RECIPE STATES AND RECIPE VERSIONS**
> 
> **Recipe states are not the same as recipe versions.** AIRO's recorded states don't appear in the recipe's version history. A new recipe version is only created when you click **Save**.

The [activity audit log](/en/features/activity-audit-log#airo-attribution) attributes the change to your user account with a `(via AIRO)` label. The recipe's **Latest activity** panel shows the same label.

![The recipe's Latest activity panel showing an edit and create both labeled via AIRO.](/assets/airo-latest-activity.C964Arkg.png)_The recipe's Latest activity panel labels AIRO-driven changes_

## Refine the recipe

Ask AIRO to change the recipe, map fields, or write formulas at any point in the chat. Example requests:

- "Modify the Slack message to also include the lead's phone number and the name of the lead owner."
- "Write a formula that formats the lead's created date as MM/DD/YYYY."
- "Add a step to send the lead's name, email, and company to the assigned Salesforce sales rep via Slack DM."
- "Delete the Slack step and replace it with an email to the sales team distribution list."

You can also edit any steps manually.

![AIRO chat panel with a change request typed in the message field](/assets/refine-the-recipe.DLZzU8Dq.gif)_Ask AIRO to make a change in the chat at any point_

## Manage conversations

Select **New chat** to start a new session. Your recipe content is preserved, but AIRO loses context from the previous session. Select **Chat history** to switch back to an earlier session.

Refreshing the page returns you to the same session.

## Test the recipe

Test the recipe after AIRO finishes building. The following guides cover testing, security, and error handling:

- [Testing recipes](/en/recipes/testing)
- [Security best practices for recipes](/en/recipes/recipe-security)
- [Error handling and monitoring](/en/recipes/best-practices-error-handling)

## Save the recipe

Click **Save** to create a new recipe version.

---
