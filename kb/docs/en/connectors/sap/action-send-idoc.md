---
url: 'https://docs.workato.com/en/connectors/sap/action-send-idoc.md'
description: >-
  The Send IDoc (Legacy) action in the SAP connector lets you send IDocs to an
  on-premise SAP system or a system behind a corporate firewall.
---

# SAP - Send IDoc action (Legacy)

![Action Send IDoc](/assets/action-send-idoc.DiWZLCpw.png)

This action allows you to send IDoc to an on-premise SAP system, or to an SAP system on a server behind the corporate firewall. You must [configure IDocs in your SAP system](/en/connectors/sap/configure-idoc-sap) before using this action.

> **LEGACY ACTION**
> 
> This action is a legacy version that is retained for backward compatibility. We recommend that you use the [Send IDoc (Advanced) action](/en/connectors/sap/action-send-idoc-advanced) instead. The Advanced action removes the need for dummy configurations that were previously required for this action.

## Input

| Field name | Description |
| --- | --- |
| IDoc name | The IDoc to send. You can select an IDoc name from the picklist or enter IDoc name directly. The picklist only displays [IDocs that are configured in the partner profile in your SAP system](/en/connectors/sap/configure-idoc-sap#profile-create). |
| Wait for SAP to process the IDoc? | IDoc is processed asynchronously in SAP. So you can configure the recipe to wait for the processing to finish before moving on to the next recipe step. |
| Check IDoc status every | This field will appear if **Wait for SAP to process the IDoc** is set to **Yes**. Select how often Workato should call SAP. This is useful when you want to control the workload of your SAP system. |

> **ERROR BEHAVIOR**
> 
> The Send IDoc action confirms that SAP accepted the IDoc at a technical level. A successful step doesn't indicate that SAP completed business processing. Business failures may surface later through IDoc status tracking rather than as step-level errors. Refer to [Error behavior in the SAP RFC connector](/en/connectors/sap/sap-error-behavior) for details.

After IDoc is selected, you can select IDoc input segments and fields. In this example, `E1MARAM` and `EDI_DC40` are selected.

![IDoc input segment 1](/assets/idoc-input-1.D-KPoa2t.png)

![IDoc input segment 2](/assets/idoc-input-2.CtP-RtnB.png)

### Default IDoc parameters

Workato provides the following default values for EDI\_DC40 segments. Beginning with OPA version 22.2, providing values for the following attributes in EDI\_DC40 segments overrides the default values. Other fields in the EDI\_DC40 segment are empty by default.

| Field Name | Description | OPA V22.1 and prior | OPA V22.2 and above | Default value |
| --- | --- | --- | --- | --- |
| SNDPRT | Partner type of sender | Cannot be overridden | Can be overridden | `LS` indicates Logical System. |
| SNDPOR | Sender port | Cannot be overridden | Can be overridden | The ALE port definition based on the current connection. |
| SNDPRN | Partner number of sender | Cannot be overridden | Can be overridden | The partner number defined in the distribution model based on the current connection. |
| RCVPRT | Partner type of receiver | Cannot be overridden | Can be overridden | `LS` indicates Logical System. |
| RCVPOR | Receiver port | Cannot be overridden | Cannot be overridden | `SAP` plus `systemName`. System name is determined by the current connection to the SAP server: host/user/password, and prefixed with `SAP`. For example, if the `systemName` is `XYZ`, the `ReceiverPort` is `SAPXYZ`. |
| RCVPRN | Partner number of receiver | Cannot be overridden | Can be overridden | The SAP server's partner number. |
| ARCKEY | Key for external message archive | Can be overridden | Can be overridden | Unique submission ID which enables Workato to track IDoc status. If overridden, checking for IDoc status in the "Send IDoc" action and "Check IDoc Status" actions will not work. We recommend that you leave this field blank. |
| MANDT | Client | Can be overridden | Can be overridden | The value of the `user_logon.client` provided in the current connection. |
| DIRECT | Direction of communication | Can be overridden | Can be overridden | `1` indicates Outbound communication. We recommend that you leave this field blank. |
| OUTMOD | Output mode | Can be overridden | Can be overridden | `2` indicates the output mode in the sender application. |
| MESTYP | Message type | Can be overridden | Can be overridden | The selected IDoc message type based on the IDoc you select. For example, if you select the IDoc `ORDERS.ORDERS05.ZORDERS`, the message type is `ORDERS`. |
| IDOCTYP | Basic IDoc type | Can be overridden | Can be overridden | The selected IDoc basic type based on the IDoc you select. For example, if you select the IDoc `ORDERS.ORDERS05.ZORDERS`, the basic type is `ORDERS05`. |
| CIMTYP | Extension type | Can be overridden | Can be overridden | The selected IDoc basic type based on the IDoc you select. For example, if you select the IDoc `ORDERS.ORDERS05.ZORDERS`, the extension type is `ZORDERS`. If no extension is selected, then this field is empty. |

## Output

| Field name | Description |
| --- | --- |
| IDoc number | SAP assigns this IDoc number after receiving the IDoc. |
| Status | Status of the IDoc after being received by SAP. |
| Status code | Status code of the IDoc after being received by SAP. |
| Status description | Status description of the IDoc after being received by SAP. |
| Submission ID | When Workato sends an IDoc to SAP, we will attach a **Submission ID** to that IDoc. You can use that ID to check for IDoc status using action [Check IDoc Status](/en/connectors/sap/action-check-idoc). |
| Detail | Long text of the IDoc after being received by SAP. (OPA v27 and above required to populate value for this field) |

---
