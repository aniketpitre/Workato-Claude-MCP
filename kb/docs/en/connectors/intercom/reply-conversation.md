---
url: 'https://docs.workato.com/en/connectors/intercom/reply-conversation.md'
description: >-
  The Reply to conversation as user action in the Intercom connector lets you
  reply to an existing conversation as a specified Intercom user.
---

# Intercom - Reply to conversation as user action

The **Reply to conversation as user** action allows you to reply to an existing conversation as an Intercom user.

![Create users action](/assets/reply-conversation-action.CigvB1jG.png)_Intercom - Reply to conversation as user action_

## Input

- Conversation ID
  
- Enter the unique identifier for the conversation you are replying to.
  
- User ID
  
- Specify the user ID of the Intercom user sending the reply.
  
- Reply text
  
- Type the message text you plan to send as the reply to the conversation.
  

## Output

<dl><dt>Type</dt><dd>The entity type for the conversation.</dd><dt>ID</dt><dd>The unique identifier for the conversation.</dd><dt>Created at</dt><dd>The timestamp of when the conversation was created.</dd><dt>Updated at</dt><dd>The timestamp of when the conversation was last updated.</dd><dt>User</dt><dd><dl><dt>Type</dt><dd>The entity type related to the user.</dd><dt>ID</dt><dd>The unique identifier for the user involved in the conversation.</dd></dl></dd><dt>Assignee</dt><dd><dl><dt>Type</dt><dd>The entity type for the assignee.</dd><dt>ID</dt><dd>The unique identifier for the assignee of the conversation.</dd></dl></dd><dt>Conversation message</dt><dd><dl><dt>Type</dt><dd>The entity type for the message.</dd><dt>ID</dt><dd>The unique identifier for the conversation message.</dd><dt>Subject</dt><dd>The subject of the conversation message.</dd><dt>Body</dt><dd>The body text of the conversation message.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author.</dd><dt>ID</dt><dd>The unique identifier for the author of the message.</dd></dl></dd></dl></dd><dt>Open</dt><dd>Indicates whether the conversation is open.</dd><dt>Read</dt><dd>Indicates whether the conversation has been marked as read.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for conversation parts.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for individual conversation parts.</dd><dt>ID</dt><dd>The unique identifier for each part of the conversation.</dd><dt>Part type</dt><dd>The type of conversation part.</dd><dt>Body</dt><dd>The content of the conversation part.</dd><dt>Created at</dt><dd>The timestamp of when the conversation part was created.</dd><dt>Updated at</dt><dd>The timestamp of when the conversation part was last updated.</dd><dt>Notified at</dt><dd>The timestamp of when notifications were sent for the conversation part.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author of the conversation part.</dd><dt>ID</dt><dd>The unique identifier for the author of the part.</dd></dl></dd><dt>List size</dt><dd>The total number of conversation parts associated with the conversation.</dd><dt>List index</dt><dd>The index of the particular conversation part within the list of parts.</dd></dl></dd></dl></dd></dl>

---
