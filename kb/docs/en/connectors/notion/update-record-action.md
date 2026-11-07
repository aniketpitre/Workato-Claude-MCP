---
url: 'https://docs.workato.com/en/connectors/notion/update-record-action.md'
description: >-
  The Update record action in the Notion connector lets you update an existing
  object, such as a page, database, or block, in Notion.
---

# Notion - Update record action

The **Update record** action updates an existing object in Notion.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to update. The recipe editor generates additional input fields based on your **Object** selection. Use the generated input fields to specify the instance you plan to update. |
| Parent | Specify whether the object is a page or database. |
| Pages | Select the page to update. |
| Databases | Select the database to update. |
| Child page | Select the child element to update. |
| Block | Select the block to update. |
| Custom fields | Enter the contents to update the object with. This field contains a sub-field for each object element. |

> **UPDATE PAGE CONTENT**
> 
> Selecting **Page** in the **Object** field allows you to update a page's properties. To update a page's content instead, select the **Block** object.

## Output

| Field | Description |
| --- | --- |
| Object | The type of object updated. |
| Page ID | The identifier for the associated page. |
| Created time | The timestamp when the object was created. |
| Last edited time | The timestamp when the object was last updated. |
| Created by | Contains information about the user who created the object, such as their `User ID` and the `Object` type. |
| Last edited by | Contains information about the user who last updated the object, such as their `User ID` and the `Object` type. |
| Cover | Contains information about the updated object's cover, such as its `Type` and `URL`. |
| Icon | Contains information about the updated object's icon, such as its `Type` and associated `Emoji`. |
| Archived | Indicates whether the object is archived. |
| URL | The updated object's URL. |
| Parent | Contains information about the updated object's parent, such as its `Type` and `ID`. |
| Properties | Contains information about the updated object's properties such as its `Title`, `Type`, and `ID`. |
| Blocks | Contains information about the updated block, such as its `Block ID`, `Created time`, and `Type`. |
| Next cursor | The identifier for the next page of results. |
| Has more | Indicates if there are additional results. |

---
