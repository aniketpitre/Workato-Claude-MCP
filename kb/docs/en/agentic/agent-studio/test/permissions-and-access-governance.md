---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/test/permissions-and-access-governance.md
description: Learn about test mode user access and governance.
---

# Test mode permissions and access governance

Test mode differs from the production genie. Skills in test mode run against real connected systems unless you configure the recipe to use non-production connections. A test session that triggers a write skill can write to production systems. Test mode access allows users to execute skills outside standard user access controls, including actions against production systems.

## Test mode user access

Grant test mode access based on the following guidelines:

- **Active builders**: Grant access to genies that builders actively build or maintain. Use test mode for development tasks such as testing job description changes, validating skill behavior, debugging conversation patterns, and verifying new functionality before promotion to production.
- **Genie owners conducting quality assurance testing**: Grant access to genie owners who validate behavior before changes go live. Limit access to the genies they own. Clearly state that test mode can trigger real skill executions.

Don't grant test mode access in the following cases:

- **End users**: End users interact with the production genie through the chat interface. Test mode allows users to conduct conversations that trigger skills outside standard access controls, including unauthorized write operations.
- **Builders who are no longer actively working on a genie**: Test mode access for inactive builders represents unnecessary risk. Remove test mode access when a builder transitions off a project or leaves the organization.
- **Stakeholders reviewing the genie before go-live**: Test mode isn't a preview environment for stakeholders. Use the production genie with a pilot user group for stakeholder preview instead.

## Test mode and production system risk

Test mode can impact production systems. It uses real skill connections unless you configure those connections to use non-production systems. Test mode doesn't isolate changes from production, unlike a sandbox environment.

Test mode access allows users to perform write operations without standard user confirmation and approval flows enforced by the production genie. These operations include ticket creation, record updates, leave submissions, and access provisioning.

You can mitigate this risk using the following practices:

- **Configure test-time connection overrides where possible**: Configure the development environment to use non-production connections if the skill supports environment-specific connections. Test mode sessions in the development environment execute against staging systems rather than production.
  
- **Document production-impacting skills**: Document which skills execute against production systems in test mode. Treat test mode runs as production operations when testing against production systems.
  
- **Track and clean up changes**: Track all records created or modified during test runs. Clean up these changes after testing completes.
  

> **POTENTIAL PRODUCTION SYSTEM IMPACT**
> 
> Skills in test mode use the connection configured in the recipe. A test conversation that triggers a write skill can write to the production system. Verify connection configuration before running test scenarios that invoke write operations.

## Governance considerations

Apply the following governance practices to test mode access controls:

- **Document access decisions**: Document who has access, why you granted access, and when you granted it. Use this documentation to support periodic access reviews and audits.
- **Review access quarterly**: Access can become outdated over time. Confirm that each user with test mode access is still an active builder for the relevant genie.
