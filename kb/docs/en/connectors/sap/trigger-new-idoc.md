---
url: 'https://docs.workato.com/en/connectors/sap/trigger-new-idoc.md'
description: >-
  The New IDoc trigger in the SAP connector listens to and receives IDocs from
  an on-premise SAP system or a system behind a corporate firewall.
---

# SAP - New IDoc trigger

![Trigger New IDoc](/assets/trigger-new-idoc.D_D_Qxkf.png)

This trigger allows you to listen to and receive IDocs from an on-premise SAP system, or from a SAP system on a server behind a corporate firewall.

> **IDOC DEDUPLICATION**
> 
> When you resend the IDoc, recipes that previously received the IDoc do not process it again due to Workato's deduplication logic.

> **BEFORE YOU BEGIN**
> 
> You must [configure IDocs in your SAP system](/en/connectors/sap/configure-idoc-sap) before using this trigger.

* * *

## Input

| Field name | Description |
| --- | --- |
| IDoc name | The IDoc to listen to. Select an IDoc name from the drop-down menu or enter an IDoc name manually using the format `message_type.basic_type.extension`. For example: **ORDERS.ORDERS05** or **DEBMAS.DEBMAS03.ZDEBMAS**. Note that the picklist only displays [IDocs that are configured in the partner profile in your SAP system](/en/connectors/sap/configure-idoc-sap#profile-create). |

> **MESSAGE TYPE, BASIC TYPE, AND CUSTOM EXTENSIONS**
> 
> We subscribe to one **message type**, **basic type**, and **custom extension** (if applicable) at a time. You must maintain the recipe logic to ensure that the workflow processes appropriately for different partners. For example, you can apply the condition on the RCVPRN datapill from the trigger or add the RCVPRT datapill in addition to the RCVPRN datapill.

Starting in OPA v27.1, SAP partner details are included automatically in the IDoc description. The description shows the partner number/partner profile and partner type. These values come from the message type, IDoc type, and custom extensions included in the ALE configuration for SAP transaction codes `WE20` and `BD64`. ![Trigger New IDoc Description](/assets/idoc-trigger-description.CASNvgYf.png)_New IDoc description_

In earlier OPA versions, the description only shows the total number of partners if there is more than one. The description doesn't include partner details. ![Trigger New IDoc Description Old OPA](/assets/idoc-trigger-desc-old.DOQtle0Y.png)_IDoc description with earlier OPA version_

> **BATCH IDOC TRIGGER**
> 
> Enhanced descriptions also applies to the [Batch IDoc trigger](/en/connectors/sap/new-idocs-batch-trigger).

* * *

## Output

The trigger outputs all segments and data fields of the IDoc received from SAP. In this sample IDoc, `EDI_DC40` and `E1MARAM` segments.

![Trigger New IDoc output](/assets/trigger-new-idoc-output.T5E8Sdar.png)

* * *

> **FURTHER READING**
> 
> - [Learn how to track IDoc status in SAP](/en/connectors/sap/track-idoc).

---
