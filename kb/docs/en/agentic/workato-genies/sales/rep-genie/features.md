---
url: 'https://docs.workato.com/en/agentic/workato-genies/sales/rep-genie/features.md'
description: >-
  Core and extended features for Sales Rep Agent, from post-call CRM updates and
  account research through CRM self-service, alerts, and knowledge retrieval.
---

# Sales Rep Agent features

Sales Rep Agent works across the deal lifecycle, from research before a call to CRM updates and post-call monitoring. This page describes the core features available in every deployment and the extended features you can enable.

## Core features

Core features run from chat requests, scheduled jobs, and events in your connected systems.

### Call completion workflow

Sales Rep Agent performs the following actions after each call:

- Retrieves the recording and transcript from your call recording application
- Summarizes the conversation against the selling methodology fields your organization tracks
- Shows you the fields it plans to change and updates the opportunity after you approve
- Logs a note and creates a follow-up task, if enabled
- Suggests relevant case studies
- Drafts a follow-up email and sends it after you approve it, if enabled

### Account research and Customer 360

A single request pulls data from every system your organization has configured and returns a single account summary.

Sales Rep Agent can also prepare this research ahead of upcoming customer meetings without being asked. Refer to [Proactive pre-meeting research](/en/agentic/workato-genies/sales/rep-genie/how-it-works#proactive-pre-meeting-research) for details.

### CRM self-service operations

You can query, create, and update CRM records in conversation. Sales Rep Agent finds the record, asks a clarifying question when a request matches more than one, shows you the change it plans to make, and applies it only after you confirm.

Sales Rep Agent inherits your existing CRM permissions and can't access records you can't already access yourself.

### CRM alerts and notifications

Sales Rep Agent evaluates opportunities against alert rules you configure and notifies the rep through their chat interface when a record meets a condition. An alert that goes unaddressed escalates to a recipient you configure. Rules cover conditions such as a deal stalled in one stage, a close date that has passed, and a required field left blank for the current stage.

### Knowledge base retrieval

Sales Rep Agent answers questions from your connected knowledge bases, including battlecards, product documentation, and case studies.

Sales Rep Agent logs any question it can't answer from the knowledge base and sends admins a weekly digest of the gaps. Refer to [Knowledge gap logging](/en/agentic/workato-genies/sales/rep-genie/how-it-works#knowledge-gap-logging) for details.

## Extended features

Extended features are optional. Enable them after initial setup.

### Knowledge ingestion

Sales Rep Agent syncs sales content, documentation, and historical ticket and request data from connected source systems into its knowledge base. Ingestion supports full and delta loads. It stores content in the knowledge base only and doesn't create or modify records in the source system.

The following sources are available for knowledge ingestion:

- Confluence
- Freshdesk
- Gong
- Google Drive
- Jira Service Desk
- Microsoft SharePoint
- Salesforce
- Salesforce Service Cloud
- Slack

### Custom skills

The **Core** folder is read-only and managed by Workato. You can use skills in the **Extensions** folder as-is or clone them into **Custom Extensions** to customize them. Build your own skills in **Custom Extensions**.

---

---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/sales/rep-genie/how-it-works.md
description: >-
  Learn how Sales Rep Agent processes calls, gathers account research, applies
  CRM changes, evaluates alert rules, and organizes its project folders.
---

# How Sales Rep Agent works

This page explains how Sales Rep Agent processes completed calls, gathers account research, applies CRM changes, evaluates alert rules, and organizes its project folders.

## How the call completion workflow works

When a call ends, Sales Rep Agent retrieves the recording and transcript from the application set in the **CallRecording.Application** project property. Calls shorter than the **Minimum.Call.Duration** threshold are skipped.

It then summarizes the transcript against the fields in the **Agentic Selling Methodology Fields | Definition** data table. Each row specifies a Salesforce field, its associated object, and the criteria to assess how thoroughly the transcript addresses that field. The same workflow supports a MEDDPICC deployment and a value-selling deployment without changes to the skills.

Sales Rep Agent presents a before-and-after comparison of the proposed field updates for the rep to review, then updates the Salesforce opportunity once the rep approves the changes.

It then creates the following records based on the enabled project properties:

| Project property | When enabled, Sales Rep Agent creates |
| --- | --- |
| **PostCall.Create.Note** | A note on the opportunity. |
| **PostCall.Create.Tasks** | A follow-up task. |
| **PostCall.Send.Email** | A follow-up email, sent after the rep approves the draft. |

## How account research works

Sales Rep Agent reads your project properties to determine which applications your organization has configured, then routes each part of the research to the matching connected application. You don't specify which systems to check or in what order.

Each configured system contributes a different part of the account picture:

| System | Contribution |
| --- | --- |
| **CRM** | Account summary, related contacts, contracts, and cases. |
| **IT service management (ITSM) application** | Open and high-priority issues tied to the account, narrowed by the filters in the **JiraServiceDesk.filters** project property. |
| **Document repository** | Related internal documentation and notes. |
| **Customer support platform** | Support tickets matching the company name, narrowed by your configured filters. |
| **Enrichment platform** | External company details such as industry, size, and key personnel. |
| **Call recording application** | Summaries of recent calls with the account. |
| **Calendar application** | Upcoming and past meetings associated with the account. |
| **Knowledge base** | Articles relevant to the account or its industry. |
| **Web search** | Recent news mentions. |

Sales Rep Agent merges these results into one summary.

### Proactive pre-meeting research

Sales Rep Agent can prepare account research before customer meetings without being asked. It checks each covered rep's Google Calendar and, for each meeting with an external attendee, identifies the customer's company and prepares account research for that rep.

- **Schedule**: Set by the **FetchEvents.Interval** project property.
- **Covered reps**: Reps in the **Agentic SalesExecutives** data table with **is\_active** set to `TRUE`.
- **External attendee**: An attendee whose email domain differs from the **Domain** project property.

The following limits apply to proactive research:

- Only Google Calendar is supported.
- Only meetings with Zoom conferencing are included.
- Meetings with no external attendee are ignored.

## How CRM self-service operations work

Sales Rep Agent first searches the CRM for the record you referred to, which can be an account, contact, lead, opportunity, or task. It asks which record you meant instead of guessing when a request matches more than one, such as two opportunities with similar names.

Sales Rep Agent shows you the exact change it plans to make and waits for your confirmation before it creates or changes anything. You can correct a wrong record or a wrong value before it reaches the CRM. It applies the change and returns a direct link to the record after you confirm.

Sales Rep Agent acts with your own CRM permissions. It can search, read, summarize, create, and update records. It has no skills that delete, archive, cancel, merge, or unassign anything.

## How CRM alerts work

Three independent processes generate alerts, and none of them requires a prompt from a user:

- **Scheduled checks**: On the cron schedule set in the **CRM.Health.Time.Interval** project property, Sales Rep Agent reviews your opportunities and leads against the alert rules configured by your administrator. Each alert type has its own trigger recipe, and the agent sends an alert for every record that meets a rule.
- **Real-time stage-change checks**: An opportunity's stage change in Salesforce triggers an immediate check of fields required at the new stage, instead of waiting for the next scheduled check.
- **Email monitoring**: Sales Rep Agent watches incoming email and links messages related to an opportunity to the right record.

### Supported alert types

Administrators enable each alert type and set its threshold in the **Agentic Opportunity | Alert Configurations** data table. Enter the alert type exactly as shown below.

| Alert type | Applies to | When it fires |
| --- | --- | --- |
| **IncomingEmail** | Opportunity | An email related to the opportunity has arrived. |
| **DealStuck** | Opportunity | The opportunity has stayed in its current stage longer than the configured number of days. |
| **MissingFields** | Opportunity | Fields required for the opportunity's current stage are empty. Checked on a schedule and also as soon as the stage changes. |
| **OverDueCloseDate** | Opportunity | The opportunity's close date has passed and the opportunity is still open. |
| **RenewalOpportunityCloseDate** | Renewal opportunity | The renewal opportunity's close date is within the configured number of days. |
| **InactiveLead** | Lead | The lead has had no activity for longer than the configured number of days. |

### How stage change checks work

The **TRIGGER | \[Salesforce\] Start Genie Process for Opportunity Stage Change** recipe watches Salesforce for updated opportunities and acts only when the update is a stage change. It then:

- Looks up the active **MissingFields** rules for the opportunity's new stage in the **Agentic Opportunity | Alert Configurations** table.
- Checks each required field in those rules on the opportunity.
- For each empty field, collects the opportunity, account and owner details, and sends a **MissingFields** alert to the right people.
- Records the alert, so the cooldown and escalation rules below apply to it.

If the recipe hits an error it can't recover from, it notifies the configured administrator with the error details.

### Delivery, escalation, and cooldown

Alerts arrive through Sales Rep Agent's chat interface. If an alert isn't addressed within the rule's **EscalationThreshold**, Sales Rep Agent escalates it to the **EscalationRecipients**.

Two settings limit how often alerts repeat:

- **NotifyOnFirstInstance**: Controls whether Sales Rep Agent notifies on a record's first appearance against a rule.
- **SnoozeDays**: Sets the number of days before the same rule can notify again for the same record.

## How knowledge retrieval works

Sales Rep Agent answers questions from the knowledge bases added to it. Knowledge ingestion syncs content from each source system at the frequency set in the **Agentic Data Ingestion | Scheduler** data table.

### Knowledge gap logging

Sales Rep Agent records any question it can't answer in the **Agentic KB Gap User Conversations** data table. Each row holds the conversation ID, the user, the question they asked, the response it gave, a category, and a **Not in KB** flag. Sales Rep Agent sets **Not in KB** to `TRUE` when it can't resolve the request, including when no knowledge base article matches, a skill fails after a retry, or the request stays ambiguous after a clarifying question.

Sales Rep Agent sends the admins listed in the **KBGap.digest.admins** project property a weekly digest of the questions it couldn't answer in the previous seven days. To close a gap, add or update the content in the source system, run ingestion again, then ask the same question to confirm Sales Rep Agent now answers it.

## Folder structure

The Sales Rep Agent project is organized into the following top-level folders:

- **Config**: Connections and metadata required to run Sales Rep Agent.
- **Core**: Foundational skills maintained by Workato. You can't modify or clone these skills.
- **Extensions**: Additional app skills and functions maintained by Workato and updated during release cycles. You can use these as-is or as a reference when you build custom integrations.
- **Custom Extensions**: Custom assets that you maintain. Clone Extension assets into this folder before you modify them. Assets in this folder remain intact across upgrades.
- **Runtime Data**: Data tables that store the data Sales Rep Agent generates during runtime.

View folder structure

```text
Agentic | Sales Rep Agent
├── Config
│   ├── Metadata
│   └── Connections
├── Core
│   ├── Apps
│   │   ├── Confluence
│   │   ├── Freshdesk
│   │   ├── Gmail
│   │   ├── Gong
│   │   ├── Google Calendar
│   │   ├── Jira Service Desk
│   │   ├── Salesforce
│   │   ├── Zoom
│   │   └── ZoomInfo
│   ├── Functions
│   └── Skills
├── Extensions
│   ├── Apps
│   │   ├── Freshdesk
│   │   ├── Google Calendar
│   │   ├── Jira Service Desk
│   │   └── Salesforce
│   ├── Functions
│   ├── Knowledge Ingestion
│   │   ├── Confluence
│   │   ├── Freshdesk
│   │   ├── Gong
│   │   ├── Google Drive
│   │   ├── Jira Service Desk
│   │   ├── Salesforce
│   │   ├── Salesforce Service Cloud
│   │   ├── Sharepoint
│   │   └── Slack
│   └── Skills
├── Custom Extensions
└── Runtime Data
```

> **CORE AND EXTENSIONS ARE MANAGED BY WORKATO**
> 
> Don't modify the skills, functions, or data table schemas in the **Core** and **Extensions** folders. Make all customizations in **Custom Extensions**.

### Working with Extensions and Custom Extensions

You can activate Extension skills and add them to Sales Rep Agent as-is. You can also clone them into **Custom Extensions** to customize them or build support for apps that aren't available in the **Extensions** folder.

Customizations in **Custom Extensions** are isolated from platform updates and remain intact across upgrades. You can't clone or modify core skills.

---
