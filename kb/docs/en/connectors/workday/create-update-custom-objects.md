---
url: 'https://docs.workato.com/en/connectors/workday/create-update-custom-objects.md'
description: >-
  The Create/Update custom object action in the Workday connector lets you
  create or update a custom object value on a Workday record.
---

# Workday - Create/Update custom object action

You can extend Workday business objects by configuring custom objects. These custom objects are based on default Workday and can store additional custom fields. Custom objects enable you to record additional data which is not captured by the default Workday objects.

This action allows you to create or update custom object values to a Workday record. If the parent object does not have the specified custom object record, this action will create one. Otherwise, it will update the custom object record with the values provided.

#### Example

For example, we are setting a new onboarding process for our employee. Every employee has to undergo a drug test. On Workday, we set up a custom object called **drugTested** under the parent object **Workers**.

We can use this action to assign a status to a worker. If a worker does not previously have a **drugTested** status, this action will create the custom object for this worker.

Otherwise, if this worker already has a **drugTested** object (for example, `True`/`False`), this action will update the custom object with a new value.

## Inputs

![Create/update custom object action](/assets/create-custom-object-action.CuGIRLfl.png)_Create/update custom object action_

| Input field | Description |
| --- | --- |
| Is multi-instanced? | Custom objects in Workday can be single-instanced or multi-instanced. An example of multi-instanced custom object is a worker's COVID19 vaccination records, whereas an example of single-instanced custom object is whether worker is allowed to work from home. Set this to Yes if custom object being fetched is multi-instanced. |
| Parent object | The name of the parent object. You may find the list of acceptable values in the [supported parent objects](/en/connectors/workday/create-update-custom-objects#supported-parent-objects) section below. |
| Custom object fields | Define the fields in this custom object. If left blank, it will retrieve all fields with their default names. |
| Parent object ID | The Workday ID of the parent object that you are selecting. |
| Custom object name | The web service alias of custom object that you want to attach to the parent object. |

![Example of single-instanced and multi-instanced custom object](/assets/multi-instanced-custom-object.D8Q4uRhT.png)_Example of single-instanced and multi-instanced custom object_

The input schema of the custom object will be automatically generated. You may also override or redefine the schema using the optional "Custom object fields" schema designer.

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

For example, for worker `6b36787a2e6301e185df0a95ff272a04` who has passed their drug test, we will use the **Create/update custom object** action and define it like so:

- Parent object name: `workers`
- Custom object: `drugTested`
- Custom object field (Drug tested): `True`
- Parent object ID: `6b36787a2e6301e185df0a95ff272a04`

## Outputs

There are no output for this action.

You can check the custom object status of your worker with a [Get custom object action](/en/connectors/workday/get-custom-objects).

---
