---
url: >-
  https://docs.workato.com/en/features/runtime-user-connections/using-runtime-user-connections-in-recipe-functions.md
description: >-
  Set up runtime user connections in recipe functions so actions run with each
  user's own credentials instead of the default recipe connection.
---

# Use runtime user connections in recipe functions

This guide provides information on how to use [Runtime user connections](/en/features/runtime-user-connections) in **Recipe functions**.

## Prerequisites

Ensure you have the following privileges before you begin:

- **Create/edit Recipes**
- **View/edit Runtime user connections**
- **Create/edit Connections**

* * *

## Create a recipe function

1. Go to your account and create a new **Recipe function**. The recipe must use the [Recipe functions - New function call trigger](/en/connectors/recipe-functions/triggers/new-function-call).
   
2. Add steps and actions. You can choose whether to use runtime user connections or the default recipe connection when selecting app connections for your actions.
   
   ![Configure runtime user connections in recipe functions](/assets/recipe-function-runtime-user-connections.Dwy-_oJW.png)_Configure runtime user connections in recipe functions_
   
3. Save and test the recipe.
   

* * *

## Call the recipe and swap connections

You must define how recipes use the [recipe from Step 1's](#step-1-create-a-recipe-function) runtime user connections:

1. Create a new recipe or open an existing recipe.
   
2. Click **+** (plus) and select **Action in an app**.
   
3. Search for and select the **Recipe function by Workato** connector.
   
4. Select either of the [**Call recipe function (synchronous)**](/en/connectors/recipe-functions/actions/call-recipe-function-synchronously) or [**Call recipe function (asynchronous)**](/en/connectors/recipe-functions/actions/call-recipe-function-asynchronously) actions.
   
5. Go the **Recipe to call** field and select the recipe you created in [Step 1](#step-1-create-a-recipe-function).
   
6. Go to the **Connection overrides** section and configure the connections you plan to use at runtime.
   
7. Click **Save**.
   

* * *

## What's next?

- [Recipe functions](/en/connectors/recipe-functions)
- [Runtime user connections](/en/features/runtime-user-connections)
- [Using runtime user connections in Workbot recipes](/en/features/runtime-user-connections/using-runtime-user-connections-in-workbot-recipes)
- [Managing runtime user connections](/en/features/runtime-user-connections#managing-runtime-user-connections)
