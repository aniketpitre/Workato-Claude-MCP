---
url: 'https://docs.workato.com/en/api-mgmt/configure-recipe-endpoint.md'
description: >-
  Configure a new API recipe endpoint in an API recipe collection so clients can
  call your recipe through the Workato API platform.
---

# Configure a new API recipe endpoint

Complete the following steps to configure a new API recipe endpoint:

- [Prerequisites](#recipe-prerequisites)
- [Step 1: Create the recipe endpoint](#step-1-create-the-endpoint)
- [Step 2: View the recipe endpoint](#step-2-view-the-endpoint)

## Prerequisites

Before you create a new API recipe endpoint, ensure that you complete the following prerequisites:

- [Create an API recipe](/en/api-mgmt/api-recipes/)
- [Create an API recipe collection](/en/api-mgmt/api-collections#create-api-recipe-collection)
- Review the [endpoint path guidelines](/en/api-mgmt/api-endpoints#endpoint-path-guidelines)

  

> **ORGANIZE API RECIPES AND ENDPOINTS**
> 
> We recommend that you organize API recipes with related endpoints in the same API collection and folder within your workspace. For example, group Salesforce endpoints used by sales team recipes into one API collection.
> 
> Learn more about API [endpoint URLs](/en/api-mgmt/api-prefix#understanding-the-endpoint).

## Create the recipe endpoint

Complete the following steps to create a recipe-based endpoint:

1. Go to **Platform > API platform > API collections** and select the API recipe collection for which you plan to create the new endpoint.
   
2. Select **\+ New endpoint**.
   
   ![Select new endpoint](/assets/select-new-recipe-endpoint.C9HHmOFk.png)_Select **\+ New endpoint**_
   
3. Fill in the following fields:
   
   - Recipe
     
   - Select the API recipe to associate with this endpoint. The drop-down menu contains the API recipes you can access.
     
   - HTTP method
     
   - Select the HTTP method to use for the endpoint.
     
   - Endpoint name
     
   - Enter a descriptive name for the endpoint.
     
   - Endpoint path
     
   - Enter the endpoint path, which can include [path parameters](/en/api-mgmt/api-endpoints#path-templating). Ensure the endpoint path follows the [endpoint path guidelines](/en/api-mgmt/api-endpoints#endpoint-path-guidelines).
     
   - Endpoint description
     
   - Enter a description for the endpoint.
     
   - Request timeout
     
   - Enter the request timeout duration: 30 seconds (default), 240 seconds (maximum).
     
   - Schema validation
     
   - Optional. Enable [schema validation](#schema-validation).
     
   - Cache response
     
   - Click the **Cache response** toggle to enable caching. This option is available only for GET methods.
     
     - Time-to-live period
       
     - Required. Enter the duration in seconds for storing a response in the cache before it refreshes or deletes. The default value is 600 seconds and the maximum value is 3600 seconds.
       
     - Cache key parameters
       
     - Optional. Define additional parameters to include in the cache key if required. The cache key always starts with the endpoint URL. For more information, see [API endpoint caching](/en/api-mgmt/api-caching).
       
   
   ![Add a recipe-based endpoint](/assets/add-new-recipe-endpoint.CsWrjO_7.png)_Add a recipe-based endpoint_
   
4. Select **Add endpoint**. The new recipe endpoint appears on the API collection page.
   
5. Click **•••** (ellipsis) next to the endpoint to rename, activate, or delete it.
   

### Schema validation

Schema validation operates at the endpoint level, allowing you to enforce validation for API recipe endpoints. It helps ensure data integrity by requiring that incoming API requests conform to predefined data formats and constraints. By validating required fields and field types, you can prevent invalid or empty requests, which enhances security, data accuracy, and system reliability.

#### Enforced schema rules

Schema validation applies the following checks to each request on a per-endpoint basis:

- **Field presence**: Ensures that all required fields are included. If a required field is missing, the request is rejected.
- **Field types**: Confirms that each field matches the specified data type. If a field has an incorrect data type, the request is rejected.

If a request fails validation, the server responds with a `400 Bad Request` error, which provides details about the error.

> **PAYLOAD SIZE QUOTA**
> 
> Schema validation applies only to requests with a payload size of up to **1MB**.

#### Enable schema validation

Complete the following steps to enable schema validation for an API recipe endpoint:

1. Go to **Platform > API platform > API collections**.
   
2. Select an API collection.
   
3. Select an API recipe endpoint.
   
4. Open the **Settings** tab for the endpoint.
   
5. Enable the **Schema validation** toggle.
   

## View the recipe endpoint

Select an API endpoint from the API collection overview to access detailed information about it. You can also download this information in the [OpenAPI 2.0 specification](/en/api-mgmt/api-collections#openapi) from the collection overview.

A **recipe-based endpoint** includes the following tabs:

**Details tab**

The **Details** tab provides an overview of the request and response settings defined in the associated API recipe.

![Add a recipe-based endpoint](/assets/view-api-recipe.eTAZx3YU.png)_View API recipe_

When you create a new recipe-based endpoint, Workato automatically includes the following in the recipe:

- A [New API request](/en/api-mgmt/api-recipes/trigger-new-api-request) trigger to define the incoming request.
- A [Response to API request](/en/api-mgmt/api-recipes/action-response-to-api-request) action to define the response sent back to the client.

To modify the endpoint's behavior, click **View recipe** to edit the API recipe directly in the recipe editor.

> **API RECIPE CHANGES**
> 
> Any change you make to the associated API recipe automatically applies to the endpoint. This ensures that the endpoint behavior stays in sync with your recipe logic.

**Test request tab**

The **Test request** tab displays parameters and responses and allows you to test the endpoint.

Refer to the [Test a recipe endpoint](/en/api-mgmt/testing-endpoints#test-recipe-endpoint) section for detailed steps on sending test requests and verifying responses for your new recipe endpoint.

**Settings tab**

The **Settings** tab allows you to update recipe endpoint details. For example, you can adjust the request timeout for specific API requirements or rename an endpoint for better organization.

![View a recipe-based endpoint's settings tab](/assets/api-view-recipe-endpoint-setting.Du0JqRvp.png)_View a recipe-based endpoint's **Settings** tab_

The **Settings** tab includes the following fields:

- Recipe
  
- Select the API recipe to associate with this endpoint. The drop-down menu contains the API recipes you can access.
  
- HTTP method
  
- Select the HTTP method to use for the endpoint.
  
- Endpoint name
  
- Enter a descriptive name for the endpoint.
  
- Endpoint path
  
- Enter the endpoint path, which can include [path parameters](/en/api-mgmt/api-endpoints#path-templating). Ensure the endpoint path follows the [endpoint path guidelines](/en/api-mgmt/api-endpoints#endpoint-path-guidelines).
  
- Endpoint description
  
- Enter a description for the endpoint.
  
- Request timeout
  
- Enter the request timeout duration: 30 seconds (default), 240 seconds (maximum).
  
- Schema validation
  
- Optional. Enable [schema validation](#schema-validation).
  
- Cache response
  
- Click the **Cache response** toggle to enable caching. This option is available only for GET methods.
  
  - Time-to-live period
    
  - Required. Enter the duration in seconds for storing a response in the cache before it refreshes or deletes. The default value is 600 seconds and the maximum value is 3600 seconds.
    
  - Cache key parameters
    
  - Optional. Define additional parameters to include in the cache key if required. The cache key always starts with the endpoint URL. For more information, see [API endpoint caching](/en/api-mgmt/api-caching).
    

You can make changes directly in this tab and click **Save** to apply them.

---
