---
url: 'https://docs.workato.com/en/connectors/aconex/create-mail-action.md'
description: The Create mail action creates a new mail item in Aconex.
---

# Aconex - Create mail action

The **Create mail** action creates a new mail item in Aconex.

## Input

| Input field | Description |
| --- | --- |
| Project | Select the project where you plan to create the new mail action. |
| Mail types | Select the type of mail item you plan to create. |
| Rich text | Select `Yes` or `No` to enable HTML rendering in the mail item. |
| To | Select the recipient of the new mail item. |
| Subject | Enter the number of the new mail item. Maximum 250 characters. |
| Total attachment count | Enter the total number of attachments in the new mail item. |
| Reason for issue | Select a reason that you plan to create a new mail item. |
| Cc | Select recipients to CC on the new mail item. |
| Response required date | Enter the date that a response to the mail item is required. |
| Confidential | Select `Yes` or `No` to indicate if the mail item is confidential. |
| Attribute 1 | Select any attributes you plan to associate with the mail item. |
| Bcc | Select recipients to BCC on the new mail item. |
| Response required | Select the type of response required for the new mail item. |
| Body | Enter the body of the new mail item. |
| Attribute 2 | Select the attribute you plan to associate with the mail item. |
| Attribute 3 | Select the attribute you plan to associate with the mail item. |
| Attribute 4 | Select the attribute you plan to associate with the mail item. |
| Attached documents | Enter the IDs of documents attached to the mail item. |
| Mail form fields | Enter additional fields for forms in the mail item. |
| Restricted fields | Enter restricted fields for forms in the mail item. |
| Existing draft mail | Select an existing mail item draft to update. |
| Attachments | Enter base64 encoded attachments you plan to include in the new mail item. |

## Output

| Output field | Description |
| --- | --- |
| Mail ID | The ID of the mail item. |
| Send status | A response indicating if the mail item is sent or not. |
| Project ID | The ID of the project where the new mail item was created. |
| Mail subject | The subject line text of the new mail item. |

---
