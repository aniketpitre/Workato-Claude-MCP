---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-enhance-bulk-action-migration.md
description: >-
  Learn how to migrate NetSuite recipes from deprecated bulk actions to the
  enhanced NetSuite bulk actions for faster ingestion and job completion.
---

# Netsuite SOAP - Migrating to our newly enhanced NetSuite bulk actions

A new set of bulk actions for the NetSuite connector have been released that provide better ingestion performance and job completion speeds. Due to this, existing bulk actions for NetSuite have been deprecated in favor of these new actions. Existing recipes that use these deprecated actions still work, but we recommend that you migrate your recipes during the regular maintenance of NetSuite automations.

The following actions were affected:

- Create standard records in bulk
- Update standard records in bulk
- Upsert standard records in bulk
- Create custom records in bulk
- Update custom records in bulk

## Why did we do this?

NetSuite's bulk actions are used when you need many records moved and record ingestion is critical for your workflow to complete. When you imagine moving millions of records for during a one time migration or weekly bulk load of data, its important that your recipes are able to do this efficiently.

## What was improved to achieve this?

Workato's Netsuite bulk actions use Netsuite's asynchronous processing queues to load batches of records into a ingestion queue on the NetSuite side. Previously, our connector would check every 5 minutes to understand if the batch of records was ingested. This meant a delay of a minimum of 5 minutes before Workato would send the next batch of records.

Now, Workato's enhanced set of bulk actions utilize new capabilities to reduce the time interval for the first check to 30 seconds. Most batches of lightweight records are expected to finish within that time. After the first check, intervals between subsequent checks are slowly increased.

## Migrating to new bulk actions

With these release of these new bulk actions, we have decided to deprecate our legacy bulk actions. Any recipes using our legacy bulk actions will continue to work as per normal. We strongly recommend that you migrate over to our new bulk actions during the regular upgrades to your Netsuite recipes.

1. To migrate, simply head over to the recipe with the legacy Netsuite bulk action. You will be able to see the "Deprecated" tag next to the action to differentiate them from our newly enhanced bulk actions with the same name.
   
   ![Deprecated Bulk Netsuite record](/assets/deprecated-bulk-action.CITY0cP-.png)
   
2. After selecting the action in the recipe editor, simply head over to the action selection tab and search for the corresponding bulk action.
   
3. Select this new action and all existing configurations for both input fields and output datapills will be preserved in your recipe.
   
4. Continue to do this for other deprecated bulk actions as needed.
