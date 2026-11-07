---
url: 'https://docs.workato.com/en/developing-connectors.md'
description: >-
  Workato universal connectors let you build custom triggers, actions, and
  connectors using HTTP, OpenAPI, GraphQL, SOAP, and the connector SDK.
---

# Universal connectors

If you're stuck on an integration because of a missing trigger, action, or connector, Workato has platform extensions that enable you to easily build a working trigger or action with minimal work. In this section, we have guides to walk you through the building process.

However, before building your own, consider some possible alternatives to connect to your apps.

- **Use CSV file import/export via a file connector**

Many apps support [CSV import/export](/en/features/handling-csv-files). Workato can help to automatically import data from a CSV file into your apps, or write data to CSV files.

If you're missing a trigger to read data from your apps, you can configure your apps to create a CSV file and upload it to an SFTP server for Workato to read.

If you're missing an action to write data to your apps, Workato can upload a CSV file into your app's file server for you to mass import at your convenience.

- **Connect with the database directly**

If you want to connect to a proprietary app developed in-house or a self-hosted app that Workato doesn't connect with, you can check if Workato has a connector for the database used by the app, such as MySQL or SQL Server. If yes, you might consider connecting directly to the database to read or write data.

Documentation on the databases can be found under the [connectors section](/en/connectors).

## Workato connector extensions

You can build your own triggers, actions, and connectors on Workato via custom actions, the [HTTP universal connector](/en/developing-connectors/http-v2) or the [SDK](/en/developing-connectors/sdk). Here's a flowchart to guide you on the framework to use.

![Flowchart to decide what framework to use](/assets/connector-dev-flowchart.CKDLo3Q4.png)_Flowchart to decide what framework to use_

### Custom actions

[Custom actions](/en/developing-connectors/custom-actions) allow you to build an action on top of an existing Workato connector. This allows you to focus on the HTTP request and response, and the Workato connector handles the authorization flow.

### Universal connectors

- The [HTTP connector](/en/developing-connectors/http-v2) allows you to work with any API that supports HTTP connectivity. The HTTP connector works with a variety of auth models, content types, and HTTP methods.
- The [OpenAPI universal connector](/en/connectors/openapi/) can be used to work with any application that describes its API endpoints using the OpenAPI specification.
- The [GraphQL universal connector](/en/connectors/graphql) enables you to query and mutate records from any application that supports the GraphQL API.
- The [SOAP universal connector](/en/connectors/soap) lets you connect to any web service through the use of WSDL descriptions.

### Connector SDK

The [connector SDK](/en/developing-connectors/sdk) is a developer framework for developing a connector. You can choose to share the connectors you build with other Workato users, or submit your code via the Developers Program to make your connector public to all Workato users.

---
