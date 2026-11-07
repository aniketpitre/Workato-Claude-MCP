---
url: 'https://docs.workato.com/en/airo/blueprints/requirements-best-practices.md'
description: >-
  Structure requirements in chat or a PRD or BRD so they map to the right
  assets.
---

# Best practices for writing requirements

AIRO maps your requirements onto the Workato assets it builds, such as recipes, skills, and genies. The clearer your requirements, the more accurately AIRO can map them, and the less rework you'll do after the blueprint is generated.

A written requirements document isn't required. You can describe what you need conversationally and let AIRO ask clarifying questions as you go. The same details help AIRO map your requirements to the right assets, whether you're chatting with AIRO directly or preparing a PRD or BRD in advance.

## Describe the outcome, not the task

State what the automation should accomplish and for whom, not just a general area to improve.

- **Recommended**: `When a support ticket is tagged Billing, look up the customer's account status in Salesforce and post a summary to the assigned agent's Slack channel.`
- **Not recommended**: `Help our support team with billing tickets.`

A specific outcome tells AIRO which systems are involved and what a successful run looks like. A general goal forces AIRO to guess, or to spend a round of clarifying questions narrowing it down.

## List your applications and objects

Name every system involved and the records or objects your automation reads or writes. A table works well for this, for example:

| Application | Purpose | Objects/Data |
| --- | --- | --- |
| Salesforce | Customer account lookup | Accounts, Cases |
| Slack | Agent notification | Channels, Messages |

AIRO asks clarifying questions to identify your systems if you don't name them upfront. If your workspace has more than one connection to the same application, such as a Salesforce sandbox and a Salesforce production instance, specify which connection each process should use.

## Spell out business logic and error handling

AIRO's [blueprint flow](/en/airo/blueprints/create#fill-in-the-gaps) asks clarifying questions to fill in whatever your requirements leave out before mapping them onto assets, specifically around:

- Problem and business context
- Applications and objects
- Execution and frequency
- Business logic and validation
- Error handling

The more of these you answer upfront, the fewer clarifying questions AIRO needs to ask before it can map your requirements into a blueprint. This matters most for business logic and error handling, which are the details most likely to be missing from a first draft:

- **Business logic**: What conditions change the automation's behavior. For example, `escalate to a manager if the discount requested is above 15%`, not just `handle discount requests`.
- **Error handling**: What should happen when a step fails or a system is unavailable. For example, `retry the API call up to 3 times, then notify the requester and log the failure`, not just `handle errors`.

Review the [generated blueprint](/en/airo/blueprints/create#generate-your-blueprint) against your original business rules, particularly for conditional logic. Confirm each rule is reflected the way you intended before you build the underlying assets.

## If you do write a PRD or BRD, structure it consistently

Group your requirements into categories that tend to map cleanly onto the assets AIRO builds:

1. **Summary**: What the automation does and why it's needed.
2. **Applications and objects**: The systems and data involved, often shown as a table.
3. **Triggers**: What starts each process.
4. **Functional requirements**: What the automation must do, broken into logical sections.
5. **Error handling and exceptions**: What happens when something goes wrong, by condition.

This isn't a required or exhaustive structure. AIRO can work from other formats and use any additional context you provide. Organizing requirements this way makes it easier for AIRO to map them to the right assets, and easier for you to spot gaps before you start.

You can use the following template as a starting point:

```markdown
# PROJECT_NAME PRD

## Summary

[What the automation does and why it's needed.]

## Applications and objects

*One row per application.*

| Application | Purpose                      | Objects/Data           |
| ----------- | ---------------------------- | ---------------------- |
| [App name]  | [Purpose in this automation] | [Objects or data used] |

## Triggers

| Process        | Trigger         | Frequency                |
| -------------- | --------------- | ------------------------ |
| [Process name] | [Trigger event] | [Real-time/hourly/daily] |

## Functional requirements

*One subsection per feature area.*

### [Feature area name]

- [What the automation must do]
- [A business rule or condition]

## Error handling and exceptions

*One Condition/Resolution pair per error scenario.*

**Condition**: [What triggers this handling]

**Resolution**:

- [For example: Retry up to N times, then notify the requester and log the failure]
- [For example: Skip the record and continue processing the next one]
```

These categories are a starting point, not a constraint. For example, a genie's requirements may also include its AI provider and model, the skills and knowledge sources it uses, and a job description covering what it does, who it helps, and how it should communicate.

Review the following filled-out examples:

See the Onboarding Genie example PRD

**Onboarding Genie PRD**

**Summary**

The Onboarding Genie serves as each new hire's AI assistant. It provides real-time status updates, schedules meetings, processes application access requests, and escalates complex issues to support teams. This AI-powered assistant transforms the new hire experience by offering personalized guidance and immediate support throughout the onboarding journey.

**Problem Statement**

New hires currently feel lost and uninformed about their onboarding progress, leading to:

- Confusion about next steps and expectations
- Difficulty accessing help when needed
- Delays in resolving onboarding issues
- Poor new employee satisfaction affecting retention

**Applications & Objects**

| Application | Purpose | Objects/Data |
| --- | --- | --- |
| Workday | Employee data and management chain | Workers, Positions, Manager relationships |
| Outlook | Meeting scheduling and calendar management | Users, Calendar Events, Availability |
| Okta | Identity verification and access requests | Users, Groups, Applications |
| Jira | Issue tracking and escalation | Tickets, Projects, Assignments |

**Triggers**

| Process | Trigger | Frequency / Schedule |
| --- | --- | --- |
| Onboarding Genie Activation | New hire's employee record reaches their start date | Real-time (event-based) |

**Functional Requirements**

**AI Assistant Activation and Core Functionality**

**Requirements:**

- Activate the Onboarding Genie on the new hire's start date
- The Genie must provide personalized guidance based on the employee's position and department
- The Genie must provide status updates on onboarding progress and next steps

**Implementation Details:**

- Extract worker information from Workday for personalization
- Use employee department and role data to customize guidance
- Implement natural language processing for question interpretation
- Maintain session state and conversation history

**Meeting Scheduling Capability**

**Requirements:**

- The Genie must process meeting requests from new hires
- The system must check participant availability using Outlook Calendar
- The Genie must create calendar events with 30-minute default duration
- Meeting invites must be sent to all participants automatically
- The system must handle scheduling conflicts and suggest alternative times

**Implementation Details:**

- Integrate with Outlook Calendar API for availability checks
- Default meeting duration of 30 minutes unless specified otherwise
- Include relevant onboarding context in meeting invitations
- Provide rescheduling options when conflicts occur

**Access Request Management**

**Requirements:**

- The Genie must handle self-service application access requests
- The system must validate requester identity using Okta
- Access requests must be routed to appropriate approval workflows
- The Genie must provide status updates on pending access requests
- The system must notify users when access has been granted or denied

**Implementation Details:**

- Use Okta for identity verification before processing requests
- Route requests based on application type and organizational policies
- Track request status and provide real-time updates
- Send notifications for request status changes

**Issue Escalation and Ticket Creation**

**Requirements:**

- The Genie must identify complex issues that require human intervention
- The system must create Jira tickets for escalated issues with full context
- Tickets must be routed to appropriate support teams based on issue type
- The system must use Workday data to identify correct managers and support contacts
- Escalated issues must include conversation history and relevant employee information

**Implementation Details:**

- Define escalation triggers for different issue types
- Create Jira tickets with comprehensive context and troubleshooting history
- Use Workday manager lookup for proper routing
- Preserve chat history for human support reference
- Provide estimated resolution timelines to employees

**Employee Data Integration**

**Requirements:**

- The system must access employee information via a new Employee Directory API endpoint
- The system must retrieve and utilize the following employee data:
  - Basic information: first name, last name, work email, worker ID, phone
  - Organizational details: department, cost center, manager, direct reports
  - Employment information: start date, position title, employment type, location
  - Status information: active/inactive, PTO status

**Implementation Details:**

- Required parameter: employee\_id
- Use retrieved data for personalized interactions and proper routing
- Cache employee data appropriately for performance
- Handle API failures gracefully with fallback procedures

**Error Handling & Exception Management**

**System Availability Exceptions**

**Condition**: Target systems (Workday, Outlook, Okta, Jira) unavailable

**Resolution**:

- Implement retry logic with exponential backoff
- Provide offline guidance where possible
- Escalate to human support after 3 failed attempts
- Log all system availability issues for monitoring

**Data Integration Exceptions**

**Condition**: Missing or incomplete employee information

**Resolution**:

- Use generic onboarding guidance when personalized data unavailable
- Flag missing data for HR review
- Notify manager of data gaps that affect onboarding quality
- Continue service with available information

**Business Logic Exceptions**

**Condition**: Invalid or complex requests beyond Genie capabilities

**Resolution**:

- Create Jira ticket with full context and conversation history
- Route to appropriate support team based on request type
- Provide estimated resolution timeline to employee
- Send confirmation that issue has been escalated

**Technical Implementation Notes**

- All Jira ticket creation logic must be embedded directly in the Genie workflow
- System must maintain conversation context and history throughout onboarding period
- Escalation procedures must preserve complete chat history for human support context
- Error handling should be graceful with clear communication to users about next steps

See the Salesforce to NetSuite example PRD

**Salesforce to NetSuite order synchronization PRD**

**Summary**

Sales orders created in Salesforce aren't automatically synced to NetSuite, requiring manual data entry that leads to errors and delays in order fulfillment. This automation syncs order data between Salesforce and NetSuite in real time, in both directions, to eliminate manual entry and cut order processing time.

**Applications and objects**

| Application | Purpose | Objects/Data |
| --- | --- | --- |
| Salesforce | Order source and status updates | Order, Customer, Product, Pricing |
| NetSuite | Order fulfillment and reconciliation | Sales Order, Customer, Shipment, Tracking |
| Email | Reconciliation reporting | Report |

**Triggers**

| Process | Trigger | Frequency / Schedule |
| --- | --- | --- |
| New order synchronization | Order status changes to Approved in Salesforce | Real-time |
| Order status update synchronization | NetSuite order status changes | Every 15 minutes (polling) |
| Daily order reconciliation | Scheduled report generation | Daily at 6:00 AM EST |

**Functional requirements**

**New order synchronization**

- Validate that all required fields are present before syncing
- Transform the Salesforce order format to the NetSuite sales order format
- Check whether the customer exists in NetSuite, and create the customer record if not
- Create or update the sales order in NetSuite, then update the Salesforce order record with the resulting NetSuite order ID
- Order total must be greater than zero, the billing address must be complete, all line items must have valid NetSuite SKUs, payment terms must match approved values, and the order date can't be in the future

**Order status update synchronization**

- Query NetSuite for orders updated in the last 15 minutes
- Match the NetSuite order ID to the Salesforce order using the external ID field, then update the Salesforce order's status and tracking fields
- Send a customer notification email when the status changes to Shipped
- Status can't transition backward, for example from Shipped to Pending

**Daily order reconciliation**

- Retrieve orders created or modified in the last 24 hours from both Salesforce and NetSuite
- Match orders by external ID, and compare order totals (within $0.01) and status between systems
- Flag any orders older than 1 hour that haven't synced
- Generate an Excel report of discrepancies and email it to finance and sales operations

**Error handling and exceptions**

**Condition**: Customer not found in NetSuite during order creation

**Resolution**:

- Create the customer record in NetSuite, then retry the order creation

**Condition**: Product SKU is invalid

**Resolution**:

- Log the error and notify the sales rep by email

**Condition**: NetSuite connection fails

**Resolution**:

- Retry up to 3 times with exponential backoff, then queue for manual review

**Condition**: Matching Salesforce order not found during status sync

**Resolution**:

- Log a warning and skip

**Condition**: Report generation fails during daily reconciliation

**Resolution**:

- Retry once, then escalate to IT

---
