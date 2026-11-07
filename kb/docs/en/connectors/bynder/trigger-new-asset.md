---
url: 'https://docs.workato.com/en/connectors/bynder/trigger-new-asset.md'
description: >-
  The New asset trigger in the Bynder connector fires when a new asset is added
  to the account, checking for new assets every five minutes.
---

# Bynder - New asset trigger

Triggers when a new asset is added to the Bynder account. Trigger will pick up new assets created from the time recipe has started. Checks for new assets every 5 minutes.

The trigger event contains only metadata about the file, however, such as file name and size. To retrieve content of the file, use the **Download asset in Bynder** action.

  

## Input

| Field name | Description |
| --- | --- |
| When first started, this recipe should pick up events from | When recipe starts for the first time, it will pick up CSV files created from this specified time. Once recipe has been run or tested, value cannot be changed. Learn more about this field here. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

This trigger supports [Trigger conditions](/en/recipes/triggers#trigger-conditions), which can filter incoming trigger events.

  

## Output

| Field name | Description |
| --- | --- |
| Copyright | Label for the copyright. |
| Description | Description of asset. |
| ID | ID of the asset. |
| Extension | File extension type |
| Type | Type of this asset. Possible values are `image` , `document` , `audio` , `video` , `3d`. |
| User Created | User who created the asset |
| Date Created | Date/time the asset is created |
| IdHash | Hashed Id of the asset |
| isPublic | Indicates whether or not the response should only contain assets marked as public. |
| Width | Width of an image asset |
| Height | Height of an image asset |
| Orientation | Possible values include `square` , `portrait` , `landscape` . |
| Archive | Indicates whether or not the response should only contain archived assets. When 0, no filtering happens. |
| Date Modified | Date/time the asset is modified |
| Date Published | Date/time the asset is published |
| File Size | Size of file |
| Brand Id | Id of the brand |
| Name | Name of the asset |
| Watermarked | Indicates whether or not the asset is watermarked. When 0, the asset is not watermarked. |
| Limited | Indicates whether or not the asset is hidden for users who do not have the permission to access. When 0, the asset is not labeled Limited Use. |
| Thumbnails | Preview of the asset |

---
