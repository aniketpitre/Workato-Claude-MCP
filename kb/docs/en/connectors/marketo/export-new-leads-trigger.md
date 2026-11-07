---
url: 'https://docs.workato.com/en/connectors/marketo/export-new-leads-trigger.md'
description: >-
  The Export new leads trigger (bulk) in the Marketo connector runs on a
  schedule and returns new leads from your instance as a CSV stream.
---

# Marketo - Export new leads in Marketo trigger (bulk)

This trigger runs on a schedule you set and returns new leads from Marketo.

Search results are returned as a complete CSV stream. You can write the CSV stream to a file using a file connector, such as [Box](/en/connectors/box) or [SFTP](/en/connectors/sftp), or parse it for use as a data list in Workato using the **Parse CSV** action in the [CSV by Workato utility connector](/en/features/handling-csv-files#csv-by-workato).

Processing times can vary and be delayed due to the time required for the query to be completed in Marketo. Because of this, Workato doesn't support test jobs for recipes with this trigger.

You can also use this trigger in conjunction with the [Get object schema](/en/connectors/marketo/get-objects-action) action to fetch schema information of a Marketo object and replicate it to your data warehouse. Learn more about [bulk triggers and ELT/ETL processes](/en/features/etl-elt-guide#bulk-vs-batch).

## Input

| Field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour after the recipe starts. After the recipe runs or is tested, you can't change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| CSV format | Describe the formatting of the exported file. Column names default to Marketo API names. |
| Fields (CSV format) | Select the lead fields to export into the file. Workato permits a maximum combined field length of 7300 characters. |
| Column separator (CSV format) | Select the delimiter of the exported file. Available options include **Comma**, **Tab**, and **Semi-colon**. |

## Output

| Field | Description |
| --- | --- |
| Job ID | The unique identifier of the query job in Marketo. |
| CSV content | The datapill that contains the output of the trigger. |
| Object name | Name of the object being retrieved. |
| Created from | The datetime the record was created in Marketo. |
| Object schema | The schema of the object being retrieved. |
| Field name (object schema) | The name of the field in the object schema. |
| Field label (object schema) | The label of the field in the object schema. |
| Original type (object schema) | The original data type of the field. |
| Mapped type (object schema) | The data type that the field is mapped to in the target system, if different. |
| Length (object schema) | The length or size of the field, if applicable. |
| Precision (object schema) | The number of digits to the right of the decimal point for numeric fields. |
| Scale (object schema) | The number of digits to the left of the decimal point for numeric fields. |
| Read only (object schema) | Indicates whether the field is read-only and can't be edited. |

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/export-new-updated-leads-trigger.md
description: >-
  The Export new/updated leads trigger (bulk) in the Marketo connector runs on a
  schedule and returns new or updated leads as a CSV stream.
---

# Marketo - Export new/updated leads in Marketo trigger (bulk)

This trigger runs on a schedule you set and returns new or updated leads from Marketo.

Search results are returned as a complete CSV stream. You can write the CSV stream to a file using a file connector, such as [Box](/en/connectors/box) or [SFTP](/en/connectors/sftp), or parse it for use as a data list in Workato using the **Parse CSV** action in the [CSV by Workato utility connector](/en/features/handling-csv-files#csv-by-workato).

Processing times can vary and be delayed due to the time required for the query to be completed in Marketo. Because of this, Workato doesn't support test jobs for recipes with this trigger.

You can also use this trigger in conjunction with the [Get object schema](/en/connectors/marketo/get-objects-action) action to fetch schema information of a Marketo object and replicate it to your data warehouse. Learn more about [bulk triggers and ELT/ETL processes](/en/features/etl-elt-guide#bulk-vs-batch).

## Input

| Field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour after the recipe starts. After the recipe runs or is tested, you can't change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| CSV format | Describe the formatting of the exported file. Column names default to Marketo API names. |
| Fields (CSV format) | Select the lead fields to export into the file. Workato permits a maximum combined field length of 7300 characters. |
| Column separator (CSV format) | Select the delimiter of the exported file. Available options include **Comma**, **Tab**, and **Semi-colon**. |

## Output

| Field | Description |
| --- | --- |
| Job ID | The unique identifier of the query job in Marketo. |
| CSV content | The datapill that contains the output of the trigger. |
| Object name | Name of the object being retrieved. |
| Created or updated from | The datetime the record was created or updated. |
| Object schema | The schema of the object being retrieved. |
| Field name (object schema) | The name of the field in the object schema. |
| Field label (object schema) | The label of the field in the object schema. |
| Original type (object schema) | The original data type of the field. |
| Mapped type (object schema) | The data type that the field is mapped to in the target system, if different. |
| Length (object schema) | The length or size of the field, if applicable. |
| Precision (object schema) | The number of digits to the right of the decimal point for numeric fields. |
| Scale (object schema) | The number of digits to the left of the decimal point for numeric fields. |
| Read only (object schema) | Indicates whether the field is read-only and can't be edited. |

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/monitor-leads-added-to-list-trigger.md
description: >-
  The Monitor leads added to list trigger (batch) in the Marketo connector picks
  up leads added to a specified list each poll interval, in batches.
---

# Marketo - Monitor leads added to list trigger (batch)

This trigger picks up leads added to a specified list in your Marketo instance. It checks for new leads once every poll interval and Workato processes each lead as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up leads added to the list from this specified date and time. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| List | Select the list to monitor for new leads. Alternatively, switch to **Use list IDs** to enter a comma-separated list of IDs. The list ID is the first contiguous set of numbers after the `ST` in the URL. For example, if the list URL is `https://app-ab.marketo.com/#ST1001A1`, then `1001` is the list ID. |
| Enrich lead data | Select whether to enrich the lead data. If **Yes**, the trigger output performs additional requests to supplement each activity record with the associated lead data. If you plan to reduce the number of API requests, select **No** to exclude lead enrichment requests. |
| Batch size | Provide the number of records to be returned in each job. The minimum batch size is `1` and the maximum is `1000`. This field defaults to `300`. |

## Output

| Field | Description |
| --- | --- |
| First lead ID | The identifier of the first lead in the batch. |
| Last lead ID | The identifier of the last lead in the batch. |
| First batch | Whether this is the first batch of lead activities. |
| Last batch | Whether this is the last batch of lead activities. |
| Total number of records | The total number of records in the batch. |
| Activities | The activities associated with the leads. |
| Activity ID (activities) | The identifier of the activity. |
| Lead ID (activities) | The identifier of the lead associated with the activity. |
| Activity date (activities) | The datetime of the activity. |
| Activity type ID (activities) | The identifier of the activity type. |
| Primary attribute value ID (activities) | The identifier of the primary attribute value. |
| Activity primary attribute (activities) | The primary attribute of the activity. |
| Attributes (activities) | List of attributes associated with the activity. |
| Name (attributes) | The name of the attribute. |
| Value (attributes) | The value of the attribute. |
| Lead (activities) | An object representing the lead associated with the activity. |

Refer to the Marketo documentation for a [list of standard fields](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/assets/list-of-standard-fields) available through the API. This list includes common fields but may not cover all input fields specific to this action.

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/new-marketo-self-service-flow-step-trigger.md
description: >-
  The New Marketo Self Service Flow Step trigger picks up new self-service flow
  steps in real time, processing each as a separate job in Workato.
---

# Marketo - New Marketo Self Service Flow Step trigger (real-time)

This trigger picks up new Self-service Flow Steps in your Marketo instance. It listens for new flow steps in real-time and Workato processes each flow step as a separate job.

> **TRIGGER AND ACTION CONFIGURATION**
> 
> This trigger must be used with the [Return data to Marketo Self Service Flow Step action](/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action).
> 
> Ensure you start the recipe in Workato before completing the setup in Marketo. If you modify the trigger or action configuration, you must create a new flow step service in Marketo and deprecate the old one.
> 
> For detailed steps on configuring this trigger, action, and setting up a new service in Marketo, refer to our [Self-service Flow Steps](/en/connectors/marketo/self-service-flow-steps#steps-to-configure-self-service-flow-steps) documentation.

## Input

| Field | Description |
| --- | --- |
| API Key | Provide an API key to secure your Marketo Self Service Flow Step. |
| Flow step inputs | The input that users must provide when configuring your flow step. At least one must be defined. |
| Incoming lead attributes | Select the lead attributes you need from the flow. Lead ID is returned from the Marketo Flow. |
| Outgoing lead attributes | Determines what values this recipe sends back to Marketo to update the lead. |
| Step output | Describes what data to send back that is not tied to leads. |
| Program context | Select **Yes** if you plan for data related to the parent program of the smart campaign to invoke this flow step. |
| Campaign context | Select **Yes** if you plan for data related to the smart campaign to invoke this flow step. |
| Trigger context | Select **Yes** if you plan for data related to the event that triggered the campaign to invoke this flow step. |
| Program member context | Select **Yes** if you plan to collect data related to program membership, including status, success, and program-member custom field data. |
| Subscription context | Select **Yes** if you plan to collect identifiers for the Marketo subscription. These can be used to locate invoking instances for REST API calls. |

## Output

| Field | Description |
| --- | --- |
| Callback URL | The callback URL for the flow step. |
| Callback API key | The API key for the callback. |
| Callback token | The token for the callback. |
| Lead data | The lead data associated with the flow step. |
| Flow attributes | The flow attributes associated with the flow step. |
| Program context | The program context associated with the flow step. |
| Campaign context | The campaign context associated with the flow step. |
| Trigger context | The trigger context associated with the flow step. |
| Program member context | The program member context associated with the flow step. |
| Subscription context | The subscription context associated with the flow step. |

> **FURTHER READING**
> 
> - [Self-service Flow Steps](/en/connectors/marketo/self-service-flow-steps)
> - [Return data to Marketo Self Service Flow Step action](/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action)

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/new-lead-activity-batch-trigger.md
description: >-
  The New lead activity trigger (batch) in the Marketo connector detects new
  lead activities each poll interval, processed as separate jobs.
---

# Marketo - New lead activity trigger (batch)

This trigger detects new lead activities in your Marketo instance. It checks for new activities once every poll interval and Workato processes each activity as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up lead activities from this specified date and time. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Activity | The activity types to monitor. You can select up to ten activities. |
| List | The list to monitor for lead activities. If empty, lead activities from all lists are included. |
| Enrich lead data | If you select **Yes**, the trigger output performs additional requests to supplement each activity record with the associated lead data. Select **No** to exclude lead enrichment requests to reduce the number of API requests. |

## Output

| Field | Description |
| --- | --- |
| First lead ID | The unique identifier of the first lead in the list. |
| Last lead ID | The unique identifier of the last lead in the list. |
| Activities | A list containing details about each lead activity. |

---
