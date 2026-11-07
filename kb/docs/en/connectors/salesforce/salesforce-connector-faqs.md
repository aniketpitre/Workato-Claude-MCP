---
url: 'https://docs.workato.com/en/connectors/salesforce/salesforce-connector-faqs.md'
description: >-
  Answers to frequently asked questions about the Salesforce connector in
  Workato, covering OAuth 2.0 and JWT authentication and connection setup.
---

# Salesforce connector FAQs

Get answers to frequently asked Salesforce connector questions.

What authentication method can I use to connect to Salesforce on Workato?

You can connect to Salesforce on Workato using either [OAuth 2.0 or JWT authentication](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato).

How do I configure an OAuth 2.0 connection for Salesforce on Workato?

To [configure an OAuth 2.0 connection](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato) for Salesforce, you must provide a unique connection name, specify if it's a Sandbox connection, and fill in the necessary fields. You must provide your Salesforce login credentials for OAuth 2.0 authorization.

What are the advanced settings for OAuth 2.0 Salesforce connections?

[Advanced settings for OAuth 2.0](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato) Salesforce connections are:

- Organization/community custom domain URL
- Requested permissions
- Verified user access configuration
- Custom OAuth profiles

Why does my Salesforce connection disconnect repeatedly?

Frequent, recurring disconnections that require manual reconnection are usually caused by a missing OAuth scope, an aggressive Refresh Token Policy, or an IP Relaxation setting blocking Workato's requests. Refer to [Salesforce connection disconnects repeatedly](/en/connectors/salesforce/troubleshoot-connection-setup#salesforce-connection-disconnects-repeatedly) to diagnose and resolve the issue.

What is JWT Bearer Authentication for Salesforce?

[JWT Bearer Authentication](/en/connectors/salesforce#jwt-bearer-authentication) allows you to create a connection without linking a specific user account. This process uses a digital certificate to sign the JWT request. You must have prior approval from the client app in Salesforce.

How do I configure a Salesforce JWT Bearer connection on Workato?

To [configure a Salesforce JWT Bearer connection](/en/connectors/salesforce#jwt-bearer-authentication), you must:

- Create a private key and digital certificate.
- Specify the issuer, subject, and Salesforce subdomain.

What permissions should the connected user have?

The connected user's profile must have API enabled, and [permissions](/en/connectors/salesforce#roles-and-permissions-required-to-connect) to interact with both standard and custom objects. It's essential to set up API-enabled permission, standard and custom object permissions, and platform event permissions for the user's profile.

The API-enabled permission allows access to the Salesforce API. This permission is located in **Setup > Profiles**.

Standard and custom object permissions in Salesforce allow users to interact with objects in Salesforce. The connected user's profile must have permissions for reading, writing, editing, deleting, and viewing standard or custom objects. This is necessary to avoid issues when working with records.

The connected user has the same permissions through the Workato Salesforce connector as in Salesforce.

What is field-level security in Salesforce?

[Field-level security](/en/connectors/salesforce#field-level-security) controls whether a user can see, edit, and delete specific fields on an object. This is essential for protecting sensitive data while allowing access to certain fields. Field-level security must be managed in profiles and permission sets.

Can I connect more than one Salesforce account in a single recipe?

Yes. You can connect up to two Salesforce accounts in a single recipe by using [Secondary connectors](/en/features/secondary-connectors).

---
