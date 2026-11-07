---
url: >-
  https://docs.workato.com/en/connectors/assemblyai/completed-transcript-trigger.md
description: >-
  Fire a recipe when a transcript job finishes using a static webhook you set on
  the submit action.
---

# AssemblyAI - Completed transcript trigger

The **Completed transcript** trigger invokes when a transcript's status reaches **completed** in AssemblyAI.

> **STATIC WEBHOOK, NO SUBSCRIPTION API**
> 
> This trigger uses a static webhook URL. Copy the webhook URL from the trigger step after you save the recipe. Set it as the **Webhook URL** field on the [Create record](/en/connectors/assemblyai/create-record-action) or [Transcribe and wait](/en/connectors/assemblyai/transcribe-and-wait-action) action when you submit a transcript. AssemblyAI doesn't have a subscription API for this webhook.

> **NO TRANSCRIPT TEXT IN THE PAYLOAD**
> 
> AssemblyAI's webhook payload includes only the transcript ID and status, not the transcript text. Chain a [Get record](/en/connectors/assemblyai/get-record-action) action step using the trigger's **Transcript ID** output to fetch the full transcript.

## Input

| Input field | Description |
| --- | --- |
| Webhook auth header name | Optional. Enter the same header name you set as **Webhook auth header name** when you submitted the transcript, for example `X-My-Webhook-Secret`. Leave the **Webhook auth header name** field blank only if you didn't configure webhook authentication on the submit action. |
| Webhook auth header value | Optional. Enter the same header value you set as **Webhook auth header value** when you submitted the transcript. Leave the **Webhook auth header value** field blank only if you didn't configure webhook authentication on the submit action. |

## Output

| Output field | Description |
| --- | --- |
| Transcript ID | The completed transcript's unique identifier. |
| Status | The transcript's status, for example `completed`. |
