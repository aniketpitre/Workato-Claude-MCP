---
url: >-
  https://docs.workato.com/en/connectors/openapi/guides/setting-up-the-openapi-connector.md
description: >-
  Install and set up an OpenAPI connector in Workato, including providing a
  Swagger file and configuring authentication and connection fields.
---

# Setting Up The OpenAPI Connector

In this guide, we'll walk you through installing and setting up an OpenAPI connector in your Workato account.

> **INFO**
> 
> Refer to the [Using OpenAPI connector to create custom connectors guide](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors) if you want to fully customize your connector.

* * *

## Requirements

To set up an OpenAPI connection, you'll need:

- **Privileges in Workato that allow you to create connections.**
  
- **A Swagger file that**:
  
  - Conforms to the OpenAPI v2 or v3 [specifications](https://swagger.io/specification/v3/)
  - Is valid JSON or YAML
  
  **Note**: We recommend using the connector with [RESTful APIs](https://restfulapi.net/). Refer to the [Limitations section in the OpenAPI overview](/en/connectors/openapi/#limitations) for more info.
  

* * *

## Step 1: Install The Connector

The first step is to install the connector in your Workato account:

1. Open [the connector in the community library](https://app.workato.com/custom_adapters/50046/details?community=true).
   
2. Click **Install connector**.
   
3. Click **Release latest version**.
   

* * *

## Step 2: Configure The Connection In Workato

- [Step 2.1: Provide The OpenAPI Document](#provide-api-definition)
- [Step 2.2: Define The Authentication Settings](#define-auth)
- [Step 2.3: Define Server And Testing URLs](#define-server-testing-urls)
- [Step 2.4: Customize The Interface](#customize-interface)

### Step 2.1: Provide The OpenAPI Document

In this step, you'll provide the Swagger file containing the API definition.

How you accomplish this is dependent on whether the file is publicly accessible on the internet:

My file is publicly accessible

If the Swagger file is publicly accessible:

1. Select **Document URL** as the **OpenAPI document source**.
   
2. In the **Document URL** field, paste the document URL to the file.
   

**Note**: Files are only downloaded and parsed at recipe design time. When recipes are run - or when OpenAPI actions are executed - the file won't be downloaded.

My file is not publicly accessible

If the Swagger file isn't hosted or isn't publicly accessible, you can copy and paste the file into Workato:

1. Select **Download content** as the **OpenAPI document source**.
   
2. In the **Document content** field, paste the contents of the file.
   

### Step 2.2: Define The Authentication Settings

Next, you'll define the authentication method for the connection. Learn more about the supported authentication methods [in the OpenAPI overview guide](/en/connectors/openapi/guides/authentication).

Select the method you're using from the **Authentication Method** menu.

### Step 2.3: Define Server And Testing URLs

Next, you'll define the server and testing URLs for the connector:

- **Server URL**: Enter the URL to the application's target host or service, including the `https://`. This is the base URL for requests sent by the connector. For example: `https://api.example.com`
  
  Relative endpoint paths from the [API definition](#provide-api-definition) will be appended to this URL to construct the full endpoint URL.
  
- **Test Request URL**: Enter the relative path of an API endpoint that Workato can use to verify the connection. This path will be appended to the **Server URL** to construct a full endpoint URL for testing. For example: `/user/profile`
  
  Connections are successful when the API responds with a `2XX` status code.
  

For example: A **Server URL** of `https://api.example.com` and a **Test Request URL** of `/users/profile` creates a full request URL of: `https://api.example.com/users/profile`

### Step 2.4: Customize The Interface

The OpenAPI connector automatically generates the user interface based on the content of the provided [Swagger file](#provide-api-definition). The following elements can be customized to improve the user experience:

- Object names
- Object hints
- Field names
- Field hints
- Links to external documentation
- API operation grouping
- Fields to ignore

Check out the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces) for more info and examples.

* * *

## Step 3: Test The Connection

When finished configuring the connection, click **Connect** to save and test the connection.
