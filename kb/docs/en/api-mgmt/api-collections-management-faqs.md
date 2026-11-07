---
url: 'https://docs.workato.com/en/api-mgmt/api-collections-management-faqs.md'
description: >-
  Answers to common questions about API collection management in Workato,
  including collection types, access, and how to manage endpoints.
---

# API collection management FAQs

Get answers to frequently asked questions (FAQs) about API collection management.

What is an API collection, and why is it used in Workato?

An [API collection](/en/api-mgmt/api-collections#collection-types) is a grouping of API endpoints that share a common access pattern, allowing them to be managed together. API collections are used to organize and manage related endpoints efficiently.

How can I access the API collections page in Workato?

To [access the API collections](/en/api-mgmt/api-collections#create-api-recipe-collection) page:

1. Log in to Workato and navigate to the workspace you plan to access the API collections page for.
   
2. Click to **Platform > API platform > API collections**.
   

What are the three types of API collections available at Workato?

There are three [types of API collections](/en/api-mgmt/api-collections#collection-types) available at Workato:

- API proxy collections
- API recipe collections
- AI gateway collections

What is an API recipe collection, and how does it work?

An [API recipe collection](/en/api-mgmt/api-collections#create-api-recipe-collection) consists of endpoints created from individual API recipes, with one recipe corresponding to one endpoint. API recipe collections enable you to make powerful API endpoints accessible to both internal and external users, even those without a Workato account.

Before creating an API recipe collection, you must create a project, create a folder within the project, and add one or more API recipes to the folder.

What is an API proxy collection, and what is it's purpose?

An [API proxy collection](/en/api-mgmt/api-collections#create-api-proxy-collection) contains proxy endpoints that act as intermediaries between API clients and servers. It adds a layer of security and control to internal APIs. This makes it easier to manage and monitor access control features.

To create API proxy collections, you must create a project and set up an HTTP connection to forward requests to.

How do I choose between an API recipe collection and an API proxy collection?

Your [choice depends on your use case](/en/api-mgmt/api-collections#collection-types). API recipe collections are suitable when you plan to build your own backend, allowing customization of data retrieval and processing. API proxy collections are ideal for forwarding requests to existing backend APIs with minimal latency.

What settings can be configured for API collections, and where can I find them?

To find and [configure your API collections settings](/en/api-mgmt/api-collections#configure-settings):

1. Log in to Workato and navigate to the workspace you plan to access the API collections page for.
   
2. Click to **Platform > API platform > API collections > Settings**.
   

Configuration settings include:

- Version tags
- Descriptions
- URL settings
- Sharing options
- Ability to sync the collection to Postman

How can I synchronize an API collection with Postman?

To [sync an API collection with Postman](/en/api-mgmt/api-collections#sync-to-postman):

1. Log in to Workato and navigate to the workspace you plan to access the API collections page for.
   
2. Click to **Platform > API platform > API collections**.
   
3. Select **Settings > Sync to Postman**.
   
4. Connect to your Postman instance and configure the location for the collection to complete the synchronization.
   

Is there machine-readable documentation available for API collections?

Yes, [machine-readable documentation](/en/api-mgmt/api-collections#openapi) in the form of OpenAPI specifications is available for API collections. You can download the OpenAPI spec for an API collection from the upper-right corner of the API collection page.

---
