---
url: 'https://docs.workato.com/en/connectors/redmine/get-record-action.md'
description: The Get record action retrieves an issue from Redmine by its ID.
---

# Redmine - Get record action

The **Get record** action retrieves an issue from Redmine by its ID. You can optionally include associated data, such as attachments or journals.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type. **Issue** is the only supported object type. |
| Issue ID | Enter the ID of the issue you plan to retrieve. |
| Include | Optional. Select the associated data to return with the issue. Options include **Children**, **Attachments**, **Relations**, **Changesets**, **Journals**, **Watchers**, and **Allowed statuses**. Click **Use custom value** to enter comma-separated values manually. For example, `children,journals`. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the issue. |
| Subject | Subject of the issue. |
| Description | Description of the issue. |
| Project | Project the issue belongs to. Includes the project ID and name. |
| Tracker | Tracker of the issue, such as **Bug** or **Feature**. Includes the tracker ID and name. |
| Status | Status of the issue. Includes the status ID and name. |
| Priority | Priority of the issue. Includes the priority ID and name. |
| Assigned to | User or group the issue is assigned to. Includes the ID and name. |
| Due date | Date the issue is due. |
| Updated on | Date and time the issue was last updated. |
| Children | Associated children. Returned when you select **Children** in the **Include** input field. |
| Attachments | Associated attachments. Returned when you select **Attachments** in the **Include** input field. |
| Relations | Associated relations. Returned when you select **Relations** in the **Include** input field. |
| Changesets | Associated changesets. Returned when you select **Changesets** in the **Include** input field. |
| Journals | Associated journals. Returned when you select **Journals** in the **Include** input field. |
| Watchers | Associated watchers. Returned when you select **Watchers** in the **Include** input field. |
| Allowed statuses | Associated statuses. Returned when you select **Allowed statuses** in the **Include** input field. |

---
