---
url: 'https://docs.workato.com/en/troubleshooting/403-forbidden-error.md'
description: >-
  Learn why the 403 Forbidden error occurs in Workato when a connection lacks
  permissions, and how to troubleshoot it in triggers and actions.
---

# 403 Forbidden error

A **403 Forbidden** error indicates that your connection is not authorized to access a requested resource or perform a specified action.

![Example of 403 Forbidden error](/assets/403-forbidden-error.BWxGt9WW.png)_Example of **403 Forbidden** error_

## Why it happens

This error occurs when the connected app blocks access to a specific record or field due to insufficient permissions. For example, a connection might allow access to basic employee information but restrict sensitive fields such as salary or Social Security numbers. This typically happens when the connected user's role lacks the required scopes or privileges.

## How to troubleshoot

The steps to troubleshoot depend on whether the error occurs in a trigger or an action.

- [Action errors](#action-errors): Use network tracing to inspect the job and identify the step that returned the **403 Forbidden** error. Check the request and response to determine which data caused the issue.
- [Trigger errors](#trigger-errors): Tracing isn’t available for triggers. Instead, build a recipe using the Scheduler trigger to fetch and log records one at a time. This helps identify the record Workato can't access.

### Action errors

You can use [network tracing](/en/recipes/job-debug-tracing) to troubleshoot and identify the step that returned a **403 Forbidden** error. The trace shows which request triggered the error, such as the HTTP URL, headers, payload, and response.

Complete the following steps to resolve the issue:

1. Open the job and locate the step that returned the **403 Forbidden** error.
   
2. Inspect the HTTP response body in the debug trace for permission-related messages.
   
3. Review the request URL and payload to determine which data or resource the connector tried to access.
   
4. Check the connected user's role or token permissions in the app to confirm access to that data.
   
5. Update the user's role or access level in the app if necessary.
   
6. Reconnect the app in Workato if token scopes or user permissions changed.
   
7. Repeat the job to confirm that the issue is resolved.
   

### Trigger errors

If a **403 Forbidden** error occurs in a trigger, you can't use job debug tracing to inspect the request. However, you can build a diagnostic recipe to identify which specific record causes the error during the trigger execution.

Complete the following steps to troubleshoot:

1. Create a new recipe using the **Scheduler** trigger to simulate the records that the original trigger would process.
   
2. Add a list action to check which records the original trigger is trying to access. For example, if a **New employee** trigger returns a **403 Forbidden** error, use a **List employees** action to identify the record that the trigger can't process.
   
3. Add a **Repeat** action to loop through each record that was retrieved by the previous action.
   
   ![Add a Repeat action](/assets/403-add-repeat.-8QpiZGu.png)_Add a Repeat action_
   
4. Map a list datapill to the **Input list** field in the Repeat action. This ensures that the records retrieved in the previous step are processed individually during the loop.
   
   ![Input a list datapill](/assets/403-list-datapill.Btj5yCoN.png)_Input a list datapill_
   
5. Set the **Repeat mode** to **One item at a time** to isolate and check each record individually.
   
6. Add a **Handle errors** step inside the **Repeat** step to capture any errors triggered by processing a specific record.
   
   ![Add a Handle errors step](/assets/handle-error-403.mSLCyfWz.png)_Add a **Handle errors** step_
   
7. Add an action inside the monitor path to retrieve more details about the record that caused the error. For example, use a **Get details** action to retrieve more information about the record using its ID.
   
8. Add a **Logger by Workato** action inside the on error path to capture the record ID of the item that triggered the error.
   
   ![Log the record ID](/assets/403-log-id.DJeGJFQl.png)_Log the record ID_
   
9. Run the recipe and review the logs to identify which records returned a **403 Forbidden** error and investigate what caused the access issue.

---
