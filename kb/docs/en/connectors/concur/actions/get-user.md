---
url: 'https://docs.workato.com/en/connectors/concur/actions/get-user.md'
description: The Get user action retrieves information about a specific user in SAP Concur.
---

# SAP Concur - Get user action

The **Get user** action retrieves information about a specific user in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| User ID | Enter the unique identifier of the SAP Concur user. |

## Output

| Output field | Description |
| --- | --- |
| Locale overrides | Custom locale settings that override default preferences. |
| Preference end day view hour (Locale overrides) | The ending hour for day view. |
| Preference first day of week (Locale overrides) | The first day of the week preference. |
| Preference date format (Locale overrides) | The date display pattern preference. |
| Preference currency symbol location (Locale overrides) | The currency symbol position preference. |
| Preference hour minute separator (Locale overrides) | The separator used between hours and minutes. |
| Preference distance (Locale overrides) | The preferred unit of distance measurement. |
| Preference default cal view (Locale overrides) | The default calendar view preference. |
| Preference 24 hour (Locale overrides) | The time display format preference. |
| Display name format (Locale overrides) | The format used for displaying names. |
| Preference number format (Locale overrides) | The numeric display standard preference. |
| Preference start day view hour (Locale overrides) | The starting hour for day view. |
| Preference negative currency format (Locale overrides) | The format for displaying negative currency values. |
| Preference negative number format (Locale overrides) | The format for displaying negative numbers. |
| Addresses | List of addresses associated with the user. |
| Street address (Addresses) | The full street location. |
| Locality (Addresses) | The city designation. |
| Region (Addresses) | The state or province code. |
| Country (Addresses) | The ISO 3166-1 alpha-2 country code. |
| Postal code (Addresses) | The zip or postal code. |
| Type (Addresses) | The function label for the address. |
| Timezone | The user's timezone in Olson format. |
| Meta | Metadata about the user resource. |
| Created (Meta) | The timestamp when the user was created. |
| Last modified (Meta) | The timestamp of the last modification to the user. |
| Resource type (Meta) | The type of resource. Value is User. |
| Version (Meta) | The version number of the user record. |
| Location (Meta) | The URL for retrieving the user's details. |
| Provision ID | A unique number used for querying the provisioning status. |
| Status URL | The URL for checking the provisioning status. |
| Locale | The locale setting for the user. |
| Display name | The public-facing name combining given and family names. |
| Entitlements | The entitlements assigned to the user. |
| Name | The full name of the user. |
| Middle initial (Name) | The middle initial abbreviation. |
| Middle name (Name) | The middle name of the user, if applicable. |
| Formatted (Name) | The complete name formatted for display purposes. |
| Honorific prefix (Name) | A title or prefix. |
| Legal name (Name) | The official legal name designation. |
| Family name (Name) | The last name of the user. |
| Given name (Name) | The first name of the user. |
| Honorific suffix (Name) | A suffix designation. |
| Academic title (Name) | The academic title of the user. |
| Family name prefix (Name) | A prefix to the family name. |
| Phone numbers | List of phone numbers associated with the user. |
| Value (Phone numbers) | The phone number. |
| Display (Phone numbers) | The human-readable format of the phone number. |
| Type (Phone numbers) | The category of the phone number. |
| Primary (Phone numbers) | Indicates whether this is the primary mobile number. |
| Notifications (Phone numbers) | The alert subscription status for this phone number. |
| Issuing country | The issuing country for the user. |
| Work extension | The work phone extension. |
| Emergency contacts | List of emergency contact information for the user. |
| Locality (Emergency contacts) | The city of the emergency contact. |
| Name (Emergency contacts) | The contact's full name. |
| Relationship (Emergency contacts) | The connection type. |
| Street address (Emergency contacts) | The physical location of the emergency contact. |
| Region (Emergency contacts) | The state or province of the emergency contact. |
| Phones (Emergency contacts) | The contact phone numbers. |
| Postal code (Emergency contacts) | The postal code of the emergency contact. |
| Emails (Emergency contacts) | The contact email addresses. |
| Country (Emergency contacts) | The country of the emergency contact. |
| Preferred language | The user's preferred language code. |
| Title | The user's job title. |
| Date of birth | The user's date of birth in YYYY-MM-DD format. |
| Nick name | The user's nickname or preferred casual name. |
| External ID | An identifier from the provisioning client. |
| Active | Indicates whether the user account is active. |
| ID | The unique identifier (UUID) for the user. |
| Emails | List of email addresses associated with the user. |
| Value (Emails) | The email address. |
| Verified (Emails) | Indicates whether the email has been verified. |
| Type (Emails) | The category of email. |
| Notifications (Emails) | The email notification opt-in status. |
| User name | The login name in user@domain format. |
| Enterprise user | Attributes representing the user as an enterprise employee. |
| Employee number (Enterprise user) | Client-supplied unique employee identifier. |
| Department (Enterprise user) | The client-supplied department name. |
| Division (Enterprise user) | The client-supplied division name. |
| Start date (Enterprise user) | The employee start date in ISO 8601 format. |
| Organization (Enterprise user) | The company name. |
| Cost center (Enterprise user) | The employee cost center designation. |
| Leaves of absence (Enterprise user) | List of leave periods for the user. |
| Start date (Leaves of absence) | The leave start date in YYYY-MM-DD format. |
| End date (Leaves of absence) | The leave end date in YYYY-MM-DD format. |
| Type (Leaves of absence) | The leave category. |
| Manager (Enterprise user) | The user's manager information. |
| Value (Manager) | The unique identifier (UUID) of the manager. |
| $ref (Manager) | The reference URL to the manager's profile. |
| Display name (Manager) | The display name of the manager. |
| Employee number (Manager) | The employee number of the manager. |
| Termination date (Enterprise user) | The employee termination date in ISO 8601 format. |
| Legal entity | The legal entity information. |
| Travel user | Travel-specific user attributes. |
| Rule class (Travel user) | The travel class information. |
| ID (Rule class) | The unique identifier of the travel class. |
| Name (Rule class) | The name of the travel class. |
| Name prefix (Travel user) | The name prefix for travel purposes. |
| Has no middle name (Travel user) | Indicates whether the user has a middle name. |
| Travel name remark (Travel user) | A remark about the traveler's name. |
| Gender (Travel user) | The gender designation for travel purposes. |
| Org unit (Travel user) | The organizational unit code. |
| Xml profile sync ID (Travel user) | The XML profile synchronization identifier. |
| Travel crs name (Travel user) | The CRS/GDS name for the traveler. |
| Groups (Travel user) | List of travel group identifiers. |
| Permissions (Travel user) | Travel permissions assigned to the user. |
| Travel user (Permissions) | Indicates travel user permission. |
| Open booking user (Permissions) | Indicates open booking permission. |
| Profile user (Permissions) | Indicates profile access permission. |
| Custom fields (Travel user) | List of custom fields for travel. |
| Spend user | Spend-specific user attributes. |
| Bi hierarchy (Spend user) | Business intelligence reporting hierarchy information. |
| Code (Bi hierarchy) | The reporting hierarchy long code. |
| Href (Bi hierarchy) | The hierarchy resource URI. |
| Sync guid (Bi hierarchy) | The hierarchy synchronization identifier. |
| Bi manager (Spend user) | The reporting manager for business intelligence purposes. |
| Display name (Bi manager) | The display name of the BI manager. |
| Employee number (Bi manager) | The employee number of the BI manager. |
| Budget country code (Spend user) | The budget country code. |
| Cash advance account code (Spend user) | The cash advance account identifier. |
| Country (Spend user) | The ISO 3166 country code. |
| Ledger code (Spend user) | The associated ledger code. |
| Locale (Spend user) | The locale from the list of configured locales. |
| Non employee (Spend user) | Indicates whether the user is a non-employee. |
| Reimbursement currency (Spend user) | The three-digit currency code for reimbursements. |
| Reimbursement type (Spend user) | The reimbursement method. |
| Custom data (Spend user) | List of custom field values. |
| Href (Custom data) | The URI to the list item if the field is a list type. |
| ID (Custom data) | The custom field identifier. |
| Sync guid (Custom data) | The synchronization identifier for the custom field. |
| Value (Custom data) | The field value or list item code. |
| State province (Spend user) | The ISO sub country code. |
| Test employee (Spend user) | Indicates whether this is a test user. |
| Spend user preference | User preferences for spend features. |
| Allow auto create trip report (Spend user preference) | Allow automatic trip report creation. |
| Allow credit card trans arrival emails (Spend user preference) | Allow credit card transaction arrival email notifications. |
| Allow receipt image avail emails (Spend user preference) | Allow receipt image availability email notifications. |
| Auto add trip card trans on report (Spend user preference) | Automatically add trip card transactions to reports. |
| Enable ocr for email (Spend user preference) | Enable OCR processing for email receipts. |
| Enable ocr for ui (Spend user preference) | Enable OCR processing for UI-uploaded receipts. |
| Enable trip based assistant (Spend user preference) | Enable trip-based assistant features. |
| Expense audit required (Spend user preference) | The audit requirement level. |
| Processor report access (Spend user preference) | The processor report access level. |
| Prompt for card transactions on report (Spend user preference) | Prompt user for card transactions when creating reports. |
| Use quick itin as default (Spend user preference) | Use quick itinerary as the default. |
| Show expense on report (Spend user preference) | The expense display mode. |
| Default report print format (Spend user preference) | The default print format. |
| Prompt for report print format (Spend user preference) | Prompt user for print format selection. |
| Show total on report (Spend user preference) | Display the total on reports. |
| Show imaging intro (Spend user preference) | Display the imaging introduction. |
| Show instruct help panel (Spend user preference) | Display the instruction help panel. |
| Spend workflow preference | Workflow notification preferences for spend activities. |
| Email await approval on cash advance (Spend workflow preference) | Send email notifications when cash advance awaits approval. |
| Email status change on cash advance (Spend workflow preference) | Send email notifications on cash advance status changes. |
| Email await approval on payment (Spend workflow preference) | Send email notifications when payment awaits approval. |
| Email status change on payment (Spend workflow preference) | Send email notifications on payment status changes. |
| Email on purchase request await approval (Spend workflow preference) | Send email notifications when purchase request awaits approval. |
| Email on purchase request status change (Spend workflow preference) | Send email notifications on purchase request status changes. |
| Email await approval on report (Spend workflow preference) | Send email notifications when report awaits approval. |
| Email status change on report (Spend workflow preference) | Send email notifications on report status changes. |
| Email await approval on travel request (Spend workflow preference) | Send email notifications when travel request awaits approval. |
| Email status change on travel request (Spend workflow preference) | Send email notifications on travel request status changes. |
| Prompt for approver on report submit (Spend workflow preference) | Prompt for approver selection when submitting reports. |
| Prompt for approver on payment submit (Spend workflow preference) | Prompt for approver selection when submitting payments. |
| Prompt for purchase request approver on submit (Spend workflow preference) | Prompt for approver selection when submitting purchase requests. |
| Prompt for approver on travel request submit (Spend workflow preference) | Prompt for approver selection when submitting travel requests. |
| Spend role | Roles assigned to the user in the spend system. |
| Roles (Spend role) | List of role assignments. |
| Role groups (Spend role) | The role groups associated with the role. |
| Role name (Spend role) | The identifier of the role. |
| Spend delegate | Delegate permissions for spend activities. |
| Expense (Spend delegate) | Expense delegation settings. |
| Can approve (Expense) | Permission to approve expenses on behalf of the user. |
| Can prepare (Expense) | Permission to prepare expenses on behalf of the user. |
| Can prepare for approval (Expense) | Permission to prepare expenses for approval. |
| Can receive approval email (Expense) | Permission to receive approval email notifications. |
| Can receive email (Expense) | Permission to receive general email notifications. |
| Can submit (Expense) | Permission to submit expenses on behalf of the user. |
| Can submit travel request (Expense) | Permission to submit travel requests. |
| Can use bi (Expense) | Permission to access business intelligence features. |
| Can view receipt (Expense) | Permission to view receipts. |
| Delegate (Expense) | The delegate user information. |
| Display name (Delegate) | The display name of the delegate. |
| Employee number (Delegate) | The employee number of the delegate. |
| $ref (Delegate) | The reference URL to the delegate's profile. |
| Value (Delegate) | The unique identifier of the delegate. |
| Temporary delegation (Expense) | Indicates if the delegation is temporary. |
| Temporary delegation from date (Expense) | The start date for temporary delegation. |
| Temporary delegation to date (Expense) | The end date for temporary delegation. |
| Purchase request (Spend delegate) | Purchase request delegation settings. |
| Invoice (Spend delegate) | Invoice delegation settings. |
| Delegate prod code(deprecated) (Spend delegate) | Deprecated delegation code. |
| Spend approver | Approver assignments for various spend activities. |
| Request (Spend approver) | Approvers for requests. |
| Approver (Request) | The approver information. |
| Display name (Approver) | The display name of the approver. |
| Employee number (Approver) | The employee number of the approver. |
| $ref (Approver) | The reference URL to the approver's profile. |
| Value (Approver) | The unique identifier (UUID) of the approver. |
| Primary (Approver) | Indicates whether this is the primary approver. |
| Report (Spend approver) | Approvers for expense reports. |
| Statement (Spend approver) | Approvers for statements. |
| Cash advance (Spend approver) | Approvers for cash advances. |
| Purchase request (Spend approver) | Approvers for purchase requests. |
| Budget (Spend approver) | Approvers for budget items. |
| Invoice (Spend approver) | Approvers for invoices. |
| Approver type(deprecated) (Spend approver) | Deprecated approver type field. |
| Enterprise payroll | Payroll integration information. |
| Adp (Enterprise payroll) | ADP payroll integration details. |
| Company code (Adp) | The payroll company code. |
| Deduction code (Adp) | The payroll deduction code. |
| Employee file number (Adp) | The payroll employee file identifier. |

---

---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-user-provisioning-status-details.md
description: >-
  The Get user provisioning status details action retrieves a detailed status
  report for a provisioning request.
---

# SAP Concur - Get user provisioning status details action

The **Get user provisioning status details** action retrieves a detailed status report for a provisioning request. The provisioning status is stored for seven days from the provisioning request date.

## Input

| Input field | Description |
| --- | --- |
| Provision ID | Enter the unique identifier of the provisioning request. |
| Start index | Specify the 1-based index of the first query result. |
| Count | Specify the desired number of operations per page. |
| State | Select the state to filter results. Options include: Pending, Success, Failed |

## Output

| Output field | Description |
| --- | --- |
| Schemas | SCIM schema identifiers for the response. |
| ID | The provisioning request ID. This is a unique number used for querying status. |
| Meta | Metadata information about the provisioning request. |
| Location (Meta) | The location URL to receive status on the provisioning request. |
| Created (Meta) | The timestamp when the provisioning request was created. |
| Last modified (Meta) | The timestamp of the last modification to the provisioning request. |
| Resource type (Meta) | The type of resource. |
| Correlation ID (Meta) | A unique identifier value attached to requests and messages for tracking purposes. |
| Status | The overall completion and success status of the provisioning request. |
| Completed (Status) | Indicates whether the provisioning request has completed processing. |
| Success (Status) | Indicates whether the user provisioning was successful. |
| Operations count | Counts across provisioning operations within the request. |
| Total (Operations count) | The total number of operations requests within the provisioning request. |
| Success (Operations count) | The number of operations that were successful. |
| Failed (Operations count) | The number of operations that failed. |
| Pending (Operations count) | The number of operations that are still processing. |
| Operations | List of individual provisioning operations within the request. |
| ID (Operations) | The unique identifier of the operation. |
| Status (Operations) | The status of the operation. |
| Resource (Operations) | The resource associated with the operation. |
| Extensions (Operations) | Additional extension data for the operation. |
| Total results | The total number of results available. |
| Start index | The 1-based index of the first result in the current set of list results. |
| Items per page | The number of operations returned per page. |

---

---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/retrieve-children-of-list-item.md
description: >-
  The Retrieve children of list item action retrieves child items of a specific
  list item in SAP Concur.
---

# SAP Concur - Retrieve children of list item action

The **Retrieve children of list item** action retrieves child items of a specific list item in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| List / List ID | Select the list to retrieve child items from, or enter the unique identifier of the list. |
| Item / Item ID | Select the parent list item, or enter the unique identifier of the parent list item. Only the first 100 items are displayed in the selection list. |
| Has children? | Select whether to display only items with children. By default, returns items with their children attributes if present. |
| Is deleted? | Select whether to display deleted items. By default, deleted items are not returned. |
| Short code or value | Enter a value to filter list items by their value or short code. |
| Page number | Specify the page number to retrieve. Defaults to 1. |
| Sort by | Select the field to sort results by. Options include: Value, Short code |

## Output

| Output field | Description |
| --- | --- |
| Links | Hypermedia links related to the list items. |
| Rel (Links) | The relationship of the link to the current resource. |
| Href (Links) | The URL of the linked resource. |
| Content | List of child list items retrieved from the specified parent list item. |
| ID (Content) | The unique identifier of the list item. |
| Code (Content) | The long code value of the list item. |
| Short code (Content) | The short code value of the list item. |
| Value (Content) | The name or text value of the list item. |
| Parent ID (Content) | The unique identifier of the parent list item. |
| Level (Content) | The level of the list item within the hierarchy. |
| Is deleted (Content) | Indicates whether the list item has been deleted from all lists. |
| List ID (Content) | The unique identifier of the list containing this item. |
| Lists (Content) | Information about the lists containing this item. |
| ID (Lists) | The unique identifier of the list that contains the list item. |
| Has children (Lists) | Indicates whether the list item has children in this particular list. |
| Page | Pagination information for the results. |
| Size (Page) | The number of list items returned per page. |
| Total elements (Page) | The total number of list items available across all pages. |
| Total pages (Page) | The total number of pages available. |
| Number (Page) | The current page number. |

---

---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/search-expense-reports-batch.md
description: >-
  The Search expense reports batch action searches for expense reports in SAP
  Concur based on specified criteria.
---

# SAP Concur - Search expense reports action (batch)

The **Search expense reports** batch action searches for expense reports in SAP Concur based on specified criteria. This action retrieves 100 records maximum. When no search criteria is provided, reports owned by the current user are returned.

## Input

| Input field | Description |
| --- | --- |
| User | Specify the user to filter reports by report owner. If set to `ALL`, reports for all report owners are returned. Note: Works only if you are the admin. |
| Approval status | Select the approval status to filter reports. Options include: Not submitted, Submitted, Submission triggered an anomaly and fraud check, Pending reviews, Pending external validation, Pending Budget approval, Pending Cost object approval, Pending manager approval, Pending prepayment validation, Pending receipt images, Needs to be resubmitted, Approved, Expired in approval queue |
| Payment status | Select the payment status to filter reports. Options include: On hold, Not paid, Confirmed, In process to be paid, Paid |
| Currency code | Enter the three-letter ISO 4217 currency code for the report currency (for example, USD). |
| Payment type | Select the payment method for the report entries. Options include: Company Paid, Out-of-Pocket, Pending Card Transaction |
| Reimbursement method | Select how the report owner is reimbursed. Options include: ADP payroll, AP (Company Check), Expense pay, Other Payment Service |
| Approver login ID | Enter the login ID for the report approver that is the current approver assigned to the report. |
| Expense type | Select the expense type code to filter reports that contain at least one expense entry of the specified type. Options include: Airfare, Car Rental, Hotel, Hotel Tax, Train, Fuel |
| Attendee type | Select the attendee type to filter reports that contain expense entries with attendees of the specified type. Options include: Business Guest, Detailed Attendee Information, Employee (Not using Concur), Spouse, Associate |
| Country code | Enter the ISO 3166-1 alpha-2 country code (for example, US for United States). |
| Has VAT | Select whether to filter reports that have at least one expense entry with VAT details. |
| Has images | Select whether to filter reports with at least one expense entry with an entry image or a report image. |
| Has attendees | Select whether to filter reports with at least one expense entry with an attendee. |
| Has billable expenses | Select whether to filter reports with at least one billable expense entry. |
| Is test user | Select whether to filter reports whose owner is a test user using the report for testing purposes in a non-production environment. |
| Expense group configuration | Select the expense group configuration to filter reports. Options include: Global, US Group, AU Group, CA Group, DE Group, FR Group, GB Group, IE Group, SG Group |
| Entry transaction date before | Enter the date to filter reports with expense entry transactions before this date. |
| Entry transaction date after | Enter the date to filter reports with expense entry transactions after this date. |
| Created date before | Enter the date to filter reports created before this date. |
| Created date after | Enter the date to filter reports created after this date. |
| User defined date before | Enter the date to filter reports with user-defined dates before this date. |
| User defined date after | Enter the date to filter reports with user-defined dates after this date. |
| Submit date before | Enter the date to filter reports submitted before this date. |
| Submit date after | Enter the date to filter reports submitted after this date. |
| Processing payment date before | Enter the date to filter reports that completed approvals and were ready for payment extraction before this date. |
| Processing payment date after | Enter the date to filter reports that completed approvals and were ready for payment extraction after this date. |
| Paid date before | Enter the date to filter reports where all journal entries were integrated with the financial system before this date. |
| Paid date after | Enter the date to filter reports where all journal entries were integrated with the financial system after this date. |
| Modified date before | Enter the date to filter reports last modified before this date. |
| Modified date after | Enter the date to filter reports last modified after this date. |

## Output

| Output field | Description |
| --- | --- |
| Expense reports | List of expense reports matching the search criteria. |
| Report name (Expense reports) | The name of the expense report. |
| Report ID (Expense reports) | The unique identifier of the resource. |
| Report URI (Expense reports) | The URI to the resource. |
| Total (Expense reports) | The total amount of the report. |
| Currency code (Expense reports) | The three-letter ISO 4217 currency code for the expense report currency. |
| Country (Expense reports) | The report country. Format: ISO 3166-1 alpha-2. |
| Country subdivision (Expense reports) | The report country subdivision. Format: ISO 3166-2:2007 country subdivision. |
| Personal amount (Expense reports) | The total amount of expenses marked as personal. |
| Amount due employee (Expense reports) | The total amount due to the employee for the report. |
| Amount due company card (Expense reports) | The total amount due to the company card for the report. |
| Total claimed amount (Expense reports) | The total amount of all non-personal expenses in the report. |
| Total approved amount (Expense reports) | The total amount of approved expenses in the report. |
| Receipts received (Expense reports) | Indicates whether the receipts have been received. If true, this entry has been marked as confirmed by the Expense Processor. |
| Ever sent back (Expense reports) | Indicates whether the report has ever been sent back to the employee. |
| Has exception (Expense reports) | Indicates whether the report has exceptions. |
| Last comment (Expense reports) | The text of the most recent comment on the report. |
| Owner login ID (Expense reports) | The Login ID of the user this report belongs to. |
| Owner name (Expense reports) | The name of the expense report owner. |
| Approver login ID (Expense reports) | The Login ID of the report owner's expense approver. |
| Approval status name (Expense reports) | The report's approval status, in the OAuth consumer's language. |
| Approval status code (Expense reports) | The approval status code for the report. |
| Payment status name (Expense reports) | The report's payment status, in the OAuth consumer's language. |
| Payment status code (Expense reports) | The payment status code for the report. |
| Ledger name (Expense reports) | The name of the expense report ledger. |
| Policy ID (Expense reports) | The unique identifier of the policy that applies to this report. |
| Workflow action URL (Expense reports) | The URL to post a workflow action to the report. |
| Create date (Expense reports) | The date the report was created. |
| Submit date (Expense reports) | The date the report was submitted. |
| Processing payment date (Expense reports) | The date that the report completed approvals and was ready for payment extraction. |
| Paid date (Expense reports) | The date when all journal entries were integrated with the financial system. |
| User defined date (Expense reports) | The report date assigned by the user. |
| Last modified date (Expense reports) | The date the report was last modified. |

---
