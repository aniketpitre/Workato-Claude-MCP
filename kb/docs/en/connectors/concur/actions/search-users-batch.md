---
url: 'https://docs.workato.com/en/connectors/concur/actions/search-users-batch.md'
description: >-
  The Search users batch action searches for users in SAP Concur based on
  specified criteria.
---

# SAP Concur - Search users action (batch)

The **Search users** batch action searches for users in SAP Concur based on specified criteria.

## Input

| Input field | Description |
| --- | --- |
| Filter | Enter the filter string to request a subset of users. Supported attributes are `userName`, `employeeNumber`, and `externalId`. Format: `attribute eq "value"`. |
| Attributes | Enter a comma-delimited list of resource attribute names to return in the response. |
| Username | Enter the requested user's username. |
| Company ID | Enter the ID of the company the user belongs to. Required if `employeeNumber` is used. |
| Employee number | Enter the user's employee number. Required if `companyId` is used. The `employeeNumber` must be unique within the `companyId`. |
| External ID | Enter the user's external ID. The `externalId` must be unique within the `companyId`. |
| Excluded attributes | Enter a comma-delimited list of resource attribute names to be removed from the default set of attributes to return. |
| Start index | Specify the 1-based index of the first query result. Defaults to 1. |
| Count | Specify the desired maximum number of query results per page. Maximum count is 100. Defaults to 10. |

## Output

| Output field | Description |
| --- | --- |
| Schemas | The SCIM schema URIs for the response. |
| Total results | The total number of results matching the search criteria. |
| Start index | The 1-based index of the first result in the current page. |
| Items per page | The number of users returned in the current page. |
| Resources | List of user resources matching the search criteria. |
| Active (Resources) | Indicates whether the user account is active. |
| Addresses (Resources) | List of addresses associated with the user. |
| Country (Addresses) | The ISO 3166-1 alpha-2 country code. |
| Locality (Addresses) | The city designation. |
| Postal code (Addresses) | The zip or postal code. |
| Region (Addresses) | The state or province code. |
| Street address (Addresses) | The full street location. |
| Type (Addresses) | The function label for the address. |
| Date of birth (Resources) | The user's date of birth in YYYY-MM-DD format. |
| Display name (Resources) | The public-facing name combining given and family names. |
| Emails (Resources) | List of email addresses associated with the user. |
| Notifications (Emails) | The email notification opt-in status. |
| Type (Emails) | The category of email. |
| Value (Emails) | The email address. |
| Verified (Emails) | Indicates whether the email has been verified. |
| Date added (Emails) | The date when the email was added. |
| Date verified (Emails) | The date when the email was verified. |
| Emergency contacts (Resources) | List of emergency contact information for the user. |
| Country (Emergency contacts) | The country of the emergency contact. |
| Emails (Emergency contacts) | The contact email addresses. |
| Locality (Emergency contacts) | The city of the emergency contact. |
| Name (Emergency contacts) | The contact's full name. |
| Phones (Emergency contacts) | The contact phone numbers. |
| Postal code (Emergency contacts) | The postal code of the emergency contact. |
| Region (Emergency contacts) | The state or province of the emergency contact. |
| Relationship (Emergency contacts) | The connection type. |
| Street address (Emergency contacts) | The physical location of the emergency contact. |
| Entitlements (Resources) | The entitlements assigned to the user. |
| External ID (Resources) | An identifier from the provisioning client. |
| ID (Resources) | The unique identifier (UUID) for the user. |
| Locale overrides (Resources) | Custom locale settings that override default preferences. |
| Preference end day view hour (Locale overrides) | The ending hour for day view. |
| Preference first day of week (Locale overrides) | The first day of the week preference. |
| Preference date format (Locale overrides) | The date display pattern preference. |
| Preference currency symbol location (Locale overrides) | The currency symbol position preference. |
| Preference hour minute separator (Locale overrides) | The separator used between hours and minutes. |
| Preference distance (Locale overrides) | The preferred unit of distance measurement. |
| Preference default cal view (Locale overrides) | The default calendar view preference. |
| Preference 24 hour (Locale overrides) | The time display format preference. |
| Preference number format (Locale overrides) | The numeric display standard preference. |
| Preference start day view hour (Locale overrides) | The starting hour for day view. |
| Preference negative currency format (Locale overrides) | The format for displaying negative currency values. |
| Preference negative number format (Locale overrides) | The format for displaying negative numbers. |
| Meta (Resources) | Metadata about the user resource. |
| Resource type (Meta) | The type of resource. |
| Created (Meta) | The timestamp when the user was created. |
| Last modified (Meta) | The timestamp of the last modification to the user. |
| Version (Meta) | The version number of the user record. |
| Location (Meta) | The URL for retrieving the user's details. |
| Name (Resources) | The full name of the user. |
| Academic title (Name) | The academic title of the user. |
| Family name (Name) | The last name of the user. |
| Given name (Name) | The first name of the user. |
| Honorific prefix (Name) | A title or prefix. |
| Honorific suffix (Name) | A suffix designation. |
| Legal name (Name) | The official legal name designation. |
| Middle initial (Name) | The middle initial abbreviation. |
| Middle name (Name) | The middle name of the user, if applicable. |
| Family name prefix (Name) | A prefix to the family name. |
| Formatted (Name) | The complete name formatted for display purposes. |
| Nick name (Name) | The user's nickname or preferred casual name. |
| Schemas (Resources) | The SCIM schema URIs for the user resource. |
| Phone numbers (Resources) | List of phone numbers associated with the user. |
| Display (Phone numbers) | The human-readable format of the phone number. |
| Notifications (Phone numbers) | The alert subscription status for this phone number. |
| Operating system (Phone numbers) | The operating system for the phone device. |
| Primary (Phone numbers) | Indicates whether this is the primary mobile number. |
| Type (Phone numbers) | The category of the phone number. |
| Value (Phone numbers) | The phone number. |
| Preferred language (Resources) | The user's preferred language code. |
| Timezone (Resources) | The user's timezone in Olson format. |
| Title (Resources) | The user's job title. |
| User name (Resources) | The login name in user@domain format. |

---
