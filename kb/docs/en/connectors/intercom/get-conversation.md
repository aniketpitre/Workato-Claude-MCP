---
url: 'https://docs.workato.com/en/connectors/intercom/get-conversation.md'
description: >-
  The Get conversation by ID action in the Intercom connector lets you retrieve
  the details of a specific conversation by its unique identifier.
---

# Intercom - Get conversation by ID action

The **Get conversation by ID** action allows you to retrieve the details of a specific conversation in Intercom using the conversation's unique identifier.

![Get conversation by ID action](/assets/get-conversation-action.CRUsjm-N.png)_Intercom - Get conversation by ID action_

## Input

- ID
- Enter the unique identifier of the conversation you plan to retrieve.

## Output

<dl><dt>Type</dt><dd>The entity type for the conversation.</dd><dt>ID</dt><dd>The unique identifier for the conversation.</dd><dt>Created at</dt><dd>The timestamp of when the conversation was created.</dd><dt>Updated at</dt><dd>The timestamp of when the conversation was last updated.</dd><dt>User</dt><dd><dl><dt>Type</dt><dd>The entity type related to the user.</dd><dt>ID</dt><dd>The unique identifier for the user involved in the conversation.</dd></dl></dd><dt>Assignee</dt><dd><dl><dt>Type</dt><dd>The entity type for the assignee.</dd><dt>ID</dt><dd>The unique identifier for the assignee of the conversation.</dd></dl></dd><dt>Conversation message</dt><dd><dl><dt>Type</dt><dd>The entity type for the message.</dd><dt>ID</dt><dd>The unique identifier for the conversation message.</dd><dt>Subject</dt><dd>The subject of the conversation message.</dd><dt>Body</dt><dd>The body text of the conversation message.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author.</dd><dt>ID</dt><dd>The unique identifier for the author of the message.</dd></dl></dd></dl></dd><dt>Open</dt><dd>Indicates whether the conversation is open.</dd><dt>Read</dt><dd>Indicates whether the conversation has been marked as read.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for conversation parts.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for individual conversation parts.</dd><dt>ID</dt><dd>The unique identifier for each part of the conversation.</dd><dt>Part type</dt><dd>The type of conversation part.</dd><dt>Body</dt><dd>The content of the conversation part.</dd><dt>Created at</dt><dd>The timestamp of when the conversation part was created.</dd><dt>Updated at</dt><dd>The timestamp of when the conversation part was last updated.</dd><dt>Notified at</dt><dd>The timestamp of when notifications were sent for the conversation part.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author of the conversation part.</dd><dt>ID</dt><dd>The unique identifier for the author of the part.</dd></dl></dd><dt>List size</dt><dd>The total number of conversation parts associated with the conversation.</dd><dt>List index</dt><dd>The index of the particular conversation part within the list of parts.</dd></dl></dd></dl></dd></dl>

---
