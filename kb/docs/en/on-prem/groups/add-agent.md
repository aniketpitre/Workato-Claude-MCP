---
url: 'https://docs.workato.com/en/on-prem/groups/add-agent.md'
description: >-
  Add an on-prem agent to a Workato on-prem group, set the agent name, and
  select the operating system where you install it.
---

# Add an agent to an on-prem group

Refer to the information on this page to add an agent to an on-prem group.

> **PREREQUISITES**
> 
> You must [create an on-prem group](/en/on-prem/groups/create-group) before you can set up an on-prem agent.

Complete the following steps to set up an on-prem agent in Workato:

1. Sign in to Workato.
   
2. Go to **Tools > On-prem groups** and select the on-prem group in which you plan to add an agent.
   
3. Click **Add new agent**.
   
4. Provide a meaningful **Agent name** and select the **Operating system** (OS) where you plan to install the agent.
   
   ![Choose OS](/assets/windows-select-os.eI4n6XDp.png)_Choose OS_
   
5. Download and then start the installer. ![Install agent](/assets/windows-download-installer.ps7UsM4C.png)_Install agent_
   
6. Refer to the following OS-specific guides to complete the remaining installation steps:
   
   - [Windows](/en/on-prem/groups/add-agent/windows)
   - [Linux DEB package](/en/on-prem/groups/add-agent/linux-deb)
   - [Linux RPM package](/en/on-prem/groups/add-agent/linux-rpm)
   - [Docker image](/en/on-prem/groups/add-agent/docker)
   - [Mac](/en/on-prem/groups/add-agent/macos)

Refer to [Run an on-prem agent](/en/on-prem/agents/run) to start an agent after installation.

## Next steps

You can perform the following actions after setting up an on-prem group and adding an on-prem agent:

- Set up recipe connections [with on-prem agents](/en/on-prem/agents/connection).
- [Configure connection profiles](/en/on-prem/agents/connection/profile) for your agents.
- [Upgrade](/en/on-prem/agents/upgrade) your on-prem agent.
- Set up [password encryption](/en/on-prem/agents/password-encryption).
- Set up a [proxy environment](/en/on-prem/agents/proxy) for your on-prem agent.
- Toggle the [active/inactive](/en/on-prem/agents/run) status of your on-prem agents.
- Connect to legacy applications [using Java](/en/on-prem/agents/extension).

---
