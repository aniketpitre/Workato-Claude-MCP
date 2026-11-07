---
url: 'https://docs.workato.com/en/connectors/greenhouse/migration.md'
description: >-
  Migrate Greenhouse recipes from the v1 and v2 APIs to v3, including creating
  an OAuth 2.0 connection and replacing legacy actions and triggers.
---

# Migrate your Greenhouse connection to v3

Greenhouse uses OAuth 2.0 authorization (v3) for new connections. API key authentication (v1/v2) is available only for existing connections.

> **DEPRECATION NOTICE**
> 
> Greenhouse will remove v1 and v2 API support on August 30, 2026. Recipes that use v1 or v2 will stop functioning after this date. You must migrate all existing recipes to v3.

Greenhouse doesn't support automatic migration. You must manually update all triggers and actions when you switch to a v3 connection.

Use this guide with the [Greenhouse v3 object coverage guide](/en/connectors/greenhouse/object-coverage) to understand object support and required field updates.

## Connection types and action compatibility

Greenhouse v3 uses OAuth 2.0 authorization and updated API behavior. API key authentication (v1/v2) is available only for existing connections. These connections will stop working on August 30, 2026, when Greenhouse removes support for the v1 and v2 APIs.

- Connections that use **OAuth 2.0 authorization** support **v3 actions only**
- Connections that use **API key authentication** support **v1/v2 actions only**

You can't use v1/v2 actions with a v3 connection, or v3 actions with a v1/v2 connection.

You also can't upgrade an existing connection to v3. You must create a new connection that uses OAuth 2.0 authorization (v3).

## Review existing Greenhouse connections

Complete the following steps to identify all Greenhouse connections that use v1 or v2:

1. Sign in to your Workato account.
   
2. Go to **Assets > Connections**.
   
3. Search for `Greenhouse` and select it.
   
4. Review your connections and identify those that use API key authentication.
   

## Review dependent recipes

Complete the following steps to determine which recipes use your existing Greenhouse connections:

1. Select a Greenhouse connection.
   
2. Locate the **Dependencies** section.
   
3. Click the link to open the dependency graph.
   
4. Review all recipes that use this connection.
   

Repeat these steps for each Greenhouse connection.

## Prepare recipes for testing

Prepare a safe environment before making changes.

Open the recipe version in your test environment, or clone the recipe if you don't use environments. Testing a separate version helps you identify migration issues before updating production recipes.

## Migrate recipes to Greenhouse v3

Complete the following steps to migrate recipes to Greenhouse v3:

- [Create a v3 connection](#create-a-v3-connection)
- [Update triggers and actions](#update-triggers-and-actions)

### Create a v3 connection

Complete the following steps to create a v3 connection:

1. Go to **Assets > Connections**.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for `Greenhouse` and select it.
   
4. Enter a name in the **Connection name** field.
   
5. Optional. Select the required **Harvest OAuth scopes**. Workato uses a default set of scopes if left blank.
   
6. Optional. Enter a value in the **Custom domain** field. Leave blank to use the default Harvest API host: `https://harvest.greenhouse.io`. If your organization uses a custom subdomain, such as `https://acme.greenhouse.io`, enter `acme.greenhouse.io`.
   
7. Click **Connect**.
   
8. Sign in to your Greenhouse account and approve access.
   

### Update triggers and actions

Replace each v1 action with its v3 equivalent and update the configuration.

1. Open the recipe.
   
2. Select a Greenhouse step.
   
3. Replace the v1 action with the corresponding v3 action.
   
4. Update input fields and mappings.
   
5. Repeat for all Greenhouse steps in the recipe.
   

Refer to the [Greenhouse v3 object coverage guide](/en/connectors/greenhouse/object-coverage) to identify supported objects, fields, and differences between v1 and v3 actions and triggers.

## Test updated recipes

Validate that your updated recipes function correctly:

1. Open the recipe in the editor.
   
2. Click **Test recipe**.
   
3. Verify inputs and outputs for each step.
   
4. Resolve any errors or mismatched fields.
   

Repeat testing for all updated recipes.

## Activate updated recipes

After testing, activate your updated recipes:

1. Open the production recipe.
   
2. Confirm all Greenhouse steps use v3 actions and the v3 connection.
   
3. Save and start the recipe.
   

If your workspace uses environments, deploy your updated recipes to production before you start them.

## v1 to v3 action mapping

Use the following table to identify replacement actions and required updates.

| v1 action | v3 action | Migration notes |
| --- | --- | --- |
| [Upload attachment](/en/connectors/greenhouse/upload-attachment-action) | [Create attachment (v3)](/en/connectors/greenhouse/create-attachment-v3) | Direct replacement |
| [Create object](/en/connectors/greenhouse/create-object-action) | [Create object (v3)](/en/connectors/greenhouse/create-object-v3) | Object coverage differs |
| [Mark candidate as hired](/en/connectors/greenhouse/mark-candidate-as-hired-action) | [Mark candidate as hired (v3)](/en/connectors/greenhouse/mark-candidate-v3) | No major change |
| [Advance application](/en/connectors/greenhouse/advance-application-action) | [Move application (v3)](/en/connectors/greenhouse/move-application-v3) | Not a 1:1 match. Move supports broader transitions |
| [Reject application](/en/connectors/greenhouse/reject-application-action) | [Reject application (v3)](/en/connectors/greenhouse/reject-application-v3) | Direct replacement |
| [Search objects](/en/connectors/greenhouse/search-objects-action) | [Search objects (v3)](/en/connectors/greenhouse/search-objects-v3) | Query parameters and object coverage differ |
| [Update object](/en/connectors/greenhouse/update-object-action) | [Update object (v3)](/en/connectors/greenhouse/update-object-v3) | Supported objects differ |
| [Get object by ID](/en/connectors/greenhouse/get-object-by-id-action) | [Search objects (v3)](/en/connectors/greenhouse/search-objects-v3) | Filter by a comma-separated list of IDs |

## Key differences between v1 and v3

Greenhouse v3 introduces changes to action behavior, search functionality, and object support. Some v1 actions aren't available in v3 and require alternative approaches.

### Broader action behavior

The [Move application (v3)](/en/connectors/greenhouse/move-application-v3) action replaces the [Advance application](/en/connectors/greenhouse/advance-application-action) action and supports a wider range of transitions. Review your recipe logic to ensure it behaves as expected.

### Search behavior changes

The [Search objects (v3)](/en/connectors/greenhouse/search-objects-v3) action replaces multiple v1 patterns. It uses different query parameters and supports different object coverage. Update your filters and queries accordingly.

### Object coverage differences

Object support differs between v1 and v3. Confirm that the objects used in your recipes are available before migration.

### Get object by ID

Greenhouse v3 doesn't include a direct equivalent for the [Get object by ID](/en/connectors/greenhouse/get-object-by-id-action) action. Use the [Search objects (v3)](/en/connectors/greenhouse/search-objects-v3) and filter by a comma-separated list of IDs.

## Migration timeline

| Date | Description |
| --- | --- |
| March 2026 | Greenhouse v3 support is available in Workato |
| August 15, 2026 | Complete migration to v3 |
| August 30, 2026 | Greenhouse removes v1 and v2 API support |

Complete migration by August 15, 2026 to allow time for testing before the final deadline.

---
