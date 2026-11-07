---
url: 'https://docs.workato.com/en/connectors/hubspot/scopes.md'
description: >-
  Configure scopes for HubSpot Custom OAuth profiles in Workato so requested
  scopes match the HubSpot app and connections succeed without errors.
---

# Scopes for Custom OAuth profiles

The scopes you define in Workato must either match or be a subset of the scopes that admins configure in the HubSpot app. This ensures a successful connection between Workato and HubSpot using Custom OAuth profiles. Scope mismatches can cause HubSpot connection setup errors. This [additional security measure](https://developers.hubspot.com/changelog/advanced-auth-and-scope-settings-for-public-apps) is required by HubSpot since October 21, 2024.

Workato users can select scopes in **Advanced settings** during [connection setup](/en/connectors/hubspot#connection-setup). These scopes are requested when establishing the HubSpot connection.

Admins [configure scopes](/en/connectors/hubspot/custom-oauth) in the `auth` object of their HubSpot app's `app-hsmeta.json` file. Refer to HubSpot's [Scopes](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/scopes) documentation to learn more about the scope types available to public apps.

## Configuration approaches

Admins can use one of the following approaches to configure scopes in HubSpot. The approach you choose depends on whether you're configuring scopes for internal users or if you're a Workato Embedded partner serving customers.

> **REQUIRED SCOPE**
> 
> The following scope is required for all connections, regardless of your configuration approach. You must add this scope to the `requiredScopes` array in your HubSpot app:
> 
> `crm.objects.contacts.read`
> 
> HubSpot also requires the `oauth` scope for apps that use OAuth. Add it to the `requiredScopes` array alongside `crm.objects.contacts.read`. Add all other scopes to the `optionalScopes` array.

### Use default scopes and add more on demand

You can use the default scopes and assign additional scopes on demand when required. This approach is common for admins that work with users who won't adjust scopes in **Advanced settings** when connecting to HubSpot from Workato.

The connection can be established with no errors as long as no one on your team adjusts the scopes. If someone adjusts scopes during the connection setup, the connection fails with an error. In this case, you must contact the HubSpot admin who can request that the HubSpot Custom OAuth app owner adds the new scope. Alternatively, you can contact Workato support. You can't establish a connection to HubSpot until the scopes are in sync.

Admins should add the following scopes as optional in HubSpot, as they are requested by Workato's connection by default:

Workato default scopes

- `crm.lists.read`
- `crm.lists.write`
- `crm.objects.companies.read`
- `crm.objects.companies.write`
- `crm.objects.contacts.write`
- `crm.objects.deals.read`
- `crm.objects.deals.write`
- `crm.objects.owners.read`
- `crm.schemas.companies.read`
- `crm.schemas.companies.write`
- `crm.schemas.contacts.read`
- `crm.schemas.contacts.write`
- `crm.schemas.deals.read`
- `crm.schemas.deals.write`

### Principle of least privilege

The principle of least privilege approach is suitable if you're an admin and can configure a HubSpot Custom OAuth app in accordance with security best practices. This approach isn't suitable for Embedded partners who plan for their customers to connect to HubSpot using the profile.

Admins work with users to identify the relevant triggers and actions in the connector. Admins use this input to select and mark the appropriate scopes as optional in the HubSpot OAuth app. Users configure their HubSpot connection in Workato using the same scopes after the app is updated. This setup ensures access stays limited to only the required data and prevents users from viewing HubSpot information outside their roles.

### All scopes

Admins must configure all available scopes as optional when using the all scopes approach. This eliminates potential connection errors when users configure additional scopes during the connection setup. Refer to the following list of optional scopes:

## Full list of scopes

The following list of scopes are available for users to choose when configuring a HubSpot connection in Workato:

- `accounting`
- `account-info.security.read`
- `actions`
- `analytics.behavioral_events.send`
- `automation`
- `automation.sequences.enrollments.write`
- `automation.sequences.read`
- `behavioral_events.event_definitions.read_write`
- `business_units_view.read`
- `business-intelligence`
- `cms.domains.read`
- `cms.domains.write`
- `cms.functions.read`
- `cms.functions.write`
- `cms.knowledge_base.articles.publish`
- `cms.knowledge_base.articles.read`
- `cms.knowledge_base.articles.write`
- `cms.knowledge_base.settings.read`
- `cms.knowledge_base.settings.write`
- `cms.membership.access_groups.read`
- `cms.membership.access_groups.write`
- `cms.performance.read`
- `collector.graphql_query.execute`
- `collector.graphql_schema.read`
- `communication_preferences.read`
- `communication_preferences.read_write`
- `communication_preferences.statuses.batch.read`
- `communication_preferences.statuses.batch.write`
- `communication_preferences.write`
- `content`
- `conversations.custom_channels.read`
- `conversations.custom_channels.write`
- `conversations.read conversations.write`
- `conversations.visitor_identification.tokens.create`
- `crm.dealsplits.read_write`
- `crm.export`
- `crm.import`
- `crm.lists.read`
- `crm.lists.write`
- `crm.objects.appointments.read`
- `crm.objects.appointments.write`
- `crm.objects.carts.read`
- `crm.objects.carts.write`
- `crm.objects.commercepayments.read`
- `crm.objects.companies.read`
- `crm.objects.companies.write`
- `crm.objects.contacts.write`
- `crm.objects.courses.read`
- `crm.objects.courses.write`
- `crm.objects.custom.read`
- `crm.objects.custom.write`
- `crm.objects.deals.read`
- `crm.objects.deals.write`
- `crm.objects.feedback_submissions.read`
- `crm.objects.goals.read`
- `crm.objects.goals.write`
- `crm.objects.invoices.read`
- `crm.objects.invoices.write`
- `crm.objects.leads.read`
- `crm.objects.leads.write`
- `crm.objects.line_items.read`
- `crm.objects.line_items.write`
- `crm.objects.listings.read`
- `crm.objects.listings.write`
- `crm.objects.marketing_events.read`
- `crm.objects.marketing_events.write`
- `crm.objects.orders.read`
- `crm.objects.orders.write`
- `crm.objects.owners.read`
- `crm.objects.partner-clients.read`
- `crm.objects.partner-clients.write`
- `crm.objects.products.read`
- `crm.objects.products.write`
- `crm.objects.quotes.read`
- `crm.objects.quotes.write`
- `crm.objects.services.read`
- `crm.objects.services.write`
- `crm.objects.subscriptions.read`
- `crm.objects.subscriptions.write`
- `crm.objects.users.read`
- `crm.objects.users.write`
- `crm.pipelines.orders.read`
- `crm.pipelines.orders.write`
- `crm.schemas.appointments.read`
- `crm.schemas.appointments.write`
- `crm.schemas.carts.read`
- `crm.schemas.carts.write`
- `crm.schemas.commercepayments.read`
- `crm.schemas.companies.read`
- `crm.schemas.companies.write`
- `crm.schemas.contacts.read`
- `crm.schemas.contacts.write`
- `crm.schemas.courses.read`
- `crm.schemas.courses.write`
- `crm.schemas.custom.read`
- `crm.schemas.custom.write`\*
- `crm.schemas.deals.read`
- `crm.schemas.deals.write`
- `crm.schemas.invoices.read`
- `crm.schemas.invoices.write`
- `crm.schemas.line_items.read`
- `crm.schemas.listings.read`
- `crm.schemas.listings.write`
- `crm.schemas.orders.read`
- `crm.schemas.orders.write`
- `crm.schemas.quotes.read`
- `crm.schemas.services.read`
- `crm.schemas.services.write`
- `crm.schemas.subscriptions.read`
- `crm.schemas.subscriptions.write`
- `ctas.read`
- `e-commerce`
- `external_integrations.forms.access`
- `files`
- `files.ui_hidden.read`
- `forms`
- `forms-uploaded-files`
- `hubdb`
- `integration-sync`
- `marketing-email`
- `marketing.campaigns.read`
- `marketing.campaigns.revenue.read`
- `marketing.campaigns.write`
- `media_bridge.read`
- `media_bridge.write`
- `sales-email-read`
- `scheduler.meetings.meeting-link.read`
- `settings.billing.write`
- `settings.currencies.read`
- `settings.currencies.write`
- `settings.security.security_health.read`
- `settings.users.read`
- `settings.users.teams.read`
- `settings.users.teams.write`
- `settings.users.write`
- `social`
- `tax_rates.read`
- `tickets`
- `timeline`
- `transactional-email`

> **AVAILABLE SCOPES**
> 
> \* The `crm.schemas.custom.write` scope is not available by default. If you require this scope for your integration, you can request access to [HubSpot's Custom Objects Schema pilot program](https://developers.hubspot.com/custom-objects-schema-pilot).

---
