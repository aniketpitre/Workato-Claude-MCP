---
url: 'https://docs.workato.com/en/connectors/wordpress/new-comment-trigger.md'
description: >-
  The New comment trigger in the WordPress connector runs when a new comment is
  detected, checking for new comments every five minutes by default.
---

# WordPress - New comment trigger

The **New comment** trigger runs when a new comment is detected in WordPress. The trigger checks for new comments every five minutes by default.

![New comment trigger](/assets/new-comment-trigger.iwL_aBah.png)_New comment trigger_

## Input

No additional input is required for this trigger.

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the comment. For example: `9`. |
| Post ID | The ID of the post to which the comment was added. For example: `57`. |
| Title | The title of the post associated with the comment. For example: `Trial post 2`. |
| Type | The type of the post associated with the comment. For example: `post`. |
| Link | The link to the associated post. |
| Author ID | The ID of the comment author. For example: `64588464`. |
| Login | The login name of the author. |
| Email | The email address of the author. |
| Name | The display name of the author. For example: `poster1`. |
| First name | The first name of the author. |
| Last name | The last name of the author. |
| Nice name | The nicely formatted name of the author. |
| URL | The URL to the author's WordPress site. |
| Avatar URL | The URL to the author's avatar. For example: `https://2.gravatar.com/avatar/...` |
| Profile URL | The URL to the author's Gravatar profile. For example: `https://gravatar.com/1d30c24261dfd9aee30c2acf520119a5.` |
| IP address | The IP address of the author. |
| Date | The date the comment was created. |
| URL | The URL to the comment. For example: `https://example1.wordpress.com/2024/09/27/trial-post-2/comment-page-1/#comment-9` |
| Short URL | The short URL to the comment. For example: `https://wp.me/p4zxxx-V%23comment-9`. |
| Content | The HTML content of the comment. |
| Raw content | The raw text content of the comment. |
| Status | The status of the comment. For example: `approved`. |
| Parent ID | The ID of the parent item. |
| Parent type | The type of the parent item. |
| Parent link | The link to the parent item. |
| Like count | The number of likes on the comment. |
| I like | Indicates whether the current profile likes the comment or not. Values are `true` or `false`. |
| Can moderate | Indicates whether the current profile can moderate the comment or not. Values are `true` or `false`. |
| I replied | Indicates whether the current profile has replied to the comment or not. Values are `true` or `false`. |
| Meta links self | The API link for the comment. For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx/comments/9` |
| Meta links help | The help link for the comment. For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx/comments/9/help` |
| Meta links site | The site link. For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx` |
| Meta links post | The link to the associated post. |
| Meta links replies | The link to the comment replies. For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx/comments/9/replies/` |
| Meta links likes | The link to the comment likes. For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx/comments/9/likes/` |

---
