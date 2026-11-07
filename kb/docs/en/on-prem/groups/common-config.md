---
url: 'https://docs.workato.com/en/on-prem/groups/common-config.md'
description: >-
  Learn how the on-prem agent config.yml file stores connection profiles and why
  agents in a group must share identical configuration.
---

# Configuration file

The configuration file (**config.yml**) contains one or more [connection profiles](/en/on-prem/agents/connection/profile) used to establish an [on-prem connection](/en/on-prem/agents/connection).

Since requests will be distributed evenly across all agents, the on-prem connection makes an assumption that the profile name used to obtain credentials is available and identical across every agent in the same group. Hence, all on-prem agents in the same on-prem group must use identical configuration files.

> **GROUPED AGENT CONFIGURATIONS**
> 
> Storing agents with different or incomplete profile configurations in the same on-prem group can cause unexpected errors.

It is recommended to configure a single agent first, with all the required profiles, and complete the setup before moving on to backup agents. The configuration file can then be duplicated and used for subsequent agents in the same group.

---
