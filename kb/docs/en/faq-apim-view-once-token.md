---
url: 'https://docs.workato.com/en/faq-apim-view-once-token.md'
description: >-
  Answers to common questions about view-once tokens in the Workato API
  platform, how they protect secrets, and what to do if a token is misplaced.
---

# Update: View-once tokens in the API Platform

## What is the update?

On **Jan 11th, 2023**, Workato is releasing view-once tokens to improve the security of secrets in the API platform. When users create access profiles with Auth token and OAuth 2.0 type, Workato only displays the token and client secret once. Users cannot return to the page to retrieve old tokens and client secrets.

## Who is affected?

This update does not change the state of existing tokens and secrets. It also does not affect your APIs and clients. After the update, your APIs continue to behave exactly the same.

## What do I need to do to prepare for this change?

You do not need to take any action in anticipation of this change. Tokens/secrets in use should be in your clients' possession and inaccessible to other parties. To back up your existing tokens, navigate to the API clients page and copy them. We encourage you to store your tokens/secrets in a secure place, such as a password manager or secret store.

## What happens if my clients misplace their old tokens and want a copy of them? How can I retrieve them?

In the event of a misplaced token/secret, we highly recommend that you invalidate the token/secret immediately to prevent unwanted access to your APIs. To generate a new token, refresh the access profile. Workato displays the new token/secret once so you can copy it to secure storage. It does not display the token/secret again to keep it safe.

## After this change, will I be able to identify my tokens?

Workato will continue to display the token's last four (4) characters. This assists you with identifying tokens/secrets without compromising them.

---
