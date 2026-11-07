---
url: 'https://docs.workato.com/en/connectors/sap/rfc-destination-create.md'
description: >-
  Create an RFC destination of type TCP/IP for Workato in SAP using transaction
  SM59, including program ID setup for OPA versions.
---

# Create an RFC Destination for Workato in SAP

In SAP, use Transaction `SM59` to create a new RFC Destination of type `TCP/IP` (type T).

> **REQUIRED STEPS**
> 
> - Setting up the RFC destination with a **Program ID** is a mandatory step until OPA v24.3.
> - Effective OPA v25, program ID is an optional field. (Leave it blank in the connection page if you only intend to use RFC/BAPI)

1. Select the `TCP/IP Connection` folder and click the **create** button.
   
   > **RFC DESTINATION NAME**
   > 
   > Use the RFC Destination name in accordance to the SAP system landscape. For example: the Development, Test, and Production environments can be `WORKATODEV`, `WORKATOTST`, and `WORKATOPRD` respectively.
   
   ![Create RFC connection](/assets/rfc-connection-create.C_0aXtl_.png)
   
2. In the **Technical Settings** tab, select the **Registered Server Program** option.
   
3. Enter `WORKATODEV`, `WORKATOTST`, or `WORKATOPRD` as the program ID, according to the SAP system landscape. These values are case-sensitive.
   
   > **PROGRAM ID**
   > 
   > There can be only one registration with a combination of **SAP Gateway host** + **SAP Gateway service** + **Program ID** active at one time. We recommend that you use a unique program ID to establish multiple connections from Workato pointing to different clients within the same SAP system.
   
   ![RFC destination](/assets/rfc-destination.BWwwzZeZ.png)
   
4. Proceed to the **MDMP & Unicode** or **Unicode** tab. Set the communication type to `Unicode`.
   
   ![RFC destination](/assets/rfc-unicode.-WYwcgHE.png)
   
5. Click **Save**. Your newly-created RFC destination should appear.
   
   ![RFC connections](/assets/rfc-connection.igk9xksN.png)
   

* * *

> **FURTHER READING**
> 
> Read the following guides to complete your connection to SAP RFC:
> 
> - [Create a Workato integration user in SAP](/en/connectors/sap/integration-user-create).
> - [Configure OPA for SAP](/en/connectors/sap/opa-configure).
> - [Configure the Workato SAP connector](/en/connectors/sap/sap-connector).
> - [Optional: Configure IDocs to/from Workato in SAP](/en/connectors/sap/configure-idoc-sap).

---
