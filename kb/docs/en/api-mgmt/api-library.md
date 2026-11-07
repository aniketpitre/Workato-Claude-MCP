---
url: 'https://docs.workato.com/en/api-mgmt/api-library.md'
description: >-
  The API library is a centralized catalog where users in your workspace
  discover, document, and test shared API collections with auto-generated
  OpenAPI specs.
---

# API Library

The API library is a centralized catalog of API collections that are discoverable by other users in your organization. Here, users can discover the documentation, examples, and tools that they need to successfully adopt your API.

The library includes the following key features:

- **Automatic documentation:** OpenAPI specs are automatically generated for all your API collections. Users can browse and use it with their preferred tool.
- **Swagger testing tool:** API collections in the library are displayed with Swagger UI, which displays the sample request and response data, and enables users to make test calls to the endpoints.
- **Workspace-based sharing:** Make use of your role-based access settings to securely share APIs with people in your workspace.
- **Access control**: Users can view and test the endpoints in shared API collections; to consume actual data, users must request and receive permission from the API publisher.

![API library](/assets/api-library.lnbJ5ia0.png)_API library with shared collections_

## Sharing API collections

API collections aren't available in the library by default. To share a collection, go to **API collection > Settings > Sharing** and click **Show in API library**. ![API collection > Settings > Sharing > Show in API library](/assets/api-library-enable-sharing.CYkGbH5A.png)_API collections sharing tab_

## Gaining access to APIs in the library

Users who have access to the API platform can browse the shared collections in the library. Each collection page contains the OpenAPI spec file, a Swagger UI where users can see sample request and response data, and test the endpoints.

To consume the API, click **Request access** in the upper right corner and optionally provide a reason. The request is sent to the API publisher as an email.

---
