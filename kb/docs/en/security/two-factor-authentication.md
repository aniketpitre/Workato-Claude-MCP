---
url: 'https://docs.workato.com/en/security/two-factor-authentication.md'
description: >-
  Learn how two-factor authentication works in Workato and how to set it up
  using an authenticator app and recovery codes.
---

# Two-factor authentication

Two-factor authentication (2FA) is an industry standard for multi-layered authentication. It requires two separate methods to verify your identity:

- Your ID and password
- A temporary code generated from an authenticator app on your phone

This additional layer of security ensures that no one else can access your Workato account.

> **SUMMARY**
> 
> - Workato uses two-factor authentication (2FA) for enhanced security, requiring an ID/password and a code from an authenticator app.
> - To enable 2FA, navigate to **My profile > Two-factor authentication > Set up two-factor authentication**. Scan the QR code with your authenticator app, then enter the six-digit verification code from the app.
> - You can temporarily or permanently disable 2FA in specific situations. Recovery codes serve as an alternative access method.

## How it works

There are multiple situations in which you may be prompted to authenticate your Workato credentials through an authenticator app, including the following:

- When you sign in to a workspace that requires two-factor authentication with your email and password.
  
- When you switch from a workspace that does not require two-factor authentication to a workspace that does require two-factor authentication.
  
- When sessions are invalidated due to security policy updates, changes in user authentication status, or other critical security events, Workato automatically signs out all active workspace sessions. This action mitigates the risk of unauthorized access. This proactive measure ensures prompt termination of any session after its associated credentials or security status has been compromised or modified. During session invalidation, Workato also implements an automatic backend refresh. This process ensures that all changes to user authentication status or security settings are promptly reflected across the system, including within active sessions. The automatic backend refresh enforces necessary re-authentication or access right adjustments immediately, without requiring users to restart their sessions or re-login manually.
  

![Workato requesting two-factor authentication](/assets/6-digit-code.i1QvwTr-.png)_Workato requesting two-factor authentication_

Your authenticator app generates a unique, temporary six-digit code each time you sign in to your Workato account. This code verifies your identity and expires after use.

### Workspace configuration for two-factor authentication

Additional configuration is required to enable two-factor authentication for a workspace and its collaborators.

- A workspace owner must enable two-factor authentication on their personal profile before enabling it within a workspace.
  
- All collaborators within a workspace with two-factor authentication (2FA) enabled must enable 2FA in their personal profile to access the workspace.
  
  Collaborators invited to a workspace with 2FA enabled must enable it in their personal profiles before joining the workspace.
  
  - Collaborators who are part of an existing workspace that later enables 2FA must enable 2FA in their personal profiles to maintain workspace access.

## Choose an authenticator app

Workato allows authentication through mobile applications. Common authenticator apps include the following:

- Google Authenticator ([iOS](https://itunes.apple.com/us/app/google-authenticator/id388497605) or [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&))
- Authy ([iOS](https://itunes.apple.com/us/app/authy/id494168017) or [Android](https://play.google.com/store/apps/details?id=com.authy.authy))
- Microsoft Authenticator ([iOS](https://itunes.apple.com/sg/app/microsoft-authenticator/id983156458) or [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator))

## Set up two-factor authentication

Set up two-factor authentication (2FA) in two minutes

**Note**: Two-factor authentication configuration is now located in **My profile**.

[Video](https://www.youtube.com/embed/hxkJhV7qJu4)

### New login flow

To enable two-factor authentication, first ensure you have your authenticator app ready. This example uses Google Authenticator. Complete the following steps to set up two-factor authentication:

1. Sign in to your Workato account.
   
   ![Sign in to Workato](/assets/sign-in.CLo-aXqy.png)_Sign in to Workato_
   
2. Click **Set up two-factor authentication**.
   
   ![Enable two-factor authentication](/assets/enable-2fa.8pUrHzsn.png)_Enable two-factor authentication_
   
3. Enter your password and click **Verify password** if prompted to verify your credentials. Learn why you're asked to [verify your password](/en/security/two-factor-authentication#why-verify-password). ![Verify password](/assets/verify-password-updated.BnX-1U5x.png)_Verify your password_
   
4. Scan the QR code using Google Authenticator or register using the provided code. Click **Next**.
   
   ![2FA setup](/assets/qr-code-scan-1.l8lAOjur.png)_Two-factor authentication setup_
   
5. Navigate to Google Authenticator and copy the six-digit verification code.
   
   The Workato label and profile name confirm that the connection between Google Authenticator and the Workato platform functions correctly.
   
   ![Verification code](/assets/google-authenticator-workato.DFsO2nM-.png)_Google Authenticator unique verification code_
   
6. Enter the verification code into Workato.
   
   ![Confirm app](/assets/6-digit-code.i1QvwTr-.png)_Confirm authenticator app with Workato account_
   
7. Click **Copy** or **Download** to keep a copy of your recovery codes. If you opt to download, the file is named `workato_2fa_recovery_codes`.
   
   ![Recovery codes](/assets/recovery-codes.FjyXWnn9.png)_Recovery codes_
   
   Remember to store your recovery codes in a secure location. Learn more about [recovery codes](#recovery-codes).
   
   This completes the one-time setup of your Workato two-factor authentication.
   
   ![Two-factor authentication enabled](/assets/new-2fa-enabled.AakBJWND.png)_Two-factor authentication enabled_
   

> **NEW LOGIN FLOW FOR WORKATO AUTHENTICATION USERS**
> 
> Starting September 1, 2024, Workato is enhancing its login process for users using Workato authentication (email + password). To improve platform security and encourage the adoption of 2FA, we're introducing a new step in the login flow.
> 
> Upon attempting to sign in, users see an intermediary screen that encourages setting up 2FA. This step makes the configuration of 2FA straightforward and accessible before users gain access to their workspace.
> 
> This update addresses the increasing need for robust security measures. Implementing 2FA enhances account security by adding an additional layer of verification, protecting against unauthorized access and potential account takeover attempts.
> 
> We strongly recommend all users enable 2FA to safeguard their accounts and contribute to a more secure Workato community.

### Enable two-factor authentication

If you didn’t set up two-factor authentication using the new login flow, configure it by going to **Profile settings > Two-factor authentication** and clicking **Setup two-factor authentication**.

1. ![Profile drop-down](/assets/my-profile-2fa.BEtv6Ek-.png)_My profile_
   
2. ![Enable 2FA](/assets/2fa-setup.D6Oa8JRK.png)_Set up Two-factor authentication_
   

Follow the steps from the [New login flow](#new-login-flow) section to complete your 2FA setup.

### Disable two-factor authentication

In certain situations, you may need to disable your two-factor authentication. For example, you may need to disable 2FA if your device is stolen or if you are switching to a new work device.

1. Click **Profile settings**.
   
   ![Profile drop-down](/assets/disable-2fa-steps.AJHKxg9y.png)_My profile_
   
2. Click **Two-factor authentication > Disable two-factor authentication**.
   
   ![Disable two-factor authentication](/assets/disable-2fa.CwZOfJeL.png)_Disable two-factor authentication_
   
   > **TRUSTED DEVICES**
   > 
   > Disabling two-factor authentication removes all trusted devices that signed in with the authenticator app.
   
3. Enter your password and click **Verify password** if prompted to verify your credentials. Learn why you're prompted to [verify your password](/en/security/two-factor-authentication#why-verify-password).
   
   ![Verify password](/assets/verify-password-updated.BnX-1U5x.png)_Verify your password_
   
4. Click **Disable 2FA**.
   
   ![Disable 2FA](/assets/confirm-disable-2fa.pSR3oCrs.png)_Disable two-factor authentication_
   

### Recovery codes

Recovery codes are alphanumeric strings that are uniquely tied to your Workato account. You can use a recovery code to verify your identity instead of the six-digit verification code. Each recovery code can be used **only once**.

![Using recovery code](/assets/recovery-screen.-3DsiyGN.png)_Use a recovery code_

A list of twelve recovery codes auto-generates during the two-factor authentication setup. Store your recovery codes in a secure location, preferably separate from your authenticator app, such as on a device other than your phone. If you download your recovery codes, the file is named `workato_2fa_recovery_codes`.

#### Lost authentication device

If you delete, change, or lose your app or device, you can still access your Workato account using a recovery code for two-factor authentication.

When you sign in with a recovery code, reset your two-factor authentication settings. This step prevents unauthorized access to your account through a stolen device and reconfigures two-factor authentication for your new device. Complete the following steps to reconfigure two-factor authentication for your new device:

- [Disable two-factor authentication](/en/security/two-factor-authentication#disable-two-factor-authentication).
- [Set up two-factor authentication](/en/security/two-factor-authentication#setup-two-factor-authentication) with your new device.

#### Lost recovery codes

If you forgot to store your recovery codes or accidentally deleted them, you can retrieve them from your two-factor authentication setup.

Complete the following steps to view your recovery codes:

1. Click **My profile**.
   
2. Click **Two-factor authentication > View recovery codes**.
   
   ![View recovery codes](/assets/view-recovery-codes.BfElF9xz.png)_View recovery codes_
   
   We recommend storing your recovery codes in a secure and accessible location.
   

#### Generate new recovery codes

If you misplace your recovery codes, you can generate a new set. Note that others can use the recovery codes to access your Workato account.

You can also generate new recovery codes if they are depleting. Using the single-use recovery codes for two-factor authentication reduces the total number of available codes. Generating a new set of recovery codes ensures you don't get locked out of your Workato account.

1. Click **My profile**.
   
2. Click **Two-factor authentication > View recovery codes > Regenerate codes**.
   
   ![Generate new recovery codes](/assets/regenerate-recovery-codes.EnFkt6Lg.png)_Generate new recovery codes_
   

### Trusted devices

You can temporarily turn off two-factor authentication for trusted devices, such as a secured work laptop. This allows the device to sign in without two-factor authentication for 7 days.

Click **Trust this device** during the [Set up two-factor authentication](/en/security/two-factor-authentication#setup-two-factor-authentication) process.

![Trust this device for 7 days](/assets/trust-this-device.jmOuoDuD.png)_Trust this device for 7 days_

Your trusted devices appear on the two-factor authentication settings page, where you can revoke access to unrecognized devices or those no longer in use.

![Trusted devices](/assets/trusted-devices-updated.CJf6XP5u.png)_Trusted devices_

### Why am I being asked to verify my password?

When you change your account security settings, Workato requires your password for an extra layer of authentication. This applies when making changes to your two-factor authentication configuration, including enabling two-factor authentication and viewing recovery codes.

After you verify your password, Workato won't ask you to verify it again for fifteen minutes.

![Verify password](/assets/verify-password-updated.BnX-1U5x.png)_Verify password_

> **NEED A PASSWORD?**
> 
> If you signed up for Workato using SSO, or if your workspace is switching authentication methods from SAML SSO to 2FA and you don't have a password to verify your Workato account, you must reset your password using your email by clicking the **Forgot password** link on the sign-in page.

---
