---
url: 'https://docs.workato.com/en/oauth2-format-faq.md'
description: >-
  Find answers about Workato OAuth 2.0 token request format enforcement, which
  malformed requests are rejected, and who is affected by the change.
---

# OAuth 2.0 format enforcement

## What is the update?

On **October 12th, 2022**, we are tightening the list of accepted format for OAuth 2.0 token request. With this change, we will formally reject malformed token requests.

## Who is affected?

1. This change may affect you or your clients using OAuth 2.0 authentication method. Find out if any of your access profiles use OAuth 2.0 by browsing the list of Clients in API Platform page.
   
2. This change will affect you or your clients if are sending malformed token requests today. Refer to this [list of accepted formats for token request](/en/api-mgmt/oauth2).
   

## Malformed token requests

This list of malformed requests are currently accepted, but will be rejected after the change.

| Content-Type | Basic header present? | client\_id & client\_secret | grant\_type | Reason |
| --- | --- | --- | --- | --- |
| Form | Yes (missing client id/secret) | Form payload | Form payload | If basic header is used, it must contain client ID and secret. |
| Form | Yes | Basic | JSON payload | `grant_type` format does not match `Content-Type`. |
| Form | No | JSON payload | JSON payload | Body format does not match `Content-Type`. |
| _Blank_ | No | Query string | Query string | Must have `Content-Type` & parameters in request payload. |
| JSON | No | JSON payload | Query string | If `Content-Type: application/json` is used, all parameters must be in payload. |
| JSON | Yes | Basic | Query string | If `Content-Type: application/json` is used, all parameters must be in payload. |

## How does this affect me?

If you or your clients have been submitting token requests according to this [list of accepted formats for token request](/en/api-mgmt/oauth2), there will be no disruption.

---
