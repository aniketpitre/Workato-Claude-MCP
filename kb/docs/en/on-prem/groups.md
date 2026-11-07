---
url: 'https://docs.workato.com/en/on-prem/groups.md'
description: >-
  Learn how on-prem groups pool Workato on-prem agents for high availability
  through fault tolerance and load balancing.
---

# On-prem group

![On-prem groups](/assets/on-prem-groups.DyO7Tf4i.png)_On-prem groups_

On-prem group is a logical grouping of one or more on-prem agents into a common connection pool. The workload is distributed evenly to all agents in an on-prem group. A recipe that uses an on-prem group with more than one active agent achieves **High availability**. This has a few advantages.

## High Availability

High Availability is the ability of a system to be continuously operational for a long period of time. For any system to be highly available, every part of a system needs to be present and functional for the whole to be operational. This is typically achieved through **Fault tolerance** and **Load balancing**.

### Fault Tolerance

Fault tolerance allows a system to continue operating properly in the event of the failure of some components. In on-prem groups, this is achieved by adding redundancy to the on-prem agents. Each of these agents acts as a backup or fail-safe, in the event that one or more server hosting them goes offline.

### Load Balancing

Load balancing is the distribution of work across multiple resources. In this case, we are distributing requests across multiple on-prem agents in the same group. This avoids overloading a single server, improves responsiveness and overall performance of a recipe using on-prem connections.

## In this section

- [Create a group](/en/on-prem/groups/create-group)
- [Add agent to a group](/en/on-prem/groups/add-agent)
- [Status of a group](/en/on-prem/groups/group-status)
- [Common configuration for agents](/en/on-prem/groups/common-config)

---
