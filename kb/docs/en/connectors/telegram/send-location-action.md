---
url: 'https://docs.workato.com/en/connectors/telegram/send-location-action.md'
description: >-
  Share a set of coordinates, optionally as a live-updating location, in a
  Telegram chat.
---

# Telegram - Send location action

The **Send location** action sends a point on the map to a chat in Telegram.

## Input

| Input field | Description |
| --- | --- |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. |
| Latitude | Enter the latitude of the location. |
| Longitude | Enter the longitude of the location. |
| Horizontal accuracy | Optional. Enter the radius of uncertainty for the location. Measured in meters. Valid values are 0-1500. |
| Live period | Optional. Enter the period for which the location is updated. Measured in seconds. Valid values are 60-86400. |
| Heading | Optional. Enter the direction the user is moving. Measured in degrees. Valid values are 1-360. Only used for live locations. |
| Proximity alert radius | Optional. Enter the maximum distance for proximity alerts about approaching another chat member. Measured in meters. Only used for live locations. |
| Disable notification | Optional. Select whether to send the message silently. |
| Protect content | Optional. Select whether to protect the message content from forwarding and saving. |
| Reply markup | Optional. Enter a JSON-serialized inline keyboard, custom reply keyboard, or other reply markup object. |

## Output

This action returns the sent message. Refer to the Telegram Bot API [Message](https://core.telegram.org/bots/api#message) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Message ID | The message's unique identifier inside the chat. |
| From | The bot that sent the message. |
| Chat | The chat the message was sent to. |
| Date | The Unix timestamp the message was sent. |
| Location | The sent location's latitude and longitude. |

---
