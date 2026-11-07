---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/create-record-action.md
description: The Create record action creates a new record in Oracle Object Storage.
---

# Oracle Object Storage - Create record action

The **Create record** action creates a new record in Oracle Object Storage.

## Input

| Input field | Description |
| --- | --- |
| Record type | Specify the record type to create. Fields load dynamically based on the selected record type. |

For example, if the selected record type is **Bucket**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Bucket name | Enter the name of the new bucket. |
| Auto tiering | Choose between standard and infrequent access modes for your objects. |
| Compartment ID | Enter the compartment's Oracle Cloud ID (OCID) to create the bucket. |
| Defined tags | Define a list of defined tags for the bucket. |
| Freeform tags | Define a list of freeform tags for the bucket. |
| KMS key ID | Enter the Oracle Cloud ID (OCID) of the master key used to generate or encrypt data keys via the Key Management service. |
| Metadata | Define key-value pairs of user-defined metadata. |
| Object events enabled | Select whether to allow events for objects inside the bucket. |
| Public access type | Choose the level of public access to the bucket. |
| Storage tier | Choose the storage tier to use for the bucket. |
| Versioning | Select whether to enable versioning for the bucket. |
| Headers | Specify custom request headers to send with the request. Includes client request ID. |

## Output

The output fields are determined by the record type selected in the input. Map the relevant datapill from the datatree to subsequent steps. For example, selecting **Bucket** as the record type returns the following output fields:

| Output field | Description |
| --- | --- |
| Headers | Response headers. |
| Approximate count | The approximate number of objects in the bucket. |
| Approximate size | The approximate total size in bytes of all objects in the bucket. |
| Approximate size multipart uploads | The approximate size of multipart uploads in the bucket. |
| Auto tiering | The auto tiering status on the bucket. |
| Compartment ID | The compartment ID is the one for which the bucket is authorized. |
| Created by | The Oracle Cloud ID (OCID) of the bucket user created. |
| Defined tags | Defined tags for this resource. |
| Entity tag | The entity tag (ETag) for the bucket. |
| Freeform tags | Free-form tags for this resource. |
| ID | The Oracle Cloud ID (OCID) of the bucket. |
| Is read only | Whether or not this bucket is read-only. |
| KMS Key ID | The Oracle Cloud ID (OCID) of a master encryption key is used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key. |
| Metadata | Arbitrary string keys and values for user-defined metadata. |
| Bucket name | The name of the bucket. |
| Namespace | The Object Storage namespace is where the bucket resides. |
| Object events enabled | Whether or not events are emitted for object state changes in this bucket. |
| Object level audit mode | Audit mode of the objects in this bucket. |
| Object lifecycle policy ETag | The entity tag (ETag) for the live object lifecycle policy on the bucket. |
| Public access type | The type of public access enabled on this bucket. |
| Replication enabled | Whether or not this bucket is a replication source. |
| Storage tier | The storage tier type assigned to the bucket. |
| Time created | The date and time the bucket was created, as described in RFC 2616. |
| Versioning | The versioning status on the bucket. |
