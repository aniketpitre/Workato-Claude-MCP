---
url: 'https://docs.workato.com/en/connectors/bluesky/delete-record-action.md'
description: The Delete record action enables you to delete a post in Bluesky.
---

# Bluesky - Delete record action

The **Delete record** action enables you to delete a post in Bluesky.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to delete. **Post** is the only available object for this action. |
| AT-URI | Enter the AT-URI of the post you plan to delete. |
| Record key | Enter the record key of the post you plan to delete. Provide the record key if you don't provide the AT-URI. |
| Swap record | Enter a content identifier that you plan to delete posts matching the value. |
| Swap commit | Enter a the repository's current commit identifier that you plan to delete posts matching the value. |

## Output

| Output field | Description |
| --- | --- |
| Success | True when the post was deleted. |
| AT-URI | AT-URI of the deleted post. |
| CID | Content identifier of the deleted post. |
| Commit | Repository commit for the deletion, including the following properties. |
| CID (Commit) | Content identifier of the commit. |
| Revision (Commit) | Revision of the commit. |

---
