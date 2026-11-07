---
url: >-
  https://docs.workato.com/en/agentic/workato-genies/hr/hr-self-service-genie/features.md
description: >-
  Core and extended features of HR Self Service Genie, from time-off management
  and approvals to HR knowledge Q&A and reference letters.
---

# HR Self Service Genie features

HR Self Service Genie handles routine HR requests for employees and managers in chat. Every deployment includes the core features, and you can enable extended features on top of them.

## Core features

Core features provide profile lookups, time-off management, manager approvals, and holiday information.

### Employee profile and organization information

Employees can retrieve their own Workday profile, manager, and reporting chain. Managers can also list their direct reports. The core skills enforce employee and manager access boundaries, so they return only the employee's own record and a manager's direct reports. The [employee lookup](#employee-lookup) extension adds profile lookups across departments.

### Time-off balances and requests

Employees can check available time-off types and balances, then view, submit, and cancel time-off requests in Workday without leaving chat. Only in-progress requests can be canceled.

### Manager time-off management

Managers can view time-off requests and balances for confirmed direct reports, and approve or reject their requests.

### Approval and notification workflow

The approval workflow notifies managers about pending time-off requests and tracks each request through approval. Employees receive status updates when a request is approved, rejected, sent back, or reaches another outcome, including actions taken directly in Workday.

### Holiday calendar

The genie retrieves location-specific holidays for a requested date range from Workday, and combines them with organization-wide Global Days Off from the HR knowledge base.

## Extended features

Extended features are optional and maintained separately from the core. Enable a feature when its required connections and Workday permissions are configured.

### Employee data management

Employees can update their own name, contact, demographic, biographic, and identification information through Workday Web Services skills. The genie applies Workday security permissions to each update, blocks changes to restricted attributes, such as the primary work email, and checks the mandatory fields and country-specific values in the Workday Validation Fields knowledge base. It asks the employee for anything missing or invalid.

### Worker document access

Employees can list and retrieve the worker documents they can access in Workday. The genie respects the document permissions defined in Workday and cleans up temporary document copies. It retrieves only documents that employees uploaded in Workday, not documents stored under other Workday objects.

### Employee lookup

Employees can look up a colleague's public workplace information in Workday, such as contact details, by providing the colleague's employee ID or work email. The genie returns only the fields that the Workday security model allows and doesn't return sensitive information, such as compensation.

### HR knowledge Q&A

The genie answers HR policy questions using the HR knowledge base, so responses are based on approved organizational content. This feature requires a configured HR knowledge base. Refer to [Enable HR knowledge Q&A](/en/agentic/workato-genies/hr/hr-self-service-genie/setup#enable-hr-knowledge-qa) for more information.

### HR knowledge ingestion

The genie syncs approved HR content from Confluence to its knowledge base on a schedule that you set, so answers reflect current policies. It supports full and incremental loads, and source filters determine which content is synced.

### Knowledge gap tracking

The genie records the conversation, question, and response in the **KB Gap User Conversations** data table when the knowledge base can't answer an HR question. Administrators can review this table to identify policies that need to be added or updated. The genie does not generate or infer policy when authoritative content is unavailable.

### HR reference letters

Employees can generate HR reference letters as PDFs. Supported letter types include:

- Employment Verification Letter
- No Objection Certificate
- Business Visa Application – Employment Letter
- Business Visa Application – Invitation Letter

The genie retrieves employment details from Workday and asks only for the additional information required for the selected letter type. By default, the genie doesn't generate letters for employees whose business title contains "Intern" or "Contractor". Configure the letter templates with the message templates tool or another tool you choose. The packaged extension stores and delivers letters through Workato FileStorage. You can customize the storage and delivery steps to use another document repository.

### HR ticketing

The genie offers to raise an HR ticket in Jira Service Management when the knowledge base can't answer an HR question. It checks for known problems and workarounds first, collects the fields the request type requires, and confirms the details with the employee before it creates the ticket. Employees can also list their open tickets, check a ticket's status, and add comments. The genie uses the employee's verified identity to limit which tickets it returns.

### Custom skills

Use the **Custom Extensions** folder to build new skills and integrations, customize cloned extension assets, or add deployment-specific knowledge ingestion. Keep assets in **Extensions** unchanged unless you are customizing a cloned copy.
