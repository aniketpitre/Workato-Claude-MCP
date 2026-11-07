---
url: 'https://docs.workato.com/en/connectors/onetrust/reassign-record-action.md'
description: The Reassign record action reassigns an assessment in OneTrust.
---

# OneTrust - Reassign record action

The **Reassign record** action reassigns an assessment in OneTrust.

## Input

| Input field | Description |
| --- | --- |
| Assessment ID | Enter the UUID of the assessment you plan to reassign. OneTrust ignores reassignments for completed assessments. Supported assessment types are `PIA`, `Vendor`, `ITRM`, `Control`, `Exchange`, and `Incident`. |
| Organization group ID | Enter the ID of the organization you plan to reassign the assessment to. Respondents and approvers you assign must exist in this organization. |
| Approvers | Add the users who replace the current approvers. Each approver requires an **Approver ID** and can include an approver name, a comment, and workflow stage IDs. |
| Respondents | Add the users who replace the current respondents. Each respondent requires a **Respondent name** and can include a respondent ID, a comment, and section IDs. Leave **Respondent ID** blank to create a new user. |
| Respondent creation type | Select the type of user to create for respondents that don't already exist. Options are **Invited** and **Project respondent**. Defaults to **Invited**. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the assessment was reassigned. |

---
