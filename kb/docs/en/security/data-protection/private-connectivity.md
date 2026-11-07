---
url: 'https://docs.workato.com/en/security/data-protection/private-connectivity.md'
description: >-
  Learn about Workato private connectivity options, including AWS PrivateLink,
  Azure Private Link, the on-prem agent, and Virtual Private Workato.
---

# Private connectivity

Workato offers the following private connectivity options for an enhanced level of security and data protection:

- [AWS PrivateLink](#aws-privatelink)
- [Azure Private Link](#azure-private-link)
- [On-prem agent](#opa)
- [Virtual Private Workato](#virtual-private-workato)

## AWS PrivateLink

[AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink) uses private endpoints to connect an AWS Virtual Private Cloud (VPC) to the Workato multi-tenant cloud without traversing the public internet. This connection provides secure access to OPA-capable connectors and Workato's API platform.

Refer to the [AWS PrivateLink](/en/security/data-protection/private-link-aws) page for more information about AWS PrivateLink, including setup instructions.

## Azure Private Link

[Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) uses private endpoints to connect an Azure Virtual Network (VNet) to the Workato multi-tenant cloud without traversing the public internet. This connection provides secure access to OPA-capable connectors and Workato's API platform.

Refer to the [Azure Private Link](/en/security/data-protection/private-link-azure) page for more information about Azure Private Link, including setup instructions.

## On-prem agent

The Workato on-prem agent (OPA) supports secure data transfer to Workato without requiring inbound firewall openings and allows Workato to access applications that are only available from the user's private network. OPA establishes an outbound connection from a user’s network to Workato’s cloud gateways, allowing for TLS-encrypted data transfer over the public internet.

Refer to the [Accessing on-prem](/en/on-prem) section for more information about OPA, including setup instructions.

## Virtual Private Workato

Virtual Private Workato (VPW) offers a dedicated private Workato instance separate from Workato’s commercial cloud environment. VPW is hosted in its own AWS Virtual Private Cloud (VPC) and connected through VPC peering and transit gateway to customer external networks. VPW is ideal for customers with strict compliance, data residency, or security requirements.

Refer to the [VPW](/en/cloud-hosting-editions/hosting-editions) page for more information about Virtual Private Workato.

---
