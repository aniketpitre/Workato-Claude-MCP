---
url: 'https://docs.workato.com/en/connectors/tiktok/get-record-action.md'
description: >-
  Retrieve the connected TikTok user's profile, or the creator posting limits
  and privacy options for publishing.
---

# TikTok - Get record action

The **Get record** action retrieves a record for the connected user in TikTok. Select **User** to retrieve the user's profile, or **Creator info** to retrieve the posting limits and privacy options that apply when you publish.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type. Options are **User** or **Creator info**. |
| Fields | Optional. Select the fields to return for the connected user. Leave blank to return all user fields. The **Fields** field is only available when **Object** is **User**. |

## Output

Output fields dynamically generate based on the **Object** you select. The following are a representative set of output fields. Refer to the [TikTok API](https://developers.tiktok.com/doc/tiktok-api-v2-introduction) documentation for more information on available output fields.

### User output

The following fields are available when **Object** is **User**.

| Output field | Description |
| --- | --- |
| Open ID | The user's unique ID for your developer app. |
| Union ID | The user's unique ID across all of your developer apps. |
| Display name | The user's display name. |
| Username | The user's TikTok username. |
| Follower count | The number of followers the user has. |
| Video count | The number of public videos the user has posted. |

### Creator info output

The following fields are available when **Object** is **Creator info**.

| Output field | Description |
| --- | --- |
| Creator username | The creator's TikTok username. |
| Creator nickname | The creator's display nickname. |
| Privacy level options | The privacy levels the creator can publish with, for example `FOLLOWER_OF_CREATOR` or `SELF_ONLY`. |
| Max video post duration (sec) | The maximum length, in seconds, of a video the creator can post. |

---
