---
url: 'https://docs.workato.com/en/connectors/exa/delete-record-action.md'
description: Permanently delete a monitor in Exa and return the deleted monitor's details.
---

# Exa - Delete record action

The **Delete record** action permanently deletes a record in Exa. Select **Monitor** to delete a monitor and return its details.

## Input

Input fields dynamically generate based on the **Object** you select. The following are a representative set of input fields. Refer to the Exa [Delete a monitor](https://exa.ai/docs/reference/monitors/delete-a-monitor) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the object to delete. **Monitor** is the only option. |
| Output schema properties | Optional. Define the properties of the monitor's structured output. Add properties manually or generate a schema from a sample. Each property becomes an individual datapill. Leave blank to return no individual property datapills. |
| Metadata keys | Optional. Enter the metadata keys set on the monitor. Each key becomes an individual output datapill. Leave blank to return **Metadata** as a single datapill. |
| Monitor | Select the monitor to delete. The list shows up to 200 monitors. Switch to **Use custom value** and enter the monitor ID if the list doesn't include your monitor. |

## Output

Output fields dynamically generate based on the **Object** you select. The following are a representative set of output fields. Refer to the Exa [Delete a monitor](https://exa.ai/docs/reference/monitors/delete-a-monitor) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The deleted monitor's unique ID. |
| Name | The monitor's display name. |
| Status | The monitor's status. For example, `active`. |
| Search | The recurring search the monitor ran. |
| Trigger | How often the monitor ran. |
| Webhook | Where Exa delivered monitor runs. |
| Metadata | The key-value metadata set on the monitor. Each key you enter in **Metadata keys** becomes an individual output datapill. |
| Next run at | The date and time of the monitor's next scheduled run. |
| Created at | The date and time the monitor was created. |
| Updated at | The date and time the monitor was last updated. |

---
