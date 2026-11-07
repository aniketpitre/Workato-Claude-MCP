---
url: 'https://docs.workato.com/en/faq-api-developer-portal-changes.md'
description: >-
  Find answers about the Workato API developer portal launch, the new API client
  and key model, and the deprecation timeline for legacy API clients.
---

# API developer portal updates

The [API developer portal](/en/api-mgmt/api-developer-portal#api-developer-portal) launches on February 24, 2025. This portal provides a more intuitive and powerful experience for developers and API consumers.

This update enhances API discovery, security, and management while introducing [API client and API key model](/en/api-mgmt/api-client-mgmt) (formerly API access profiles). Workato has also updated the developer APIs and embedded APIs that manage API clients and keys.

The legacy API portal remains available until **August 1, 2025**, and legacy API clients and access profiles are supported until **July 1, 2026**. After this date, Workato will fully deprecate legacy API clients, access profiles, and associated tokens.

## What's changing?

### API client and API key model

The [API clients and API keys model](/en/api-mgmt/api-client-mgmt) consolidates access control at the API client level. API keys inherit client settings, which enables faster provisioning and self-service key management. Workato has released updated [developer APIs](/en/workato-api/api-platform#api-platform) and [embedded APIs](/en/oem/oem-api/api-platform#api-platform) to support this model. We recommend that you use this model for all future API clients and integrations.

### Legacy API clients and access profiles

You can create and modify legacy API clients and access profiles until **December 1, 2025**. After this date, you can't modify existing configurations or create new legacy API clients and access profiles.

On **July 1, 2026**, Workato will fully deprecate legacy API clients and access profiles. After this date, access tokens associated with legacy profiles will no longer be valid.

### Deprecation of the legacy API portal

The API developer portal replaces the [legacy API portal](/en/api-mgmt/api-portal), which is accessible through the client URL on the API clients page. The legacy portal remains available until **August 1, 2025**, after which it will no longer be accessible.

## What you need to do

You must [create new API clients](/en/api-mgmt/api-client-mgmt#create-new-client) to access the API developer portal. Legacy API clients aren't compatible with the API developer portal. You should plan to transition before **August 1, 2025**, to access enhanced capabilities and prevent disruptions. Until then, legacy API clients can continue using the existing client URL.

Refer to the [Configure the developer portal](/en/api-mgmt/api-developer-portal#configure-api-developer-portal) to set up and use the API developer portal.

We recommend that you migrate to the API client and API key model before **July 1, 2026**, when Workato deprecates legacy access profiles and tokens.

---
