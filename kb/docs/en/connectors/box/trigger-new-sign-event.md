---
url: 'https://docs.workato.com/en/connectors/box/trigger-new-sign-event.md'
description: >-
  The New/updated sign event trigger starts a recipe when a new sign request is
  created or an existing sign request is updated in a specified Box folder.
---

# Box - New/updated sign event in folder trigger

The **New/updated sign event in folder** trigger starts a recipe when a new sign request is created or an existing sign request is updated in a specified Box folder.

You must connect a Box account with admin level privileges or select **manage enterprise properties** in the OAuth scopes to use the **New or updated sign event in folder** trigger.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select the folder to monitor for sign events. Sub-folders aren't monitored. |
| Sign events | Select the sign events to monitor from the drop-down menu. |

## Output

The output fields vary depending on the type of event. The following example shows the output for a signature request event:

| Output field | Description |
| --- | --- |
| Event ID | Unique ID of the event. |
| Event type | Type of event. For example, `SIGN_DOCUMENT_VIEWED_BY_SIGNER`. |
| Created by | Member who triggered the event. |
| Action by | Action that matched the trigger condition. |
| Created at | Date and time of the event. |
| IP address | IP address of the member who triggered the event. |
| Session ID | Unique ID of the event session. |
| Sign request ID | Unique ID of the sign request. |
| Sign request short ID | Short form of the sign request ID. |
| Status | Status of the sign request. For example, `viewed`. |
| File ID | ID of the file associated with the event. |
| File name | Name of the file. For example `SampleSignDocument.pdf`. |
| Parent ID | ID of the parent folder. |
| Expires | Expiration date and time of the sign request. |
| Requester | Details of the user who requested the signature. Includes ID, type, name, and login. |
| Signer | Details of the signer. Includes ID, type, name, and login. |
| Signer IP address | IP address of the signer. |
| Requester IP address | IP address of the requester. |
| Template | Template name used to create the request. If no template was used, the value is null. |
| Sender message | Subject and message sent with the request. |
| Forward | Indicates if the request was forwarded. |
| Batch send | Indicates if the request was sent to multiple recipients in a batch. |
| Ready sign link | Link to the document for signing. |
| Redirection | Redirection details, including redirect URL and declined redirect URL. |
| Additional details | Any additional metadata if available. |

---
