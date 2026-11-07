---
url: 'https://docs.workato.com/en/agentic/workato-genies/it/edi-genie/features.md'
description: >-
  Learn about EDI Genie's core and extended features, including transaction
  retrieval, partner health monitoring, proactive alerts, and knowledge
  ingestion.
---

# EDI Genie features

EDI Genie provides conversational access to Orderful transaction data and proactive monitoring for EDI operations. This page describes the core features available in every deployment and the extended features you can enable.

## Core features

Core features support the end-to-end EDI operations workflow, from transaction retrieval and monitoring through diagnostics, reporting, and proactive alerts.

### Transaction retrieval and analysis

EDI Genie retrieves and filters EDI transactions using natural language. You can query by date range, trading partner, transaction type, or status.

For a specific transaction, EDI Genie retrieves its details by ID, including error information for failed transactions.

### Poller diagnostics

EDI Genie identifies transactions stuck in a poller queue. You provide the poller ID, which you can retrieve from the Orderful UI, and EDI Genie returns the stuck transactions, how long each has been blocked, and suggested next steps.

### Trading partner health

EDI Genie summarizes success rates, latency trends, and error trends for a specific trading partner over a time window you specify.

### Audit report generation

EDI Genie generates a comprehensive audit trail report for all transactions processed over a date range you specify.

### Real-time dashboard monitoring

EDI Genie retrieves the current status of the Orderful EDI gateway and system health dashboard.

### Proactive alerts

EDI Genie sends summaries to your notification channel (Slack by default) covering successful and failed transactions, emerging error patterns, and partner-specific issues. Each summary identifies whether failures are concentrated around a specific trading partner and includes a generated report.

### Knowledge-based onboarding help

EDI Genie answers onboarding and setup questions using Orderful guides and customer-supplied FAQs stored in its knowledge base.

## Extended features

Extended features are optional and can be enabled after initial setup.

### Knowledge ingestion

You can ingest Orderful documentation and customer-specific content into the EDI Genie knowledge base. The packaged genie supports file storage by default. To ingest from Google Drive or another app, install the knowledge ingestion module for that specific app. Once ingested, EDI Genie uses this content to answer onboarding, configuration, and troubleshooting questions.

### Custom FAQ upload

You can add customer-specific troubleshooting FAQs, configuration guides, and escalation playbooks to the knowledge base. EDI Genie references this content alongside the standard Orderful guides.

### Custom alert notifications

You can configure when EDI Genie notifies you, such as sending a summary of failed transactions to your notification channel. The underlying alert thresholds aren't configurable.

### Custom skills

You can extend EDI Genie with custom skills built in the **Custom Extensions** folder. The **Core** folder is read-only and managed by Workato. Extensions can be used as-is or cloned into **Custom Extensions** as a starting point.

## Limitations

- **Transaction pagination**: The **Search transactions** skill returns up to 100 records per page due to Orderful API constraints. Use the `next_cursor` value returned in the response to retrieve the next page with the prompt: "Continue to the next page using the cursor `{next cursor value}`."
- **Cross-partner analysis**: EDI Genie supports partner analysis only when you provide a specific partner name or ID. Broad queries across all trading partners aren't supported.
- **Onboarding actions**: EDI Genie answers onboarding and setup questions from its knowledge base. It can't complete onboarding or configuration in Orderful on your behalf.
- **Ticketing**: EDI Genie can't create or escalate tickets automatically. If EDI Genie encounters an error or returns unexpected data, raise a ticket manually with your support or operations team.
- **Date filtering**: Orderful filters transactions inclusive of the start date and exclusive of the end date.

---

---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/it/edi-genie/how-it-works.md
description: >-
  Learn how EDI Genie processes user requests, routes them to Orderful skills,
  and delivers results, including folder structure details.
---

# How EDI Genie works

This page explains how EDI Genie processes requests and describes the project's folder structure.

## Request processing

When a user sends a message in Slack (or Microsoft Teams or Workato GO, if configured), EDI Genie classifies the intent and either calls an Orderful skill to retrieve live data, pulls relevant content from the knowledge base, or sends a proactive alert summary.

EDI Genie doesn't modify EDI payloads and doesn't store sensitive PII or EDI payload data.

## Proactive alerts

The **Error pattern recognition and proactive alert generation** app event fires on a schedule. It retrieves transaction activity from Orderful, identifies failure patterns, and sends summaries to the configured notification channel (Slack by default). The alert includes a generated report and highlights whether failures are concentrated around a specific trading partner.

## Folder structure

The EDI Genie project is organized into the following top-level folders:

- **Config**: Connections and metadata required to run EDI Genie.
- **Core**: Foundational skills maintained by Workato. You can't modify or clone these skills.
- **Extensions**: Additional app skills and functions maintained by Workato and updated during release cycles. You can use these as-is or as a reference when you build custom integrations.
- **Custom Extensions**: Custom assets that you maintain. Clone Extension assets into this folder before you modify them. Assets in this folder remain intact across upgrades.
- **Runtime Data**: Data tables that store the data EDI Genie generates during runtime.

View folder structure

```text
Agentic | EDI Genie
├── Config
│   ├── Metadata
│   └── Connections
├── Core
│   └── EDI Skills
│       └── Orderful
├── Extensions
│   ├── App Events
│   └── Knowledge Ingestion
│       └── Orderful
├── Custom Extensions
│   └── Knowledge Ingestion
└── Runtime Data
```

### Working with Extensions and Custom Extensions

You can activate Extension skills and add them to EDI Genie as-is. You can also clone them into **Custom Extensions** to customize them or build support for apps that aren't available in the **Extensions** folder.

Customizations in **Custom Extensions** are isolated from platform updates and remain intact across upgrades. You can't clone or modify core skills.

---
