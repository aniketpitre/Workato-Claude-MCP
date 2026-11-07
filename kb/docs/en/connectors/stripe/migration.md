---
url: 'https://docs.workato.com/en/connectors/stripe/migration.md'
description: >-
  Migrate your Stripe connection in Workato from the sunset Stripe extension to
  Stripe Apps, including testing and replacing connections in recipes.
---

# Migrate your connection to Stripe Apps

This guide explains how to migrate your Stripe connection from the Stripe extension to [Stripe Apps](https://stripe.com/apps). Stripe extensions were sunset on **January 1, 2025**.

> **STRIPE APPS**
> 
> If you created your Stripe connection **on or after December 10, 2024**, it is already configured to use Stripe Apps. No additional action is required.
> 
> Similarly, no action is needed if your Stripe connection uses [API key authentication](/en/connectors/stripe#api-key).

## Review active Stripe connections

Refer to the email you received for a list of your active Stripe connections. Alternatively, you can locate your active Stripe connections in Workato by completing the following steps:

1. Sign in to your Workato account.
   
2. Go to **Assets > Connections**.
   
   ![Click the Connections tab](/assets/connections-tab.BjprR4eM.png)_Click the Connections tab_
   
3. Click the **All apps** filter, then search for `Stripe` and select it.
   
   ![Filter for Stripe connections](/assets/search-stripe.CyK65v1o.png)_Filter for Stripe connections_
   
4. Click the **All statuses** filter and select **Connected** to view active Stripe connections in your workspace.
   
   ![View your active Stripe connections](/assets/active-connections.Wa2yk2mS.png)_View your active Stripe connections_
   

## Review dependent recipes

Evaluate the number of recipes that use your active Stripe connections by completing the following steps:

1. Click the Stripe connection.
   
2. Confirm that the **Authentication type** is set to **Authorization code grant**.
   
   > **API KEY AUTHENTICATION**
   > 
   > If the connection uses API key authentication, this guide does not apply, and no action is needed.
   
3. Locate the **Dependencies** section to view the number of recipes using your Stripe connection.
   
4. Click the link to open the [Dependency graph](/en/features/dependency-graph) for more details about the dependent recipes.
   
   ![Click the link to view dependencies](/assets/dependencies-link.ChbPgCiU.png)_Click the link to view dependencies_
   
5. Assess the number and status of dependent recipes to determine the scope of your migration.
   

Repeat these steps for all Stripe connections created or connected before December 10, 2024.

## Prepare your recipes for testing

Before you [test your recipes](/en/recipes/testing), ensure you're working with a version that uses the extension-based Stripe connection. Testing a version that mirrors your current setup helps you identify migration-related issues early.

- **For workspaces with Environments enabled**: Open the version of your active recipe in the test environment.
- **For workspaces without Environments**: Clone your active recipe to create a separate version for testing.

## Test your Stripe recipes

1. [Create a demo Stripe connection](#create-a-demo-stripe-connection)
2. [Replace the connection in test recipes](#replace-the-connection-in-test-recipes)
3. [Test the recipe](#test-the-recipe)

### Create a demo Stripe connection

Complete the following steps to connect to a demo Stripe account:

1. Provide a name for your Stripe connection in the **Connection name** field.
   
2. Use the **Location** drop-down menu to specify where you plan to store this connection.
   
3. Select **Authorization code grant** from the **Authentication type** drop-down menu.
   
4. Select **Yes** from the **Demo** drop-down menu.
   
5. Click **Connect**. The Stripe sign-in dialog opens and prompts you to enter your credentials.
   
   ![Stripe connection setup](/assets/connection-setup-auth-code-grant.DZieT5yZ.png)_Stripe connection setup_
   
6. Sign in to your Stripe account and approve the connection.
   

### Replace the connection in test recipes

Complete the following steps to replace the Stripe connection in a cloned recipe or an active recipe in a test environment:

1. Open the recipe you’re testing and click the **Connections** tab.
   
2. Select the current Stripe connection.
   
   ![Select the existing Stripe connection](/assets/recipe-connections-tab.D8P1hmDW.png)_Select the existing Stripe connection_
   
3. Click **Switch**.
   
   ![Click Switch](/assets/click-switch.D9qOS6an.png)_Click Switch_
   
4. Choose the demo Stripe connection you created.
   

### Test the recipe

Complete the following steps to ensure your recipe is functioning correctly:

1. Open the recipe in the recipe editor.
   
2. Click **Test recipe** to initiate the test run.
   
3. Monitor the recipe's execution to verify that it processes data correctly at each step. Ensure all inputs and outputs align with your expectations.
   

Repeat these steps for each recipe that requires an updated Stripe connection.

## Replace the connection in production recipes

After confirming that your recipes function correctly with the demo Stripe connection, replace the connections in your active production recipes.

1. [Create a new Stripe connection](/en/connectors/stripe#authorization-code-grant) using the **Authorization code grant** authentication method. Select **No** from the **Demo** drop-down menu to specify that the connection is for a live account.
   
2. Open a recipe that uses an extension-based Stripe connection and click the **Connections** tab.
   
3. Choose the Stripe connection.
   
   ![Select the existing Stripe connection](/assets/recipe-connections-tab.D8P1hmDW.png)_Select the existing Stripe connection_
   
4. Click **Switch**.
   
   ![Click Switch](/assets/click-switch.D9qOS6an.png)_Click Switch_
   
5. Select the new Stripe connection you created.
   

> **LIMITATIONS**
> 
> Stripe allows only one connection per Stripe account and Stripe App pair. When you create a new App-based Stripe connection for the **same Stripe account**, it invalidates the tokens of any existing App-based connections for that account, making them inactive. However, if the connection is linked to a **different Stripe account**, existing connections remain unaffected.
> 
> This limitation doesn't impact pre-existing extension-based Stripe connections in Workato, which can coexist with App-based connections.

---
