---
url: 'https://docs.workato.com/en/connectors/mailchimp/campaign-opened-trigger.md'
description: >-
  The Campaign opened trigger in the MailChimp connector fires when a contact in
  your audience opens a campaign communication sent to them.
---

# MailChimp - Campaign opened trigger

This trigger runs when a contact in your audience opens a campaign communication sent to them.

![Campaign opened trigger](/assets/campaign-opened-trigger.cF7ZI13m.png)_Campaign opened trigger_

## Input

| Input field | Description |
| --- | --- |
| Campaign ID | The ID of the campaign you plan to monitor. |

## Output

| Output field | Description |
| --- | --- |
| Members | The members included in the campaign. |
| Campaign ID | The ID of the campaign for which open details are being monitored. |
| List ID | The list ID used in the campaign for which open details are being monitored. |
| List is active | Indicates if the list used in the campaign is active or not. This value is `true` or `false`. |
| Contact status | The status of the contacts who opened the campaign. |
| Email ID | The email ID of the contacts. |
| Email address | The email address of the contact. |
| Opens count | Indicates how many times the campaign was opened. |
| Timestamp | The time at which the campaign was opened by the recipient. For example: `2023-08-24T14:15:22Z`. |
| Total opens | Indicates how many times the campaign was opened by recipients in total. |

---
