---
url: 'https://docs.workato.com/en/connectors/intacct/new-updated-vendor-trigger.md'
description: >-
  The New/updated vendor trigger in the Sage Intacct connector fires when vendor
  records are created or updated in your instance.
---

# Sage Intacct - New/updated vendor trigger

This trigger fetches new/updated vendor records in your Sage Intacct instance. Note that inactive records are also included. Use **Trigger-IF** to filter for only active records.

![New/updated vendor trigger](/assets/new-updated-vendor-trigger.DmFZieAb.png)_New/updated vendor trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new/update events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the vendor object.

Find out more about [vendor object](https://developer.intacct.com/api/accounts-payable/vendors/).

---
