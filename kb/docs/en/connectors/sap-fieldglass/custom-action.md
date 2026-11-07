---
url: 'https://docs.workato.com/en/connectors/sap-fieldglass/custom-action.md'
description: >-
  The Custom action allows you to build and execute an HTTP request with your
  SAP Fieldglass connection.
---

# SAP Fieldglass - Custom action

The **Custom action** allows you to build and execute an HTTP request with your SAP Fieldglass connection.

![Custom action](/assets/sap-fieldglass-custom-action.CPAA77fn.png)_Custom action_

## Input

| Input Field | Description |
| --- | --- |
| Request type | Select the HTTP method of the request, such as POST, GET, PUT, or DELETE. |
| Path | Define the API endpoint path to append to the base URI. Use an absolute URI to override the base URI if necessary. |
| URL parameters | Add any required URL parameters to refine the API call. |
| Request body parameters | For actions like POST or PATCH that modify data, define the JSON structure of the data payload. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/job-posting-upload-action.md
description: >-
  The Job posting upload action enables you to upload job postings to SAP
  Fieldglass.
---

# SAP Fieldglass - Job posting upload action

The **Job posting upload** action enables you to upload job postings to SAP Fieldglass.

![Job posting upload action](/assets/sap-fieldglass-job-posting-upload-action.BCDGBCjZ.png)_Job posting upload action_

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
| Date format | Determine the date format used in the file. |
| Submit | Determine the status in which the job postings are saved. |
| MSP | Determine if the custom field present in the file is associated with the respective MSP for a multiple MSP buyer. |
| Comments | Upload comments. |

### Data

| Input fields | Description |
| --- | --- |
| Template ID | System-generated template identifier. |
| Location code | The code of the location in which this job posting is located. The location code aids suppliers in knowing where the work occurs so that appropriate candidates within that locale are submitted. |
| Start date | The date when the contract begins. |
| End date | The date when the contract ends. |
| Cost center code | The code of the cost center to which this job posting is assigned. The cost center code typically identifies to what cost center (or total estimated budget) this job posting applies and is used for accounting purposes. |
| Currency | Valid three-character currency code associated with the cost center listed in the cost center code field. Only one currency code can be given. |
| External job posting ID | An external job posting identifier for tracking purposes. |
| Site code | The code of the site in which this job posting is located. |
| Owner username | The SAP Fieldglass username of the individual who owns this specific job posting. |
| Title | The title of the position requested for this job posting. |
| Creator username | The valid SAP Fieldglass username of the individual who creates this specific job posting. |

> **OPTIONAL FIELDS**
> 
> You can specify the optional fields and [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/f87d50883f3f46b0b3d1df2cfd13aa27.html?locale=en-US#file-formatting) as required.

## Output

| Output fields | Description |
| --- | --- |
| Transaction ID | Transaction ID returned by SAP Fieldglass. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/location-download-action.md
description: >-
  The Location download action enables you to retrieve location details from SAP
  Fieldglass.
---

# SAP Fieldglass - Location download action

The **Location download** action enables you to retrieve location details from SAP Fieldglass.

![Location download action](/assets/sap-fieldglass-location-download-action.DGtdCp5p.png)_Location download action_

## Input

You can specify the [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/b8e228457f67407195dac612a212a5be.html?locale=en-US#file-formatting) that you plan to include in the result and the order that you plan to see in the result.

## Output

| Output fields | Description |
| --- | --- |
| Code | Code for the Work Location. |
| Name | Name of work location. |
| Site code | Site code of the site associated with the work location. |
| Country/region | Country/region code for the country where the location is located. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/location-upload-action.md
description: The Location upload action enables you to upload location to SAP Fieldglass.
---

# SAP Fieldglass - Location upload action

The **Location upload** action enables you to upload location to SAP Fieldglass.

![Location upload action](/assets/sap-fieldglass-location-upload-action.kZDCkbpP.png)_Location upload action_

## Input

| Input field | Description |
| --- | --- |
| Code | Provide the code for the work locations. |

> **OPTIONAL FIELDS**
> 
> You can specify the [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/82013fa8a2444e6a8a4b8ad4941f4dc6.html?locale=en-US#file-formatting) that you plan to include in the result and the order that you plan to see in the result.

## Output

| Output fields | Description |
| --- | --- |
| Transaction ID | Transaction ID returned by SAP Fieldglass. |
| Return code | Code returned by SAP Fieldglass |
| Message | Message returned by SAP Fieldglass. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/supplier-worker-download-action.md
description: >-
  The Supplier worker download action enables you to retrieve supplier worker
  details from SAP Fieldglass.
---

# SAP Fieldglass - Supplier worker download action

The **Supplier worker download** action enables you to retrieve supplier worker details from SAP Fieldglass.

![Supplier worker download action](/assets/sap-fieldglass-supplier-download-action.C8KkSaDD.png)_Supplier worker download action_

## Input

You can specify the [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/cc8db95dce20430cacdf7f887c6860bf.html?locale=en-US#file-formatting) that you plan to include in the result and the order that you plan to see in the result.

## Output

| Output fields | Description |
| --- | --- |
| Job seeker ID | SAP Fieldglass job seeker ID. |
| Worker ID | SAP Fieldglass worker ID. |
| Status | Status of the worker. |
| First name | First name of the worker as defined in SAP Fieldglass. |
| Last name | Last name of the worker as defined in SAP Fieldglass. |
| Vendor number | SAP Fieldglass supplier code. |
| Vendor name | Supplier name. |
| Buyer code | Buyer company code. |
| Remit to address code | Code as assigned to the RTA by the supplier. |
| Cost center name | Cost center name in SAP Fieldglass. |
| Cost center code | Cost center code in SAP Fieldglass. |
| Task name | Task name in SAP Fieldglass. |
| Task code | Task code in SAP Fieldglass. |
| Billable per diem | Expense amount that is billable per day. |
| Start date | Worker start date. |
| End date | Worker end date. |
| Currency | Currency designation (USD). |
| Segmented object detail | The segmented object detail feature allows buyers to accommodate complex accounting codes that need to be included with cost centers and passed to workers and work orders or SOW line items. |
| Job code | Worker’s job code. |
| Cost center start date | Worker cost center start date. Can be non-primary. |
| Cost center end date | Worker cost center end date. Can be non-primary. |
| Worker country of origin | Indicates worker's country of origin. The company configurations `Security ID format by Worker country of origin` and `Security Information` must be enabled. |
| Time zone | Time zone for the worker. If not entered, it defaults to the default setting of the buyer's time zone. |
| Discount % | Discount % from SOW Worker. |
| \[br\] Rate category / UOM | The base rate for rate category/UOM. |
| \[pr\] Rate category / UOM | Pay rate for rate category/UOM. |
| Custom fields | [Custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/cc8db95dce20430cacdf7f887c6860bf.html?locale=en-US#custom-fields) can be defined following SAP's guidelines. |

---
