---
url: 'https://docs.workato.com/en/troubleshooting/500-internal-server-error.md'
description: >-
  Learn why the 500 Internal Server Error occurs in Workato from a server-side
  failure in the external service, and what to do next.
---

# 500 Internal Server Error

A **500 Internal Server Error** occurs when the external service fails to process a request due to an internal issue on its end. This error indicates a server-side failure, and the response often doesn't include enough detail to identify the cause.

![Non-descriptive 500 Internal Server error message](/assets/netsuite-500-internal-error.DyYR0To5.png)_Non-descriptive 500 Internal Server error message_

## Why it happens

The following conditions commonly trigger a 500 error in Workato:

- The external service is temporarily unavailable or returns an internal failure.
- The request is valid, but the external server encounters an unexpected error during processing.

The error message typically doesn't provide enough detail to identify the cause. You may see this error in any app connector or HTTP-based integration.

## What to do next

You can't resolve 500 errors directly in Workato. Contact [Workato support](https://support.workato.com/en/support/tickets/new) to help diagnose the issue.

---
