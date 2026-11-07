---
url: 'https://docs.workato.com/en/troubleshooting/400-bad-request-error.md'
description: >-
  Learn why the 400 Bad Request error occurs in Workato from malformed requests
  or invalid input, and how to troubleshoot and resolve it.
---

# 400 Bad Request

The **400 Bad Request** error occurs when the external server can't process a request because it's malformed or invalid. This typically results from incorrect formatting, invalid field values, or missing required data.

![Example of 400 Bad Request error](/assets/400-bad-request.BlUsKsnz.png)_Example of 400 Bad Request error_

## Why it happens

The following conditions commonly trigger this error in Workato:

- A recipe sends a request with improperly formatted field or column names.
- Required input fields are empty or contain invalid values.
- The request includes an invalid record ID.
- A file exceeds the external app's size limits.

You may encounter this in HTTP connector actions, custom connectors, or app-specific actions that require structured input.

## How to troubleshoot

Complete the following steps to identify and resolve the error:

1. Check that field or column names match the expected format. Confirm case sensitivity and naming conventions, such as snake case or camel case.
   
2. Confirm that record IDs are correct and that all required fields are populated.
   
3. Check file size constraints. If your request uploads a file, ensure the file size meets the receiving service's quotas.
   
4. Reconnect the app to ensure the request uses a valid and current authentication token.
   

Contact [Workato support](https://support.workato.com) if the issue persists.

---
