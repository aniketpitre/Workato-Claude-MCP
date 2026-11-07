---
url: 'https://docs.workato.com/en/connectors/pipedrive.md'
description: >-
  The Pipedrive connector lets you automate sales CRM workflows: create, update,
  search, and delete records and trigger recipes on new or updated records.
---

# Pipedrive

[Pipedrive](https://www.pipedrive.com/) is sales CRM and pipeline management software that helps small sales teams manage intricate or lengthy sales processes. It's built to be simple and easy to use, yet powerful.

> **CONNECTOR UPGRADE TO API V2**
> 
> Action required by July 31, 2026. Pipedrive is sunsetting a significant portion of its API v1 endpoints that Workato's Pipedrive connector currently relies on. Recipes using deprecated Pipedrive triggers, actions, or affected custom actions will stop functioning after this date. Refer to [Connector upgrade to API v2](/en/connectors/pipedrive/connector-upgrade-to-api-v2) for more information.

## Connection setup

The Pipedrive connector uses API token authentication.

### Pipedrive setup for API token authentication

Complete the following steps to retrieve credentials in Pipedrive:

1. Click your profile icon on your Pipedrive dashboard, then click **Personal preferences**.
   
2. Select the **API** tab.
   
3. Copy and save **Your personal API token** for use in Workato.
   

### Connect to Pipedrive with API token authentication

Complete the following steps to connect to Pipedrive in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Pipedrive` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Pipedrive connection](/assets/pipedrive-connection-setup.CKOYaeNm.png)_Pipedrive connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API token**. Refer to [Retrieve the API token](#pipedrive-setup) for more information.
   
6. Click **Connect**.

---

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

---
