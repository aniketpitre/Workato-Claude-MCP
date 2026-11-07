---
url: 'https://docs.workato.com/en/troubleshooting/422-unprocessable-entity.md'
description: >-
  Learn why the 422 Unprocessable Entity error occurs in Workato from invalid or
  conflicting input data, and how to troubleshoot and fix it.
---

# 422 Unprocessable Entity

The **422 Unprocessable Entity** error occurs when the external service receives a request but can't process it due to issues with the input data. This typically means the request contains invalid values, is missing required data, or includes values that conflict with existing data.

![Example of 422 Unprocessable entity](/assets/422-unprocessable-entity.r4-kp8gv.png)_Example of 422 Unprocessable Entity error_

## Why it happens

The following issues often trigger a **422 Unprocessable Entity** error in Workato:

- The recipe tries to create a record with a value that already exists for a unique field, such as an email or ID.
- The recipe tries to update a record that doesn't exist.
- The recipe uses reference IDs that don't match any existing records.
- The request leaves a required field blank or includes an invalid value.

## How to troubleshoot

Complete the following steps to resolve the error:

1. Check for conflicts in unique fields. If you create a record, ensure the value, such as an email or ID, doesn't already exist in the external app.
   
2. Verify that the record exists before you run an **Update record** action. If the record is missing, create it first.
   
3. Use only valid reference IDs. For example, if you assign a Salesforce lead to a sales representative, ensure the sales representative exists in Salesforce.
   
4. Populate all required fields. Don't leave required fields blank.
   

Contact [Workato support](https://support.workato.com) if the issue persists.

---
