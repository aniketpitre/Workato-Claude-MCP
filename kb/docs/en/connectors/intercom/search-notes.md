---
url: 'https://docs.workato.com/en/connectors/intercom/search-notes.md'
description: >-
  The Search notes by user action in the Intercom connector lets you retrieve
  the list of notes associated with a specific user by their unique ID.
---

# Intercom - Search notes by user action

The **Search notes by user** action allows you to retrieve a list of notes associated with a specific user in Intercom based on the user's unique identifier.

![Search notes by user action](/assets/search-notes-action.Br9YH5FY.png)_Intercom - Search notes by user action_

## Input

- User ID
- Enter the unique identifier for the user whose notes you plan to search.

## Output

<dl><dt>Notes</dt><dd><dl><dt>Type</dt><dd>The type of entity.</dd><dt>ID</dt><dd>The unique identifier for the note.</dd><dt>Created at</dt><dd>The timestamp of when the note was created.</dd><dt>Body</dt><dd>The content of the note.</dd><dt>User</dt><dd><dl><dt>Type</dt><dd>The type of entity.</dd><dt>ID</dt><dd>The unique identifier of the user associated with the note.</dd></dl></dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The type of entity, indicating the author's role.</dd><dt>ID</dt><dd>The unique identifier for the author of the note.</dd><dt>Name</dt><dd>The full name of the author.</dd></dl></dd><dt>List size</dt><dd>The total number of notes retrieved.</dd><dt>List index</dt><dd>The index of the note within the list of retrieved notes.</dd></dl></dd></dl>

---
