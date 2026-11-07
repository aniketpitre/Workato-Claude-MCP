---
url: 'https://docs.workato.com/en/connectors/sap/action-check-idoc.md'
description: >-
  The Check IDoc status action in the SAP connector lets you verify whether an
  IDoc sent from Workato was successfully processed in SAP.
---

# SAP - Check IDoc status action

![Action Check IDoc Status](/assets/action-check-idoc.DgtOcfVZ.png)

This action allows you to check if an IDoc is successfully processed in SAP, after being sent from Workato.

Workato automatically attaches a unique **Submission ID** to your IDoc when you use the [Send IDoc](/en/connectors/sap/action-send-idoc) action. Use this **Submission ID** in the following input field:

> **ERROR BEHAVIOR**
> 
> IDocs are processed asynchronously in SAP. Use this action to detect business failures that occur after SAP accepts an IDoc. Refer to [Error behavior in the SAP RFC connector](/en/connectors/sap/sap-error-behavior) for details on how technical and business errors surface for IDoc-based integrations.

* * *

## Input

| Field name | Description |
| --- | --- |
| Submission ID | When Workato sends an IDoc to SAP, we will attach a **Submission ID** to that IDoc. Find this **Submission ID** in the output of action [Send IDoc](/en/connectors/sap/action-send-idoc). |

* * *

## Output

| Field name | Description |
| --- | --- |
| IDoc number | SAP assigns this IDoc number after receiving the IDoc. |
| Status | Status of the IDoc after being received by SAP (Error, Success). |
| Status code | [Status code](/en/connectors/sap/track-idoc) of the IDoc after being received by SAP. |
| Status description | Status description of the IDoc after being received by SAP. |
| Detail | Long text of the IDoc after being received by SAP. (OPA v27 and above required to populate value for this field) |

* * *

> **FURTHER READING**
> 
> - [Learn more about status codes in SAP](/en/connectors/sap/track-idoc).

---
