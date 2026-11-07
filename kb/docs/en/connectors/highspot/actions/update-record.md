---
url: 'https://docs.workato.com/en/connectors/highspot/actions/update-record.md'
description: The Update record action updates existing items and spots in Highspot.
---

# Highspot - Update record action

The **Update record** action updates existing items and spots in Highspot.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to update. Options include: Item, Spot |

Additional fields appear based on the object type you select.

### For items

| Input field | Description |
| --- | --- |
| Item ID | Enter the ID of the item to update. |
| Perform operation as | Enter the email address of the user to impersonate for this operation. |
| Title | Enter the updated title of the item. |
| Description | Enter the updated description of the item. |
| Author | Enter the updated author of the item. |
| Date created | Enter the updated creation date of the item. |
| Internal | Select whether to mark the item as internal use only. |
| Custom usage label | Enter an updated custom usage label for the item. |
| Lists | Provide the updated list IDs for the item. |
| CMS | Provide CMS integration details. |
| ID (CMS) | Enter the CMS ID. |
| Integration (CMS) | Enter the CMS integration name. |
| Content version (CMS) | Enter the CMS content version. |
| Metadata version (CMS) | Enter the CMS metadata version. |
| Metadata (CMS) | Provide CMS metadata details. |
| Filename (Metadata) | Enter the filename in CMS metadata. |
| Author (Metadata) | Enter the author in CMS metadata. |
| Deleted | Select whether to mark the item as deleted. |
| Content owners | Specify updated content ownership details. |
| Users (Content owners) | Enter the user IDs for content ownership. |
| Groups (Content owners) | Enter the group IDs for content ownership. |

> **INTERNAL AND CUSTOM USAGE LABEL INTERACTION**
> 
> The most restrictive label is applied to an item if you provide both **Internal** and **Custom usage label**. For example, an item is marked as Internal if **Internal** is set to `true` and a **Custom usage label** is supplied. The custom usage label is applied if **Internal** is set to `false` and a **Custom usage label** is supplied.

### For spots

| Input field | Description |
| --- | --- |
| Spot ID | Enter the ID of the spot to update. Note that you can only update either **Visibility** or **Is official** at a single time, not both. |
| Visibility | Select the updated spot privacy setting. Options include: Private, Public, Shared |
| Is official | Select whether to mark the spot as official. |
| Perform operation as | Enter the email address of the user to impersonate for this operation. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the update operation. |

---
