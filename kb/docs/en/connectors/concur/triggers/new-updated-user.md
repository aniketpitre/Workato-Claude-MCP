---
url: 'https://docs.workato.com/en/connectors/concur/triggers/new-updated-user.md'
description: >-
  The New/updated user trigger activates when a user is created or updated in
  SAP Concur.
---

# SAP Concur - New/updated user trigger

The **New/updated user** trigger activates when a user is created or updated in SAP Concur. This trigger is supported for EU and US data centers only.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Specify when the recipe should start picking up users. When you start the recipe for the first time, it picks up users created or updated after the specified date and time. Leave this field empty to get users from one hour ago. You can't change this value after running or testing the recipe. |
| Trigger poll interval | Select how frequently to check for new events. |

## Output

| Output field | Description |
| --- | --- |
| Locale overrides | The locale-specific preferences for the user. Read-only fields. |
| Preference end day view hour (Locale overrides) | The end hour for day view preference. |
| Preference first day of week (Locale overrides) | The first day of the week preference. |
| Preference date format (Locale overrides) | The date format selection. |
| Preference currency symbol location (Locale overrides) | The currency symbol placement preference. |
| Preference hour minute separator (Locale overrides) | The hour-minute separator preference. |
| Preference distance (Locale overrides) | The distance unit preference. |
| Preference default cal view (Locale overrides) | The default calendar view preference. |
| Preference 24 hour (Locale overrides) | The 24-hour time format preference. |
| Display name format (Locale overrides) | The display name format preferences. |
| With nick name (Display name format) | The display name format with nickname. |
| Without nick name (Display name format) | The display name format without nickname. |
| Preference number format (Locale overrides) | The number formatting preference. |
| Preference start day view hour (Locale overrides) | The start hour for day view preference. |
| Preference negative currency format (Locale overrides) | The negative currency format preference. |
| Preference negative number format (Locale overrides) | The negative number format preference. |
| Addresses | The physical mailing addresses with type labels. |
| Street address (Addresses) | The street address. |
| Locality (Addresses) | The city or locality. |
| Region (Addresses) | The state or region. |
| Country (Addresses) | The country. |
| Postal code (Addresses) | The postal or ZIP code. |
| Type (Addresses) | The type of address. |
| Timezone | The user's time zone per Olson database format. |
| Meta | The metadata about the resource. |
| Created (Meta) | The date and time the resource was created. |
| Last modified (Meta) | The date and time the resource was last modified. |
| Resource type (Meta) | The type of the resource. |
| Version (Meta) | The version of the resource. |
| Location (Meta) | The location URI of the resource. |
| Provision ID (Meta) | The provisioning identifier. |
| Status URL (Meta) | The status URL for the provisioning operation. |
| Locale | The locale setting for the user. |
| Display name | The public-facing name combining given and family names. |
| Entitlements | The features enabled for the user. |
| Name | The name object containing the user's name components. |
| Middle initial (Name) | The middle initial. |
| Middle name (Name) | The middle name if applicable. |
| Formatted (Name) | The full name combining given, middle, and family components. |
| Honorific prefix (Name) | The title prefix(es) of the user. |
| Legal name (Name) | The legal name of the user. |
| Family name (Name) | The last or family name. Required field. |
| Given name (Name) | The first or given name. Required field. |
| Honorific suffix (Name) | The title suffix(es) of the user. |
| Academic title (Name) | The academic title of the user. |
| Family name prefix (Name) | The family name prefix. |
| Phone numbers | The phone numbers for the user. |
| Value (Phone numbers) | The phone number value. Required when provisioning. |
| Display (Phone numbers) | The display format for the phone number. |
| Type (Phone numbers) | The function label. |
| Primary (Phone numbers) | Indicates the primary mobile device designation. |
| Notifications (Phone numbers) | The notification opt-in status for the phone number. |
| Issuing country (Phone numbers) | The country that issued the phone number. |
| Work extension (Phone numbers) | The work phone extension. |
| Emergency contacts | The emergency contact information with name and relationship. |
| Locality (Emergency contacts) | The city or locality of the emergency contact. |
| Name (Emergency contacts) | The name of the emergency contact. |
| Relationship (Emergency contacts) | The relationship to the emergency contact. |
| Street address (Emergency contacts) | The street address of the emergency contact. |
| Region (Emergency contacts) | The state or region of the emergency contact. |
| Phones (Emergency contacts) | The phone numbers of the emergency contact. |
| Postal code (Emergency contacts) | The postal or ZIP code of the emergency contact. |
| Emails (Emergency contacts) | The email addresses of the emergency contact. |
| Country (Emergency contacts) | The country of the emergency contact. |
| Preferred language | The written or spoken language preference. |
| Title | The job title within the company. |
| Date of birth | The user's birth date in YYYY-MM-DD format. |
| Nick name | The casual address name. Displays as preferred name in the UI. |
| External ID | The client-supplied user identifier from the provisioning system. |
| Active | Indicates whether the user account is enabled. |
| ID | The unique identifier for the user. |
| Emails | The email addresses for the user. |
| Value (Emails) | The email address value. Required when provisioning. |
| Verified (Emails) | Indicates whether the email has been verified. |
| Type (Emails) | The label indicating the email attribute's function. |
| Notifications (Emails) | The notification opt-in status for the email. |
| User name | The login identifier for the user. |
| Enterprise user | The enterprise-specific user information. |
| Employee number (Enterprise user) | The client-supplied employee ID unique per company. |
| Department (Enterprise user) | The client-supplied department name. |
| Division (Enterprise user) | The client-supplied division name. |
| Start date (Enterprise user) | The employment start date. |
| Organization (Enterprise user) | The company name. |
| Cost center (Enterprise user) | The employee cost center for product usage. |
| Leaves of absence (Enterprise user) | The leaves of absence information for the user. |
| Start date (Leaves of absence) | The start date of the leave of absence. |
| End date (Leaves of absence) | The end date of the leave of absence. |
| Type (Leaves of absence) | The type of leave of absence. |
| Manager (Enterprise user) | The manager information for the user. |
| Value (Manager) | The manager's UUID identifier. |
| $ref (Manager) | The reference to the manager's resource. |
| Display name (Manager) | The display name of the manager. |
| Employee number (Manager) | The employee number of the manager. |
| Termination date (Enterprise user) | The employment end date. |
| Legal entity (Enterprise user) | The legal entity associated with the user. |

---
