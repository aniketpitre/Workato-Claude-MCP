---
url: 'https://docs.workato.com/en/connectors/sendgrid/troubleshoot-sendgrid.md'
description: >-
  Troubleshoot the SendGrid 403 Forbidden error in Workato, including missing
  API key scopes and unverified sender identity or domain authentication.
---

# SendGrid - 403 Forbidden error

You may encounter a `403 Forbidden` error when you connect to SendGrid in Workato. This typically means that the API key doesn't have the required permissions.

## Why it happens

SendGrid returns a `403 Forbidden` error when the API key doesn't include the required scopes. For example, the connector can't send emails if the key doesn't include full access to the `Mail Send` scope. Restricted access or misconfigured permissions typically cause this issue.

## How to troubleshoot

Verify the API key settings in your SendGrid account. Ensure your SendGrid API key includes the required scopes for Workato to connect. The key must include full access to the `Mail Send` scope to send emails with SendGrid.

If the issue persists, review your SendGrid API key configuration and confirm the scopes. Retry the request a few minutes later so SendGrid can apply the updated API key permissions.

Refer to the SendGrid connection setup [prerequisites](/en/connectors/sendgrid#prerequisites) for more information.

## Confirm sender identity and feature access

SendGrid may return a 403 error if the sender address in the request isn't verified. The email address used to send the message must match a domain that you've authenticated in your SendGrid account. [Learn more](https://www.twilio.com/docs/sendgrid/ui/account-and-settings/how-to-set-up-domain-authentication).

Refer to SendGrid's [4XX API Errors and Troubleshooting Suggestions](https://support.sendgrid.com/hc/en-us/articles/18322114821403-4XX-API-Errors-and-Troubleshooting-Suggestions) for more details.

---
