---
url: 'https://docs.workato.com/en/api-mgmt/api-recipes/walkthrough.md'
description: >-
  Create a Workato API recipe so external partners and internal users can access
  and consume data through an API endpoint.
---

# Create an API recipe

This guide explains how to create an API recipe. External business partners and internal stakeholders can use this endpoint to access and consume data without requiring access to a Workato account.

> **PREREQUISITES**
> 
> You must have the following prerequisites to create an API recipe:
> 
> - **Access to the API platform feature**. The API Platform feature is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.
> - **Create** privileges for [API collections and endpoints](/en/privileges#collections-and-endpoints) and [recipes](/en/privileges#recipe).

Refer to the [Add users to Google Workspace](/en/getting-started/use-cases/api-recipes/add-users-to-google-workspace) use case for steps to create an integration for Workato API platform and Google Workspace that enables you to add users to your Google Workspace with your preferred CLI or when a new employee is detected in BambooHR.

## Supported data types

Use the **Content type** drop-down menu to configure the data format the connector accepts. API recipes support the following options:

- **JSON**: Accepts data in JavaScript Object Notation format. Use this for most REST APIs and structured payloads.
- **Text/XML**: Accepts raw content such as XML, SOAP, CSV, and YAML. Use this to handle non-JSON formats or plain text payloads.
- **Multipart**: Accepts requests in multiple parts. Use this for requests that include mixed data.

Refer to [Parse the request body](#parse-the-request-body) for additional data processing information.

## Top-level array support

The **Request structure** and **Response structure** drop-down menus control the outermost shape of the request or response body with a single object or a top-level array.

- **Object**: Use this option if you need the body to nest an array under a key, for example:
  
  ```json
  {
    "accounts": [
      { "id": 1, "name": "Acme Corp" },
      { "id": 2, "name": "Globex Inc" }
    ]
  }
  ```
  
- **Array of objects**, **Array of strings**, **Array of integers**, **Array of numbers**, **Array of booleans**, **Array of dates**, or **Array of date-times**: Use one of these options if you need the body to be a bare top-level array, for example:
  
  ```json
  [
    { "id": 1, "name": "Acme Corp" },
    { "id": 2, "name": "Globex Inc" }
  ]
  ```
  

The **Request body** and **Response schema** sections only appear when the structure is set to **Object** or **Array of objects**, because the other array types hold scalar values and don't have a schema to define. The selected structure defines the type of each item for an array type.

New endpoints default to **Object**, and existing endpoints behave as they did before. Top-level arrays also work when you import or export a specification in OpenAPI 3 or Swagger 2 format.

The **Request parameters** output group includes **List size** and **List index** datapills so you can loop over the request body's items when you set **Request structure** to an array type.

## Request body and legacy request schema

The trigger's **Request** section defines path parameters, query parameters, and the request body in separate sections. Previously, query parameters were part of the request schema. You can still define query parameters in the request body. If the same field appears in more than one place, path parameters take precedence over query parameters, and query parameters take precedence over the request body.

Existing endpoints keep their saved **Request schema** field, which is now a legacy field. The **Request schema** field remains fully supported, and the datapills it generates continue to resolve in your recipe. Workato doesn't migrate existing endpoints, and refreshing the schema doesn't change them. New endpoints use the **Request body** field instead. The **Response** section doesn't have a legacy field. Use **Response structure** to select the shape of the response.

### Migrate to the Request body field

You can keep using the legacy **Request schema** field. Complete the following steps if you prefer to move an existing endpoint to the **Request body** field:

1. Open the recipe and select the **New API request** trigger.
   
2. Go to the **Request** section and copy the schema in the legacy **Request schema** field. Workato removes the schema when you clear the field.
   
3. Clear the fields in the legacy **Request schema**. The **Request body** field replaces it.
   
4. Define the schema in the **Request body** field.
   
5. Define any query or path parameters in the **Query parameters** and **Path parameters** sections.
   
6. Review the steps that use datapills from the **Request parameters** group. Datapills for the request body appear in the **Request body** group and must be remapped where needed.
   
7. Save and test the recipe.
   

## Create the recipe

Complete the following steps to create an API recipe:

> **TROUBLESHOOTING**
> 
> We recommend [building recipes in small steps](/en/troubleshooting/tips-and-tricks/test-frequently) and frequently saving and testing your recipe to make it easier to troubleshoot any issues you encounter.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
4. Enter a name for your recipe in the **Name** field.
   
5. Use the **Location** drop-down menu to select the project where you plan to store the recipe.
   
6. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
7. Click **Pick a starting point > Build an API endpoint**. Workato automatically creates a **New API request** trigger.
   
8. Select the **New API request** trigger.
   
9. Set up the endpoint request structure.
   
   1. Go to the trigger's **Request** section.
      
   2. Use the **Content type** drop-down menu to select the type of data for the endpoint to accept. For example, selecting `application/json` means the endpoint accepts valid JSON data.
      
   3. Optional. Use the **Request header** section to define parameters to accept in request headers.
      
   4. Optional. Use the **Path parameters** section to define parameters to accept in the endpoint path for `JSON` and `Text/XML` requests. You can either upload a sample JSON file or enter the fields manually.
      
   5. Optional. Use the **Query parameters** section to define parameters to accept in the endpoint's query string for `JSON` and `Text/XML` requests. You can either upload a sample JSON file or enter the fields manually.
      
   6. Use the **Request structure** drop-down menu to select the outermost structure of the request body this endpoint accepts. Defaults to **Object**. Refer to [Top-level array support](#top-level-array-support) for the available options.
      
   7. Use the **Request body** section to define the schema of request bodies for `JSON` and `Multipart` requests. You can either upload a sample JSON file or enter the fields manually.
      
      > **REQUEST BODY BASED ON REQUEST STRUCTURE**
      > 
      > The **Request body** section only appears when **Request structure** is set to **Object** or **Array of objects**.
      
      > **LEGACY REQUEST SCHEMA**
      > 
      > Endpoints created before the **Request body** section was available show a legacy **Request schema** field instead. The **Request schema** field remains fully supported. Refer to [Migrate to the Request body field](#migrate-to-request-body) for more information.
      
   
   **Step summary**
   
   This step defines the request structure for the endpoint using fields in the **New API request** trigger.
   
10. Set up the endpoint response structure.
    
    1. Go to the trigger's **Response** section.
       
    2. Use the **Content type** drop-down menu to select the type of data to send in the response.
       
    3. Optional. Use the **Response headers** section to define parameters to send in response headers.
       
    4. Go to the **Responses** section and select **Add response**.
       
    5. Specify a name for the response in the **Response #1** section.
       
    6. Use the **HTTP status code** drop-down menu to select a code for the response. Alternatively, you can toggle the input field from **Standard response** to **Custom response** and enter a custom HTTP status code from `2xx` to `5xx`.
       
    7. Use the **Response structure** drop-down menu to select the outermost structure of the response body this endpoint returns. Defaults to **Object**. Use **Object** if you need the response to nest an array under a key, for example `{"accounts": [...]}`. Use one of the array options if you need the response body to be a bare top-level array, for example `[...]`. Refer to [Top-level array support](#top-level-array-support) for the available options.
       
    8. Use the **Response schema** section to define the schema of response bodies. You can either upload a sample JSON file or enter the fields manually.
       
       > **RESPONSE SCHEMA BASED ON RESPONSE STRUCTURE**
       > 
       > The **Response schema** section only appears when **Response structure** is set to **Object** or **Array of objects**.
       
       You can create a nested schema by dragging and dropping properties between parents. Alternatively, click the **Edit schema** button and provide the schema you plan to use.
       
       ![Response schema](/assets/api-platform-drag-and-drop-properties.x-sGM9w7.png)_Response schema_
       
       ```json
       [
         {
           "name": "ID",
           "type": "string",
           "optional": false,
           "control_type": "text",
           "label": "ID",
           "hint": "Account ID"
         },
         {
           "name": "Name",
           "type": "string",
           "optional": false,
           "control_type": "text",
           "label": "Name",
           "hint": "Account name"
         }
       ]
       ```
       
    
    **Step summary**
    
    This step defines the response structure for the endpoint using fields in the **New API request** trigger.
    
11. Click **\+ Add step**, then select **Handle errors**.
    
    ![Add an error handling step](/assets/handle-errors-standard.D9k1lANk.png)_Add an error handling step_
    
    > **MCP SERVERS**
    > 
    > The **Handle errors** control statement isn't required if you plan to use your API endpoints with an MCP server. Refer to [MCP local servers](/en/mcp/mcp-local-servers) for information about how MCP servers connect to the API platform or [MCP use cases](/en/getting-started/use-cases/mcp/mcp-use-cases) for a step-by-step guide on how to create and use API endpoints with an MCP server.
    
    How does the Handle errors control statement work?
    
    The [Handle errors control statement](/en/recipes/steps#handle-errors-step) allows you to monitor your recipe for errors in actions, similar to the try/catch concept in programming languages. You have the opportunity to perform the following actions if an error occurs:
    
    - Retry the sequence of actions again, in case it was a temporary error such as network issues.
      
    - Take remedial actions, such as notifying users of the error through email or error messages in the app, or to carry out a rollback. For example, you can reverse the job by deleting any created or half-created records.
      
    
    This control statement consists of two blocks: the **Monitor** block and the **Error** block. Place the actions that you plan to monitor for errors within the **Monitor** block. If all actions are successful, Workato ignores the **Error** block. However, if any action in the **Monitor** block results in an error, the actions within the **Error** block are executed.
    
    ```mermaid
    graph TD
        A(Monitor action for errors) ---> B((Error found?))
        B --> C{Yes}
        B --> D{No}
        C --> E(Define how to <br/> handle the error)
        D --> F(Continue processing <br/> the recipe)
       classDef default fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
    ```
    
12. Set up the Monitor block.
    
    1. Add the actions you plan to expose through the API endpoint inside the **Monitor actions for error** block. Refer to [Connectors](/en/connectors) for an app's specific connection and configuration steps.
       
       ![Add actions to monitor for errors](/assets/monitor-action-error.hamSaKjt.png)_Add actions to monitor for errors_
       
    2. Click **\+ Add step > Action in app**.
       
    3. Search for and select `API platform by Workato`.
       
    4. Use the **Response** drop-down menu to select the type of the response to send if the operation doesn't encounter errors. The options in this menu are determined by the responses defined in the recipe's New API request trigger.
       
       You can use [IF conditions](/en/features/if-conditions) to send differing responses based recipe data.
       
    5. Use the **Response body** section to configure the data to return in the response body if the recipe doesn't encounter errors. The structure of this section varies based on the schema defined in the **New API request** trigger.
       
    6. Use the **Response headers** section to configure the data to return in the response headers if the recipe doesn't encounter errors. The structure of this section varies based on the schema you defined in the **New API request** trigger.
       
    
    **Step summary**
    
    This step defines the recipe logic to expose through the API endpoint and the response data to send when the recipe doesn't encounter errors.
    
13. Set up the Error found? block.
    
    1. Select **Do not retry** in the **Error found?** block.
       
    2. Use the **Retry actions in Monitor block?** drop-down menu to select how many times to retry failed actions. Workato allows up to three retries.
       
    3. Click **Select an app and action**.
       
    4. Search for and select `API platform by Workato`.
       
    5. Use the **Response** drop-down menu to select the type of the response to send if the operation encounters errors. The options in this menu are determined by the responses you defined in the recipe's New API request trigger.
       
       You can use [IF conditions](/en/features/if-conditions) to send differing responses based recipe data.
       
    6. Use the **Response body** section to configure the data to return in the response body if the recipe encounters errors. The structure of this section varies based on the schema you defined in the **New API request** trigger.
       
    7. Use the **Response headers** section to configure the data to return in the response headers if the recipe encounters errors. The structure of this section varies based on the schema you defined in the **New API request** trigger.
       
    
    **Step summary**
    
    This step defines retry attempt settings and the response data to send when the recipe encounters errors.
    

Your API recipe is ready to test and implement.

![A configured API recipe](/assets/api-recipe.CkEqu1UN.png)_A configured API recipe_

> **API PERFORMANCE**
> 
> You can go to a recipe's **Settings > Data retention** tab and configure the **Jobs data retention** setting to disable log creation if your API recipes require reduced latency.
> 
> Refer to the [Defining data retention for recipes](/en/security/data-protection/data-retention/configure-retention-for-recipes) guide for more information.

### Parse the request body

Optionally, you can use Workato's [data handling connectors](/en/handling-files-and-attachments) to create datapills from data an endpoint receives.

Complete the following steps to parse a request body:

1. Click **\+ Add step > Action in app**.
   
2. Search for and select a [data handling connector](/en/handling-files-and-attachments), for example: `XML tools by Workato`.
   
3. Select the connector's **Parse document** action, for example: **Parse XML document**.
   
4. Refer to the [connector's documentation](/en/handling-files-and-attachments) to configure connector-specific fields.
   
5. Enter a **Sample document** that defines the expected structure of the input. Workato uses this to generate the output schema.
   
6. Map the Request body (Step 1) datapill from the **New API request** trigger's output to the **Document** field.
   

The data parsing step is complete. Workato generates datapills based on the structure defined in the **Sample document** field.

## Expose an API endpoint

After you [create the recipe](#create-the-recipe), the next step is to expose the API recipe as an endpoint in the API platform. This allows you to test the endpoint before releasing it to production and ensure it behaves as expected.

Complete the following steps to expose the recipe as an endpoint:

1. Go to **Platform > API platform > API collections**.
   
2. Create a new [API collection](/en/api-mgmt/api-collections) if you don't have an existing collection in your workspace.
   
3. [Configure the recipe endpoint](/en/api-mgmt/configure-recipe-endpoint).
   

## Endpoint management

You can manage an API endpoint using the following tools:

- [API recipe collections](/en/api-mgmt/api-collections#create-api-recipe-collection) organize endpoints into groups for distribution and version control.
- [API clients](/en/api-mgmt/api-client-mgmt#create-new-client) organize users into groups for API access management.
- [API keys](/en/api-mgmt/api-client-mgmt#api-keys) provide secure authentication for API clients.
- [API access policies](/en/api-mgmt/api-access-policies) enforce rate limits and request quotas for clients.
- The [RecipeOps](/en/connectors/recipeops) connector enables you to build recipes to monitor and manage workspaces. For example, you can use the **API concurrency threshold exceeded** trigger to monitor the concurrency quota in a workspace.

---
