---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/set-value.md'
description: >-
  Configure a Set value action as a primary or follow-up to populate a page
  component or variable in a Workflow app.
---

# Set value

**Set value** actions set the value of a page component or variable, either as the primary action or as a follow-up after another action.

## Compatible components and data

You can configure a **Set value** action on any component that supports component actions. Refer to [Compatible components](/en/workflow-apps/component-actions#compatible-components) for the list of components and trigger events.

**Set value** can target any component type except **Text block**, **Divider**, **Container**, **Button**, **Image**, and **Table** components.

You can set the value for components or variables using the following data, accessible in the data tree:

- User
- Request
- Variables
- Page components

## Set a page component or variable value

Complete the following steps to configure a **Set value** action:

> **INFO**
> 
> Use the **Follow up action** drop-down instead of **Action** when configuring **Set value** as a follow-up to another action.

1. Select a component compatible with **Set value** actions, such as a **page**, **drop-down**, **table**, **button**, or **file**.
   
2. Go to the **Action** panel.
   
3. Use the **Action** drop-down menu to select `Set value`.
   
4. Go to the **Elements to set** section and use the **Element** drop-down menu to select an element, such as a page component or variable.
   
   ![Select element](/assets/element-set.oWDNET3Y.png)_Select element_
   
5. Use the **Page data** modal to map data into the **Value** field. Alternatively, enter the value directly.
   
   ![Set value](/assets/value-set.ER97D9O9.png)_Set a component or variable's value_
   
6. Click **Save**.

---
