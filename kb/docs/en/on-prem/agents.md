---
url: 'https://docs.workato.com/en/on-prem/agents.md'
description: >-
  The Workato on-prem agent securely connects recipes to on-prem apps,
  databases, and folders without opening ports in your firewall.
---

# On-prem agent

The Workato on-prem agent provides a secure way for Workato to selectively access customer-authorized on-prem apps, databases, and folders without having to open ports in the corporate firewall.

Users can communicate securely with Workato by installing the agent within the protected server.

The on-prem agent is used to create connections that are used by recipes to perform requests. These on-prem connections can be connected to one or more agents in an [on-prem group](/en/on-prem/groups).

> **USE MULTIPLE AGENTS**
> 
> On-prem groups distribute their workload evenly across all contained agents. Workato recommends adding multiple agents to an on-prem group to ensure high availability, fault tolerance, and load balancing. You can further enhance these capabilities by hosting some of the group's agents on a separate server.

![On-prem menu option](/assets/navigate-to-opa.Ie_o-suc.png)_On-prem menu option_

## Common errors when using the on-prem agent

If connecting to on-prem applications fail, check that:

- The selected agent is active
- Credentials provided in the app connection are correct
- Credentials provided by user in the app connection has the correct role and permission to connect

If connecting to on-prem databases fail, check that:

- Selected agent is active
- Credentials provided in the connection profile are correct
- Database name and type provided in the connection profile is correct

## In this section

- [Add an agent](/en/on-prem/groups/add-agent)
- [Run an agent](/en/on-prem/agents/run)
- [Profiles](/en/on-prem/agents/connection/profile)
- [Upgrade an agent](/en/on-prem/agents/upgrade)
- [On-prem connections](/en/on-prem/agents/connection)
- [Password encryption](/en/on-prem/agents/password-encryption)
- [Proxy server](/en/on-prem/agents/proxy)
- [Logging](/en/on-prem/agents/logging)
- [Extensions](/en/on-prem/agents/extension)

---
