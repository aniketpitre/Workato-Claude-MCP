# Community recipe examples

Public Workato community-library recipes harvested as JSON pattern examples by
`kb/community/harvest.py`. Search steps: `grep -rl '"slack.post_message' kb/community/recipes`.

| Recipe | Trigger | Steps | Copies | File |
| --- | --- | --- | ---: | --- |
| Post Slack notifications when new leads are created in Salesforce | salesforce | salesforce.new_custom_object, slack.post_message_to_channel | 1061 | `kb/community/recipes/salesforce/671384-post-slack-notifications-when-new-leads-are-created-in-salesforce.json` |
| Post Slack message when new rows are added in Google Sheets | google_sheets | google_sheets.new_spreadsheet_row_v4, slack.post_message_to_channel | 757 | `kb/community/recipes/google_sheets/803804-post-slack-message-when-new-rows-are-added-in-google-sheets.json` |
| Notify Slack channel for High or Highest priority Jira tickets | jira | jira.new_issue, slack.post_message_to_channel | 242 | `kb/community/recipes/jira/576971-notify-slack-channel-for-high-or-highest-priority-jira-tickets.json` |
| New email in Gmail will conditionally post message to channel in Slack | gmail | gmail.new_email, slack.post_message_to_channel | 175 | `kb/community/recipes/gmail/96211-new-email-in-gmail-will-conditionally-post-message-to-channel-in-slack.json` |
| New/Updated Jira Issue will create/update ServiceNow Incident with attachments (Real - Time) | jira | jira.updated_issue_webhook, service_now.search_objects, email.send_mail, service_now.update_object, slack.post_message_to_channel, service_now.create_object, ji | 163 | `kb/community/recipes/jira/555682-new-updated-jira-issue-will-create-update-servicenow-incident-with-att.json` |
| New comment in Wrike with @mentioned user will send Slack message to the user | wrike | wrike.new_comment_v2, wrike.__adhoc_http_action, logger.log_message, workato_list.create_list, workato_list.accumulate_list_items, wrike.list_users, lookup_tabl | 125 | `kb/community/recipes/wrike/845812-new-comment-in-wrike-with-mentioned-user-will-send-slack-message-to-th.json` |
| New signed document in Docusign posts notification in Slack channel | docusign | docusign.new_event, slack.post_message_to_channel | 74 | `kb/community/recipes/docusign/551067-new-signed-document-in-docusign-posts-notification-in-slack-channel.json` |
| Zendesk new/update Ticket notification | zendesk | zendesk.updated_ticket_webhook, slack.post_message_to_channel | 58 | `kb/community/recipes/zendesk/576969-zendesk-new-update-ticket-notification.json` |
| New comments in Wrike will post message to Slack via Slack | wrike | wrike.new_comment_v2, slack.post_message_to_channel | 36 | `kb/community/recipes/wrike/835999-new-comments-in-wrike-will-post-message-to-slack-via-slack.json` |
| Stripe new Charge notification | stripe | stripe.new_charge, stripe.get_customer_by_id, slack.post_message_to_channel | 21 | `kb/community/recipes/stripe/577036-stripe-new-charge-notification.json` |
| Completed tasks in Wrike will post message to Slack via Slack    | wrike | wrike.new_or_updated_task_v2, slack.post_message_to_channel | 20 | `kb/community/recipes/wrike/835977-completed-tasks-in-wrike-will-post-message-to-slack-via-slack.json` |
| Slack notification for Quickbooks invoices over $5000 | quickbooks | quickbooks.new_invoice, slack.post_message_to_channel | 7 | `kb/community/recipes/quickbooks/576966-slack-notification-for-quickbooks-invoices-over-5000.json` |
