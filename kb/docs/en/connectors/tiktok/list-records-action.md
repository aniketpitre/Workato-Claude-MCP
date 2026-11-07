---
url: 'https://docs.workato.com/en/connectors/tiktok/list-records-action.md'
description: >-
  List a TikTok user's public videos with paging, or retrieve specific videos by
  video ID.
---

# TikTok - List records action

The **List records** action lists public videos for the connected user in TikTok. Enter **Video IDs** to retrieve specific videos, or leave **Video IDs** blank to page through the user's public videos.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type. The only option is **Video**. |
| Video IDs | Optional. Enter up to 20 video IDs owned by the connected user. Leave blank to page through the user's public videos. |
| Cursor | Optional. Enter a UTC Unix timestamp in milliseconds. Use the **Cursor** value from the previous response when **Has more** is `true`. The **Cursor** field is only available when **Video IDs** is blank. |
| Max count | Optional. Enter the number of videos to return per page. Valid values are 1-20. Defaults to `10` if left blank. The **Max count** field is only available when **Video IDs** is blank. |
| Fields | Optional. Select the fields to return for each video. Leave blank to return all video fields. |

## Output

The following are a representative set of output fields. Refer to the [TikTok API](https://developers.tiktok.com/doc/tiktok-api-v2-introduction) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Videos | The videos that match your request. |
| ID (Videos) | The video's unique identifier. |
| Title (Videos) | The video's title. |
| Share URL (Videos) | The video's public share URL. |
| Like count (Videos) | The number of likes the video received. |
| Comment count (Videos) | The number of comments the video received. |
| Share count (Videos) | The number of times viewers shared the video. |
| View count (Videos) | The number of views the video received. |
| Cursor | The timestamp to pass as **Cursor** in your next request. The **Cursor** field is only available when **Video IDs** is blank. |
| Has more | A boolean value (`true` or `false`) that indicates whether more videos are available. The **Has more** field is only available when **Video IDs** is blank. |

---
