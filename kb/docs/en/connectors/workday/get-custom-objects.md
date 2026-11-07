---
url: 'https://docs.workato.com/en/connectors/workday/get-custom-objects.md'
description: >-
  The Get custom object action in the Workday connector lets you retrieve a
  custom object value for a specific Workday business object.
---

# Workday - Get custom object action

You can extend Workday business objects by configuring custom objects. These custom objects are based standard Workday business objects and can be used to store additional information. This allows you to capture data unique to your organization in Workday. This action allows you to retrieve a custom object value of a specific Workday object.

#### Example

For example, we are setting a new onboarding process for our employee. Every employee has to undergo a drug test. On Workday, we set up a custom object called **drugTested** under the parent object **Workers**.

We can use this action to check if a drug test has been conducted for this worker.

## Inputs

![Get custom objects action](/assets/get-custom-object.DuhWim4n.png)_Get custom objects action_

| Input field | Description |
| --- | --- |
| Alias | Select the custom object that you want to retrieve. This is the Web service alias. |
| Parent object ID | The Workday ID of the parent object that you are selecting. |
| Custom object fields | Define the fields in this custom object. If left blank, it will retrieve all fields with their default names. |
| Is multi-instanced? | Custom objects in Workday can be single-instanced or multi-instanced. An example of multi-instanced custom object is a worker's COVID19 vaccination records, whereas an example of single-instanced custom object is whether worker is allowed to work from home. Set this to Yes if custom object being fetched is multi-instanced. |

![Example of single-instanced and multi-instanced custom object](/assets/multi-instanced-custom-object.D8Q4uRhT.png)_Example of single-instanced and multi-instanced custom object_

### Supported parent objects

Workday supports extending the following list of objects with custom objects:

- academicAffiliates
- academicUnits
- academicUnitHierarchies
- bankAccounts
- businessAssets
- companies
- costCenters
- customers
- customerContracts
- customerContractLines
- customerInvoices
- customerInvoiceAdjustments
- employeeContracts
- formerWorkers
- jobProfiles
- ledgerAccounts
- loans
- locations
- positionRestrictions
- projects
- applicants
- purchaseOrders
- regions
- supervisoryOrganizations
- suppliers
- supplierContracts
- supplierInvoices
- supplierInvoiceAdjustments
- workers

#### Example

Let's us assume that there can only be one instance of drug test status for each worker. To retrieve the drug test status of Worker `1da8b422311b4929bfa4520f7f0b4e83`, we will use the **Get custom object** action and define it like so:

- Alias: `drugTested`
- Parent object ID: `1da8b422311b4929bfa4520f7f0b4e83`
- Is multi-instanced?: `No`

## Outputs

The outputs of this action can be one/more instances of the custom object, depending on whether the object is single- or multi-instanced. The contents of each instance are as follows:

| Output field | Description |
| --- | --- |
| ID | A unique Workday ID for this custom object. |
| Custom field values | The values for the custom fields belonging to this specific Workday object. |

Each field is retrieved and converted into a datapill. These can be used in subsequent recipe actions.

> **Parent object ID**
> 
> If the parent object does not contain the custom object, this action will return `Error 404: Not found`.

---
