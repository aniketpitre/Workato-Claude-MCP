---
url: 'https://docs.workato.com/en/workflow-apps/component-actions.md'
description: >-
  Learn how Workflow apps component actions respond to button clicks, page
  loads, and other UI events to run recipes and complete tasks.
---

# Component actions

Component actions in Workflow apps provide a dynamic and interactive user experience by enabling real-time responses to UI events such as button clicks, page loads, drop-down value changes, and table row selections. This enables users to complete a range of tasks, including:

- **Run recipe**: Allow users to complete tasks that involve external systems directly within the app interface
- **Reset/reload components**: Clear component values or reload a component after an action is taken
- **Open a webpage**: Direct app-users to a specific URL
- **Complete a task**: Review, approve, and complete requests within the Workflow apps portal
- **Save data to table**: Save request and approval data in a data table
- **Set value**: Configure a value for a variable or page component

## Compatible components

Specific page components have the **Action** property which enables you to define the action to take within the page editor. The following table describes available actions and compatible components:

| Action | Trigger events | Compatible components |
| --- | --- | --- |
| **Run recipe** | Button click, Drop-down value change, File value change, Page load, Table row selection | **Button**, **Single-select drop-down**, **Multi-select drop-down**, **File**, **Page** (on page load), **Table** |
| **Reset/reload components** | Button click, Drop-down value change, File value change, Table row selection | **Button**, **Single-select drop-down**, **Multi-select drop-down**, **File**, **Page** (on page load), **Table** |
| **Open a webpage** | Button click | **Button** |
| **Complete task** | Button click | **Button** |
| **Save data to table** | Button click | **Button** |
| **Set value** | Button click, Drop-down value change, File value change, Page load, Table row selection | **Button**, **Single-select drop-down**, **Multi-select drop-down**, **File**, **Page** (on page load), **Table** |

The **Compatible components** column lists the components you configure to perform the action. **Set value** actions set the value of a different component. Refer to [Set value compatible components](/en/workflow-apps/component-actions/set-value#compatible-components) for the components whose values a **Set value** action can target.

## Default actions

Button components must have a defined action. All other component actions have a default state of **Do nothing**. This means that you must configure components to respond to user actions.

## Follow-up actions

You can configure one of the following follow-up actions to run after a primary action, such as a [Run recipe action](/en/workflow-apps/component-actions/run-recipe), completes:

- [Reset/reload components](/en/workflow-apps/component-actions/reset-components)
- [Set value](/en/workflow-apps/component-actions/set-value)

The default is **Do nothing** if you don’t configure a follow-up action.

---
