---
url: 'https://docs.workato.com/en/connectors/ghost/search-records-action.md'
description: >-
  The Search records action searches and retrieves a list of posts or members in
  Ghost.
---

# Ghost - Search records action

The **Search records** action searches and retrieves a list of posts or members in Ghost.

## Input

Input fields dynamically generate based on the object you select. The following fields are common to all objects. Refer to the [Ghost Admin API](https://docs.ghost.org/admin-api) documentation for filter and include syntax specific to each object.

| Input field | Description |
| --- | --- |
| Object type | Select the object to search. You can select `Post` or `Member`. |
| Filter | Enter a Ghost NQL filter. For example, `status:published` for posts or `email:jamie@example.com` for members. |
| Include | Select related data to include. Available options depend on the object you select. |
| Order by | Select the sort criteria. For example, `published_at`. |
| Sort order | Select the sort order. For example, `desc`. |
| Page | Enter the page number to retrieve. Defaults to `1` if left blank. |
| Limit | Enter the number of results per page. Defaults to `15` if left blank. Use `all` to fetch every page. |

## Output

Output fields dynamically generate based on the object you select. The following fields are common to all objects. Refer to the [Ghost Admin API](https://docs.ghost.org/admin-api) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Records | List of posts or members matching the search. |

---
