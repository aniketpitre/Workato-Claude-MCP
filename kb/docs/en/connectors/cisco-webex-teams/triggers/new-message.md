---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/triggers/new-message.md
description: >-
  The New message trigger in the Cisco Webex Teams connector fires in real time
  when a new message is posted in a selected room.
---

# Cisco Webex Teams - New message trigger (real-time)

This trigger monitors new messages in your Cisco Webex Teams instance in real-time. Workato processes each message as a separate job.

> **USING THIS TRIGGER WITH BOT ACCESS TOKEN AUTHENTICATION**
> 
> To ensure new messages sent to the bot are processed, tag the bot in the message. For example, `@bot_name new message`.
> 
> Additionally, due to API response times, this trigger may experience delays. To minimize delays, bot users should avoid sending messages less than three seconds apart. If a message doesn’t trigger a job, try sending another message to process the previous job.

## Input

| Field | Description |
| --- | --- |
| Room name | Select the room from which to receive messages. You can choose from a list of rooms or use a specific room ID. |
| Max | Specify the number of existing messages to retrieve starting from the latest. Defaults to 1. |

## Output

| Field | Description |
| --- | --- |
| Room type | The type of room where the message was posted. |
| Message | The content of the message. |
| Message ID | The unique identifier of the message. |
| Room ID | The unique identifier of the room. |
| Person ID | The unique identifier of the person who sent the message. |
| Person email | The email address of the person who sent the message. |
| Created | The timestamp when the message was created. |
