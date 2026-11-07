---
url: 'https://docs.workato.com/en/security/ip-allowlists.md'
description: >-
  Add Workato IP addresses to your allowlist to secure traffic, with the IP
  ranges for each data center and example configurations.
---

# IP allowlists

You can add IPs to the allowlist to prevent a malicious website from hijacking traffic to and from Workato.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This page provides general guidance for all Workato users. If you're a Virtual Private Workato (VPW) customer, refer to your private documentation for detailed configuration guidance specific to your instances.

## Traffic from Workato

Traffic from Workato uses a unique set of IP addresses for each [data center](/en/datacenter/datacenter-overview).

### Workato Enterprise customers

- US data center: 52.5.142.59, 34.226.132.221, 52.54.43.157
- EU data center: 3.65.225.246, 3.66.45.94, 18.198.249.58
- JP data center: 52.193.168.95, 13.113.30.44, 18.176.45.101
- SG data center: 13.215.42.244, 18.141.131.114, 52.74.226.121
- AU data center: 54.253.214.156, 13.236.115.248, 13.238.90.15
- IL data center: 51.16.210.3, 51.84.133.176, 51.17.208.207
- CN data center: 161.189.63.116, 52.82.72.174, 52.83.128.24
- KR data center: 43.200.205.181, 43.201.190.232, 3.36.217.81
- UK data center: 35.179.4.243, 35.179.240.64, 16.60.82.97

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: 174.129.15.46, 13.216.205.222, 3.234.79.251

You can add these IP addresses to your application or firewall allowlist. Add all three IP addresses to ensure continuous access.

### Example allowlist configuration

If you have a recipe that accesses a MySQL server that runs on an Amazon EC2 machine, with a special **integrationuser** user, you can run the following SQL command on your database to add Workato IP addresses to the allowlist:

```sql
GRANT ALL ON db1.*
TO 'integrationuser'@'52.5.142.59',
'integrationuser'@'34.226.132.221',
'integrationuser'@'52.54.43.157';
```

## Traffic to Workato

### On-prem agent

Workato's [on-prem agent](/en/on-prem) (OPA) provides secure selective access from Workato to customer-authorized on-prem apps, databases, and folders without having to open inbound ‘ports’ in the corporate firewall.

The OPA creates an outbound connection to the Workato cloud's on-premise gateways with the following domain names and IP addresses.

Each [data center](/en/datacenter/datacenter-overview) uses a unique set of IP addresses.

All Workato IP addresses use TCP port 443.

> **ON-PREM GROUP SETTINGS**
> 
> Add Workato IPs to your network's allowlist through its firewall or security settings. Don't use an on-prem group's **Settings > IP Allowlist** page to allowlist Workato IPs. This page defines which IPs on-prem agents can connect from, not which IPs they can connect to.

> **SSL/TLS CONFIGURATION**
> 
> The OPA gateway connection uses mutual TLS with Workato's private PKI. SSL inspection tools that intercept and re-sign HTTPS traffic break this connection. Configure your inspection tool to bypass the gateway FQDNs listed below. Refer to [Configure SSL/TLS inspection](/en/on-prem#ssl-tls-inspection) for more information.

### On-premise gateway addresses

If you are using OPA, add the following addresses to the allowlist. You must use both the **sg3** and **sg4** versions for load balancing.

### Workato Enterprise customers

- United States: US data center
  - `sg3.workato.com`: 54.224.75.148, 52.206.161.203, 52.204.114.159
  - `sg4.workato.com`: 54.91.65.247, 54.221.112.165, 3.216.209.184
- European Union: EU data center
  - `sg3.eu.workato.com`: 3.123.148.167, 18.192.102.156, 52.29.133.142
  - `sg4.eu.workato.com`: 3.72.205.158, 18.156.149.92, 52.58.222.49
- Japan: JP data center
  - `sg3.jp.workato.com`: 35.79.205.155, 52.199.27.57, 35.78.12.221
  - `sg4.jp.workato.com`: 3.113.210.186, 3.113.92.57, 54.92.47.124
- Singapore: SG data center
  - `sg3.sg.workato.com`: 52.76.214.244, 13.215.168.151, 54.255.216.78
  - `sg4.sg.workato.com`: 52.221.44.179, 52.221.46.218, 18.138.33.21
- Australia: AU data center
  - `sg3.au.workato.com`: 13.239.42.137, 3.105.83.213, 13.210.248.78
  - `sg4.au.workato.com`: 54.206.76.14, 13.211.112.228, 3.24.233.233
- Israel: IL data center
  - `sg3.il.workato.com`: 51.16.76.235, 51.16.76.9, 51.17.147.58
  - `sg4.il.workato.com`: 51.84.119.32, 51.84.73.53, 51.84.91.163
- China: CN data center
  - `sg3.workatoapp.cn`: 43.192.0.198, 52.83.137.238, 69.234.233.220
  - `sg4.workatoapp.cn`: 43.192.188.57, 43.192.33.170, 69.231.160.59
- South Korea: KR data center
  - `sg3.kr.workato.com`: 15.164.1.152, 54.116.86.97, 15.165.239.112
  - `sg4.kr.workato.com`: 43.202.190.67, 3.37.152.153, 43.202.15.147
- United Kingdom: UK data center
  - `sg3.uk.workato.com`: 18.168.230.99, 3.11.158.160, 3.10.163.73
  - `sg4.uk.workato.com`: 16.60.63.49, 18.170.249.104, 18.170.142.41

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center
  - `sg3.trial.workato.com`: 34.197.33.27, 54.197.241.34, 54.208.38.233
  - `sg4.trial.workato.com`: 3.220.106.228, 50.19.105.34, 52.70.118.186

### On-premise gateway IP address allowlist

If your organization has strict outbound traffic rules, you must enable OPA's access to the Workato cloud by adding it to the allowlist.

Ensure any proxies or firewalls allow outbound TCP connections from the OPA to Workato's [on-prem gateways](#on-premise-gateway-addresses).

### DNS resolution of FQDNs

Some organizations also restrict DNS resolutions on the machines and networks where the OPA runs. Ensure that the machine running OPA can resolve the IP addresses of the on-premise gateway's FQDNs.

## APIM IP addresses

APIM doesn't include permanent IP addresses. APIM IP addresses generally remain static, but can change due to routine maintenance or scaling. Refer to [Custom APIM domains and IP addresses](#custom-apim-domains) if you require a permanent IP address.

## Custom APIM domains and IP addresses

Static IP addresses are configured for APIM using [custom domains](/en/api-mgmt/custom-domain). Workato routes client traffic to the following set of IP addresses when using custom domains for API recipes. Each [data center](/en/datacenter/datacenter-overview) uses a unique set of IP addresses.

> **FEATURE AVAILABILITY**
> 
> API platform custom domains aren't supported in the China data center.

### Workato Enterprise customers

- US data center: 18.211.121.35, 34.232.254.255, 52.203.235.136
- EU data center: 3.127.182.4, 3.64.168.57, 3.66.114.67
- JP data center: 18.177.63.189, 52.194.114.232, 52.196.96.189
- SG data center: 18.136.28.27, 13.215.62.220, 13.214.235.186
- AU data center: 13.236.168.184, 13.238.90.32, 3.24.69.138
- IL data center: 51.17.82.211, 51.84.107.232, 51.84.126.94
- KR data center: 3.38.38.151, 43.200.62.59, 3.37.69.159
- UK data center: 13.134.241.137, 3.10.40.174, 18.169.202.36

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: 13.219.6.188, 54.82.211.237, 54.86.143.73

> **TLS AND HTTP STANDARDS**
> 
> Refer to [Security](/en/security#tls-http-standards) for information about supported TLS and HTTP standards for custom domain endpoints.

## Webhook domains

You must allowlist the Workato webhook domain before sending webhooks to Workato.

Each [data center](/en/datacenter/datacenter-overview) uses a unique domain:

### Workato Enterprise customers

- US data center: `webhooks.workato.com`
- EU data center: `webhooks.eu.workato.com`
- JP data center: `webhooks.jp.workato.com`
- SG data center: `webhooks.sg.workato.com`
- AU data center: `webhooks.au.workato.com`
- IL data center: `webhooks.il.workato.com`
- CN data center: `webhooks.workatoapp.cn`
- KR data center: `webhooks.kr.workato.com`
- UK data center: `webhooks.uk.workato.com`

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: `webhooks.dev.workato.com`

## Static assets

Certain assets like recipe packages, profile photos, and customer adapter logos are served from a dedicated S3 bucket in your regional data center. Each [data center](/en/datacenter/datacenter-overview) has its own S3 bucket. Add the domain to your firewall allowlist based on the data center your account is hosted in.

### Workato Enterprise customers

- US data center: `workato-assets.s3.amazonaws.com`
- EU data center: `workato-assets-eu-2.s3.amazonaws.com`
- JP data center: `workato-assets-jp.s3.amazonaws.com`
- SG data center: `workato-assets-sg.s3.amazonaws.com`
- AU data center: `workato-assets-au.s3.amazonaws.com`
- IL data center: `workato-assets-ilc1.s3.il-central-1.amazonaws.com`
- CN data center: `assets.cdn.workatoapp.cn`
- KR data center: `workato-assets-kr.s3.ap-northeast-2.amazonaws.com`
- UK data center: `workato-assets-uk.s3.eu-west-2.amazonaws.com`

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: `workato-assets-trial.s3.us-east-1.amazonaws.com`

## Browsers and API endpoints

All other traffic to Workato may be served by a different set of IP addresses, distinct from IP addresses discussed previously:

### Browsers

Browser-based user interaction depends on the data center where your account is located:

#### Workato Enterprise customers

- US data center: `https://www.workato.com`
- EU data center: `https://app.eu.workato.com/`
- JP data center: `https://app.jp.workato.com`
- SG data center: `https://app.sg.workato.com/`
- AU data center: `https://app.au.workato.com/`
- IL data center: `https://app.il.workato.com`
- CN data center: `https://app.workatoapp.cn`
- KR data center: `https://app.kr.workato.com`
- UK data center: `https://app.uk.workato.com`

#### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: `https://app.trial.workato.com`

### API endpoint requests

API endpoint requests depend on the data center where your account is located:

#### Workato Enterprise customers

- US data center: `https://apim.workato.com/`
- EU data center: `https://apim.eu.workato.com/`
- JP data center: `https://apim.jp.workato.com/`
- SG data center: `https://apim.sg.workato.com/`
- AU data center: `https://apim.au.workato.com/`
- IL data center: `https://apim.il.workato.com/`
- CN data center: `https://apim.workatoapp.cn/`
- KR data center: `https://apim.kr.workato.com/`
- UK data center: `https://apim.uk.workato.com/`

#### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: `https://apim.trial.workato.com/`

> **TLS AND HTTP STANDARDS**
> 
> See [Security](/en/security#tls-http-standards) for more information about supported TLS and HTTP standards for API endpoints.

---
