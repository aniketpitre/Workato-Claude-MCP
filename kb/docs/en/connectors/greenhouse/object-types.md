---
url: 'https://docs.workato.com/en/connectors/greenhouse/object-types.md'
description: >-
  Reference for Greenhouse object types exposed as Workato datapills, including
  the candidate, user, application, job, and offer objects and their fields.
---

# Greenhouse - Object types

Greenhouse has several object types that represent different stakeholders in their ecosystem. Each object type holds different attributes. Workato exposes these attributes as datapills.

The comment object types are:

- [Candidate object](#candidate-object)
- [User object](#user-object)
- [Application object](#application-object)
- [Job object](#job-object)
- [Offer object](#offer-object)

## Candidate object

| Datapill | Description |
| --- | --- |
| Candidate ID | A unique candidate ID. |
| First name | The first name. |
| Last name | The last name. |
| Company | The current company of the candidate. |
| Title | The current title of the candidate. |
| Created at | When this candidate's profile was created. |
| Updated at | When this candidate's profile was last updated. |
| Last activity | The last activity of this candidate. |
| Photo URL | The candidate's photo URL. Returns `null` if this candidate does not have a photo attachment. |
| Attachments | A list of attachments, including the **List size** and **List index**. Each attachment contains a **filename**, **URL**, and **Type**. |
| Application IDs | A list of application IDs for associated [Greenhouse applications](#application-object), including the **List size** and **List index**. |
| Is private | Whether the candidate is private. |
| Phone numbers | A list of phone numbers, including the **List size** and **List index**. |
| Addresses | A list of addresses, including the **List size** and **List index**. |
| Email addresses | A list of email addresses, including the **List size** and **List index**. |
| Website addresses | A list of website addresses, including the **List size** and **List index**. |
| Social media addresses | A list of social media addressed, including the **List size** and **List index**. |
| Recruiter | A [Greenhouse user](#user-object) who is responsible for this candidate. |
| Coordinator | A [Greenhouse user](#user-object) who is responsible for this candidate. |
| Can email | Whether this candidate can be emailed. |
| Tags | A list of tags, including the **List size** and **List index**. |
| Applications | A list of [Greenhouse applications](#application-object), including the **List size** and **List index**. |
| Educations | A list of education records, including the **List size** and **List index**. Each education record contains a **Education ID**, **School name**, **Degree**, **Discipline**, **Start date** and **End date**. |
| Employments | A list of previous employments, including the **List size** and **List index**. Each employment record contains a **Employment ID**, **Company name**, **Job title**,**Start date** and **End date**. |
| Custom fields and keyed custom fields | Custom fields and keyed custom fields are exposed as discrete datapills. |

Find out more about [Greenhouse candidate object](https://developers.greenhouse.io/harvest.html#the-candidate-object).

## User object

| Datapill | Description |
| --- | --- |
| User ID | A unique user ID. |
| First name | The first name. |
| Last name | The last name. |
| Primary email address | The email address designated as the primary email address. |
| Updated at | When this user's profile was last updated. |
| Created at | When this user's profile was created. |
| Disabled | Whether this user has been disabled. |
| Site admin | Whether this user is a site admin. |
| Emails | A list of email addresses, including the **List size** and **List index**. This list includes the **Primary email address**. |
| Employee ID | A unique employee ID. |
| Linked candidate IDs | A list of previous candidate records, including the **List size** and **List index**. |

Find out more about [Greenhouse user object](https://developers.greenhouse.io/harvest.html#the-user-object).

## Application object

| Datapill | Description |
| --- | --- |
| Application ID | A unique application ID. |
| Candidate ID | A unique candidate ID. |
| Prospect | Whether this is a prospect application. |
| Applied at | When this application was applied for. |
| Rejected at | When this application was rejected. |
| Last activity at | The last activity of this application. |
| Location | The contents of the location question on a job post. |
| Source | A source object that contains a **Source ID** and **Public name**. |
| Credited to | A [Greenhouse user](#user-object) who will receive credit for this application. |
| Rejection reason | A datapill that contains a **rejection reason ID**, **Rejection reason name**, and **Type**. |
| Rejection details | Custom fields and keyed custom fields for rejection details. |
| Jobs | A list of [Greenhouse job IDs](#job-object), including the **List size** and **List index**. |
| Status | The status of this application. Only `active` applications can be [advanced](/en/connectors/greenhouse/advance-application-action) or [marked as hired](/en/connectors/greenhouse/mark-candidate-as-hired-action). |
| Current stage | The **Stage ID** and **Stage name**. |
| Answers | A list of job application questions and answers, including the **List size** and **List index**. |
| Prospective office | The office that this application is being considered for. |
| Prospective department | The department that this application is being considered for. |
| Prospect detail | Information about the **Prospect pool**, **Prospect stage**, and **Prospect owner**. |
| Custom fields and keyed custom fields | Custom fields and keyed custom fields are exposed as discrete datapills. |

Find out more about [Greenhouse application object](https://developers.greenhouse.io/harvest.html#the-application-object).

## Job object

| Datapill | Description |
| --- | --- |
| Job ID | A unique job ID. |
| Job name | The job name. |
| Requisition ID | An external ID. |
| Notes | Notes attached to this job. |
| Confidential | Whether this job is confidential. |
| Job status | The status of the job. |
| Created at | When this job was created. |
| Opened at | When this job was opened. |
| Closed at | When this job was closed. |
| Updated at | When this job was last updated. |
| Departments | A list of departments which this job belongs to, including the **List size** and **List index**. |
| Offices | A list of offices which this job belongs to, including the **List size** and **List index**. |
| Hiring team | A list of [Greenhouse users](#user-object) who are responsible for this job. This includes **Hiring managers**, **Recruiters**, **Coordinators** and **Sourcers**. |
| Openings | A list of openings, including the **List size** and **List index**. Each opening contains an **Opening ID** and **Opening status**. |
| Custom fields and keyed custom fields | Custom fields and keyed custom fields are exposed as discrete datapills. |

Find out more about [Greenhouse job object](https://developers.greenhouse.io/harvest.html#the-job-object).

## Offer object

| Datapill | Description |
| --- | --- |
| Offer ID | A unique offer ID. |
| Version | The version of the current offer. |
| Application ID | The ID of the associated [Greenhouse application](#application-object). |
| Job ID | The ID of the associated [Greenhouse job](#job-object). |
| Candidate ID | The ID of the associated [Greenhouse candidate](#candidate-object). |
| Opening | Details about the opening that was associated with this offer. |
| Created at | When this offer was created. |
| Updated at | When this offer was last updated. |
| Sent at | When this job was sent to the candidate. |
| Resolved at | When this job was resolved. |
| Stats at | The data when the candidate starts. |
| Status | The status of the job offer. |
| Custom fields and keyed custom fields | Custom fields and keyed custom fields are exposed as discrete datapills. |

Find out more about [Greenhouse offer object](https://developers.greenhouse.io/harvest.html#the-offer-object).

---
