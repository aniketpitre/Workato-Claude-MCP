---
url: 'https://docs.workato.com/en/workflow-apps/application-page.md'
description: >-
  Learn how the Workflow apps Application page lets app-users submit, manage,
  filter, and view requests from connected data tables.
---

# Application page

On the Application page, you can submit, manage, filter, and view requests.

This page displays the columns in your Workflow app's corresponding [data table](/en/data-tables). You can determine which columns appear on this page in the [App tab](/en/workflow-apps/interface#columns-display).

## Submit a request

Every application with a request submission page configured has a **Create new request** button on the top-right corner of the application page. When an app-user clicks **Create new request**, Workato displays the page used to submit a new request for the application.

![Submit a request](/assets/new-request.Bwi1OPSJ.png)_Submit a request_

## Manage requests

The Application page displays all requests that are visible to the app-user. Managers of the application can see all requests. Members can only see the requests that they've created or the ones they are assigned to.

Workato administrators can set up the roles for the users in the application at the project level. See [user groups](/en/workflow-apps/setup-and-access) for more information on assigning roles.

## Filter requests

### Quick filters

The Application page contains three quick filters:

- Assigned to me
  
- Requests assigned to the authenticated user.
  
- Created by me
  
- Requests created by the authenticated user.
  
- Due today
  
- Requests due on the day the user views the request.
  

### Filters for system-generated columns

In your Workflow app's corresponding [data table](/en/data-tables), you can filter requests by the following system-generated columns:

- Current stage
  
- The workflow stage of the request. Builders can define custom workflows to track requests in Workato in **Projects > Project name > Settings > App**.
  
  See [workflow stages](/en/workflow-apps/interface#pages-assign) for more information.
  
- Name of the record
  
- Workato uses the first column in the table to display as the record name. The order of the columns can be changed in the **Data tables** interface.
  
- Last updated
  
- The most recent date the request was updated.
  
- Created at
  
- The date the user created the request.
  
- Created by
  
- The user that created the request. This field is empty if the request was created using the Data table connector.
  
- Due on
  
- The date by which the task for the request must be processed. This field is empty if there are no active tasks for the current request.
  
- Assignee
  
- The user or group assigned to the active task for the request. This field is empty if there are no active tasks for the current request.
  

![View/filter requests](/assets/filter-requests.DAYaFpHJ.png)_View/filter requests_

> **ADJUST COLUMN WIDTHS IN WORKFLOW REQUESTS**
> 
> The Workflow apps portal supports the ability to adjust the width of the columns in the **Workflow requests** tab. These settings are saved in your browser, ensuring a consistent user experience across different sessions.

### Custom filters

This page also supports the ability to create custom filters. The available filters vary and are based on the user-generated custom columns in your Workflow app's corresponding [data table](/en/data-tables).

To create a custom filter:

1. Click **+** (plus) and select an item from the drop-down.
   
   ![Add custom filter](/assets/custom-filters.Ckwmub9M.png)_Add a custom filter_
   
2. Select an operand from the following options to define your custom filter:
   
   - Equals
   - Is not equal to
   - Starts with
   - Is not empty
   - Is empty
3. _Optional_. Add additional custom filters as required.
   

## View request details

Clicking on any request in the list displays the right panel with the details of this request. Task details display to task assignees and users with access to the request.

Additionally, this panel displays all activity streams for the request, including the following activities:

- Comments
- Creation
- [Custom task status labels](/en/workflow-apps/tasks#custom-task-status)
- Task creation or assignment
- Task completion
- Task expiration
- Task reassignment
- Task sharing
- Workflow stage changes

![Details panel](/assets/portal-details-panel.DYeRyYEM.png)_Details panel_

### Submit comments on requests

Within the details panel, users can engage with requests by leaving comments. This feature is useful when additional information is required from the requester for a proper evaluation of the request. The commenting privilege varies based on the user's [Workflow apps role](/en/workflow-apps/setup-and-access#app-access-manage) (Manager or Member) and their association with the specific request, as outlined in the following table.

| Role | Permissions |
| --- | --- |
| Manager | Managers can submit and view comments on all requests in an application, even requests to which they are not assigned. |
| Member | Members can submit and view comments on requests they’ve submitted or been assigned to. |

All comments are documented within the request's activity stream. Additionally, when a user comments on a request, Workato automatically sends email notification to the following users:

- The request's originator
- Assignees to the request
- App managers (users with the **Manager** role)

The email notification contains the commenter's name and comment. Users can [disable email notifications](/en/workflow-apps/email-notifications#disable-notifications) in the Workflow apps portal.

![Email notifications](/assets/email-notifications.B9UZ4d9Q.png)_Example email notification_

#### Style comments

The comment input field offers styling options through the formatting toolbar or Markdown syntax, supporting the following [Markdown](https://daringfireball.net/projects/markdown/) syntax:

| Markdown element | Markdown syntax |
| --- | --- |
| Bold | `**bold text**` |
| Italic | `*italic text*` or `_italic text_` |
| Link | `[link text](https://www.example.com)` |
| Ordered list | `1. First item` `1. Second item` `1. Third item` |
| Unordered list | `- First item` `- Second item` `- Third item` |

#### Preview comments

You can preview your comments before you submit them.

To preview comments:

1. Open the details panel of a request.
   
2. Enter text into the comment input field.
   
3. Click the **Preview** (eye) icon to see the text you added.
   
   ![Click the Preview icon](/assets/preview-comment.CwivdSih.png)_Preview comment_
   

#### Show or hide comments

You can hide or display comments for a request.

To show or hide comments:

1. Open the details panel of a request.
   
2. Click the **...** (ellipses), then click **Show comments** or **Hide comments**.
   

## View completed requests

View completed requests at any time in the Workflow apps portal from the Application page. There are two ways to access a completed request:

- Open the details panel for the request you plan to view and click **View details**.
- From the list of requests, hover over the request you plan to view. Click the **View details** button that appears.

![View completed requests](/assets/completed-requests.DmIU4_Z8.png)_View details of a completed request_

> **PAGES ASSIGNED TO STAGES WITHOUT ACTIVE TASKS**
> 
> You can view pages assigned to workflow stages without active tasks. To view a page assigned to stages without active tasks, simply hover over the request and click the **View details** button, similar to how you would access details of a completed request.

## Print pages

You can print pages from the Workflow apps portal. Dashboard pages can also be downloaded.

Workflow apps support printing submission, review, dashboard, and custom pages. The Workflow requests page can't be printed.

Complete the following steps to print a page:

1. Go to the Workflow apps portal and select an app.
   
2. Select the page you plan to print, such as a submission, review, or dashboard page.
   
3. Click the **Print** button.
   
   ![Print a page](/assets/page-print.B2CBhfm9.png)_Print a page_
   
4. Optional. Click the **Download** button to download a dashboard page as a PNG image.
   
   ![Download a dashboard page](/assets/page-download.BPireR2Z.png)_Download a dashboard page_

---
