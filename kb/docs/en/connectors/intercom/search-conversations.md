---
url: 'https://docs.workato.com/en/connectors/intercom/search-conversations.md'
description: >-
  The Search conversations by user action in the Intercom connector lets you
  retrieve the conversations associated with a specific user by their ID.
---

# Intercom - Search conversations by user action

The **Search conversations by user** action allows you to retrieve a list of conversations associated with a specific user in Intercom based on the user's unique identifier.

![Search conversations action](/assets/search-conversations-action.BsFjbnzd.png)_Intercom - Search conversations by user action_

## Input

- User ID
- Enter the unique identifier for the user whose conversations you plan to search.

## Output

<dl><dt>Conversations</dt><dd>A list of conversations associated with the user.</dd><dd><dl><dt>Type</dt><dd>The type of record.</dd><dt>ID</dt><dd>The unique identifier for the conversation.</dd><dt>Created at</dt><dd>Timestamp of when the conversation was created.</dd><dt>Updated at</dt><dd>Timestamp of the last update to the conversation.</dd><dt>User</dt><dd><dl><dt>Type</dt><dd>The type of associated entity.</dd><dt>ID</dt><dd>The unique identifier of the user involved in the conversation.</dd></dl></dd><dt>Assignee</dt><dd><dl><dt>Type</dt><dd>The type of associated entity.</dd><dt>ID</dt><dd>The unique identifier of the assignee for the conversation.</dd></dl></dd><dt>Conversation message</dt><dd><dl><dt>Type</dt><dd>The type of record.</dd><dt>ID</dt><dd>The unique identifier for the message within the conversation.</dd><dt>Subject</dt><dd>The subject line of the message.</dd><dt>Body</dt><dd>The content body of the message.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The type of entity, indicating the author's role.</dd><dt>ID</dt><dd>The unique identifier of the author of the message.</dd></dl></dd></dl></dd><dt>Open</dt><dd>Indicates if the conversation is currently open.</dd><dt>Read</dt><dd>Indicates if the conversation has been read.</dd><dt>List size</dt><dd>The number of conversations retrieved.</dd><dt>List index</dt><dd>The index of the current conversation in the list.</dd></dl></dd></dl>

---
