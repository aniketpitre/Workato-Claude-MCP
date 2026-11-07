---
url: 'https://docs.workato.com/en/connectors/workday/new_updated_object.md'
description: >-
  The New/updated business object trigger in the Workday connector fires when a
  supported business object is created or updated in a Workday instance.
---

# Workday - New/updated business object trigger

![New/updated business object trigger](/assets/new-updated-object.Dqy5nyua.png)_New/updated business object trigger_

This trigger uses Workday Web Services (WWS) to check for new/updated business object from a connected Workday instance.

Supported business objects are:

- Workers
- Organizations
- Job Profiles
- Payees
- Positions
- Job Requisitions
- Evergreen Requisitions
- Customer Contracts

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Workday objects that are created after this date and time will be processed in the trigger. If left blank, the trigger will pick up entries created 1 hour before the first time this recipe is started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Business object | The object type. |
| **\[Optional\]** Request criteria | The request criteria element lets you apply additional criteria to identify the specific instance(s) desired. |
| **\[Optional\]** Trigger poll interval | Select how frequently to check for new events. |

Additional/advanced input fields may be present for specific business objects.

## Output

We will output the complete set of fields and attributes for the selected operation as the output datatree, except in cases where additional/advanced input fields dictate we return a subset of the available object data.

## Limitations

Based on the [Workday documentation](https://doc.workday.com/r/3DMnG~27o049IYFWETFtTQ/sGhnezv85Vfp9LabNN~EWw):

- The maximum number of instances in a web service response is 1 million.
- Responses with attachments/images, the maximum size of each attachment/image is 30MB.
- Rich text string responses have a size limit of 1,048,576 characters or 1MB.

---
