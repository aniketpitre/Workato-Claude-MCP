---
url: 'https://docs.workato.com/en/connectors/exa/list-monitor-runs-action.md'
description: >-
  List the runs for a monitor in Exa, newest first, with cursor-based
  pagination.
---

# Exa - List monitor runs action

The **List monitor runs** action lists the runs for a monitor in Exa. Exa returns runs in reverse chronological order, so the newest run comes first.

## Input

The following are a representative set of input fields. Refer to the Exa [List runs](https://exa.ai/docs/reference/monitors/runs/list-runs) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Monitor | Select the monitor to list runs for. The list shows up to 200 monitors. Switch to **Use custom value** and enter the monitor ID if the list doesn't include your monitor. |
| Results schema | Optional. Define additional fields for each item in **Results**. Add fields manually or generate a schema from a sample result. Each field becomes an individual output datapill. Leave blank to return only the standard result fields. |
| Content schema | Optional. Define the fields of each run's **Content** object when the monitor has an output schema. Add fields manually or generate a schema from a sample. Leave blank to return a single plain **Content** datapill. |
| Limit | Optional. Enter the number of runs to return. Valid values are `1`\-`100`. Defaults to `50` if left blank. |
| Cursor | Optional. Enter the **Next cursor** value from a previous response to get the next page of runs. Leave blank to start from the newest run. |

## Output

The following are a representative set of output fields. Refer to the Exa [List runs](https://exa.ai/docs/reference/monitors/runs/list-runs) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Data | The monitor's runs. |
| ID (Data) | The run's unique ID. |
| Status (Data) | The run's status. For example, `completed` or `failed`. |
| Fail reason (Data) | Why the run failed. Exa returns this value only when the run failed. |
| Started at (Data) | The date and time the run started. |
| Completed at (Data) | The date and time the run completed. |
| Duration ms (Data) | The run's duration in milliseconds. |
| Output (Data) | The run's results and content. Exa returns this value only when the run produced output. |
| Has more | Whether Exa has more runs to return. |
| Next cursor | The value to enter in **Cursor** to get the next page of runs. |

---
