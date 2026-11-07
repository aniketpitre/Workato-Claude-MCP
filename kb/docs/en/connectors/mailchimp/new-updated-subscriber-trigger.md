---
url: >-
  https://docs.workato.com/en/connectors/mailchimp/new-updated-subscriber-trigger.md
description: >-
  The New or updated subscriber trigger in the MailChimp connector fires when a
  subscriber is added or updated, checking every five minutes by default.
---

# MailChimp - New or updated subscriber trigger

This trigger runs when a new subscriber is added or an existing subscriber is updated in MailChimp. This trigger checks for new or updated subscribers every five minutes by default.

![New or updated subscriber trigger](/assets/new-updated-subscriber-trigger.CvUfIutN.png)_New or updated subscriber trigger_

## Input

| Input field | Description |
| --- | --- |
| List | The list you plan to monitor for subscriber changes. |
| Subscriber status | This is an optional field. Subscriber status allows you to select a specific status. For example, unsubscribed, pending, or archived. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the subscriber. |
| Email address | The email address of the subscriber. |
| Unique email ID | The unique ID assigned to the subscriber's email address. |
| Contact ID | The contact ID of the subscriber. This is a 32-character alpha-numeric ID. For example: `abc3e082f3156bd9e1defg7010f92606`. |
| Full name | The full name provided by the subscriber. This field is blank if the subscriber did not provide a name. |
| Web ID | The web ID of the new subscriber. |
| Email type | The email type, for example `html`. |
| Status | The status that triggered the subscriber notification. |
| Consents to one to one messaging | Indicates whether the subscriber has consented to receive one-to-one messaging or not. This value is `true` or `false`. |
| Click rate | The click rate of the subscriber. |
| IP sign up | The IP address of the subscriber. This field is `null` if tracking is not turned on. |
| Timestamp sign up | The timestamp of the subscription. This field is `null` if tracking is not turned on. |
| Member rating | The member rating of the subscriber. For example, if the subscriber is the second person to subscribe, this value is `2`. |
| Last changed | The date the subscriber's account was last changed. For example: `2023-12-30`. |
| Language | The language of the subscriber. This field is `null` if tracking is not turned on. |
| VIP | Indicates whether the subscriber is a VIP customer or not. Values are `true` or `false`. |
| Location | The location of the subscriber. This field is `null` if tracking is not turned on. |
| Source | The source of the subscriber. |
| Tags count | The number of tags applied to the subscriber. |
| Tags | The tags applied to the subscriber. This field is blank if no tags are applied to the subscriber. |
| List ID | The ID of the list to which the subscriber was added or updated. For example: `69219a8a88`. |
| EUID | The unique identifier of the subscriber or contact on an account level, across all audiences. |
| LEID | The unique identifier for the subscriber or contact, specific to an audience. |
| Notes | Notes added to the subscriber listing. This field is blank if no notes are added. |
