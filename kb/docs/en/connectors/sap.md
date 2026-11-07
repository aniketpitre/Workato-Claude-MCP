---
url: 'https://docs.workato.com/en/connectors/sap.md'
description: >-
  The SAP RFC connector lets you automate ERP workflows: send and track IDocs,
  call BAPIs and remote function modules, and trigger recipes on new IDocs.
---

# SAP RFC

SAP serves as an enterprise resource planning software adopted by most of the world's largest and significant corporations. The SAP RFC Connector allows you to connect with SAP systems even if they're behind a corporate firewall. The connector supports using IDoc or RFC to communicate with SAP. Using Workato, you can build powerful automation around SAP and other applications, without writing code.

The Workato SAP RFC connector is a [SAP-certified](https://sapblobs.blob.core.windows.net/csd-live/workato-rfc-connector-30-certificate-eee22820-bcfd-11ed-8582-6b093a4ee825) solution and recognized as a high quality, cost effective, and sustainable solution for SAP integration needs.

We initially developed the connector for on-prem SAP systems, but you can also use it with [SAP S/4HANA Cloud, private edition](https://www.sap.com/products/erp/s4hana-private-edition.html).

* * *

## Supported SAP versions

Workato's SAP RFC connector supports SAP ERP ECC 6.0 and all it's enhancement Packages, SAP S/4HANA (On-Premise Edition and Private Edition), SAP CRM, SAP SRM, SAP SCM, and any other products compatible with the NetWeaver AS ABAP.

* * *

## Supported communication methods

The connector supports the following communication methods with SAP:

- Inbound IDoc (Sending an IDoc from Workato to SAP).
- Outbound IDoc (Receiving an IDoc from SAP to Workato).
- Call Remote Functions (Invoke a function module in SAP from Workato).
- Call BAPI (Invoke a BAPI in SAP from Workato).

* * *

## Additional capabilities

The SAP RFC connector supports the following capabilities:

- Direct connection to SAP, allowing you to establish a connection to the application server.
- Message server connection to SAP, allowing you to establish a connection to the load balancer.
- Encrypted communication between an OPA and your SAP instance using Secure Network Communications (SNC). Refer to our [Enabling SNC encryption](/en/connectors/sap/snc-encryption) documentation to learn more about this capability.
- Custom BAPI/RFC and extended IDocs.

* * *

## SAP Certified

Beginning March, 06 2023, our SAP RFC connector is [SAP certified](https://www.sap.com/dmc/exp/sap-certified-solutions/#/solutions?search=Worka&id=s:5f017ab0-bfce-43c1-aeb7-bfe2584d3f20) for the following capabilities:

- Access SAP Business Objects Repository (BOR) based on Application Components
- Extract RFC/BAPI/IDOC Meta Data
- Exchange RFC/BAPI/IDOC calls including SAP return parameters
- Unicode communication enabled

![Create RFC connection](/assets/SAP-certified.BvXUkMXR.png)_SAP Certified Solutions Directory_

> **SAP ODP-BASED EXTRACTION**
> 
> The SAP RFC connector fully complies with SAP best practices for third-party integration. According to [SAP Note 3255746](https://me.sap.com/notes/3255746/E), customers and third-party applications are not allowed to use remote function modules related to the Operational Data Provisioning (ODP) Data Replication API to access SAP ABAP sources. Instead, SAP recommends using ODP-based data extraction through externally consumable [OData services](https://help.sap.com/docs/SAP_NETWEAVER_750/ccc9cdbdc6cd4eceaf1e5485b1bf8f4b/11853413cf124dde91925284133c007d.html?locale=en-US). This can be achieved by using Workato platform connectors such as the [SAP OData connector](/en/connectors/sap-odata) or the [universal HTTP connector](/en/developing-connectors/http-v2).

* * *

## Prerequisites

You must have the following to use the SAP RFC connector:

- The SAP JCo library version 3.1.7 and above.

Refer to [SAP Note 2786882 - SAP JCo 3.1 release and support strategy](https://launchpad.support.sap.com/#/notes/2786882) for more details and to make sure your operating system fulfills all prerequisites.

> **DEPRECATION NOTICE**
> 
> Starting with OPA version 2.16, Workato no longer maintains support for JCo 3.0 libraries. Prior to submitting any support requests, ensure that you are now using the latest JCo 3.1.7 libraries or above. Refer to the [configuration section](/en/connectors/sap/opa-configure#library-download) for more information.
> 
> Additionally, if you use IDocs, you must use SAP Java Connector 3.1.7 libraries or above and [SAP Java IDoc Library 3.1.3](https://support.sap.com/en/product/connectors/jco.html) or above.

* * *

## Introduction to IDoc

`IDoc` stands for intermediate document. It is simply a data container used to exchange information between SAP systems or between SAP and third-party systems.

IDoc is an open interface which is independent of the internal data structure stored in SAP, and independent of sending or receiving applications. Any application can use IDoc by following the syntax and semantics of IDoc.

IDoc is independent of the direction of data exchange, having both outbound and inbound capabilities.

* * *

## Introduction to RFC

`RFC` is a protocol used in SAP to manage communication between SAP systems and third-party applications. It facilitates the invocation of function modules residing on remote SAP systems from calling programs.

Workato can call SAP RFCs residing in an SAP system to fetch the data returned or make synchronous updates to the SAP data. RFCs can also be configured to leveraged to call Workato directly from your SAP instance. Determine how to set up an API endpoint on Workato and [connect SAP directly to Workato here.](/en/connectors/sap/tls1.2#_2-adding-workato-ssl-certificates-to-trust-manager)

If you have trouble connecting to Workato with RFCs, review our [Troubleshooting guide](/en/connectors/sap/sap-troubleshooting) for more information.

* * *

> **FURTHER READING**
> 
> To complete your connection to SAP RFC, read the following guides:
> 
> 1. [Create RFC destination for Workato in SAP](/en/connectors/sap/rfc-destination-create)
> 2. [Create a Workato integration user in SAP](/en/connectors/sap/integration-user-create)
> 3. [Configure OPA for SAP](/en/connectors/sap/opa-configure)
> 4. [Configure the Workato SAP connector](/en/connectors/sap/sap-connector)
> 5. [Optional: Configure IDocs to/from Workato in SAP](/en/connectors/sap/configure-idoc-sap)

---
