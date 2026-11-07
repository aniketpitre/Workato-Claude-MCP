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
