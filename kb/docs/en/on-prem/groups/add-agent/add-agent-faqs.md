---
url: 'https://docs.workato.com/en/on-prem/groups/add-agent/add-agent-faqs.md'
description: >-
  Answers to common questions about adding Workato on-prem agents, including
  supported operating systems and activation codes.
---

# On-prem add agent FAQs

Get answers to frequently asked questions (FAQs) about adding on-prem agents.

## What is an on-prem group in Workato, and why would I need to create one?

View answer

An [on-prem group](/en/on-prem/groups#on-prem-group) in Workato is a way to manage a group of on-prem agents that perform specific tasks. You may need to create an on-prem group to organize and manage your agents effectively.

## What operating systems are supported for setting up on-prem agents in Workato?

View answer

Workato supports the following operating systems for on-prem agent setup:

- [Windows](/en/on-prem/groups/add-agent/windows)
- [Linux DEB package](/en/on-prem/groups/add-agent/linux-deb)
- [Linux RPM package](/en/on-prem/groups/add-agent/linux-rpm)
- [Docker image](/en/on-prem/groups/add-agent/docker)
- [Mac](/en/on-prem/groups/add-agent/macos)

## What is the Windows Service user account used for in the on-prem agent setup?

View answer

Beginning with version 2.18.0, the [Windows Service user account](/en/on-prem/groups/add-agent/windows) for Workato on-prem agents is set to **Local Service** instead of **Local System** You can change this user account by editing the OPA windows service properties.

## Where can I find the activation code needed during agent installation?

View answer

You can find the [activation code](/en/on-prem/agents/run) in the agent creation wizard in Workato. Copy the code and paste it into the Windows installer during installation.

## Is there an alternative way to activate the agent if I don't have the activation code during installation?

View answer

Yes, you can [activate your agent](/en/on-prem/agents/run) later by running the `activation.cmd` script from the `bin` folder in your agent installation directory.

## On-prem agent connectivity

## What should I be aware of regarding network configuration when setting up the on-prem agent?

View answer

Traffic to Workato must be allowed from your server to use OPA. Refer to [security allowlists](/en/security/ip-allowlists#traffic-to-workato) to add Workato to your allowlist.

## How can I verify that my on-prem agent is functioning correctly?

View answer

After the agent becomes active, you can click **Test agent** to verify that the connection is successful. This confirms that your agent is working as expected.

---
