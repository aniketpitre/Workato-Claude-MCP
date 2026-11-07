---
url: 'https://docs.workato.com/en/connectors/intacct/new-updated-expense-trigger.md'
description: >-
  The New/updated expense trigger in the Sage Intacct connector fires when
  expense records are created or updated in your instance.
---

# Sage Intacct - New/updated expense trigger

This trigger fetches new/updated expense records in your Sage Intacct instance.

![New/updated expense trigger](/assets/new-updated-expense-trigger.XsD3bbob.png)_New/updated expense trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new/updated events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the expense object.

Find out more about [expense object](https://developer.intacct.com/api/employee-expenses/).

---

---
url: >-
  https://docs.workato.com/en/connectors/intacct/new-updated-gl-account-trigger.md
description: >-
  The New/updated GL account trigger in the Sage Intacct connector fires when
  general ledger account records are created or updated in your instance.
---

# Sage Intacct - New/updated GL account trigger

This trigger fetches new/updated general ledger account records in your Sage Intacct instance. Note that inactive records are also included. Use **Trigger-IF** to filter for only active records.

![New/updated GL account trigger](/assets/new-updated-gl-account-trigger.BdDxoghE.png)_New/updated GL account trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new/updated events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the GL account object.

Find out more about [GL account object](https://developer.intacct.com/api/general-ledger/accounts/).

---
