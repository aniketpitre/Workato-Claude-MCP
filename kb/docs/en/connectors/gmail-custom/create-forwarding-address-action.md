---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/create-forwarding-address-action.md
description: >-
  The Create forwarding address action creates a forwarding address for a Gmail
  mailbox.
---

# Gmail (Custom) - Create forwarding address action

The **Create forwarding address** action creates a forwarding address for a Gmail mailbox. Gmail sends a message to the recipient and sets the address's verification status to **pending** if ownership verification is required. The address is created with its verification status set to **accepted** if ownership verification isn't required. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Forwarding email | Enter an email address to which messages can be forwarded. |

## Output

| Output field | Description |
| --- | --- |
| Forwarding email | The forwarding address. |
| Verification status | The verification status of the forwarding address, such as `accepted` or `pending`. |
| User id | The user's email address. |
