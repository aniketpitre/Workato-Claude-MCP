---
url: >-
  https://docs.workato.com/en/features/runtime-user-connections/using-runtime-user-connections-in-workbot-recipes.md
description: >-
  Set up runtime user connections in Workbot recipes so users authenticate with
  their own credentials in Slack or Microsoft Teams commands.
---

# Use runtime user connections in Workbot recipes

This guide will walk you through using [Runtime user connections](/en/features/runtime-user-connections) in **Workbot recipes**.

Any of Workato's Workbots can be used, including **Workbot for Slack** and **Workbot for Microsoft Teams**.

In this guide, we'll cover:

- [Prerequisites](#prerequisites)
- [Create a Workbot command recipe](#step-1-create-a-workbot-command-recipe)

* * *

## Prerequisites

To complete the steps in this guide, you need:

- The following privileges in Workato:
  
  - **Create/edit Recipes**
  - **View/edit Runtime user connections**
  - **Create/edit Connections**
- Access to the **Workbot** feature
  

* * *

## Create a Workbot command recipe

1. In your account, create a new **Workbot** recipe.
   
2. Select the **New Command** trigger.
   
3. Add steps and actions. You can choose whether to use runtime user connections or the default recipe connection when selecting app connections for your actions.
   
   ![Configure runtime user connections in Workbot recipes](/assets/workbot-runtime-user-connections.Bli_y4zl.png)_Configure runtime user connections in Workbot recipes_
   
4. Save and test the recipe.
   

Now when this recipe is triggered, users will be prompted to provide their credentials for this connection. For example:

![personal-connection-flow](/assets/slack-flow.BTFiRurD.gif)_Personal connection setup for Salesforce Approval flow_

* * *

## What's Next?

- [Runtime user connections](/en/features/runtime-user-connections)
- [Using runtime user connections in Recipe functions](/en/features/runtime-user-connections/using-runtime-user-connections-in-recipe-functions)
- [Managing runtime user connections with Workbot](/en/features/runtime-user-connections#managing-runtime-user-connections-with-workbot-in-slack)
