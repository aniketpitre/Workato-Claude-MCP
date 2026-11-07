---
url: 'https://docs.workato.com/en/agentic/workato-genies/it/license-genie.md'
description: >-
  License Genie helps IT and finance teams identify underutilized software
  licenses, coordinate approvals, and reduce software costs.
---

# License Genie

License Genie helps IT and finance teams identify underutilized software licenses, coordinate approvals, and reduce software costs.

## What License Genie does

License Genie supports IT and finance teams across the license management lifecycle:

- **Identify license optimization opportunities**: License Genie analyzes user activity to surface low-engagement users who are candidates for license downgrade or removal. It supports applications managed through Okta and Microsoft Entra ID, and accepts manual usage uploads for applications without API access.
- **Govern and approve optimization events**: License Genie routes approval requests to the user, manager, and app admin before proceeding with license optimization actions.
- **Execute license optimization**: After approval, License Genie revokes or downgrades licenses through the connected application's API or through an SSO provider.

## Connected systems

License Genie integrates with your existing identity providers, applications, and notification channels, including:

- **Identity management**: Okta, Microsoft Entra ID
- **Optimized applications**:
  - **Included by default**: Salesforce, Gong, Zoom
  - **Available as [extensions](/en/agentic/workato-genies/it/license-genie/setup#extensions)**: SAP Concur, Coupa, Outreach, and more
- **Notification channels**: Slack, Microsoft Teams, Workato GO

---

---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/it/license-genie/features.md
description: >-
  Learn about the core and extended features in License Genie, including
  scheduled optimization, multi-tier approval workflows, and contract data
  extraction.
---

# License Genie features

License Genie automates license optimization across your connected apps. This page describes the features it provides, grouped into **core** capabilities that make up the optimization workflow and **extended** capabilities that add optional functionality.

## Core features

The following diagram shows how core features map to each stage of the workflow, from scheduling through approval and execution.

![Workflow diagram showing the stages of the License Genie optimization process.](/assets/diagram.D9Q6UtkE.png)_License Genie optimization workflow_

### Scheduler

License Genie runs on a configurable schedule that supports weekly (by weekday) or monthly (by date) cadences. You can set cadences independently per connected app. For example, you can have an Okta-managed Salesforce deployment that runs on the first of every month, while an Okta-managed Zoom deployment runs every Tuesday.

### License discovery

License Genie identifies underutilized licenses using API data from connected applications. You can configure inactivity thresholds per app, and extend support to additional apps.

### Downgrade detection

For Salesforce, Gong, and Zoom, License Genie analyzes usage activity to identify users on a higher license tier than they need. You can extend support to additional apps.

### Multi-tier approval

License Genie routes identified users through a multi-tier approval workflow before reclaiming a license. You can enable user, manager, and admin tiers independently:

- **User approval**: The user receives a notification. Approving reclaims the license; rejecting escalates the request to the manager, if enabled.
- **Manager approval**: The manager reviews requests escalated from the user. Approving reclaims the license. Rejecting ends the workflow and retains the license. A timeout escalates the request to the admin, if enabled.
- **Admin approval**: The admin acts as the final reviewer, or as the default tier when user and manager approval are both disabled.

If all tiers are disabled, License Genie applies the default action set in the `Approval.TimedOutDefaultAction` project property.

Approvers can handle all pending escalated requests in a single interaction. License Genie maintains a full audit trail of all approval actions.

### License optimization

After approval, License Genie either revokes or downgrades the license through the connected application's API or through an SSO provider such as Okta or Microsoft Entra ID. When an app requires manual processing, admins receive a notification to complete the action.

### Exclusion list

You can add users to an exclusion list to prevent them from being flagged during optimization. Exclusion lists are scoped per app and are checked before any user enters the approval workflow.

## Extended features

Extended features add optional capabilities to the core optimization workflow.

### Contract data extraction

License Genie uses intelligent document processing to extract license counts, SKUs, pricing, and contract dates from uploaded contract PDFs. The extracted data feeds directly into cost and license analysis.

### Manual upload of usage data

You can manually upload usage data as a CSV file for apps without a direct API integration. The uploaded data triggers the same discovery, approval, and optimization workflow as API-connected apps. For the upload steps, see [Manual upload of usage data](/en/agentic/workato-genies/it/license-genie/setup#manual-upload) in the setup guide.

> **CORE IS READ-ONLY**
> 
> Don't modify assets in the **Core** folder. Activate **Extensions** assets as-is, or clone them to **Custom Extensions** before customizing.

---

---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/it/license-genie/how-it-works.md
description: >-
  Learn how the approval workflow and license downgrade process in License Genie
  work, including folder structure and audit trail details.
---

# How License Genie works

This page explains how the License Genie approval and downgrade processes work, and describes the project's folder structure.

## How approvals work

The scheduler creates entries in the **License Optimization Events** data table (in **Runtime Data**) on a cadence you configure. The approval workflow triggers for each new entry. The workflow includes two skills: single user approval for individual requests, and bulk approval for processing multiple escalated requests at once. Both skills require explicit user confirmation before License Genie can take any action.

![Flowchart showing the License Genie approval escalation path from user to manager to admin, with outcomes for approvals, rejections, timeouts, and disabled tiers](/assets/how-approvals-work.BRKgp2ru.png)_License Genie approval workflow_

### Single user approval

Single user approval handles a license optimization request for an individual user:

- Approving reclaims the license.
- Rejecting escalates the request to their manager, if manager approval is enabled; otherwise it escalates to an admin.
- If both manager and admin approval are disabled, the user's decision is final.

If user approval is disabled entirely, License Genie skips this step and applies the configured default action.

**Approve**

![Animated walkthrough showing an approver confirming a license optimization request in License Genie](/assets/approve-license-optimization.CDgz88nU.gif)_Approving a license optimization request_

**Reject**

![Animated walkthrough showing a user rejecting a license optimization request in License Genie, triggering escalation to the manager](/assets/reject-license-optimization.Dp4rObty.gif)_Rejecting a license optimization request_

### Bulk approval

Bulk approval lets managers or admins handle all escalated requests in a single interaction rather than one at a time. A manager receives all pending approvals for their direct reports at once.

Both skills use the **License Optimization Approvals** data table (in **Runtime Data**) as a shared audit trail, tracking status, assignee, event ID, and rejection reasons across every decision.

## How downgrades work

The downgrade process follows four stages: detection, recommendation, approval, and execution.

### Detection

License Genie periodically analyzes usage data for licensed users in an application. It compares each user's activity against their current license tier to identify users who aren't using their full license.

### Recommendation

License Genie evaluates each detected user against the **Application License Inventory** and **License Optimization Events** data tables, which together provide available tiers, their hierarchy, and SSO group IDs. License Genie produces a list of eligible downgrade options for each user, showing the tiers available below the one currently assigned to them. **FUNC | License Downgrade Recommendation Engine** determines the appropriate target tier based on the configured hierarchy and rank.

### Approval

Each recommendation enters the approval workflow described in [How approvals work](#how-approvals-work). Execution begins after an approver confirms the downgrade.

### Execution

After approval, License Genie updates the user's license assignment by modifying their SSO group membership. It removes the user from the current tier group and adds them to the approved target tier group. Both group IDs are sourced from the **Application License Inventory** and **License Optimization Events** data tables. For apps that support provisioning through their own API without SSO, License Genie uses that path instead.

## Folder structure

The License Genie project is organized into the following top-level folders:

- **Config**: Connections and metadata required to run License Genie.
- **Core**: Foundational skills maintained by Workato. You can't modify or clone these skills.
- **Extensions**: Additional app skills and functions maintained by Workato and updated during release cycles. You can use these as-is or as a reference when you build custom integrations.
- **Custom Extensions**: Custom assets that you maintain. Clone Extension assets into this folder before you modify them. Assets in this folder remain intact across upgrades.
- **Runtime Data**: Data tables that store the data License Genie generates during runtime.

View folder structure

```text
Agentic | License Genie
├── Config
│   ├── Connections
│   └── Metadata
├── Core
│   ├── Approval Workflow
│   │   └── Functions
│   ├── Apps to Optimize
│   │   ├── Gong
│   │   ├── Microsoft Entra ID
│   │   ├── Okta
│   │   ├── Salesforce
│   │   └── Zoom
│   ├── Functions
│   ├── Reports
│   ├── Scheduler
│   ├── User Feedback
│   └── User Memory
├── Custom Extensions
│   └── Apps to Optimize
│       └── [App Name]
├── Extensions
│   ├── App Events
│   ├── Apps to Optimize
│   │   ├── Concur
│   │   ├── Coupa
│   │   ├── Manual
│   │   └── Outreach
│   ├── Contract License Data
│   ├── Entra ID License Data
│   ├── Functions
│   ├── Knowledge Ingestion
│   └── Salesforce License Data
└── Runtime Data
```

### Working with Extensions and Custom Extensions

You can activate Extension skills and add them to License Genie as-is. You can also clone them into **Custom Extensions** to customize them or build support for apps that aren't available in the **Extensions** folder.

Customizations in **Custom Extensions** are isolated from platform updates and remain intact across upgrades. You can't clone or modify core skills.

---
