---
url: 'https://docs.workato.com/en/connectors/xero/new-bill.md'
description: >-
  The New/updated bill trigger in the Xero connector fires when a bill is
  created or updated in your connected Xero organization.
---

# Xero - New/updated bill trigger

The **New/updated bill** trigger activates when a bill is created or updated.

![New/updated event trigger](/assets/new-bill-trigger.5GWqgjiT.png)_Xero - New/updated bill trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. Defaults to five minutes if blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |
| Status | Specify the bill status that triggers the recipe. |
| Sent to contact | Filter bills sent to a particular contact, applicable to approved bills only. |

## Output

| Output field | Description |
| --- | --- |
| Type | The type of the bill. |
| Invoice ID | The unique identifier for the bill. |
| Reference | A reference note or number associated with the bill. |
| Payments | Payment details associated with the bill. |
| Credit notes | Credit note details applied to the bill. |
| Amount due | The total amount due on the bill. |
| Amount paid | The total amount paid against the bill. |
| Amount credited | The total amount credited to the bill. |
| URL | The URL link to the bill in Xero. |
| Currency code | The currency code used for the bill. |
| Currency rate | The exchange rate applied to the bill currency. |
| Has errors | Indicates if there are errors associated with the bill. |
| Is discounted | Indicates if any discounts have been applied to the bill. |
| Has attachments | Indicates if there are attachments included with the bill. |
| Contact | Contact details associated with the bill. |
| Date | The date the bill was issued. |
| Due date | The date by which the bill must be paid. |
| Status | The current status of the bill. |
| Branding theme ID | The identifier for the branding theme applied to the bill. |
| Line amount types | The type of line amounts on the bill. |
| Line items | Itemized details of services or products billed. |
| Sub total | The bill sub total before tax. |
| Total tax | The total tax amount for the bill. |
| Total | The total amount of the bill, including tax. |
| Updated date | The last date when the bill details were updated. |
| Paid date | The date when the bill was fully paid. |
| Planned payment date | The date planned for the bill payment. |

---
