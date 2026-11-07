---
url: 'https://docs.workato.com/en/connectors/exa/new-monitor-run-trigger.md'
description: >-
  Invoke a recipe when a monitor run completes in Exa, with results, content,
  and grounding from the run.
---

# Exa - New monitor run (real-time) trigger

The **New monitor run (real-time)** trigger invokes when a monitor run completes in Exa. Workato updates the monitor's webhook URL to point to the recipe when you start the recipe, and leaves the webhook URL unchanged when you stop the recipe.

> **CREATE THE MONITOR FIRST**
> 
> This trigger receives runs from an existing monitor. Create the monitor in Exa or with the **Create record** action before you select it in this trigger.

## Input

| Input field | Description |
| --- | --- |
| Content schema | Optional. Define the fields of the run's **Content** object when the monitor has an output schema. Add fields manually or generate a schema from a sample. Leave blank to return a single plain **Content** datapill. |
| Results schema | Optional. Define additional fields for each item in **Results**. Add fields manually or generate a schema from a sample result. Each field becomes an individual output datapill. Leave blank to return only the standard result fields. |
| Monitor | Select the monitor to receive runs from. The list shows up to 200 monitors. If the list doesn't include your monitor, switch to **Use custom value** and enter the monitor ID. |
| Webhook secret | Optional. Enter the monitor's webhook secret to verify the signature of each delivery. Exa returns the secret once, when you create the monitor. Exa must sign every delivery when you enter a secret. Leave blank to skip signature verification. |

## Output

Output fields dynamically generate based on the **Content schema** and **Results schema** you define. The following are a representative set of output fields. Refer to the Exa [Create a monitor](https://exa.ai/docs/reference/monitors/create-a-monitor) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Monitor ID | The monitor's unique ID. |
| Run ID | The run's unique ID. |
| Status | The run's status. For example, `completed`. |
| Completed at | The date and time the run completed. |
| Results | The results the run returned. |
| ID (Results) | The result's unique ID. |
| Title (Results) | The result's title. |
| URL (Results) | The result's URL. |
| Content | The run's content, as text or as an object when you define a **Content schema**. |
| Grounding | The citations that support the run's content. |

---
