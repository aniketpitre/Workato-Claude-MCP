---
url: 'https://docs.workato.com/en/oem/apip-enablement.md'
description: >-
  Enable the API platform in Embedded customer workspaces by building endpoint
  recipes, importing collections, and creating clients and applications.
---

# Enabling API platform for customers

The [API platform](/en/api-management) is a tool that helps Embedded partners securely share content or microservices with their customers. It enables use cases that extend their product's functionality by building recipes triggered by API endpoints.

The following guide covers the concepts and [platform API endpoints](/en/oem/oem-api) required to programmatically enable the API platform in customer workspaces.

> **PROCESS OVERVIEW**
> 
> Enabling the API platform for customers entails the following:
> 
> 1. Creating API endpoint recipes and collections
> 2. Creating customers
> 3. Importing the recipes and collections to customer workspaces
> 4. Creating client applications in customer workspaces
> 5. Starting recipes and activating the endpoints

## Creating API endpoint recipes

1. The first step in setting up an API endpoint is to create a recipe that uses the **API platform - New API request** trigger. Click the **Build an API endpoint** starting point to automatically select this trigger. ![Admin console](/assets/api-endpoint-recipe.Cfnt5SlC.png)_Select Build an API endpoint recipe as the recipe starting point_
   
2. Organize these recipes into one or more API Collections. Generally, an API Collection contains endpoints whose access patterns share common features, permitting you to manage them together. For example, if you have a set of Salesforce endpoints used by your sales team in recipes, you might group them together in an API Collection.
   
3. Activate and test your API endpoints. Reference our [API endpoint management](/en/api-mgmt/api-endpoints#configuring-a-new-api-endpoint) and [API collection creation](/en/api-mgmt/api-collections) guides for detailed information on building and activating endpoints and collections.
   
4. After creating and testing your endpoints, use the [Recipe lifecycle management](/en/recipe-development-lifecycle/export#create-a-manifest) tool to create a manifest that includes all the collections and endpoints.
   

* * *

> **Best practice**
> 
> Build and test API endpoint recipes in the Embedded partner's admin account before importing them into customer workspaces. Create the recipes in the same folder to simplify the import and export processes.

## Creating customers

You can create customers in the UI of the Admin console or by using the [Manage customers platform API](/en/oem/oem-api/managed-users). The customer ID is returned in the response body when using the API to create customers.

If viewing or creating the customer in the UI of the Admin console, the customer ID is available in the URL of the customer info page.

![Admin console](/assets/customer-id.DXwl62FA.png)_Obtain the customer ID in the UI in the URL_

> **Embedded platform API shortcuts**
> 
> 1. Create a customer: [POST /api/managed\_users](/en/oem/oem-api/managed-users#create-customer-account)

* * *

## Importing the recipes and collections to customer workspaces

You can import recipes and collections to customer workspaces in the Workato UI or with Embedded platform APIs.

Before importing recipes from the admin account to the customer workspace, create a folder in the customer workspace. The folder must be a top-level folder (nested one level within `Home`).

Use the manifest saved in the admin workspace to export packages into customer workspaces. Exporting copies the endpoints and collections in the package into the customer workspace.

> **Embedded platform API shortcuts**
> 
> 1. Create a top-level required folder in the customer workspace: [POST /api/managed\_users/:id/folders](/en/oem/oem-api/folders#create-folder)
> 2. Export a package from the admin workspace: [POST /api/packages/export/:id](/en/workato-api/recipe-lifecycle-management#export-package-based-on-a-manifest)
> 3. Import a package into the customer workspace: [POST /api/managed\_users/:id/imports](/en/oem/oem-api/recipe-lifecycle-management#package-import)

* * *

## Creating client applications in customer workspaces

API clients are groups of users who receive access to one or more API collections through an application. For example, members of the same organization comprise an API client and access API collections through individual applications. You can create API clients and applications in the Workato UI or by using Embedded platform APIs.

1. Add API clients and applications to your customer workspaces to enable these endpoints. Reference our [client and application](/en/api-mgmt/api-client-mgmt) guide for detailed instructions.
   
2. Assign the collection imported in the preceding step to an application. Considering each customer already has an account, you may only need to create one default client and one default application.
   

Update the application to include the new collection IDs when you add more collections.

> **Embedded platform API shortcuts**
> 
> 1. Create an API client: [POST /api/managed\_users/:id/api\_clients](/en/oem/oem-api/api-platform#create-api-client)
> 2. Create an API key within the client: [POST /api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys](/en/oem/oem-api/api-platform#create-an-api-key)
> 3. Update an API key: [PUT /api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](/en/oem/oem-api/api-platform#update-api-key)

* * *

## Starting recipes and activating endpoints

After importing recipes into the customer workspace, you must start them before activating the endpoints. After the endpoints are activated, you can call the endpoints using the API client.

You can start recipes and activate endpoints in the Workato recipe building UI or by using Embedded platform API endpoints.

If the Embedded partner needs to limit access to endpoints for the API client, the partner may deactivate the endpoints.

> **Embedded platform API shortcuts**
> 
> 1. Obtain recipe IDs: [GET /api/managed\_users/:id/recipes](/en/oem/oem-api/recipes#list-recipes-in-a-customer-account)
> 2. Start a recipe: [PUT /api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/start](/en/oem/oem-api/recipes#start-recipe-in-a-customer-account)
> 3. Activate an endpoint: [PUT /api/managed\_users/:id/api\_endpoints/:api\_endpoint\_id/enable](/en/oem/oem-api/api-platform#enable-api-endpoint)
> 4. Disable an endpoint: [PUT /api/managed\_users/:id/api\_endpoints/:api\_endpoint\_id/enable](/en/oem/oem-api/api-platform#disable-api-endpoint)

---
