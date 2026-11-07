---
url: 'https://docs.workato.com/en/connectors/zendesk/custom-objects.md'
description: >-
  Learn how Zendesk custom objects work in Workato, letting you create, read,
  update, and delete objects not native to Zendesk.
---

# Zendesk - Custom objects

Zendesk allows you to create custom objects to model, store, and retrieve objects that are not native to Zendesk (for example, Tickets, Users, Organization). Custom objects can be configured to suit your various use-cases.

Workato allows you to interact with custom objects in the same way you interact with native Zendesk objects. You can create, read, update, and delete custom objects through recipe actions.

> **LEGACY CUSTOM OBJECTS SUNSET**
> 
> Zendesk removed legacy custom objects, relationships, and records on July 27, 2026, in favor of its current custom objects platform. Refer to [Zendesk's announcement](https://support.zendesk.com/hc/en-us/articles/9156194392730-Announcing-the-removal-of-legacy-custom-objects) for details. The custom object record actions in this connector now use the current Custom Objects API by default for new recipes. Refer to [Custom relationships](#custom-relationships) for the status of the relationship record actions.

You can access custom objects control in your Zendesk instance by clicking **Objects and rules** in the Admin Center sidebar, then selecting **Custom objects** > **Objects**.

### Custom objects

You can view your custom object types in the **Objects** tab.

After configuring your custom object type, you can proceed to [create records](/en/connectors/zendesk/create-custom-object-record-action), [get records](/en/connectors/zendesk/get-custom-object-record-by-id-action), [update records](/en/connectors/zendesk/update-custom-object-record-action), and [delete records](/en/connectors/zendesk/delete-custom-object-record-action) through recipe actions.

### Custom relationships

Legacy custom relationships connect two custom objects, or a custom object and a Zendesk object. For example: `Zendesk:user`.

> **DEPRECATED**
> 
> The [Create relationship record](/en/connectors/zendesk/create-relationship-record-action), [Get relationship records](/en/connectors/zendesk/get-relationship-records-action), and [Delete relationship record by ID](/en/connectors/zendesk/delete-relationship-record-by-id-action) actions are deprecated due to the sunset of their underlying Zendesk endpoints. Existing recipes that use these actions continue to run unchanged. These actions are no longer available when you add a new step to a recipe.

Refer to [Zendesk's custom objects documentation](https://support.zendesk.com/hc/en-us/articles/5914453843994-Understanding-custom-objects) for more information on Zendesk custom objects.

---
