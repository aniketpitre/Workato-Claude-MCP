---
url: 'https://docs.workato.com/en/apim-legacy-url-deprecation.md'
description: >-
  Answers to common questions about the Workato API Platform legacy URL
  deprecation, who is affected, and how to switch to current URLs.
---

# API Platform - Legacy URL deprecation

## What is the update?

Starting on **February 1st, 2023**, we will deprecate support for the API platform legacy URL. Requests to these endpoints will no longer be routed to your API recipe. These URLs use the format `https://www.workato.com/service/*`, followed by the unique API collection prefix.

## Who is affected?

This deprecation affects API clients that are actively using the legacy URL. You must use the current URLs, either `https://apim.workato.com/*` or your [API custom domain](/en/api-mgmt/custom-domain).

Workato lists the correct URL in your API Collection page.

## Do these clients need to change anything else?

Other than the URL, API clients do not have to change anything.

## How can my API clients test their application using the current URL before the deprecation date?

![API endpoint current URL](/assets/api_platform_current_url.Dgork1On.png)_API endpoint current URL_

The current URL can be found on the API endpoint page. We recommend that you share this URL with your clients immediately. They should begin switching and testing in advance of the deprecation date.

## What happens if my API clients do not switch to the current URLs after the deprecation?

API requests to the legacy URLs will be rejected with a 401 response code.

---
