---
url: 'https://docs.workato.com/en/connections.md'
description: >-
  Learn how Workato connections authorize recipes to interact with apps through
  triggers and actions, and how to create and reuse them.
---

# Connections

A connection authorizes a recipe to interact with apps through triggers and actions.

When you start building a recipe, the first step is establishing a connection between Workato and an app.

Each connection is associated with one instance of the app, such as a user account, and can be re-used across recipes.

Watch a quick video guide

[Video](https://www.youtube.com/embed/m3lajUatO7w)

  

> **SUMMARY**
> 
> - Workato connects to apps to build recipes, with each connection reusable across multiple recipes.
> - Connections require the `Create Connections` privilege and use the app's authentication API with various methods like OAuth or Basic authentication.
> - Workato's data access is tied to the user's permissions, and connections can be made within the recipe editor or through the connection wizard.
> - Multiple app instances require distinct connections. Some apps have a [secondary connector](#multiple-app-instances-one-recipe) that allows you to work with multiple instances in a single recipe.

## Create connections

Workato typically uses the app's authorization/authentication API to establish the connection and request permissions, using one of the following methods:

- OAuth 2.0
- OAuth 1.0 (and variations)
- Basic authentication (username and password)
- API key or secret

Workato's permissions in the connected app usually match those of the account used for authentication. For example, Workato can't modify cases through recipe actions if the connected Salesforce account has view-only access to cases. Refer to the [Runtime user connections](#runtime-user-connections) section for an alternative.

> **PREREQUISITES**
> 
> You must have the `Create Connections` privilege to create a connection. Refer to [Project privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets) for more information.

> **CUSTOM OAUTH PROFILES**
> 
> You can use [custom OAuth profiles](/en/custom-oauth-profiles) when you create connections to supported apps. This lets you control scopes, branding, app ownership, and more.

**In the recipe editor**

Complete the following steps to add a connection while in the recipe editor:

1. In the recipe editor, click an app from the side menu.
   
2. Click the trigger or action you plan to use.
   
3. Follow the prompts and [setup guide](/en/connectors) for the app.
   

![Connection via new recipe](/assets/via-new-recipe.CJfnafTE.gif)

**In the connection wizard**

Go to one of the following locations to add a connection using the connection wizard:

- **Assets > Create > Connection**
- **Assets > Recipes > Create > Connection**
- **Assets**, then press C twice
- **Any project > Create > Connection**

![Connection via new connection](/assets/via-new-connection.DsWF8YT_.gif)

## Use connections in recipes

Refer to the following sections for information about how connections work in recipes:

- [Multiple app instances, one recipe](#multiple-app-instances-one-recipe)
- [Runtime user connections](#runtime-user-connections)

> **ESTABLISH CONNECTIONS FIRST**
> 
> You must establish a valid connection to each app you plan to integrate with Workato before you can configure any recipe triggers or actions.

### Multiple app instances, one recipe

Most users typically have one or two instances of an app, such as one instance for production and another instance for testing.

When you have multiple instances of an app, you should create multiple connections in Workato. Each connection should authenticate to each instance of the app.

Most connectors only allow one connection per app, per recipe. You can use [secondary connectors](/en/features/secondary-connectors) if you need to work with two separate instances of an app.

> **SECONDARY CONNECTORS**
> 
> Workato doesn't support secondary connectors for all Workato connectors.
> 
> If the apps you plan to use don't have secondary connectors, then you can only use one connection per app, per recipe.
> 
> If you try to connect to multiple instances of an app that doesn't support secondary connectors within the same recipe, Workato prevents you from doing so. When you create the second connection, it automatically overrides your first connection and replaces it with the second connection.
> 
> For example, consider a scenario where you have a trigger called **New email in Gmail** that uses the **My Gmail account** connection. If a subsequent step in the recipe also involves a Gmail action, it must use the same connection. If you attempt to use a different connection, such as **My second Gmail account**, Workato updates the **New email in Gmail** trigger's connection to **My second Gmail account**.

### Runtime user connections

Recipes perform actions based on the credentials used to authorize the connection by default. However, you can use the [Runtime user connection](/en/features/runtime-user-connections) feature to swap out connections when a recipe runs.

For example, if you have a recipe that creates opportunities in Salesforce, using a Sales Manager's credentials, all opportunities show as created by the Sales Manager, even though other sales reps are creating opportunities.

Refer to [Runtime user connections](/en/features/runtime-user-connections) for more information.

> **AVAILABLE IN RECIPE FUNCTION, WORKBOT, AND SKILLS**
> 
> The runtime user connections feature is only available in Recipe function, Workbot, and skills.

## Connection errors

On occasion, app connections can become invalid. These are the most common reasons:

- The credentials were changed in the app and not in Workato.
  
- The user authorizing the connection doesn't have the permissions to access required data or perform certain actions.
  

If you encounter an invalid connection error:

- Verify that the user who is authorizing the connection has sufficient permissions.
  
- Double-check that the password, API key, and other information is entered correctly.
  
- If you've verified the user's permissions and credentials, try re-connecting the connection.
  

![Design-time errors for app connection errors](/assets/connection-error.3NnM6M4V.png)_Design-time errors for app connection errors_

## Best practices

Use the following best practices for your connections:

### Create a dedicated user for Workato

Create a dedicated app user for Workato to ensure that recipes aren't dependent on the account of a human user. If someone leaves the company, recipes continue to run.

This also allows you to tailor the permissions Workato has in the app and reduce security risk.

Apps have different granularity when it comes to defining user roles and permissions. Refer to the [connector documentation](/en/connectors) for your app for more information.

### Use sandbox credentials for development

We recommend using sandbox (or non-production) credentials for your connections when developing and testing recipes. Using test data during development ensures that live data isn't accidentally altered.

Refer to the [Use connections in recipes](#use-connections-in-recipes) section for more information.

## Quotas

| Description | Quota |
| --- | --- |
| Combined maximum of runtime user connections (RUC) and verified user access (VUA) connections per workspace | 100,000 per workspace |
| Maximum shared connections per workspace | 500 per workspace |

---
