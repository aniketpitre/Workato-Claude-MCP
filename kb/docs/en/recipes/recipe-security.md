---
url: 'https://docs.workato.com/en/recipes/recipe-security.md'
description: >-
  Follow security best practices for Workato recipes, including storing
  credentials in connections, using a secrets manager, and data masking.
---

# Security best practices for recipes

This page provides best practices for safeguarding sensitive information and maintaining compliance when creating recipes in Workato.

## Best practices for sensitive data management

Don't include sensitive data as plain text in recipe steps. This includes tokens, authentication keys, personal information like names, addresses, emails, or other private data.

Instead, use the following best practices:

- [Store authentication details in the connection](#store-authentication-details-in-the-connection)
- [Use a secrets manager](#use-a-secrets-manager)
- [Enable data masking](#enable-data-masking)

### Store authentication details in the connection

Don't hardcode authentication details, such as API tokens, in recipe steps.

For example, when you set the **Base URL** for an [HTTP connection](/en/developing-connectors/http/connection-setup), don't hardcode the token value in the URL:

```plaintext
https://www.myapp.com/services/api-method?token=3ababe3235Z2z
```

Instead, store the authentication token as a [query parameter](/en/developing-connectors/http/connection-setup#authentication-type-query-params) during connection setup.

**Recommended**

![Recommended](/assets/recommended.BdcN8Nx-.png)_Recommended: Store the authentication token as a query parameter_

**Not recommended**

![Not recommended](/assets/not-recommended.3zmvQmrr.png)_Not recommended: Hardcoding the token in the base URL_

### Use a secrets manager

Store sensitive data, such as API keys and tokens, in a supported [secrets manager](/en/security/data-protection/secrets-management/secrets-management).

![Store sensitive data in a secrets manager](/assets/add-external-secret-aws.BWQsU5qc.png)_Store sensitive data in a secrets manager_

Workato supports the following secrets managers:

- [AWS Secrets Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager)
- [Azure Key Vault](/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault)
- [CyberArk Conjur Secrets Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur)
- [Google Secret Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager)
- [HashiCorp Vault](/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine)

> **DON'T STORE SECRETS IN PROPERTIES**
> 
> We no longer recommend storing sensitive data in [environment properties](/en/features/account-properties) or [project properties](/en/features/project-properties) due to new property quotas.
> 
> Use a secrets manager instead for better scalability and security.

### Enable data masking

Use [data masking](/en/features/data-masking) to exclude sensitive information from the job report and recipe step output.

![Enable data masking](/assets/data-masking.Cd3okNzj.gif)_Enable data masking_

## Benefits

Using these best practices offers the following security benefits:

- **Enhanced security**: Sensitive data isn't visible to other users in your Workato workspace.
- **Safe cloning**: Sensitive data remains secure when recipes are cloned. Cloned recipes retain recipe steps while excluding project properties, environment properties, and dynamic data from datapills.
- **Centralized management**: Storing sensitive data centrally simplifies updates and reduces the risk of inconsistencies.
- **Community safety**: Sharing recipes publicly doesn't expose sensitive data.

## Sensitive data and compliance

Workato maintains the following security compliance frameworks:

- **PCI-DSS v4.0.1 − Level 1**: Secure cardholder data.
- **ISO 27001, 27701 & 42001**: Information, privacy, and AI management aligned with global standards.
- **SOC 1 Type II, SOC 2 Type II, and SOC 3**: Audited controls for financial and security integrity.
- **HIPAA**: Healthcare data protection, with Business Associate Agreements (BAAs) available.
- **IRAP**: Strict cybersecurity standards aligned to Australian government requirements.
- **NIST 800-171A r2**: Controlled Unclassified Information (CUI) protection for federal contractors, partners, and subcontractors.

We also encrypt data at rest and in transit.

However, users are responsible for ensuring that sensitive data is handled to meet organizational policies and regulatory requirements. This includes:

- Determining whether storing sensitive data in [Workato FileStorage](/en/features/workato-filestorage) or [Data tables](/en/data-tables) aligns with organizational policies and compliance needs.
- Applying appropriate access controls to restrict unauthorized access to sensitive data.

Examples of sensitive data to handle with caution include:

- Personal data subject to privacy laws and regulations
- Financial information
- Healthcare data

---
