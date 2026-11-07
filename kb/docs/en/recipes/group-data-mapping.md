---
url: 'https://docs.workato.com/en/recipes/group-data-mapping.md'
description: >-
  Learn how to use group data mapping in Workato to automatically map recipe
  fields when field names match datapill names across many fields.
---

# Group Data Mapping

Group data mapping is a useful feature that enables the automatic mapping of fields based on matches between the field name and datapill name. This is especially helpful when there are a large number of fields that need to be mapped, such as in database application.

Get the quick version in this video!

[Video](https://www.youtube.com/embed/_nncrLSYIZU?rel=0&rel=0)

This feature allows you to map fields one-to-one in a recipe step from a selected data source.

> **LIMITATIONS**
> 
> Group data mapping does not support map input data for `Execute ruby code` or `Execute JavaScript code`.

## Activate the group mapping wizard

Group data mapping is available for all recipe actions, excluding the trigger. Complete the following steps to use group mapping:

1. Expand the recipe step you plan to map.
   
2. Click the **group mapping** icon to activate the group mapping wizard.
   
   ![expand step to be mapped](/assets/expand-step-group-mapping-icon.DZ6yXxpp.gif)_Activate the group mapping wizard_
   

## Select the field group and data source

The group mapping wizard displays the fields and field groups available for mapping and the available data sources. These data sources are similar to the app data you use in recipe building.

Field groups are fields that appear as nested fields in the recipe UI, and follow the object structure you have in your application. You may select either all fields in a step (including nested fields) or a specific field group. The following image uses the nested fields **Bill** to and **Ship to**:

![field groups](/assets/field-groups.Cr2jxcIW.png)_An example of fields and field groups within an action_

1. Select the fields you plan to map.
   
2. Select the data source for the datapills from your Environment properties, including the trigger and all preceding recipe steps. You can map from either the output of an entire step or a nested array within it.
   
3. Review the wizard to confirm that display options match your selections and then click **Next**.
   

## How data sources and fields are matched

In the current iteration, the system determines matches between data sources and fields based on the **name/label** and **API name** of both the field to be mapped and the datapills from the data source.

- Matches are case-insensitive
- Matches ignore underscores and spaces
- All data types (string, integer, boolean, and so on) can be matched to each other, but arrays cannot be mapped to non-arrays
- The pill label and API name will be matched to the field label or API name
- The match has to be an exact match minus underscores, spaces, and case

### Examples

The following examples refer to the field and datapill labels:

| **Field** | **Datapill** | **Match?** | **Explanation** |
| --- | --- | --- | --- |
| Account name | Account name | Yes | Exact match |
| ACCOUNT NAME | account name | Yes | Case is ignored |
| account\_name | accountname | Yes | Underscores and spaces are ignored |
| Account\_name | accountname\_c | No | accountname\_c has an extra character 'c' |

## Data mapping preview

The second screen in the wizard displays fields successfully matched with datapills sharing the same name and data type. Complete the following steps to apply these mappings:

1. Review the field and datapill mappings to ensure the selections are correct.
   
2. Select the checkboxes for the fields you plan to map. You can deselect fields that you don't plan to map.
   
   ![mapping preview](/assets/mapping-preview.Y82pUp3L.png)_Data mapping preview_
   
3. Click the **Apply mappings** button to map the datapills to the fields you selected. You can edit these mappings in the recipe.

---
