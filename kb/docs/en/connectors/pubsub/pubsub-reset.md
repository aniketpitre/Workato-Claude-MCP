---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-reset.md'
description: >-
  Reset a Workato Event streams topic to clear all of its messages, which is
  useful after an incompatible schema change or invalid data.
---

# Resetting the Event topic

You might need to clear the topic of all messages. This might be useful if you change the message schema to a schema that is incompatible with the old one, or if the topic was populated with invalid data. To reset the topic:

1. Open the **Settings** tab.
   
2. Click **Reset**.
   
3. Confirm resetting the topic in the prompt window.
   

> **ACCESS TO PREVIOUSLY PUBLISHED MESSAGES**
> 
> This action cannot be undone and you cannot access any messages published prior to resetting the topic.

![Topic reset](/assets/reset-topic.D_e4dWkX.png)_Topic reset_

---
