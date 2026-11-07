---
url: 'https://docs.workato.com/en/recipes.md'
description: Learn more about recipes in Workato.
---

# Recipes

A recipe is an automated workflow that executes a series of steps to integrate and process data across multiple applications.

> **SUMMARY**
> 
> - Recipes use connectors to integrate with different apps, enabling seamless data flow and process automation.
> - Workato supports different types of recipes, including workflow recipes, API recipes, data pipeline recipes, app event recipes, and knowledge base recipes for various automation needs.
> - You can create recipes manually or use AIRO to build recipes from a plain-language description of your automation.

## What is a recipe?

A recipe is an automated workflow that executes a series of steps to integrate and process data across multiple applications.

Every recipe has a [trigger](/en/recipes/triggers), which defines the event that starts the workflow. When triggered, the recipe performs one or more [actions](/en/recipes/steps#action-step), such as creating a corresponding contact in Salesforce or sending a welcome email. Recipes use [connectors](/en/connections) to interact with different apps, ensuring seamless data flow across systems.

Recipes support both simple and complex workflows, with features like conditional logic for decision-making, loops to process datasets, and error handling to manage exceptions.

## What types of recipes can I create?

You can create various types of recipes in Workato:

- **Workflow recipes**: These are the most common recipes used to automate tasks between different applications. Workflow recipes can include triggers, actions, conditional logic, loops, and error handling to manage complex workflows.
  
- **API recipes**: These recipes allow you to create and expose [API endpoints](/en/api-mgmt/api-recipes/) using the [API platform](/en/api-management). They enable external users, other recipes, or integrated systems to access and exchange data securely. API recipes are useful for sharing data with partners or different accounts, such as providing real-time inventory status to suppliers. Learn more about [API recipes](/en/api-mgmt/api-recipes/).
  
- **Data pipeline recipes**: These recipes simplify the setup, management, and monitoring of data pipelines by enabling seamless data movement from a source to a destination. They can ingest thousands of objects in a single step, automatically matching schemas as data moves across systems. Data pipeline recipes are ideal for syncing data to warehouses, running post-load transformations, and building ETL/ELT workflows. Learn more about [data pipeline recipes](/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe).
  
- **App event recipes**: These recipes send real-time business events from external applications to a genie. This enables the genie to take over part of the process, such as researching, analyzing, or drafting messages, and notify users when processing is complete or when it requires further input or approval. Learn more about [app event recipes](/en/agentic/agent-studio/app-events).
  
- **Knowledge base recipes**: These recipes automate the process of syncing, storing, and updating documents or textual content into a genie's knowledge base. By specifying how data from external sources is ingested and stored as searchable knowledge, these recipes enable genies to answer questions and support workflows using up-to-date information. Learn more about [knowledge base recipes](/en/agentic/agent-studio/create-a-genie#create-a-knowledge-recipe).
  

> **COMMUNITY LIBRARY**
> 
> Need inspiration? You can [clone recipes](/en/community-library/install-recipes) from the [community library](https://app.workato.com/browse/recipes) and modify them to fit your use case.
> 
> Learn more about the [community library](/en/community-library).

## Create a new recipe

Complete the following steps to create a new recipe:

1. Sign in to Workato.
   
2. Click the **Recipes** tab.
   
3. Click **Create**, then select **Recipe**. Alternatively, press C+R.
   
4. Enter a name for your recipe in the **Name** field.
   
5. Select the project or folder where you plan to store your recipe from the **Location** drop-down menu.
   
6. Click **Start building** to open your new recipe in the recipe editor.
   

From here, you can use [AIRO](#airo) to build your recipe or select a [starting point](#recipe-starting-points) to create your recipe manually.

### AIRO

[AIRO](/en/airo) is Workato's AI automation engineer. Describe the automation you plan to build in plain language, and AIRO configures the recipe's steps, connections, and field mappings for you.

![AIRO chat panel with a prompt typed in the message field](/assets/describe-your-automation.nl1Xm0Ps.gif)_Type your automation description in the AIRO chat panel_

Refer to [Build recipes with AIRO](/en/airo/build/recipes) for more information.

### Recipe starting points

If you choose to build your recipe manually, you have several options for the starting point of your recipe:

- **Trigger from an app**: Choose an [app](/en/connectors/prebuilt-connectors) and trigger event to start your recipe.
- **Send app event to a genie**: Use the Workato Genie **Send business event** action to pass business context to a genie. The genie can then take over part of the process and either notify you when it's done or request guidance for next steps.
- **Sync to a knowledge base**: Use the Workato Genie **Store knowledge** action to fetch data from external sources such as websites, documents, or databases, and store it as searchable documents within the genie's knowledge base.
- **Run on a schedule**: Use the Scheduler by Workato [New recurring event](/en/features/scheduler/triggers/new-recurring-event) trigger to run your recipe at specified intervals, such as once a week. You can also use [cron expressions](/en/features/scheduler/triggers/new-recurring-event#cron-expressions) to create customized schedules.
- **Trigger from a webhook**: Use the Webhooks [New event via HTTP webhook](/en/connectors/workato-webhooks/config) trigger to activate your recipe in real-time when webhook events are sent to a generated webhook address.
- **Manage other recipes**: Use [RecipeOps by Workato](/en/connectors/recipeops) to monitor and manage other recipes, jobs, or your Workato account.
- **Build recipe function**: Create a recipe function with the Recipe function by Workato [New call for function](/en/connectors/recipe-functions/triggers/new-function-call) trigger.
- **Build an API endpoint**: Use the API platform by Workato [New API request](/en/api-mgmt/api-recipes/trigger-new-api-request) trigger to [create API-based recipes](/en/api-mgmt/api-recipes/walkthrough).
- **Build a Slack bot command**: Use the Workbot for Slack [New command](/en/workbot/workbot-triggers#new-command-trigger-building-custom-commands) trigger and [Post command reply](/en/workbot/workbot-command-reply) action to automate Slack interactions.

![Select a starting point](/assets/options.DGXKGGz0.png)_Select a starting point_

> **FURTHER READING**
> 
> - [Connections](/en/connections)
> - [Triggers](/en/recipes/triggers)
> - [Steps and actions](/en/recipes/steps)

---
