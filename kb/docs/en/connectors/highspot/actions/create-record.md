---
url: 'https://docs.workato.com/en/connectors/highspot/actions/create-record.md'
description: >-
  The Create record action creates various types of records in Highspot
  including items, spots, and item versions.
---

# Highspot - Create record action

The **Create record** action creates various types of records in Highspot including items from files, items as web links, item versions, and spots.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to create. Options include: Item by file, Item as web link, Item version by file, Item version by web link, Spot |

Additional fields appear based on the object type you select.

### For items (file or web link)

| Input field | Description |
| --- | --- |
| Spot | Enter the spot ID in which to create the item. |
| File contents | Provide the binary data of the file. Required if you select **Item by file** as the **Object**. |
| URL | Enter the URL for the web link. Required if you select **Item by web link** as the **Object**. |
| Perform operation as | Enter the email address of the user to impersonate for this operation. |
| Link embed code | Enter the embed code for the web link item. Available if you select **Item by web link** as the **Object**. |
| Metadata | Provide metadata for the item. |
| Title (Metadata) | Enter the title of the item. |
| Description (Metadata) | Enter the description of the item. |
| Author (Metadata) | Enter the author of the item. |
| Date created (Metadata) | Enter the creation date of the item. |
| Internal (Metadata) | Select whether to mark the item as internal use only. |
| Custom usage label (Metadata) | Enter a custom usage label for the item. |
| Lists (Metadata) | Provide the list IDs to add the item to. |
| CMS | Provide CMS integration details. |
| ID (CMS) | Enter the CMS ID. |
| Integration (CMS) | Enter the CMS integration name. |
| Content version (CMS) | Enter the CMS content version. |
| Metadata version (CMS) | Enter the CMS metadata version. |
| Metadata (CMS) | Provide CMS metadata details. |
| Filename (Metadata) | Enter the filename in CMS metadata. |
| Author (Metadata) | Enter the author in CMS metadata. |
| Deleted (Metadata) | Select whether to mark the item as deleted. |
| Content owners (Metadata) | Specify content ownership details. |
| Users (Content owners) | Enter the user IDs for content ownership. |
| Groups (Content owners) | Enter the group IDs for content ownership. |

> **INTERNAL AND CUSTOM USAGE LABEL INTERACTION**
> 
> The most restrictive label is applied to an item if you provide both **Internal** and **Custom usage label**. For example, an item is marked as Internal if **Internal** is set to `true` and a **Custom usage label** is supplied. The custom usage label is applied if **Internal** is set to `false` and a **Custom usage label** is supplied.

### For item versions (file or web link)

| Input field | Description |
| --- | --- |
| Item ID | Enter the ID of the existing item to create a new version for. |

All other fields are the same as for creating new [items](#for-items-file-or-web-link).

### For spots

| Input field | Description |
| --- | --- |
| Title | Enter the title of the spot. |
| Description | Enter the description of the spot. |
| Visibility | Select the spot's privacy setting. Options include: Private, Public, Shared |
| Is official | Select whether to mark the spot as official. |
| Perform operation as | Enter the email address of the user to impersonate for this operation. |

## Output

- [For items and item versions](#for-items-and-item-versions)
- [For spots](#for-spots-output)

### For items and item versions

| Output field | Description |
| --- | --- |
| Item ID | The unique identifier of the created item. |
| Title | The title of the item. |
| Title external | The external title of the item. |
| Description | The description of the item. |
| Description external | The external description of the item. |
| Content name | The name of the content. |
| Content type | The type of content. |
| Mime type | The MIME type of the content. |
| Author | The author of the item. |
| Spot | The spot ID where the item was created. |
| Internal | Indicates if the item is marked as internal. |
| Lists | The list IDs the item belongs to. |
| Can download | Indicates if the item can be downloaded. |
| Date added | The timestamp when the item was added. |
| Date updated | The timestamp when the item was last updated. |
| Date original added | The original addition timestamp. |
| Expires at | The expiration timestamp for the item. |
| Available at | The availability timestamp for the item. |
| Imported at | The import timestamp. |
| Content owners | The content ownership details. |
| Users (Content owners) | The user IDs with content ownership. |
| Groups (Content owners) | The group IDs with content ownership. |
| Bookmark | The bookmark details for the item. |
| From ID (Bookmark) | The source ID for bookmarked items. |
| Original ID (Bookmark) | The original ID for bookmarked items. |

### For spots

| Output field | Description |
| --- | --- |
| Spot ID | The unique identifier of the created spot. |

---
