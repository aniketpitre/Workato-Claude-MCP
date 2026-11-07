---
url: 'https://docs.workato.com/en/on-prem/agents/deprecation.md'
description: >-
  Reference for Workato on-prem agent version deprecation and sunset dates, with
  the upgrade schedule to avoid recipe disruptions.
---

# On-prem agent version deprecation

Workato regularly releases new versions of the on-prem agent (OPA). Workato deprecates older OPA versions on a recurring schedule to ensure users benefit from these improvements.

Upgrading the OPA provides the following benefits:

- **Security:** Newer versions include enhanced security.
- **Performance:** Newer versions are better optimized for speed and reliability.
- **New features:** Newer versions support the latest Workato platform features, including new connectors, updated triggers and actions, and additional configuration options.

Refer to the [OPA version notes](/en/on-prem/agents/versions) for information about recent OPA changes.

> **UPGRADE THE OPA**
> 
> Workato recommends that you [upgrade the OPA](/en/on-prem/agents/upgrade) regularly to keep the version no more than one year old.

## Deprecation schedule

The following schedule lists the deprecation and sunset dates of the Workato on-prem agents. Contact your Workato Customer Success Manager if you have additional questions about OPA deprecation.

- After the **Deprecation date**, the OPA continues to run, but Workato no longer provides support.
  
- On the **Sunset date**, the OPA stops connecting to Workato, which disrupts all running recipes. Upgrade the OPA before the sunset date to avoid interruptions.
  

| Agent version | Release date | Deprecation date | Sunset date | Notes |
| --- | --- | --- | --- | --- |
| **Older than 2.19.0** | Before May 24, 2023 | January 8, 2026 | January 8, 2026 | Workato introduced a new activation flow in [2.19.0](/en/on-prem/agents/versions#v2-19-0). |
| **Older than 2.14.0** | Before September 7, 2022 | September 30, 2023 | January 31, 2024 | These agents used an internal web server that was replaced in version [2.14.0](/en/on-prem/agents/versions#v2-14-0). Also, agents older than [2.11.0](/en/on-prem/agents/versions#v2-11) used gateways `sg1.workato.com` and `sg2.workato.com`, which shut down on January 31, 2024. |
| **Older than 2.6.2** | Before May 16, 2020 | May 1, 2023 | June 12, 2023 | These agents used the `sg.workato.com` gateway, which shut down on June 12, 2023. |

---
