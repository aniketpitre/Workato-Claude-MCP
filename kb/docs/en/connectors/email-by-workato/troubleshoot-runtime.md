---
url: >-
  https://docs.workato.com/en/connectors/email-by-workato/troubleshoot-runtime.md
description: >-
  Use this guide to troubleshoot errors that occur at runtime when you use the
  Email by Workato connector in Workato.
---

# Troubleshoot Email by Workato runtime errors

Use this guide to troubleshoot errors that occur at runtime when you use the Email by Workato connector in Workato.

## Email delivery delays

Recipients may receive emails sent through Email by Workato with delays up to 24 hours. Workato logs show on-time delivery and message headers confirm the correct send time, but the delay occurs during email infrastructure routing. This error occurs because Email by Workato is not meant for use cases with a high volume of email messages.

Complete the following steps to troubleshoot this issue:

1. Whitelist all required IP addresses on your server and any partner servers. Refer to [IP allowlists](/en/security/ip-allowlists#ip-allowlists) for the complete list of Workato IP addresses.
   
2. Verify that any anti-spam solutions have [mailer@workato.com](mailto:mailer@workato.com) marked as a safe sender.
   
3. Use an external email provider and it's corresponding Workato connector if delays persist. Other email providers may perform better for high-volume email scenarios.
   

## Job is marked as complete but the recipient did not receive the email

This error occurs when a job is marked as complete in the job report, but the recipient did not receive the email sent in the recipe workflow.

Complete the following troubleshooting steps to resolve this error:

1. Check your spam folders to ensure that the email wasn't sent there.
   
2. Send a test email to the recipient's email address to ensure that the email address is valid.
   
3. [Contact Workato support](https://support.workato.com/en/support/home) to check if the email is blocked by Workato if the preceding steps didn't work.
