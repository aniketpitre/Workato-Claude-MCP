---
url: 'https://docs.workato.com/en/api-mgmt/api-collections/proxy-collection.md'
description: >-
  Create an API proxy collection in Workato to forward requests to your existing
  API backend with monitoring, access control, and authentication.
---

# API proxy collections

An API proxy collection forwards incoming requests to your existing API backend. Each proxy endpoint acts as a secure intermediary between the client and your API server.

You can use proxy collections to perform the following:

- Add monitoring and access control to existing APIs
- Secure internal APIs with proxy authentication
- Minimize latency for high-volume traffic

> **COLLECTION TYPES**
> 
> Refer to [Collection types](/en/api-mgmt/api-collections#collection-types) to determine whether an API proxy collection, API recipe collection, SOAP API recipe collection, or AI gateway collection fits your use case.

## Prerequisites

Complete the following setup before creating an API proxy collection:

- [Create a project](/en/projects#create-a-project-and-folder) or select an existing project.
- Create an [HTTP connection](/en/developing-connectors/http-v2) to forward requests.

### Create an API proxy collection

Complete the following steps to create an API proxy collection:

1. Sign in to your Workato account.
   
2. Go to **Platform > API platform > API collections**.
   
3. Select **\+ Create new collection**.
   
4. Go to the **Which type of collection would you like to create?** field and select **API proxy collection**.
   
   ![Select API proxy collection](/assets/api-proxy-collection-choose-type.znqbJC4K.png)_Select API proxy collection_
   
5. Select the gateway that hosts the collection in the **API gateway** field. This field appears only after you set up an [Edge Gateway](/en/api-mgmt/api-edge-gateway). Choose **Workato cloud gateway** for managed hosting, or select an edge gateway to process requests on-prem.
   
6. Use **Choose a target HTTP connection** to select an existing HTTP connection from the list or refer to [Create an HTTP connection](/en/developing-connectors/http/connection-setup) to create a new one. You can select **Details** to view a connection's configuration.
   
   ![Choose HTTP connection to forward requests to](/assets/api-proxy-collection-choose-connection.hMdN7gu1.png)_Choose HTTP connection to forward requests to_
   
   > **SUPPORTED AUTHENTICATION TYPES**
   > 
   > API proxy collections support the following HTTP connection authentication types:
   > 
   > - No auth
   > - Query
   > - Basic
   > - Header
   > - OAuth 2.0 (Client credentials grant)
   > - AWS IAM role auth
   > - AWS access key auth
   > 
   > Workato displays an **Unsupported authentication type** error message if you select an unsupported auth type.
   > 
   > Use **AWS IAM role auth** or **AWS access key auth** when your proxy forwards requests to AWS services such as DynamoDB or S3.
   
7. **Choose a configuration type** to specify the configuration you plan to use in your proxy collection:
   
   - **Import OpenAPI Specification**: Upload a JSON or UTF-8 encoded YAML [OpenAPI 3.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md) file, or enter its URL. Workato uses this specification to generate endpoint schemas automatically. Time values must be enclosed in quotes. For example, use `"2024-07-18T10:00:00Z"` instead of `2024-07-18T10:00:00Z`.
     
   - **Manual configuration**: Workato creates an empty collection to which you can add endpoints later. Refer to [Configure the schema](/en/api-mgmt/configure-proxy-endpoint#step-3-set-up-schema) for details.
     
8. > **OPENAPI ONLY**
   > 
   > This step applies **only if you imported an OpenAPI specification** during setup.
   
   Go to **Customize endpoints** and select the checkbox next to each endpoint you plan to add to the collection.
   
9. Optional. Select **Edit details** next to an endpoint to configure its settings:
   
   1. Enter an **Endpoint name**.
      
      ![Customize API proxy collection endpoints](/assets/api-proxy-collection-customize-endpoints.Dujsv4QE.png)_Customize API proxy collection endpoints_
      
   2. Define a path for the endpoint in the **Endpoint path** field. You can include [path parameters](/en/api-mgmt/api-endpoints#path-templating). Ensure that you follow the [endpoint path guidelines](/en/api-mgmt/api-endpoints#endpoint-path-guidelines).
      
   3. Select the **HTTP method** to use for the endpoint.
      
   4. Required when you toggle **Customize timeout**. Customize the time that a request is given to complete in the **Request timeout** field. The default value is 30 seconds and the maximum value is 240 seconds.
      
10. Click **Next** to go to the **Set collection details** page and enter the following:
    
    1. Enter a **Collection name** for the API collection.
       
       ![Set collection details](/assets/set-collection-details.DuT_hOzV.png)_Set collection details_
       
    2. Enter a **Version**. Use a unique identifier between 1–10 characters. Collections with the same name but different versions are treated as separate objects.
       
    3. Enter a **Description** for the API collection.
       
11. Select **Create collection**. Workato creates the collection and shows the number of endpoints added.
    
12. Select **View API collection**.
    
13. Toggle the **Inactive** button to activate the endpoints you plan to use in your new collection.
    
    > **NEW ENDPOINTS INACTIVE BY DEFAULT**
    > 
    > All new endpoints are inactive by default. You must activate an endpoint before recipes or apps can call it.
    
    ![Activate API proxy endpoint in a collection](/assets/api-proxy-collection-activate-endpoint.Bn3od9fk.png)_Activate API proxy endpoint in a collection_
    
    Refer to [Activating or deactivating an endpoint](/en/api-mgmt/api-endpoints#activating-or-deactivating-an-endpoint) for more information about activating endpoints.
    
14. Assign this collection to a client's API key to grant access to specific users or apps. [Learn how to create a new API key.](/en/api-mgmt/api-client-mgmt#create-a-new-application)
    

You can configure this collection to accept unauthenticated requests so that any caller can reach its endpoints without credentials. This is useful for serving public endpoints such as OIDC discovery documents. Refer to [Unauthenticated API collections](/en/api-mgmt/unauthenticated-collections) for more information.

---
