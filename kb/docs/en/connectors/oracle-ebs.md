---
url: 'https://docs.workato.com/en/connectors/oracle-ebs.md'
description: >-
  Connect to Oracle E-Business Suite to manage enterprise resources, automate
  business processes, and integrate ERP, CRM, and supply chain operations.
---

# Oracle E-Business Suite

[Oracle E-Business Suite](http://www.oracle.com/us/products/applications/ebusiness/overview/index.html) (also known as Applications/Apps or EB-Suite/EBS) is a collection of enterprise resource planning (ERP), customer relationship management (CRM), and supply chain management (SCM) applications that enables organizations of any size to operate and perform effectively.

The Oracle E-Business Suite connector enables integration with cloud applications through Oracle's Business Event System for real-time event-driven automation and direct data operations for retrieving and updating records.

## Business value

The Oracle E-Business Suite connector addresses critical enterprise integration challenges by:

- **Modernizing legacy systems**: Bridge Oracle E-Business Suite with modern cloud applications.
- **Automating workflows**: Eliminate manual data entry and reduce processing time.
- **Ensuring data consistency**: Maintain synchronized data across enterprise systems.
- **Enabling real-time operations**: React to business events as they occur with real-time workflow triggers.
- **Supporting digital transformation**: Facilitate migration to cloud-first architectures.
- **Extending platform capabilities**: Build and consume SQL procedures exposed as REST APIs.

## Use cases

Key use cases of the Oracle E-Business Suite connector include:

- **Order processing**: Synchronize orders between Oracle E-Business Suite, [Salesforce](/en/connectors/salesforce), and logistics providers for streamlined fulfillment workflows.
- **Financial reporting**: Automate financial data extraction to data warehouses like [Snowflake](/en/connectors/snowflake) for advanced analytics and reporting.
- **Inventory management**: Synchronize inventory data across e-commerce platforms like [Shopify](/en/connectors/shopify) and warehouse management systems.
- **HR automation**: Integrate with modern HR platforms like [Workday](/en/connectors/workday) or [SAP SuccessFactors](/en/connectors/successfactors/successfactors) for unified employee lifecycle management.

## Prerequisites

Ensure you have the following before connecting to Oracle E-Business Suite:

- Admin access to your Oracle EBS instance for deploying REST services
- The [Oracle E-Business Suite Integrated SOA Gateway](https://docs.oracle.com/cd/E26401_01/doc.122/e20925/T511175T578675.htm) installed
- [Enabled and deployed the following services as REST APIs](https://docs.oracle.com/cd/E18727_01/doc.121/e12169/T682519T513044.htm#isgig_restdeploy) in the Integrated SOA Gateway:
  - **Metadata Provider** (internal name: `oracle.apps.fnd.rep.ws.service.EbsMetadataProvider`)
  - **Event Manager** (internal name: `oracle.apps.fnd.wf.bes.EventManager`)
  - Any other interface definitions you plan to use in your recipes, also exposed as REST APIs in the Integrated SOA Gateway
- (For on-prem connections) The [Workato on-prem agent](https://www.workato.com/on_prem_groups) installed

## How to connect to Oracle E-Business Suite

Complete the following steps to establish an Oracle E-Business Suite connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Oracle E-Business Suite` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Oracle recipe](/assets/connect.CA53ZLWk.png)_Set up your Oracle E-Business Suite connection_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Use the **Connection type** drop-down menu to specify whether this is a cloud or on-prem connection. If you're connecting to an on-premise Oracle E-Business Suite instance, select the appropriate on-prem group from the drop-down menu.
   
6. Enter the base URL for your Oracle SOA Gateway REST services in the **Instance URL** field. For example, `https://oracleebs.mycompany.com:8000/`.
   
7. Enter your Oracle SOA Gateway REST services username in the **Username** field.
   
8. Enter your password in the **Password** field.
   
9. Click **Connect**.

---
