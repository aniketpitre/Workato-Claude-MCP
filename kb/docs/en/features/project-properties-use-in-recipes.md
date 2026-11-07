---
url: 'https://docs.workato.com/en/features/project-properties-use-in-recipes.md'
description: >-
  Use project properties as datapills in Workato recipes within their scope by
  mapping them from the Recipe data menu into input fields.
---

# Use project properties in recipes

Project properties are accessible as datapills in recipes within their [scope](#project-property-scope).

Complete the following steps to use project properties in a recipe:

1. Click **Recipe data** to expand the **Recipe data** menu.
   
2. Go to **Recipe data > Properties > Project properties**.
   
3. Map the project property datapill to the appropriate input field. For example, you can map a project property named Admin email to the **To** field in a Gmail action to specify the email recipient.
   
   ![Project properties in datatree](/assets/datatree.B7oymDm-.png)_Project properties are a child element of the Properties datatree_
   

## Project property scope

Project properties are not accessible outside of the project folder you define them in. To create properties with a larger scope, use [Environment properties](/en/features/account-properties), which are accessible from all recipes within your workspace.

> **RECIPE MOVE ERROR**
> 
> If you move a recipe that uses project properties to a folder outside the project where the properties were originally defined, the recipe will display a `Please replace invalid datapill(s)` error message. To resolve this error, replace or remap the invalid datapill with a valid one.
> 
> ![Replace invalid datapills](/assets/delete-move-error.BjBpcVcW.png)_Replace invalid datapills_

---
