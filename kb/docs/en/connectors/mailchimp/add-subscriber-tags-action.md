---
url: 'https://docs.workato.com/en/connectors/mailchimp/add-subscriber-tags-action.md'
description: >-
  The Add subscriber tags action in the MailChimp connector lets you add a tag
  to a subscriber you specify on a given list.
---

# MailChimp - Add subscriber tags action

This action adds a tag to a subscriber you specify in MailChimp.

![Add subscriber tags action](/assets/add-subscriber-tags-action.CZakRceq.png)_Add subscriber tags action_

## Input

| Input field | Description |
| --- | --- |
| List | The list that the subscriber you plan to add tags to is assigned. |
| Email address | The email address of the subscriber. |
| Tag source list | The source list of the tag. This field is optional. |
| Name | The name of the tag you plan to add to the subscriber. For example: `campaignInfluencer`. |

## Output

The output for this action is a datatree indicating the status of the object. For example, `success`, if the tag was added.

---

---
url: >-
  https://docs.workato.com/en/connectors/mailchimp/get-subscriber-activity-action.md
description: >-
  The Get subscriber activity action in the MailChimp connector lets you fetch a
  subscriber's activity on a list, including opens, clicks, and unsubscribes.
---

# MailChimp - Get subscriber activity action

This action fetches a subscriber's activity on a specific list, including opens, clicks, and unsubscribes.

![Get subscriber activity action](/assets/get-subscriber-activity-action.DPN117PW.png)_Get subscriber activity action_

## Input

| Input field | Description |
| --- | --- |
| List | The list to which the subscriber you plan to fetch activity for is assigned. |
| Email address | The email address of the subscriber. |

## Output

| Output field | Description |
| --- | --- |
| Activity type | The type of activity. For example `unsub` for unsubscribes or `generic-signup` for a general sign up. |
| Created at timestamp | The timestamp of when the activity was requested. For example: `2024-01-03T20:19:26.000000+00:00`. |
| Campaign ID | The ID of the campaign associated with the activity. This field is blank if the activity is not associated with a specific campaign. |
| Campaign title | The title of the campaign associated with the activity. This field is blank if the activity is not associated with a specific campaign. |
| Is admin unsubscribed | Indicates whether the list admin unsubscribed the contact or not. This value is `true` or `false`. |
| Unsubscribe reason | The reason the subscriber unsubscribed. For example: `N/A (Unsubscribed by admin)`. |
| Sign up category | The category for how the subscriber signed up. For example: `manual_add`. |
| Email ID | The email ID of the subscriber. For example: `49bf743a5rm9f47cjm6d83f3a8dd9661`. |
| List ID | The ID of the list where the activity was logged. For example: `91930a8a88`. |

---
