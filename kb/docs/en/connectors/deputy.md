---
url: 'https://docs.workato.com/en/connectors/deputy.md'
description: >-
  The Deputy connector lets you automate workforce management: create, update,
  and search employees, create tasks, and trigger on new leave or timesheets.
---

# Deputy

[Deputy](https://deputy.com/) is an all-in-one employee scheduling, time and attendance tracking, tasking, communication, and compliance platform.

## API version

The Deputy connector uses the [Deputy V1 REST API](https://www.deputy.com/api-doc/API/) with the base URL of `https://{baseURI}.deputy.com/api/v1`.

## How to connect to Deputy on Workato

The Deputy connector supports both OAuth2.0 and permanent access token authentications.

### OAuth2.0 authentication

When authenticating through OAuth2.0, follow these steps:

1. Log into your Deputy instance using the account username and password in a separate window.
2. Select the organization accessible to Workato.

### Permanent access token authentication

To set up permanent access token authentication, follow these steps:

1. Get the [permanent token](https://www.deputy.com/api-doc/API/Authentication/) for your Deputy instance.
2. Navigate to the Workato connections setup page, and start a new connection.
3. Use the token to fill the **Permanent access token** field.
4. Specify the base URI found in the URL of your workspace in the **Endpoint** field. For example, if your workspace URL is `eafaf305033125.na.deputy.com`, then enter `eafaf305033125.na`.

## Triggers and Actions

### Triggers

- [New employee trigger](/en/connectors/deputy/new-employee-trigger)
- [New leave trigger](/en/connectors/deputy/new-leave-trigger)
- [New timesheet trigger](/en/connectors/deputy/new-timesheet-trigger)

### Actions

- [Create employee action](/en/connectors/deputy/create-employee-action)
- [Create sales data action](/en/connectors/deputy/create-sales-data-action)
- [Create resource action](/en/connectors/deputy/create-resource-action)
- [Create task action](/en/connectors/deputy/create-task-action)
- [Get resource action](/en/connectors/deputy/get-resource-action)
- [Search employees action](/en/connectors/deputy/search-employees-action)
- [Search resources action](/en/connectors/deputy/search-resources-action)
- [Search operational units action](/en/connectors/deputy/search-operational-units-action)
- [Update employee action](/en/connectors/deputy/update-employee-action)
- [Update resource action](/en/connectors/deputy/update-resource-action)
- [Associate employee action](/en/connectors/deputy/associate-employee-action)
- [Unassociate employee action](/en/connectors/deputy/unassociate-employee-action)

---
