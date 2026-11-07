---
url: 'https://docs.workato.com/en/recipes/error-notifications.md'
description: >-
  Learn how Workato error notification emails work, including when alerts are
  sent, what triggers them, and how to manage recipients and alert scope.
---

# Error notification emails

Set up error notifications in 2 minutes

[Video](https://www.youtube.com/embed/DiyrIpcYnY8)

Workato sends email alerts to help you track recipe failures and critical issues. This section covers when notifications are sent, what triggers them, and how to manage recipients and alert scope.

## Notification policy

Workato sends error notification emails to the workspace owner by default. Notifications are sent in the following cases:

- A recipe encounters a new type of error for the first time.
- A recipe encounters 3 consecutive trigger errors.
- A recipe is stopped by Workato after 60 consecutive trigger errors. Refer to [Trigger errors and notifications](/en/recipes/error-notifications#trigger-errors-and-notifications) for more information.

Workato throttles repeat notifications to reduce noise. By default, it applies a one-minute throttle per error type per recipe. You can also enable a one-hour throttle to further quota alert frequency.

![Error notification email](/assets/error-notification-email.sUFZaskN.png)_Error notification email example_

### Customize notification recipients

Workato sends error emails to the workspace owner by default. Complete the following steps to customize recipients and send alerts to other users:

1. Go to **Workspace admin > Settings > Error alerts**.
   
2. Enter the email addresses that should receive error notifications in the **Recipients** field. Separate multiple addresses with commas.
   
   ![Configure error alert recipients and throttling settings](/assets/error-notification-config.DANDDXFB.png)_Configure error alert recipients and throttling settings_
   
3. Optional. Enable the **Receive error alerts only from specific projects** toggle to [filter notifications by project](#filter-error-alerts-by-project).
   
4. Optional. Enable the **Quota error alerts to one per hour for each recipe** toggle to reduce email frequency.
   
5. Click **Save** to apply your settings.
   

### Filter error alerts by project

By default, Workato sends error alerts for all recipes across all projects.

To filter notifications:

1. Enable the **Receive error alerts only from specific projects** toggle.
   
   ![Select the projects you plan to send error alerts](/assets/error-notifications-for-select-projects-all.p6MoMO5l.png)_Select the projects you plan to send error alerts_
   
2. Choose the relevant projects in the **Choose projects** field.
   

This reduces alert volume and quotas notifications to selected projects.

## Trigger errors and notifications

Trigger errors occur when a recipe fails to fetch trigger events. Workato continues polling unless the issue persists. Workato sends notifications at specific thresholds, not for every trigger error:

- **After 3 consecutive trigger errors**: Workato sends an error notification email to configured recipients.
- **After 60 consecutive trigger errors**: Workato stops the recipe and sends a separate notification informing configured recipients that the recipe has been stopped.

Common causes include invalid connections, expired credentials, and timeouts from temporary app downtime.

## Action errors and notifications

Action errors occur when a recipe step fails during execution. These errors create job-level failures and may trigger email notifications based on your alert settings.

Common causes include missing or invalid input values, unexpected data formats, or downstream app errors or timeouts. Use the **Input** and **Output** tabs in the job report to troubleshoot and resolve these errors.

---
