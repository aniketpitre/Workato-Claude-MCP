---
url: 'https://docs.workato.com/en/features/project-properties-manage.md'
description: >-
  Create, edit, and delete project properties in Workato using the Project
  properties interface within a project's settings.
---

# Manage project properties

The **Project properties** interface enables you to perform the following actions:

- [Create a project property](#create)
- [Edit a project property](#edit)
- [Delete a project property](#delete)

## Create a project property

Complete the following steps to create a project property:

1. Go to **Projects**.
   
2. Select a project.
   
3. Go to **Settings > Project properties**.
   
4. Click **\+ Add new property**.
   
5. Enter a **Property name** and **Value**. Ensure the **Property name** is descriptive and unique.
   
6. Click **✓ Save** to save the property.
   
   ![Save new property](/assets/create.vvoJpbcD.png)_Save your project property_
   

> **DUPLICATE PROPERTY NAMES ERROR**
> 
> Ensure project property names are unique. If you attempt to create a project property with a name already in use within the same project, Workato displays a warning message and prevents you from saving it.
> 
> ![Duplicate names error](/assets/duplicate-names.DsIlAuGf.png)_Duplicate names error_

## Edit a project property

Complete the following steps to edit a project property:

1. Go to **Projects**.
   
2. Select a project.
   
3. Go to **Settings > Project properties**.
   
4. Hover over the last column of the property you plan to edit and click the **Edit** (pencil icon) when it appears. ![Pencil icon](/assets/edit.BqWOQKqw.png)_Click **Edit** (pencil icon)_
   
5. Edit the property.
   
6. Click **✓ Save** to save the changes. ![Save new property](/assets/create.vvoJpbcD.png)_Save your changes_
   

## Delete a project property

Complete the following steps to delete a project property:

1. Go to **Projects**.
   
2. Select a project.
   
3. Go to **Settings > Project properties**.
   
4. Hover over the last column of the property you plan to delete and click **Delete** (trash icon) when it appears.
   
5. Click **Delete**.
   
   ![Delete property](/assets/delete.CHGlwMWw.png)_Delete a project property_
   

> **DELETED ACTIVE PROJECT PROPERTIES ERROR**
> 
> When you delete a project property, recipes using the deleted property display a `Please replace invalid datapill(s)` error message. To resolve this error, replace or remap the invalid datapill with a valid one.
> 
> ![Project property deleted error](/assets/delete-move-error.BjBpcVcW.png)_Replace invalid datapills_

---
