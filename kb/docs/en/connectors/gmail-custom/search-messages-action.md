---
url: 'https://docs.workato.com/en/connectors/gmail-custom/search-messages-action.md'
description: The Search messages action lists the messages in a Gmail mailbox.
---

# Gmail (Custom) - Search messages action

The **Search messages** action lists the messages in a Gmail mailbox. This action requires one of the following OAuth scopes: `https://www.googleapis.com/auth/gmail.metadata`, `https://mail.google.com/`, `https://www.googleapis.com/auth/gmail.modify`, or `https://www.googleapis.com/auth/gmail.readonly`.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Query | Enter a query to use. Supports the same query format as the Gmail search box. For example, `from:someuser@example.com is:unread`. You can't use the query if the connection only has the `gmail.metadata` scope. |
| Label IDs | Enter any labels to return messages that match all of the specified label IDs. Provide label IDs separated by a comma. |
| Max results | Enter the maximum number of messages to return. |
| Page token | Enter the page token to retrieve a specific page of results. |
| Include spam trash | Select `Yes` to include messages from **SPAM** and **TRASH** in the results. |

## Output

| Output field | Description |
| --- | --- |
| Messages | Array of matching messages. Each entry includes a message ID and a thread ID. |
| Next page token | Token to retrieve the next page of results. |
| Result size estimate | Estimated total number of matching messages. |
| User id | The user's email address. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/set-auto-forwarding-action.md
description: >-
  The Set auto-forwarding action updates the auto-forwarding setting for a Gmail
  mailbox.
---

# Gmail (Custom) - Set auto-forwarding action

The **Set auto-forwarding** action updates the auto-forwarding setting for a Gmail mailbox. A verified forwarding address must be specified when auto-forwarding is enabled. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Enabled | Select `Yes` to automatically forward all incoming mail to another address. |
| Email address | Enter the email address that all incoming messages are forwarded to. This address must be a verified forwarding address. |
| Disposition | Select the state a message is left in after it's forwarded. |

## Output

| Output field | Description |
| --- | --- |
| Enabled | Whether all incoming mail is automatically forwarded to another address. |
| Email address | The email address that all incoming messages are forwarded to. |
| Disposition | The state a message is left in after it's forwarded. |
| User id | The user's email address. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/setup-notifications-with-pubsub-action.md
description: >-
  The Setup notifications with Pub/Sub action configures or renews Gmail push
  notifications to a Google Pub/Sub topic.
---

# Gmail (Custom) - Setup notifications with Pub/Sub action

The **Setup notifications with Pub/Sub** action configures or renews Gmail to send push notifications to a Google Pub/Sub topic. This action requires the `https://mail.google.com/` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Topic name | Enter the Pub/Sub topic name, using the Cloud Pub/Sub `v1` topic naming format. For example, `projects/my-project-identifier/topics/my-topic-name`. The topic must already exist, and Gmail must already have publish permission for the topic. The project identifier must exactly match the Google developer project executing this request. |
| Labels | Select the list of label IDs to restrict notifications to. Notifications are sent for all changes if unspecified. The labels determine which messages generate a push notification if specified. |
| Label filter behavior | Select the filtering behavior for the specified label IDs. Select **Include** to only get notifications for message changes related to the specified labels, or **Exclude** to get notifications for all message changes except those related to the specified labels. |

## Output

| Output field | Description |
| --- | --- |
| History ID | The ID of the last change processed for the mailbox. |
| Expiration | The date and time when Gmail stops sending notifications for the mailbox, unless the watch request is renewed. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/stop-notifications-action.md
description: The Stop notifications action stops Gmail push notifications for a mailbox.
---

# Gmail (Custom) - Stop notifications action

The **Stop notifications** action stops Gmail from sending push notifications to a Google Pub/Sub topic for the specified mailbox. This action requires the `https://mail.google.com/` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |

## Output

This action doesn't return output fields.

---
