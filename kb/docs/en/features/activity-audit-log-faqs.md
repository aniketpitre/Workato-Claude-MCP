---
url: 'https://docs.workato.com/en/features/activity-audit-log-faqs.md'
description: >-
  Answers to common questions about the Workato Activity audit log, including
  enabling it, customizing messages, and streaming retries.
---

# Activity audit log FAQs

Get answers to frequently asked questions (FAQs) about Activity audit logs.

## What is the Activity audit log in Workato?

View answer

The [Activity audit log](/en/features/activity-audit-log#activity-audit-log) provides a comprehensive interface for Workato administrators to track changes made by users in their account. This includes user activities such as logins, recipe modifications, and more. It allows administrators to monitor and analyze changes for security and operational insights.

## How do I enable the Activity audit log feature?

View answer

Contact your Workato Customer Success Manager to enable the [Activity audit log](/en/features/activity-audit-log#activity-audit-log) feature.

## How can I customize the audit log messages before streaming them?

View answer

You can [customize audit log messages](/en/features/activity-audit-log-streaming-customize-log#customize-log-message) in JSON format to include metadata, such as the source application or environment. Use the placeholders `log_message` and `log_message_str` to substitute the actual event message.

## Will audit log streaming still run if my logs exceed 40 MB?

View answer

Yes. However, the system does not send step-specific log lines if the overall [file size exceeds 40 MB](/en/features/activity-audit-log-streaming#audit-log-size). Instead, it sends contextual job information, such as `user_id`, `recipe_id`, and `time_executed`.

## Why are my audit logs stored in a persistent cache?

View answer

Audit logs are stored in a [persistent cache](/en/features/activity-audit-log-streaming-retry#audit-log-streaming-retry) to enable Workato to retry sending data that didn't successfully reach the log streaming destination.

Workato removes audit logs from the persistent cache when one of the following occurs:

- The audit log reaches its destination successfully
- The data remains in the persistent cache for more than seven days

## Can I mask data in audit logs?

View answer

Yes. You can enable [data masking](/en/features/data-masking) to prevent Workato from logging or streaming the input or output of any trigger or action. When enabled, Workato replaces the step data with a placeholder instead of the actual values.

Refer to the [Does data masking apply to audit log streaming?](/en/features/activity-audit-log-streaming#does-data-masking-apply-to-audit-log-streaming) section for more information.

## What happens if my IAM role permissions for Amazon S3 are updated?

View answer

If you update your [IAM role permissions](/en/features/activity-audit-log-streaming-destinations#amazon-s3-bucket) for an Amazon S3 bucket, you must disconnect and re-establish the connection in Workato to ensure continued access for audit log streaming. This security feature helps manage resource access.

---
