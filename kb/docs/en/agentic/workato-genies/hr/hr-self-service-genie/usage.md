---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/hr/hr-self-service-genie/usage.md
description: >-
  Use HR Self Service Genie for time off, approvals, profile lookups, HR policy
  questions, reference letters, and HR tickets, with example prompts.
---

# Use HR Self Service Genie

You can message HR Self Service Genie in your organization's chat interface. The package uses Slack by default. Available actions depend on your role and on the extensions your administrator enabled.

> **FOR ADMINS**
> 
> Open the genie's **End user access** tab to give users access. Confirm that the end-user groups are configured there and that their members can reach the connected chat interface.

## Manage time off

Check balances and leave types, view your requests, and submit or cancel requests. Include the leave type and dates to reduce follow-up questions, and review the details before confirming a submission.

- `How much vacation time do I have?`
- `What leave types are available to me?`
- `Show my pending time-off requests.`
- `Request vacation from September 14 to September 18.`
- `Cancel my pending vacation request.`

## Manage your team's time off

Managers can view direct-report information and act on their time-off requests. Name the direct report when asking about a specific person or taking an approval action. You can approve or reject several requests at once and include a comment.

The genie notifies managers of pending requests on the schedule configured by an administrator. Refer to [How approvals and notifications work](/en/agentic/workato-genies/hr/hr-self-service-genie/how-it-works#how-approvals-and-notifications-work) for more information.

- `Who reports to me?`
- `Show the time-off balances for my direct report.`
- `Which time-off requests from my team are pending?`
- `Approve the pending time-off request for EMPLOYEE_NAME.`
- `Reject the time-off request for EMPLOYEE_NAME.`

## View and update your information

View your profile, manager, and reporting chain. You can also update supported personal information. The genie checks the required fields and country-specific values, asks you for anything missing or invalid, and runs the Workday operation only after the update passes validation. Your administrator must enable the employee data extension for updates.

- `Show my employee profile.`
- `Who is my manager?`
- `Show my reporting chain.`
- `Update my phone number.`
- `Update my preferred name.`

## Look up a colleague

Find a colleague's public workplace information, such as how to contact them. Include the colleague's employee ID or work email. The genie doesn't return sensitive information, such as compensation. Your administrator must enable the employee lookup extension.

- `Show me the profile for EMPLOYEE_ID_OR_EMAIL.`

## Find and download worker documents

List the documents available to you in Workday and request a document by name. The genie returns a shareable download link. Your administrator must enable the worker document extension.

- `What worker documents are available to me?`
- `Download my DOCUMENT_NAME.`

## Ask about HR policies

Ask about HR policies. The genie answers from the HR knowledge base and directs you to the appropriate HR resource when the knowledge base doesn't cover a question. It also records a knowledge gap for administrators to review.

- `What is the parental leave policy?`
- `What is the reimbursement policy for business travel?`
- `What is the remote-work policy?`

## Raise and track HR tickets

Raise an HR ticket when the genie can't answer a question or when you have an HR issue. The genie checks for known problems, asks for the details the request type requires, and confirms them with you before it creates the ticket. Include the ticket key when you ask about a specific ticket. Your administrator must enable the HR ticketing extension.

- `Raise an HR ticket for my missing payslip.`
- `I couldn't find the answer to my HR policy question. Can you raise a ticket?`
- `Show me my open HR tickets.`
- `What is the status of my ticket TICKET_KEY?`
- `Add a comment to my ticket TICKET_KEY.`

## Check holidays

Ask about upcoming holidays. The genie returns location-specific holidays and Global Days Off in one table. Ask for either category on its own to see results from that source only.

- `Show me all the upcoming holidays.`
- `Show me all the holidays in January.`
- `Show me the holidays between November 19 and January 2.`
- `What holidays apply to my location?`
- `What are our Global Days Off?`
- `Are there any holidays next month?`

## Request an HR reference letter

Request a supported letter. The genie asks for any details it can't retrieve from Workday, then asks you to confirm them before it generates the PDF. Your administrator must enable the HR reference letter extension. By default, employees whose business title contains "Intern" or "Contractor" can't request letters.

- `I need an employment verification letter.`
- `Generate a No Objection Certificate for me.`
- `I need a Business Visa Application – Employment Letter.`
- `Generate a Business Visa Application – Invitation Letter.`

## Limitations

- **Access scope**: Employees can retrieve or update only their own supported HR information. The exception is the public workplace information that the employee lookup extension returns for other employees. Managers can view time-off information and take approval actions only for confirmed direct reports.
- **Time-off cancellation**: You can cancel only in-progress requests.
- **Time-off corrections**: Corrections are not supported. Submit or cancel requests through the genie, and make corrections in Workday.
- **Personal information updates**: Updates are limited to name, contact, demographic, biographic, and identification information. The genie cannot show restricted fields, such as Supervisor ID, or update the primary work email.
- **Employee lookup**: Lookup accepts an employee ID or work email. It doesn't search by name.
- **HR knowledge coverage**: Policy answers come only from the configured HR knowledge base. The genie doesn't infer or generate a policy when the required policy is unavailable, incomplete, or lacks employee-specific context. It directs you to the appropriate HR resource instead.
- **Holidays**: Location-specific holidays depend on the holiday data configured in Workday for your location. Global Days Off appear only when the relevant policy content is available in the HR knowledge base.
- **HR ticketing**: The genie can't change ticket status, run workflow transitions, or close tickets.
