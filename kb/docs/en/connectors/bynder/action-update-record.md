---
url: 'https://docs.workato.com/en/connectors/bynder/action-update-record.md'
description: >-
  The Update record action in the Bynder connector updates the values or content
  of an existing asset or collection, subject to the required security roles.
---

# Bynder - Update record action

This action allows you to update the values or content of any existing `asset` or `collection`.

Note that updating an asset in Bynder requires the `MEDIAEDIT` security role and the `MARKPUBLIC` security role in order to change an asset's `isPublic` state.

Updating collection in Bynder also requires the `COLLECTIONS` security role and the `PUBLISHCOLLECTIONS` security role in order to change a collection's `isPublic` state.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object (asset or collection) you want this action to update. |
| Object-specific search fields | After selecting the object you want to search, you'll be shown search fields relating to the object. You can search using any standard fields. |

  

### Asset fields

| Field name | Description |
| --- | --- |
| Asset ID **Required** | ID of the asset. |
| Name | Name of the asset |
| Description | Description of asset. |
| Copyright | Label for the copyright information of the asset. |
| Date Published | Date/time the asset is published |
| Tags | Comma-separated list of tags related to the asset. |
| Metaproperty Id | Metaproperty options to set on the asset. |
| Brand Id | Id of the brand associated with the asset |
| Archive | The archived state of the asset. |
| Archive Date | Archive datetime. |
| Watermarked | Indicates whether or not the asset is watermarked. When 0, the asset is not watermarked. |
| Watermark Date | Watermark datetime. |
| Limited | Indicates whether or not the asset is hidden for users who do not have the permission to access. When 0, the asset is not labeled Limited Use. |
| Limited Date | Limited datetime. |
| isPublic | Indicates whether or not the response should only contain assets marked as public. |

  

### Collection fields

| Field name | Description |
| --- | --- |
| Collection ID **Required** | ID of the collection. |
| Collection Name | Name of the collection |
| Collection Description | Description of collection. |
| Public state of the collection | The state of whether the collection is public or not |

---
