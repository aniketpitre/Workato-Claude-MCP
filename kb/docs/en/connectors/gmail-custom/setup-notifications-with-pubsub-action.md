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
