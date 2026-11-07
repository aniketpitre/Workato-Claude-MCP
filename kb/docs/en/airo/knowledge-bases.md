---
url: 'https://docs.workato.com/en/airo/knowledge-bases.md'
description: >-
  AIRO uses your workspace assets and Workato platform knowledge to answer
  questions.
---

# What AIRO knows

AIRO uses multiple knowledge sources to provide accurate, context-aware assistance when answering questions and building automation:

- [Company-specific knowledge](#company-specific-knowledge)
- [Workspace asset knowledge](#workspace-asset-knowledge)
- [Workato documentation](#workato-documentation)
- [Product updates](#product-updates)

## Company-specific knowledge

Company-specific knowledge includes your organization's policies, standards, and best practices. AIRO references your uploaded documents when answering questions to ensure that responses reflect your compliance, security, and operational requirements.

You can upload any documentation that describes how your organization operates. Common categories include:

| Category | Examples |
| --- | --- |
| Standard Operating Procedures | Business processes, guidelines, approval workflows, integration best practices, API management documentation |
| Compliance & Governance | Data security standards (PII handling, encryption), regulatory compliance (GDPR, HIPAA, SOX, ISO 27001), asset review and approval requirements |
| Security Policies | Credential/secrets management, key rotation, incident response protocols, escalation paths, user permissions, RBAC, least-privilege access policies |
| Technical Standards | Data integration patterns (batch, real-time, event-driven), recommended architectures (microservices, APIs, data lakes), data retention policies |
| Reuse & Standardization | Catalogs of reusable templates, recipes, connectors, assets, and guidelines for reuse and standardization (COE enforcement) |

Supported file formats include CSV, DOC, DOCX, and PDF. The maximum file size is 25 MB per file.

AIRO prioritizes company-specific knowledge over general Workato documentation when the two conflict.

Refer to [AIRO Playbooks](/en/airo/knowledge/manage) to upload, preview, and delete playbooks.

## Workspace asset knowledge

AIRO automatically understands your existing assets within your current environment, including recipes, connections, genies, Workflow apps, and more. This knowledge helps AIRO suggest improvements to existing automations and recommend reusable components when building new solutions.

**Example queries:**

- `Explain the recipes in this project.`
- `What Salesforce connections do I have?`
- `Which recipes are using the ServiceNow connector?`

## Workato documentation

AIRO references the complete [Workato documentation](/en/) to answer questions about features, connectors, best practices, and integration patterns. This foundational knowledge supports platform questions and provides guidance on using Workato capabilities.

**Example queries:**

- `How do I split a string into an array?`
- `How do I connect to an on-prem database?`
- `How do I transform a datetime to show only month and year?`
- `What's the best way to handle errors in recipes?`

## Product updates

AIRO stays current with the latest Workato features and changes through the [platform changelog](https://www.workato.com/product-hub/changelog/). This ensures AIRO can provide accurate information about recent releases, new capabilities, and platform improvements.

**Example queries:**

- `Tell me about updates to the NetSuite connector in the last 3 months.`
- `What connectors have been updated recently?`
- `Are there any breaking changes I should know about?`

---
