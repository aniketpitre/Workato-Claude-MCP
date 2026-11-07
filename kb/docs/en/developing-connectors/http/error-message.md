---
url: 'https://docs.workato.com/en/developing-connectors/http/error-message.md'
description: >-
  Learn how the Workato HTTP connector surfaces enriched error data, including
  HTTP status, structured messages, response headers, and body.
---

# HTTP error handling

The HTTP connector surfaces enriched error data that helps you identify, manage, and resolve issues when a request fails. It displays the HTTP status, a standardized error message, and structured response details such as headers and body. These details improve clarity and support automation. This feature currently applies to the HTTP connector.

## How to view the error message

The connector raises an error when the [Send request](/en/developing-connectors/http/building-http-action) action receives a non-2xx response.

The job report's **Error** tab displays the following:

- A structured error message
- HTTP response status
- Response headers
- Response body (when applicable)

Each value appears in a dedicated field. You can use these in Monitor blocks, logs, or other error-handling logic.

![HTTP connector error datapills for Monitor and On error blocks.](/assets/http-error-datapills.DmjW08Oo.png)_HTTP connector error datapills for Monitor and On error blocks._

## Error structure

The HTTP connector includes the following fields in job errors:

| Field | Description |
| --- | --- |
| `error_type_id` | Stable identifier for the error type. For example: `err.http.response.client_error.not_found`. |
| `error_type` | Display name based on HTTP status. For example: `404 Not Found`. |
| `error_id` | Unique identifier for the error instance. |
| `error_message` | High-level message. For example, `HTTP 500 error`. |
| `http_response.code` | Numeric HTTP status code. For example: `404`. |
| `http_response.status_text` | HTTP status text. For example: `Not Found`. |
| `http_response.headers` | HTTP response headers. |
| `http_response.body` | HTTP response body as a string. |

> **AVOID PARSING ERROR TEXT**
> 
> Avoid parsing `error_message` or `error_type` values for automation. These fields are display values and may change.
> 
> Use `error_type_id` or `http_response.code` for reliable programmatic checks. The `error_type_id` field provides a stable identifier aligned with Workato’s error taxonomy.

### HTTP error categories

The HTTP connector raises an error for non-2xx responses. This includes 3xx HTTP redirection errors, 4xx client errors, and 5xx server errors.

HTTP errors returned by the connector follow structured `error_type_id` patterns based on HTTP status code classes. This structured catalog of HTTP error type IDs is currently supported only by the HTTP connector.

| HTTP status class | `error_type_id` prefix | Description |
| --- | --- | --- |
| 3xx | `err.http.response.redirection.*` | Redirection responses, such as `301 Moved Permanently`, `302 Found`, or `304 Not Modified`. |
| 4xx | `err.http.response.client_error.*` | Client-side errors, such as `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, or `404 Not Found`. |
| 5xx | `err.http.response.server_error.*` | Server-side errors, such as `500 Internal Server Error`, `502 Bad Gateway`, or `503 Service Unavailable`. |

You can use `error_type_id` prefixes in **Monitor** or **On error** blocks to group related HTTP failures.

The **Retry succeeds** column indicates whether the same request may succeed if the recipe retries the request without modifying the parameters. This applies to the following tables in this section.

#### HTTP redirection error type IDs

The HTTP connector returns the following `error_type_id` values for HTTP 3xx responses:

| HTTP status | `error_type_id` | Retry succeeds |
| --- | --- | --- |
| 300 Multiple Choices | `err.http.response.redirection.multiple_choices` | No |
| 301 Moved Permanently | `err.http.response.redirection.moved_permanently` | No |
| 302 Found | `err.http.response.redirection.found` | No |
| 303 See Other | `err.http.response.redirection.see_other` | No |
| 304 Not Modified | `err.http.response.redirection.not_modified` | No |
| 305 Use Proxy | `err.http.response.redirection.use_proxy` | No |
| 306 Unused | `err.http.response.redirection.unused` | No |
| 307 Temporary Redirect | `err.http.response.redirection.temporary_redirect` | No |
| 308 Permanent Redirect | `err.http.response.redirection.permanent_redirect` | No |

#### HTTP client error type IDs

The HTTP connector returns the following `error_type_id` values for HTTP 4xx responses:

| HTTP status | `error_type_id` | Retry succeeds |
| --- | --- | --- |
| 400 Bad Request | `err.http.response.client_error.bad_request` | No |
| 401 Unauthorized | `err.http.response.client_error.unauthorized` | No |
| 402 Payment Required | `err.http.response.client_error.payment_required` | No |
| 403 Forbidden | `err.http.response.client_error.forbidden` | No |
| 404 Not Found | `err.http.response.client_error.not_found` | No |
| 405 Method Not Allowed | `err.http.response.client_error.method_not_allowed` | No |
| 406 Not Acceptable | `err.http.response.client_error.not_acceptable` | No |
| 407 Proxy Authentication Required | `err.http.response.client_error.proxy_authentication_required` | No |
| 408 Request Timeout | `err.http.response.client_error.request_timeout` | Yes |
| 409 Conflict | `err.http.response.client_error.conflict` | No |
| 410 Gone | `err.http.response.client_error.gone` | No |
| 411 Length Required | `err.http.response.client_error.length_required` | No |
| 412 Precondition Failed | `err.http.response.client_error.precondition_failed` | No |
| 413 Content Too Large | `err.http.response.client_error.content_too_large` | No |
| 414 URI Too Long | `err.http.response.client_error.uri_too_long` | No |
| 415 Unsupported Media Type | `err.http.response.client_error.unsupported_media_type` | No |
| 416 Range Not Satisfiable | `err.http.response.client_error.range_not_satisfiable` | No |
| 417 Expectation Failed | `err.http.response.client_error.expectation_failed` | No |
| 418 I'm a teapot | `err.http.response.client_error.i_m_a_teapot` | No |
| 421 Misdirected Request | `err.http.response.client_error.misdirected_request` | No |
| 422 Unprocessable Content | `err.http.response.client_error.unprocessable_content` | No |
| 423 Locked | `err.http.response.client_error.locked` | Yes |
| 424 Failed Dependency | `err.http.response.client_error.failed_dependency` | No |
| 425 Too Early | `err.http.response.client_error.too_early` | Yes |
| 426 Upgrade Required | `err.http.response.client_error.upgrade_required` | No |
| 428 Precondition Required | `err.http.response.client_error.precondition_required` | No |
| 429 Too Many Requests | `err.http.response.client_error.too_many_requests` | Yes |
| 431 Request Header Fields Too Large | `err.http.response.client_error.request_header_fields_too_large` | No |
| 451 Unavailable For Legal Reasons | `err.http.response.client_error.unavailable_for_legal_reasons` | No |

#### HTTP server error type IDs

The HTTP connector returns the following `error_type_id` values for HTTP 5xx responses:

| HTTP status | `error_type_id` | Retry succeeds |
| --- | --- | --- |
| 500 Internal Server Error | `err.http.response.server_error.internal_server_error` | Yes |
| 501 Not Implemented | `err.http.response.server_error.not_implemented` | No |
| 502 Bad Gateway | `err.http.response.server_error.bad_gateway` | Yes |
| 503 Service Unavailable | `err.http.response.server_error.service_unavailable` | Yes |
| 504 Gateway Timeout | `err.http.response.server_error.gateway_timeout` | Yes |
| 505 HTTP Version Not Supported | `err.http.response.server_error.http_version_not_supported` | No |
| 506 Variant Also Negotiates | `err.http.response.server_error.variant_also_negotiates` | No |
| 507 Insufficient Storage | `err.http.response.server_error.insufficient_storage` | Yes |
| 508 Loop Detected | `err.http.response.server_error.loop_detected` | No |
| 510 Not Extended | `err.http.response.server_error.not_extended` | No |
| 511 Network Authentication Required | `err.http.response.server_error.network_authentication_required` | No |

#### Successful HTTP response codes treated as errors

The HTTP connector may treat certain successful HTTP responses as errors for backward compatibility.

These responses use successful HTTP status codes but may still surface as errors in the HTTP connector.

| HTTP status | `error_type_id` |
| --- | --- |
| 208 Already Reported | `err.http.response.successful.already_reported` |
| 226 IM Used | `err.http.response.successful.im_used` |

#### Unsupported RFC HTTP response codes

The HTTP connector may return fallback `error_type_id` values when it receives an HTTP status code that doesn't map to a supported RFC-defined response code. These identifiers represent unsupported or non-standard HTTP response codes:

| Category | `error_type_id` |
| --- | --- |
| Informational (1xx) | `err.http.response.unsupported_rfc.informational` |
| Successful (2xx) | `err.http.response.unsupported_rfc.successful` |
| Redirection (3xx) | `err.http.response.unsupported_rfc.redirection` |
| Client error (4xx) | `err.http.response.unsupported_rfc.client_error` |
| Server error (5xx) | `err.http.response.unsupported_rfc.server_error` |
| General | `err.http.response.unsupported_rfc.general` |

## Structured HTTP error output

The HTTP connector returns a structured error object you can use for debugging, filtering, and automation. This object includes fields such as the HTTP status code, response body, headers, and a machine-readable error type ID. For example:

```json
{
  "error_type_id": "err.http.response.client_error.not_found",
  "error_type": "Not Found",
  "error_id": "ad6a...b3c",
  "error_message": "HTTP 404 error",
  "http_response": {
    "code": 404,
    "status_text": "Not Found",
    "body": "{\"error\": \"Resource not found\"}",
    "headers": {
      "Content-Type": "application/json"
    }
  }
}
```

You can access this structured error data through the following:

- Job reports
- Monitor blocks (error datapills)
- On error blocks (error datapills)

Workato recommends using `error_type_id` for automation. This field is stable and supports reliable programmatic checks.

## Best practices for error handling

Use `error_type_id` and `http_response` fields in Monitor or On error blocks to build reliable recipes:

- Catch and handle specific errors using `error_type_id`
- Retry requests based on HTTP status codes or response headers
- Send structured error data to logs or alerting systems

These fields eliminate the need for string parsing or fragile pattern matching.

---
