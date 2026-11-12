---
url: 'https://docs.workato.com/en/connectors/workday/workday-faqs.md'
description: >-
  Answers to frequent questions about the Workday connector in Workato,
  including how it integrates and which service types it supports.
---

# Workday FAQs

Get answers to frequently asked questions (FAQs) about Workday.

## What is Workday and how does it integrate with Workato?

View answer

[Workday](/en/connectors/workday#workday-connector) is a cloud-based software for financial management and human capital management. You can integrate Workday with Workato to create automations and sync data between your Workday instance and other cloud applications.

## What types of services does Workday offer for integration?

View answer

Workday offers three primary types of [services for integration](/en/connectors/workday#workday-connector):

- **Workday Web Services** (SOAP APIs for reading and writing data)
- **Workday REST** (REST APIs mainly for custom objects)
- **Workday Report-as-a-Service (RaaS)** for reading data from custom reports

## What is the Workday Approved Badge?

View answer

The [Workday Approved Badge](/en/connectors/workday#workday-approved) indicates that Workato's Workday connector is officially recognized and approved by Workday for HR Onboarding/HCM use cases.

## Which API versions does Workato support for Workday services?

View answer

Workato supports multiple [versions for Workday Web Services](/en/connectors/workday#api-version), ranging from v29.0 to v40.2, and Workday REST API v1. There are no specific versions for Workday RaaS.

## How do I connect to Workday on Workato?

View answer

Basic steps to [connect to Workday](/en/connectors/workday#connection-setup) on Workato are:

- [Register an Integration System User (ISU)](/en/connectors/workday#register-integration-system-user-isu-in-workday) in Workday.
- [Register your Workday API client](/en/connectors/workday#register-a-new-api-client-for-integrations) (if working with custom objects).

## Why is it recommended to use an Integration System User (ISU) in Workday for integration?

View answer

Using an [ISU](/en/connectors/workday#connection-setup) for integration is recommended to ensure that all operations are logged under a dedicated user for integration purposes. Using an ISU also prevents disruptions in case the worker’s security profile changes or the worker is terminated.

## What are the steps to register an Integration System User in Workday for integration?

View answer

Basic steps to [register an ISU](/en/connectors/workday#register-integration-system-user-isu-in-workday) are:

- Create an Integration System Security Group.
- Grant domain access.
- Create the ISU account.
- Assign the security group to the ISU.
- Optional. Set your global preferences for language and locale.

## Is it necessary to register an API client for Workday integration?

View answer

[Registering an API client](/en/connectors/workday#register-a-new-api-client-for-integrations) is necessary if you plan to work with custom objects in Workday, as authentication for the Workday REST API requires an OAuth client setup.

## What are the different Workday connectors available in Workato and their authentication methods?

View answer

Workato offers three [Workday connectors](/en/connectors/workday#workday-connector):

- Workday connector (main)
- Workday Web Services connector
- Workday REST connector

All three connectors support OAuth 2.0 and basic authentication.

## How do I set up the Workday Web Services connector in Workato?

View answer

Basic steps to set up the [Workday Web Services](/en/connectors/workday#connection-setup) connector are:

- Provide a connection name.
- Select your Workday Web Services version.
- Provide your tenant ID, WSDL URL, and authentication credentials.
- Configure OAuth 2.0 or basic authentication.

## How is the Workday REST connector configured in Workato?

View answer

Basic steps to [configure the Workday REST connector](/en/connectors/workday-rest) are:

- Provide connection name.
- Provide a REST API endpoint, authorization endpoint, and token endpoint.
- Enter your client ID.
- Enter your client secret.

---
