---
url: 'https://docs.workato.com/en/lut-row-limit-faq.md'
description: >-
  Find answers about the 100,000-row quota per Workato lookup table enforced
  from June 3, 2025 across all entry points, and how to stay under it.
---

# Lookup table 100,000 record quota enforced from June 3, 2025

## What is the update?

Workato will enforce a quota of **100,000 rows per Lookup table** across all entry points, including connector actions and API endpoints.

Previously, Workato only enforced this quota in the UI. Starting June 3, 2025, the platform will reject all attempts to add records beyond this quota, regardless of the entry point.

You can't add records to any Lookup table that has 100,000 rows. This applies to all new tables and existing tables with less than 95,000 rows as of June 2, 2025. Tables that had more than 95,000 rows on that date aren't affected.

## What do you need to do?

Review your Lookup table usage and identify use cases that depend on large tables. Set up a regular process to remove outdated records and avoid reaching the quota. This prevents errors and keeps workflows stable.

You can use the [Truncate table](/en/data-tables/connector/truncate-table-action) action to remove outdated data. Export data before cleanup for archival purposes if needed.

---
