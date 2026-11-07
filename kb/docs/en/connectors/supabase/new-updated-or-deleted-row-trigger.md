---
url: >-
  https://docs.workato.com/en/connectors/supabase/new-updated-or-deleted-row-trigger.md
description: >-
  Invoke a recipe when Supabase sends a database webhook for an INSERT, UPDATE,
  or DELETE event on a table.
---

# Supabase - New, updated, or deleted row trigger

The **New, updated, or deleted row** trigger invokes when Supabase sends a database webhook for an INSERT, UPDATE, or DELETE event on a table.

> **SET UP THE WEBHOOK IN SUPABASE**
> 
> Copy the webhook URL from this trigger step after you save the recipe. Supabase doesn't have a subscription API for this webhook, so you must set it up in the Supabase dashboard or by SQL. Refer to the Supabase [Database Webhooks](https://supabase.com/docs/guides/database/webhooks) documentation for setup steps.

## Input

| Input field | Description |
| --- | --- |
| Table | Optional. Select the table to accept events for. Row datapills are taken from this table. |
| Event types | Optional. Select which database events to accept. Options are **INSERT**, **UPDATE**, or **DELETE**. Leave blank to accept all events. |

## Output

| Output field | Description |
| --- | --- |
| Type | The database event type. Options are `INSERT`, `UPDATE`, or `DELETE`. |
| Table | The table the event occurred on. |
| Schema | The database schema the table belongs to. |
| Record | The new row's values. The **Record** field is only available for **INSERT** and **UPDATE** events. Row fields dynamically generate based on the table you select. |
| Old record | The previous row's values for **UPDATE** events, or the deleted row's values for **DELETE** events. Row fields dynamically generate based on the table you select. |
