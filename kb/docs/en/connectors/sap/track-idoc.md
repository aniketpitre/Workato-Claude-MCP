---
url: 'https://docs.workato.com/en/connectors/sap/track-idoc.md'
description: >-
  Track IDoc status in SAP using the list of transmission status codes to
  monitor IDocs sent through the Workato on-prem agent and webhooks.
---

# Track IDoc status in SAP

You can track the IDoc status in your SAP system. Use the following list of statuses to monitor IDoc transmission.

| Status | Description |
| --- | --- |
| `3` | IDOC was passed to Port OK. |
| `39` | The Workato OPA sent the IDOC to Workato using webhooks. If you have multiple recipes listening for the same IDoc, the OPA sent a webhook for each recipe and received `200 OK success` responses. |
| `40` | The Workato OPA failed to send IDoc to Workato using webhooks. If you have multiple recipes listening for the same IDoc, the OPA did not receive a `200 OK success` response for one or more recipe. |

> **FAILED WEBHOOKS**
> 
> If one or more webhooks fail, you must resend the IDoc. When you resend the IDoc, recipes that previously received the IDoc do not process it again due to Workato's deduplication logic.

---
