---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/it/it-support-genie/features.md
description: >-
  IT Support Genie's core and extended features, from query deflection and
  access provisioning through password and group management.
---

# IT Support Genie features

IT Support Genie answers common IT questions and automates helpdesk workflows across your connected systems. This page describes the core features available in every deployment and the extended features you can enable.

## Core features

Core features support the full IT support workflow, from answering questions and ticketing through access provisioning, approvals, and identity management.

### Query deflection

IT Support Genie answers common IT questions from a knowledge base. Automated responses reduce the number of tickets that reach your IT team.

### Ticketing

When IT Support Genie can't find an answer in the knowledge base, it creates a request in your connected ticketing application. Jira Service Desk and ServiceNow are supported.

### Access provisioning

IT Support Genie provisions application access through your SSO provider after the configured approvals complete. You define which applications and license levels are available, along with the identifiers your identity provider uses to grant them.

### Multi-tier approval

IT Support Genie routes provisioning requests through up to three sequential approval levels that you enable independently per application. The workflow supports escalation, timeouts, and default actions, and maintains a full audit trail of every decision.

### Password management

IT Support Genie performs identity management actions through Microsoft Entra ID and Okta. Users can reset their password, unlock their account, and reset their MFA factors on their own account. Authorized IT administrators and helpdesk members can perform these actions, plus account detail retrieval, on behalf of any user.

### Group management

IT Support Genie manages group memberships through Google Workspace. All users can search for and list groups. Only authorized IT administrators can create groups or add and remove group members.

## Extended features

Extended features are optional and can be enabled after initial setup.

### Knowledge ingestion

IT Support Genie syncs IT policies, runbooks, documentation, and historical ticket data from connected source systems into its knowledge base. Ingestion supports full and delta loads to keep the knowledge base up to date. Ingestion stores content in the knowledge base only. It doesn't create or modify records in the source system.

IT Support Genie currently supports Confluence, Google Drive, Jira Service Desk, and ServiceNow as knowledge ingestion sources.

### Custom skills

You can extend IT Support Genie with custom skills built in the **Custom Extensions** folder. The **Core** folder is read-only and managed by Workato. You can use skills in the **Extensions** folder as-is or clone them into **Custom Extensions** for customization.
