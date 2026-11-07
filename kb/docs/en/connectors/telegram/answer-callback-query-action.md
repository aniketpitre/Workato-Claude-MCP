---
url: >-
  https://docs.workato.com/en/connectors/telegram/answer-callback-query-action.md
description: >-
  Show a notification, alert, or URL to a Telegram user after they tap an inline
  keyboard button on your bot's message.
---

# Telegram - Answer callback query action

The **Answer callback query** action responds to a callback query sent when a user taps an inline keyboard button in Telegram.

## Input

| Input field | Description |
| --- | --- |
| Callback query ID | Enter the unique identifier of the query to answer. |
| Text | Optional. Enter the text of the notification. Leave this field blank to not display a notification. |
| Show alert | Optional. Select **Yes** or **No** to show an alert instead of a notification at the top of the chat screen. |
| URL | Optional. Enter a URL to open in the user's client, such as a link to a game accepted through @BotFather. |
| Cache time | Optional. Enter the maximum number of seconds that the result of the callback query may be cached client-side. Defaults to `0`. |

## Output

| Output field | Description |
| --- | --- |
| Is answered? | A boolean response (`true` or `false`) that indicates if the request was successful. |
