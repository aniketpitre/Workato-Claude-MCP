---
url: 'https://docs.workato.com/en/connectors/concur/actions/update-user.md'
description: The Update user action updates an existing user in SAP Concur.
---

# SAP Concur - Update user action

The **Update user** action updates an existing user in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| Replace user? | Select **Yes** to replace the complete details of the user. Select **No** to update the data attributes listed within the request. Default is false. |
| User ID | Enter the unique identifier of the SAP Concur user to update. |

> **ADDITIONAL INPUT FIELDS**
> 
> This action supports additional input fields for user attributes including emails, phone numbers, addresses, travel preferences, and spend settings. Refer to the [SAP Concur User Provisioning v4 API documentation](https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html) for the complete list of available fields.

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
| With nick name (Display name format) | The display name format that includes the user's nickname. |
| Without nick name (Display name format) | The display name format that excludes the user's nickname. |
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
| Provision ID (Meta) | A unique number used for querying the provisioning status. |
| Status URL (Meta) | The URL for checking the provisioning status. |
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
| Issuing country (Phone numbers) | The issuing country for the user. |
| Work extension (Phone numbers) | The work phone extension. |
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

---
