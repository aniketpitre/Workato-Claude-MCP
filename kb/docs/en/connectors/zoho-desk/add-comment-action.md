---
url: 'https://docs.workato.com/en/connectors/zoho-desk/add-comment-action.md'
description: The Add comment action enables you to add a comment in the Zoho Desk.
---

# Zoho Desk - Add comment action

The **Add comment** action enables you to add a comment in the Zoho Desk.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create the record. Fields load dynamically based on the object you select. |

For example, if the selected object is **Contact**, the input schema is as follows:

| Input fields | Description |
| --- | --- |
| Contacts ID | Enter the ID of the contact. |
| Comment | Enter the comment that you want to add. |
| Content type | Select the type of comment. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

For example, if the selected object is **Contact**, the output schema is as follows:

| Output field | Description |
| --- | --- |
| Comment ID | ID of the comment. |
| Comment | Comment that you added. |
| Encode content | Encoded content. |
| Commenter ID | ID of the commenter. |
| Is public | Indicated if the comment is public. |
| Commented time | Time of the comment. |
| Modified time | Time of the comment modified. |
| ID | Child parameter of ‘Commenter’. ID of the commenter. |
| Name | Child parameter of ‘Commenter’. Name of the commenter. |
| Email | Child parameter of ‘Commenter’. Email of the commenter. |
| Photo URL | Child parameter of ‘Commenter’. Photo URL of the commenter. |
| Type | Child parameter of ‘Commenter’. Type of the commenter. |
| First name | Child parameter of ‘Commenter’. First name of the commenter. |
| Last name | Child parameter of ‘Commenter’. Last name of the commenter. |
| Role name | Child parameter of ‘Commenter’. Role of the commenter. |

---
