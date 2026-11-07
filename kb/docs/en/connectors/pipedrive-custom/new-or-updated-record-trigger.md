---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/new-or-updated-record-trigger.md
description: >-
  The New/updated record trigger monitors Pipedrive for newly created or updated
  records.
---

# Pipedrive - New/updated record trigger

The **New/updated record trigger** monitors Pipedrive for newly created or updated records.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to monitor for new or updated instances. |
| Trigger poll interval | Select how frequently to check for new objects. |
| When first started, this recipe should pick up events from | Select a start date and time to retrieve trigger events. This enables your recipe to capture past events. This value cannot be changed after the recipe has been run or tested. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The **New/updated record** trigger's output fields vary based on your selected **Object** type. The following output table uses a **User** object as an example:

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the object. |
| Name | The name of the object. |
| Default currency | The default currency for the object. |
| Locale | The language locale for the object. |
| Language | The language for the object. |
| Email | The object's attached email. |
| Phone | The object's attached phone number. |
| Activated | Indicates whether the object is active or not. |
| Last login | A timestamp indicating the user's last login time. |
| Created | A timestamp indicating the creation date of the object. |
| Modified | A timestamp indicating the time the object was last modified. |
| Has created company | Indicates whether this user has created a company. |
| Access | The access roles set for this user. |
| Active flag | Indicates whether the user is active in real-time on the platform. |
| Timezone | The timezone where the user is located. |
| Timezone offset | Difference between the GMT and the user’s timezone. |
| Role ID | A unique identifier for the primary role of this user. |
| Is admin | Indicates whether the user is an admin. |
| Icon URL | The URL of the icon set for this user. |
| Is you | Indicates whether the API requester and the user who caused the trigger event are the same. |
| Is deleted | Indicates whether this object was deleted. |
