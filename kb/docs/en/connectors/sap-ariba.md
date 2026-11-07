---
url: 'https://docs.workato.com/en/connectors/sap-ariba.md'
description: >-
  The SAP Ariba connector lets you automate procurement workflows: create,
  update, search, and delete records and get record details by ID.
---

# SAP Ariba

[SAP Ariba](https://www.sap.com/india/products/spend-management/ariba-login.html) is a leading procurement and supply chain management solution. It provides a platform for managing procurement, sourcing, supplier collaboration, and financial supply chain processes, enhancing operational efficiency and transparency. This connector enables seamless integration between SAP Ariba and other applications for automated workflows.

## Prerequisites

Before using the SAP Ariba connector in Workato, ensure you have an active SAP Ariba account with appropriate permissions to access APIs.

### Request API enablement

Complete the following steps to request API enablement as user with developer or organization admin privileges:

1. Sign in to the **SAP Ariba Developer Portal**.
   
2. Click **Manage** from the navigation menu.
   
3. Click **Applications**.
   
4. Search for the application you plan to have enabled.
   
5. Click **Actions > Request API Access**.
   
6. Select the API name in the **API Names** drop-down. This is the API that you plan to access when using this application.
   
7. Enter the realm name in the **Realm Name** field. This is the site for which you plan to have the application enabled.
   
8. Enter the ANID in the **ANID** field.
   
9. Select the radio button corresponding to the **realm type**. Available options include production or test.
   
10. Click **Submit**.
    

### Approve an API enablement request

Complete the following steps to approve the API enablement request. The following steps must be taken by a user with the organization admin privilege:

1. Click **Manage** in the left navigation menu.
   
2. Click **Applications**.
   
3. Search for the application.
   
4. Click **Approve**.
   

> **WAITING PERIOD FOR API ENABLEMENT**
> 
> It can take 12 hours for SAP to enable the API. When ready, the application's Client ID is listed under the **Account Settings > API Management** section within your Ariba account.
> 
> Refer to the [SAP Business Accelerator](https://api.sap.com/products/SAPAriba/apis/all) Hub for the API list and reference documents.

## Connection setup

Establishing a connection to SAP Ariba in Workato consists of the following steps:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `SAP Ariba` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select one or more **Applications** (API) from the drop-down menu.
   
   You can authenticate to multiple APIs in a single connection. This allows you to access resources from different APIs within the same recipe without creating multiple connections.
   
   Refer to the [Available APIs](#available-apis) table to understand the required APIs based on your use case.
   
6. Provide the **Client ID** generated from the SAP Ariba Developer Portal.
   
7. Provide the **Client Secret** generated from the SAP Ariba Developer Portal. This, along with the Client ID, is used to authenticate API requests securely.
   
8. Enter the **API Key** generated from the SAP Ariba Developer Portal. It is required to authorize API calls and link them to your account.
   
9. Enter the unique realm identifier for your SAP Ariba environment in the **x-realm** field. This ensures API requests are routed to the correct instance of your SAP Ariba setup.
   
10. Enter the Ariba Network ID (**ANID**) associated with your organization. This unique identifier is used to establish communication and link your organization within the Ariba Network.
    
11. Optional. If you are authenticating to additional APIs within the same connection, repeat Steps 6-10 with the corresponding credentials for each additional API.
    
12. Click **Connect**.
    
    ![Connection setup](/assets/connection-for-procurement-api.vS4ghC2O.png)_Connect to SAP Ariba in Workato_
    

## Available APIs

The SAP Ariba connector supports multiple APIs. Each API provides access to different objects and operations. You can authenticate to multiple APIs within a single connection when you provide credentials for each one during connection setup.

The following APIs are available:

| API name | Description | Supported operations | Available objects |
| --- | --- | --- | --- |
| Master Data Retrieval API for Procurement | Retrieve and search master data from SAP Ariba Procurement | **Actions:** List objects, Search objects | Entities (Procurement) |
| Master Data Retrieval API for Sourcing | Retrieve and search master data from SAP Ariba Sourcing | **Actions:** List objects, Search objects | Entities (Sourcing) |
| Order Change Requests API for Buyers | Retrieve and search purchase order change requests from a buyer perspective | **Actions:** List objects, Search objects | Change requests (Buyer), Change requests responses (Buyer), Change requests confirmations (Buyer) |
| Order Change Requests API for Suppliers | Retrieve and search purchase order change requests from a supplier perspective | **Actions:** List objects, Search objects | Change requests (Supplier), Change requests responses (Supplier), Change requests confirmations (Supplier) |
| Ariba Network Purchase Orders Buyer API | Retrieve and search purchase order data from a buyer perspective | **Actions:** List objects, Search objects | Orders (Buyer), Items (Buyer) |
| Ariba Network Purchase Orders Supplier API | Retrieve and search purchase order data from a supplier perspective | **Actions:** List objects, Search objects | Orders (Supplier), Items (Supplier) |
| Document Approval API | Search approval data | **Actions:** Search objects | Purchase requisitions, Changes, User groups, Invoices |
| Contract Workspace Retrieval API | Manage, retrieve, and search contract workspace data | **Triggers**: New/updated record **Actions:** Get record details by ID, Search objects | Contract Workspace |
| Contract Workspace Modification API | Create, update, and modify contract workspaces | **Actions:** Create record, Update record, Delete record | Contract Workspace |
| Contract Terms Management API | Retrieve and manage contract terms | **Actions:** Create record, Get record details by ID | Contract terms |
| Project Document Management Creation API | Create project documents | **Actions:** Create record | Project document |
| Event Management API | Create, manage, retrieve, and search events and related data | **Triggers**: New/updated record **Actions:** Create record, Get record details by ID, Search objects | Events, Event item, Event awards, Event supplier invitations |

---
