---
url: 'https://docs.workato.com/en/connectors/sap-odata/actions-triggers.md'
description: >-
  Reference for the actions and triggers in the SAP OData connector, including
  create, update, search, delete, upsert, custom, and bulk data extract.
---

# SAP OData - Actions and triggers

## Actions supported

The SAP OData connector supports the following actions:

- Create object
- Update object
- Search object
- Delete object
- Upsert object
- Get object details by ID
- Custom action
- Extract bulk data
- Batch request

![actions supported](/assets/actions-odata.Dd-udO14.png)_SAP OData actions_

* * *

### Extract bulk data action

Extract bulk data action has the following limitations in comparison to search object action:

| Parameters | Search object action | Extract bulk data action |
| --- | --- | --- |
| Request timeout | Up to 120 seconds | Up to 1 hour |
| Response size | Soft response size quota of up to 200 MB | Hard response size quota of 2 GB |
| Connection types | All connection types are possible | Connections that use OPA are not supported. |
| Job processing | Jobs in the queue will be processed in order | Jobs may not be processed in order |
| Authentication | Client certificate (x509) authentication is supported | Client certificate (x509) authentication is not supported |

We recommend that you use the search object action instead of extract bulk data action and paginate the records using **Limit** and **Skip token**.

* * *

### Batch request action

This action enables customers to execute multiple CRUD (Create, Read, Update, Delete) operations in a single request, significantly improving efficiency, reliability, and cost-effectiveness.

1. Select the service. ![OData batch service selection](/assets/batch-select.iMTn5NVv.png)_Select service_
   
2. Click Add operation group. ![OData batch operation group selection](/assets/batch-operation-group.8a0SioKb.png)_Add operation group_
   
   > **FURTHER READING**
   > 
   > The uniqueness of the schema generated would be a combination of operation type and object selected for a particular service in the batch action.
   
3. Select operation type and object. ![OData batch operation type](/assets/batch-operation-type.BT2KYivR.png)_Select operation type_
   
   ![OData batch object](/assets/batch-object.C8fKcpto.png)_Select object_
   
4. Add more operation groups to be processed in batch by repeating steps 2 and 3.
   
5. For every operation group added, there will be an extended schema created where must add operation.
   
   ![OData batch operation](/assets/batch-operation.DAa_81DD.png)_Add operation_
   
6. You can add multiple operations for the same operation group with a unique operation type and object. Also, within the operation, you can add optional fields to be used for respective use-cases. ![OData batch multiple operation](/assets/batch-multiple-operations.wd73OaQz.png)_Operations_
   

* * *

### Configure actions for OData V4 services

To configure the action for an OData V4 API, you need to create a separate connection using the service URL corresponding to V4 and select V4 from the OData version drop-down on the connection page.

1. For creating an action corresponding to OData v4, navigate to the service group in the drop-down. For example, if the service URL configured in the connection is `https://<S4host>/sap/opu/odata4/sap/api_bank/srvd_a2x/sap/bank/0003/`, then the service group is `api_bank`.
   
   ![OData v4 action](/assets/odata-v4-action.be3Impgl.png)_OData v4 action_
   
   > **SERVICE GROUP NAME**
   > 
   > You can confirm the service group name in the API Business Hub documentation. Visit [SAP's documentation](https://api.sap.com/api/CE_BANK_0003/overview) and locate the **Service Group Name** in the **Attributes** tab.
   
2. As recommended practice, select the latest API version which can be identified based on the serial number like `<service name>_1`, `<service name>_2`, etc. Here, `API_BANK_3` is the latest and is corresponding to the service URL `https://<S4host>/sap/opu/odata4/sap/api_bank/srvd_a2x/sap/bank/0003/`.
   
3. If it is not shown in the drop-down due to the limited items we populate in the drop-down, then enter the **Service Name** manually. For example, if the service URL is `https://<S4host>/sap/opu/odata4/sap/api_bank/srvd_a2x/sap/bank/0003/`, then service name would be `api_bank/srvd_a2x/sap/bank/0003/`.
   
   ![OData v4 action manual](/assets/odata-v4-action-manual.BnyhGM3K.png)_Entering service name manually_
   

> **ODATA V4 API LIMITATIONS**
> 
> OData v4 API returns 100 records by default for the **Search object** action and the **Extract bulk data** action. You must adjust the `Limit` parameter in the action if you require a higher number of records.

## Triggers supported

The SAP OData connector supports the following triggers:

- New object - Triggers when an object is created in SAP.
- Updated object - Triggers when an object is updated in SAP.

![triggers supported](/assets/trigger-odata.oAE-uRE1.png)_SAP OData triggers_

---
