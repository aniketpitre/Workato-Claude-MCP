---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/updated-employee-realtime-trigger.md
description: >-
  The New/Updated employee real-time trigger in the BambooHR connector fires
  through a webhook each time an employee is created or updated.
---

# BambooHR - New/Updated employee trigger (real-time)

This trigger picks up employees that are created or updated in your BambooHR instance. Each employee is processed as a separate job.

This trigger picks up events as soon as they occur. To set up this trigger, you have to configure webhooks in your BambooHR instance. Learn how to [configure a webhook in BambooHR](#how-to-setup-a-webhook-in-bamboohr).

> **Enable Webhooks on BambooHR**
> 
> Webhooks are not enabled by default. Contact BambooHR support to enable this feature.

## Input

After defining the **Event name**, a webhook endpoint URL will be generated. This will be needed to [configure a webhook in BambooHR](#how-to-setup-a-webhook-in-bamboohr).

![New/Updated employee trigger (real-time)](/assets/updated-employee-realtime-trigger.BynyodqV.png)_New/Updated employee trigger (real-time)_

| Input field | Description |
| --- | --- |
| Event name | Provide a descriptive name for this event. It will be appended to the webhook endpoint URL. |
| Output fields | Select the fields that will be posted from BambooHR. Ensure that the fields selected are identical. Find out more about BambooHR [employee fields](https://documentation.bamboohr.com/docs/list-of-field-names). |

## Output

The output of this action are fields defined by the BambooHR webhook. By default, Workato will retrieve the **Employee ID**.

| Output field. | Description |
| --- | --- |
| Employee ID | The employee ID assigned by BambooHR. |
| Output fields | Output fields as defined in the BambooHR webhook. |

For a full list of employee fields, see [field names](https://documentation.bamboohr.com/docs/list-of-field-names).

## How to set up a webhook in BambooHR

Complete the following steps to set up a webhook in BambooHR:

1. Set up the Workato trigger and select the event to generate an endpoint URL.
   
   ![Retrieve Workato webhook endpoint URL](/assets/updated-employee-realtime-webhook.CFxiacPO.png)_Retrieve Workato webhook endpoint URL_
   
2. Sign in to your BambooHR instance and go to **Account > Webhooks > + Add Hooks**.
   
   ![BambooHR Webhooks](/assets/go-to-webhooks.BJnZJmGO.png)_BambooHR Webhooks_
   
3. Select which **Webhook fields** to monitor. Updates to this field create a trigger event. Refer to the BambooHR [webhook fields](https://documentation.bamboohr.com/docs/webhooks) documentation for more information.
   
   ![Select fields to monitor](/assets/select-webhook-fields.CP6bHp7g.png)_Select fields to monitor_
   
4. Select which **Webhook fields** to post. These fields are sent to Workato as datapills. Refer to the BambooHR [webhook fields](https://documentation.bamboohr.com/docs/list-of-field-names) documentation for more information.
   
   Ensure that the fields to post are identical to the fields configured in the [trigger input](#input).
   
   ![Select fields to post](/assets/select-return-fields.C2aJPXdF.png)_Select fields to post_
   
5. Select **JSON** as the format.
   
   ![Select JSON format](/assets/select-json-format.CUV92ymK.png)_Select JSON format_
   
6. Fill **Post to URL** with the endpoint provided by Workato.
   
   ![Provide webhook endpoint URL](data:image/png;base64,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)_Provide webhook endpoint URL_
   
7. Select **Save**.
   

Refer to the [BambooHR Webhooks](https://documentation.bamboohr.com/docs/webhooks) documentation for more information.
