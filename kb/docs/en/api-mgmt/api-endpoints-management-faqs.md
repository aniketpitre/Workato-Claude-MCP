---
url: 'https://docs.workato.com/en/api-mgmt/api-endpoints-management-faqs.md'
description: >-
  Find answers to common questions about managing API endpoints in Workato,
  including error codes, testing, securing, and monitoring endpoint usage.
---

# API endpoints management FAQs

Get answers to frequently asked questions (FAQs) about API endpoints management.

## What does a 503 Service Unavailable error mean, and is it caused by an issue on my end when using the API?

View answer

A 503 Service Unavailable error signifies that the server hosting the API is currently unable to process the request. This error is typically due to the server that is temporarily offline, undergoing maintenance, or experiencing an overload of requests.

It is important to note that a 503 error is not caused by an issue on your end. It reflects a problem with the target API's server, indicating that the server is unreachable at the time of your request.

## How do I test the endpoint with raw content?

View answer

After you create and configure the endpoint, you can [test](/en/api-mgmt/testing-endpoints#test-recipe-endpoint) it using tools like Postman or curl by sending raw content to the endpoint and verifying the response.

## Are Callable recipes still supported?

View answer

[Callable recipes](/en/features/callable-recipes) are deprecated but continue to function. The guide uses the API Platform connector, which functions similarly to Callable recipes.

## Can I secure API endpoints that handle raw content?

View answer

Yes, you can secure API endpoints by implementing authentication and authorization mechanisms. Workato supports various methods, including API tokens and OAuth to ensure that only authorized clients can access the endpoints.

## How do I monitor API endpoint usage?

View answer

You can monitor API endpoint usage through Workato’s API Platform logs. Navigate to **API platform > Logs** to view details about requests, responses, and performance metrics.

## Can I use these API endpoints with other Workato features?

View answer

Yes, API endpoints configured to handle raw content can be integrated with other Workato features such as recipes, connectors, and triggers. This allows for seamless automation and data processing across different applications.

## How do I update an existing API endpoint to handle raw content?

View answer

To update an existing API endpoint to handle raw content:

1. Navigate to **API platform > API collections** and select the collection containing the endpoint.
   
2. Select the endpoint you want to update and click **Edit**.
   
3. Update the Request and Response configurations to handle the new content type.
   
4. Save the changes and test the endpoint to ensure it functions as expected.

---
