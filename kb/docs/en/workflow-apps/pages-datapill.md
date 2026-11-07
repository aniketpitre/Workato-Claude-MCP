---
url: 'https://docs.workato.com/en/workflow-apps/pages-datapill.md'
description: >-
  Reference for using datapills in Workflow apps pages to build dynamic forms
  with user, request, project property, page component, and variable data.
---

# Use datapills in pages

Workflow apps enables you to use workflow-related data in your pages to create custom and dynamic forms that change in response to user input. This data is stored in the **Page data** modal, which is similar to the **datatree** in the recipe editor. You can use this modal to map datapills related to the application, page components, project properties, variables, and more. Workflow apps supports rendering datapill content in markdown.

Datapills enable you to create custom and personalized pages tailored to your users. You can also use datapills to [configure **IF** conditions](/en/features/conditions) to control the behavior of [page components](/en/workflow-apps/page-components), create dynamic URLs, and more.

![Map page data](/assets/page-data.Bf9ee2CN.png)_Map page data_

## Data source types

Workflow apps supports incorporating data from the following sources in datapills:

- **Users**: Access end-user profile data and attributes in your Workflow app.
- **Project properties**: Reference [project properties](/en/features/project-properties) to use shared configuration values across your Workflow apps. Project properties don't display in the **Page data** modal if your project doesn't contain them.
- **Requests**: Access data from the workflow request based on columns in your app's primary data table. Request datapills reflect current saved data and do not change based on user input or actions on your pages. Request data is available for applications with request and approval functionality only.
- **Page components**: Capture and use data collected from user interactions throughout the page.
- **Variables**: Map in [variables](/en/workflow-apps/component-actions/variables) populated with recipe output to display and manage information from other applications directly within your Workflow app.

> **DYNAMIC DATA SOURCES**
> 
> Project property, page component, and variable data depend on your configuration. You can verify the following information if the expected datapills don't appear in your **Page data** modal:
> 
> - Project properties: Ensure your project contains the necessary project properties
> - Page components: Ensure your page includes editable or conditionally editable components
> - Variables: Ensure variables are properly configured with recipe output

### User data

User data provides information about the end-user interacting with your Workflow app.

View user data

| Data | Description |
| --- | --- |
| User ID | The ID of an end-user of your Workflow app. |
| User name | The name of the end-user of your Workflow app. |
| User email | The email of the end-user of your Workflow app. |
| User groups | The groups the user belongs to. |
| Is assignee | Indicates whether the user is assigned to the request. |
| Guest user | Indicates whether the user is an anonymous user. |
| User context | Object containing information about the user. |
| Is on mobile (User context) | Indicates whether the user is using a mobile device. |
| Portal language (User context) | Indicates the user's language preferences in the Workflow apps portal. |

### Request data

Request data provides information about the workflow request and its current state. Available request data is based on the columns in your app's primary data table. Request data is available for applications with request and approval functionality only.

View request data

| Data | Description |
| --- | --- |
| Record ID | The unique identifier for the request record. |
| Application | Object containing information about your Workflow app. |
| Record ID (Application) | The unique identifier for the Workflow app. |
| Label (Application) | The display name of the Workflow app. |
| Created by | Object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| User groups (Created by) | The groups the user belongs to. |
| Guest user (Created by) | Indicates whether the user is an anonymous user. |
| Stage | Object containing information about the workflow stage. |
| Stage ID (Stage) | The unique identifier for the workflow stage. |
| Stage name (Stage) | The display name of the workflow stage. |
| Created at | The date and time the request was created. |
| Updated at | The date and time the request was updated. |

## Datapill compatibility

Workflow apps allows you to map datapills during the page editing stage. All fields that accept text input also accept datapills, with the following exception:

- **Placeholder** fields

Additionally, you can render datapill or variable content using Markdown if you map the information into the following page component:

- **Text block**

## Configure conditional statements

You can use datapills to configure conditional statements to control whether page components are editable, visible, or required only under the conditions you specify. For example, in an expense approval workflow, you might decide to make input fields editable only during a specific workflow stage. You might also decide to limit the visibility of particular components to a specific user. For example, if your workflow involves requiring users to upload receipts, you might decide that only a specific user, such as a supervisor within your organization, can view uploaded receipts.

Configuring an **IF** condition in Workflow apps is similar to adding an [IF condition](/en/features/conditions) to a recipe workflow.

Complete the following steps to set up an **IF** condition:

1. Select a component. Selecting a component opens the Properties panel (right panel).
   
   ![Open the properties panel](/assets/properties-panel.C0k6R2uh.png)_Open the Properties panel_
   
2. Use the **Page data** modal to map data related to app users, requests, and page components into your **IF** condition.
   
3. _Optional_. Click plus to add more **IF** conditions. You can chain multiple **IF** conditions using `AND` or `OR`. For example, you can configure a component to be editable by a specific user _only_ during a specific workflow stage.
   

## Render datapill content using markdown

You can render datapills or variables components using [markdown](https://daringfireball.net/projects/markdown/).

This enables you to:

- Visualize well formatted content dynamically
- Display responses from AI connectors with their native markdown applied
- Build lists dynamically in recipes and display them properly in your pages

## Examples

The following examples demonstrate how you can use datapills to customize your pages, create dynamic forms, and more.

- [Personalized page](#personalized-page)
- [Conditional visibility](#conditional-visibility)
- [Render datapill or variable content using markdown](#markdown-render)

### Personalized page

Datapills are particularly useful for customizing text fields to create pages that adapt to the current user.

The following example demonstrates how to map datapills into a page to create a personalized page that provides a summary of approved expense reimbursements. This example also uses datapills to summarize approved expenses by mapping page component data from data collected from user input.

Complete the following steps to create a personalized page:

1. Select a component. Selecting a component opens the Properties panel (right panel).
   
   ![Open the properties panel](/assets/properties-panel.C0k6R2uh.png)_Open the Properties panel_
   
2. Drag and drop one or more datapill(s) from the **Page data** modal into a field in the Properties panel.
   
   The following example demonstrates how to use datapills in a text field.
   
   ![Drag and drop datapills](/assets/datapill-personalization.mSXFOIeU.png)_Drag and drop datapills_
   
3. Click **Save** to save your changes.
   
4. Click **Preview** to open your page in preview mode.
   
5. Preview your page. You can test out how different data table records appear using the **Test preview using record {Name}** menu.
   
   ![Preview your page](/assets/datapill-personalization-preview.DBrTMqV5.png)_Preview your page_
   

### Conditional visibility

The following example uses conditional statements to make certain components visible and required based on how users fill out the page. In the following example, if the user clicks the `Check this box if you are submitting this form on another employee's behalf.` checkbox, additional input fields appear.

Complete the following steps to configure conditional visibility:

1. Select a component. When clicked, the Properties panel appears.
   
   This example applies this setting to a **container** component.
   
2. Set **Visible** to **Conditional**.
   
   Components nested within **container** components inherit the parent container's visibility settings. This means that all inputs (`Employee name`, `Employee email`, `Employee title`, `Employee's supervisor`, and `Employee's department`) inside of this container are also conditionally visible. You do not need to configure an **IF** condition for each component to update their visibility. However, if you plan to make the editability or required status of these components conditional, you must update them on an individual basis.
   
   ![Set visibility to conditional](/assets/conditional-visibility.DId8HOA3.png)_Set Visibility to Conditional_
   
3. Drag and drop relevant datapills from the **Page data** modal into the **Data** field.
   
   ![Map page data](/assets/conditional-visibility-2.D5bVUBcp.png)_Map page data_
   
4. _Optional_. Click **+** (plus) to chain additional **IF** conditions using **AND** or **OR**.
   

### Render datapill content using markdown

The following example renders datapill content using Markdown in the Workflow apps portal.

Complete the following steps to render datapill or variable content using Markdown:

1. Use the **Page data** modal to select a datapill or variable and map it into a **text block** component. Alternatively, you can select an existing datapill or variable already mapped into a **text block**.
   
2. Click the **...** (ellipses) on the **text** menu and click **Render markdown in datapill** to toggle between raw text and rendered Markdown.
   
   ![Render datapill using markdown](/assets/markdown-datapill.D5HPg17i.png)_Render datapill or variable content using markdown_
   

Datapill or variable content is rendered using markdown in the Workflow apps portal:

![Content rendered using markdown](/assets/markdown-datapill-rendered.CJOlywUD.png)_Variable content rendered using Markdown in the Workflow apps portal_

---
