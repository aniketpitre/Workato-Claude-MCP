---
url: 'https://docs.workato.com/en/connectors/exa/create-record-action.md'
description: >-
  Create a monitor in Exa that runs a search on a schedule and delivers the
  results to a webhook URL.
---

# Exa - Create record action

The **Create record** action creates a record in Exa. Select **Monitor** to create a recurring search that runs on a schedule and delivers results to a webhook URL.

## Input

Input fields dynamically generate based on the **Object** you select. The following are a representative set of input fields. Refer to the Exa [Create a monitor](https://exa.ai/docs/reference/monitors/create-a-monitor) documentation for more information on available input fields.

### Monitor input

| Input field | Description |
| --- | --- |
| Object | Select the object to create. **Monitor** is the only option. |
| Query (Search) | Enter the natural-language query the monitor runs. |
| Number of results (Search) | Optional. Enter the number of results to return for each run. Valid values are `1`\-`100`. Defaults to `10` if left blank. |
| Period (Trigger) | Optional. Select how often the monitor runs. Options are **1 hour**, **6 hours**, **1 day**, or **7 days**. Defaults to **1 day** if left blank. |
| URL (Webhook) | Enter the HTTPS URL to receive monitor run results. The URL can't point to localhost or private IP ranges. |
| Metadata | Optional. Enter key-value pairs that Exa echoes back in webhook deliveries. Use them to route updates to other systems, such as Slack. Each key becomes an individual output datapill. Leave blank to send no metadata. |

### Output schema input

| Input field | Description |
| --- | --- |
| Output schema type | Optional. Select the format of the monitor run output. Select **Text** to return a prose summary, or **Object** to return structured JSON. Leave blank to send no output schema. |
| Output schema description | Optional. Enter a description of the output. Required when **Output schema type** is **Text**. Leave blank to send no description when **Output schema type** is **Object**. The **Output schema description** field is only available when you select an **Output schema type**. |
| Output schema properties | Optional. Define the properties of the structured output. Each property becomes an individual datapill. Leave blank to let Exa infer the schema. The **Output schema properties** field is only available when **Output schema type** is **Object**. |
| Output schema required fields | Optional. Enter the names of the properties the output requires. Leave blank to require none. The **Output schema required fields** field is only available when **Output schema type** is **Object**. |
| Allow additional properties | Optional. Select **Yes** to allow properties beyond the ones you define. Defaults to **No** if left blank. The **Allow additional properties** field is only available when **Output schema type** is **Object**. |

## Output

Output fields dynamically generate based on the **Object** you select. The following are a representative set of output fields. Refer to the Exa [Create a monitor](https://exa.ai/docs/reference/monitors/create-a-monitor) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The monitor's unique ID. |
| Name | The monitor's display name. |
| Status | The monitor's status. For example, `active`. |
| Search | The recurring search the monitor runs. |
| Trigger | How often the monitor runs. |
| Webhook | Where Exa delivers monitor runs. |
| Metadata | The key-value metadata you entered. Each key becomes an individual output datapill. |
| Next run at | The date and time of the monitor's next run. |
| Created at | The date and time the monitor was created. |
| Webhook secret | The secret for verifying webhook signatures. Exa returns this value only once, when you create the monitor. Save it for the **Webhook secret** field in the [New monitor run (real-time)](/en/connectors/exa/new-monitor-run-trigger) trigger. |

---
