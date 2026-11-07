---
url: >-
  https://docs.workato.com/en/connectors/oracle-ebs/actions/execute-pl-sql-operation.md
description: >-
  The Execute PL/SQL operation action executes  PL/SQL-based REST services
  deployed in your Oracle E-Business Suite system.
---

# Oracle E-Business Suite - Execute PL/SQL operation action

The **Execute PL/SQL operation** action executes PL/SQL-based REST services deployed in your Oracle E-Business Suite system. Use this action to run custom business logic, data validation routines, and complex operations exposed through the Integrated SOA Gateway.

Only interfaces deployed as REST services appear in the action's drop-down menus. Refer to Oracle's [Deploying REST Web Services](https://docs.oracle.com/cd/E18727_01/doc.121/e12169/T682519T513044.htm#isgig_restdeploy) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Product family | Select the Oracle E-Business Suite product family that contains the interface. Examples include `Financials`, `Order Management Suite`, and `Supply Chain Management`. |
| Product | Select the specific product within the product family. Examples include `Payables`, `Receivables`, and `Order Management`. |
| Interface | Select the interface. Only interfaces deployed as REST services appear in this list. |
| Operation name | Select the operation to execute. |
| Operation input | Provide the input parameters required by the operation. Fields vary based on the selected operation. |

## Output

| Output field | Description |
| --- | --- |
| Operation output | The data returned by the PL/SQL operation. Structure varies based on the operation executed. |
| ISG service fault | Error information if the operation fails. Present only when errors occur. |
| Code (ISG service fault) | Oracle error code identifying the type of failure. |
| Message (ISG service fault) | Human-readable error message describing what went wrong. |
| Resolution (ISG service fault) | Suggested steps to resolve the error. |
| Service detail (ISG service fault) | Additional context about where the error occurred. |
| Service name (Service detail) | The REST service that encountered the error. |
| Operation name (Service detail) | The operation that failed. |
| Instance ID (Service detail) | Unique identifier for the service invocation instance. |
