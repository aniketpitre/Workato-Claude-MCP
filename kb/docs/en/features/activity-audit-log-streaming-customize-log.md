---
url: >-
  https://docs.workato.com/en/features/activity-audit-log-streaming-customize-log.md
description: >-
  Customize Workato audit log messages with JSON and placeholders before
  streaming them to destinations like Amazon S3, Splunk, or Datadog.
---

# Custom log messages

You can customize audit log messages before streaming them to external destinations like Amazon S3, Splunk, or Datadog.

For example, a customized log message can include the source application and environment metadata so that event logs are automatically processed in the destination application.

## Create a custom log message

Complete the following steps to create a custom log message:

1. Go to **Workspace admin > Settings > Log streaming**.
   
2. Locate the **Customize log message** field and enter a custom log message using JSON. You can also use [placeholders](#placeholders) to define the JSON structure. Workato replaces placeholders with actual log messages before streaming the event.
   
   ![Customize the log message](/assets/customize-log-message.CiaX9tKN.png)_Customize the log message_
   
3. Click **Save**.
   

## Supported placeholders

Workato supports the following placeholders:

| Placeholder | Description | Example |
| --- | --- | --- |
| `{{{log_message}}}` | Audit log event message as JSON | [See examples](/en/features/activity-audit-log-streaming-sample#json-file-content-sample-data) |
| `{{{log_message_str}}}` | Audit log event message as an escaped JSON string. **Required for logs sent to [Grafana Loki](#loki-log-example).** | [See example](/en/features/activity-audit-log-streaming-sample#example-log-message-str) |
| `{{{now}}}` | Timestamp | `2023-06-02T01:30:01.002-04:00` |
| `{{{now_utc}}}` | Timestamp in milliseconds | `1685683801002.2139` |
| `{{{now_utc_micro}}}` | Timestamp in microseconds | `1685683801002213` |
| `{{{now_utc_nano}}}` | Timestamp in nanoseconds | `1685683801002214000` |

> **JSON KEYS**
> 
> Currently, if you're using the placeholders in a JSON object, each key must match the name of the placeholder in the value. For example, if you use the placeholder `{{{log_message_str}}}`, you must give it the key `"log_message_str"`:
> 
> ```json
> {
>  "log_message_str": {{{log_message_str}}},
>  "now_utc_micro": {{{now_utc_micro}}}
> }
> ```

## Example custom log message

In the following example, we send the `source`, `environment`, and `service` fields to Datadog so that the message is automatically routed and stored in the correct bucket.

The `{{{log_message}}}` is the placeholder that Workato uses to substitute the actual audit log event message in JSON format.

```json
{
  "source": "workato",
  "environment": "staging",
  "hostname": "workato_cloud",
  "service": "emp_onboarding",
  "log_message": {{{log_message}}}
}
```

> **VALID JSON REQUIRED**
> 
> Make sure you define valid JSON. If the JSON is invalid or does not contain either the `{{{log_message}}}` or `{{{log_message_str}}}` placeholder, then Workato will send the default log message without any customization.

The following images show what the log message looks like in the Datadog log explorer.

![Custom audit log message fields](/assets/custom-audit-log-message.B6wnceTi.png)_Custom audit log message fields_

![Custom audit log message for recipe started event](/assets/custom-recipestarted-audit-log-message.Ds0dEigi.png)_Custom recipe started activity audit log message_

![Custom audit log message for a successfully completed job](/assets/custom-job-history-audit-log-message.BCU4w6Zk.png)_Custom job history audit log message_

## Example custom log message for Grafana Loki

The [Grafana Loki HTTP API](https://grafana.com/docs/loki/latest/api/#push-log-entries-to-loki) requires the log message to be sent as a string, so you must use the `{{{log_message_str}}}` placeholder instead of `{{{log_message}}}`.

The Loki API also expects a nanosecond timestamp formatted as a string. Use the `"{{{now_utc_nano}}}"` placeholder surrounded by double quotes to ensure the timestamp is converted to a string.

Format the JSON structure for the custom audit log message as follows:

```json
{
  "streams": [
    {
      "stream": {
        "label": "workato"
      },
      "values": [
          ["{{{now_utc_nano}}}", {{{log_message_str}}}]
      ]
    }
  ]
}
```

Example custom log message sent to Loki:

```json
{
 "streams": [
  {
   "stream": {
    "label": "workato"
   },
   "values": [
    [
     "1685687453790827508",
     "{\"event\":\"recipe_started\",\"details\":{\"run_once\":false,\"request\":{\"ip_address\":\"76.100.203.123\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36\"}},\"user\":{\"id\":1234567,\"external_id\":null,\"email\":\"example.user@workato.com\",\"name\":\"Example User\",\"environment_id\":1234567,\"environment_type\":\"dev\",\"account_id\":1234567,\"account_name\":\"Example User\"},\"team\":{\"id\":1234567,\"external_id\":null,\"email\":\"example.user@workato.com\",\"name\":\"Example User's team\",\"environment_id\":1234567,\"environment_type\":\"dev\",\"account_id\":1234567,\"account_name\":\"Example User\"},\"resource\":{\"type\":\"Flow\",\"id\":16983123,\"name\":\"Cat Fact Generator\",\"path\":\"Home/AI Testing\",\"folder_id\":9020123},\"timestamp\":\"2023-06-02 06:30:53 UTC\"}"
    ]
   ]
  }
 ]
}
```
