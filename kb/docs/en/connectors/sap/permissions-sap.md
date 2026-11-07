---
url: 'https://docs.workato.com/en/connectors/sap/permissions-sap.md'
description: >-
  Review the minimum SAP authorizations required to run the SAP connector
  triggers and actions, including New IDoc, Send IDoc, and Run RFC.
---

# Minimum permissions to run actions and triggers

The following permissions are required to run actions and triggers.

* * *

## New IDoc trigger

| Authorization Object | Activity (ACTVT) | Extension (EDI\_CIM) | Basic type (EDI\_DOC) | Transaction Code (EDI\_TCD) |
| --- | --- | --- | --- | --- |
| S\_IDOCDEFT | 03 | \[extension of IDOC if any\] | \[Basic type of IDoc - e.g. DEBMAS07\] | WE30 |

![Receive IDoc permissions](/assets/receive_idoc_permissions.CpWVeZSo.png)

* * *

## Send IDoc action

- Authorizations found in the [permissions section of the setup guide](/en/connectors/sap/integration-user-create#role-create)
- Authorizations required for the preceding [New IDoc trigger](#new-idoc-permissions).

Additionally, sending an IDoc requires the following authorization:

| Authorization Object | Message Type (EDI\_MES) |
| --- | --- |
| B\_ALE\_RECV | \[Message type of IDoc - e.g. DEBMAS\] |

![Send IDoc permissions](/assets/send_idoc_permissions.Dh0QJzE2.png)

* * *

## Run RFC action

Unfortunately, the authorizations depend largely on the RFC chosen and its parameters as well. To this end, we would suggest using ST01 to find the absolute minimum permissions required. You can use t-code ST01 to set up a trace. Select **Authorization check** and provide the user name of the Workato user in **General filters**.

![SAP connection](/assets/set-trace.BxUjne6s.png)

Turn your trace on by selecting **Trace On** in the top bar. After this, get your OPA live and begin to attempt to run the triggers and actions. With only the minimum permissions set out to create the integration user, you should hit errors. You can observe the authorization errors by selecting **Analysis** in the top navigation bar.

Select display and you should see where your permissions have failed. Add these permissions to the Authorization role you created for Workato in Step ... of the setup guide. The following example demonstrates how to read the **Trace display**. This enables you to determine additional required authorizations.

![SAP connection](/assets/set-trace.BxUjne6s.png)

> **TURN OFF TRACE**
> 
> When complete, ensure that you turn trace off. Turn off trace by selecting **Trace Off** in t-code ST01.

---
