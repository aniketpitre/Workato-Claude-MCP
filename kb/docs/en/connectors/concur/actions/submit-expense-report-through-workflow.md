---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/submit-expense-report-through-workflow.md
description: >-
  The Submit expense report through workflow action submits an expense report
  through the workflow in SAP Concur.
---

# SAP Concur - Submit expense report through workflow action

The **Submit expense report through workflow** action submits an expense report through the workflow in SAP Concur. Check the current approval status of the expense report before submitting it through the workflow.

## Input

| Input field | Description |
| --- | --- |
| Workflowstep ID | Enter the workflow step identifier. This ID can be found in the Workflow action URL datapill of an expense report output. |
| Action | Select the workflow action to perform. Options include: Approve, Send Back to Employee, Recall to Employee |

## Output

| Output field | Description |
| --- | --- |
| Message | The error message. Only appears if a submission error was generated. |
| Status | The status of the report submit action. |
