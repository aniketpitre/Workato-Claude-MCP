---
url: 'https://docs.workato.com/en/connectors/intacct/new-project-trigger.md'
description: >-
  The New project trigger in the Sage Intacct connector fires when new project
  records are created in your instance.
---

# Sage Intacct - New project trigger

This trigger fetches new project records in your Sage Intacct instance. Note that inactive records are also included. Use **Trigger-IF** to filter for only active records.

![New project trigger](/assets/new-project-trigger.DbpSdhsu.png)_New project trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the new project object.

Find out more about [project object](https://developer.intacct.com/api/project-resource-mgmt/projects/).

---
