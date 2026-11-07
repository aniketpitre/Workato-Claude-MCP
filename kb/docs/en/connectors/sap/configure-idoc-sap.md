---
url: 'https://docs.workato.com/en/connectors/sap/configure-idoc-sap.md'
description: >-
  Configure IDocs to and from Workato in SAP, including defining a port, logical
  system, partner profile, and distribution model for the connector.
---

# Optional: Configure IDocs to/from Workato in SAP

This section consists of the following steps:

1. [Define a port for Workato](#port-define)
2. [Create a logical system for Workato](#logical-system-create)
3. [Create partner profile for Workato](#profile-create)
4. [Create a distribution model for the partner](#model-create)

> **REQUIRED STEPS**
> 
> If you plan to only use RFCs and not IDocs with the SAP RFC connector, skip to [Create a Workato integration user in SAP.](/en/connectors/sap/integration-user-create#workato-integration-create)

> **LOGICAL SYSTEM/PARTNER PROFILE, PROGRAM ID, AND RFC DESTINATION**
> 
> As a requirement for an IDoc exchange through the Workato RFC connector, the logical system representing Workato and the program ID from the RFC destination used for the Workato connection must have the same name. Alternatively, you must configure at least one IDoc message type in the Outbound partner profile in `WE20`. This message type must have a port corresponding to the program ID from the RFC destination used for the Workato connection. To maintain consistency, we recommend using the same name for the logical system, program ID, and RFC destination in SAP for Workato whenever possible.
> 
> This recommendation is not mandatory for the **Send IDoc (Advanced)** action.

* * *

## Configuration for partner type LS

### Define a port

Log in to the SAP system and go to the transaction code `WE21` to define a port for sending and receiving IDocs with the **Transactional RFC** type.

1. Click **Create** and when prompted for your port, you can select to either create a new port or have one generated for you. ![IDoc ports](/assets/idoc-ports.uvLDCkL9.png)
   
2. Save this port name as you must use it later in the ALE configuration process.
   
3. Enter your **RFC Destination** created in the preceding steps (refer to this [section](/en/connectors/sap/rfc-destination-create) for more details). In this example, the RFC Destination is `WORKATOTST`.
   
   ![IDoc port for Workato](/assets/idoc-port-workato.Cz6FmJ80.png)
   

* * *

### Create a Logical System

Go to transaction code `SALE` and define a **Logical System** dedicated for Workato.

![Display IMG](/assets/display-img.BsPUdeG5.png)

1. Create a new **Logical System** to interface IDocs. The name you select is also used for the **Partner Profile** created in the following steps.
   
   ![Display IMG](/assets/logical-system.DllLowUE.png)
   

* * *

### Create a Partner profile

Go to transaction code `WE20` to define a **Partner profile** to send and receive IDocs.

![Partner profiles](/assets/partner-profiles.BefOZKOT.png)

1. Create a **Partner profile** with the **LS (Logical System)** type. Use the same name as the **Logical System** in the preceding step.
   
2. Define the **Message types** that you plan to send and receive in Workato.
   
   ![Message types](/assets/message-types.DtaspODi.png)
   
   <dl><dt>Outbound parameters</dt><dd>Outbound parameters correspond to IDocs sent from SAP to Workato.</dd><dt>Inbound parameters</dt><dd>Inbound parameters correspond to IDocs sent from Workato to SAP.</dd></dl>
   
   > **MESSAGE TYPES**
   > 
   > The message types you define here are the only message types you can use in your Workato recipes.
   
3. While adding Outbound parameters, when prompted for the `Basic Type` of the IDoc message type, register all of the IDocs you plan to use individually. For IDocs with extensions, ensure that you enter the extension as well.
   
   ![Outbound parameters](/assets/outbound-parameter.BwRm2hzH.png)
   
   > **UNRELEASED SEGMENTS, EXTENSIONS**
   > 
   > We do not populate schema for unreleased IDoc segments and extensions. If you plan to use the extended IDocs, ensure that you release the custom extension and segments where applicable.
   
4. Provide the same port you defined in the [preceding steps](#port-define) when prompted for your receiver port, and then toggle the **Output Mode** to **Pass IDoc Immediately**.
   
   > **HANDLE BATCH TRIGGER**
   > 
   > To configure batch trigger for sending IDocs from SAP to Workato, select **Collect IDocs** where ABAP program `RSEOUT00` can be scheduled in the background to trigger IDocs at regular intervals and the field “Pack. Size” in the partner profile will be used to control how many IDocs are submitted for processing at a time. Additionally, please refer to the section [New IDocs batch trigger](/en/connectors/sap/new-idocs-batch-trigger) of this guide for more information.
   
5. Add the Inbound parameters you plan to use when prompted for the process code, and choose the appropriate process code for the message type.
   
6. Toggle the **Processing by Function Module** to **Trigger Immediately** and select the **Cancel Processing After Syntax Error** check box. ![Inbound parameters](/assets/inbound-parameter.CqBWD5sC.png)
   

* * *

### Create a distribution model and add message types

Complete the following steps to create your distribution model and add message types:

1. Go to transaction code `BD64` to create a **Distribution Model** for IDocs that interfaces with the Workato system. The direction of flow for the IDocs are configured in this transaction based on the attributes `Sender`, `Receiver`, and `Message type`.
   
   ![add message type](/assets/add_mes_type.DjC3JlS0.png)_Distribution Model_
   
2. Click the **Create Model View** icon and provide a relevant **Short text** as the description and **Technical Name** for the model view. For example, Short text can be `Model view for Workato` and Technical Name can be `WORKATOTST`.
   
3. Click the model view you created in the previous step and **Add Message Type** across Sender and Receiver respectively to configure both inbound and outbound scenarios.
   
4. Distribute the model view under **Edit > Model View > Distribute** to validate the ALE configuration. The following image shows the expected output if the ALE configuration is intact: ![distribute](/assets/distribute.Dus0K5mE.png)
   

ALE INTERFACE FOR BAPI

We support ALE interface for BAPIs which are created in transaction code `BDBG`. Complete the following prerequisite steps to configure your ALE interface:

1. Add BAPI in the distribution model in transaction code `BD64`. ![bapi idoc](/assets/bapi-idocs.Zdkoa6eP.png)_Example: ExchangeRate Object added with method GetDetail_
   
2. Add one dummy message type (for example:`SYNCH`) in the model view for both inbound and outbound scenarios if you only intend to use ALE interface for BAPI. ![distribution model](/assets/distri-model-non-ls.DkO4xtXb.png)_Distribution Model_
   
3. Add message type in inbound (process code: BAPI) and outbound profile parameters in transaction code `WE20`. ![bapi idoc](/assets/bapi-idoc-in-out.DUCaVGZJ.png)_Partner profile_
   

### Example

<dl><dt>Sender:</dt><dd><code>T90CLNT090</code> (SAP system)</dd><dt>Receiver:</dt><dd><code>WORKATOTST</code> (Logical system for Workato)</dd><dt>Message type:</dt><dd><code>DEBMAS</code>, <code>MATMAS</code>, <code>CREMAS</code></dd></dl>

The following configuration in the distribution model enables SAP to send `DEBMAS` IDocs to Workato. A Workato recipe receives them using the **New IDoc** trigger.

![Distribution model](/assets/distribution-model.Bhd5VP3p.png)

Create separate entries for each inbound and outbound IDoc registered on your partner profile in WE20. In the preceding example, the image demonstrates under the model view, `WORKATO Test System Model`, that:

1. T90CLNT090 can send WORKATOTST 4 types of IDocs: `CREMAS`, `DEBMAS`, `MATMAS`, and `INVOIC`. These correlate to the **OUTBOUND parameters** set in your **Partner profile**.
2. WORKATOTST can send T90CLNT090 3 types of IDocs: `CREMAS`, `DEBMAS`, and `MATMAS`. These correlate to the **INBOUND parameters** set in your **Partner profile**.

* * *

## Configuration for non-LS partner types

We support all non-LS partner types including B, BP, GP, KU, LI, and US.

### Prerequisites

1. Configure the partner profile and receiver port in transaction code `WE20` and `WE21` respectively, to use IDoc trigger in Workato for non-LS partner types.
   
2. Complete the following steps to load the IDoc schema for a non-LS partner type in the **Send IDoc** action in Workato even if you do not plan to use partner type **LS**:
   
   1. Add the same message type to the inbound parameters of the partner type **LS** as well in transaction code `WE20`. ![partner profile](/assets/partner-profile-inbound-non-ls.xRjBTHAY.png)_Example from Partner type KU_
      
      ![partner profile](/assets/partner-profile-inbound-ls.BjPCEUsu.png)_Example from Partner type LS_
      
   2. Configure outbound parameters in transaction code `WE20` to use the same receiver port for non-LS partner types as used and created for partner type **LS**. ![partner profile](/assets/partner-profile-non-ls.BURdi4VS.png)_Example from Partner type KU_
      
      ![partner profile](/assets/partner-profile-ls.DGidIyz-.png)_Example from Partner type LS_
      
   3. Create a distribution model with both inbound and outbound scenarios (using logical systems) in transaction code `BD64`. You can use a dummy message type, for example: `SYNCH`. ![distribution model](/assets/distri-model-non-ls.DkO4xtXb.png)_Distribution Model_
      

### Send IDoc action

Complete the following steps to send your IDoc action:

1. Select the **IDoc name** from the drop-down to load the IDoc schema.
   
2. Modify the RCVPRT (Partner type of receiver) in EDI\_DC40 segment, refer to [Default IDoc parameters](/en/connectors/sap/action-send-idoc#default-idoc-parameters) for more details.
   
   ![send idoc action](/assets/send-idoc-non-ls.DhpDEuO4.png)_EDI\_DC40 segment_
   

> **FURTHER READING**
> 
> To complete your connection to SAP RFC, read the following guides:
> 
> 1. [Create RFC destination for Workato in SAP](/en/connectors/sap/rfc-destination-create)
> 2. [Create a Workato integration user in SAP](/en/connectors/sap/integration-user-create)
> 3. [Configure OPA for SAP](/en/connectors/sap/opa-configure)
> 4. [Configure the Workato SAP connector](/en/connectors/sap/sap-connector)

---
