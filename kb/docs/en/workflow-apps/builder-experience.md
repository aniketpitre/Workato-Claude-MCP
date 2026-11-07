---
url: 'https://docs.workato.com/en/workflow-apps/builder-experience.md'
description: >-
  Learn how Workflow apps define data sources, interface, and business logic
  using Workato recipes, data tables, and app settings.
---

# Builder experience

Workflow apps are built using a set of features that allow you to define your app’s data, interface, and business logic.

## Data sources

Workflow apps integrate seamlessly with your business applications using Workato recipes and [data tables](/en/data-tables). You can use these sources independently or together, depending on your use case.

- **Generic apps**  
  Generic apps, or apps without request and approval functionality, use recipes to connect directly to external systems and can pull in live or contextual data when required. Some apps rely primarily on recipes to display or process information dynamically.
  
  - Populate components like [drop-downs](/en/workflow-apps/dropdown-recipe-data-source) and [tables](/en/workflow-apps/table-recipe-data-source) with external data
  - Retrieve, send, and manipulate data across connected applications in real-time
- **Request and approval apps**  
  Apps with request and approval functionality use data tables as a primary data source. You can also use recipes alongside data tables to sync or enrich stored data.
  
  - Store and manage structured records in a primary data table
  - Define relationships between related data sets using linked tables

* * *

## App settings

The **Workflow app** tab provides access to app-level settings and a centralized view of all components that comprise your Workflow app.

Use this interface to complete the following tasks:

- Manage and organize assets including [data tables](/en/data-tables), [pages](/en/workflow-apps/pages-create), and [recipes](/en/recipes)
- Define relationships and connections across assets
- Configure permissions and control access to the app

Refer to the [app settings guide](/en/workflow-apps/app-settings) to learn how to set up your Workflow app.

* * *

## Verified user access

Verified user access uses [runtime user connections](/en/features/runtime-user-connections) to allow end users to authenticate with their own credentials when using a Workflow app. This means that recipes perform actions using each user's individual identity and permissions.

You can use verified user access with the following Workflow apps recipe types:

- **Data population recipes** Populate [table](/en/workflow-apps/table-recipe-data-source) and [drop-down](/en/workflow-apps/dropdown-recipe-data-source) components with data scoped to the end user's permissions in the external system.
- **Component event (Run recipe action) recipes** Perform actions in external apps using [Run recipe actions](/en/workflow-apps/component-actions/run-recipe) with the end user's permissions in that app.

* * *

## Pages

Pages define how users interact with your app and are used to build custom interfaces for submitting requests, reviewing tasks, and viewing dashboards.

You can design Pages using a drag-and-drop editor:

- Build layouts with configurable [components](/en/workflow-apps/page-components)
- Assign pages to [workflow stages](/en/workflow-apps/interface#pages-assign)
- [Prefill fields using URL parameters](/en/workflow-apps/prefill-forms)
- Publish pages as [public forms](/en/workflow-apps/public-links) for unauthenticated submissions

* * *

## Page components

Page components are the building blocks of a Page.

You can use Pages to capture user input, display information, and respond to user behavior:

- Add inputs, display blocks, buttons, tables, and more to your apps
- Control visibility and editability using conditional logic using IF statements
- Apply [built-in validation](/en/workflow-apps/built-in-field-validation) rules or define [custom validation](/en/workflow-apps/custom-field-validation) using regex
- Configure [properties](/en/workflow-apps/page-properties) like default values, labels, and formatting

* * *

## Component actions

Component actions define how your app responds to user interactions:

- [Run recipes](/en/workflow-apps/component-actions/run-recipe) to drive business logic
- [Reload page components](/en/workflow-apps/component-actions/reset-components)
- [Navigate to external URLs](/en/workflow-apps/component-actions/open-webpage)
- [Complete workflow tasks](/en/workflow-apps/component-actions/complete-task)
- [Save user input to a data table](/en/workflow-apps/component-actions/save-data)

* * *

## Variables

[Variables](/en/workflow-apps/component-actions/variables) store temporary data that can change based on user input, recipe output, or page state.

Use variables to achieve the following:

- Populate values dynamically during user interaction
- Display content based on live data from recipes
- Pass information between components

* * *

## Workflow apps connector

The [Workflow apps connector](/en/workflow-apps/workflow-apps-connector) allows you to manage business logic and orchestrate processes using [workflow recipes](/en/recipes#what-types-of-recipes-can-i-create).

Use the connector to:

- Start workflows using the [New request trigger](/en/workflow-apps/workflow-apps-connector/new-request-trigger)
- Update or search data records using [Update request](/en/workflow-apps/workflow-apps-connector/update-request-action) and [Search requests](/en/workflow-apps/workflow-apps-connector/search-requests-action) actions
- Assign tasks to users using the [Assign task to users](/en/workflow-apps/workflow-apps-connector/assign-task-to-users-action) action

---
