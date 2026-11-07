---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/search-records-action.md
description: >-
  The Search records action retrieves a list of records for an object in Oracle
  Object Storage that match your search criteria.
---

# Oracle Object Storage - Search records action

The **Search records** action retrieves a list of records for an object in Oracle Object Storage that match your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Record type | Specify the record type to search. Fields load dynamically based on the selected record type. |

For example, if the selected record type is **Bucket**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Compartment ID | Enter the compartment's Oracle Cloud ID (OCID) to search buckets. |
| Limit | Specify the quota for list—the maximum number of results per page. |
| Page | Specify the page number for list pagination, which is the value of the opc-next-page response header from the previous call. |
| Headers | Specify custom request headers to send with the request. Includes client request ID. |
| Fields | Select additional fields to return. |

## Output

The output fields are determined by the record type selected in the input. Map the relevant datapill from the datatree to subsequent steps. For example, selecting **Bucket** as the record type returns the following output fields:

| Output field | Description |
| --- | --- |
| Headers | Response headers. This includes the next page, client request ID, and request ID. |
| Buckets | List of buckets which match the search criteria with the following properties. |
| Compartment ID | The compartment ID is the one for which the bucket is authorized. |
| Created by | The Oracle Cloud ID (OCID) of the bucket user created. |
| Defined tags | Defined tags for this resource. |
| Entity tag | The entity tag (ETag) for the bucket. |
| Freeform tags | Free-form tags for this resource. |
| Bucket name | The name of the bucket. |
| Namespace | The Object Storage namespace is where the bucket resides. |
| Time created | The date and time the bucket was created, as described in RFC 2616. |
