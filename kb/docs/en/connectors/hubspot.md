---
url: 'https://docs.workato.com/en/connectors/hubspot.md'
description: >-
  The HubSpot connector lets you automate CRM workflows: create, update, and
  search records, manage lists, and trigger on new records and form submissions.
---

# HubSpot

[HubSpot](https://www.hubspot.com/) is a leading growth platform that offers a full suite of marketing, sales, customer service, CRM software and additional services. The platform enables businesses to optimize their content, nurture leads, and monitor contacts as they become customers, to track marketing progress. HubSpot also supports integration with an ever-growing range of customer success, productivity, and finance applications to facilitate and boost the growth of businesses.

## API version

The HubSpot connector uses the [HubSpot REST API v3](https://developers.hubspot.com/docs/api/overview).

## Supported editions and versions

The HubSpot connector works with all HubSpot cloud instances, for example, **Starter, Professional, and Enterprise**.

However, the availability of HubSpot connector triggers and action depends on the HubSpot account privileges. Access to HubSpot APIs depends on the account tier. Learn more about [HubSpot account tiers](https://developers.hubspot.com/docs/api/working-with-oauth#scopes).

## Triggers and actions

Workato's HubSpot connector includes triggers and actions for managing records, contact lists, associations, and marketing workflows.

- [Browse triggers](/en/connectors/hubspot/triggers)
- [Browse actions](/en/connectors/hubspot/actions)

> **DEPRECATED TRIGGERS AND ACTIONS**
> 
> Some triggers and actions are deprecated. Refer to the following sections for updated versions:
> 
> - [Deprecated triggers](/en/connectors/hubspot/triggers#deprecated-triggers)
> - [Deprecated actions](/en/connectors/hubspot/actions#deprecated-actions)

## How to connect to HubSpot on Workato

Complete the following steps to authenticate with HubSpot using OAuth 2.0:

1. Click **Create > Connection** or press C twice.
   
2. Search for `HubSpot` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder to store your connection.
   
5. Optional. Go to the **Advanced settings** section and select the scopes to provide to Workato. The connector requests the minimum set of scopes for its recipe triggers and actions by default. Refer to the complete list of [available scopes](/en/connectors/hubspot/scopes#full-list-scopes) for more information.
   
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a [custom OAuth profile](/en/custom-oauth-profiles) for your connection.
   
7. Click **Connect**.
   
8. Select the HubSpot account where you plan to authorize Workato and click **Choose Account**.
   
   ![Choose account](/assets/select-account.BvvC0buZ.png)_Select an account_

---
