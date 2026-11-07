---
url: 'https://docs.workato.com/en/api-mgmt/api-collections/download-openapi.md'
description: >-
  Download an OpenAPI 3.0 or 2.0 spec for a Workato API collection to document
  all endpoints and use them with tools like Postman.
---

# Download OpenAPI spec

Each API collection page includes a **Download OpenAPI spec** link.

![Download OpenAPI spec](/assets/download-openapi-spec.BuC7IrnQ.png)_Download OpenAPI spec_

Video guide: How to build APIs faster with OpenAPI

[Video](https://www.youtube.com/embed/-cMqdgCw724)

This link provides a downloadable file that documents all endpoints in the collection using the OpenAPI format, also known as Swagger, which is compatible with tools like Postman.

Workato exports API specifications in [OpenAPI version 3.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md) by default. Workato also supports [OpenAPI version 2.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md) to maintain compatibility with older tools. Add the query parameter `oas_ver=2` to the download URL to export a version 2.0 specification. For example:

```html
https://app.workato.com/doc/service/collection-name/swagger?api_group_id=123456&token=token-value&oas_ver=2
```

---
