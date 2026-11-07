---
url: 'https://docs.workato.com/en/connectors/ukg-pro/overview.md'
description: >-
  Set up and connect UKG Pro in Workato using API token credentials, including
  creating a service account API key and configuring permissions.
---

# UKG Pro

[UKG Pro](https://www.ultimatesoftware.com/hcm-solutions) is an industry-leading HCM tool that helps enterprises manage the entire employee life cycle. This connector allows you to automate recruitment, employee onboarding and offboarding processes so your team can focus on making a truly immersive employee experience.

The UKG Pro connector allows you to **trigger off and retrieve data in UKG Pro**. Use the [UKG Pro SOAP connector](/en/connectors/ukg-pro-soap) to create or update data in UKG Pro.

## API version

This connector uses [UKG Pro API v1](https://connect.ultipro.com/documentation#/api/).

## How to create an API key on UKG Pro

It is recommended to use an Integration System User (ISU) for integration with Workato. This ensures that permissions are consistent and all operations can be logged on a single account. This can be done using a service account on UKG Pro.

1. Navigate to Menu > System Configuration > Security > Service Account Administration. ![View service accounts](/assets/view-service-account.BzefxTB8.png)_View UKG Pro service accounts_
   
2. Create a new service account for Workato. Select **Add**. ![Create service account](/assets/add-service-account.li-Bq0Qp.png)_Create a service account for Workato_
   
3. Provide the necessary permissions to this API key. For the Workato integration, the service account must have **View** permission for **Company Configuration Integration**. Refer to the UKG Pro [service account permissions](https://learningcenter.ultimatesoftware.com/a/179488) documentation for more information. ![Select service account permissions](/assets/service-accounts-add-permissions.BRsifZHy.png)_Select service account permissions_
   

## How to connect to UKG Pro on Workato

Create a Workato connection to your UKG Pro instance using API token credentials.

| Input field | Description |
| --- | --- |
| Connection name | Give this connection a unique name that identifies which instance it is connected to. |
| Username | The user connecting to this UKG Pro instance. Refer to the UKG Pro [service account](https://learningcenter.ultimatesoftware.com/a/179488) documentation to learn how to create a service account. |
| Password | The password to the account. |
| API URL | The base API URL. If the Login endpoint is: `http://service.ultipro.com/services/LoginService`. The base API URL will be: `http://service.ultipro.com`. |
| Customer API key | The customer API key for the master company. |

## Permissions

Ensure that you give this API credential the necessary permission. If permissions are not configured correctly, certain actions/triggers may not work as intended - even if the connection is successful. See the required permissions below.

To operate on employee objects, it is recommended to have the following permissions enabled (View, Add, Edit).

- Company Configuration Integration
- Employee Person Details
- Employee Employment Information
- Employee job
- Employee contacts
- Employee Compensation Details
- PTO Plan Integration
- Employee Job History Details
- Personnel Integration
- Employee Export
- Global Employee Direct Deposit

## Triggers and actions

You can browse the other chapters:

### UKG Pro triggers

- [New/updated employee trigger](/en/connectors/ukg-pro/updated-employee-trigger)
- [New record trigger](/en/connectors/ukg-pro/new-record-trigger)
- [New/update record trigger](/en/connectors/ukg-pro/updated-record-trigger)
- [Terminated employee](/en/connectors/ukg-pro/terminated-employee-trigger)

### UKG Pro actions

- [Create record action](/en/connectors/ukg-pro/create-record-action)
- [Get record action](/en/connectors/ukg-pro/get-record-action)
- [Update record action](/en/connectors/ukg-pro/update-record-action)
- [Search record action](/en/connectors/ukg-pro/search-record-action)

---
