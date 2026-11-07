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
