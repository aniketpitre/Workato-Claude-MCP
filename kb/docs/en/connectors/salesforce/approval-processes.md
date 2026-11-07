---
url: 'https://docs.workato.com/en/connectors/salesforce/approval-processes.md'
description: >-
  Learn how the Salesforce connector for Workato supports approval processes,
  including approving, rejecting, and submitting records for approval.
---

# Salesforce approval process

The Salesforce approval process is an automated combination of steps for a Salesforce record to be approved and the steps to take when a record is rejected.

Approval steps define the chain of approval for a particular approval process. Each step determines which records can advance to that step, who to assign approval requests to, and whether to let each approver’s delegate respond to the requests.

In an approval process, you usually specify:

- The **steps** necessary for a record to be approved and **who** approves it at each step:
  - When the record is first submitted for approval
  - The record is approved
  - The record is rejected
  - The record is recalled
- The actions to take based on what happens during the approval process

Workato's Salesforce connector provides the following approval process actions:

- [Approve record in approval process](/en/connectors/salesforce/actions/approve-record)
- [Reject record in approval process action](/en/connectors/salesforce/actions/reject-record)
- [Submit record for approval](/en/connectors/salesforce/actions/submit-record)

## Build an approval process

The following examples approve or reject a request for a Discount rate above 10% on an Invoice. `Discount` is a custom field created on the Invoice object (custom object) for this demonstration.

The following image shows the configured approval process in Salesforce:

![Setting up a Salesforce approval](/assets/approval-setup.CrF_8_Xe.png)_Setting up a Salesforce approval_

You must activate an approval process before you can use it in a Workato recipe.

Refer to the Salesforce [Customize How Records Get Approved](https://trailhead.salesforce.com/en/content/learn/modules/business_process_automation/approvals) and [Set Up a Classic Approval Process](https://help.salesforce.com/articleView?id=approvals_getting_started.htm&type=5) guides for more information about building an approval process from start to finish.

### Who can approve requests?

Any of the following can approve or reject a request.

- A user or queue that the approval request submitter chooses.
- A queue specified by the administrator.
- A user listed in the Manager standard field on the submitter's user detail page.
- A user listed in a custom hierarchy field on the submitter's user detail page.
- Any combination of users and related users (users listed in a standard or custom field on the submitted record) specified by the administrator.

---
