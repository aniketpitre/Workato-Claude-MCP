---
url: 'https://docs.workato.com/en/connectors/intercom/add-conversation.md'
description: >-
  The Add conversation note action in the Intercom connector lets you add a note
  to an existing conversation by its conversation ID.
---

# Intercom - Add conversation note action

The **Add conversation note** action allows you to add a conversation note in Intercom.

![Add conversation note action](/assets/add-conversation-action.B3BVOTi6.png)_Intercom - Add conversation note action_

## Input

- Conversation ID
  
- Input the unique identifier of the conversation where you plan to add a note.
  
- Admin
  
- Specify the admin user within Intercom responsible for adding the note.
  
- Body
  
- Write the content of the note you plan to add to the conversation.
  

## Output

<dl><dt>Type</dt><dd>The entity type for the action.</dd><dt>ID</dt><dd>The unique identifier for the newly added conversation note.</dd><dt>Created at</dt><dd>The timestamp when the conversation note was created.</dd><dt>Updated at</dt><dd>The timestamp when the conversation note was last updated.</dd><dt>User</dt><dd><dl><dt>Type</dt><dd>The entity type related to the user.</dd><dt>ID</dt><dd>The unique identifier for the user associated with the note.</dd></dl></dd><dt>Assignee</dt><dd><dl><dt>Type</dt><dd>The entity type for the assignee of the conversation note.</dd><dt>ID</dt><dd>The unique identifier for the assignee of the conversation note.</dd></dl></dd><dt>Conversation message</dt><dd><dl><dt>Type</dt><dd>The entity type for the message.</dd><dt>ID</dt><dd>The unique identifier for the conversation message.</dd><dt>Subject</dt><dd>The subject of the conversation message.</dd><dt>Body</dt><dd>The body text of the conversation message.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author.</dd><dt>ID</dt><dd>The unique identifier for the author of the message.</dd></dl></dd></dl></dd><dt>Open</dt><dd>Indicates whether the conversation is currently open.</dd><dt>Read</dt><dd>Indicates whether the conversation has been marked as read.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for conversation parts.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for each part of the conversation.</dd><dt>ID</dt><dd>The unique identifier for each part of the conversation.</dd><dt>Part type</dt><dd>The type of conversation part.</dd><dt>Body</dt><dd>The content of the conversation part.</dd><dt>Created at</dt><dd>The timestamp when the conversation part was created.</dd><dt>Updated at</dt><dd>The timestamp when the conversation part was last updated.</dd><dt>Notified at</dt><dd>The timestamp when notifications were sent for the conversation part.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author of the conversation part.</dd><dt>ID</dt><dd>The unique identifier for the author of the part.</dd></dl></dd><dt>List size</dt><dd>The total number of conversation parts associated with the conversation.</dd><dt>List index</dt><dd>The index of the particular conversation part within the list of parts.</dd></dl></dd></dl></dd></dl>

---
