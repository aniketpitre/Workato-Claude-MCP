---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/profile-worker-upload-action.md
description: >-
  The Profile worker upload action lets you upload profile worker details to SAP
  Fieldglass.
---

# SAP Fieldglass - Profile worker upload action

The **Profile worker upload** action lets you upload profile worker details to SAP Fieldglass.

![Profile worker upload action](/assets/sap-fieldglass-profile-worker-action.CyiYs1N2.png)_Profile worker upload action_

## Input

### Header

| Input fields | Description |
| --- | --- |
| Type | Specify the upload file type. |
| Transaction | Specify the transaction type. |
| Approval required | Determine if approval rules must be followed. |
| Send notification? | Determine whether normal messaging workflow must be followed. |
| Language | Determine the language used for values in the file, such as drop-down lists and radio buttons. Column headers default to the upload user's preferred language. |
| Number format | Determine the number format used in the file. |
| Date format | Determines the date format used in the file. |
| Submit | Determine the status in which the job postings are saved. |
| MSP | Determine if the custom field present in the file is associated with the respective MSP for a multiple MSP buyer. |
| Comments | Upload comments. |

### Data

| Input fields | Description |
| --- | --- |
| Supplier Code | SAP Fieldglass supplier code for the buyer. |
| First name | First name of profile worker. |
| Last name | Last name of profile worker. |
| Email Address | Email address of the profile worker. |
| Primary Contact Username | Username of profile worker's SAP primary contact. |
| Cost center code | Associated cost center code for the profile worker. |
| Business unit code | Provide the associated business unit code for the profile worker. |
| Site code | Provide the associated site code for the profile worker. |
| Location code | Provide the associated location code for the profile worker. |
| Start date | Provide the start date of the profile worker. |
| End date | Provide the end date of the profile worker. |
| Security ID | Provide the security ID of the profile worker, if applicable to the buyer. |
| Legal Entity Code | Indicate the legal entity code associated with the profile worker. |
| MSP Code | A valid MSP code for the given supplier. |

> **OPTIONAL FIELDS**
> 
> You can specify the optional fields and [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/9295ed71eb394deab835b56d54af07fe.html?locale=en-US#file-formatting) as well, as per the requirement.

## Output

| Output fields | Description |
| --- | --- |
| Transaction ID | Transaction ID returned by SAP Fieldglass. |
