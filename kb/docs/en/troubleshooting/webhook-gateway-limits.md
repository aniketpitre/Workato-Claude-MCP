---
url: 'https://docs.workato.com/en/troubleshooting/webhook-gateway-limits.md'
description: >-
  Learn how the Workato webhook gateway enforces rate limits and byte quotas per
  environment and how leaky bucket rate limiting handles bursts.
---

# Webhook gateway quotas

When you use a real-time trigger, a webhooks connector, or build a webhook trigger on the connector SDK, events are sent to the webhook gateway before becoming jobs. Workato's webhook gateway enforces two quotas at the **Workspace level**:

- Rate limits
  
- The number of events you can send in a given time interval.
  
- Byte quotas
  
- The total memory size of webhook events allowed in a specific time interval.
  

## Rate limits

The webhook gateway uses rate limits to manage event processing efficiently. The following quotas apply per environment, such as Dev, Test, or Prod:

- Steady rate: 20 events per second, equivalent to 72,000 events per hour
- Burst allowance: 9,000 events that can be processed beyond the steady rate in a burst

### Leaky bucket rate limiting

The webhook gateway uses a **leaky bucket approach** with the following process:

- If you receive **more than 20 events** in a second, the excess events consume your burst allowance.
  
- If you receive **fewer than 20 events** in a second, the remaining capacity refills your burst allowance, but only if the burst allowance is less than 9,000 events.
  

> **BURST ALLOWANCE REFILL LIMIT**
> 
> The burst allowance does not refill if it has already reached the maximum quota of 9,000 events.

If you exceed both the steady rate (20 events per second) and the burst allowance (9,000 events), the webhook gateway returns a `429 Too Many Requests` response for additional events until the rate falls within the quota.

> **HANDLING 429 RESPONSES**
> 
> The webhook gateway sends `429` responses to maintain stability for all customers. The best practice for handling `429` responses is to retry webhooks until they are accepted.
> 
> [Learn more about handling 429 responses.](#handle-rate-limit-errors-from-the-webhook-gateway)

### Example scenarios

The following scenarios demonstrate how the webhook gateway processes different amounts of events:

#### Scenario 1: 25 events in one second

When you receive 25 events in one second, the webhook gateway processes 20 events within the steady rate. The remaining 5 events consume part of your burst allowance.

#### Scenario 2: 10 events in one second

If you receive 10 events in one second, the gateway processes all 10 events. The unused capacity (10 events) refills your burst allowance, provided it hasn’t reached the maximum quota.

#### Scenario 3: 9,050 events in one second

In this scenario, you receive 9,050 events in one second. The gateway processes 20 events at the steady rate, and the next 9,000 events deplete your entire burst allowance. The remaining 30 events result in a `429 Too Many Requests` response, as both the steady rate and burst allowance are exceeded.

## Byte quotas

Our webhook gateway has the following byte quotas, which represents the total memory in all your webhooks:

- 30 MB per minute
- Burst allowance: 30 MB

You can imagine the byte quotas per minute and burst in the same way as the rate limits.

> **HANDLING 429 RESPONSES**
> 
> 429 requests are meant to preserve the stability of our webhook gateway for all customers. Industry best practices for 429s are to retry webhooks until they are eventually accepted. In high volume scenarios, webhook gateway quotas may be adjusted on a per-customer basis and subject to commercial terms and approval.
> 
> [Learn more about handling 429 responses.](#handle-rate-limit-errors-from-the-webhook-gateway)

* * *

## Rate limit revisions

We understand that each business has unique event processing needs. Our goal is to support your objectives by offering flexible rate limits tailored to your specific requirements.

For existing customers, we recognize that some may have higher rate limits based on earlier versions of our documentation, including a steady rate of 20 events per second and a burst allowance of 18,000 events. We remain committed to honoring these higher quotas. Any changes to your rate limits are communicated in advance.

If the standard rate limits do not meet your requirements, we encourage you to contact our support team to discuss potential adjustments. We work with you to ensure that your usage aligns with your business objectives while maintaining platform stability.

## Additional information for embedded partners

For Embedded Partners using our shared connectors feature to distribute connectors to their customers, static webhook triggers in your customer workspaces have their own separate webhook rate limits. For example, webhook events to Customer A's workspace will not be counted to Customer B's workspace webhook rate limits.

* * *

## Handle rate limit errors from the webhook gateway

When you exceed your rate limits, Workato's webhook gateway responds with 429 errors. In addition to this, Workato's webhook gateway responds to every event with 5 headers that help you understand when you can successfully send your next event.

- `Retry-After`: The number of seconds to wait before retrying the request.
- `X-Rate-Limit-Remaining`: The number of events you can send before the gateway rejects additional requests. A value of `0` indicates that the quota has been reached. If the gateway accepts a request while this value is `0`, that request is the final one accepted for that time window (second).
- `X-Rate-Limit-Reset`: The number of seconds until the burst rate limit resets, assuming a steady rate of `20` requests per seconds (rps). If requests stay below this rate, the difference between the allowed and actual rates refills the burst capacity. For example, if the system allows 20 rps and you send 12 rps, it refills 8 rps of burst capacity.
- `X-Byte-Limit-Remaining`: How much cumulative data across all webhooks that can be sent before 429s are returned
- `X-Byte-Limit-Reset` - How many seconds before your Byte burst allowance is refilled

Your API can use these headers to understand how and when to throttle webhook events.

### Webhook rate limit examples

These examples use the following quotas:

- 20 rps steady rate
- 18,000 event burst capacity

At 1,020 rps, the gateway accepts 18,360 events during the first 18 seconds. After that, it accepts only 20 rps. The `X-Rate-Limit-Remaining` value decreases from `18000` to `0`. The value remains `0` for the final accepted request before throttling and for all rejected requests after.

If requests continue at 1,020 rps with even distribution, `X-Rate-Limit-Remaining` remains `0`, even for accepted requests.

The `X-Rate-Limit-Reset` value starts at `1` for the first 20 accepted requests, increases to `2` for the next 20, and reaches `900` for the first rejected request. Refilling the 18,000-event burst capacity at 20 rps takes 900 seconds.

The gateway includes `Retry-After` only in rejected requests.

---
