# Security and governance

41 pages. Paths are relative to the repository root.


## Security and governance

- **Virtual Private Workato** - `kb/docs/en/cloud-hosting-editions/hosting-editions.md` - Virtual Private Workato (VPW) is a dedicated, isolated AWS environment offering the highest level of security and data protection for regulated industries.
- **Data center overview** - `kb/docs/en/datacenter/datacenter-overview.md` - Choose the cloud region where Workato stores and processes your automation data to meet legal and regulatory compliance needs.
- **Security** - `kb/docs/en/security.md` - Explore Workato security features for access and authentication, data protection, and best practices that give you control over key security controls.
- **Data retention policies** - `kb/docs/en/security/data-protection/data-retention.md` - Learn how Workato data retention policies set the lifespan of job histories, trigger events, and reports, and how to customize them.
- **Encryption key management** - `kb/docs/en/security/data-protection/encryption-key-management.md` - Learn how Workato encrypts data at rest and in transit using a multi-level key hierarchy with encryption keys unique to each workspace.
- **Private connectivity** - `kb/docs/en/security/data-protection/private-connectivity.md` - Learn about Workato private connectivity options, including AWS PrivateLink, Azure Private Link, the on-prem agent, and Virtual Private Workato.
- **Secrets Management For Connection Credentials** - `kb/docs/en/security/data-protection/secrets-management/secrets-management.md` - Learn how external secrets management lets Workato store and retrieve connection credentials like passwords and API tokens from a secrets manager.
- **IP allowlists FAQs** - `kb/docs/en/security/ip-allowlist-faqs.md` - Answers to common questions about adding Workato IP addresses to allowlists for databases, firewalls, and on-premise gateways.
- **IP allowlists** - `kb/docs/en/security/ip-allowlists.md` - Add Workato IP addresses to your allowlist to secure traffic, with the IP ranges for each data center and example configurations.
- **Security compliance** - `kb/docs/en/security/security-compliance.md` - Learn about the security compliance frameworks Workato maintains, including PCI-DSS Level 1, ISO 27001, and ISO 27701.
- **Security FAQs** - `kb/docs/en/security/security-faqs.md` - Answers to common questions about Workato security, including access and authentication, password policies, and data protection.

## Connection credentials

- **Secrets management for connection credentials - registering an application with Microsoft Entra ID** - `kb/docs/en/security/data-protection/secrets-management/azure-key-vault-app-registration.md` - Register an application in the Microsoft Entra admin center so Workato can retrieve secrets from your Azure Key Vault on your behalf.
- **Set up a Google Cloud service account** - `kb/docs/en/security/data-protection/secrets-management/google-service-account-setup.md` - Learn how to create a Google Cloud service account and generate the JSON key file Workato needs to connect to Google Secret Manager.
- **Set up HashiCorp Vault policies** - `kb/docs/en/security/data-protection/secrets-management/hashicorp-vault-policies.md` - Set up a HashiCorp Vault policy that grants Workato read access to your secrets engine configuration and the secrets you plan to use.
- **Secrets management for connection credentials - IAM Role-based Authentication for AWS Services** - `kb/docs/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws.md` - Use IAM role-based authentication to grant Workato scoped access to AWS services without sharing AWS security credentials.
- **Secrets management for connection credentials - setting up Amazon Web Services Secrets Manager for projects** - `kb/docs/en/security/data-protection/secrets-management/setting-up-project-level-aws-secrets-manager.md` - Set up AWS Secrets Manager at the project level to scope connection credentials and IAM roles to individual Workato projects.
- **Set up project-level Azure Key Vault secrets management** - `kb/docs/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault.md` - Set up Azure Key Vault for project-level secrets management to scope connection credentials to individual Workato projects.
- **Setting up project-level CyberArk Conjur secrets** - `kb/docs/en/security/data-protection/secrets-management/setting-up-project-level-cyberark-conjur.md` - Set up CyberArk Conjur for project-level secrets management to scope connection credentials to individual Workato projects.
- **Set up Google Secret Manager for a project** - `kb/docs/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager.md` - Learn how to set up Google Secret Manager at the project level in Workato.
- **Set up project-level Hashicorp Vault secrets** - `kb/docs/en/security/data-protection/secrets-management/setting-up-project-level-hashicorp-vault-secrets-engine.md` - Set up HashiCorp Vault KV secrets engines for project-level secrets management to scope connection credentials to individual Workato projects.
- **Secrets Management For Connection Credentials - Setting Up Amazon Web Services Secrets Manager for workspaces** - `kb/docs/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager.md` - Set up AWS Secrets Manager at the workspace level to manage connection credentials for your Workato account from one secrets manager.
- **Set up workspace-level Azure Key Vault secrets management** - `kb/docs/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault.md` - Set up Azure Key Vault for workspace-level secrets management to manage connection credentials across your Workato account.
- **Set up workspace-level CyberArk Conjur secrets** - `kb/docs/en/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur.md` - Set up CyberArk Conjur for workspace-level secrets management to manage connection credentials across your Workato account.
- **Set up Google Secret Manager for your workspace** - `kb/docs/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager.md` - Learn how to set up Google Secret Manager at the workspace level in Workato.
- **Set up workspace-level Hashicorp Vault secrets** - `kb/docs/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine.md` - Set up HashiCorp Vault KV secrets engines for workspace-level secrets management to manage connection credentials across your Workato account.
- **Secrets Management For Connection Credentials - Using Amazon Web Services Secrets In Connections** - `kb/docs/en/security/data-protection/secrets-management/using-aws-secrets-in-connections.md` - Configure Workato connections using secrets stored in your AWS Secrets Manager vault, with workspace-level or project-level connections.
- **Use Azure Key Vault secrets in connections** - `kb/docs/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections.md` - Configure Workato connections using secrets from Azure Key Vault, with workspace-level or project-level connections.
- **Use CyberArk Conjur secrets in connections** - `kb/docs/en/security/data-protection/secrets-management/using-cyberark-conjur-in-connections.md` - Configure Workato connections using secrets from CyberArk Conjur Cloud or self-hosted Conjur Enterprise.
- **Use Google Secret Manager secrets in connections** - `kb/docs/en/security/data-protection/secrets-management/using-google-secret-manager-in-connections.md` - Learn how to reference secrets stored in Google Secret Manager in your Workato connections.
- **Using HashiCorp Vault Secrets in connections** - `kb/docs/en/security/data-protection/secrets-management/using-hashicorp-secrets-in-connections.md` - Configure Workato connections using secrets from your HashiCorp Vault KV secrets engine with AppRole authentication.

## Data retention

- **Data retention - recipe-level data retention** - `kb/docs/en/security/data-protection/data-retention/configure-retention-for-recipes.md` - Configure the Jobs data retention setting at the recipe level in Workato to control whether job data is stored for individual recipes.
- **Data Retention FAQs** - `kb/docs/en/security/data-protection/data-retention/data-retention-faqs.md` - Answers to common questions about Workato data retention, including default periods, affected data types, and customizing retention.

## Encryption key management

- **Encryption key management - Enterprise Key Management** - `kb/docs/en/security/data-protection/encryption-key-management/enterprise-key-management.md` - Learn how Workato Enterprise Key Management lets you control your workspace encryption keys by bringing your own key through a KMS.
- **Enterprise Key Management - glossary** - `kb/docs/en/security/data-protection/encryption-key-management/glossary.md` - Reference for Workato Enterprise Key Management terms, including Customer Main Key, connection key, data key, and bring your own key.
- **Enterprise key management - connecting Amazon Key Management Service (KMS) to Workato EKM** - `kb/docs/en/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service.md` - Set up AWS Key Management Service with Workato Enterprise Key Management to bring your own encryption keys and meet compliance needs.
- **Enterprise key management - configuring Workato EKM with a custom key** - `kb/docs/en/security/data-protection/encryption-key-management/guides/setting-up-custom-kms-key.md` - Configure Workato Enterprise Key Management with a custom key by generating your own encryption key and using it to set up EKM.
- **Enterprise Key Management Troubleshooting** - `kb/docs/en/security/data-protection/encryption-key-management/troubleshooting.md` - Reference for Workato Enterprise Key Management errors, including causes, symptoms, and steps to resolve key management issues.

## Private connectivity

- **AWS PrivateLink** - `kb/docs/en/security/data-protection/private-link-aws.md` - Configure AWS PrivateLink to create a private connection between the Workato cloud and an AWS VPC, keeping traffic off the public internet.
- **Azure Private Link** - `kb/docs/en/security/data-protection/private-link-azure.md` - Configure Azure Private Link to create a private connection between the Workato cloud and an Azure virtual network, isolated from the public internet.

## Supported cloud regions

- **China data center** - `kb/docs/en/datacenter/cn-data-center.md` - Feature availability and operational considerations for Workato's China (CN) data center, hosted on AWS China (Ningxia) Region.

## Virtual Private Workato

- **VPW FAQs** - `kb/docs/en/cloud-hosting-editions/hosting-editions-faq.md` - Find answers to common questions about Virtual Private Workato (VPW), including access, regional availability, pricing, and who should use it.
