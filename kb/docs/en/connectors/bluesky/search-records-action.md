---
url: 'https://docs.workato.com/en/connectors/bluesky/search-records-action.md'
description: >-
  The Search records action enables you to search and retrieve a list of likes
  or followers in Bluesky.
---

# Bluesky - Search records action

The **Search records** action enables you to search and retrieve a list of likes or followers in Bluesky.

## Input

Input fields are dynamically generated based on the object you select. The following fields are common to all object types. Refer to the [Bluesky API documentation](https://docs.bsky.app/docs/api) for more information on available output fields.

| Input field | Description |
| --- | --- |
| Object | Select the object to search and retrieve records for. |
| Limit | Maximum number of results per page. Accepts a value from `1` to `100`. Defaults to `50` if left blank. |
| Cursor | Pagination cursor from a previous response. |

## Output

Output fields are dynamically generated based on the object you select. Refer to the [Bluesky API documentation](https://docs.bsky.app/docs/api) for more information on available output fields.

---
