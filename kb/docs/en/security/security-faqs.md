---
url: 'https://docs.workato.com/en/security/security-faqs.md'
description: >-
  Answers to common questions about Workato security, including access and
  authentication, password policies, and data protection.
---

# Security FAQs

Get answers to frequently asked questions (FAQs) about security.

## What is Workato's approach to security?

View answer

Workato has a comprehensive approach to [security](/en/security), including a complete security program with documented policies and procedures, verified by an annual audit, secure development and testing, a secure and scalable infrastructure, and product capabilities that enhance security.

## Where can I find an overview of Workato's security practices?

View answer

Our [Workato Security Overview page](https://www.workato.com/legal/security) provides an overview of Workato's security practices.

## What are the essential features associated with access and authentication in Workato?

View answer

Workato offers the following [access and authentication features](/en/security#access-and-authentication):

- [Password policy enforcement](/en/security#password-policy-enforcement)
- [Session timeout](/en/security#session-timeout)
- [Two-factor authentication](/en/security#two-factor-authentication)
- [Organizational separation](/en/security#organizational-separation)
- [Separation of development, production, and testing environments](/en/security#separation-of-environments)
- [IP allowlists](/en/security#ip-allowlists)
- [TLS and HTTP standards](/en/security#tls-http-standards)
- [Single sign-on (SSO) using SAML 2.0 authentication](/en/security#sso-using-saml-2-0-authentication)

## How does Workato enforce password policies?

View answer

Workato enforces [password](/en/security#password-policy-enforcement) length, complexity, and expiration standards for user accounts. Workato does not store passwords and only stores secure hashes of passwords in our database.

Clients using password authentication are required to rotate their passwords every 90 days. Workato prohibits password reuse to further safeguard accounts.

## How can organizations configure session timeouts in Workato?

View answer

Organizations can set a [session timeout duration](/en/security#session-timeout) according to their security needs. The default session timeout duration is seven days, but it can be configured to range from 15 minutes to 14 days, depending on the organization’s security policy.

Users can update their timeout duration by navigating to **Workspace admin > Settings > General > Session timeout duration**.

## What two-factor authentication options are supported by Workato?

View answer

Workato supports the following [two-factor authentication](/en/security#two-factor-authentication) mobile apps:

- Google Authenticator
- Microsoft Authenticator
- Authy

## How does Workato ensure organizational separation within its platform?

View answer

Admins can [configure separate workspaces](/en/security#organizational-separation) for different teams or business functions. This ensures that users can only access the resources of the workspace to which they are assigned.

## What does "separation of environments" in Workato mean?

View answer

Workato supports a multi-phase development lifecycle, allowing development, testing, and production activities to occur in [separate environments](/en/security#separation-of-environments) and by different users. The Environments feature is available to customers on specific pricing plans.

## What single sign-on (SSO) options does Workato support?

View answer

Workato supports integration with third-party SAML-compliant SSO systems and offers single sign-on using third-party credentials. Refer to the [SSO documentation](/en/user-accounts-and-teams/single-sign-on) for a complete list of SSO options.

## How does Workato handle user provisioning and authorization to minimize data exposure?

View answer

Workato follows the [principle of least privilege](/en/security#user-provisioning-and-authorization) through a role-based access control (RBAC) model when provisioning system access.

Workspace admins use RBAC to manage access by assigning [environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) and [project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) based on collaborators' responsibilities. You can also create [custom roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#custom-roles) to control access to specific features, projects, folders, and tools at a granular level.

## How does Workato handle connections to external systems securely?

View answer

When connecting to [external systems](/en/security#connecting-to-external-systems), Workato uses OAuth 2.0 whenever possible. If credentials must be stored, they are encrypted using a 256-bit key. Custom OAuth profiles can be created for greater control.

## How is data protected within Workato?

View answer

All [data](/en/security#data-protection) stored in Workato is encrypted in transit and at rest using a strong encryption algorithm (AES-256). Data retention, data masking, and data privacy measures are in place to protect sensitive information.

Workato stores transaction-related data for a limited period based on the Workato plan, allowing system activity visibility, testing, debugging, and support for long-running transactions.

## Can Workato employees see my recipe data or job details?

View answer

No. Workato employees, including engineers, do not have access to your recipe job details, data, or execution logs, even if a job ID or URL is shared.

Shared job and recipe IDs are primarily used for troubleshooting and debugging within our internal platform logs, where error information is stored. Access to recipe and job data is strictly controlled and remains within your environment.

All data in Workato is encrypted in transit and at rest. Encrypted data cannot be accessed by Workato staff.

## How is encryption key management handled in Workato?

View answer

Workato uses a hierarchical key model for [encryption key management](/en/security#data-encryption) with different levels of keys to limit access and exposure. The Customer Main Key (CMK) is at the top of the hierarchy.

## Can Workato's encryption keys be managed using third-party services?

View answer

Workato supports [Enterprise Key Management](/en/security/data-protection/encryption-key-management/enterprise-key-management#enterprise-key-management) (EKM) that allows users to manage their workspace's encryption keys with the help of external key management services.

## What is the role of Secrets Management in Workato?

View answer

[Secrets Management](/en/security/data-protection/secrets-management/setting-up-project-level-aws-secrets-manager) allows you to securely store and retrieve sensitive information like passwords and API tokens. It centralizes credential management, improving security and ease of management.

Workato's Secrets Management feature supports the following secrets managers:

- AWS Secrets Manager
- HashiCorp Vault
- Azure Key Vault

You can configure secrets management at either the workspace or project level in Workato. Workato does not support a mixed approach to secrets management.

## What security compliance standards does Workato comply with?

View answer

Workato maintains the following security compliance frameworks:

- **PCI-DSS v4.0.1 − Level 1**: Secure cardholder data.
- **ISO 27001, 27701 & 42001**: Information, privacy, and AI management aligned with global standards.
- **SOC 1 Type II, SOC 2 Type II, and SOC 3**: Audited controls for financial and security integrity.
- **HIPAA**: Healthcare data protection, with Business Associate Agreements (BAAs) available.
- **IRAP**: Strict cybersecurity standards aligned to Australian government requirements.
- **NIST 800-171A r2**: Controlled Unclassified Information (CUI) protection for federal contractors, partners, and subcontractors.

Refer to [Security compliance frameworks](/en/security/security-compliance) for more information.

---
