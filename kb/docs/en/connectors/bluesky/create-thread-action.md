---
url: 'https://docs.workato.com/en/connectors/bluesky/create-thread-action.md'
description: The Create thread action enables you to create a multi-post thread in Bluesky.
---

# Bluesky - Create thread action

The **Create thread** action creates a multi-post thread in Bluesky. The first post you provide becomes the thread root, and each following post replies to the one before it.

## Input

| Input field | Description |
| --- | --- |
| Posts | Enter an ordered list of posts to create. Each post has the following input fields: `Posts source list`, `Posts fields`, `Text`, `Facets`, `Labels`, `Video`, `External`. |

## Output

| Output field | Description |
| --- | --- |
| Posts | List of created posts, in the order you provided them, including the following properties. |
| AT-URI (Post) | Unique identifier of the post. |
| CID (Post) | Content identifier of the post. |
| Commit (Post) | Repository commit for the write, including the following properties. |
| CID (Commit) | Content identifier of the commit. |
| Revision (Commit) | Revision of the commit. |
| Validation status (Post) | Result of validating the post against the Bluesky lexicon. |

---
