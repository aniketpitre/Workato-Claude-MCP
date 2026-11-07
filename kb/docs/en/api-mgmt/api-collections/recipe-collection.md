---
url: 'https://docs.workato.com/en/api-mgmt/api-collections/recipe-collection.md'
description: >-
  Create an API recipe collection in Workato to expose business logic through
  secure, customizable endpoints powered by individual API recipes.
---

# API recipe collection

An API recipe collection is a set of endpoints, each powered by a single [API recipe](/en/api-mgmt/api-recipes/). Each API recipe maps to one endpoint.

You can use recipe collections to expose business logic through secure, customizable API endpoints. These endpoints are available to internal users, such as teammates, and external users, such as customers or third-party systems, even if they don't have Workato accounts.

You can also use API recipe collections to allow other recipes in your workspace to call endpoints and share logic. Group related API recipe endpoints into a collection to manage access and control more effectively.

> **COLLECTION TYPES**
> 
> Refer to [Collection types](/en/api-mgmt/api-collections#collection-types) to determine whether an API proxy collection, API recipe collection, SOAP API recipe collection, or AI gateway collection fits your use case.

## Prerequisites

Complete the following before you create an API recipe collection:

- [Create a project](/en/projects#create-a-project-and-folder) or select an existing one.
- Create a folder in the project and add one or more [API recipes](/en/api-mgmt/api-recipes/). New API recipes you add to this folder are included in the collection automatically. We recommend that you group related API recipes together.

## Create an API recipe collection

Complete the following steps to create an API recipe collection:

1. Sign in to your Workato account.
   
2. Go to **Platform > API platform > API collections**.
   
3. Select **\+ Create new collection**.
   
4. Use the **Choose collection type** drop-down menu to select **API recipe collection**.
   
   ![Select API recipe collection](/assets/api-recipe-collection-choose-type.o15cDWmr.png)_Select API recipe collection_
   
5. Use the **Choose a configuration type** drop-down menu to specify the configuration you plan to use for your recipe collection:
   
   - **Use existing recipes**: Select a **Recipe folder**. Workato creates one endpoint for each API recipe in the folder.
     
   - **Import OpenAPI Specification**: Upload a JSON or UTF-8 encoded YAML [OpenAPI 3.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md) file, or enter its URL. Enclose time values in quotes. For example, use `"2024-07-18T10:00:00Z"` instead of `2024-07-18T10:00:00Z`.
     
6. Go to **Customize endpoints** and select the checkbox for each endpoint you plan to add to the collection.
   
7. Optional. Select **Edit details** next to an endpoint to configure its settings:
   
   1. Select the **HTTP method** for the endpoint.
      
      ![Customize API recipe collection endpoints](/assets/api-recipe-collection-customize-endpoints.DRnbutMI.png)_Customize API recipe collection endpoints_
      
   2. Enter an **Endpoint name**.
      
   3. Define the **Endpoint path**. It can include [path parameters](/en/api-mgmt/api-endpoints#path-templating). Ensure that you follow the [endpoint path guidelines](/en/api-mgmt/api-endpoints#endpoint-path-guidelines).
      
   4. Enter an **Endpoint description**.
      
   5. Required when you toggle **Customize timeout**. Customize the time that a request is given to complete in the **Request timeout** field. The default value is 30 seconds and the maximum value is 240 seconds.
      
   6. Enable **Schema validation** to validate all requests made to this endpoint.
      
   7. Enforce additional authorization logic using formulas in the **Request authorization** field.
      
   8. Required when you toggle **Cache response**. Use seconds to specify how long to store a response in cache before it's refreshed or deleted in the **Time-to-live period** field. The maximum is 3600 seconds.
      
8. Go to **Set collection details** and configure the following:
   
   1. Enter a **Collection name** for the API collection.
      
   2. Enter a **Version**. Use a unique identifier between 1–10 characters. Collections with the same name but different versions are treated as distinct.
      
   3. Enter a **Description** for the API collection.
      
9. Select **Create collection**. Workato adds the collection and displays the number of endpoints created.
   
   ![Create API recipe collection](/assets/api-recipe-collection-create.DHjUEV4V.png)_Create API recipe collection_
   
10. Select **View API collection**.
    
11. Toggle the **Inactive** button activate the endpoints you plan to use.
    
    > **NEW ENDPOINTS INACTIVE BY DEFAULT**
    > 
    > All new endpoints are inactive by default. You must activate each one before other recipes or apps can call it.
    
    ![Activate API endpoint in a collection](/assets/api-collection-activate-endpoint.Cqgx2E9m.png)_Activate API endpoint in a collection_
    
    Refer to [Activating or deactivating an endpoint](/en/api-mgmt/api-endpoints#activating-or-deactivating-an-endpoint) for more information about activating endpoints.
    
12. Assign the collection to a client's API key to enable access for specific users or apps. [Learn how to create a new API key.](/en/api-mgmt/api-client-mgmt#create-a-new-application)

---

---
url: >-
  https://docs.workato.com/en/api-mgmt/api-collections/soap-api-recipe-collection.md
description: >-
  Create a SOAP API recipe collection in Workato to expose SOAP 1.1 or 1.2
  endpoints generated from a WSDL definition for legacy systems.
---

# SOAP API recipe collection

A SOAP API recipe collection exposes SOAP 1.1 or 1.2 service endpoints through Workato's API platform. Each operation in the collection maps to one API recipe, automatically generated from a Web Services Description Language (WSDL) definition.

You can use SOAP API recipe collections to support legacy enterprise systems that require XML/SOAP protocols. This enables you to modernize platforms that can't migrate to REST.

> **WSDL FILE REQUIRED**
> 
> You must create SOAP API recipe collections from a WSDL file. You can't build SOAP API recipes from scratch in the recipe editor.

## Prerequisites

Ensure the following before you create a SOAP API recipe collection:

- You created or selected a project in your workspace.
- You have a valid WSDL file that meets the following requirements:
  - The file is self-contained.
  - It doesn't use `wsdl:import`, `xsd:import`, or `xsd:include` to reference external files.

## Create a SOAP API collection

Complete the following steps to create a SOAP API collection:

1. Sign in to your Workato account.
   
2. Go to **Platform > API platform > API collections**.
   
3. Click **\+ Create new collection**.
   
4. Select **API recipe collection** as the collection type.
   
   ![Select API recipe collection](/assets/api-recipe-collection-choose-type-soap.BfUnowev.png)_Select API recipe collection_
   
5. Use the **API type** drop-down menu to select **SOAP API**.
   
6. Click **Next**.
   
7. Use the **Location** drop-down menu to select the project where you plan to store the generated recipes. Workato creates one recipe per WSDL operation in this location.
   
8. Drag and drop your `.wsdl` file into the **WSDL file** upload area, or click **upload from device** to browse for the file.
   
   ![Select WSDL file](/assets/select-wsdl-file.BKH-Ufz8.png)_Select WSDL file_
   
9. Click **Next**. Workato uploads and validates the WSDL file. A success message confirms the upload completed.
   
   > **UPLOAD FAILED**
   > 
   > If the upload fails, click **Go back** to return to the previous step and re-upload your file or try a different file.
   > 
   > Ensure your WSDL file meets the requirements in the [Prerequisites](#prerequisites) section.
   
10. Click **Next**.
    
11. Review the list of operations generated from your WSDL. Workato imports all operations and creates one recipe per operation.
    
    > **SCHEMA VALIDATION**
    > 
    > All requests made to this endpoint are validated against the defined schema by default.
    
12. Optional. Expand **Edit details** for an operation to configure the following fields:
    
    1. Enter a human-readable name in the **Operation label** field. This defaults to the operation name.
       
    2. Verify the **Request Name** value. This is the unique identifier the SOAP service uses to route requests to this operation.
       
    3. Enter a short summary in the **Operation description** field.
       
    4. Set the **Request timeout** value. The default value is `30` seconds and the maximum value is `240` seconds.
       
    5. Click **Next**.
       
13. Enter a descriptive name in the **Collection name** field. For example, `Weather SOAP API`.
    
14. Enter a version number in the **Version** field.
    
15. Enter a short summary in the **Description** field.
    
16. Click **Create collection**. Workato stores the WSDL as a resource and generates one recipe per operation.
    
17. Click **View API collection** to manage access or activate endpoints.
    

## Manage a SOAP API collection

After you create a SOAP API collection, you can manage operations, configure client access, and download the WSDL from the collection overview page.

Go to **Platform > API platform > API collections** and select your SOAP API collection to open the overview page.

The overview page contains the following tabs:

- **Operations**: View and manage the operations in the collection. Each operation displays its name, SOAP action, description, and activation status.
- **Clients**: Manage which clients have access to the collection.
- **Settings**: Configure collection-level settings such as the collection path and version.

The right sidebar displays the collection type, service URL, clients with access, and creation date. The service URL is auto-generated per environment.

![SOAP API collection overview](/assets/soap-collection-overview.jrpHec5A.png)_SOAP API collection overview_

### Download the WSDL

Click **Download WSDL** in the upper-right corner of the collection overview page to export the WSDL file. This reflects the current state of the collection.

Workato doesn't edit the WSDL, but generates a new endpoint URL and preserves all mappings and namespaces without modification.

You can also download the WSDL from the resource detail page in your project's **Assets** tab. Refer to [WSDL asset management](#wsdl-asset-management) for more information.

Workato doesn't edit the WSDL and generates

### View operation details

Select an operation from the **Operations** tab to open its **Details** page. The detail page shows the auto-generated recipe with a **New SOAP API request** trigger and a **RETURN** action, along with a sidebar that displays the SOAP action, endpoint type, description, request timeout, and activation status.

### Update operation details

You can update the label, description, SOAP action, request timeout, and other details for each operation.

Complete the following steps to edit an operation:

1. Go to **Platform > API platform > API collections** and select your SOAP API collection.
   
2. Select an operation from the list.
   
3. Go to the **Settings** tab and update the operation fields as needed.
   
4. Click **Save** to apply your changes.
   

### WSDL asset management

Workato stores the WSDL file as a resource in the selected project folder when you upload it during collection creation. You can view and manage this resource in your project's **Assets** tab.

The WSDL resource enables Workato to:

- Generate API recipes and operation schemas automatically from WSDL operations
- Validate incoming XML payloads against the defined schema
- Track version history and manage dependencies between the WSDL and its linked recipes

You can click **Download** on the resource detail page to export the current WSDL file.

> **USE CAUTION**
> 
> You can't edit WSDL files or collection configuration after upload. You can upload a new version of the WSDL, but the changes don't apply to the existing API collection or its generated recipes. Ensure your WSDL contains all required operations and specifications before uploading. After the collection is created, you can only modify the recipe logic directly.

---
