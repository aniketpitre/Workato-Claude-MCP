---
url: 'https://docs.workato.com/en/connectors/sap/new-idocs-batch-trigger.md'
description: >-
  The New IDocs batch trigger in the SAP connector listens to outbound IDocs in
  real time and processes multiple IDocs together in a single job.
---

# SAP - New IDocs batch trigger

The **New IDoc batch** trigger allows you to listen to outbound IDocs from SAP in real time. You can use this trigger to process multiple IDocs in a single job. Note that the **New IDoc batch** trigger is only compatible with OPA v23.0 and higher.

You can configure the SAP system partner profile to enable sending multiple IDocs in one transaction to fully leverage this feature. This allows you to process IDocs in batches and improve your IDocs transfer speed from system to system. IDoc batches are sent to Workato's webhooks gateway and have the following quotas:

| Description | Quota |
| --- | --- |
| Maximum webhook payload size (bytes) the New IDocs (batch) trigger | 10 MB |
| Maximum webhook rate limits for the New IDocs (batch) trigger | Steady rate: 20 events per second, equivalent to 72,000 events per hour; Burst allowance: 9,000 events that can be processed beyond the steady rate in a burst |
| Maximum byte quotas for the New IDocs (batch) trigger | Steady rate: 30 MB, Burst allowance: 30 MB |

Refer to the [webhooks rate and memory quotas](/en/troubleshooting/webhook-gateway-limits#webhook-gateway-limits) section for more information.

> **LARGE BATCH SIZES**
> 
> Configuring batch sizes larger than 1000 in SAP can result in errors.

![New IDocs batch trigger](/assets/idoc-batch-trigger.BGPtfJFj.png)_New IDocs batch trigger_

> **BEFORE YOU BEGIN**
> 
> You must [configure IDocs in your SAP system](/en/connectors/sap/configure-idoc-sap) before using this trigger.

## How batching works with IDocs

The New IDocs batch trigger process events based on the batch size you configure. For example:

**Example 1**

If you configure your batch size to `5` but ten IDocs are sent, two jobs are created with each job containing five IDocs.

**Example 2**

If you configure your batch size to `5` but two IDocs are sent, one job containing two IDocs is created.

## Input

| Input field | Description |
| --- | --- |
| IDoc type | Select an IDoc type from the drop-down menu or enter an IDoc type manually using the format `message_type.basic_type.extension`. For example: **ORDERS.ORDERS05** or **DEBMAS.DEBMAS03.ZDEBMAS**. If the IDoc type you plan to use is not available in the drop-down menu, consider configuring the IDoc in the [WE20 dialogue in the SAP system](/en/connectors/sap/connection-setup) before establishing a connection between Workato and SAP. |
| Batch size | Set a batch size between `1` to `1000` to process multiple IDocs per job. The batch size should align with the solution architecture and Workato webhook volume [quotas](/en/connectors/workato-webhooks#payload-size-limits). Consider using the 'New IDoc' trigger (without the batch tag) for single-document processing. |

![Trigger New IDoc](/assets/new-idoc-batch-trigger-setup.tDeWR7fi.png)_Configure batch size_

> **MESSAGE TYPE, BASIC TYPE AND CUSTOM EXTENSIONS**
> 
> We subscribe to one **message type**, **basic type**, and **custom extension** (if applicable) at a time. You must maintain the recipe logic to ensure that the workflow processes appropriately for different partners. For example, you can apply the condition on the RCVPRN datapill from the trigger or add the RCVPRT datapill in addition to the RCVPRN datapill.

## Output

The output for this trigger includes all segments and data fields for the IDocs received from the SAP system.

---
