---
url: 'https://docs.workato.com/en/connectors/sap-fieldglass/worker-upload-action.md'
description: The Worker upload action enables you to upload workers to SAP Fieldglass.
---

# SAP Fieldglass - Worker upload action

The **Worker upload** action enables you to upload workers to SAP Fieldglass.

![Worker upload action](/assets/sap-fieldglass-worker-upload-action.Buwmg6_5.png)_Worker upload action_

## Input

### Header

| Input fields | Description |
| --- | --- |
| Transaction | Specify the transaction type. |
| Language | Determines the language used for values in the file, such as drop-down lists and radio buttons. Column headers default to the upload user's preferred language. |
| Number format | Determines the number format used in the file. |
| Date format | Determines the date format used in the file. |
| Comments | Upload comments. |

### Data

| Input fields | Description |
| --- | --- |
| Object ID | SAP Fieldglass supplier code for the buyer. |
| First name | First name of profile worker. |
| Last name | Last name of profile worker. |
| Email | Email address of the profile worker. |
| Username | Username of profile worker's SAP primary contact. |
| Calendar Start Day | Start date of the profile worker. |
| Current worker | End date of the profile worker. |

> **CUSTOM FIELDS**
> 
> You can specify the optional fields and [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/a5233e50114248c997e0e10d2f1431e7.html?locale=en-US#file-formatting) as required.

## Output

| Output fields | Description |
| --- | --- |
| Transaction ID | Transaction ID returned by SAP Fieldglass. |

---
