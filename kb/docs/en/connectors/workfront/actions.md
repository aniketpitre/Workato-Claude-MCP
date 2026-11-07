---
url: 'https://docs.workato.com/en/connectors/workfront/actions.md'
description: >-
  Actions in the Workfront connector that let you create, update, and search
  objects, including those with custom forms attached.
---

# Workfront - Actions

Workfront actions allow you to pull or push data into Workfront during a recipe.

The Workfront connector supports the following **user** actions:

- [Create object](#create-object)
- [Update object](#update-object)
- [Search objects](#search-objects)

* * *

## Create object

This action allows you to create objects in Workfront. You can also select custom forms to create objects with custom forms attached to them.

![Create object](/assets/create-object.C2s2FC-t.png)_Create an object in Workfront_

| Input field | Description |
| --- | --- |
| Object | The object you want to create. |
| Custom form | The custom forms you want to attach to the object you create in Workfront. This must be configured to work with custom fields. New input fields and output datapills will be generated based on your selection. |
| Object-specific input fields | The possible input fields based on the object you have selected as well as the custom fields you have selected. |

| Output datapills | Description |
| --- | --- |
| Object-specific output datapills | The possible datapills based on the object you have selected as well as the custom fields you have selected. |

* * *

## Update Object

This action allows you to update objects in Workfront. You can also select custom forms to update the custom forms attached to these objects or attach entirely new custom forms.

![Update object](/assets/update-object.C1eX3W7Q.png)_Update an object in Workfront_

| Input field | Description |
| --- | --- |
| Object | The object you want to update. |
| Custom form | Select the custom forms that contain the custom fields you want to update in Workfront. If you select a custom form which has not been assigned to the object, it will automatically be created. |
| Object-specific input fields | The possible input fields based on the object you have selected as well as the custom fields you have selected. |

| Output datapills | Description |
| --- | --- |
| Object-specific output datapills | The possible datapills based on the object you have selected as well as the custom fields you have selected. |

> **Clearing out the field values**
> 
> In cases where you want to remove values in a Workfront object, you will need to use the `clear` in formula mode.
> 
> ![Clear values](/assets/clear-values.DDhyCNnD.png)

* * *

## Search objects

Search objects in Workfront. This action allows you to search for any object in Workfront.

![Search objects](/assets/search-objects.DMFY_3Cq.png)_Search for objects in Workfront_

| Input field | Description |
| --- | --- |
| Object | The object you want to search for. |
| Custom form | The custom forms to be returned from Workfront. Leave blank to return all custom fields in all custom forms. |
| Filter condition | Search Workfront objects using Workfront filter syntax. When using filter conditions, search parameters given in input fields below are ignored. [Learn more about filter conditions.](https://one.workfront.com/s/article/API-Basics-638808549#using-search-modifiers) |
| Object-specific input fields | The possible input fields based on the object you have selected as well as the custom fields you have selected. When searching using input fields, we execute a search to retrieve all records that **contain** your search terms. For stricter results, use filter conditions. |

| Output datapills | Description |
| --- | --- |
| Object-specific output datapills | The output of this action is a list of objects. Each object contains datapills based on the object you have selected as well as the custom fields you have selected. |

* * *

---
