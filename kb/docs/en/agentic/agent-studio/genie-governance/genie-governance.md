---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/genie-governance/genie-governance.md
description: >-
  Learn how genie governance addresses identity, behavioral manipulation, and
  PII exposure across the layers of an enterprise Agent Studio deployment.
---

# Genie governance

Enterprise genie deployments have three distinct security concerns. Each concern is addressed at a different layer of the build.

- **[Identity](/en/agentic/agent-studio/genie-governance/establish-user-identity)**: Genies often take actions on behalf of users, such as creating records, retrieving personal data, and submitting requests. These actions require a verified user identity. Identity established from conversation text isn't trustworthy. A user can claim any name, role, or email address in a chat message, and an LLM often accepts it. Identity derived from the authenticated platform context can't be forged. This distinction is the foundation of every other security control.
  
- **[Behavioral manipulation](/en/agentic/agent-studio/genie-governance/behavioral-manipulation)**: LLMs are designed to follow instructions. This characteristic also makes them susceptible to adversarial instructions. Threats include prompt injection attempts embedded in documents the genie processes, social engineering through role-play requests, authority claims intended to unlock elevated access, and incremental scope expansion that pushes the genie toward prohibited behavior. The job description is where these threats are addressed, through explicit security safeguards, a clear definition of permitted and prohibited actions, and response templates that redirect rather than engage with manipulation attempts.
  
- **[PII data exposure](/en/agentic/agent-studio/genie-governance/pii-anonymization-patterns)**: Personally identifiable information (PII) appears throughout enterprise data, including names, email addresses, national IDs, health data, and financial details. Genies retrieve, process, and stores this data, which passes through the LLM. This raises a compliance question for many organizations: should PII reach the LLM at all? The answer depends on the use case and the organization's regulatory obligations. Controls for managing PII operate at three distinct layers and can be applied independently or in combination.
