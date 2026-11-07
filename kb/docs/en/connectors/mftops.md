---
url: 'https://docs.workato.com/en/connectors/mftops.md'
description: >-
  Use MFTOps to build recipes that react to file transfer events, such as failed
  or successful transfer runs and missed polls.
---

# MFTOps

**MFTOps** enables you to build recipes that react to [file transfer](/en/managed-file-transfer/transfer-flows) events, such as a failed or successful transfer run, or a missed poll.

## Connection setup

No connection set up is required to use **MFTOps**.

## Triggers

MFTOps supports the following recipe triggers:

- [No file detected](/en/connectors/mftops/triggers/no-file-detected)
- [Failed transfer run](/en/connectors/mftops/triggers/failed-transfer-run)
- [Successful transfer run](/en/connectors/mftops/triggers/successful-transfer-run)
- [Transfer stopped](/en/connectors/mftops/triggers/transfer-stopped)

## Example use cases

You can use MFTOps to build out solutions for the following use cases:

- Notify your operations team when a transfer run fails, so they can investigate before it affects downstream processes.
- Trigger a downstream recipe, such as a reconciliation or validation step, automatically when a transfer run succeeds.
- Catch a stalled or missing partner feed by reacting to polls that find no files, before a missed delivery becomes a bigger problem.
- Alert your team when a transfer automatically stops after repeated failures, so they can investigate before manually reactivating it.
- Build a centralized view of transfer health, such as a dashboard or report, instead of checking each transfer's run history individually.

> **FEATURE AVAILABILITY**
> 
> Contact your Customer Success Manager for information about access to Workato MFT.

---
