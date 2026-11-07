---
url: 'https://docs.workato.com/en/connectors/intercom/new-conversation.md'
description: >-
  The New conversation trigger in the Intercom connector fires when a new
  conversation is created, checking for new ones on the trigger poll interval.
---

# Intercom - New conversation trigger

The **New conversation** trigger activates when a new conversation is created in Intercom. This trigger initially retrieves conversations created up to one hour before its activation. It then continues to check for new conversations based on the trigger poll interval.

![New conversation in Intercom trigger](/assets/new-conversation-trigger.RABzUYnf.png)_Intercom - New conversation trigger_

## Input

- Trigger poll interval
- Determines the frequency of the event check. You can choose a specific interval from the drop-down menu or leave it at the default setting.

## Output

<dl><dt>Type</dt><dd>The entity type for the trigger.</dd><dt>ID</dt><dd>The unique identifier for the conversation in Intercom.</dd><dt>Created at</dt><dd>The timestamp of when the conversation was created.</dd><dt>Updated at</dt><dd>The timestamp of when the conversation was last updated.</dd><dt>User</dt><dd><dl><dt>Type</dt><dd>The entity type related to the user.</dd><dt>ID</dt><dd>The unique identifier for the user involved in the conversation.</dd></dl></dd><dt>Assignee</dt><dd><dl><dt>Type</dt><dd>The entity type for the assignee.</dd><dt>ID</dt><dd>The unique identifier for the assignee of the conversation.</dd></dl></dd><dt>Conversation message</dt><dd><dl><dt>Type</dt><dd>The entity type for the message.</dd><dt>ID</dt><dd>The unique identifier for the conversation message.</dd><dt>Subject</dt><dd>The subject of the conversation message.</dd><dt>Body</dt><dd>The body text of the conversation message.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author.</dd><dt>ID</dt><dd>The unique identifier for the author of the message.</dd></dl></dd></dl></dd><dt>Open</dt><dd>Indicates whether the conversation is open.</dd><dt>Read</dt><dd>Indicates whether the conversation has been marked as read.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for conversation parts.</dd><dt>Conversation parts</dt><dd><dl><dt>Type</dt><dd>The entity type for individual conversation parts.</dd><dt>ID</dt><dd>The unique identifier for each part of the conversation.</dd><dt>Part type</dt><dd>The type of conversation part.</dd><dt>Body</dt><dd>The content of the conversation part.</dd><dt>Created at</dt><dd>The timestamp of when the conversation part was created.</dd><dt>Updated at</dt><dd>The timestamp of when the conversation part was last updated.</dd><dt>Notified at</dt><dd>The timestamp of when notifications were sent for the conversation part.</dd><dt>Author</dt><dd><dl><dt>Type</dt><dd>The entity type for the author of the conversation part.</dd><dt>ID</dt><dd>The unique identifier for the author of the part.</dd></dl></dd><dt>List size</dt><dd>The total number of conversation parts associated with the conversation.</dd><dt>List index</dt><dd>The index of the particular conversation part within the list of parts.</dd></dl></dd></dl></dd></dl>

---
