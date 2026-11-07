---
url: 'https://docs.workato.com/en/connectors/greenhouse/object-coverage.md'
description: >-
  Reference for the objects supported by Greenhouse v3 actions and triggers,
  including per-object fields and differences from v1 object coverage.
---

# Greenhouse v3 object coverage

This guide describes the objects supported by Greenhouse v3 actions and triggers. Object availability varies by action, and not all v1 objects are available in v3.

Use this guide to:

- Identify which objects each action and trigger supports
- Understand differences between v1 and v3 object coverage
- Plan updates when you migrate recipes to v3

## Action coverage

Refer to the following sections for supported objects by action:

- [Search objects (v3)](#search-objects-v3)
- [Create object (v3)](#create-object-v3)
- [Update object (v3)](#update-object-v3)

### Search objects (v3)

The **Search objects (v3)** action searches for records from a Greenhouse v3 endpoint and returns a paginated list of matching objects.

#### Supported objects

The following objects are supported:

- Applications
- Application stages
- Attachments
- Candidates
- Close reasons
- Custom field departments
- Custom field offices
- Custom field options
- Custom fields
- Departments
- Interviews
- Job hiring managers
- Job interview stages
- Job owners
- Job posts
- Jobs
- Offers
- Offices
- Openings
- Prospect pools
- Referrers
- Scorecards
- Sources
- User emails
- Users

#### Common input parameters

The following input fields are commonly available across supported objects:

| Input field | Type | Description |
| --- | --- | --- |
| Object | Picklist | Select the object type to search. |
| IDs | Array (integer) | Filter by specific record IDs. |
| Created at (from/to) | Date/time | Filter by creation date range. |
| Updated at (from/to) | Date/time | Filter by last update date range. |
| Per page | Integer | Number of records per page. |
| Cursor | String | Pagination cursor for the next page. |

Additional fields vary by object type. Use the following per-object fields where supported.

#### Applications

The **Applications** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Job IDs | Filter by associated job IDs. |
| Candidate IDs | Filter by associated candidate IDs. |
| Stage IDs | Filter by application stage IDs. |
| Source IDs | Filter by source IDs. |
| Status | Filter by application status. |
| Prospect | Filter by prospect status. |
| Last activity at (from/to) | Filter by last activity date range. |

#### Candidates

The **Candidates** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Email | Filter by candidate email. |
| Tag | Filter by candidate tag. |
| Private | Filter by private candidate status. |
| Last activity at (from/to) | Filter by last activity date range. |
| Custom field option ID | Filter by custom field option. |

#### Interviews

The **Interviews** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Application IDs | Filter by associated application IDs. |
| Candidate IDs | Filter by associated candidate IDs. |
| Job IDs | Filter by associated job IDs. |
| Job interview IDs | Filter by job interview IDs. |
| Organizer IDs | Filter by organizer IDs. |
| Starts at (from/to) | Filter by interview start time range. |
| Ends at (from/to) | Filter by interview end time range. |
| External event ID | Filter by external calendar event ID. |

#### Jobs

The **Jobs** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Status | Filter by job status. |
| Department ID | Filter by department ID. |
| Office ID | Filter by office ID. |
| Confidential | Filter by confidential jobs. |
| Requisition ID | Filter by requisition ID. |

#### Offers

The **Offers** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Application IDs | Filter by associated application IDs. |
| Job IDs | Filter by associated job IDs. |
| Candidate IDs | Filter by associated candidate IDs. |
| Status | Filter by offer status. |
| Sent on (from/to) | Filter by sent date range. |
| Starts on (from/to) | Filter by start date range. |
| Resolved at (from/to) | Filter by resolution date range. |

#### Scorecards

The **Scorecards** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Application IDs | Filter by associated application IDs. |
| Candidate IDs | Filter by associated candidate IDs. |
| Interview kit IDs | Filter by interview kit IDs. |
| Submitter IDs | Filter by submitter IDs. |
| Interviewer IDs | Filter by interviewer IDs. |
| Status | Filter by scorecard status. |
| Interviewed at (from/to) | Filter by interview date range. |
| Submitted at (from/to) | Filter by submission date range. |

### Create object (v3)

The **Create object (v3)** action creates a new record in Greenhouse.

#### Supported objects

The following objects are supported:

- Candidate
- Candidate note
- Candidate education
- Candidate employment
- Candidate application
- Job
- User

#### Candidate

The **Candidate** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| First name | Provide the candidate's first name. |
| Last name | Provide the candidate's last name. |
| Preferred name | Provide the candidate's preferred name. |
| Time zone | Provide the candidate's time zone. |
| Company | Provide the candidate's current company. |
| Title | Provide the candidate's current job title. |
| Can email | Specify whether the candidate can receive emails. |
| Phone numbers | Provide a list of phone numbers. |
| Addresses | Provide a list of addresses. |
| Email addresses | Provide a list of email addresses. |
| Website addresses | Provide a list of website URLs. |
| Social media addresses | Provide a list of social media profiles. |
| Tags | Provide a list of tags to assign to the candidate. |
| Linked user IDs | Provide user IDs to associate with the candidate. |
| Custom fields | Provide custom field values keyed by field token. |
| Application | Provide application details to create an associated application. |

##### Application (nested within Candidate)

The **Application** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Job ID | Provide the job ID when creating an application. |
| Prospect | Specify whether the candidate is a prospect. |
| Prospect pool ID | Provide the prospect pool ID. |
| Prospect pool stage ID | Provide the prospect pool stage ID. |
| Prospect owner ID | Provide the prospect owner user ID. |
| Source ID | Provide the source ID. |
| Recruiter ID | Provide the recruiter user ID. |
| Coordinator ID | Provide the coordinator user ID. |
| Referrer ID | Provide the referrer user ID. |
| Initial stage ID | Provide the initial application stage ID. |

#### Candidate note

The **Candidate note** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Candidate ID | Provide the candidate ID. |
| Application ID | Provide the application ID. |
| Body | Provide the note content. |
| Subject | Provide the note subject. |
| Note type | Specify the note type. |
| User ID | Provide the author user ID. |
| Email from | Provide sender email addresses. |
| Email to | Provide recipient email addresses. |
| Email CC | Provide CC email addresses. |
| Visibility | Specify visibility. |

#### Candidate education

The **Candidate education** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Candidate ID | Provide the candidate ID. |
| School name | Provide the school name. |
| Degree | Provide the degree. |
| Discipline | Provide the field of study. |
| Start date | Provide the start date. |
| End date | Provide the end date. |

#### Candidate employment

The **Candidate employment** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Candidate ID | Provide the candidate ID. |
| Company name | Provide the company name. |
| Title | Provide the job title. |
| Start date | Provide the start date. |
| End date | Provide the end date. |

#### Job

The **Job** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| Template job ID | Provide the template job ID to copy configuration from. |
| Number of openings | Provide the number of openings. |
| Job name | Provide the internal job name. |
| Job post name | Provide the job post name. |
| Notes | Provide internal notes. |
| Department ID | Provide the department ID. |
| External department ID | Provide the external department ID. |
| Office IDs | Provide office IDs. |
| External office IDs | Provide external office IDs. |
| Requisition ID | Provide the requisition ID. |
| Opening IDs | Provide opening IDs. |
| Custom fields | Provide custom field values keyed by field token. |

#### User

The **User** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| First name | Provide the user's first name. |
| Last name | Provide the user's last name. |
| Primary email | Provide the user's email address. |
| Employee ID | Provide the employee ID. |
| Job title | Provide the job title. |
| Agency ID | Provide the agency ID. |
| Office IDs | Provide associated office IDs. |
| Department IDs | Provide associated department IDs. |

### Update object (v3)

The **Update object (v3)** action updates an existing record in Greenhouse. Provide the object type and record ID.

#### Supported objects

The following objects are supported:

- Candidate
- Candidate application
- Job
- User

#### Candidate

The **Candidate** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| ID | Provide the candidate ID. |
| All candidate fields from Create | Provide any candidate fields from the **Create object** action. Only provided fields are updated. |

#### Candidate application

The **Candidate application** object supports the following additional fields:

| Parameter | Description |
| --- | --- |
| ID | Provide the application ID. |
| Source ID | Provide the source ID. |
| Referrer ID | Provide the referrer ID. |
| Recruiter ID | Provide the recruiter ID. |
| Coordinator ID | Provide the coordinator ID. |
| Prospect pool ID | Provide the prospect pool ID. |
| Prospect pool stage ID | Provide the prospect pool stage ID. |
| Rejected at | Provide the rejection date. |
| Created at | Provide the created date and time. |
| Custom fields | Provide custom field values keyed by field token. |

#### Job

The **Job** object supports the following additional fields:

| Input field | Description |
| --- | --- |
| ID | Provide the job ID. |
| All job fields from Create | Provide any job fields from the **Create object** action. Only provided fields are updated. |

#### User

The **User** object supports the following additional fields:

| Input field | Description |
| --- | --- |
| ID | Provide the user ID. |
| All user fields from Create | Provide any user fields from the **Create object** action. Only provided fields are updated. |

### Create attachment (v3)

The **Create attachment (v3)** action uploads a file attachment to an application.

#### Input

The following input fields are available:

| Input field | Description |
| --- | --- |
| Application ID | Provide the application ID to attach the file to. |
| Filename | Provide the file name, including extension. |
| Type | Provide the attachment type. |
| Content | Provide the file content as a Base64-encoded string. Required if URL is not provided. |
| URL | Provide a direct file URL. Required if **Content** isn't provided. |
| Visibility | Provide the visibility setting. |

### Move application (v3)

The **Move application (v3)** action moves an application to a different stage or transfers it to another job.

#### Input

The following input fields are available:

| Input field | Description |
| --- | --- |
| Application ID | Provide the application ID to move. |
| From stage ID | Provide the current stage ID of the application. |
| To stage ID | Provide the destination stage ID within the same job. Use this to move the application forward or backward in the pipeline. |
| To job ID | Provide the destination job ID to transfer the application to a different job. |
| Email from user ID | Provide the user ID that sends the notification email. |

### Reject application (v3)

The **Reject application (v3)** action rejects an application and optionally sends a rejection email.

#### Input

The following input fields are available:

| Input field | Description |
| --- | --- |
| Application ID | Provide the application ID to reject. |
| Rejection reason ID | Provide the rejection reason ID. |
| Notes | Provide internal notes for the rejection. |
| Send email at | Provide the date and time to send the rejection email. |
| Email template ID | Provide the email template ID to use for the rejection email. |
| Email from user ID | Provide the user ID that sends the rejection email. |
| Custom fields | Provide custom field values. Each item must include a field identifier and value. |

### Mark candidate as hired (v3)

The **Mark candidate as hired (v3)** action marks an application as hired and optionally assigns a start date, opening, and close reason.

#### Input

The following input fields are available:

| Input field | Description |
| --- | --- |
| Application ID | Provide the application ID to mark as hired. |
| Start date | Provide the candidate's start date. |
| Opening ID | Provide the opening ID to associate with the hire. |
| Close reason ID | Provide the close reason ID for the hire. |

## Trigger coverage

Refer to the following sections for supported objects by trigger:

- [New object (v3)](#new-object-v3)
- [New/updated object (v3)](#new-updated-object-v3)

### New object (v3)

The **New object (v3)** trigger fires when a new record is created in Greenhouse. It uses cursor-based polling.

#### Supported objects

The following objects are supported:

- Candidates
- Applications
- Interviews

#### Input

The following input fields are available:

| Input field | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| Since | Provide the start timestamp for the initial fetch. Defaults to 1 hour before the first run. |

#### Output

Returns the full object fields for the selected object type.

### New/updated object (v3)

The **New/updated object (v3)** trigger fires when a record is created or updated in Greenhouse. It returns records in batches.

#### Supported objects

The following objects are supported:

- Candidates
- Applications
- Job posts
- Jobs
- Offers
- Interviews
- Scorecards

#### Input

The following input fields are available:

| Input field | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| From | Provide the start timestamp for the initial fetch. Defaults to 1 hour before the first run. |
| Batch size | Specify the number of records per batch. |

#### Output

Returns the full object fields for the selected object type.

## Legacy (v1) to v3 mapping

This section describes how legacy (v1) actions and triggers align with their v3 equivalents.

### Actions

The following mappings describe how legacy (v1) actions align with v3 actions and supported objects.

#### Create object (v1) and Create object (v3)

The v3 **Create object** action consolidates and standardizes object creation across supported entities.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Candidate | Candidate |
| Candidate note | Candidate note |
| Candidate education | Candidate education |
| Candidate employment | Candidate employment |
| Candidate application | Candidate application |
| Job | Job |
| User | User |

Candidate email note doesn't have a v3 equivalent.

#### Update object (v1) and Update object (v3)

The v3 **Update object** action uses the same object model as create and updates only the fields you provide.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Candidate | Candidate |
| Application | Candidate application |
| Job | Job |
| User | User |

#### Search objects (v1) and Search objects (v3)

The v3 **Search objects** action expands object coverage and introduces a unified search interface.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Candidate | Candidates |
| Application | Applications |
| Job | Jobs |
| Offer | Offers |
| User | Users |
| Scorecard | Scorecards |
| Prospect pool | Prospect pools |

Degree, School, and Discipline don't have direct v3 search endpoints.

#### Upload attachment (v1) and Create attachment (v3)

The v3 **Create attachment** action supports uploading files to applications.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Application attachment | Attachment |

Candidate attachment doesn't have a direct v3 equivalent.

#### Advance application (v1) and Move application (v3)

The v3 **Move application** action replaces advance application and supports stage movement and job transfer.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Application | Application |

#### Reject application (v1) and Reject application (v3)

The v3 **Reject application** action preserves the same core behavior and adds optional email controls.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Application | Application |

#### Mark candidate as hired (v1) and Mark candidate as hired (v3)

The v3 **Mark candidate as hired** action preserves the same behavior and adds optional fields such as start date and opening.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Application | Application |

### Triggers

The following mappings describe how legacy (v1) triggers align with v3 triggers and supported objects.

#### New object (v1) and New object (v3)

The v3 trigger detects newly created records with cursor-based polling.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Candidate | Candidate |
| Application | Application |
| Scheduled interview | Scheduled interview |

#### New/updated object (v1) and New/updated object (v3)

The v3 trigger detects created and updated records and returns results in batches.

The following table shows how v1 objects align with v3:

| v1 object | v3 object |
| --- | --- |
| Candidate | Candidate |
| Application | Application |
| Job post | Job post |
| Job | Job |
| Offer | Offer |
| Scheduled interview | Scheduled interview |
| Scorecard | Scorecard |

---
