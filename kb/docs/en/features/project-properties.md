---
url: 'https://docs.workato.com/en/features/project-properties.md'
description: >-
  Learn how project properties store name-value configuration parameters scoped
  to a single Workato project for use across recipes and Workflow apps.
---

# Project properties

Project properties are name-value pairs that store configuration parameters for a single project. Project properties are available in the **Properties** datatree of all recipes within the project. You can also access project properties in the **Page data** modal of the Workflow apps page editor.

Project properties are useful for complex deployment models across connections, recipes, and Workflow apps. For example, you can define a property that indicates a notification contact email. All recipes or Workflow app pages within the same project where the project properties exist can look up this value from the datatree and send an email to the same recipient.

Project properties are distinct from [environment properties](/en/features/account-properties) in that their scope is narrower. Environment properties are globally available within your Workato account, while project properties are available only at the project level in the specific project where you create and maintain them.

> **PROJECT PROPERTY JOB EXECUTION BEHAVIOR**
> 
> [Jobs](/en/recipes/jobs#recipe-jobs) do not dynamically detect and update changes to project property values. Project property values are frozen at the beginning of job execution by design. You can use [Lookup tables](/en/features/lookup-tables#lookup-tables) if you require dynamic detection for project property values.

You can hide sensitive properties from common access by reducing the scope of users able to access projects containing sensitive properties.

## Permissions

Workato enables you to set granular permissions for both project properties and environment properties using [role-based access control](/en/user-accounts-and-teams/role-based-access/#how-role-based-access-control-works) (RBAC) by creating a custom role.

Project property permissions are available in **Workspace admin > Access control > Project roles > + Add project role**.

![Project properties permissions](/assets/privileges-project-properties.BIKZI3CS.png)_Project properties privileges_

Learn more about [Project privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-privileges).

## Quotas

Project properties are subject to the following quotas:

| Description | Quota |
| --- | --- |
| Maximum number of project properties per project | 1,000 |
| Maximum length of project property name | 100 characters |
| Maximum length of project property value | 1,024 characters |

> **FURTHER READING**
> 
> Refer to the following guides to learn how to implement project properties:
> 
> - [Manage project properties](/en/features/project-properties-manage)
> - [Use project properties in recipes](/en/features/project-properties-use-in-recipes)
> - [Access project properties in Workflow apps](/en/workflow-apps/pages-datapill)
> - [Project properties FAQ](/en/features/project-properties-faq)

---
