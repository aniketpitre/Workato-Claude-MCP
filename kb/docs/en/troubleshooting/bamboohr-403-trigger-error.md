---
url: 'https://docs.workato.com/en/troubleshooting/bamboohr-403-trigger-error.md'
description: >-
  Learn why the BambooHR connector returns 403 errors from restricted employee
  fields or data categories, and how to resolve the permissions.
---

# BambooHR - 403 Forbidden errors

The BambooHR connector returns 403 errors when the connection lacks access to specific employee fields or data categories.

## Troubleshooting steps

Refer to the [403 Forbidden error](/en/troubleshooting/403-forbidden-error) troubleshooting guide to isolate the record that caused the error.

## Why 403 errors happen in BambooHR

Not all 403 errors result from missing access to individual fields. In many cases, BambooHR roles restrict access to entire sections of the employee profile, such as compensation, job information, or custom tabs, while still allowing access to the employee list.

These errors may also occur if the connected user lacks access to certain employee statuses, such as terminated or inactive employees, or to custom profile tabs that require additional permissions.

To resolve the issue, review the connected user's role in BambooHR and confirm they have access to all data types your recipe uses.

> **IDENTIFY 403 ERRORS**
> 
> Use the following actions to build a diagnostic recipe that identifies the record that causes the 403 error:
> 
> - [List employees in directory](/en/connectors/bamboo-hr/list-employees-in-directory-action): Return a list of employee records.
> - [Get employee details by ID](/en/connectors/bamboo-hr/get-employee-details-action): Return full profile details for a single employee.

---
