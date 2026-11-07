---
url: 'https://docs.workato.com/en/troubleshooting/404-not-found.md'
description: >-
  Learn why the 404 Not Found error occurs in Workato when a record or
  identifier is invalid, and how to troubleshoot and resolve it.
---

# 404 Not Found

The **404 Not Found** error occurs when the external service can't locate the resource your recipe tries to access. This typically means the record doesn't exist, or the request includes an invalid identifier.

![Example of 404 Not Found error](/assets/404-not-found.46_ND3fC.png)_Example of 404 Not Found error_

## Why it happens

The following issues commonly trigger a **404 Not Found** error in Workato:

- The recipe references a record ID that doesn't exist.
- The recipe uses a valid ID, but for the wrong object or application.
- The external app deleted or archived the record.

## How to troubleshoot

Complete the following steps to resolve the error:

1. Map the datapills to the correct fields and confirm that the record ID matches the expected format for the external app.
   
2. Confirm that the record ID is valid for the application. For example, use a Salesforce ID for a Salesforce record.
   
3. Ensure the record ID matches the correct object type. For example, use a customer ID for a customer object.
   
4. Check that the record still exists in the external app and hasn't been deleted or archived.
   

Contact [Workato support](https://support.workato.com) if the issue persists.

---
