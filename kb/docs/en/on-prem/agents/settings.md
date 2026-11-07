---
url: 'https://docs.workato.com/en/on-prem/agents/settings.md'
description: >-
  Configure logging, IP allowlists, and email alerts for your Workato on-prem
  agents from the on-prem group Settings page.
---

# On-prem group settings

The on-prem group **Settings** page enables you to configure logging, network access, and alert behavior for your on-prem agents.

The on-prem group **Settings** page includes the following sections:

- [Log management](#log-management): Control whether on-prem agent (OPA) logs are sent to Workato logging services.
- [IP allowlist](#ip-allowlist): Define which IP addresses agents in this group can connect from.
- [Email alerts](#email-alerts): Configure email notifications for agent disconnections.

## Prerequisites

Ensure you meet the following requirements before you begin:

- You have access to **Tools > On-prem groups**
- You have permission to edit the selected on-prem group

## Log management

You can use **Log management** to control whether the on-prem agent (OPA) sends logs to Workato.

### Configure log management

Complete the following steps to configure log management:

1. Go to **Tools > On-prem groups** and select the on-prem group you plan to configure.
   
2. Go to **Settings > Log management**.
   
   ![Configure log management](/assets/log-management-opa.DsbQynyW.png)_Configure log management_
   
3. Enable or disable **Send to Workato logs**. The on-prem agent sends a copy of its logs to Workato logging services when enabled.
   
4. Click **Save**.
   

Refer to [Workato Logging Service](/en/on-prem/agents/logging#workato-logging-service) to learn more about OPA log storage and filtering.

## IP allowlist

The **IP allowlist** settings enable you to define which IP addresses on-prem agents in this group can connect from.

### Configure IP allowlist

Complete the following steps to configure the IP allowlist:

1. Go to **Tools > On-prem groups** and select the on-prem group you plan to configure.
   
2. Go to **Settings > IP allowlist**.
   
   ![Configure IP allowlist](/assets/configure-ip-allowlist.h2stjDrp.png)_Configure IP allowlist_
   
3. Enter IP addresses in the **Allowed IPs** field. You can enter multiple IP addresses separated by commas, or define a range using CIDR notation (for example, `106.226.100.3/20`).
   
   > **ON-PREM AGENT CONNECTION RULES**
   > 
   > The **IP allowlist** setting defines which IP addresses on-prem agents can connect from.
   > 
   > It doesn't define which IP addresses or services the agent can connect to. Configure outbound access in your network firewall.
   
4. Click **Save**.
   

## Email alerts

Email alerts notify you when an on-prem agent disconnects. You can configure alert behavior, recipients, and disconnection types in the **Email alerts** page. Refer to the [Automatic alerts](/en/on-prem/agents/alert) page for more information.

---
