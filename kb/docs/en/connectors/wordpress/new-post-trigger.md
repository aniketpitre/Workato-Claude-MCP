---
url: 'https://docs.workato.com/en/connectors/wordpress/new-post-trigger.md'
description: >-
  The New post created trigger in the WordPress connector runs when a new post
  is detected, checking for new posts every five minutes by default.
---

# WordPress - New post created trigger

The **New post created** trigger runs when a new post is detected in WordPress. The trigger checks for new posts every five minutes by default.

![New post created trigger](/assets/new-post-trigger.D5NA8aKB.png)_New post created trigger_

## Input

No additional input is required for this trigger.

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the post. For example: `182`. |
| Site ID | The ID of the site. For example: `67514089`. |
| Author ID | The ID of the author. For example: `64588464`. |
| Login | The login name of the author. For example: `workato1`. |
| Email | The author's email address. |
| Name | The display name of the author. |
| First name | The first name of the author. |
| Last name | The last name of the author. |
| Nice name | The nicely formatted name of the author. |
| URL | The URL to the author's WordPress site. For example: `http://example.wordpress.com`. |
| Avatar URL | The URL to the author's avatar. For example: `https://2.gravatar.com/avatar/...` |
| Profile URL | The URL to the author's Gravatar profile. For example: `https://gravatar.com/example1`. |
| IP address | The IP address of the author. |
| Site visible | Indicates if the site is visible or not. Values are `true` or `false`. |
| Date | The date the post was created. For example: `2024-02-21T15:21:02.000000-06:00`. |
| Modified | The date the post was last modified. For example: `2024-02-21T15:21:02.000000-06:00`. |
| Title | The title of the post. For example: `Monthly news`. |
| URL | The URL to the post. For example: `https://example1.wordpress.com/2024/02/21/docs-test/`. |
| Short URL | The short URL to the post. For example: `https://wp.me/p4zxxx-2W`. |
| Content | The content of the post. |
| Excerpt | The excerpt of the post. |
| Slug | The slug of the post. For example: `monthly-news`. |
| GUID | The globally unique identifier for the item. For example: `https://example1.wordpress.com/?p=182`. |
| Status | The status of the post. For example: `publish` or `draft`. |
| Sticky | Indicates if the post is sticky or not. Values are `true` or `false`. |
| Password | The password for the post, if any. |
| Parent | Indicates the parent of the post. |
| Type | The type of the post. |
| Comments open | Indicates if comments are open or not. Values are `true` or `false`. |
| Pings open | Indicates if pings are open or not. Values are `true` or `false`. |
| Likes enabled | Indicates if likes are enabled or not. Values are `true` or `false`. |
| Sharing enabled | Indicates if sharing is enabled or not. Values are `true` or `false`. |
| Comment count | The number of comments on the post. |
| Like count | The number of likes on the post. |
| I like | Indicates if the current profile likes the post or not. Values are `true` or `false`. |
| Is reblogged | Indicates if the item is reblogged or not. Values are `true` or `false`. |
| Is following | Indicates if the current profile is following or not. Values are `true` or `false`. |
| Global ID | The global ID of the post. For example: `318af433c3f54f6bdce981a6bdf79xxx`. |
| Featured image | The URL of the featured image, if any. |
| Post thumbnail | The thumbnail of the post, if any. |
| Format | The format of the post. For example: `standard`. |
| Geo | Indicates the geographical information of the post. |
| Menu order | The menu order of the post. |
| Publicize URLs | The URLs used for publicizing the post, if any. |
| Tags | The tags associated with the post, if any. |
| Categories | The categories associated with the post. |
| Attachments | The attachments to the post, if any. |
| Metadata | The metadata associated with the post. |
| Links | The links associated with the post. |
| Current user can | The capabilities of the current user regarding the post. |
| Capabilities | The capabilities associated with the post. |

---
