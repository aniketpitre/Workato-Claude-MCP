---
url: 'https://docs.workato.com/en/pricing/usage-metrics/data-pipelines.md'
description: >-
  Learn how Workato measures Data pipeline usage in Rows, including calculation
  rules and example scenarios.
---

# Data pipeline usage

Workato measures data pipeline usage in Rows. Rows count the number of rows extracted from the source across all successful objects in each sync.

## How rows are counted

The following diagram illustrates where usage is measured in a data pipeline. Rows are counted at extraction from the source, across all objects that sync successfully. Transformation and load steps don't add to the count.

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    A(["&nbsp;&nbsp;Source&nbsp;&nbsp;"]) --> D["&nbsp;&nbsp;Extract&nbsp;&nbsp;<br/>(Rows counted here)"]
    D --> H["&nbsp;&nbsp;Transform&nbsp;&nbsp;"]
    H --> R["&nbsp;&nbsp;Load&nbsp;&nbsp;"]
    R --> B(["&nbsp;&nbsp;Destination&nbsp;&nbsp;"])
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    classDef NonBillable fill:#fff,stroke:#b3e0e1,stroke-width:2px,color:#666,stroke-dasharray: 5 5;
    class D Focus
    class H,R NonBillable
```

## Data pipeline calculation rules

Data pipeline usage calculations follow the general [usage calculation rules](/en/pricing/usage-metrics#rules), where rows from successful objects count toward usage and rows from failed objects are excluded.

Workato uses the following additional rules to calculate Rows:

- Each row extracted from a successful object counts as 1 Row.
- Rows from objects that fail to sync don't count toward usage. Failed objects are retried on later syncs. Once an object syncs successfully, its rows count then.
- Transformation and load steps within a pipeline don't contribute to Rows.
- Failed or canceled syncs count only the rows from objects that completed successfully before the failure or cancellation.
- ETL or ELT performed in a workflow recipe is measured as workflow recipe usage, not as data pipeline usage.

## Data pipeline usage examples

The following examples demonstrate how Workato calculates data pipeline usage.

### Example: Successful sync

The following table demonstrates how usage is counted when all synced objects complete successfully:

| Object | Sync status | Rows extracted | Counted |
| --- | --- | --- | --- |
| Customers | Success | 100 | 100 |
| Orders | Success | 250 | 250 |
| Products | Success | 50 | 50 |
| **Total Rows** |  |  | **400** |

Each row extracted from a successful object counts as 1 Row.

### Example: Sync with partial object failure

The following table demonstrates how usage is counted when a portion of the synced objects fail:

| Object | Sync status | Rows extracted | Counted |
| --- | --- | --- | --- |
| Customers | Success | 100 | 100 |
| Orders | Success | 250 | 250 |
| Products | Failed | 50 | 0 |
| **Total Rows** |  |  | **350** |

Only rows extracted from successful objects count toward usage.

---
