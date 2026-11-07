---
url: 'https://docs.workato.com/en/connectors/coupa/purchase-order-actions.md'
description: >-
  Use the Coupa connector purchase order actions to close or cancel a purchase
  order in Coupa by its internal Coupa ID.
---

# Coupa - Purchase order actions

Workato allows you to close or cancel purchase orders in Coupa. Use the object actions and select purchase orders when prompted for an object to create, update, or query purchase orders in Coupa. Refer to the [Coupa - Object actions](/en/connectors/coupa/object-actions) section for more information.

This action is typically used in response to recipes triggered when a purchase order is closed in NetSuite. Data integrity is maintained by closing both purchases orders in NetSuite and Coupa.

**Purchase order specific actions**

- **Close purchase order**
- **Cancel purchase order**

* * *

### Input fields for purchase order actions

The **Close purchase order** and **Cancel purchase order** actions require the purchase order's internal Coupa ID. This allows the actions to find that specific purchase order in Coupa and close or cancel it. You can use `search objects` to search purchase orders based on other attributes if you don't have the specific internal Coupa ID.

### Close purchase order

This action finds and closes the purchase order defined in the step input.

### Cancel purchase order

This action finds and cancels the purchase order defined in the step input.

### Output fields for purchase order actions

When canceled or closed, Workato also returns the purchase order object so you can use its datapills in subsequent steps.

---
