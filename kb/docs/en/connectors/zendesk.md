---
url: 'https://docs.workato.com/en/connectors/zendesk.md'
description: >-
  Connect to Zendesk to manage customer support tickets, track engagement, and
  automate customer service workflows.
---

# Zendesk

[Zendesk](https://www.zendesk.com/) is a cloud-based ticketing solution that empowers customer engagement and support management.

## API version

The Zendesk connector uses [Zendesk REST API v2](https://developer.zendesk.com/rest_api/docs/zendesk-apis/resources).

## Connection setup

The Zendesk connector uses OAuth 2.0 authentication.

> **DEPRECATED AUTHENTICATION METHODS**
> 
> Effective March 31, 2026, you can no longer create new Zendesk connections using Basic authentication or Custom OAuth profiles. This change is required by [Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/).
> 
> Existing connections using these authentication methods will continue to work until **April 30, 2027**. On this date, Zendesk connections still using Basic authentication or a Custom OAuth profile will be terminated, and recipes relying on these connections will stop functioning.

Complete the following steps to connect to Zendesk in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Zendesk` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Zendesk with OAuth 2.0](/assets/oauth2.CJ5g3KV-.png)_Connect to Zendesk with OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Zendesk subdomain in the **Subdomain** field. For example, your subdomain is `acme` if your Zendesk URL is `https://acme.zendesk.com`.
   
6. Click **Connect**.
   
7. Sign in to Zendesk using your credentials to authorize Workato.

---
