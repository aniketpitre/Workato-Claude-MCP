---
url: 'https://docs.workato.com/en/connectors/sap.md'
description: >-
  The SAP RFC connector lets you automate ERP workflows: send and track IDocs,
  call BAPIs and remote function modules, and trigger recipes on new IDocs.
---

# SAP RFC

SAP is an enterprise resource planning (ERP) system used by many large organizations. The SAP RFC connector lets you connect to SAP systems, including systems behind a corporate firewall. The connector uses IDocs or RFCs to communicate with SAP. You can build automations between SAP and other applications without writing code.

The SAP RFC connector was designed for on-prem SAP systems, but it is also compatible with [SAP S/4HANA Cloud, private edition](https://www.sap.com/products/erp/s4hana-private-edition.html).

* * *

## Supported SAP versions

The SAP RFC connector supports SAP ERP ECC 6.0 and all its enhancement packages, SAP S/4HANA (on-premise and private editions), SAP CRM, SAP SRM, SAP SCM, and other products compatible with SAP NetWeaver AS ABAP.

* * *

## Supported communication methods

The connector supports the following communication methods with SAP:

- Inbound IDoc: Send an IDoc from Workato to SAP.
- Outbound IDoc: Receive an IDoc from SAP in Workato.
- Call remote functions: Invoke a function module in SAP from Workato.
- Call BAPI: Invoke a BAPI in SAP from Workato.

* * *

## Additional capabilities

The SAP RFC connector supports the following capabilities:

- Direct connection to the SAP application server.
- Message server connection to the SAP load balancer.
- Encrypted communication between the on-prem agent and your SAP instance through Secure Network Communications (SNC). Refer to [Enable SNC encryption](/en/connectors/sap/snc-encryption) for more information.
- Custom BAPIs, custom RFCs, and extended IDocs.

* * *

## SAP integration practices

The Workato SAP RFC connector supports RFC-based integration in accordance with SAP-supported integration practices and doesn't rely on the restricted Operational Data Provisioning (ODP) Data Replication API.

> **SAP ODP-BASED EXTRACTION**
> 
> According to [SAP Note 3255746](https://me.sap.com/notes/3255746/E), customers and third-party applications aren't permitted to use RFC modules associated with the ODP Data Replication API to access SAP ABAP sources. These modules are intended only for SAP-internal applications.
> 
> SAP provides an officially supported, externally consumable [OData API](https://help.sap.com/docs/SAP_NETWEAVER_750/ccc9cdbdc6cd4eceaf1e5485b1bf8f4b/11853413cf124dde91925284133c007d.html?locale=en-US) for ODP-based extraction. Workato supports this approach through the [SAP ODP](/en/data-orchestration/data-pipeline-recipe/configure-sap-agent-odp) source in data pipelines, which is part of SAP Data Agent. You can also consume externally exposed OData services with the [SAP OData connector](/en/connectors/sap-odata) or the [universal HTTP connector](/en/developing-connectors/http-v2).

* * *

## Prerequisites

You must have the following to use the SAP RFC connector:

- SAP JCo library version 3.1.7 or later.

Refer to [SAP Note 2786882 - SAP JCo 3.1 release and support strategy](https://launchpad.support.sap.com/#/notes/2786882) to confirm your operating system meets all prerequisites.

> **DEPRECATION NOTICE**
> 
> Workato doesn't support JCo 3.0 libraries in on-prem agent version 2.16 and later. Make sure you use JCo 3.1.7 libraries or later before you submit a support request. Refer to [Download the SAP JCo libraries](/en/connectors/sap/opa-configure#library-download) for more information.
> 
> IDocs require SAP Java Connector 3.1.7 libraries or later and [SAP Java IDoc Library 3.1.3](https://support.sap.com/en/product/connectors/jco.html) or later.

* * *

## Introduction to IDoc

An intermediate document (IDoc) is a data container that exchanges information between SAP systems, or between SAP and third-party systems.

IDoc is an open interface that's independent of the internal data structure in SAP and of the sending and receiving applications. Any application that follows IDoc syntax and semantics can use IDocs.

IDocs support both inbound and outbound data exchange.

* * *

## Introduction to RFC

Remote Function Call (RFC) is a protocol that manages communication between SAP systems and third-party applications. Calling programs use RFC to invoke function modules on remote SAP systems.

Workato can call RFCs in an SAP system to fetch data or make synchronous updates to SAP data. You can also configure RFCs to call Workato directly from your SAP instance. Refer to [Configure SAP to interact with the Workato API platform](/en/connectors/sap/tls1.2#_2-adding-workato-ssl-certificates-to-trust-manager) to set up an API endpoint in Workato and connect SAP to it.

Refer to the [SAP troubleshooting guide](/en/connectors/sap/sap-troubleshooting) if you have trouble connecting to Workato with RFCs.

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
