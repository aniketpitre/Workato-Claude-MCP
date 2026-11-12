---
url: 'https://docs.workato.com/en/connectors/workato-webhooks/webhooks-faqs.md'
description: >-
  Answers to frequent questions about Webhooks in Workato, including common
  errors, rate limits, generating addresses, and trigger error logs.
---

# Webhooks FAQs

Get answers to frequently asked questions (FAQs) about Webhooks.

## What are common errors encountered with the Webhooks connector?

View answer

Common errors with the Webhooks connector include:

- [Error generating schema for response](/en/connectors/workato-webhooks/common-errors#error-generating-schema-for-response)
  
  - This error appears when there's a mismatch between the Content-Type specified in the webhook header and the actual payload data type. For example, the header indicates JSON data, but the payload is in XML format. This mismatch typically occurs with legacy or custom applications that don't follow standard HTTP practices, resulting in a Content-Type that doesn't match the actual payload format. To correct this error, check with the application owner to ensure the webhook API sends data in the correct format. If adjusting the source isn’t possible, you can manually configure the payload schema in Workato by selecting **Skip guided setup** and then defining the schema yourself.

## What should I do if the application sending the webhook does not follow standard HTTP practices?

View answer

If the sending application's Content-Type doesn’t match the payload format, and it cannot be corrected at the source, you should manually [configure the payload schema](/en/connectors/workato-webhooks/config#input) in Workato to match the actual data format being received.

## What are rate limits for webhooks?

View answer

Our webhook gateway has the following [rate limits](/en/troubleshooting/webhook-gateway-limits#rate-limits):

- Steady rate: 20 events per second, equivalent to 72,000 events per hour
- Burst allowance: 9,000 events that can be processed beyond the steady rate in a burst

### Leaky bucket rate limiting

The webhook gateway uses a **leaky bucket approach** with the following process:

- If you receive **more than 20 events** in a second, the excess events consume your burst allowance.
  
- If you receive **fewer than 20 events** in a second, the remaining capacity refills your burst allowance, but only if the burst allowance is less than 9,000 events.
  

If you exceed both the steady rate (20 events per second) and the burst allowance (9,000 events), the webhook gateway returns a `429 Too Many Requests` response for additional events until the rate falls within the quota.

## How many webhook recipes can listen to the same URL?

View answer

The maximum number of webhook recipes that can listen to the same URL is 100.

## How do I generate a unique webhook address?

View answer

Complete the following steps to [generate a unique webhook address](/en/connectors/workato-webhooks/wizard):

1. Select the **Webhooks** connector from the list of Apps.
   
2. Click **Start guided setup** to open the setup wizard.
   
3. Enter a unique event name for the webhook.
   
4. Complete the remaining steps in the setup wizard.
   

## What causes webhook trigger errors?

View answer

Webhook trigger errors occur when there is an issue with accepting or processing a webhook event. These errors can occur for various reasons, such as an invalid request, incorrect URL, or server issues. Refer to [Webhook trigger errors](/en/connectors/workato-webhooks/common-errors#webhook-trigger-errors) for more information.

## Where can I view error logs for the webhook trigger?

View answer

You can view error logs for the webhook trigger by using the [Workato Logging Service](/en/features/logging-service). Filter trigger errors on the [logging service page](https://app.workato.com/logs) to identify and troubleshoot specific issues.

## Why didn't I get a notification about invalid data in my trigger?

View answer

A job isn't generated for a recipe when a trigger error occurs. This means that there is no job ID, and no entry is created in the job history table. These errors are only visible on the logging service page. Data-related errors don't generate a prompt or notification because no job was generated.

Learn more about [Workato data types](/en/data-tables/user-interface/column-types).

---
