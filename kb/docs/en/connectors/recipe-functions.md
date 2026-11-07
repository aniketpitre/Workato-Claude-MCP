---
url: 'https://docs.workato.com/en/connectors/recipe-functions.md'
description: >-
  The Recipe Functions by Workato connector enables you to build reusable
  recipes that can be called from other recipes to reduce redundancy and
  simplify testing.
---

# Recipe function by Workato

Set up a Recipe Function in 5min

[Video](https://www.youtube.com/embed/rBFu_BIslCA)

The connector allows you to build recipes that can be called from other recipes.

Called a **Recipe Function**, this recipe type is triggered by a [call from another recipe](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously). Use this connector to separate repeatable sets of actions into recipes that you can re-use in other recipes.

**If you're migrating from Callable Recipes**, check out the [Migrating to Recipe Functions and API Recipes guide](/en/features/callable-recipes/migrating-to-recipe-functions-api-recipes) for help making the switch.

* * *

## Usage Inspiration

Need some inspiration? Using , you could:

- **Reduce testing efforts**. Grouping sets of actions into dedicated recipes instead of repeating them makes your workflows easier to test and modify.
- **Increase recipe readability.** Breaking steps into smaller recipes that you can call where needed means recipes are easier to read.
- **Single-source recipe steps.** Build once and re-use anywhere! For example: If you have a standardized error notification policy, create one recipe and then re-use it to prevent redundancy.
- **Verify recipe users at runtime.** Using [Runtime user connections](/en/features/runtime-user-connections), you can allow users to use their own credentials when recipes are run.

**Looking to expose REST APIs?** Check out the [API Platform connector](/en/api-mgmt/api-recipes/).

## Quotas

Recipe functions are subject to the following quotas:

| Description | Quota |
| --- | --- |
| Size of recipe function queue | 10,000 |

### Example

Let's say we want to build this workflow:

1. Read new/updated contact info from a database
   
2. Perform some data transformation
   
3. Create new accounts in Salesforce
   
4. Add the new Salesforce accounts to a MailChimp campaign
   
5. Back the data up in a Redshift database
   

To accomplish this, we'll split the workflow into **four** recipes:

1. **Parent (calling) recipe**: Start the workflow; retrieve data from the database
   
2. **Recipe 1**: Create Salesforce accounts
   
3. **Recipe 2:** Add contacts to a MailChimp campaign
   
4. **Recipe 3**: Back contact data up to Amazon Redshift
   

By splitting this workflow into multiple recipes, we can re-use recipes elsewhere without triggering this workflow. This design approach reduces the number of redundant steps in our recipes.

Check out the following diagram to see how these recipes are connected.

![Split workflow example using recipe functions](/assets/split-workflow-example.sFsVDokZ.png)

* * *

## Setup

No configuration is required to set up this connector.

To learn how to use recipe functions in other recipes, check out the [walkthrough](/en/connectors/recipe-functions/guides/walkthrough).

> **WHO CAN SET UP CONNECTIONS?**
> 
> Collaborators must have the **Create Connections** privilege to create connections.

* * *

## Triggers

The connector supports the following recipe triggers:

- [New function call](/en/connectors/recipe-functions/triggers/new-function-call)

* * *

## Actions

The connector supports the following recipe actions:

- [Call recipe function asynchronously](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously)
- [Call recipe function synchronously](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously)
- [Return data from a recipe function](/en/connectors/recipe-functions/actions/return-data-from-a-recipe-function)
- [Wait for async calls](/en/connectors/recipe-functions/actions/wait-for-async-calls)

---
