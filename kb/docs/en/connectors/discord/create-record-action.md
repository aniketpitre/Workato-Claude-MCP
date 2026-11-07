---
url: 'https://docs.workato.com/en/connectors/discord/create-record-action.md'
description: The Create record action creates a record in Discord.
---

# Discord - Create record action

The **Create record** action creates a record in Discord.

## Input

| Input field | Description |
| --- | --- |
| Object | Select an object. Objects include `Message` and `Reaction`. |

The remaining input fields vary based on the object you select. Refer to the [Discord](https://docs.discord.com/developers/interactions/application-commands) guide for more information on available objects and fields.

## Output

The output of this action varies based on the object you select. Refer to the Discord guide link in the [Input](#input) section for more information on available objects and fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/discord/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action retrieves a specific record with its ID in
  Discord.
---

# Discord - Get record details by ID action

The **Get record details by ID** action retrieves details of a specific record with its ID in Discord.

## Input

| Input field | Description |
| --- | --- |
| Object | Select an object. Objects include `User` and `Guild member`. |
| User ID | Enter the user ID. |
| Guild ID | Enter the guild ID. |

## Output

| Output field | Description |
| --- | --- |
| User ID | The user ID. |
| Username | The username. |
| Avatar | Optional. The avatar URL. The value is `null` if no custom avatar is set. |
| Discriminator | This is a legacy 4-digit tag that used to follow usernames. The current tag is `0` for most users. |
| Public flags | Indicates the number of badges visible on the user profile. |
| Flags | Indicates the number of badges visible on the user profile. This may include internal or private flags. |
| Banner | Optional. The user profile banner image URL. The value is `null` if no banner is set. |
| Accent color | Optional. The color integer displayed as a banner if no banner image is set. The value is `null` if no color is set. |
| Global name | The user display name. This is the name displayed in the UI, distinct from the unique username. |
| Clan | The user clan tag and badge. The value is `null` if not in a clan. |

---
