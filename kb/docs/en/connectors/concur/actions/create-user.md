---
url: 'https://docs.workato.com/en/connectors/concur/actions/create-user.md'
description: >-
  The Create user action creates a single user profile with identity, spend, and
  travel attributes.
---

# SAP Concur - Create user action

The **Create user** action creates a single user profile with identity, spend, and travel attributes.

## Input

| Input field | Description |
| --- | --- |
| Name | Expand this section to configure the user's name. |
| Family name (Name) | Enter the family name or last name of the user. |
| Given name (Name) | Enter the given name or first name of the user. |
| Active | Select whether the user is active. |
| User name | Enter the username for the user. Username should end with `@` followed by the company domain. |
| Enterprise user | Expand this section to configure attributes representing users that belong to or act on behalf of a business enterprise. |
| Company ID (Enterprise user) | Enter the Concur ID of the company. |
| Start date (Enterprise user) | Enter the start date for the user's employment or relationship with the enterprise. |

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
| Preference number format (Locale overrides) | The numeric display standard preference. |
| Preference start day view hour (Locale overrides) | The starting hour for day view. |
| Preference negative currency format (Locale overrides) | The format for displaying negative currency values. |
| Preference negative number format (Locale overrides) | The format for displaying negative numbers. |
| Addresses | The addresses associated with the user. |
| Street address (Addresses) | The full street location. |
| Locality (Addresses) | The city designation. |
| Region (Addresses) | The state or province code. |
| Country (Addresses) | The ISO 3166-1 alpha-2 country code. |
| Postal code (Addresses) | The zip or postal code. |
| Type (Addresses) | The function label for the address. |
| Timezone | The user's timezone in Olson format. |
| Meta | Metadata about the user, including creation and last modified dates. |
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
| Phone numbers | The phone numbers associated with the user. |
| Value (Phone numbers) | The phone number. |
| Display (Phone numbers) | The human-readable format of the phone number. |
| Type (Phone numbers) | The category of the phone number (mobile, work, home, fax). |
| Primary (Phone numbers) | Indicates whether this is the primary mobile number. |
| Notifications (Phone numbers) | The alert subscription status for this phone number. |
| Issuing country | The issuing country for the user. |
| Work extension | The work phone extension. |
| Emergency contacts | Emergency contact information for the user. |
| Locality (Emergency contacts) | The city of the emergency contact. |
| Name (Emergency contacts) | The contact's full name. |
| Relationship (Emergency contacts) | The relationship type, such as Spouse or Parent. |
| Street address (Emergency contacts) | The physical location of the emergency contact. |
| Region (Emergency contacts) | The state or province of the emergency contact. |
| Phones (Emergency contacts) | The contact phone numbers. |
| Postal code (Emergency contacts) | The postal code of the emergency contact. |
| Emails (Emergency contacts) | The contact email addresses. |
| Country (Emergency contacts) | The country of the emergency contact. |
| Preferred language | The user's preferred language code. |
| Title | The user's job title. |
| Date of birth | The user's date of birth. |
| Nick name | The user's nickname. |
| External ID | An external identifier for the user. |
| Active | Indicates whether the user account is active. |
| ID | The unique identifier of the user (UUID). |
| Emails | The email addresses associated with the user. |
| Value (Emails) | The email address. |
| Verified (Emails) | Indicates whether the email address has been verified. |
| Type (Emails) | The classification of the email. |
| Notifications (Emails) | The opt-in status for email notifications. |
| User name | The username of the user, used as the login credential. |
| Enterprise user | Attributes representing users that belong to or act on behalf of a business enterprise. |
| Employee number (Enterprise user) | The unique identifier within the organization. |
| Department (Enterprise user) | The organizational unit assignment. |
| Division (Enterprise user) | The business segment classification. |
| Start date (Enterprise user) | The start date for the user's employment or relationship with the enterprise. |
| Organization (Enterprise user) | The organization the user belongs to. |
| Cost center (Enterprise user) | The financial allocation center. |
| Leaves of absence (Enterprise user) | Information about the user's leaves of absence. |
| Start date (Leaves of absence) | The start date of the leave of absence. |
| End date (Leaves of absence) | The end date of the leave of absence. |
| Type (Leaves of absence) | The type of leave of absence. |
| Manager (Enterprise user) | Information about the user's line manager, including reference and details. |
| Value (Manager) | The manager's unique identifier. |
| $ref (Manager) | A reference to the manager's user record. |
| Display name (Manager) | The display name of the manager. |
| Employee number (Manager) | The employee number of the manager. |
| Termination date (Enterprise user) | The termination date of the user's employment, if applicable. |
| Legal entity (Enterprise user) | The legal entity associated with the user. |

---
