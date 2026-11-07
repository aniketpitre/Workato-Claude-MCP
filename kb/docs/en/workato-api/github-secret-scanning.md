---
url: 'https://docs.workato.com/en/workato-api/github-secret-scanning.md'
description: >-
  Learn how Workato integrates Developer API tokens with GitHub secret scanning
  to revoke leaked tokens and notify workspace admins.
---

# GitHub secret scanning

Starting from mid-May 2023, Workato Developer API client tokens are now integrated with [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns), allowing us to provide additional layers of security when your API tokens are found in plain text on public GitHub repositories.

When these tokens are found, Workato will perform the following steps:

1. Revoke your Developer API token to ensure no bad actors can have unauthorized access to your Workato workspace
2. Send an email to the workspace admins about the leaked token, including information about where it was found and how to recover from the leaked token

![Leaked token email](/assets/leaked-token-email.BgO9weE6.png)_Leaked token email_

> **TIP**
> 
> Remember to add your Workspace admins to your email notification lists to ensure that relevant individuals are informed if tokens are leaked. This can be done by going to your [Workspace settings](https://app.workato.com/users/current/edit/email_notifications) when logged in as the workspace admin.

3. Mark the API Client as leaked on the Workato UI
4. Add an audit log event indicating that the API token was leaked

![Audit event](/assets/leaked-token-audit-event.L1_N9Ur_.png)_Leaked token audit event_

## Why do we revoke tokens immediately?

Human error is one of the most common ways that malicious actors can access your account. We have found that many bad actors use crawlers on GitHub public repositories to find leaked tokens which makes it important that we are able to secure your Workato workspace.

This process is also aligned with many best practices proposed by tools like [GitLab](https://about.gitlab.com/blog/2023/01/04/pat-revocation-coming-soon/), [Okta](https://developer.okta.com/blog/2018/06/20/what-happens-if-your-jwt-is-stolen) and more!

---
