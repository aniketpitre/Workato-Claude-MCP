---
url: 'https://docs.workato.com/en/workflow-apps/page-templates.md'
description: >-
  Reference for Workflow apps page templates, including submission form,
  approval form, dashboard, and blank page options for building pages quickly.
---

# Page templates

Page templates allow you to quickly add new pages to your Workflow apps. The following page templates are available:

- [Submission form](#submission-form)
- [Approval form](#approval-form)
- [Dashboard](#dashboard)

Alternatively, select **Blank page** to create a page from scratch.

End-users can [print pages](/en/workflow-apps/application-page#print-pages) from the Workflow apps portal. Dashboard pages can also be downloaded as PNG images.

* * *

## Submission form

Generates a form to submit a request to the data table. The form includes input fields that map to columns in the Workflow app's corresponding data table, allowing you to store the values submitted in each field. The type of data allowed in each input field must conform to the [column type](/en/data-tables/user-interface/column-types) of the corresponding column. For example, if an input field maps to a **date** column type, the field only accepts values in **MM/DD/YYYY** format and does not accept short text or an integer as input.

Additionally, the **hint** and **is required** flags for the input field are copied from the table column settings.  
The form Workato generates has a button that saves the data you provide to the data table.

![Submission form template](/assets/page-template-submission-form.DQcUA_Rd.png)_Submission form template_

* * *

## Approval form

The Approval form is similar to the Submission form, except all fields are **read-only** by default. This form includes two buttons to complete the current task with an **Approved** or **Rejected** outcome.  
See [Workflow apps by Workato connector](/en/workflow-apps/workflow-apps-connector) for more information.

![Approval form template](/assets/page-template-approval-form.dKxhtQ6g.png)_Approval form template_

* * *

## Dashboard

Use the dashboard page type to build custom dashboards to visualize your data.

Dashboard pages support the following data sources:

- Workspace data
- Workflow apps
- Data tables
- Individual recipe job history data

Refer to the [Insights](/en/insights) documentation for more information.

![Dashboard template](/assets/insights-dashboard-template.kXUb2VcQ.png)_Dashboard page template_

* * *

> **FURTHER READING**
> 
> - [Create a Page](/en/workflow-apps/pages-create)
> - [Customize a Page](/en/workflow-apps/pages-customize)

---
