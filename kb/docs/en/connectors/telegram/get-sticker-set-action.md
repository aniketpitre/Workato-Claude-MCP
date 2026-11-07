---
url: 'https://docs.workato.com/en/connectors/telegram/get-sticker-set-action.md'
description: >-
  Look up a Telegram sticker set's stickers, type, and thumbnail image by its
  unique name.
---

# Telegram - Get sticker set action

The **Get sticker set** action retrieves a sticker set by name in Telegram.

## Input

| Input field | Description |
| --- | --- |
| Name | Enter the name of the sticker set. |

## Output

| Output field | Description |
| --- | --- |
| Name | The sticker set's name. |
| Title | The sticker set's title. |
| Sticker type | The sticker set's type. Options are `regular`, `mask`, and `custom_emoji`. |
| Is animated | A boolean response (`true` or `false`) that indicates if the sticker set contains animated stickers. |
| Is video | A boolean response (`true` or `false`) that indicates if the sticker set contains video stickers. |
| Stickers | The stickers in the set. |
| Thumbnail | The sticker set's thumbnail image, if any. |

---
