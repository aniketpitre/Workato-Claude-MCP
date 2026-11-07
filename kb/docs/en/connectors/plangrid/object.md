---
url: 'https://docs.workato.com/en/connectors/plangrid/object.md'
description: >-
  Overview of the PlanGrid connector triggers and actions in Workato, with the
  supported objects such as projects, tasks, RFIs, sheets, and documents.
---

# PlanGrid object triggers and actions

The PlanGrid connector in Workato provides triggers and actions that allows you to select the object you want to work with when configuring the step. The required input fields will then be dynamically generated based on the object you select.

The following triggers are supported:

- New object
- New or updated object

![PlanGrid triggers](/assets/plangrid-triggers.DKp-OODw.png)_Supported Plangrid triggers_

The following actions are supported:

- Create object
- Download object
- Get object
- Search object
- Update object
- Upload object

![PlanGrid actions](/assets/plangrid-actions.DsFkQ--p.png)_Supported Plangrid actions_

## Objects

| Object name | Available triggers | Available actions |
| --- | --- | --- |
| Document | [New](/en/connectors/plangrid/object-trigger#document) | [Get, Update, Upload](/en/connectors/plangrid/object-action#document) |
| Photo | [New](/en/connectors/plangrid/object-trigger#photo) | [Get, Update, Upload](/en/connectors/plangrid/object-action#photo) |
| RFI | [New, New/updated](/en/connectors/plangrid/object-trigger#rfi) | [Create, Get, Get status, Update](/en/connectors/plangrid/object-action#rfi) |
| Annotation | [New](/en/connectors/plangrid/object-trigger#annotation) |  |
| Field report | [New, New/updated](/en/connectors/plangrid/object-trigger#field-report) | [Get](/en/connectors/plangrid/object-action#field-report) |
| Project | [New, New/updated](/en/connectors/plangrid/object-trigger#project) | [Create, Get, Update](/en/connectors/plangrid/object-action#project) |
| Sheet | [New](/en/connectors/plangrid/object-trigger#sheet) | [Create version upload, Complete version upload, Create sheet packet, Get, Get sheet packet, Upload file to sheet version](/en/connectors/plangrid/object-action#sheet) |
| Snapshot | [New](/en/connectors/plangrid/object-trigger#snapshot) | [Get](/en/connectors/plangrid/object-action#snapshot) |
| Task | [New, New/updated](/en/connectors/plangrid/object-trigger#task) | [Create, Create task list, Get task, Get task list, Update task, Update task list](/en/connectors/plangrid/object-action#task) |

This is a non-exhaustive list of objects and there are still more enhancements to come. If you see an object that we don't currently support, you can use custom actions that allow you to send custom HTTP requests.

---
