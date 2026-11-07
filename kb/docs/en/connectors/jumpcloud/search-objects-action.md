---
url: 'https://docs.workato.com/en/connectors/jumpcloud/search-objects-action.md'
description: >-
  The Search objects batch action in the JumpCloud connector searches for
  objects in batches and returns up to 100 results matching your criteria.
---

# JumpCloud - Search objects action (batch)

The **Search objects** batch action searches for JumpCloud objects in batches and returns a list of results matching the criteria you specify.

## Input

| Field | Description |
| --- | --- |
| Object | Select the type of object you plan to search for. |
| Search type | Specify whether to retrieve objects that **Contain** or **Equal** the search criteria. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on the **Object** type you select. Use these fields to specify the search criteria. Refer to JumpCloud's [API 1.0 documentation](https://docs.jumpcloud.com/api/1.0/index.html) for more information about the input fields for each type.

## Output

The **Search objects** action's output fields vary based on your selected **Object** type. Refer to JumpCloud's [API 1.0 documentation](https://docs.jumpcloud.com/api/1.0/index.html) for more information about the output fields for each type.

> **MAXIMUM OUTPUT LENGTH**
> 
> The **Search objects** action returns a maximum of 100 records from JumpCloud.

---

---
url: >-
  https://docs.workato.com/en/connectors/jumpcloud/search-user-by-employee-id-action.md
description: >-
  The Search user by employee ID action in the JumpCloud connector retrieves
  data about a user based on the employee ID you provide.
---

# JumpCloud - Search user by employee ID action

The **Search user by employee ID** action retrieves data about a JumpCloud user based on the employee ID you provide.

## Input

| Field | Description |
| --- | --- |
| Employee ID | Provide the employee ID of the user whose data you plan to retrieve. |

## Output

| Field | Description |
| --- | --- |
| Email | The user's email. |
| User name | The user's user name. |
| Allow public key | Indicates whether the user can authenticate with a public key. |
| Public key | The user’s public key, used for authentication. |
| Sudo | Indicates whether the user has sudo privileges in Unix-like systems. |
| Enable managed uid | Indicates whether JumpCloud manages the user's UID. |
| Unix uid | The user's unique user identifier (UID) in Unix-like systems. |
| Unix guid | The user's group identifier (GUID) in Unix-like systems. |
| Activated | Indicates whether the user is active. |
| Tags | The user's tags. |
| Account locked | Indicates whether the user’s account is locked. |
| Passwordless sudo | Indicates whether the user can run sudo commands without a password prompt. |
| Externally managed | Indicates whether an external system manages the user. |
| External dn | The user's external distinguished name (DN). |
| External source type | The type of external source managing the user. |
| First name | The user's first name. |
| Last name | The user's last name. |
| Ldap binding user | Indicates whether the user is bound to an LDAP directory. |
| Enable user portal multi-factor | Indicates whether the user can use multi-factor authentication (MFA) to access the JumpCloud user portal. |
| Attributes | Contains information about the user's custom attributes, such as their `Value` and `Name`. |
| Samba service user | Indicates whether the user is connected to Samba. |
| Addresses | Contains information about user's addresses, such as their `Street address` and `Type`. |
| Job title | The user's job title. |
| Department | The user's department. |
| Phone numbers | Contains information about the user’s phone numbers, such as their `Type` and `Number`. |
| Password never expires | Indicates whether the user’s password never expires. |
| Middle name | The user's middle name. |
| Display name | The user's display name, usually a combination of `First name` and `Last name`. |
| Description | The user's description. |
| Location | The user's physical or office location. |
| Cost center | The user's associated cost center. |
| Employee type | The user's employee type, such as `full-time`, `part-time`, or `contractor`. |
| Company | The company the user works for. |
| Employee identifier | A unique identifier for the user, often used for HR or payroll purposes. |
| MFA | Contains information about the user's multi-factor authentication, such as its `Exclusion until` date and `Configured` status. |
| Suspended | Indicates whether the user is suspended, blocking their access the system. |
| Alternate email | The user's alternate email. |
| Disable device max login attempts | Indicates whether the user is allowed unlimited login attempts. |
| External password expiration date | The expiration date of the user’s external management password. |
| Managed apple ID | The Apple ID of the user's device. |
| Manager | The name or JumpCloud ID of the user's manager or supervisor. |
| State | The user's identity lifecycle state. |
| Relationships | Contains information about the user's relationships, such as their `Type` and `Value`. |
| Restricted fields | Contains information about restricted user fields, such as their `Field` name and `ID`. |
| Ssh keys | Contains information about the user's SSH keys, such as their `Name` and `ID`. |
| Password expired | Indicates whether the user’s password is expired. |
| Totp enabled | Indicates whether time-based one-time password (TOTP) is enabled as part of the user's MFA. |
| Created | A timestamp indicating when the user's account was created. |
| ID | The user's unique JumpCloud’s identifier. |
| Organization | The organization that contains the user. |
| Bad login attempts | The user's number of failed login attempts. |
| Password expiration date | The expiration date of the user’s password. |
| Admin | Contains information about the admin associated with the user, such as their `ID`. |
| Creation source | The source from which the user was created. |
| Password date | The date the user's password was last updated. |
| Recovery email | Contains information about the user's recovery email, such as its `Address` and `Verified` status. |
| Mfa enrollment | Contains information about the user's MFA, such as its `Overall status` and `Totp status`. |

---
