---
url: 'https://docs.workato.com/en/connectors/telegram/send-venue-action.md'
description: >-
  Share a named venue's address and location, optionally with a Foursquare or
  Google Places ID, in a Telegram chat.
---

# Telegram - Send venue action

The **Send venue** action sends information about a venue to a chat in Telegram.

## Input

| Input field | Description |
| --- | --- |
| Chat ID | Enter the unique identifier for the target chat or the username of the target channel. |
| Latitude | Enter the latitude of the venue. |
| Longitude | Enter the longitude of the venue. |
| Title | Enter the name of the venue. |
| Address | Enter the address of the venue. |
| Foursquare ID | Optional. Enter the Foursquare identifier of the venue. |
| Google place ID | Optional. Enter the Google Places identifier of the venue. |
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
| Venue | The sent venue's title, address, and location. |

---
