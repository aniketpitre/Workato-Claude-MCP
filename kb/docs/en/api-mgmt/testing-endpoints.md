---
url: 'https://docs.workato.com/en/api-mgmt/testing-endpoints.md'
description: >-
  Learn how to test recipe-based and proxy-based API endpoints in the Workato
  API platform before exposing them to clients.
---

# Testing API endpoints

Workato allows you to test [API endpoints](/en/api-mgmt/api-endpoints), whether they are [recipe-based](#test-recipe-endpoint) or [proxy-based](#test-proxy-endpoint).

## Test a recipe endpoint

If you want to [test a recipe endpoint](#test-recipe-endpoint), you must configure the corresponding [API recipe](/en/api-mgmt/api-recipes/) first.

1. Make sure the endpoint's corresponding API recipe is running. You can do this by [starting the recipe](/en/recipes/start-and-stop#start-recipe) or [enabling the recipe's test mode](/en/recipes/testing).
   
2. From the API recipe collection page, open the endpoint you want to test.
   
3. Recipe-based endpoints must be active before you can test them. If you haven't activated the endpoint yet, select the **Inactive** toggle in the upper right of the page to change it to **Active**.
   
   ![Activate API recipe endpoint](/assets/api-recipe-endpoint-activate.uiPb2v4j.png)_Activate API recipe endpoint_
   
   For more information about activating endpoints, see [Activating or deactivating an endpoint](/en/api-mgmt/api-endpoints#activating-or-deactivating-an-endpoint).
   
4. Select the **Try it out** button to the right of the **Parameters** section.
   
   ![API recipe endpoint Try it out button](/assets/api-recipe-endpoint-try-it-out-button.D1TclnHJ.png)_Try it out button on an API recipe endpoint_
   
5. Enter any required path, query, or body parameters in the **Parameters** section.
   
   The following screenshot shows a recipe endpoint with its required `username` path parameter filled out:
   
   ![Entering a path parameter for a recipe endpoint](/assets/api-endpoint-test-get-path-parameter.CsnvfL9V.png)_Entering a path parameter for a recipe endpoint_
   
6. Select **Execute** to send the test request.
   
   The following screenshot of a recipe endpoint shows a test response with a `200` success code:
   
   ![Successful test response](/assets/test-response.hlbRPXbW.png)_Successful test response_
   
   > **USING THE EXAMPLE CURL COMMAND**
   > 
   > The **Responses** section includes an example curl command you can copy and run in your terminal to test the recipe endpoint. Note that before you run the command in your terminal, you must complete the following steps:
   > 
   > 1. [Create an API client.](/en/api-mgmt/api-client-mgmt#create-new-client)
   > 2. [Create an API key](/en/api-mgmt/api-client-mgmt#create-a-new-application) to grant the client access to the collection with the recipe endpoint you want to test.
   > 3. Copy the auth token that was generated when you created the API key.
   > 4. Add `-H 'api-token: <your-api-token>'` to the example curl command yourself. For example:
   > 
   > ```shell
   > curl -X 'GET' \
   >   'https://api.na.workato.com/exampleuser/subscription-api-v1/user/rsloan' \
   >   -H 'accept: application/json' \
   >   -H 'api-token: 1234567890abcdefgh'
   > ```
   
7. View the **Jobs** tab for the corresponding recipe to see the test job you just executed. Select the job to see more details.
   

## Test a proxy endpoint

You can [test a proxy endpoint](#test-proxy-endpoint) immediately after you create the collection from an OpenAPI specification because Workato simply forwards the request to the specified target URL.

1. [Create an API client](/en/api-mgmt/api-client-mgmt#create-new-client) if you don't already have one.
   
2. [Create a new API key](/en/api-mgmt/api-client-mgmt#create-a-new-application) or assign an existing one to give the API client access to the API proxy collection containing the endpoint you want to test.
   
3. From the API proxy collection page, open the endpoint you want to test and navigate to the **Test** tab.
   
4. Select the **Try it out** button in the **Parameters** section:
   
   ![API proxy endpoint Try it out button](/assets/api-proxy-endpoint-try-it-out-button.ohQ0NhTh.png)_API proxy endpoint Try it out button_
   
5. Enter any required path, query, or body parameters in the **Parameters** section.
   
   The following screenshot shows a proxy endpoint with its required `orderId` path parameter set to the value `1`:
   
   ![Entering a path parameter for a proxy endpoint](/assets/api-proxy-endpoint-test-get-path-parameter.CFet1pSD.png)_Entering a path parameter for a proxy endpoint_
   
6. In the **Authentication** box, select the **Edit token** button:
   
   ![Slect the Edit token button](/assets/api-test-proxy-endpoint-edit-token.DJ_Sibal.png)_Select the Edit token button_
   
7. Select an authentication method from the **Auth method** picklist and enter the access or auth token for your client in the **Token** field.
   
8. Select **Set token** to confirm the auth token.
   
9. Select **Execute** to send the test request.
   
   The following screenshot of a proxy endpoint shows a test response with a `200` success code and a downloadable response body:
   
   ![Successful test response](/assets/api-test-proxy-endpoint-success.CxU7QiGL.png)_Successful test response_
   
   > **USING THE EXAMPLE CURL COMMAND**
   > 
   > The **Responses** section includes an example curl command you can copy and run in your terminal. Note that you must add `-H 'API-TOKEN: <your-API-TOKEN>'` to the command yourself. For example:
   > 
   > ```shell
   > curl -X 'GET' \
   >   'https://api.na.workato.com/exampleuser/store/order/1' \
   >   -H 'accept: application/json' \
   >   -H 'api-token: 1234567890abcdefgh'
   > ```
   

## Errors

If the response value is not 2XX, the test results in an error. There can be numerous reasons for an error.

The most common error when performing a test from the same account that owns the API recipe is "Invalid request" (400). This usually indicates that the input parameters were incorrect, not all required parameters were supplied, or contained values that are invalid for the target recipe.

If you are configuring an endpoint, proceed to the next section to activate the endpoint.

---
