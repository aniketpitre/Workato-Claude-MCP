---
url: 'https://docs.workato.com/en/connectors/namely/post-comment-action.md'
description: >-
  The Post comment action in the Namely connector lets you add a new comment to
  a specified post using the post ID and comment text.
---

# Namely - Post comment action

The **Post comment** action allows you to post a new comment in Namely.

![Post comment action](/assets/post-comment-action.EFF6OOSr.png)_Post comment action_

## Input

| Input field | Description |
| --- | --- |
| Post ID | Enter the ID of the post you plan to comment on. You can find the post ID at the end of the post URL. To view the post URl: Click the date/time next to the post. For example, if the post URL is `https://acme.namely.com/events/2d65841f-2f3d-40d8-bdad-a44cac5575e4`, the post ID is `2d65841f-2f3d-40d8-bdad-a44cac5575e4`. |
| Comment | Enter the comment you plan to add to the post. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the message. |
| Content | The text content of the message. |
| HTML content | The HTML version of the message content. |
| Created at | The timestamp when the message was created. |
| Can destroy | Indicates whether the message can be deleted or not. Values are `true` or `false`. |
| Can edit | Indicates whether the message can be edited or not. Values are `true` or `false`. |
| UTC offset | The UTC offset for the message's timestamp. |
| Likes count | The number of likes the message has received. |
| Liked by current profile | Indicates whether the current profile has liked the message or not. Values are `true` or `false`. |
| Updated at | The timestamp when the message was last updated. |
| Profile ID | The ID of the profile associated with the message. |
| Profile company UUID | The universally unique ID (UUID) of the company associated with the profile. For example: `6d82888e-9c39-4fa8-ba84-c2145485a730`. |
| Profile email | The email address associated with the profile. |
| Profile first name | The first name of the person associated with the profile. |
| Profile last name | The last name of the person associated with the profile. |
| Profile user status | The status of the profile. For example: `active`. |
| Profile updated at | The timestamp when the profile's information was last updated. |
| Profile created at | The timestamp when the profile was created. |
| Profile preferred name | The preferred name of the person associated with the profile, if any. |
| Profile preferred last name | The preferred last name of the person associated with the profile, if any. |
| Profile image | Details about the profile's image, if any. |
| Profile full name | The full name of the person associated with the profile. |
| Profile job title ID | The ID of the profile's job title. |
| Profile job title | The job title associated with the profile. |
| Profile employee type | The type of employment. For example: `Full Time` or `Part Time`. |
| Profile access role | The access role associated with the profile within the system, if any. |
| Profile ethnicity | The ethnicity of the employee associated with the profile. |
| Profile team positions | The team positions associated with the profile. |
| Profile is Namely admin | Indicates whether the profile is an admin within Namely or not. Values are `true` or `false`. |
| Profile date format | The date format preferred by the employee associated with the profile. |

---
