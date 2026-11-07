---
url: 'https://docs.workato.com/en/connectors/eventbrite/new-contact-trigger.md'
description: >-
  The New contact created trigger in the Eventbrite connector checks for new
  contacts added to a specific contact list in Eventbrite.
---

# Eventbrite - New contact created trigger

The **New contact created** trigger in Eventbrite checks for new contacts added to a specific contact list in Eventbrite.

![New contact trigger](/assets/new-contact-eventbrite.D7j8BUXH.png)_Eventbrite - New contact trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Set the frequency at which Workato checks for new contacts. This field defaults to every 30 minutes if not set. |
| Organization | Select the organization within Eventbrite to monitor for new contacts. |
| When first started, this recipe should pick up events from | Choose a start date for the trigger to begin fetching contacts. After you test or run the recipe, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Contact list | Choose the contact list for Workato to monitor for new contacts. |

## Output

| Output field | Description |
| --- | --- |
| Date created | The date and time when the contact was added to Eventbrite. |
| First name | The first name of the contact. |
| Last name | The last name of the contact. |
| Email | The email address of the contact. |

---
