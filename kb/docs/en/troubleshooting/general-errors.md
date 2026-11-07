---
url: 'https://docs.workato.com/en/troubleshooting/general-errors.md'
description: >-
  Reference for common HTTP error codes returned in Workato recipes, including
  400, 401, 403, 404, 422, and 500, with causes and fixes.
---

# General error codes

When a Workato recipe makes an API call that fails, the external service returns an HTTP error code. These codes appear in job reports and error handling datapills, and help you identify the cause of the failure.

This reference covers the most common HTTP error codes returned in Workato and links to guides that describe their causes and how to resolve them.

## Common HTTP error codes

The following table highlights the most frequently encountered HTTP error codes:

| Error code | Description |
| --- | --- |
| 400 Bad Request | The request sent to the external service is invalid or improperly formatted. [Learn more](/en/troubleshooting/400-bad-request-error). |
| 401 Unauthorized | Authentication failed due to invalid or expired credentials. [Learn more](/en/troubleshooting/401-unauthorized-error). |
| 403 Forbidden | The user or connection has authenticated but lacks permission to access the resource. [Learn more](/en/troubleshooting/403-forbidden-error). |
| 404 Not Found | The requested resource doesn't exist in the external app. [Learn more](/en/troubleshooting/404-not-found). |
| 422 Unprocessable Entity | The request contains valid syntax but invalid or unprocessable content. [Learn more](/en/troubleshooting/422-unprocessable-entity). |
| 500 Internal Server Error | The external service failed to process the request due to an internal issue. [Learn more](/en/troubleshooting/500-internal-server-error). |

Refer to the [Monitor errors with the handle errors step](/en/recipes/best-practices-error-handling#monitor-errors-with-the-handle-errors-step) section to learn how to detect and handle these errors in your recipes.

---
