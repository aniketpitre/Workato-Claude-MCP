---
url: 'https://docs.workato.com/en/connectors/tiktok/publish-photo-carousel-action.md'
description: >-
  Publish a photo carousel to TikTok from public image URLs, as a direct post or
  a draft in the creator inbox.
---

# TikTok - Publish photo carousel action

The **Publish photo carousel** action publishes a photo carousel to TikTok from public image URLs. Select **Direct post** to publish immediately or **Upload to inbox** to send a draft to the creator inbox.

## Input

| Input field | Description |
| --- | --- |
| Post mode | Select how to publish the carousel. Options are **Direct post** or **Upload to inbox**. |
| Privacy level | Select who can see the carousel. The **Privacy level** field is required when **Post mode** is **Direct post**, and it must match one of the connected creator's privacy level options. Unaudited apps must use **Only me**. |
| Photo images | Enter up to 35 public photo URLs on a domain you [verified in your TikTok app](/en/connectors/tiktok#url-verification). |
| Photo cover index | Enter the position of the cover photo in **Photo images**, starting at `0`. |
| Title | Optional. Enter the carousel's caption, up to 90 UTF-16 runes. |
| Description | Optional. Enter the photo description, up to 4000 UTF-16 runes. |
| Disable comment | Optional. Select **Yes** to turn off comments on the carousel. Defaults to **No** if left blank. |
| Paid partnership | Optional. Select **Yes** to label the carousel as a paid partnership that promotes a third-party business. The **Paid partnership** field is only available when **Post mode** is **Direct post**. Defaults to **No** if left blank. |
| Brand organic | Optional. Select **Yes** to label the carousel as promoting the creator's own business. The **Brand organic** field is only available when **Post mode** is **Direct post**. Defaults to **No** if left blank. |
| Is AI generated content | Optional. Select **Yes** to mark the carousel as AI generated content. Defaults to **No** if left blank. |
| Auto add music | Optional. Select **Yes** to let TikTok add music to the carousel. Defaults to **No** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Publish ID | The post's unique identifier. Pass this value to the [Check post status](/en/connectors/tiktok/check-post-status-action) action to track publishing. |

---
