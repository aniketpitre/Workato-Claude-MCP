---
url: 'https://docs.workato.com/en/connectors/wordpress/search-post-action.md'
description: >-
  The Search post action in the WordPress connector lets you search for a post
  by its title and return the matching post details.
---

# WordPress - Search post action

The **Search post** action allows you to search for a post in WordPress.

![Search post action](/assets/search-post-action.B3wugTeL.png)_Search post action_

## Input

| Input field | Description |
| --- | --- |
| Post title | The title of the post for which you plan to search. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID for the post. For example: `187`. |
| Site ID | The ID of the site. For example: `6751xxxx`. |
| Author ID | The ID of the author. For example: `64588464`. |
| Login | The login name of the author. For example: `integrator1`. |
| Email | The email address of the author. |
| Name | The display name of the author. For example: `example1`. |
| First name | The first name of the author. |
| Last name | The last name of the author. |
| Nice name | The nicely formatted name of the author. |
| URL | The URL to the author's WordPress site. For example: `http://example1.wordpress.com` |
| Avatar URL | The URL to the author's avatar. For example: `https://2.gravatar.com/avatar/...` |
| Profile URL | The URL to the author's Gravatar profile. For example: `https://gravatar.com/example1` |
| IP address | Indicates the IP address of the author. |
| Site visible | Indicates if the site is visible or not. Values are `true` or `false`. |
| Date | The date the post was created. For example: `2024-02-21T15:36:53.000000-06:00`. |
| Modified | The date the post was last modified. |
| Title | The title of the post. For example: `Monthly newsletter`. |
| URL | The URL to the post. For example: `https://example1.wordpress.com/?p=187` |
| Short URL | The short URL to the post. For example: `https://wp.me/p4xxxx-31` |
| Content | The HTML content of the post. |
| Excerpt | The excerpt of the post. |
| Slug | The slug of the post. |
| GUID | The globally unique identifier for the post. For example: `https://example1.wordpress.com/?p=187` |
| Status | The status of the post. For example: `draft`. |
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
| Is reblogged | Indicates if the post is reblogged or not. Values are `true` or `false`. |
| Is following | Indicates if the current profile is following the post or not. Values are `true` or `false`. |
| Global ID | The global ID of the post. For example: `xx91abdae40f9e8d2966332245409ba5`. |
| Featured image | The URL of the featured image, if any. |
| Post thumbnail | The thumbnail of the post, if any. |
| Format | The format of the post. For example: `standard`. |
| Geo | Indicates whether geographical information of the post is available or not. Values are `true` or `false`. |
| Menu order | The menu order of the post. |
| Publicize URLs | The URLs used for publicizing the post, if any. |
| Tags | The tags associated with the post, if any. |
| Categories | The categories associated with the post. |
| Attachments | The attachments to the post, if any. |
| Metadata | The metadata associated with the post. |
| Meta links self | The API link for the post. For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx/posts/187` |
| Meta links help | The help link for the post. For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx/posts/187/help` |
| Meta links site | For example: `https://public-api.wordpress.com/rest/xx/sites/6751xxxx` |

---
