---
url: 'https://docs.workato.com/en/user-accounts-and-teams/admin-email.md'
description: >-
  Learn how to assign Workato email notification contacts for admin, technical,
  error, legal, and billing alerts across workspaces and environments.
---

# Email notifications

As an [Automation HQ](/en/automation-hq) or workspace administrator, it's important to assign specific contacts to receive different email notifications in your organization. Workato sends out important updates such as usage alerts, incident and error notifications, legal, and security updates.

An admin can designate contacts to receive emails for [admin notifications](#admin-notifications) and [other notifications](#other-notifications) in the [Notifications](https://app.workato.com/members/settings/notifications) page under **Workspace admin > Settings > Workspace > Notifications**. They can also designate contacts to receive emails for [recipe error alerts](#error-notifications) in the [Error alerts](https://app.workato.com/members/settings/env_notifications) page under **Workspace admin > Settings > Debug and logs > Error alerts**.

* * *

## Set up contacts in different workspaces/environments

The availability of contact fields in your Workspace admin settings may vary depending on your workspace or environment. This distinction exists because certain contacts, such as the Legal contact for your company, only need to be set once for the entire organization. On the other hand, some contacts, such as the Admin and Error notification emails, are specific to workspaces and environments.

### Workspace admin

You can configure notifications for all contacts in your Workspace admin settings. However, if you are in a workspace within your organization, you won't have visibility or access to the Company-scoped contacts, including Security & Privacy, Legal, and Billing contacts.

Within an environment, however, you can set up the specific [Admin and Technical contacts](#admin-notifications), [Error notification recipients](#error-notifications) and a [Primary business sponsor](#other-notifications) for the specific workspace. You must have an **Environment admin** or legacy **Admin** role to configure workspace settings.

### Environments

In workspaces with [environments](/en/features/environments), you only need to configure notification preferences once for your workspace in the main DEV environment. In the TEST and PROD environments, you can only specify [Recipe error alerts](#error-notifications) to accommodate the fact that distinct users operate and build/test in different environments.

## Admin notifications

![Configure admin notification contacts](/assets/admin-notification-email.Z7Lnb6uK.png)

Two primary contacts should receive Admin notifications: the **Primary admins** and the **Technical contacts**. You can assign multiple contacts or email aliases to receive these notifications by entering a comma-separated list of emails.

For example: `admin-one@yourdomain.com, alias@yourdomain.com`

### Primary admins

Primary admins are the main, active users and administrators of the workspace. They receive all notifications about usage, incidents, and account updates. We **highly recommend** adding at least one contact in this field to avoid missing important information.

If no **Primary admins** are configured, the **workspace owner** or **account email** receives these notifications by default.

Additionally, the following events trigger a primary admin email notification when they occur in the workspace:

- Collaborator joined the workspace
- Collaborator left the workspace
- Community connector approved by the Workato community team
- Community connector updated by the Workato community team
- Transaction quota threshold
- Access request for an API collection
- Deployment package deployed

### Technical contacts

Technical contacts are members in your workspace that own recipe and technical implementation. Workato platform connectors and features, including the [OPA](/en/on-prem/agents#on-prem-agent) and [API platform](/en/api-management#api-platform), are frequently updated and may require changes from your recipe building team. If incidents occur that affect the components the workspace uses, Workato sends notifications to the technical contact.

List the technical contacts in your organization in this field so these critical updates are not missed.

## Recipe error alerts

![Configure error notification settings](/assets/error-notification-email.BKgariQP.png)

Monitoring recipe errors and failed jobs is critical in operations and ensuring uptime. Use the **Recipe error alerts** section in **Workspace admin > Settings > Debug and logs > Error alerts** to configure recipients of recipe and job-related notifications.

You can assign multiple contacts or email aliases to receive these notifications by entering a comma-separated list of emails.

> **ENVIRONMENT-SPECIFIC ERROR ALERTS**
> 
> Error alerts can be configured separately for each environment when environments are enabled. You can set different recipients for each environment. Workato sends alerts to the root account email if no recipients are set.

Workato sends recipe error alerts in the following scenarios:

- When a job error occurs during action execution.
- When a recipe encounters 3 consecutive trigger errors.
- When a recipe is stopped after 60 consecutive trigger errors.

Learn more about [trigger errors](/en/recipes/error-notifications#trigger-errors), [trigger warnings](/en/recipes/error-notifications#trigger-warnings), [action errors](/en/recipes/error-notifications#action-errors), and Workato's [error notification policy](/en/user-accounts-and-teams/admin-email#error-notifications).

By default, Workato sends recipe error alerts for all recipes in your [projects](/en/projects#projects). The **Receive error notifications only from specific projects** toggle provides greater flexibility to our customers on receiving notifications from recipes that matter to them. Deselect each project containing the recipes you don't want to receive error notifications from.

## Other notifications

![Configure contacts for business sponsor, legal/security and billing](/assets/other-notification-email.CpJNYQDB.png)

Other notifications include notices about invoices, legal, security, and account-level updates. This category has four contact types:

- Primary business sponsors
- Security & privacy contacts
- Legal contacts
- Billing contacts

> **AHQ WORKSPACES**
> 
> If your organization uses [Automation HQ](/en/automation-hq), Security & privacy contacts, Legal contacts, and Billing contacts are company-scoped and only configurable from the AHQ workspace. In managed workspaces, [workspace moderators](/en/ahq-workspace-moderator) can only configure **Primary business sponsors**.

### Primary business sponsors

Primary business sponsors are the Workato champions who receive updates on your account. These contacts are usually executive sponsors for the Workato program at your organization. These updates are sent on an ad hoc basis from your customer success manager or our customer experience teams.

### Security & privacy contacts

These contacts usually belong to your organization's security team. They receive security and privacy notifications such as sub-processor and policy updates. You may also provide an alias (for example, `privacy@yourdomain.com`).

### Legal contacts

These contacts usually belong to your organization's legal team. These contacts receive legal, DPA (Data Protection Authority), or contract related updates. You may also provide an alias (for example, `legal@yourdomain.com`).

### Billing contacts

Lastly, enter your organization's billing contact. This contact usually belongs to your organization's finance team. They receive invoices, receipts, and other billing-related notifications. You may also provide an alias (for example, `accounts_payable@yourdomain.com` or `billing@yourdomain.com`).

---
