---
url: 'https://docs.workato.com/en/connectors/bluesky/create-record-action.md'
description: The Create record action enables you to create a post in Bluesky.
---

# Bluesky - Create record action

The **Create record** action enables you to create a post in Bluesky.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create. **Post** is the only available object for this action. |
| Text | Post text. |
| Languages | Comma-separated language codes. For example, `en,th`. |
| Created at | Select a date and time to determine the post's timestamp. |
| Validate | Select whether to validate the record against the lexicon. |
| Reply parent AT-URI | AT-URI of the post you're replying to. Leave blank to create a standalone post. |
| Facets | Enter any rich-text facets you plan to include in the post. |
| Tags | Enter any hashtags you plan to include associate with the post. |
| Labels | Enter any self-labels or content warnings you plan to include associate with the post. |
| Video | Determine if the post includes an embedded video. |
| External | Determine if the post includes an external link card. |

## Output

| Output field | Description |
| --- | --- |
| AT-URI | Unique identifier of the created post. |
| CID | Content identifier of the created post. |
| Commit | Repository commit for the write, including the following properties. |
| CID (Commit) | Content identifier of the commit. |
| Revision (Commit) | Commit revision. |
| Validation status | Result of validating the post against the Bluesky lexicon. |

---
