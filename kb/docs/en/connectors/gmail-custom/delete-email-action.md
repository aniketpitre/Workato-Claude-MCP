---
url: 'https://docs.workato.com/en/connectors/gmail-custom/delete-email-action.md'
description: >-
  The Delete email action immediately and permanently deletes a message from a
  Gmail mailbox.
---

# Gmail (Custom) - Delete email action

The **Delete email** action immediately and permanently deletes a message from a Gmail mailbox. This action can't be undone and requires the `https://mail.google.com/` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Message ID | Enter the ID of the message to delete. |

## Output

This action doesn't return output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/delete-email-delegation-access-action.md
description: >-
  The Delete email delegation access action removes a delegate from a Gmail
  mailbox and revokes any verification required for it.
---

# Gmail (Custom) - Delete email delegation access action

The **Delete email delegation access** action removes a delegate of any verification status from a Gmail mailbox and revokes any required verification. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Delegate email | Enter the email address of the user to remove as a delegate. |

## Output

This action doesn't return output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/delete-forwarding-address-action.md
description: >-
  The Delete forwarding address action deletes a forwarding address and revokes
  any verification required for it.
---

# Gmail (Custom) - Delete forwarding address action

The **Delete forwarding address** action deletes a forwarding address and revokes any required verification in Gmail. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Forwarding email | Enter the forwarding address to delete. |

## Output

This action doesn't return output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/get-message-content-action.md
description: >-
  The Get message content action gets the full content of a Gmail message,
  identified by a Pub/Sub notification payload or a message ID.
---

# Gmail (Custom) - Get message content action

The **Get message content** action gets the full content of a Gmail message. You can identify the message using the Pub/Sub payload from a Gmail push notification or directly from a Gmail message ID. This action requires the `https://mail.google.com/` OAuth scope.

Decoded message body content is included alongside the raw base64-encoded data returned by Gmail.

## Input

| Input field | Description |
| --- | --- |
| Identify message by | Select to identify the message using Pub/Sub message data or a message ID. Defaults to **Pub/Sub message data**. |
| User id | Enter the user's email address. |
| Pub/Sub message data | Enter the base64 encoded data from the Pub/Sub trigger. Shown when **Identify message by** is set to **Pub/Sub message data**. |

## Output

| Output field | Description |
| --- | --- |
| Message ID | The unique ID of the message. |
| Thread ID | The ID of the thread the message belongs to. |
| Label IDs | The IDs of labels applied to the message. |
| Snippet | A short excerpt from the message body. |
| Payload | The parsed email structure, including MIME headers and body parts. Each body part includes the raw base64-encoded content in **Data** and the decoded, human-readable text in **Decoded content**. |
| Size estimate | The estimated size of the message in bytes. |
| History ID | The ID of the last history record that modified the message. |
| Internal date | The internal Gmail timestamp for the message, in epoch milliseconds. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/list-email-delegates-action.md
description: The List email delegates action lists the delegates for a Gmail mailbox.
---

# Gmail (Custom) - List email delegates action

The **List email delegates** action lists the delegates for a Gmail mailbox. This action requires one of the following OAuth scopes: `https://www.googleapis.com/auth/gmail.settings.basic`, `https://mail.google.com/`, `https://www.googleapis.com/auth/gmail.modify`, or `https://www.googleapis.com/auth/gmail.readonly`.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |

## Output

| Output field | Description |
| --- | --- |
| Delegates | Array of delegates for the mailbox. Each entry includes a delegate email and a verification status. |
| User id | The user's email address. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/list-forwarding-address-action.md
description: >-
  The List forwarding address action lists the forwarding addresses configured
  for a Gmail mailbox.
---

# Gmail (Custom) - List forwarding address action

The **List forwarding address** action lists the forwarding addresses configured for a Gmail mailbox. This action requires one of the following OAuth scopes: `https://www.googleapis.com/auth/gmail.settings.basic`, `https://mail.google.com/`, `https://www.googleapis.com/auth/gmail.modify`, or `https://www.googleapis.com/auth/gmail.readonly`.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |

## Output

| Output field | Description |
| --- | --- |
| Forwarding addresses | Array of forwarding addresses configured for the mailbox. Each entry includes a forwarding email and a verification status. |
| User id | The user's email address. |

---
