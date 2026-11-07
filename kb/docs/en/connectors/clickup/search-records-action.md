---
url: 'https://docs.workato.com/en/connectors/clickup/search-records-action.md'
description: >-
  The **Search records** action returns results from ClickUp that match all your
  search criteria.
---

# ClickUp - Search records action

The **Search records** action returns results from ClickUp that match all your search criteria.

## Input

Input fields load dynamically based on the selected object. For example, if you select the **List members** object, the following input fields are available.

| Input field | Description |
| --- | --- |
| List ID | Select the name of the list from the drop-down menu. |
| Workspace/Team | Select the name of the workspace or team from the drop-down menu. |
| Space | Select the name of the space from the drop-down menu. |
| Folder | Select the name of the folder from the drop-down menu. |

## Output

The output loads dynamically based on the object selected when configuring the action. For example, if you select the **List members** object, the following output schema is generated.

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the user (member) in ClickUp. |
| Username | Display name or username of the user as shown in ClickUp. |
| Email | The email address associated with the user’s ClickUp account. |
| Color | Hex color code associated with the user, typically used in task assignments or avatars. |
| Profile picture | URL of the user’s profile picture (avatar) in ClickUp. |
| Initials | Automatically generated initials based on the user's name. |
| Role | The user’s role in the workspace (such as, admin, member, or guest). |
| Profile info | Additional metadata or profile-related settings for the user. |

---
