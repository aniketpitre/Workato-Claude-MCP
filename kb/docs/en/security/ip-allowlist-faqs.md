---
url: 'https://docs.workato.com/en/security/ip-allowlist-faqs.md'
description: >-
  Answers to common questions about adding Workato IP addresses to allowlists
  for databases, firewalls, and on-premise gateways.
---

# IP allowlists FAQs

Get answers to frequently asked questions (FAQs) about IP allowlists.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This page provides general guidance for all Workato users. If you're a Virtual Private Workato (VPW) customer, refer to your private documentation for detailed configuration guidance specific to your instances.

## Why should I add Workato's IP addresses to my allowlist?

View answer

Adding [Workato's IP addresses](/en/security/ip-allowlists#traffic-from-workato) to your allowlist enhances connection security by helping prevent traffic hijacking to and from Workato by malicious websites.

## How can I configure my database to allowlist Workato's IP addresses?

View answer

You can [use SQL commands](/en/security/ip-allowlists#example-allowlist-configuration) to allowlist Workato's IP addresses in your database. Run the following SQL command on your database to allowlist the Workato IP addresses:

```sql
GRANT ALL ON db1.*
TO 'integrationuser'@'52.5.142.59',
'integrationuser'@'34.226.132.221',
'integrationuser'@'52.54.43.157';
```

## What should I consider when adding IP addresses to the allowlist for OPA version 2.11.0 or newer?

View answer

For [OPA version 2.11.0 or later](/en/security/ip-allowlists#on-premise-gateway-addresses), you must add specific FQDNs and IP addresses to the allowlist. It's important to use both the sg3 and sg4 versions for load balancing.

## How do I configure firewall allowlists for on-premise gateway IP addresses?

View answer

To [configure firewall allowlists](/en/security/ip-allowlists#static-assets) for on-premise gateway IP addresses, you must enable outbound TCP connections from the OPA to port 443.

## What should I do if my organization restricts DNS resolutions for the OPA?

View answer

Ensure that the machine where OPA runs can resolve the IP addresses of the on-premise gateway's FQDNs if your organization [restricts DNS resolutions](/en/security/ip-allowlists#dns-resolution-of-fqdns).

## Which IP addresses should I add to the allowlist when using custom domains for API recipes in Workato?

View answer

The [IP addresses for custom domains](/en/security/ip-allowlists#custom-apim-domains) vary by data center. Refer to the following lists to determine which IP address to use.

### Workato Enterprise customers

- US data center: 52.5.142.59, 34.226.132.221, 52.54.43.157
- EU data center: 3.65.225.246, 3.66.45.94, 18.198.249.58
- JP data center: 52.193.168.95, 13.113.30.44, 18.176.45.101
- SG data center: 13.215.42.244, 18.141.131.114, 52.74.226.121
- AU data center: 54.253.214.156, 13.236.115.248, 13.238.90.15
- IL data center: 51.16.210.3, 51.84.133.176, 51.17.208.207
- KR data center: 43.200.205.181, 43.201.190.232, 3.36.217.81
- UK data center: 35.179.4.243, 35.179.240.64, 16.60.82.97

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: 13.219.6.188, 54.82.211.237, 54.86.143.73

## What IP addresses are used for browser-based user interaction to Workato?

View answer

The [IP addresses for browser-based user interaction](/en/security/ip-allowlists#browsers-and-api-endpoints) depend on the data center where your account is located.

Workato Enterprise customers:

- **US Data Center**: [https://www.workato.com](https://www.workato.com)
- **EU Data Center**: [https://app.eu.workato.com/](https://app.eu.workato.com/)
- **JP Data Center**: [https://app.jp.workato.com](https://app.jp.workato.com)
- **SG Data Center**: [https://app.sg.workato.com/](https://app.sg.workato.com/)
- **AU Data Center**: [https://app.au.workato.com/](https://app.au.workato.com/)
- **IL Data Center**: [https://app.il.workato.com/](https://app.il.workato.com/)
- **CN Data Center**: [https://app.workatoapp.cn/](https://app.workatoapp.cn/)
- **KR Data Center**: [https://app.kr.workato.com/](https://app.kr.workato.com/)
- **UK Data Center**: [https://app.uk.workato.com/](https://app.uk.workato.com/)

Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:

- **Self-service Data Center**: [https://app.trial.workato.com/](https://app.trial.workato.com/)

## Where can I find the API endpoint IP addresses for Workato?

View answer

The [API endpoint IP address](/en/security/ip-allowlists#browsers-and-api-endpoints) differs depending on the location of your data center.

- **Workato Enterprise customers**
  - US Data Center: [https://www.workato.com](https://www.workato.com)
  - EU Data Center: [https://app.eu.workato.com/](https://app.eu.workato.com/)
  - JP Data Center: [https://app.jp.workato.com](https://app.jp.workato.com)
  - SG Data Center: [https://app.sg.workato.com/](https://app.sg.workato.com/)
  - AU Data Center: [https://app.au.workato.com/](https://app.au.workato.com/)
  - IL Data Center: [https://app.il.workato.com/](https://app.il.workato.com/)
  - CN Data Center: [https://app.workatoapp.cn/](https://app.workatoapp.cn/)
  - KR Data Center: [https://app.kr.workato.com/](https://app.kr.workato.com/)
  - UK Data Center: [https://app.uk.workato.com/](https://app.uk.workato.com/)
- **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users**
  - Self-service Data Center: [https://app.trial.workato.com/](https://app.trial.workato.com/)

---
