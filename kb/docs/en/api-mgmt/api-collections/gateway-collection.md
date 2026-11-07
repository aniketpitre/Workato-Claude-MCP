---
url: 'https://docs.workato.com/en/api-mgmt/api-collections/gateway-collection.md'
description: >-
  Create an AI gateway collection in Workato to expose endpoints to LLMs, GPTs,
  and AI applications for secure, authorized actions.
---

# AI gateway collection

An AI gateway collection exposes endpoints to LLMs, GPTs, or other AI applications. This setup enables AI agents to take actions on your behalf using secure, authorized requests. Refer to [AI gateway](/en/api-mgmt/ai-gateway) for more information.

> **COLLECTION TYPES**
> 
> Refer to [Collection types](/en/api-mgmt/api-collections#collection-types) to determine whether an API proxy collection, API recipe collection, SOAP API recipe collection, or AI gateway collection fits your use case.

## Prerequisites

Complete the following before you create an AI gateway collection:

- [Create a project](/en/projects#create-a-project-and-folder) or select an existing project.

## Create an AI gateway collection

Complete the following steps to create an AI gateway collection:

1. Sign in to your Workato account.
   
2. Go to **Platform > API platform > API collections**.
   
3. Click **\+ Create new collection**.
   
4. Use the **What type of collection would you like to create?** drop-down menu to select **AI gateway collection**.
   
   ![Select AI gateway collection](/assets/select-ai-gateway-collection.o9IjvMCH.png)_Select AI gateway collection_
   
5. Use the **Select AI model provider** drop-down menu to select an AI provider. This setting optimizes your OpenAPI specification and prompt formats for the selected provider.
   
6. Use the **Choose a configuration type** drop-down menu to specify the configuration you plan to use for your recipe collection:
   
   - **Use existing recipes**: Select the **Recipe folder** from the drop-down menu. Workato maps each API recipe in this folder to a new endpoint.
     
   - **Import OpenAPI Specification**: Upload a JSON or YAML [OpenAPI 3.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md) specification file, or enter the URL of the specification.
     
   
   ![Choose configuration type](/assets/choose-gateway-configuration.ByrSKU9P.png)_Choose your configuration type_
   
7. Go to **Customize endpoints** and select the checkbox next to each endpoint you plan to add to the collection.
   
8. Optional. Select **Edit details** next to an endpoint to configure its settings:
   
   1. Select the **HTTP method** to use for the endpoint.
      
      ![Customize AI gateway collection endpoints](/assets/ai-gateway-custom-endpoints.-EqNg9M7.png)_Customize AI gateway collection endpoints_
      
   2. Enter an **Endpoint name**.
      
   3. Define a path for the endpoint in the **Endpoint path** field. This path is appended to both the AI and target base URLs. It can include [path parameters](/en/api-mgmt/api-endpoints#path-templating). Ensure that you follow the [endpoint path guidelines](/en/api-mgmt/api-endpoints#endpoint-path-guidelines).
      
   4. Enter an **Endpoint description**.
      
   5. Required when you toggle **Customize timeout**. Customize the time that a request is given to complete in the **Request timeout** field. The default value is 30 seconds and the maximum value is 240 seconds.
      
   6. Enable **Schema validation** to validate all requests made to this endpoint.
      
   7. Enforce additional authorization logic using formulas using the **Request authorization** field.
      
   8. Enable response caching to improve performance in the **Cache response** field.
      
   9. Required when **Cache response** is enabled. Use seconds to specify how long to store a response in cache before it's refreshed or deleted in the **Time-to-live period** field. The maximum value is 3600 seconds.
      
9. Go to **Set collection details** and enter the following information:
   
   1. Enter a **Collection name** for the AI gateway collection.
      
   2. Enter a **Version**. Use a unique identifier between 1–10 characters. Workato treats collections with the same name but different versions as separate objects.
      
   3. Optional. Enter a **Description** for the AI gateway collection.
      
      ![Set collection details](/assets/collection-details.BP2xvApl.png)_Set collection details_
      
10. Click **Create collection**.
    
11. Select a **Next steps** link or click **View API collection**.
    
    ![View API collection](/assets/new-ai-gateway-collection.BwiaG15r.png)_View API collection_

---
