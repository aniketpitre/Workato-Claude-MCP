---
url: >-
  https://docs.workato.com/en/connectors/pipedrive/connector-upgrade-to-api-v2.md
description: Pipedrive connector upgrade to API v2 notice and instructions.
---

# Connector upgrade to API v2

Pipedrive is sunsetting a significant portion of its API v1 endpoints that Workato's Pipedrive connector currently relies on. To align with this change, we've introduced new triggers and actions based on API v2 and marked the affected v1-based triggers and actions as deprecated. This also affects custom actions that call the deprecated v1 endpoints directly. You'll need to migrate those separately.

Pipedrive sunsets these endpoints on July 31, 2026. After that date, deprecated triggers, actions, and affected custom actions stop working. Recipes using them need to be updated to avoid unexpected behavior.

## Prevent recipe impact

Update each affected recipe before July 31, 2026. Affected recipes include any that use a deprecated trigger, deprecated action, or custom action that calls a deprecated endpoint. Complete the following steps to update the recipes:

1. Open each affected recipe and locate the impacted trigger, action(s), or custom action(s). Deprecated triggers and actions are labeled **Deprecated**. The **Deprecated** label is only displayed when a recipe is edited, not when it's viewed.
   
   ![Pipedrive deprecated label](/assets/pipedrive-deprecated-label.Cym47VZH.png)_Pipedrive deprecated label_
   
2. Replace them with their v2 equivalents using the table below.
   
3. If the recipe uses custom actions that call Pipedrive API v1 endpoints directly, update those endpoints to their v2 equivalents. Refer to the [Pipedrive API v2 migration guide](https://pipedrive.readme.io/docs/pipedrive-api-v2-migration-guide) for the full list of changes. You'll need to use the absolute URI, as the connector's default base URI still points to v1.
   
4. Review all downstream actions to confirm datapills are still valid and adjust as needed.
   

Contact your Customer Success Manager or [Workato Support](https://support.workato.com/en/support/login) for assistance.

| Deprecated trigger/action | Replacement trigger/action |
| --- | --- |
| Trigger: **New object API v1**. These objects are deprecated: Activity, Deal, Organization, Person, Pipeline, Product, Stage This trigger still supports these objects: Activity Type, Note, and User. | The **New object (batch)** trigger supports the deprecated objects. |
| Trigger: **New/updated object API v1**. These objects are deprecated: Activity, Deal, Organization, Person, Pipeline, Product This trigger still supports these objects: Activity Type, Note, and User. | The **New/updated object (batch)** trigger supports the deprecated objects. |
| Trigger: **New/updated object API v1 (batch)**. | Trigger: **New/updated object (batch)**. |
| Action: **Create activity API v1**. | Action: **Create activity**. |
| Action: **Create deal API v1**. | Action: **Create deal**. |
| Action: **Update deal API v1**. | Action: **Update deal**. |
| Action: **Create organization API v1**. | Action: **Create organization**. |
| Action: **Update organization API v1**. | Action: **Update organization**. |
| Action: **Update person API v1**. | Action: **Update person**. |
| Action: **Get deal-related products API v1 (batch)**. | Action: **Get deal-related products (batch)**. |
| Action: **Get object API v1 (batch)**. These objects are deprecated: Activity, Deal, Organization, Person, Pipeline, Product, Stage This action still supports these objects: Activity Type, Note, and User. | The **Get object (batch)** action supports the deprecated objects. |
