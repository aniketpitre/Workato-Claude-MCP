---
url: 'https://docs.workato.com/en/connectors/namely/search-people-profiles-action.md'
description: >-
  The Search people profiles batch action in the Namely connector lets you
  search employee profiles by email, name, job title, or reporting manager.
---

# Namely - Search people profiles batch action

The Search people profiles batch action allows you to search for employee profiles in batch.

![Search people profiles batch action](/assets/search-people-profiles-action.FvaPKMdI.png)_Search people profiles batch action_

## Input

| Input field | Description |
| --- | --- |
| Profile email | Enter the email address associated with the profile you plan to search. This field is optional. Specifying this field results in a search based solely on Profile email, ignoring other fields, and returns a maximum of 50 results. |
| First name | Enter the first name of the person whose profile you plan to search for. This field is optional. |
| Last name | Enter the last name of the person whose profile you plan to search for. This field is optional. |
| Personal email | Enter the personal email address associated with the profile you plan to search. This field is optional. |
| Job title | Enter the job title associated with the profile you plan to search. This field is optional. |
| Reports to | Enter the manager or supervisor of the person whose profile you plan to search for. This field is optional. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier for the profile. |
| Company UUID | The universally unique ID (UUID) of the company associated with the profile. |
| Email | The email address associated with the profile. |
| First name | The first name associated with the profile. |
| Last name | The last name associated with the profile. |
| User status | The status of the profile. For example: `active`. |
| Updated at | The timestamp when the profile's information was last updated. |
| Created at | The timestamp when the profile was created. |
| Preferred name | The preferred name of the employee. |
| Preferred last name | The preferred last name of the employee. |
| Image | The profile image details. |
| Full name | The full name of the employee. |
| Job title ID | The unique identifier for the job title associated with the profile. |
| Job title | The title of the job associated with the employee profile. |
| Parent ID | The parent ID of the job title, indicating hierarchical relationship. |
| Links | The hyperlinks associated with the job title, if any. |
| Active | Indicates whether the job title is active. |
| Salary bands | The salary bands associated with the job title, if any. |
| Reports to | Information about the reporting structure, if any. |
| Employee type | The type of employment associated with the profile. For example: `Full Time`. |
| Access role | The access role of the employee within the system, if any. |
| Ethnicity | The ethnicity of the employee, if any. |
| Team positions | The team positions held by the employee, if any. |
| Is Namely admin | Indicates whether the employee is an admin within Namely. |
| Date format | The date format preferred by the employee. |
| Start date | The start date of the employee. |
| Linkedin URL | The LinkedIn URL of the employee, if any. |
| Office direct dial | The direct dial number for the employee's office. |
| Office phone | The general phone number for the employee's office. |
| Veteran protected classes | Information about veteran protected classes for the employee. |
| Middle name | The middle name of the employee. |
| Bio | The biography of the employee. |
| Office main number | The main phone number for the employee's office. |
| Office | Details about the employee's office address, including address lines, city, state ID, country ID, ZIP code, and phone number. |
| Groups | The groups the employee is part of. |
| Teams | The teams the employee is part of. |

---
