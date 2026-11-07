---
url: >-
  https://docs.workato.com/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action.md
description: >-
  The Return data to Self Service Flow Step action in the Marketo connector lets
  you send lead updates back to Marketo from a flow step invocation.
---

# Marketo - Return data to Marketo Self Service Flow Step action

This action returns data to Marketo from a Self Service Flow Step invocation.

It must be used with the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). Together, these create a [Marketo Self Service Flow Step](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/flow-actions/flow-step-service). The recipe must be started in Workato before you can continue setting up the flow step in Marketo.

If any changes are made to the trigger or action configurations, a new flow step service must be created in Marketo, and the old service should be deprecated. To specify which values are returned to Marketo, you must first select the corresponding fields in the trigger configuration.

## Input

| Field | Description |
| --- | --- |
| Callback URL | The callback URL. This input field must be mapped from the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). |
| Callback API key | The callback API key. This input field must be mapped from the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). |
| Callback token | The callback token. This input field must be mapped from the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger). |
| Outgoing lead attributes | Lead data that Workato sends to Marketo to update each lead. |
| Outgoing lead attributes source list (outgoing lead attributes) | Input a list datapill from which outgoing lead attributes are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Lead attributes (outgoing lead attributes) | Expand to configure the lead attributes fields. |
| ID (lead attributes) | Provide the lead ID to specify which lead to update. |

## Output

There is no output for this action.

> **FURTHER READING**
> 
> - [Self-service Flow Steps](/en/connectors/marketo/self-service-flow-steps)
> - [New Marketo Self Service Flow Step trigger (real-time)](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger)
