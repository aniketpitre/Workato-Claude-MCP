---
url: 'https://docs.workato.com/en/connectors/bynder/trigger-new-updated-asset.md'
description: >-
  The New/updated asset trigger in the Bynder connector fires when an asset is
  added or an existing asset is updated, checking every five minutes.
---

# Bynder - New/updated asset trigger

Triggers when a new asset is added to the Bynder account or existing asset in the Bynder account is updated. Trigger will pick up new assets created from the time recipe has started. Checks for new assets every 5 minutes.

Bynder allows an asset to be updated by having multiple versions. You can update the original file in Bynder while keeping all the metaproperties, tags and other information the asset is tagged with as well as any attached additional files and manual derivatives.

Refer to the Bynder [Upload New Version of an Asset](https://support.bynder.com/hc/en-us/articles/360013931859-Upload-a-New-Version) tutorial to learn how to add a new version of the asset.

This trigger supports [Trigger conditions](/en/recipes/triggers#trigger-conditions), which can filter incoming trigger events.

The trigger event contains only metadata about the file, however, such as file name and size. To retrieve content of the file, use the **Download asset in Bynder** action.

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
