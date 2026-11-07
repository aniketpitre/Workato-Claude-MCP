---
url: 'https://docs.workato.com/en/connectors/workday/update-object.md'
description: >-
  The Update business object action updates a Workday custom object such as
  Worker additional data or Service dates.
---

# Workday - Update business object action

The **Update business object** action updates a Workday custom object associated with a business process. This action supports custom objects like **Worker additional data**, **Service dates**, and other effective-dated data tied to workers or other entities.

The action dynamically adjusts input and output fields based on the selected **Business object**.

## Input

| Input field | Description |
| --- | --- |
| Business object | Select the Workday custom object to update, such as `Worker additional data`, `Service dates`, or `Work eligibility`. |
| Business process parameters | Configure optional workflow settings. If omitted or set to `false`, Workday runs the business process with standard approvals, reviews, and validations as if submitted through the UI. |
| Edit object record data | Provide effective-dated data to update for the selected object. Include all instances if the object supports multiples. Workday deletes any omitted instances. |
| Fields with attributes | Select additional fields with custom attributes to update. The list varies depending on the selected business object. |
| Fields with multiple values | Select fields that accept multiple values (arrays or lists). These are also specific to the selected business object. |

Additional input fields may appear based on the **Business object** selected.

## Output

Output fields depend on the selected **Business object**. For example, updating the `Worker additional data` object returns the following output:

| Output field | Description |
| --- | --- |
| Event reference (IID) | Internal ID of the Workday event. |
| Event reference (WID) | Workday ID of the event. |
| Event reference | Object representing the associated business process event. |
| Worker reference (WID) | Workday ID of the worker. |
| Worker reference (Contingent\_Worker\_ID) | Contingent worker ID, if applicable. |
| Worker reference (Employee\_ID) | Employee ID of the worker. |
| Worker reference | Object representing the worker. |
| Effective date | Date the update takes effect. |
| Additional data | List of custom fields updated in this request. |

---
