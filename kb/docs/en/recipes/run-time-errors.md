---
url: 'https://docs.workato.com/en/recipes/run-time-errors.md'
description: >-
  Learn how to identify and troubleshoot run-time errors that occur during
  recipe job execution in Workato.
---

# Run-time errors

Run-time errors are errors that occur during the execution of a recipe, specifically within its jobs. A job is an individual run of a recipe, beginning with a trigger and followed by a series of actions. These jobs may involve Workato’s internal functions or interactions with external systems. The following sections address potential errors in both scenarios.

## How to identify run-time errors

To identify run-time errors, monitor your recipe's execution and review the error messages in the job history.

Complete the following steps to diagnose and resolve run-time errors:

1. Identify the error location by monitoring the [job history](/en/recipes/jobs#viewing-job-reports) in your Workato account.
   
2. Review the associated error messages and logs to gather more details about the failed job.
   
3. Determine whether the error is related to an action, trigger, or an external system.
   
4. Consult the appropriate troubleshooting guide based on the identified error type.
   

## Common run-time errors

Run-time errors occur while the recipe is running and prevent it from completing successfully. The following are some of the most common run-time errors you may encounter during recipe execution:

### Action errors

Action errors occur when a recipe action encounters a problem during execution. These errors can include data formatting errors, API call failures, or processing errors. Learn more about [action errors](/en/recipes/run-time-errors/action-internal-errors#action-errors).

### Trigger errors

Trigger errors occur when a recipe trigger fails to execute correctly. These errors can result from misconfigurations or external systems failing to provide the expected data. Learn more about [trigger errors](/en/recipes/run-time-errors/action-internal-errors#trigger-errors).

### Internal and upstream/downstream application errors

Errors may originate from within Workato (internal errors) or from external systems that the recipe interacts with (upstream/downstream application errors).

#### Internal errors

Internal errors occur within the Workato platform, such as issues with SQL collections, parsers, readers, or lookup tables. Learn more about [internal errors](/en/recipes/run-time-errors/internal-upstream-errors#internal-errors).

#### Upstream/downstream application errors

Upstream/downstream application errors involve external systems connected to the recipe, such as APIs, databases, or on-prem systems. You can troubleshoot these issues by understanding HTTP status codes and reviewing specific error messages. Learn more [upstream/downstream application errors](/en/recipes/run-time-errors/internal-upstream-errors#upstream-downstream-application-errors).

### APIM/webhooks

Errors may also occur when calling Workato through APIM (API Management) or webhooks. You can troubleshoot these errors by analyzing HTTP status codes and ensuring correct data payloads. Learn more about [APIM/webhooks errors](/en/recipes/run-time-errors/apim-webhooks).

---
