---
url: 'https://docs.workato.com/en/recipes/infinite-loops.md'
description: >-
  Learn what infinite loops are in Workato recipes, how to recognize them in
  bi-directional syncs, and how to prevent recipes from triggering themselves.
---

# Infinite Loops

## What are infinite loops and when do they occur?

Infinite loops are logic errors that cause a recipe to run continuously because an action in the recipe is also triggering the recipe again.

Infinite loops occur most commonly when the recipe is performing a **bi-directional** sync, such as when there is more than one application and data moves from application A to application B and back to A.

## How will I Know if my Recipe is in an Infinite Loop?

Recipes may be in an infinite loop if:

- There is an **unexpectedly high transaction count**
- The recipe is triggered when there are **no new trigger events** in the applications
- There are many **duplicates** of an object in applications that was created by a recipe

### Example Recipe that is in an Infinite Loop

The example below shows how an infinite loop may occur:

![Recipe will caused an infinite loop error](/assets/recipe-will-cause-infinite-loop.MuLbwdof.png)_Recipe will caused an infinite loop error_

1. The trigger picks up new or updated Contacts in Salesforce.
   
2. The recipe checks if there is an existing Marketo lead with the contact's email. If it does not yet exist, the recipe will create a Marketo lead.
   
3. In the final step, the recipe will update the Salesforce contact with the Marketo lead details.
   

## Why does the infinite loop error occur?

Because of the last update step, the Salesforce contact would have been updated. Thus, triggering the recipe to start another job.

Infinite loops may also occur if you have **multiple recipes** running at once and a similar issue occurs where one recipe is updating another that is triggered by an update in an object.

> **How does Workato know a record has been updated?**
> 
> Workato identifies updated records using the **Last Modified** datetime field. If the record has been recently updated, it will trigger and create a new recipe job.

## Use Trigger Filters to Prevent Infinite Loops

In order to stop the re-triggering of recipes, implement filters in the trigger. An example of how this can be done is as follows:

![Add a trigger condition to prevent infinite loops](/assets/fix-infinite-loop-recipe.CDgxdSJV.png)_Add a trigger condition to prevent infinite loops_

Use trigger filters to filter out records that you do not want to process. In this example recipe, since we are only checking for Marketo lead IDs, we can ignore all Salesforce contacts that already have an existing **Marketo Acquisition Date**.

By filtering out these Salesforce contacts, the contact will be ignored by the recipe and will not cause an infinite loop.

## Best Practices - Creating Custom Fields

Create fields in the connected applications that are meant for identifying jobs synced by Workato. In the example above, the **Marketo Acquisition Date** field in the Salesforce Opportunity should be empty by default.

Thus, it is not advisable to use a commonly used field for these purposes, as they may be filled in by mistake and cause that job to be filtered out in the trigger.

---
