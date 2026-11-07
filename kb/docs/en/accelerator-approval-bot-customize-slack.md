---
url: 'https://docs.workato.com/en/accelerator-approval-bot-customize-slack.md'
description: >-
  Configure the Approval bot accelerator recipes for Slack to customize the
  approval workflow, dashboard, and source application.
---

# Customize the Approval bot accelerator for Slack

If you plan on implementing the **Approval bot accelerator** in Slack, you must configure the following recipes:

- [ABS | Call-006 | Slack Update Homepage](#update-homepage)
- [ABS | REC-001 | Slack Request Parent Recipe](#parent-recipe-modify)
- [ABS | REC-003 | Approve/Reject Request from Slack](#request-recipe-modify)

> **DEFAULT APPROVAL WORKFLOW**
> 
> The approval workflow in this accelerator triggers from a new/updated row in Google Sheets by default. If you decide to use an application other than Google Sheets as the basis of your approval workflow, you must also change the connection in the preceding recipes. Contact Customer Success for support.

* * *

## Configure recipe **ABS | Call-006 | Slack Update Homepage**

Modify this recipe to customize the Approval Dashboard to include your company's email address. This recipe includes `support@workato.com` as a placeholder.

To add your company's email address:

1. In the recipe builder, select **Step 18**, **Publish an app home view**.
   
2. Update the **Text** field with your team's support email address.
   

* * *

## Configure recipe **ABS | REC-001 | Slack Request Parent Recipe**

This recipe calls the **ABS | Call-002 | Request to Slack** recipe when there is a new/updated row in a sheet in Google Sheets.

![Slack Request Parent Recipe](/assets/parent-recipe.xK9Uo6ZR.png)_Slack Request Parent Recipe_

To configure this recipe:

1. _Optional._ If you plan to use an application other than Google Sheets, replace Google Sheets with your chosen application in **Step 1**.
   
2. Map the datapill according to your specific application.
   
   ![Map the datapill](/assets/datapill-map.DdtSs2P-.png)_Map the datapill_
   
   The input fields in Workato correspond to headers in Google Sheets. Alternate applications should contain similar fields.
   
   <dl><dt>Requester</dt><dd>The person who submitted an approval request.</dd><dt>Requester_email</dt><dd>This is the email address belonging to the person who submitted the approval request.</dd><dt>Request_app</dt><dd>The app the requester is seeking approval for.</dd><dt>Request_description</dt><dd>The message accompanying approval request.</dd><dt>Date_requested</dt><dd>Date of the approval request.</dd><dt>Approver</dt><dd>This is the person you designate to process approval requests.</dd><dt>Approver_email</dt><dd>This is the email address belonging to the person you designate to process approval requests.</dd><dt>Request_url</dt><dd>The URL of the request.</dd><dt>Date_approved</dt><dd>If the approver approves the request, this is the approval date.</dd><dt>Date_rejected</dt><dd>If the approver denies the request, this is the rejection date.</dd><dt>Request_ID</dt><dd>The unique ID that belongs to the request.</dd></dl>
   

* * *

## Configure recipe **ABS | REC-003 | Approve/Reject Request from Slack**

Follow these steps to configure this recipe:

1. _Optional._ If you plan to use an application other than Google Sheets, change the sheet connection to your chosen application.
   
2. Map the result (approval or rejection) back to your application in **Step 16** and **Step 21**.
   
   ![Modify step 16 and step 21](/assets/recipe-steps-modify.29uZF04i.png)_Modify Step 16 and Step 21_
   
3. _Optional._ If you are not using the **Sheet connector**, delete **Step 11**.

---
