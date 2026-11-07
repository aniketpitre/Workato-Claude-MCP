---
url: 'https://docs.workato.com/en/recipes/run-time-errors/apim-webhooks.md'
description: >-
  Troubleshoot APIM and webhook call errors in Workato by checking network
  connectivity, access permissions, and HTTP status codes.
---

# APIM/webhook calls at run time

When interacting with Workato through APIM or webhooks, errors can arise that may not be immediately clear. Use the following guidelines to troubleshoot these issues effectively:

## Verify network connectivity

Ensure that the server calling Workato has internet access. Network restrictions or firewall settings can disrupt the connection. If your application or server security setup requires outbound connections to be allowlisted, verify that you’ve included Workato’s IP addresses. For the most current list of Workato's IPs, refer to our [IP allowlists](/en/security/ip-allowlists) documentation.

## Configure access permissions

Workato allows you to restrict which IPs can access its API Management (APIM) endpoints. Secure your endpoints by allowlisting the specific IP addresses permitted to make these calls. Refer to the [API clients and API keys](/en/api-mgmt/api-client-mgmt#api-clients) documentation for instructions on configuring your IP allowlist.

## Review HTTP status codes

After verifying network connectivity and access permissions, check the HTTP status code provided by Workato. This code can offer valuable insight into the nature of the problem and guide your next steps. For a detailed understanding of HTTP status code replies when using Workato HTTP connector actions, refer to the [Categorize HTTP status responses](/en/recipes/run-time-errors/internal-upstream-errors#categorize-http-status-responses) section. If you don’t find a readable status code, investigate further using logs or by reaching out to Workato support for assistance.

---
