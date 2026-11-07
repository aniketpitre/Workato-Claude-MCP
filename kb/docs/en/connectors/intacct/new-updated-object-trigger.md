---
url: 'https://docs.workato.com/en/connectors/intacct/new-updated-object-trigger.md'
description: >-
  The New/updated object trigger in the Sage Intacct connector fires when a
  selected object with unique key and timestamp fields is created or updated.
---

# Sage Intacct - New/updated object trigger

This trigger fetches new/updated object records in your Sage Intacct instance. Checks for new or updated object every 5 minutes. This trigger works only for objects with unique key and timestamp fields.

![New/updated object trigger](/assets/new-updated-object-trigger.Bz6OJJ9P.png)_New/updated object trigger_

## Input

| Input field | Description |
| --- | --- |
| Object | Select an object to fetch. The object is expected to have unique key and timestamp fields. |
| Unique key | Select the unique key of the object to deduplicate on. |
| Timestamp field | Select record modified timestamp field. Records will be filtered from the specified time based on this field. |
| When first started, this recipe should pick up events from | Optional. Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new/update events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the object.

---
