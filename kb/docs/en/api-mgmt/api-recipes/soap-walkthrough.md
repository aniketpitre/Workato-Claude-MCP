---
url: 'https://docs.workato.com/en/api-mgmt/api-recipes/soap-walkthrough.md'
description: >-
  Build a Workato SOAP API recipe that parses and processes SOAP requests
  through a target API hosted on-premises using an HTTP connection.
---

# SOAP API recipe walkthrough

This walkthrough shows you how to build a SOAP endpoint manually in Workato. The endpoint accepts raw XML, and the recipe parses and validates the SOAP envelope before passing the request to a target API hosted on a private server. This lets external business partners and internal stakeholders access the API's data without connecting to the target API directly.

This walkthrough builds the Workato-side endpoint in front of the target API, not the target API itself. You can build and test much of the endpoint before the target API is available, but the recipe can return data from the target API only after that API is reachable.

## What you'll build

In this walkthrough, you'll build the following components:

- A SOAP API recipe that accepts XML requests, identifies the requested operation, checks whether the operation is approved, and forwards approved requests to the target API.
- A separate API recipe that returns the WSDL that describes the SOAP API.
- An [API recipe collection](/en/api-mgmt/api-collections/recipe-collection) that exposes both recipes as endpoints.

The SOAP API recipe uses three response paths:

- `success` when the target API request succeeds.
- `not_found` when the requested operation isn't on the approved list.
- `error` when the request to the target API fails.

## Prerequisites

Ensure the following before you create the SOAP API recipe:

- Access to the API platform. The API platform is available to customers on specific pricing plans. Refer to your pricing plan and contract for more information.
- **Create** privileges for [API collections and endpoints](/en/privileges#collections-and-endpoints) and [recipes](/en/privileges#recipe).
- A lookup table that contains the SOAP operations the endpoint should allow.
- An HTTP connection for the target API. Configure the connection to use an [on-prem group](/en/on-prem/groups) to reach an API hosted on a private server.
- The request details required to call the target API, such as its URL, method, headers, and payload format.
- A WSDL that describes the SOAP API if you plan to expose the WSDL endpoint in this walkthrough. This walkthrough shows how to return the WSDL, not how to author one.

## Create the SOAP API recipe

Complete the following steps to create the SOAP API recipe:

1. Create a new recipe and give it a name.
   
2. Select a folder for the recipe.
   
3. Click **Build an API endpoint** as the starting point.
   
4. Click **Start building**.
   

The **Build an API endpoint** starting point automatically creates a recipe with a **New API request** trigger and a **Respond to API request** action.

## Define the recipe's trigger

The **New API request** trigger defines the request and response structures for the endpoint.

1. [Define the request structure](#define-the-request-structure)
2. [Define the response structure](#define-the-response-structure)

### Define the request structure

Complete the following steps to define the request structure:

1. Click the trigger to open its **Setup** tab.
   
2. Expand the **Request** section if it isn't open already.
   
3. Select **Text/XML** in the **Content type** field. This allows the trigger to accept the raw XML body of the SOAP request instead of parsing the request as JSON. Refer to [Supported data types](/en/api-mgmt/api-recipes/walkthrough#raw-content) for the full list of content type options.
   
4. Define request headers in the **Request header** section if callers must provide them.
   

### Define the response structure

The response structure defines the outputs the SOAP API recipe can return. This recipe uses three responses: `success`, `not_found` for an operation that isn't on the approved list, and `error` if the target API request fails.

Complete the following steps to define the response structure:

1. Expand the **Response** section if it isn't open already.
   
2. Select **Text/XML** in the **Content type** field.
   
3. Define response headers in the **Response headers** field if the endpoint must return them.
   
4. Select **Add response** from the **Responses** field.
   
5. Enter `success` in the **Name** field.
   
6. Use the **HTTP status code** field to specify whether the response code is standard or custom.
   
   - If you select **Standard response**, choose an HTTP status code from the picklist. For example, `200 - OK` for the `success` response.
   - If you select **Custom response**, enter a custom HTTP status code. You can specify response codes from 2xx to 5xx.
7. Repeat the previous two steps to add a `not_found` response (`404 - Not Found`) and an `error` response (`500 - Internal Server Error`).
   

## Process the SOAP request

Add steps to the recipe to parse the SOAP envelope, validate the requested operation, and call the target API:

1. [Parse and inspect the XML payload](#parse-and-inspect-the-xml-payload)
2. [Check whether the operation is approved](#check-whether-the-operation-is-approved)
3. [Call the target service and handle errors](#call-the-target-service-and-handle-errors)

### Parse and inspect the XML payload

A SOAP request arrives as a SOAP envelope in the request body. For example:

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <OperationName>
      <Parameter>value</Parameter>
    </OperationName>
  </soap:Body>
</soap:Envelope>
```

Complete the following steps to parse and inspect the XML payload:

1. Add the **Parse XML document** action from [XML Tools by Workato](/en/connectors/xml-tools-workato). Enter a representative SOAP envelope as the **Sample document** so the action generates datapills for the values you need from the SOAP body.
   
   Use the datapill that identifies the requested operation in the next step. Your sample document should match the structure of the SOAP requests your endpoint receives.
   
2. Add the **Search entries** action from **Lookup tables by Workato**. Search the lookup table that contains your approved operations using the operation value parsed from the SOAP body.
   

### Check if the operation is approved

Branch the recipe based on whether the lookup table contains the requested operation.

1. Add an **IF** condition that checks whether the lookup table search returned a match: the entry ID from the previous step **is present**.
   
2. Add an **ELSE** block to reject the requested operation when the lookup table search doesn't return a match.
   
   Inside the **ELSE** block, select the return action (**Action in an app > API platform by Workato > Respond to API request**) and choose the `not_found` response.
   

### Call the target service and handle errors

Inside the **IF** block, wrap the call to the target API in a **Handle errors** control statement. This lets the endpoint return a defined API response if the target API request fails.

Complete the following steps:

1. Inside the **IF** block, click **\+ Add step** and select **Handle errors**. Workato creates a **Monitor actions for error** block and an **Error found?** block.
   
2. Inside the **Monitor actions for error** block, add **Action in an app > HTTP > Send request**. Select the HTTP connection for the target API. For a target API hosted on a private server, use a connection that forwards requests through an [on-prem group](/en/on-prem/groups).
   
   Configure the request using the URL, method, headers, and payload expected by the target API.
   
3. Immediately after the **Send request** action, still inside the **Monitor actions for error** block, add **Action in an app > API platform by Workato > Respond to API request**. Choose the `success` response and map the payload returned by the target API to the response body.
   
4. Configure the **Error found?** block. Choose whether to retry the target API request and how many times.
   
5. Inside the **Error found?** block, add **Action in an app > API platform by Workato > Respond to API request** and choose the `error` response. This response runs if the target API request still fails after any configured retries.
   

## Create a recipe to return the WSDL

Create a separate API recipe that returns the WSDL describing the SOAP API. Create this recipe in the same folder as the SOAP API recipe, so you can add both recipes to the same API recipe collection.

The WSDL can be stored in Workato FileStorage. Configure the recipe to retrieve the WSDL and return its contents as the response body.

![WSDL API recipe](/assets/wsdl-api-recipe.BnVpIe6I.png)_WSDL API recipe_

## Test the recipe logic

Save and test the SOAP API recipe as you build it. [Building recipes in small steps](/en/troubleshooting/tips-and-tricks/test-frequently) makes it easier to isolate problems before you test the complete endpoint.

### Test request parsing and operation validation

The target API doesn't need to be reachable to test the trigger, XML parsing, and lookup table logic.

[Skip](/en/recipes/steps/skip-step) the **Send request** action and send sample SOAP requests to verify that:

- The recipe parses the value used to identify the requested operation.
- An approved operation follows the **IF** branch.
- An operation that isn't in the lookup table follows the **ELSE** branch and returns the `not_found` response.

### Test the error path

You can also test the `error` response before the target API is available. Leave the **Send request** action enabled and send a request that reaches that step while the target API is unavailable or otherwise causes the HTTP request to fail.

The failed request enters the **Error found?** block and returns the `error` response after any configured retries.

### Test the success path with a public API

You can temporarily point the **Send request** action at a reachable public test API, such as `https://jsonplaceholder.typicode.com/todos`, to test the recipe's success path before your target API is available.

When you use JSONPlaceholder for this test:

- Configure the **Send request** action for the public test endpoint rather than the private target API.
- Match the **Request content type** field to the payload you're sending.
- Set the **Response content type** field to **Text** to pass the response through without parsing it as XML or JSON.
- After you validate the recipe flow, restore the **Send request** action to the real target API configuration.

## Group the recipes into a collection

Group the SOAP API recipe and WSDL recipe into an [API recipe collection](/en/api-mgmt/api-collections/recipe-collection). Select **Use existing recipes** and choose the folder that contains both recipes.

This creates two endpoints: one that processes SOAP requests and one that returns the WSDL.

> **NEW ENDPOINTS INACTIVE BY DEFAULT**
> 
> New endpoints are inactive by default. You must activate both endpoints before other recipes or apps can call them. Refer to [Activating or deactivating an endpoint](/en/api-mgmt/api-endpoints#activating-or-deactivating-an-endpoint) for more information.

## Test the endpoint end-to-end

You can [test the SOAP endpoint](/en/api-mgmt/testing-endpoints#test-recipe-endpoint) with the real target API after you activate the endpoints and the API is reachable.

Send an approved operation and verify the complete flow:

1. The endpoint accepts the SOAP request as raw XML.
2. The recipe parses the SOAP body and identifies the requested operation.
3. The lookup table confirms that the operation is approved.
4. The HTTP action sends the request to the target API.
5. The recipe returns the target API payload through the `success` response.

You can send the request with curl or another HTTP client. The **Try it out** tester doesn't expose a field for a raw request body, so use a client that lets you send the SOAP envelope directly:

```shell
curl -X POST 'ENDPOINT_URL' \
  -H 'api-token: API_KEY' \
  -H 'Content-Type: text/xml' \
  --data-binary '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><OperationName><Parameter>APPROVED_OPERATION</Parameter></OperationName></soap:Body></soap:Envelope>'
```

Refer to [Test a recipe endpoint](/en/api-mgmt/testing-endpoints#test-recipe-endpoint) for how to create the API client and key required by the curl request.

The SOAP API recipe is now ready to implement with your target API.

---
