---
url: 'https://docs.workato.com/en/connectors/wordpress/get-like-details-action.md'
description: >-
  The Get details of likes for post batch action in the WordPress connector
  fetches like details for one or more posts that you specify.
---

# WordPress - Get details of likes for post batch action

The **Get details of likes for post** batch action allows you to fetch the WordPress like details of a post or posts that you specify.

![Get details of likes for post action](/assets/get-details-for-likes-post-action.BIXbCtfG.png)_Get details of likes for post batch action_

## Input

| Input field | Description |
| --- | --- |
| Post ID | Enter the ID of the post for which you plan to fetch like details. |

## Output

| Output field | Description |
| --- | --- |
| Found | The number of items fetched. |
| I like | Indicates if the current user likes the post or not. Values are `true` or `false`. |
| Can like | Indicates if the current user can like the post or not. Values are `true` or `false`. |
| Site ID | The ID of the site. For example: `6751xxxx`. |
| Post ID | The ID of the post. For example: `180`. |
| Likes ID | The ID for the like. For example: `230252325`. |
| Login | The login name of the user who liked the item. |
| Email | The email address of the user. |
| Name | The display name of the user. |
| First name | The first name of the user. |
| Last name | The last name of the user. |
| Nice name | The nicely formatted name of the user. |
| URL | The URL to the user's WordPress site. For example: `http://example1.wordpress.com` |
| Avatar URL | The URL to the user's avatar. For example: `https://2.gravatar.com/avatar/...` |
| Profile URL | The URL to the user's Gravatar profile. For example: `https://gravatar.com/example` |
| IP address | The IP address of the user. |
| Site ID (Likes) | The ID of the user's site. For example: `214052927`. |
| Site visible | Indicates if the user's site is visible or not. Values are `true` or `false`. |
| Default avatar | Indicates if the default avatar is used or not. Values are `true` or `false`. |

---
