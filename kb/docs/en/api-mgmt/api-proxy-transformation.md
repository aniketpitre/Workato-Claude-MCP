---
url: 'https://docs.workato.com/en/api-mgmt/api-proxy-transformation.md'
description: >-
  Configure API proxy transformations to modify requests and responses as they
  pass through the Workato gateway, aligning client and target schemas and
  formats.
---

# API proxy transformation

API proxy transformation allows you to modify API proxy requests and responses as they pass through Workato's API gateway. You can transform inbound request data before forwarding it to the target endpoint or transform target responses before returning them to the client. Transformations streamline API consumption, improve data integrity, and enable you to align different schemas and data formats, providing greater control over your API usage.

![API proxy transformation flow](/assets/proxy-transformation.BkGhqt6p.png)_API proxy transformation flow_

## Key concepts

Review the following key concepts before beginning the transformation process:

- Client
  
- The user or application that sends requests to the API proxy endpoint.
  
- Proxy schema
  
- The schema defined within Workato that specifies the structure of requests and responses exchanged between the client and the API proxy. It serves as the client-facing interface for the API.
  
- Target
  
- The backend service that processes API requests forwarded by the API proxy.
  
- Target schema
  
- The schema of the backend service, also referred to as the backend API or external API. This schema defines the structure of the request forwarded to the target and the response returned by the target. Transformations enable compatibility when the proxy schema and target schema differ, aligning inbound request data with the backend service’s requirements and responses with the client’s expectations.
  

## Supported transformation types

API proxy transformation supports the following modifications to requests and responses:

- Schema manipulation
  
- Modify the schema for both proxy or target requests and responses, ensuring proper structure and data flow.
  
- Key-value pair mapping
  
- Create or modify parameters within the request or response, such as masking sensitive data or adding custom headers.
  
- In-line formulas
  
- Use Workato's formula capabilities to manipulate values within the request or response. You can apply static or dynamic values (using datapills) and perform calculations or formatting based on the data.
  
- Conditional response mapping
  
- Apply conditional logic to return different HTTP statuses or responses based on specific conditions.
  
- Request method transformation
  
- Modify the HTTP method between the proxy and the target. For example, transform a GET request at the proxy into a POST request at the target. Method transformation is only available when you select **Transform request** in the **Forward request to target** action.
  

> **OPTIMIZED SUPPORT**
> 
> Optimized support is available only for JSON content types. Use `Plain text` to manage alternative content formats.

## Partially supported transformation types

API proxy transformation partially supports the following modifications to requests and responses:

- Partially supported content types for request and response bodies
- XML is partially supported, which enables you to construct XML bodies using the `text/plain` content type when transforming request or response bodies.

## Unsupported transformation types

While API proxy transformation offers flexibility in modifying requests and responses, the following transformations are not supported:

- Dynamic path transformations
  
- You cannot use dynamic transformations with datapills or formulas for the target URL path. Only static text paths are allowed.
  
- Transforming arrays or objects in query parameters
  
- For `GET` and `DELETE` requests, you can't transform arrays or objects in query parameters. However, you can still use arrays and objects in the request body.
  
- Unsupported content types for request and response bodies
  
- You cannot apply transformations to certain content types in both request and response bodies. These include multipart form data, URL-encoded forms, plain text, or binary data.
  
- Multiple conditional responses
  
- You cannot map multiple response status codes for a single proxy endpoint to different conditions. Handling multiple status-code mappings using conditional logic is not supported.
  

## Formula limitations

Workato allows you to [use formulas to transform requests and responses](#transform-data-with-workato-formulas), offering flexibility to dynamically transform data. While most documented formulas are supported, certain exceptions apply.

If you encounter limitations or require additional formula support, contact your Customer Success Manager (CSM) for assistance.

## Transform proxy requests

Transforming proxy requests allows you to modify inbound request data before forwarding it to the target endpoint. You can configure the HTTP method, endpoint path, query parameters, headers, or request body based on your requirements. Use transformations when the client schema differs from the target schema to reconcile mismatched data formats or structures.

> **PREREQUISITES**
> 
> Before you can apply API proxy transformation, ensure you have the following:
> 
> - **Configured API proxy endpoint**: Verify that your API proxy endpoint is properly set up. For more information, refer to the [API proxy endpoint configuration](/en/api-mgmt/configure-proxy-endpoint) documentation.
> - **Defined client schema**: Configure the request and response format expected by the proxy-facing client. This is typically predefined during the proxy setup.
> - **Defined target schema**: Configure the target request schema and response schema. You can do this by sending a sample request with the guided setup wizard or providing a JSON sample.

Transforming proxy requests involves two key steps:

- **Configuring the target endpoint schema**: Set up the target endpoint request schema to align with the target API’s data format.
- **Applying transformations**: Modify the request using transformation options to match the client schema or adapt to specific target API constraints.

### Configure the target endpoint schema

Before applying transformations, you must define the schema for the target endpoint. This step ensures the proxy endpoint aligns with the target API’s data format. You can define the schema using the [guided setup](#guided-setup) or [manual configuration](#manual-configuration) for full control over the process.

#### Guided setup

The guided setup helps you configure the schema for the target API. This setup automatically generates the request and response schema by sending a sample request to the target API.

> **WHEN TO USE GUIDED SETUP**
> 
> The guided setup simplifies schema definition based on real-time responses from the target API. This ensures compatibility and creates a foundation for transformations.

Complete the following steps to use the guided setup:

1. Go to **Platform > API Platform > API collections**.
   
2. Choose the **API proxy collection** where the endpoint is located.
   
3. Choose the proxy endpoint, then open the **Details** tab.
   
4. Select the endpoint that you plan to modify, then click **Edit endpoint**.
   
5. Click the **Forward request to target** action in your proxy workflow to open the configuration.
   
   ![Configure the Forward request to target action](/assets/forward-request.Bv_1tnpf.png)_Configure the **Forward request to target** action_
   
6. Click **Start guided setup** to open the schema definition wizard. If you prefer not to send a sample request to the target API, click **Skip guided setup** to [manually](#manual-configuration) define schemas.
   
   ![Start guided setup](/assets/start-guided-setup.DXMz2Ffl.png)_Start guided setup_
   
7. Choose the HTTP **Method** for the sample request.
   
8. Define the **Target endpoint path** appended to the target API’s base URL.
   
9. Review the **Target URL preview** to ensure the full target URL is correct.
   
10. Specify the **Request content type**, if applicable. This field is required for methods such as POST, PUT, PATCH, or DELETE, where a payload is sent.
    
11. Configure the **Request body** by either using the JSON template or adding fields manually. This field appears for methods like POST, PUT, or PATCH.
    
12. Define **Request parameters** to send additional data to the target endpoint.
    
13. Add any required **Request headers** to the HTTP request.
    
14. Use the **Response** drop-down menu to define the expected **Response content type**, such as JSON or XML.
    
15. Click **Send request**.
    
16. Review the schema generated from the sample request to ensure it matches the target API’s expected data format. If the request succeeds, Workato displays a `200 - OK` code.
    
    ![Start guided setup](/assets/review-http.Dd_Qfr_7.png)_Review HTTP configuration_
    
17. Click **Apply configuration** to save the schema. This ensures the proxy endpoint aligns with the target API’s data format and is ready for transformations.
    

After you’ve configured the target schema, proceed to [apply proxy request transformations](#apply-proxy-request-transformations) to modify requests based on your requirements.

#### Manual configuration

Manual setup allows you to configure the target endpoint’s schema without sending a sample request to the target API. This approach gives you complete control over request and response definitions, making it ideal for custom configurations or when guided setup is not suitable.

> **WHEN TO USE MANUAL SETUP**
> 
> Use manual setup if you prefer to define schema fields without sending a sample request to the target API.

When configuring proxy requests, determine whether transformations are necessary. For pass-through requests, no transformations or request schema configuration are needed. If transformations are required, fields appear dynamically to allow you to define the target schema and [configure request transformations](#apply-proxy-request-transformations).

Complete the following steps to configure the target endpoint's schema manually:

1. Go to **Platform > API Platform > API collections**.
   
2. Choose the **API proxy collection** containing the endpoint.
   
3. Select the proxy endpoint and open the **Details** tab.
   
4. Choose the endpoint that you plan to configure, then select **Edit endpoint**.
   
5. Click the **Forward request to target** action in your proxy workflow to open the configuration.
   
   ![Configure the Forward request to target action](/assets/forward-request.Bv_1tnpf.png)_Configure the **Forward request to target** action_
   
6. Click the **setup manually** link to access the schema definition editor.
   
   ![Select setup manually](/assets/setup-manually.Poi-joZC.png)_Select setup manually_
   
7. Define the target request schema, such as the **Request body**, **Request parameters**, and **Request headers**.
   
8. Use the **Response schema** drop-down menu to define the response expected from the target API. This configuration forms the basis for [transforming the response](#transform-target-responses) in subsequent steps and includes the **Response content type**, **Response body**, and **Response headers**.
   
9. Click **Save** to finalize the schema.
   

After you’ve configured the target schema, proceed to [apply proxy request transformations](#apply-proxy-request-transformations) to modify requests based on your requirements.

### Apply proxy request transformations

After schema setup, return to the **Forward request to target** action to configure transformations. Use the **What would you like to do?** drop-down menu to determine how the proxy handles requests.

![Choose what to do with the API proxy request](/assets/target-request-choose.rdyAIGju.png)_Choose what to do with the API proxy request_

Based on your specific requirements, choose one of the following options:

**Forward request without transformation**

This is the default option for handling requests. The proxy forwards the request it receives from the client to the target API without any modifications. Use this option when no transformations or changes to the request are required.

![Configure the target response schema](/assets/configure-response-schema.RyuW1q37.png)_Configure the target response schema_

**Transform request**

This option allows you to modify all aspects of the request before it is forwarded to the target endpoint. Use this option if the client and target API have different schemas for the request structure.

1. Select the **Target endpoint method**. By default, it matches the method used at the proxy endpoint. Change this value to transform the HTTP method sent to the target. Workato automatically adjusts the configuration fields such as request body, content type, and query parameters based on the selected method.
   
   ![Transform request](/assets/transform-request.pBeS24K_.png)_Transform request_
   
2. Modify the **Target endpoint path** to append or update a specific path to the target base URL, such as `testing`.
   
3. Review the **Target URL preview** to verify the complete target URL, including the appended path.
   
4. Specify the **Request content type**, if applicable. This field is required for methods such as POST, PUT, PATCH, or DELETE, where a payload is sent.
   
5. Configure the **Request body** by either using the JSON template or adding fields manually. This field appears for methods like POST, PUT, or PATCH.
   
6. Define **Request query parameters** to include additional data in the request forwarded to the target endpoint.
   
7. Add or modify any **Request headers** required by the target endpoint.
   
8. Click **Save** to apply the configuration.
   

After completing these steps, the transformed request is forwarded to the target API.

**Transform headers only**

Use this option if you need to modify request headers without changing the body, query parameters, or endpoint path:

1. Add or modify any **Request headers** required by the target endpoint.
   
   ![Transform request](/assets/transform-headers.c4jbeaka.png)_Transform request headers_
   
2. Click **Save** to apply the configuration.
   

After completing these steps, the proxy endpoint forwards the modified headers to the target API.

**Transform body or parameters only**

Use this option to update the request body or query parameters without altering the endpoint path or headers:

1. Specify the **Request content type**, if applicable. This field is required for methods such as POST, PUT, PATCH, or DELETE, where a payload is sent.
   
2. Configure the **Request body** using either the JSON template or by adding fields manually. This field appears for methods like POST, PUT, or PATCH.
   
   ![Transform request](/assets/transform-request-body.CZ3IMMMm.png)_Transform request body_
   
3. Define **Request query parameters** to include additional data in the request forwarded to the target endpoint.
   
4. Click **Save** to apply the configuration.
   

After completing these steps, the proxy endpoint forwards the transformed body or query parameters to the target API as part of the request.

> **QUERY PARAMETER BEHAVIOR**
> 
> When applying transformations, the proxy forwards only query parameters explicitly configured in the transformation step to the target API. Query parameters not mapped in the transformation step are excluded from the forwarded request. To pass all query parameters from the client request, explicitly map each parameter.

After configuring and saving the request transformations, configure the **Return response** action to [transform the response](#transform-target-responses) before returning it to the client, if needed.

## Transform target responses

Target response transformations allow you to modify the data returned by the target before returning it to the client. You can configure headers, modify the body, or apply conditional logic to customize the response.

> **PREREQUISITES**
> 
> Before you can apply API proxy transformation, ensure you have the following:
> 
> - **Configured API proxy endpoint**: Verify that your API proxy endpoint is properly set up. For more information, refer to the [API proxy endpoint configuration](/en/api-mgmt/configure-proxy-endpoint) documentation.
> - **Defined client schema**: Configure the request and response format expected by the proxy-facing client. This is typically predefined during the proxy setup.
> - **Defined target schema**: Configure the target request schema and response schema. The response schema is essential for enabling transformations before returning the response to the client. You can do this by sending a sample request with the guided setup wizard or providing a JSON sample.

Complete the following steps to configure response transformations:

1. Go to **Platform > API Platform > API Collections**.
   
2. Select the **API proxy collection** containing the endpoint.
   
3. Choose the proxy endpoint, then open the **Details** tab.
   
4. Select the endpoint you plan to modify, then select **Edit endpoint**.
   
5. Click the **Return response** action in the endpoint configuration to define how to [handle the target response](#transform-response-options) before returning it to the client.
   
   ![API proxy transformation flow](/assets/return-response-action.BO6cUHAJ.png)_Configure the **Return response** action_
   

### Apply target response transformations

Choose a transformation option that matches your API’s requirements. Each option determines how the response is modified before returning to the client:

**Return response without transformation**

This default option returns the response received from the target API to the client without any modifications. Use this option when no response transformations are required.

1. Use the **What would you like to do?** drop-down menu to select **Return response without transformation**.
   
2. Click **Save** to finalize the configuration.
   

**Return transformed response**

This option allows you to transform the entire response, including the body and headers, before returning it to the client.

1. Use the **What would you like to do?** drop-down menu to select **Return transformed response**.
   
2. Use the **Response** drop-down menu to specify the response status or message, such as `200 - OK`.
   
3. Define the **Response body** by selecting the data fields to modify or include in the transformed response.
   
4. Define any necessary **Response headers**.
   
5. Click **Save** to finalize the configuration.
   

**Return response with transformed body**

This option enables you to transform only the body of the response while keeping the headers unchanged:

1. Use the **What would you like to do?** drop-down menu to select **Return response with transformed body**.
   
2. Use the **Response** drop-down menu to specify the response status or message, such as `200 - OK`.
   
3. Modify the **Response body** by selecting or configuring the relevant data fields.
   
4. Click **Save** to finalize the configuration.
   

**Return response with transformed headers**

This option allows you to modify only the headers of the response while keeping the body unchanged.

1. Use the **What would you like to do?** drop-down menu to select **Return response with transformed headers**.
   
2. Add or modify **Response headers** as required.
   
3. Click **Save** to finalize the configuration.
   

### Conditional response mapping

Conditional response mapping allows you to return different responses based on defined conditions. You can configure one conditional response using dynamic values from both the proxy request or the target response. For example, you can evaluate fields such as HTTP status codes and return designated responses depending on whether the condition is met.

Complete the following steps to set up conditional response mapping:

1. Add a **Conditional response** step in the transformation editor. This step evaluates the target API’s response based on defined conditions, such as HTTP status codes or other response data.
   
   ![Add a conditional response step](/assets/add-conditional-response.CyWnD-TQ.png)_Add a conditional response step_
   
2. Choose the **Data field** from the response that you plan to evaluate, such as a Status code (Step 2) datapill or any specific response data.
   
   ![Configure data field](/assets/configure-data-field.CTk4ceHp.png)_Configure data field_
   
3. Set the **Condition** that triggers the outcome. For example, to check for error codes, you can use conditions like Status code (Step 2) equals `400`.
   
4. Define the **Value** for the condition. For example, if you're monitoring for a specific status code, set the value to `400` or another relevant code.
   
5. Use the **What would you like to do?** drop-down menu to select how the response should be handled if the condition is met. You can choose options like **Return transformed response** to customize the response.
   
   ![Define response](/assets/define-response.zcuidPMh.png)_Define response_
   
6. Use the **Response** drop-down menu to specify the status code or message, such as `200 - OK`, if **Return transformed response** is selected. Configure the **Response body** and **Response headers** as needed to customize the response. Note that the **Response** drop-down menu applies only when transforming the response.
   
7. Use the **What would you like to do?** drop-down menu again to select how the response should be handled if the condition is not met. For example, you can choose **Return response without transformation** or another option.
   

## Transform data with Workato formulas

Workato formulas allow you to dynamically transform data in API requests and responses. You can use formulas to streamline data formats, perform arithmetic calculations, and manipulate strings. Most documented formulas are supported, with some exceptions. For more information, refer to the Workato [formula](/en/formulas/formula-mode) documentation.

### Example formula transformation

You can use formulas to define default values for request parameters. For example, you can define a request parameter with a formula to set a default value if the input is missing:

![Define response](/assets/transform-parameter.C9I-RIgs.png)_Transform request parameter_

In this example, the Search term (Step 1) datapill is mapped to the **Search term** field using the formula `.presence || 'Featured products'`. This formula sets the **Search term** request parameter to `Featured products` if no search term is provided.

> **FORMULA LIMITATIONS**
> 
> Formulas are limited to the capabilities supported by Workato’s Formula interpreter. They can compute new values based on available data formats but must adhere to documented formula functions.

## Send test requests

After configuring transformations, send test requests to ensure everything works as expected. When sending test requests, verify the following:

- Request transformations are applied correctly to parameters, headers, and the body.
- Response transformations modify the response body and headers as intended before returning them to the client.
- HTTP status codes are accurate and reflect the intended response behavior.
- Test data reflects real-world scenarios to check for any edge cases.

Testing ensures your API proxy transformations function properly and meet client and target requirements.

---
