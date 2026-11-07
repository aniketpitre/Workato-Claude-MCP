---
url: 'https://docs.workato.com/en/connectors/concur/actions/create-vendors-batch.md'
description: The Create vendors batch action creates multiple vendors in SAP Concur.
---

# SAP Concur - Create vendors action (batch)

The **Create vendors** batch action creates multiple vendors in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| Vendor | Provide details of the vendors to create. |
| Vendor source list (Vendor) | Provide a list datapill containing multiple vendor records. |
| Vendor code (Vendor) | Enter the vendor code for the request. |
| Address code (Vendor) | Enter the address code. |
| Currency code (Vendor) | Select the vendor currency code. |
| Account number (Vendor) | Enter the buyer account number. |
| Address 1 (Vendor) | Enter the vendor address line 1. |
| Address 2 (Vendor) | Enter the vendor address line 2. |
| Address 3 (Vendor) | Enter the vendor address line 3. |
| Address import sync ID (Vendor) | Enter the address import synchronization identifier. |
| Approved (Vendor) | Specify the vendor approval status. |
| City (Vendor) | Enter the vendor city. |
| Contact email (Vendor) | Enter the vendor contact email address. |
| Contact first name (Vendor) | Enter the vendor contact first name. |
| Contact last name (Vendor) | Enter the vendor contact last name. |
| Contact phone number (Vendor) | Enter the vendor contact phone number. |
| Country (Vendor) | Enter the vendor country. |
| Country code (Vendor) | Enter the vendor country code. |
| Default employee ID (Vendor) | Enter the default employee ID of the employee connected to the vendor. |
| Default expense type name (Vendor) | Enter the default expense type tied to the vendor. |
| Discount percentage (Vendor) | Enter the discount percentage. |
| Discount terms days (Vendor) | Enter the vendor discount terms in days. |
| Is line item VAT included (Vendor) | Specify whether the line item unit price contains VAT. |
| Is visible for content extraction (Vendor) | Specify whether the vendor is available for OCR within brainware. |
| Payment method type (Vendor) | Select the preferred payment type for the vendor. |
| Payment terms (Vendor) | Enter the vendor payment terms. Specify the number of days by which a payment must be made. For example, 30 days. |
| Postal code (Vendor) | Enter the vendor postal code or zip code. |
| Provincial tax ID (Vendor) | Enter the vendor provincial tax ID. Note that this value is not encrypted at REST. |
| Purchase order contact email (Vendor) | Enter the purchase order contact email address. |
| Purchase order contact first name (Vendor) | Enter the purchase order contact first name. |
| Purchase order contact last name (Vendor) | Enter the purchase order contact last name. |
| Purchase order contact phone number (Vendor) | Enter the purchase order contact phone number. |
| Shipping method (Vendor) | Enter the vendor shipping method. |
| Shipping terms (Vendor) | Enter the vendor shipping terms. |
| State (Vendor) | Enter the vendor state. |
| Status list (Vendor) | Provide the status list for the vendor operation. |
| Status list source list (Status list) | Provide a list datapill containing status records. |
| Code (Status list) | Enter the code of the request result. |
| Message (Status list) | Enter the message of the request result. |
| Record number (Status list) | Enter the record number for the create or update request. |
| Type (Status list) | Enter the type of the request result. |
| Tax ID (Vendor) | Enter the vendor tax ID. Note that this value is not encrypted at REST. |
| Tax type (Vendor) | Enter the vendor tax type. |
| URI (Vendor) | Enter the URI to the vendor resource. |
| Vendor form name (Vendor) | Enter the vendor form name this vendor is associated with. |
| Vendor name (Vendor) | Enter the name of the vendor. |
| Voucher notes (Vendor) | Enter notes to send to the vendor along with authorization to charge the card voucher. |
| Custom 1-20 (Vendor) | Enter values for custom fields 1-20 that are part of the vendor form. |

## Output

| Output field | Description |
| --- | --- |
| Vendors | The collection of vendor objects. |
| Vendor code (Vendors) | The vendor code of the request. |
| Address code (Vendors) | The address code. |
| Currency code (Vendors) | The vendor currency code. |
| Account number (Vendors) | The buyer account number. |
| Address 1 (Vendors) | The vendor address 1. |
| Address 2 (Vendors) | The vendor address 2. |
| Address 3 (Vendors) | The vendor address 3. |
| Address import sync ID (Vendors) | The address import synchronization identifier. |
| Approved (Vendors) | Vendor approval status. |
| City (Vendors) | The vendor city. |
| Contact email (Vendors) | The vendor contact email. |
| Contact first name (Vendors) | The vendor contact first name. |
| Contact last name (Vendors) | The vendor contact last name. |
| Contact phone number (Vendors) | The vendor contact phone number. |
| Country (Vendors) | The vendor country. |
| Country code (Vendors) | The vendor country code. |
| Default employee ID (Vendors) | The default employee ID of the employee connected to the vendor. |
| Default expense type name (Vendors) | The default expense type tied to the vendor. |
| Discount percentage (Vendors) | The discount percentage. |
| Discount terms days (Vendors) | The vendor discount terms days. |
| Is line item VAT included (Vendors) | Flag that indicates if the line item unit price contains VAT. |
| Is visible for content extraction (Vendors) | Flag that indicates if the vendor is available for OCR within brainware. |
| Payment method type (Vendors) | Preferred payment type for vendor. |
| Payment terms (Vendors) | The vendor payment terms. |
| Postal code (Vendors) | The vendor postal code or zip. |
| Provincial tax ID (Vendors) | The vendor provincial tax ID. |
| Purchase order contact email (Vendors) | The purchase order contact email. |
| Purchase order contact first name (Vendors) | The purchase order contact first name. |
| Purchase order contact last name (Vendors) | The purchase order contact last name. |
| Purchase order contact phone number (Vendors) | The purchase order contact phone number. |
| Shipping method (Vendors) | The vendor shipping method. |
| Shipping terms (Vendors) | The vendor shipping terms. |
| State (Vendors) | The vendor state. |
| Status list (Vendors) | The status results of the operation. |
| Code (Status list) | The status code of the request result. |
| Message (Status list) | The status message of the request result. |
| Record number (Status list) | The record number for create or update request. |
| Type (Status list) | The type of request result. |
| Tax ID (Vendors) | The vendor tax ID. |
| Tax type (Vendors) | The vendor tax type. |
| URI (Vendors) | The URI to the vendor resource. |
| Vendor form name (Vendors) | The vendor form name this vendor is associated with. |
| Vendor name (Vendors) | The name of the vendor. |
| Voucher notes (Vendors) | Notes sent to vendor along with authorization to charge card voucher. |
| Custom 1-20 (Vendors) | Custom field values for Custom 1-20 that are part of the vendor form. |
| Vendor bank list (Vendors) | The list of vendor bank accounts. |
| Account number (Vendor bank list) | The bank account number. |
| Account type (Vendor bank list) | The bank account type. |
| Address code (Vendor bank list) | The address code. |
| Bank code (Vendor bank list) | The bank code. |
| Bank name (Vendor bank list) | The bank name. |
| Branch code (Vendor bank list) | The branch code. |
| Branch location (Vendor bank list) | The branch location. |
| Country code (Vendor bank list) | The country code. |
| Currency alpha code (Vendor bank list) | The currency alpha code. |
| ID (Vendor bank list) | The unique identifier of the bank account. |
| Is active (Vendor bank list) | Indicates whether the bank account is active. |
| Name on account (Vendor bank list) | The name on the bank account. |
| Routing number (Vendor bank list) | The bank routing number. |
| Status list (Vendor bank list) | The status results for the bank account operation. |
| Code (Status list) | The status code of the request result. |
| Message (Status list) | The status message of the request result. |
| Record number (Status list) | The record number for create or update request. |
| Type (Status list) | The type of request result. |
| Trans type (Vendor bank list) | The transaction type. |
| URI (Vendor bank list) | The URI to the bank account resource. |
| Vendor code (Vendor bank list) | The vendor code associated with the bank account. |
| ID (Vendors) | The unique identifier for the vendor. |
| Vendor group list (Vendors) | The list of vendor groups the vendor belongs to. |
| Items | The collection of all vendor results. |
| Next page | The URI of the next page of results, if any. |
| Request run summary | Summary information about the request execution. |
| Total count | The total count of vendors in the result set. |

---
