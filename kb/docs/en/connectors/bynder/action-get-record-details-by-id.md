---
url: >-
  https://docs.workato.com/en/connectors/bynder/action-get-record-details-by-id.md
description: >-
  The Get record details by ID action in the Bynder connector retrieves an
  asset, asset usage, or metaproperty record using its unique Bynder ID.
---

# Bynder - Get record details by ID action

This action will get record details by id in Bynder. Retrieves data for a specific asset (Asset usage, Asset, Metaproperty) by Bynder's unique ID.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object you want this action to search for. |
| Object-specific search fields | After selecting the object you want to search, you'll be shown search fields relating to the object. You can search using any standard fields. |
| Object ID **Required** | Object ID to retrieve. ID can be found at the end of the URL. |

After selecting the object you want to search, you'll be prompted for search criteria to search by. You can search by any standard fields.

  

## Output

Object specific output fields will be dynamically rendered based on the objects you select.

  

### Asset Output fields

| Field name | Description |
| --- | --- |
| Asset ID | ID of the asset. |
| Name | Name of the asset |
| Description | Description of asset. |
| IdHash | Hashed Id of the asset |
| Brand Id | Id of the brand |
| Archive | Indicates whether or not the response should only contain archived assets. When 0, no filtering happens. |
| Copyright | Label for the copyright. |
| Type | Type of this asset. Possible values are `image` , `document` , `audio` , `video` , `3d`. |
| Date Published | Date/time the asset is published |
| Date Created | Date/time the asset is created |
| User Created | User who created the asset |
| Date Modified | Date/time the asset is modified |
| isPublic | Indicates whether or not the response should only contain assets marked as public |
| Extension | File extension type |
| Tags | List of tags associated with the asset |
| Height | Height of an image asset |
| Width | Width of an image asset |
| File Size | Size of file |
| Orientation | Possible values include `square` , `portrait` , `landscape` . |
| Watermarked | Indicates whether or not the asset is watermarked. When 0, the asset is not watermarked. |
| Limited | Indicates whether or not the asset is hidden for users who do not have the permission to access. When 0, the asset is not labeled Limited Use. |
| Thumbnails | Preview of the asset |
| Media items | List of different media items (derivatives) available for each asset. |
| Active Original Focus Point | Coordinates of the focus point. View how to [set focus point](https://support.bynder.com/hc/en-us/articles/360013931299-Set-the-focus-point) in Bynder. |

  

### Asset Usage Output fields

Asset usage information allows you to keep track of assets being exported from Bynder and imported into a third party application.

| Field name | Description |
| --- | --- |
| Id | Asset usage Id |
| Asset Id | Id of the asset |
| URI | URL to directly go to the page where the asset is used |
| Additional | Additional comments or description |
| Integration | Integration Id and Description |
| Timestamp | Date/time of the integration |

  

### Metaproperty Output fields

| Field name | Description |
| --- | --- |
| Name | Metaproperty Name |
| Label | Metaproperty Label |
| Z index | The Z-index specifies the order in which the metaproperty options are displayed. The lower the Z-index value, the higher the metaproperty option will be displayed in the list. |
| Id | Metaproperty Id |
| Type | Comma-separated list of asset types for the filtered results |
| Options | List of metaproperty options |
| Is multiselect | Indicates whether or not the metaproperty is multiselect. Default is 0. |
| Is multifilter | Indicates whether or not the metaproperty is multifilter. Default is 0. |
| Is required | Indicates whether or not the metaproperty is required. Default is 0. |
| Is mainFilter | Indicates whether or not the metaproperty is the main filter. Default is 0. |
| Is API field | Indicates whether or not the metaproperty is the API field. Default is 0. |
| Is display field | Indicates whether or not the metaproperty is displayed on the Asset detail page. Default is 0. |
| Is drilldown | Indicates whether or not the metaproperty can be filtered as drilldown results. Default is 1. |
| Is searchable | Indicates whether or not the metaproperty can be filtered by searching. Default is 1. |
