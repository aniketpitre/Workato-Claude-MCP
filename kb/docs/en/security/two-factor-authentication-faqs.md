---
url: 'https://docs.workato.com/en/security/two-factor-authentication-faqs.md'
description: >-
  Answers to common questions about two-factor authentication in Workato,
  including authenticator apps and recovery codes.
---

# Two-factor authentication FAQs

Get answers to frequently asked questions (FAQs) about two-factor authentication (2FA).

What is 2FA?

[2FA](/en/security/two-factor-authentication#two-factor-authentication) is a security measure that requires two separate methods of verifying your identity when signing into your Workato account. It combines something you know (ID and password) with something you have (an authenticator app on your phone) to enhance security.

Which authenticator apps are compatible with Workato?

Workato supports [authentication through popular mobile apps](/en/security/two-factor-authentication#choose-an-authenticator-app) on both iOS and Android devices, including:

- Google Authenticator
- Authy
- Microsoft Authenticator

How do I get a new recovery code?

[Recovery codes](/en/security/two-factor-authentication#recovery-codes) are alphanumeric strings unique to your Workato account. They can be used to verify your identity in place of the 6-digit verification code. Each recovery code can be used only once. Store them securely.

To generate a new recovery code:

1. Sign in to Workato and select **My profile**.
   
2. Select **Two-factor authentication > View recovery codes > Regenerate recovery codes**.
   

What should I do if I've lost my authentication device (phone or laptop) or changed devices?

If you've [lost your authentication device](/en/security/two-factor-authentication#lost-authentication-device), you can still access your Workato account by using a recovery code. However, resetting your 2FA settings after signing in is recommended to prevent unauthorized access through the lost device.

What should I do if I've lost my recovery codes?

If you've [lost your recovery codes](/en/security/two-factor-authentication#lost-recovery-codes), you can retrieve them from your 2FA setup in **My profile > Two-factor authentication**. Make sure to store them securely in a separate location from your authenticator app.

Can I temporarily disable Two-Factor Authentication for trusted devices?

Yes, you can temporarily disable 2FA for [trusted devices](/en/security/two-factor-authentication#trusted-devices), such as a secured work laptop. Disabled devices are allowed to sign in without 2FA for 30 days if you select **Trust this device for 30 days** during the 2FA setup.

What should I do if I signed up for Workato using Single Sign-On (SSO) and don't have a password?

If you signed up with SSO or your workspace is transitioning from SAML SSO to 2FA and you don't have a [password](/en/security/two-factor-authentication#why-verify-password), complete the following steps:

1. Navigate to the Workato login page and click the **Forgot password** link.
   
2. Complete the prompts to reset your password through your email.

---
