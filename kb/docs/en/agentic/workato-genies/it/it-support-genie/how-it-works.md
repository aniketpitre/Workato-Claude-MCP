---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/it/it-support-genie/how-it-works.md
description: >-
  Learn how IT Support Genie processes requests, runs its multi-tier approval
  workflow, validates identity actions, manages groups, and organizes its
  project folders.
---

# How IT Support Genie works

This page explains how IT Support Genie processes requests, runs approvals, validates identity actions, manages groups, and organizes its project folders.

## Request processing

When a user sends a message through their chat interface, IT Support Genie identifies what the user is asking for and either answers from the knowledge base, creates a ticket, or starts a workflow such as access provisioning or a password reset. It validates the requester's identity and scope before taking any action.

## How approvals work

When a user requests access to an application, IT Support Genie creates an entry in the **App Access Provisioning Events** data table. This entry starts the approval workflow configured for the application.

You define the approval levels per application in **Config > Metadata > Application Approvers**. Each application supports up to three sequential approval levels, and you can enable or disable each level independently. Each level also supports multiple approvers. The 2nd approver and admin approver fields in Application Approvers accept a comma-separated list of emails, so more than one person can act at a given level. Whichever approver responds first determines the outcome for that level: their decision is final, and any decision submitted afterward by another approver at the same level is disregarded.

The request goes to the first level. The workflow moves to the next enabled level only after the current level approves. When every enabled level has approved, IT Support Genie provisions access automatically or routes the request for manual provisioning, depending on the application's processing type.

If any approver rejects the request, the workflow stops immediately and the user is notified. No further escalation occurs. The **Approval.TimedOutDefaultAction** project property sets the outcome when a request expires without a decision.

> **DEFAULT ACTION**
> 
> If an application has no approval configuration in the **Application Approvers** table, IT Support Genie applies the action set in the **Approval.TimedOutDefaultAction** project property. The recommended value is `REJECTED`, which prevents access from being provisioned unless an approval path is configured.

IT Support Genie uses the **Access Provisioning Approvals** data table in **Runtime Data** as a shared audit trail. It tracks status, assignee, event ID, and rejection reasons for every decision.

## How password management works

IT Support Genie validates every password reset, account unlock, MFA reset, and account details request before taking action. It checks the requester's identity against the authorized admin channel configured in the **Application Approvers** data table to determine whether they're an authorized user or an administrator. Authorized users can act only on their own account, while administrators and helpdesk members can act on behalf of any user. A request for an admin-only action from an unauthorized requester is blocked, and the requester is notified that it's unauthorized. Other requests that can't be completed are routed to ticket creation.

## How group management works

IT Support Genie manages group memberships through Google Workspace.

All users can perform read operations, such as searching for and listing groups. Creating groups and adding or removing members are restricted to authorized IT administrators.

## Folder structure

The IT Support Genie project is organized into the following top-level folders:

- **Config**: Connections and metadata required to run IT Support Genie.
- **Core**: Foundational skills maintained by Workato. You can't modify or clone these skills.
- **Extensions**: Additional app skills and functions maintained by Workato and updated during release cycles. You can use these as-is or as a reference when you build custom integrations.
- **Custom Extensions**: Custom assets that you maintain. Clone Extension assets into this folder before you modify them. Assets in this folder remain intact across upgrades.
- **Runtime Data**: Data tables that store the data IT Support Genie generates during runtime.

View folder structure

```text
Agentic | IT Support Genie
├── Config
│   ├── Connections
│   └── Metadata
├── Core
│   ├── Access Provisioning
│   │   ├── Entra ID
│   │   └── Okta
│   ├── Approval Workflow
│   │   └── Functions
│   ├── Password Management
│   │   ├── Entra ID
│   │   └── Okta
│   ├── Group Management
│   │   └── Google Workspace
│   ├── Ticketing
│   │   ├── Jira Service Desk
│   │   └── ServiceNow
│   ├── User Feedback
│   └── Reporting
├── Extensions
│   ├── App Events
│   ├── Knowledge Ingestion
│   │   ├── Confluence
│   │   ├── Jira Service Desk
│   │   ├── Google Drive
│   │   └── ServiceNow
│   └── Functions
├── Custom Extensions
│   └── Knowledge Ingestion
└── Runtime Data
```

> **CORE AND EXTENSIONS ARE MANAGED BY WORKATO**
> 
> Don't modify the skills, functions, or data table schemas in the **Core** and **Extensions** folders. Make all customizations in **Custom Extensions**.

### Working with Extensions and Custom Extensions

You can activate Extension skills and add them to IT Support Genie as-is. You can also clone them into **Custom Extensions** to customize them or build support for apps that aren't available in the **Extensions** folder.

Customizations in **Custom Extensions** are isolated from platform updates and remain intact across upgrades. You can't clone or modify core skills.
