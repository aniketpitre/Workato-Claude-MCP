---
url: 'https://docs.workato.com/en/datacenter/datacenter-overview.md'
description: >-
  Choose the cloud region where Workato stores and processes your automation
  data to meet legal and regulatory compliance needs.
---

# Supported cloud regions

Workato enterprise customers can choose the region where Workato stores and processes your organization’s automation data. This includes recipes, connections, shared assets like lookup tables, and the job history. This data remains isolated in that specific region and can't be transferred to other regions.

> **SELF-SERVICE (WORKATO FREE, WORKATO PRO, OR DEVELOPER SANDBOX)**
> 
> Self-service users can't choose the region where Workato stores and processes your organization’s automation data.

This approach allows you to localize your data and processing in specific locations when necessary for legal and regulatory compliance.

> **SECURITY MEASURES ARE THE SAME ACROSS DATA CENTERS**
> 
> Refer to the [Workato Security Overview](https://www.workato.com/legal/security) to learn more about how Workato addresses security.

![Workato data center locations](/assets/international-datacenters.DCXbxkl7.png)_Workato data center locations_

## Data center locations

You can host your Workato data in the following regions.

### Workato Enterprise customers

<dl><dt id="us-data-center">US data center</dt><dd>The US data center is hosted on Amazon Web Services (AWS) in the US East region. It is available for Workato customers in the North America region.<br><a href="https://app.workato.com/users/sign_in">Sign in to the US data center</a>.</dd><dt id="european-union-data-center">EU data center</dt><dd>The European Union (EU) data center is available for customers in the European Economic Area (EEA) who prefer to store and process their data locally. The new data center is hosted in the AWS EU Central region.<br><a href="https://app.eu.workato.com/users/sign_in">Sign in to the EU data center</a>.</dd><dt id="japan-data-center">JP data center</dt><dd>The JP data center is available for customers who require their data within Japan.<br><a href="https://app.jp.workato.com/users/sign_in">Sign in to the JP data center</a>.</dd><dt id="singapore-data-center">SG data center</dt><dd>The SG data center is available for customers who require their data within Singapore.<br><a href="https://app.sg.workato.com/users/sign_in">Sign in to the SG data center</a>.</dd><dt id="australia-data-center">AU data center</dt><dd>The AU data center is available for customers who require their data within Australia.<br><a href="https://app.au.workato.com/users/sign_in">Sign in to the AU data center</a>.</dd><dt id="israel-data-center">IL data center</dt><dd>The IL data center is available for customers who require their data within Israel.<br><a href="https://app.il.workato.com/users/sign_in">Sign in to the IL data center</a>.</dd><dt id="china-data-center">CN data center</dt><dd>The CN data center is available for customers who require their data within China. The <a href="https://www.docs.workato.com/en/datacenter/cn-data-center.html">CN data center</a> is subject to considerations unique to the greater China region.<br><a href="https://app.workatoapp.cn/users/sign_in">Sign in to the CN data center</a>.</dd><dt id="korea-data-center">KR data center</dt><dd>The KR data center is available for customers who require their data to be stored within South Korea.<br><a href="https://app.kr.workato.com/users/sign_in">Sign in to the KR data center</a>.</dd><dt id="uk-data-center">UK data center</dt><dd>The UK data center is available for customers who require their data within the United Kingdom.<br><a href="https://app.uk.workato.com/users/sign_in">Sign in to the UK data center</a>.</dd></dl>

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

<dl><dt>Self-service</dt><dd>These users sit in one of Workato's US data centers and have access to our cloud-based environment for exploring Workato and building enterprise-grade automations, integrations, and AI-powered workflows that connect your applications, data, and teams.<br><a href="https://app.trial.workato.com/users/sign_in_trial">Sign in to Workato</a>.</dd></dl>

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This page provides general guidance for all Workato users. If you're a Virtual Private Workato (VPW) customer, refer to your private documentation for detailed configuration guidance specific to your instances.

> **WORKATO ACROSS REGIONS**
> 
> Each Workato account is hosted in a single regional data center. If you want to use Workato across multiple regions, you must sign up for and maintain a Workato account in each of the desired regional data centers.
> 
> Refer to the [share assets across regions](#sharing-assets) section for more information.

## Share data between regions

Workato does not share or transfer customer data across regions. Each data center independently hosts customer workspaces. Customer data in a workspace in one region cannot be shared with a workspace in a different region.

Workato collects certain kinds of data to provide services. This data may be transferred to and stored in the US. This data includes:

- In-app chat
- Support tickets and other interactions with the Workato support
- Interactions with the Workato blog
- Interactions with Workato educational offerings, like Workato Academy

Refer to the [Privacy policy](https://www.workato.com/legal/privacy-policy) for information about the data Workato collects.

> **CUSTOMER SUPPORT**
> 
> Workato maintains a globally-distributed support team to offer product support to our customers in all timezones. Refer to the [Workato Success Center](https://support.workato.com/en/support/home) to connect with the support team.

## Can I share assets across data centers?

The following cross-region interactions are not supported:

- **Cross-region user collaboration**
  
- To prevent customer data from transferring between different regions, Workato does not support cross-region collaboration. For example, a Workato user in the US data center cannot join a workspace in the EU data center as a collaborator.
  
- **Cross-region recipe sharing using a private link**
  
- Users can [generate private sharing URLs](/en/recipes/settings#share-privately) that grant access to specific recipes. Recipe sharing URLs are specific to a workspace's data center and are only accessible by other users with a workspace in the same region.
  
- **Cross-region custom connector sharing using a private link**
  
- Similar to recipe sharing, users can [generate private sharing URLs](/en/ahq-shared-connector-share) that grant access to their custom connectors. Recipe sharing URLs are specific to a workspace's data center and are only accessible by other users with a workspace in the same region.

---
