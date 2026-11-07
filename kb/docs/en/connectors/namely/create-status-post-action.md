---
url: 'https://docs.workato.com/en/connectors/namely/create-status-post-action.md'
description: >-
  The Create status post action in the Namely connector lets you publish a new
  status post with a message and optional file attachment.
---

# Namely - Create status post action

The **Create status post** action creates a new status post in Namely.

![Create status post action](/assets/create-status-post-action.BlDTK0XA.png)_Create status post action_

## Input

| Input field | Description |
| --- | --- |
| Post message | Enter the message you plan to post. |
| File URL | Enter the URL of the file you plan to include in the post, or enter the file ID. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier for the message. |
| Content | The text content of the message. |
| HTML content | The HTML version of the message content. |
| Created at | The timestamp when the message was created. |
| Can destroy | Indicates whether the message can be deleted or not. Values are `true` or `false`. |
| Can edit | Indicates whether the message can be edited or not. Values are `true` or `false`. |
| UTC offset | The UTC offset for the message's timestamp. |
| Likes count | The number of likes the message has received. |
| Liked by current profile | Indicates whether the current profile has liked the message or not. Values are `true` or `false`. |
| Updated at | The timestamp when the message was last updated (in Unix epoch format). |
| Profile ID | The unique identifier for the profile associated with the message. |
| Profile company UUID | The universally unique ID (UUID) of the company associated with the profile. For example: `6d82888e-9c39-4fa8-ba84-c2145485a730`. |
| Profile email | The email address associated with the profile. |
| Profile first name | The first name of the person associated with the profile. |
| Profile last name | The last name of the person associated with the profile. |
| Profile user status | The status of the profile. For example: `active`. |
| Profile updated at | The timestamp when the profile's information was last updated. |
| Profile created at | The timestamp when the profile was created. |
| Profile preferred name | The preferred name of the person associated with the profile, if any. |
| Profile preferred last name | The preferred last name of the person associated with the profile, if any. |
| Profile image | Details about the profile's image, if any. |
| Profile full name | The full name of the person associated with the profile. |
| Profile job title ID | The ID of the profile's job title. |
| Profile job title | The job title associated with the profile. |
| Profile employee type | The type of employment. For example: `Full Time` or `Part Time`. |
| Profile access role | The access role associated with the profile within the system, if any. |
| Profile ethnicity | The ethnicity of the employee associated with the profile. |
| Profile team positions | The team positions associated with the profile. |
| Profile is Namely admin | Indicates whether the profile is an admin within Namely or not. Values are `true` or `false`. |
| Profile date format | The date format preferred by the employee associated with the profile. |

---

---
url: >-
  https://docs.workato.com/en/connectors/namely/get-employee-profile-by-id-action.md
description: >-
  The Get employee profile details by ID action in the Namely connector lets you
  fetch the full details of an employee profile by its ID.
---

# Namely - Get employee profile details by ID action

The **Get employee profile details by ID** action allows you to fetch an employee profile by ID.

![Get employee profile by ID action](/assets/get-employee-profile-details-by-id-action.DDvxvwqR.png)_Get employee profile details by ID action_

## Input

| Input field | Description |
| --- | --- |
| Profile ID | Enter the ID of the employee profile you plan to fetch. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the employee. |
| Company UUID | The universally unique ID (UUID) of the company associated with the employee. |
| Email | The employee's email address. |
| First name | The first name of the employee. |
| Last name | The last name of the employee. |
| User status | The current status of the employee. For example: `active`. |
| Updated at | The timestamp when the employee's information was last updated. |
| Created at | The timestamp when the employee's information was created. |
| Preferred name | The preferred name of the employee, if any. |
| Preferred last name | The preferred last name of the employee, if any. |
| Image | Details about the employee's image, including ID, filename, MIME type, original, and thumbnails. |
| Full name | The full name of the employee. |
| Job title | Details about the employee's job title, including ID, title, parent ID, links, active status, and salary bands. |
| Reports to | Information about whom the employee reports to, including ID, first name, last name, preferred name, and email. |
| Employee type | The type of employment of the employee. For example: `Full Time` or `Part Time`. |
| Access role | The access role of the employee within the system, if any. |
| Ethnicity | The ethnicity of the employee, if any. |
| Team positions | The team positions held by the employee, if any. |
| Is Namely admin | Indicates whether the employee is an admin within Namely or not. |
| Date format | The date format preferred by the employee. |
| Start date | The start date of the employee's employment. |
| LinkedIn URL | The LinkedIn URL of the employee, if any. |
| Office direct dial | The direct dial number for the employee's office, if any. |
| Office phone | The general phone number for the employee's office, if any. |
| Veteran protected classes | Information about veteran protected classes for the employee, if any. |
| Middle name | The middle name of the employee. |
| Bio | The biography of the employee, if any. |
| Office main number | The main phone number for the employee's office, if any. |
| Office address1 | The first line of the office address, if any. |
| Office address2 | The second line of the office address, if any. |
| City | The city of the office address, if any. |
| State ID | The ID of the state where the office is located. |
| Country ID | The ID of the country where the office is located. |
| Zip | The ZIP code of the office address. |
| Phone | The phone number of the office, if any. |
| Groups | The groups the employee is part of, if any. |
| Teams | The teams the employee is part of, if any. |

---
