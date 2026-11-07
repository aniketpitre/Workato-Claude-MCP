---
url: >-
  https://docs.workato.com/en/connectors/sap-successfactors-lms/search-object-action.md
description: >-
  The Search object action in the SAP SuccessFactors LMS connector returns a
  list of objects that match your filters, with paging, offset, and count
  options.
---

# SAP SuccessFactors LMS - Search object action

The **Search object** action enables you to return the list of the objects in SAP SuccessFactors LMS that match the search criteria.

![Search object action](/assets/search-object-action.DjZXeco5.png)_Search object action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to create. Fields load dynamically based on the object you select. |
| Filters | Select the fields and their corresponding values along with the correct operator by which you plan to filter the search results. Refer to [SAP's documentation](https://help.sap.com/doc/cd753f29622244df98e335af737b5422/2405/en-US/SF_LRN_Web_Svc_Integ.pdf) for more information. |
| Page size | Specify the number of items that you plan to return in the search output. |
| Offset | Specify the number of items that you plan to skip in the search output. |
| Count | This is a boolean (yes/no) field. If you plan the output to return the total count of items present for an object, select this field as `yes`. Otherwise, select `no`. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.
