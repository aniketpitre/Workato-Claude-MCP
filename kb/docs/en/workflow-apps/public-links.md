---
url: 'https://docs.workato.com/en/workflow-apps/public-links.md'
description: >-
  Create public submission forms in Workflow apps to collect requests and
  reports from users without a Workflow apps account.
---

# Public submission forms

Workflow apps enables you to create public submission forms. This allows you to collect submissions and requests from users that don't have a Workflow apps account. This feature is useful in scenarios where you plan to share the link with a broader audience outside of your app users. For example, you can host a publicly available form on your website, send a link to a form through email, or collect submissions from a broad audience outside your organization.

![Public form](/assets/public-form.C2l6AyZO.gif)_Public form_

## Use cases

The following use cases provide examples of how you can use this feature to address your business objectives.

**Intake requests**

### Intake requests from unauthenticated users

Share request forms that unauthenticated users can access and fill out without signing in. This is particularly useful for collecting information from external stakeholders, customers, or prospective employees. For example, you can use public forms to complete pre-hiring processes. Additionally, you can [prefill form content](/en/workflow-apps/prefill-forms), allowing users to review and confirm pre-populated information.

![New client intake form](/assets/new-client-intake.zs5wpQnj.png)_New client intake form_

**Collect reports**

### Collect reports from unauthenticated users

Share report submission forms with unauthenticated users. This can be useful for providing external partners or customers access to forms. For example, you can use public forms to allow unauthenticated users to report issues they have encountered using your service.

![Report issue form](/assets/report-issue.m-A6KNmp.png)_Report issues form_

## How it works

> **SAVE DATA TO A TABLE ACTION**
> 
> To use this feature, your page must have a button configured with the **Save data to a table** action. Without this configuration, your pages can't capture user submissions.
> 
> Learn more about [button](/en/workflow-apps/page-components#button) actions.

**Overview**

You can create public links for your Workflow apps instantly with one click from the [App interface](/en/workflow-apps/interface). Each page can have one public link, which facilitates anonymous user submissions. When an end-user submits the form, their input is saved to columns in your app's data table. This information is displayed in the [Workflow apps portal](/en/workflow-apps/portal-settings) as a request from an anonymous user and is available in the recipe editor as a datapill. You can use this datapill to configure trigger conditions or other conditional logic to control how your workflow responds to requests from anonymous users.

**Workflow apps portal**

![Anonymous submission in Workflow apps portal](/assets/apps-portal-anonymous-user.KnGU5w-B.png)_Submissions from unauthenticated users are displayed as requests from anonymous users_

**Recipe**

![Anonymous user datapill](/assets/datapill-anonymous-user.BTBzrR7A.png)_Submissions from unauthenticated users are available in output of the Workflow apps New request trigger in the User name datapill_

### Enable public links

Complete the following steps to enable this functionality for one or more pages:

1. Select a Workflow app and click **Manage public links** or **`{N}` Public links** next to the app name.
   
   ![Create a public link](/assets/public-link.BY3keShH.gif)_Create a public link_
   
2. In the **\+ Add page** drop-down, select the page for which you plan to create a public link.
   
3. Optional. Select the **Enable CAPTCHA** checkbox to add a user verification step, helping prevent spam and bot submissions.
   
4. Copy the link.
   
5. Click **Done**.
   

### Manage public links

You can manage public links directly from the main [App interface](/en/workflow-apps/interface) in Workflow apps. The interface displays the total number of public links you have at all times, regardless of whether they are currently active or inactive. This allows you to keep track of all your public links efficiently.

![Enable links](/assets/enable-links.CEwpRM1L.gif)_Enable links and revoke access_

Manage your links with the following actions:

- **Enable or revoke access**: Revoke access to public links at any time. This action preserves the link structure but prevents users from accessing your page. This is useful if you must update your forms or workflow and plan to prevent form submission during the maintenance window.
  
- **Enable CAPTCHA**: Enhance security and ensure the validity of form submissions. This protects your infrastructure from overuse and bot activity by requiring users to complete a CAPTCHA for every submission attempt. This helps prevent automated abuse of your public forms.
  
- **Embed forms**: Embed publicly accessible forms and pages within your application.
  
- **Regenerate**: Generate a new link instantly. When you generate a new link, the previous link becomes invalid.
  
- **Delete**: Permanently delete the link. When you try to delete a link, Workato displays a prompt confirming deletion.
  

### Malware scanning for uploaded files

Workato performs malware scanning for all files uploaded through public submission forms. When you upload a file through a public form, submission is blocked until scanning completes. If file scanning detects malware, Workato displays an error message and dismisses the file.

![Malware scanning for uploaded files](/assets/virus-scanning.BeYBKE2R.gif)_Malware scanning_

## Use in recipes

When anonymous users fill out forms using public links without authenticating, Workato captures this data in datapills for use in recipe steps. This data is available in the recipe editor in the output of the **Workflow apps New request** trigger. For example, the Guest user datapill is a boolean (true/false) value that indicates if the submission was made by an anonymous user. This enables you to set trigger conditions and other conditional logic to handle submissions from anonymous users differently than how you handle requests from authenticated users.

### Save user data

Additionally, public forms can capture user data, such as user names and email addresses, for use in recipe steps. To achieve this, you must configure your pages to save this data to system columns during the page design stage. This makes the values available in the output of the **Workflow apps New request** trigger as User name and User email datapills.

Complete the following steps to save user names and email addresses to system columns:

1. In the **Save user input to data column** field, select one of the **System data** columns, such as **User name** or **User email**.
   
   ![Save components to system-generated columns](/assets/system-columns-save.3aKwlOY0.png)_Save the user name and email to system columns for use in recipe steps_
   
2. Click **Save**.
   

> **COMPATIBILITY**
> 
> Saving user data in system columns is available exclusively for anonymous user submissions and is compatible only with the **Short text** and **Email** component types.
> 
> Additionally, this feature doesn't work if there are columns in your data table that are set as **required**.

### Set a trigger condition

Complete the following steps to create a trigger condition to ensure your recipe only responds to submissions from anonymous users.

1. Edit your **New request in {App name}** recipe.
   
2. Configure the trigger condition
   
   1. Click the **Set trigger condition** toggle.
      
   2. Map the Guest user (Step 1) datapill to the **Trigger data** field.
      
   3. Select **is true** from the **Condition** drop-down menu.
      
      ![Set up a trigger condition](/assets/trigger-condition.DgX7Aq1X.gif)_Set up a trigger condition to process only events from anonymous users_
      
   
3. Click **Save**.
   

## Limitations

Public links and anonymous form submission are not compatible with [Dashboard](/en/workflow-apps/page-templates#dashboard) pages.

Additionally, public forms don't support the following features:

- **Drop-down** components with [recipes as a data source](/en/workflow-apps/dropdown-recipe-data-source)
- **Table** components with [recipes as a data source](/en/workflow-apps/table-recipe-data-source)
- Components configured with the [Run recipe](/en/workflow-apps/component-actions/run-recipe) action

Public links to the page still work and other portions render correctly when these components or actions are included, but the affected components won't display data and **Run recipe** actions won't execute.

Further limitations can apply depending on your pricing plan and contract. Contact your Customer Success Manager to learn more.

---
