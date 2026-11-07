---
url: 'https://docs.workato.com/en/oem/dynamic-field-mapping.md'
description: >-
  Dynamic field mapping lets Embedded partners configure recipes so customers
  map source and destination fields outside the recipe builder.
---

# Dynamic field mapping

Dynamic field mapping lets Embed partners configure recipes to support mappings between third-party systems. Embedded customers can map fields outside the recipe builder, typically within the partner's platform. This feature enables end customers to map standard or custom fields from a source step to a destination step without modifying the core recipe logic.

> **FEATURE AVAILABILITY**
> 
> Contact your Customer Success Manager to enable the dynamic field mapping feature or to discuss your operational requirements.

Dynamic field mapping consists of two main components:

- **Dynamic mapping recipe configuration**: A toggle within each recipe action step enables field mapping for that step. Select a preceding step as the source for mapped data. Each action in a recipe can use dynamic mapping across all connectors.

![Dynamic field mapping](/assets/dynamic-field-mapping.DlQTvlRR.png)_Dynamic field mapping in the recipe editor_

- **Field map schemas and [field map introspection APIs](/en/oem/oem-api/dynamic-field-mapping)**: A field map schema defines the mapped fields in JSON format. Each action step with dynamic mapping has a unique schema. You can use these APIs to retrieve introspection data, fetch source and target schemas, and update field map schemas. This enables partners to build a custom mapping interface within their products.

![Field map schema](/assets/schema-field-mapping.CNNqZTcN.png)_Field map schema_

## Set up dynamic field mapping

Complete the following steps to set up dynamic field mapping:

1. Open your Embed admin workspace to create a recipe you plan to distribute to multiple customers, or go to a customer workspace to create a recipe for a specific customer.
   
2. Select the action step where you plan to apply dynamic field mapping, then click the **Use dynamic mapping** toggle.
   
3. Select the prior step you plan to use in the recipe as the **Source**.
   
   > **DYNAMIC MAPPINGS OVERRIDE STATIC MAPPINGS**
   > 
   > You must map all required fields before you start the recipe. Once you set a field map schema, the recipe uses those mappings at runtime instead of any static mappings defined in the builder.
   
4. Repeat the preceding steps for additional action steps. You can view the field map schema for each step to confirm the field mappings and identify the field map ID.
   

You can use the [prebuilt dynamic field mapping widget](/en/oem/workato-embedded-implementation#dynamic-field-mapping-widget) or the [field map introspection APIs](/en/oem/oem-api/dynamic-field-mapping) to build the mapping interface after you enable dynamic field mapping in your recipes.

## Roles and permissions

Users with the system **Admin** role can use this feature by default. For custom roles, you must update your permissions to grant access.

![Required role permissions](/assets/roles-and-permissions.CK0ERBhO.png)_Required role permissions_

## Create your own mapping experience

Choose one of the following methods to support dynamic field mapping in your embedded integration:

- [Use the prebuilt dynamic field mapping widget](#use-the-prebuilt-dynamic-field-mapping-widget)
- [Build your own widget with APIs](#api-access)

### Use the prebuilt dynamic field mapping widget

Use the prebuilt widget to embed dynamic field mapping in your product with minimal configuration. This widget includes the mapping logic and user interface, which removes the need to create a custom solution.

Refer to the [Construct the URL by iframe type](/en/oem/workato-embedded-implementation#configure-mapping-widget) section for configuration steps.

### Build your own widget with APIs

Use the following API endpoints to build a custom mapping interface:

- Field maps introspections in recipe | `GET /api/v2/managed_users/:managed_user_id/recipes/:id/field_map_introspections`
- Field maps introspection | `GET /api/v2/managed_users/:managed_user_id/recipes/:id/field_map_introspections/:id`
- Update Field maps introspection | `PUT /api/v2/managed_users/:managed_user_idrecipes/:id/field_map_introspections/:id`
- Refresh recipe's schema for Field maps introspection | `POST /api/v2/managed_users/:managed_user_id/recipes/:id/field_map_introspections/:id/refresh_schema`
- Fetch pick\_list for recipe's Field maps introspection | `POST /api/v2/managed_users/:managed_user_id/recipes/:id/field_map_introspections/:id/pick_list`

![Field mapping endpoints](/assets/field-mapping-apis.C2Bi3nXL.png)_Required fielding mapping endpoints_

Update your API client roles to include these endpoints if they require access to the dynamic field mapping feature.

> **ENDPOINTS FOR ADMIN WORKSPACE AND CUSTOMER WORKSPACES**
> 
> Select all field map introspection endpoints under both **Your workspace** and **Customer workspaces**.

## Considerations for dynamic field mapping

Dynamic field mapping supports adjustments to most field types. Consider the following factors when you build your mapping experience:

- **Complex data structures**: Dynamic field mapping doesn't support array fields or complex data transformations.
- **Schema integrity**: The platform blocks mappings that significantly alter the schema, such as fields marked with `extends_schema: true`. This ensures data consistency and integration stability.
- **Mapping types**: Supported mapping types include `map`, `static`, `nullify`, and `skip`.
- **Decoupled logic**: Recipe lifecycle management supports the export and import of dynamic field mapping configurations. However, field map schemas are excluded from manifests. The field map ID remains consistent across new recipe versions imported with recipe lifecycle management.
- **Audit activity**: All updates to field map schemas appear in the workspace's activity audit log.
- **Join points**: Dynamic field mapping doesn't surface data connected through join points. Join points are only present in the following connectors: `active_reg_online`, `bamboohr`, `bill`, `fresh_desk`, `infusionsoft`, `intacct`, `quickbooks`, `replicon`, `salesforce`, `service_now`, `tsheets`, and `zendesk`.

---
