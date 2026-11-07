---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/hr/hr-self-service-genie/how-it-works.md
description: >-
  Learn how HR Self Service Genie routes requests, enforces access boundaries,
  runs approvals and notifications, and builds holiday responses.
---

# How HR Self Service Genie works

HR Self Service Genie decides how to handle each request, checks access boundaries before it acts, and runs the matching capability, from time-off approvals to HR ticketing.

## Request processing

HR Self Service Genie routes each message by type. Policy questions go to the HR knowledge base. Transactional requests, such as checking a time-off balance or submitting leave, go to the matching Workday skill. Some requests have no enabled skill or configured knowledge source that supports them. For those, the genie explains that self-service can't complete the request and directs the employee to HR, or offers to raise an HR ticket if HR ticketing is enabled. It never simulates an action or invents a result.

## Access boundaries

The genie maps the request to the authenticated employee identity and checks the applicable employee or manager boundary before it acts:

- Employees can retrieve or update only their own supported HR information.
- Employees can also retrieve public workplace information for other employees when the employee lookup extension is enabled.
- Managers can view time-off information and approve or reject requests only for confirmed direct reports. The genie verifies the manager-to-employee relationship before returning direct-report data or applying a decision.
- Workday security permissions and business processes still apply. The genie cannot bypass Workday validation or approval requirements.

## How time-off requests work

The genie retrieves the employee's available balance and confirms the leave type, start date, and end date before submitting a request. The balance covers the number of days ahead set in the **TimeOffBalances.RetrieveBalanceForDaysFollowing** project property. The genie asks whether to proceed when the balance is insufficient or the dates include weekends in the employee's location. It then submits the request to Workday and returns the resulting status.

Each request is recorded in the **Time Off Requests** data table in **Runtime Data**, along with its status, approver, and notification timestamps. The notification workflow uses this table to determine whom to notify and when.

## How approvals and notifications work

The approval workflow routes the time-off request to the employee's manager when manager approval is required. Managers can approve or reject one or more requests through the genie and may include a comment. The genie applies each decision to the Workday request only while the request remains in progress.

Manager notifications run on a schedule set in project properties. Managers are notified at the next scheduled run, not when an employee submits a request.

- **Manager notifications**: A scheduled run checks Workday for pending time-off requests, including requests entered directly in Workday, and sends each manager a consolidated notification of their pending queue. Set the schedule with **ApprovalWorkflow.ManagerNotificationTriggerSchedule**. Reminders for requests that remain pending repeat at the interval set in **TimeOffRequests.ReminderFrequencyDays**.
- **Employee notifications**: When a manager acts on a request through the genie, the employee is notified right away. A scheduled run detects requests handled directly in Workday and sends each employee a consolidated update that includes any comments. Set the schedule with **ApprovalWorkflow.EmployeeNotificationTriggerSchedule**.

## How holiday responses work

For general holiday questions, the genie combines these sources in one table:

- **Location-specific holidays**: Retrieved from Workday for the authenticated employee. They depend on the holiday data configured in Workday for the employee's location.
- **Global Days Off**: Retrieved from the HR knowledge base. They appear only when the relevant policy content is available there.

The **Type** column shows whether a holiday applies to the employee's location or is a global day off. The genie returns only one source when the user asks for location-specific holidays or Global Days Off alone.

## How knowledge gap tracking works

The genie doesn't generate an answer to a question that the HR knowledge base can't answer. It directs the user to the appropriate HR resource and records the conversation, user query, genie response, and gap classification in the **KB Gap User Conversations** data table in **Runtime Data**. Gap tracking complements the full and delta ingestion loads. The recorded gaps show which HR content to add or update, and the genie can answer the question after the next ingestion picks up that content.

## How HR reference letters work

The HR Reference Letters extension retrieves the employee's details from Workday and collects any additional information required for the selected letter type. The genie asks the employee to confirm those details before generating the letter.

Each letter is generated from a Workato [message template](/en/features/message-template) configured for that letter type. The template controls the letter's content, formatting, and branding. The extension then delivers the PDF through the configured document storage, which is [Workato FileStorage](/en/features/workato-filestorage) in the packaged extension. Files are eligible for cleanup after the number of days set in the **Delete Files Older Than in Days** project property.

## How personal information updates work

The genie retrieves the mandatory fields and supported reference values for the requested change from the **Workday Validation Fields** knowledge base before an update. It asks the employee for anything missing and checks reference values against the Workday configuration for the employee's country. The genie runs the Workday operation only after the update passes validation, and it never updates restricted fields, such as the primary work email.

The knowledge base holds the validation values you add. Refer to [Configure Workday validation fields](/en/agentic/workato-genies/hr/hr-self-service-genie/setup#configure-workday-validation-fields) to set it up.

## How HR ticketing works

HR ticketing requires the HR ticketing extension. The genie offers to raise a ticket when the knowledge base can't answer a question, and employees can also ask for one directly. The genie raises a ticket only after the employee agrees. It checks for known problems, identifies the request type, collects the fields that type requires, and confirms the details with the employee before it creates the ticket.

The request types and their fields come from the `hr_service_desk_request_types.json` file in FileStorage. The genie reports a ticket as created or updated only after Jira confirms the operation, then returns the ticket details.

Ticket searches return only the employee's own tickets. Employees can retrieve the details of a ticket and add comments by providing its issue key, so colleagues who share a project can follow up on the same ticket. You can limit this by cloning the **Get Jira Service Desk Issue Details** and **Add Comment to Jira Service Desk Issues** skills into **Custom Extensions** and modifying them.

## Folder structure

The HR Self Service Genie project is organized into the following top-level folders:

- **Config**: Connections and metadata required to run HR Self Service Genie.
- **Core**: Foundational skills maintained by Workato. You can't modify or clone these skills.
- **Extensions**: Additional app skills and functions maintained by Workato and updated during release cycles. You can use these as-is or as a reference when you build custom integrations.
- **Custom Extensions**: Custom assets that you maintain. Clone Extension assets into this folder before you modify them. Assets in this folder remain intact across upgrades.
- **Runtime Data**: Data tables that store the data HR Self Service Genie generates during runtime.

View folder structure

```text
Agentic | HR Self Service Genie
├── Config
│   ├── Connection
│   └── Metadata
├── Core
│   ├── Approval Workflow
│   │   └── Workday
│   └── Skills
│       └── Workday REST
├── Extensions
│   ├── App Events
│   ├── File Management & Cleanup
│   ├── Knowledge Ingestion
│   │   ├── Confluence
│   │   └── Workday
│   ├── Skills
│   │   └── Workday SOAP
│   └── Ticketing
│       └── Apps
│           └── Jira Service Desk
├── Custom Extensions
│   └── Knowledge Ingestion
└── Runtime Data
```

The HR reference letters skill, `get_hr_reference_letters`, is in **Extensions > Skills > Workday SOAP**. The notification recipes are in **Core > Approval Workflow > Workday**, and the notification function is in **Extensions > App Events**. The **Time Off Requests** and **KB Gap User Conversations** data tables are in **Runtime Data**.

### Working with Extensions and Custom Extensions

You can activate Extension skills and add them to HR Self Service Genie as-is. You can also clone them into **Custom Extensions** to customize them or build support for apps that aren't available in the **Extensions** folder.

Customizations in **Custom Extensions** are isolated from platform updates and remain intact across upgrades. You can't clone or modify core skills.
