---
url: 'https://docs.workato.com/en/connectors/namely/new-event-trigger.md'
description: >-
  The New event trigger in the Namely connector runs when a new event, such as
  an announcement, birthday, or anniversary, is detected in Namely.
---

# Namely - New event trigger

The **New event** trigger runs when a new event is detected in Namely.

![New event trigger](/assets/new-event-trigger.DZSipwoK.png)_New event trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Enter the date at which you plan to begin monitoring events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Type | Enter the type of event you plan to monitor. For example, `announcement`, `birthday`, `recent arrival`, or `anniversary`. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the event. |
| HREF | The hyperlink reference associated with the event. |
| Type | The type of event. |
| Time | The timestamp of the event. |
| UFC offset | The offset for UFC events. |
| Content | The content of the event in plain text. |
| HTML content | The content of the event in HTML format. |
| Years at company | The number of years the person associated with the event has spent at the company. |
| Use comments | Indicates if comments are enabled for the event or not. Values are `true` or `false`. |
| Can comment | Indicates if commenting is allowed on the event or not. Values are `true` or `false`. |
| Can destroy | Indicates if the event can be deleted or not. Values are `true` or `false`. |
| Links profile | The link to the profile associated with the event. |
| Links comments | The links to comments associated with the event. |
| Links file | The link to the file associated with the event. |
| Links appreciations | The link to appreciations associated with the event. |
| Can like | Indicates if the event can be liked or not. Values are `true` or `false`. |
| Likes count | The count of likes for the event. |
| Liked by current profile | Indicates if the current profile has liked the event. |
| Meta response | The response meta-data for the event. |
| Meta use comments | Indicates if comments are used in the meta data. |
| Meta use updates | Indicates if updates are used in the meta data. |
| Meta use mentions | Indicates if mentions are used in the meta data. |
| Meta use appreciations | Indicates if appreciations are used in the meta data. |
| Meta use likes | Indicates if likes are used in the meta data. |
| Meta count | The count of items in the meta data. |
| Links events profile | The type of profile associated with events in links. |
| Links events comments | The type of comments associated with events in links. |
| Links events file | The type of file associated with events in links. |
| Links comments profile | The type of profile associated with comments in links. |
| Links profile image | The type of image associated with the profile in links. |
| Linked profiles id | The ID of the profile in linked data. |
| Linked profiles email | The email of the profile in linked data. |
| Linked profiles first name | The first name of the profile in linked data. |
| Linked profiles last name | The last name of the profile in linked data. |
| Linked profiles user status | The user status of the profile in linked data. |
| Linked profiles updated at | The last update timestamp of the profile in linked data. |
| Linked profiles created at | The creation timestamp of the profile in linked data. |
| Linked profiles preferred name | The preferred name of the profile in linked data. |
| Linked profiles image | The image of the profile in linked data. |
| Linked profiles full name | The full name of the profile in linked data. |
| Linked comments ID | The ID of the comment in linked data. |
| Linked comments content | The content of the comment in plain text. |
| Linked comments HTML content | The content of the comment in HTML format. |
| Linked comments created at | The creation timestamp of the comment in linked data. |
| Linked comments can destroy | Indicates if the comment can be deleted. |
| Linked comments links profile | The link to the profile associated with the comment. |
| Linked comments UTC offset | The UTC offset for the comment. |
| Linked comments likes count | The count of likes for the comment. |
| Linked comments liked by current profile | Indicates if the current profile has liked the comment. |
| Linked files ID | The ID of the file in linked data. |
| Linked files filename | The filename of the file in linked data. |
| Linked files MIME type | The MIME type of the file in linked data. |
| Linked files original | The original source of the file in linked data. |
| Linked files thumbs | The thumbnails of the file in various sizes in linked data. |

---
