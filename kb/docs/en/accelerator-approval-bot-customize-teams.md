---
url: 'https://docs.workato.com/en/accelerator-approval-bot-customize-teams.md'
description: >-
  Configure the Approval bot accelerator recipes for Microsoft Teams to
  customize the approval workflow and source application.
---

# Customize the Approvals bot accelerator for Microsoft Teams

If you plan on implementing the **Approval bot accelerator** in Microsoft Teams, you must configure the following recipes:

- [ABT | REC-001 | Requests from Source System](#parent-recipe-modify)
- [ABT | REC-003 | Approve/Reject Request from Microsoft Teams](#request-recipe-modify)

> **CUSTOMIZE APPROVAL WORKFLOW**
> 
> The approval workflow in this accelerator triggers from a new/updated row in Google Sheets by default. If you decide to use an application other than Google Sheets as the basis of your approval workflow, you must also change the connection in the preceding recipes.

* * *

## Configure recipe **ABT | REC-001 | Requests from Source System**

This recipe calls the **ABT | Call-001 | Request to Microsoft Teams** recipe when there is a new/updated row in a sheet in Google Sheets.

To configure this recipe:

1. _Optional_. If you plan on using a connection other than Google Sheets, update your connection in **Step 1**.
   
2. In **Step 1**, enter the **spreadsheet**, **sheet**, and **column to monitor**.
   
   ![Modify parent recipe](/assets/teams-parent-recipe.D6GxeGYk.png)
   
   <dl><dt>Spreadsheet</dt><dd>Select a spreadsheet to monitor for a new/updated row.</dd><dt>Sheet</dt><dd>Select a sheet to monitor for a new/updated row. The sheet must have at least one header row and one data row.</dd><dt>Column to monitor</dt><dd>Workato monitors this column for changes. When a cell in this column changes value, Workato considers the corresponding row as <strong>updated</strong> and triggers the recipe.</dd></dl>
   
3. Map the datapills from **Step 1** into **Step 2**. Workato preconfigures this step for you.
   
   The input fields in Workato correspond to headers in Google Sheets. Alternate applications should contain similar fields.
   
   <dl><dt>Requester</dt><dd>The person who submitted an approval request.</dd><dt>Requester_email</dt><dd>The email address belonging to the person who submitted the approval request.</dd><dt>Request_app</dt><dd>The app the requester is seeking approval for.</dd><dt>Request_description</dt><dd>The message accompanying the approval request.</dd><dt>Date_requested</dt><dd>Date of the approval request.</dd><dt>Approver</dt><dd>The person you designate to process approval requests.</dd><dt>Approver_email</dt><dd>The email address that belongs to the person you designate to process approval requests.</dd><dt>Request_url</dt><dd>The URL of the request.</dd><dt>Date_approved</dt><dd>If the approver approves the request, this is the approval date.</dd><dt>Date_rejected</dt><dd>If the approver denies the request, this is the rejection date.</dd><dt>Request_ID</dt><dd>The unique ID that belongs to the request.</dd></dl>
   

* * *

## Configure recipe **ABT | REC-002 | Approve/Reject Request from Microsoft Teams**

Follow these steps to configure this recipe:

1. _Optional._ If you plan to use an application other than Google Sheets, change the sheet connection to your chosen application.
   
2. Map the result (approval or rejection) back to your application in **Step 14** and **Step 23**.
   
   ![Update recipe](/assets/update-teams-recipe.DPpXT4JQ.png)
   
3. _Optional._ If you are not using the **Sheet connector**, delete **Step 5**.

---
