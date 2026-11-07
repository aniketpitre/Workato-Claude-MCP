---
url: 'https://docs.workato.com/en/connectors/calcom/search-records-action.md'
description: >-
  The Search records action searches for bookings or event types that match the
  filters you specify in Cal.com.
---

# Cal.com - Search records action

The **Search records** action searches for bookings or event types that match the filters you specify in Cal.com.

## Input

Input fields dynamically generate based on the object you select. The following input fields are common to all objects. Refer to the [Cal.com](https://cal.com/docs/api-reference/v2/introduction) documentation for a complete list of input fields.

| Input field | Description |
| --- | --- |
| Object | Select the object type you plan to search. Options include `Booking` and `Event type`. |
| Metadata output fields | Available when Object is **Booking**. Comma-separated metadata keys, for example `orderId` or `stripeCustomerId`, to expose as individual output datapills. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Cal.com](https://cal.com/docs/api-reference/v2/introduction) documentation for a complete list of output fields.

---
