---
url: 'https://docs.workato.com/en/connectors/xero/new-item.md'
description: >-
  The New/updated item trigger in the Xero connector fires when an item is
  created or updated in your connected Xero organization.
---

# Xero - New/updated item trigger

The **New/updated item** trigger activates when an item is created or updated.

![New/updated item trigger](/assets/new-item-trigger.C2SZffRE.png)_Xero - New/updated item trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |

## Output

| Output field | Description |
| --- | --- |
| Item ID | The unique identifier for the item. |
| Item code | The code associated with the item. |
| Inventory asset account code | The account code used for inventory assets. |
| Purchase description | Description of the item for purchasing purposes. |
| Item name | The name of the item. |
| Item description | A detailed description of the item. |
| Updated date | The date when the item was last updated. |
| Is tracked as inventory | Indicates if the item is tracked in inventory. |
| Quantity on hand | The quantity of the item available in inventory. |
| Total cost pool | The total cost associated with the item's inventory. |
| Is sold | Indicates if the item is sold. |
| Is purchased | Indicates if the item is purchased. |
| Sales details | Details about the item's sales aspects. |
| Purchase details | Details about the item's purchase aspects. |

---
