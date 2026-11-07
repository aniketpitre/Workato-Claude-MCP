---
url: 'https://docs.workato.com/en/connectors/concur/actions/search-vendors-batch.md'
description: >-
  The Search vendors batch action searches for vendors in SAP Concur based on
  specified criteria.
---

# SAP Concur - Search vendors action (batch)

The **Search vendors** batch action searches for vendors in SAP Concur based on specified criteria.

## Input

| Input field | Description |
| --- | --- |
| Search type | Select the matching strategy for search parameters. Options include: Exact, Begins, Contains, Ends |
| Vendor code | Enter the vendor code to search for. |
| Address code | Enter the address code to search for. |
| Vendor name | Enter the vendor name to search for. |
| Tax ID | Enter the tax ID to search for. |
| Buyer account number | Enter the buyer account number to search for. |
| Payment method type | Select the payment method type. Options include: ACH, Card, Card voucher, Check, Client, Payment provider |
| Address 1 | Enter the first line of the street address to search for. |
| Address 2 | Enter the second line of the street address to search for. |
| Address 3 | Enter the third line of the street address to search for. |
| City | Enter the city to search for. |
| State | Enter the state or province to search for. |
| Postal code | Enter the postal code to search for. |
| Approved | Select whether to filter by vendor approval status. |
| Country | Enter the country to search for. |
| Custom 1-20 | Enter values for custom fields 1 through 20 to search for. |
| Limit | Specify the maximum number of items to return in the response. Maximum is 1000. Defaults to 25. |
| Offset | Specify the starting point for paginated results. Use with paged collections of resources. Use the offset value from the previous search result to retrieve subsequent pages. When offset is specified, other search criteria will not be used. |
| Sort direction | Select the sort direction. Options include: ascending, descending |
| Sort by | Select the field to sort results by. Defaults to `Vendor Name`. Only fields that are added to the vendor form can be used. |

## Output

| Output field | Description |
| --- | --- |
| Vendor | The primary vendor object containing vendor details. |
| Vendor code (Vendor) | The unique code for the vendor. |
| Address code (Vendor) | The code for the vendor's address. |
| Currency code (Vendor) | The three-letter ISO 4217 currency code for the vendor. |
| Account number (Vendor) | The buyer's account number with the vendor. |
| Address 1 (Vendor) | The first line of the vendor's street address. |
| Address 2 (Vendor) | The second line of the vendor's street address. |
| Address 3 (Vendor) | The third line of the vendor's street address. |
| Address import sync ID (Vendor) | The synchronization identifier for the address import. |
| Approved (Vendor) | Indicates whether the vendor is approved. |
| City (Vendor) | The city where the vendor is located. |
| Contact email (Vendor) | The email address of the vendor contact. |
| Contact first name (Vendor) | The first name of the vendor contact. |
| Contact last name (Vendor) | The last name of the vendor contact. |
| Contact phone number (Vendor) | The phone number of the vendor contact. |
| Country (Vendor) | The country where the vendor is located. |
| Country code (Vendor) | The ISO 3166-1 alpha-2 country code for the vendor. |
| Default employee ID (Vendor) | The default employee ID associated with the vendor. |
| Default expense type name (Vendor) | The default expense type name for the vendor. |
| Discount percentage (Vendor) | The discount percentage offered by the vendor. |
| Discount terms days (Vendor) | The number of days for discount terms. |
| Is line item VAT included (Vendor) | Indicates whether VAT is included in line items. |
| Is visible for content extraction (Vendor) | Indicates whether the vendor is visible for content extraction. |
| Payment method type (Vendor) | The payment method type. |
| Payment terms (Vendor) | The payment terms for the vendor. |
| Postal code (Vendor) | The postal code for the vendor's address. |
| Provincial tax ID (Vendor) | The provincial tax identifier for the vendor. |
| Purchase order contact email (Vendor) | The email address for purchase order contacts. |
| Purchase order contact first name (Vendor) | The first name of the purchase order contact. |
| Purchase order contact last name (Vendor) | The last name of the purchase order contact. |
| Purchase order contact phone number (Vendor) | The phone number for purchase order contacts. |
| Shipping method (Vendor) | The shipping method for the vendor. |
| Shipping terms (Vendor) | The shipping terms for the vendor. |
| State (Vendor) | The state or province where the vendor is located. |
| Status list (Vendor) | List of status information for the vendor. |
| Code (Status list) | The status code. |
| Message (Status list) | The status message. |
| Record number (Status list) | The record number associated with the status. |
| Type (Status list) | The type of status. |
| Tax ID (Vendor) | The tax identifier for the vendor. |
| Tax type (Vendor) | The type of tax applied to the vendor. |
| URI (Vendor) | The URI to the vendor resource. |
| Vendor form name (Vendor) | The name of the vendor form used. |
| Vendor name (Vendor) | The name of the vendor. |
| Voucher notes (Vendor) | Notes associated with vouchers for the vendor. |
| Custom 1-20 (Vendor) | Custom field values 1 through 20 for the vendor. |
| Vendor bank list (Vendor) | List of bank accounts associated with the vendor. |
| Account number (Vendor bank list) | The bank account number. |
| Account type (Vendor bank list) | The type of bank account. |
| Address code (Vendor bank list) | The address code for the bank. |
| Bank code (Vendor bank list) | The code for the bank. |
| Bank name (Vendor bank list) | The name of the bank. |
| Branch code (Vendor bank list) | The branch code of the bank. |
| Branch location (Vendor bank list) | The location of the bank branch. |
| Country code (Vendor bank list) | The country code for the bank. |
| Currency alpha code (Vendor bank list) | The three-letter currency code for the bank account. |
| ID (Vendor bank list) | The unique identifier for the bank account. |
| Is active (Vendor bank list) | Indicates whether the bank account is active. |
| Name on account (Vendor bank list) | The name on the bank account. |
| Routing number (Vendor bank list) | The routing number for the bank. |
| Status list (Vendor bank list) | Status information for the bank account. |
| Code (Status list) | The status code for the bank account. |
| Message (Status list) | The status message for the bank account. |
| Record number (Status list) | The record number associated with the bank account status. |
| Type (Status list) | The type of status for the bank account. |
| Trans type (Vendor bank list) | The transaction type for the bank account. |
| URI (Vendor bank list) | The URI to the bank account resource. |
| Vendor code (Vendor bank list) | The vendor code associated with the bank account. |
| ID (Vendor) | The unique identifier for the vendor. |
| Vendor group list (Vendor) | List of vendor groups associated with the vendor. |
| Global (Vendor group list) | Indicates whether the vendor group is global. |
| Items | List of vendor items matching the search criteria. |
| Vendor code (Items) | The unique code for the vendor. |
| Address code (Items) | The code for the vendor's address. |
| Currency code (Items) | The three-letter ISO 4217 currency code for the vendor. |
| Account number (Items) | The buyer's account number with the vendor. |
| Address 1 (Items) | The first line of the vendor's street address. |
| Address 2 (Items) | The second line of the vendor's street address. |
| Address 3 (Items) | The third line of the vendor's street address. |
| Address import sync ID (Items) | The synchronization identifier for the address import. |
| Approved (Items) | Indicates whether the vendor is approved. |
| City (Items) | The city where the vendor is located. |
| Contact email (Items) | The email address of the vendor contact. |
| Contact first name (Items) | The first name of the vendor contact. |
| Contact last name (Items) | The last name of the vendor contact. |
| Contact phone number (Items) | The phone number of the vendor contact. |
| Country (Items) | The country where the vendor is located. |
| Country code (Items) | The ISO 3166-1 alpha-2 country code for the vendor. |
| Default employee ID (Items) | The default employee ID associated with the vendor. |
| Default expense type name (Items) | The default expense type name for the vendor. |
| Discount percentage (Items) | The discount percentage offered by the vendor. |
| Discount terms days (Items) | The number of days for discount terms. |
| Is line item VAT included (Items) | Indicates whether VAT is included in line items. |
| Is visible for content extraction (Items) | Indicates whether the vendor is visible for content extraction. |
| Payment method type (Items) | The payment method type. |
| Payment terms (Items) | The payment terms for the vendor. |
| Postal code (Items) | The postal code for the vendor's address. |
| Provincial tax ID (Items) | The provincial tax identifier for the vendor. |
| Purchase order contact email (Items) | The email address for purchase order contacts. |
| Purchase order contact first name (Items) | The first name of the purchase order contact. |
| Purchase order contact last name (Items) | The last name of the purchase order contact. |
| Purchase order contact phone number (Items) | The phone number for purchase order contacts. |
| Shipping method (Items) | The shipping method for the vendor. |
| Shipping terms (Items) | The shipping terms for the vendor. |
| State (Items) | The state or province where the vendor is located. |
| Status list (Items) | List of status information for the vendor. |
| Code (Status list) | The status code. |
| Message (Status list) | The status message. |
| Record number (Status list) | The record number associated with the status. |
| Type (Status list) | The type of status. |
| Tax ID (Items) | The tax identifier for the vendor. |
| Tax type (Items) | The type of tax applied to the vendor. |
| URI (Items) | The URI to the vendor resource. |
| Vendor form name (Items) | The name of the vendor form used. |
| Vendor name (Items) | The name of the vendor. |
| Voucher notes (Items) | Notes associated with vouchers for the vendor. |
| Custom 1-20 (Items) | Custom field values 1 through 20 for the vendor. |
| Vendor bank list (Items) | List of bank accounts associated with the vendor. |
| Account number (Vendor bank list) | The bank account number. |
| Account type (Vendor bank list) | The type of bank account. |
| Address code (Vendor bank list) | The address code for the bank. |
| Bank code (Vendor bank list) | The code for the bank. |
| Bank name (Vendor bank list) | The name of the bank. |
| Branch code (Vendor bank list) | The branch code of the bank. |
| Branch location (Vendor bank list) | The location of the bank branch. |
| Country code (Vendor bank list) | The country code for the bank. |
| Currency alpha code (Vendor bank list) | The three-letter currency code for the bank account. |
| ID (Vendor bank list) | The unique identifier for the bank account. |
| Is active (Vendor bank list) | Indicates whether the bank account is active. |
| Name on account (Vendor bank list) | The name on the bank account. |
| Routing number (Vendor bank list) | The routing number for the bank. |
| Status list (Vendor bank list) | Status information for the bank account. |
| Trans type (Vendor bank list) | The transaction type for the bank account. |
| URI (Vendor bank list) | The URI to the bank account resource. |
| Vendor code (Vendor bank list) | The vendor code associated with the bank account. |
| ID (Items) | The unique identifier for the vendor. |
| Vendor group list (Items) | List of vendor groups associated with the vendor. |
| Next page | The URL to retrieve the next page of results. |
| Offset | The offset value for retrieving the next page of results. |
| Request run summary | Summary information about the request execution. |
| Total count (Request run summary) | The total number of vendors matching the search criteria. |

---

---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/submit-expense-report-through-workflow.md
description: >-
  The Submit expense report through workflow action submits an expense report
  through the workflow in SAP Concur.
---

# SAP Concur - Submit expense report through workflow action

The **Submit expense report through workflow** action submits an expense report through the workflow in SAP Concur. Check the current approval status of the expense report before submitting it through the workflow.

## Input

| Input field | Description |
| --- | --- |
| Workflowstep ID | Enter the workflow step identifier. This ID can be found in the Workflow action URL datapill of an expense report output. |
| Action | Select the workflow action to perform. Options include: Approve, Send Back to Employee, Recall to Employee |

## Output

| Output field | Description |
| --- | --- |
| Message | The error message. Only appears if a submission error was generated. |
| Status | The status of the report submit action. |

---
