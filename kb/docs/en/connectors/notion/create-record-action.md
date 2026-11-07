---
url: 'https://docs.workato.com/en/connectors/notion/create-record-action.md'
description: >-
  The Create record action in the Notion connector lets you create a new object
  inside a page or database in Notion.
---

# Notion - Create record action

The **Create record** action creates a new object in Notion.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to create. |
| Parent | Specify whether to create the object inside a page or database. |
| Pages | Select the specific page to contain the new object. |
| Databases | Select the specific database to contain the new object. |
| Custom fields | Enter details for the new object. This field contains a sub-field for each object element. |

## Output

| Field | Description |
| --- | --- |
| Object | The type of object created. |
| Page ID | The unique identifier of the created page. |
| Created time | The timestamp indicating when the object was created. |
| Last edited time | The timestamp indicating when the object was last updated. |
| Created by | Contains information about the user who created the object, such as their `User ID` and the `Object` type. |
| Last edited by | Contains information about the user who last updated the object, such as their `User ID` and the `Object` type. |
| Cover | Contains information about the new object's cover, such as its `Type` and `URL`. |
| Icon | Contains information about the new object's icon, such as its `Type` and associated `Emoji`. |
| Archived | Indicates whether the object is archived. |
| URL | The created object's URL. |
| Parent | Contains information about the new object's parent, such as its `Type` and `ID`. |
| Properties | Contains information about the new object's properties, such as its `Title`, `Type`, and `ID`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/notion/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action in the Notion connector retrieves data
  about a page, database, or block object in Notion.
---

# Notion - Get record details by ID action

The **Get record details by ID** action retrieves data about an object in Notion.

## Input

| Field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |
| Pages | Select the page to retrieve details from. |
| Databases | Select the database to retrieve data from. |
| Block ID | Provide the internal ID of the block to retrieve. |

## Output

| Field | Description |
| --- | --- |
| Object | The type of object retrieved. |
| Page ID | The unique identifier of the retrieved page. |
| Created time | The timestamp when the object was created. |
| Last edited time | The timestamp when the object was last updated. |
| Created by | Contains information about the user who created the object, such as their `User ID` and the `Object` type. |
| Last edited by | Contains information about the user who last updated the object, such as their `User ID` and the `Object` type. |
| Cover | Contains information about the retrieved object's cover, such as its `Type` and `URL`. |
| Icon | Contains information about the retrieved object's icon, such as its `Type` and associated `Emoji`. |
| Archived | Indicates whether the object is archived. |
| URL | The object's URL. |
| Parent | Contains information about the retrieved object's parent, such as its `Type` and `ID`. |
| Properties | Contains information about the retrieved object's properties, such as its `Title`, `Type`, and `ID`. |

---
