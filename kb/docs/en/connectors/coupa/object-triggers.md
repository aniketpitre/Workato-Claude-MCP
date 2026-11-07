---
url: 'https://docs.workato.com/en/connectors/coupa/object-triggers.md'
description: >-
  The New/updated object trigger in the Coupa connector polls your instance and
  fires when objects are created or updated, with optional trigger conditions.
---

# Coupa - Object triggers

Coupa triggers continuously poll your Coupa instance and trigger recipes based on new/updated objects on Coupa. These can be used with Coupa objects supported by Workato. Refer to the [Objects](/en/connectors/coupa#objects) section for more information.

**Object triggers available in Workato**

- `New/updated object`

* * *

### Input fields for object triggers

The only required input field to set up Coupa triggers is the object which you plan Workato to poll for. You can set the last time to pull Coupa events from when you start the recipe. This allows you to pull events retrospectively.

#### Trigger conditions

Trigger conditions are like filters in Workato. Turning on trigger conditions in Workato means that you can selectively choose which events you want to trigger workflows. Conditions can be set on object attributes like approval status. This allows you to build workflows that are only triggered on things such as approved purchase orders or invoices.

### New/updated object

This action continuously polls for recently created or updated objects since the previous poll. When Workato finds newly created or updated objects, it checks whether it fulfills the trigger conditions and executes a new job run for each object it finds.

### Output fields for object triggers

Each new or updated object triggers a separate run. You can then use the output datapills in subsequent steps in your recipe. This trigger in Workato retrieves all object-related information including custom fields. Custom fields are also useful to store the IDs of this same record which exist in other applications. For example, creating a custom field for an invoice in Coupa which stores the same invoice's ID in NetSuite allows you to quickly find and update that invoice in NetSuite based on the ID.

---
