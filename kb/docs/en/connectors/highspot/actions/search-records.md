---
url: 'https://docs.workato.com/en/connectors/highspot/actions/search-records.md'
description: >-
  The Search records action searches for items or spots in Highspot that match
  your search criteria.
---

# Highspot - Search records action

The **Search records** action searches for items or spots in Highspot. The action returns results that match all your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to search. Options include: Item, Spot |

Additional fields appear based on the object type you select.

### For items

| Input field | Description |
| --- | --- |
| Spot ID | Enter the spot ID to search within. |
| List ID | Enter the list ID to filter results by list. |
| Offset | Enter the starting position of the results to be displayed. Default value is 0. |
| Limit | Enter the number of results to return. Maximum is 100. |
| Perform operation as | Enter the email address of the user to impersonate for this operation. |

### For spots

| Input field | Description |
| --- | --- |
| Filter by role | Select the role to filter spots by. Options include: Editor, Viewer, Manager, Owner Note that role and role permissions can't be combined. |
| Filter by role permissions | Select the permission level to filter spots by. Options include: View, Edit, Manage Note that role and role permissions can't be combined. |
| Show only official roles? | Select whether to show only official spots. |
| Offset | Enter the starting position of the results to be displayed. Default value is 0. |
| Limit | Enter the number of results to return. Maximum is 100. |
| Perform operation as | Enter the email address of the user to impersonate for this operation. |

## Output

| Output field | Description |
| --- | --- |
| {Collection} | The list of records matching the search criteria. |

### For items

| Output field | Description |
| --- | --- |
| Item ID (Items) | The unique identifier of the item. |
| Title (Items) | The title of the item. |
| Title external (Items) | The external title of the item. |
| Description (Items) | The description of the item. |
| Description external (Items) | The external description of the item. |
| Content name (Items) | The name of the content. |
| Content type (Items) | The type of content. |
| Mime type (Items) | The MIME type of the content. |
| Author (Items) | The author of the item. |
| Spot (Items) | The spot ID where the item exists. |
| Internal (Items) | Indicates if the item is marked as internal. |
| Lists (Items) | The list IDs the item belongs to. |
| Can download (Items) | Indicates if the item can be downloaded. |
| Date added (Items) | The timestamp when the item was added. |
| Date updated (Items) | The timestamp when the item was last updated. |
| Date original added (Items) | The original addition timestamp. |
| Expires at (Items) | The expiration timestamp for the item. |
| Available at (Items) | The availability timestamp for the item. |
| Imported at (Items) | The import timestamp. |
| Content owners (Items) | The content ownership details. |
| Users (Content owners) | The user IDs with content ownership. |
| Groups (Content owners) | The group IDs with content ownership. |
| Bookmark (Items) | The bookmark details for the item. |
| From ID (Bookmark) | The source ID for bookmarked items. |
| Original ID (Bookmark) | The original ID for bookmarked items. |

### For spots

| Output field | Description |
| --- | --- |
| ID (Spots) | The unique identifier of the spot. |
| Title (Spots) | The title of the spot. |
| Description (Spots) | The description of the spot. |
| Is official (Spots) | Indicates if the spot is marked as official. |

---
