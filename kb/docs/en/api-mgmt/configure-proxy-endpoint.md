---
url: 'https://docs.workato.com/en/api-mgmt/configure-proxy-endpoint.md'
description: >-
  Configure a new API proxy endpoint to forward requests to an external API,
  including creating, viewing, and setting up the schema.
---

# Configure a new API proxy endpoint

Complete the following steps to configure a new API proxy endpoint:

- [Prerequisites](#proxy-prerequisites)
- [Step 1: Create the endpoint](#step-1-create-the-proxy-endpoint)
- [Step 2: View the proxy endpoint](#step-2-view-proxy-endpoint)
- [Step 3: Configure the schema](#step-3-set-up-schema)

## Prerequisites

Before creating a new API proxy endpoint, ensure that you complete the following prerequisites:

- [Create an HTTP connection](/en/developing-connectors/http-v2) to enable Workato to forward requests to the external API.
- [Create an API proxy collection](/en/api-mgmt/api-collections#create-api-proxy-collection) to organize related endpoints.
- Review the [endpoint path guidelines](/en/api-mgmt/api-endpoints#endpoint-path-guidelines) to ensure consistent and valid path configurations.

## Create the endpoint

Complete the following steps to create a proxy endpoint:

1. Go to **Platform > API platform > API collections** and select the API proxy collection for which you plan to create the new endpoint.
   
2. Select **\+ New endpoint**.
   
   ![Select new endpoint](/assets/add-new-proxy-endpoint.5jSj6C8e.png)_Select **\+ New endpoint**_
   
3. Fill in the following fields:
   
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
     
   - Keep base URL
     
   - Toggle whether to forward requests directly to the connection's base URL without appending the endpoint path.
     
   - Cache response
     
   - Click the **Cache response** toggle to enable caching. This option is available only for GET methods.
     
     - Time-to-live period
       
     - Required. Enter the duration in seconds for storing a response in the cache before it refreshes or deletes. The default value is 600 seconds and the maximum value is 3600 seconds.
       
     - Cache key parameters
       
     - Optional. Define additional parameters to include in the cache key if required. The cache key starts with the endpoint URL. For more information, see [API endpoint caching](/en/api-mgmt/api-caching).
       
4. Select **Add endpoint**. The new proxy endpoint appears on the API collection page.
   
5. Click **•••** (ellipsis) next to the endpoint to rename, activate, or delete it.
   

## View the proxy endpoint

Select an API endpoint in the API collection overview to view its details. You can also download these details in the [OpenAPI 2.0 specification](/en/api-mgmt/api-collections#openapi) from the API collection overview.

A **proxy-based endpoint** includes the following tabs:

**Details tab**

The **Details** tab summarizes settings from the following components in the proxy workflow:

![View a proxy-based endpoint's Details tab](/assets/api-view-proxy-endpoint-details.DF2Ldxds.png)_View a proxy-based endpoint's **Details** tab_

- New API proxy request trigger
  
- Defines the schema for incoming requests, including the content type, query parameters, body, headers, and the expected response schema.
  
- Forward request to target action
  
- By default, all proxy endpoints forward requests to the target API. If needed, you can [transform incoming request data](/en/api-mgmt/api-proxy-transformation#transform-proxy-requests), such as headers, query parameters, and the request body, before forwarding it to the target API endpoint. Refer to the [API proxy transformation](/en/api-mgmt/api-proxy-transformation) guide to learn how to transform requests.
  
- Return response action
  
- Configures the response sent to the client, including the content type, headers, HTTP status codes, and body. You can also [transform the response](/en/api-mgmt/api-proxy-transformation#transform-target-responses) by modifying its data before sending it to the client.
  

If you created an endpoint manually or chose **Manual configuration** when creating the collection, you must configure the schema and headers. For more information, refer to [Configure the schema](#step-3-set-up-schema).

If you imported an OpenAPI specification when you created the collection, the schema and headers for each endpoint are preconfigured.

The **Target URL** section displays the address that requests to the proxy endpoint are forwarded to. You can modify the target URL by modifying the associated HTTP connection in the API proxy collection settings.

**Test request tab**

The **Test request** tab enables you to [test the proxy endpoint](/en/api-mgmt/testing-endpoints#test-proxy-endpoint) by sending sample requests and reviewing responses.

![View a proxy-based endpoint's Test tab](/assets/api-view-proxy-endpoint-test.DX4EcVBV.png)_View a proxy-based endpoint's **Test** tab_

This tab includes the following sections:

- Parameters
  
- Lists the required query parameters, headers, and request body for the endpoint.
  
- Responses
  
- Displays the expected HTTP status codes and response schema for the client.
  

**Settings tab**

The **Settings** tab allows you to update proxy endpoint details. For example, you can adjust the request timeout for specific API requirements or rename an endpoint for better organization.

![View a proxy-based endpoint's settings tab](/assets/api-view-proxy-endpoint-setting.COx1uZNl.png)_View a proxy-based endpoint's **Settings** tab_

The **Settings** tab includes the following fields:

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
  
- Keep base URL
  
- Toggle whether to forward requests directly to the connection's base URL without appending the endpoint path.
  
- Cache response
  
- Click the **Cache response** toggle to enable caching. This option is available only for GET methods.
  
  - Time-to-live period
    
  - Required. Enter the duration in seconds for storing a response in the cache before it refreshes or deletes. The default value is 600 seconds and the maximum value is 3600 seconds.
    
  - Cache key parameters
    
  - Optional. Define additional parameters to include in the cache key if required. The cache key starts with the endpoint URL. For more information, see [API endpoint caching](/en/api-mgmt/api-caching).
    

You can make changes directly in this tab and click **Save** to apply them.

## Configure the schema

If you created an endpoint manually or selected **Manual configuration** when setting up the API proxy collection, configure the schema and headers in the **New API proxy request** trigger.

Complete the following steps to configure the schema:

1. Open the **New API proxy request** trigger from your proxy workflow.
   
2. Expand the **Request** section and configure the following fields:
   
   - Request body
     
   - Define the schema for the body of incoming requests. This applies to HTTP methods like POST, PUT, or PATCH. You can either paste a sample JSON payload or add fields manually.
     
   - Request query parameters
     
   - Describe one or more request query parameters.
     
   - Request headers
     
   - Add any required headers to the request.
     
3. Expand the **Response schema** section and configure the following fields:
   
   - Response content type
     
   - **Required.** Specify the format of the response, such as JSON or XML.
     
   - Response headers
     
   - Specify any headers that you plan to include in the HTTP response.
     
   - Responses
     
   - **Required.** Specify at least one **HTTP status code**, such as `200 - OK`, and describe the expected response body schema. Click **Use JSON** to paste or upload example JSON output, or manually define fields in the response body.
     
4. Click **Save** to apply your changes.
   

Your schema configuration is complete. To learn how to test your new proxy endpoint, see [Test a proxy endpoint](/en/api-mgmt/testing-endpoints#test-proxy-endpoint).

> **IMPORT OPENAPI SPEC FOR AUTOMATIC SETUP**
> 
> To automatically configure the endpoint schema, select **Import OpenAPI specification** when [creating a new API proxy collection](/en/api-mgmt/api-collections#create-api-proxy-collection). Workato will populate the schema for each endpoint in the collection.

---
