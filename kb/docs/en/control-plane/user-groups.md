---
url: 'https://docs.workato.com/en/control-plane/user-groups.md'
description: >-
  Create and manage end-user groups in Control plane, assign environment access,
  and scope user access more securely.
---

# End-user group management

Control plane enables you to create and manage end-user groups. You can store end-users and end-user groups with customized environment access and assign access to specific groups. This lets you scope user access more securely.

End-user groups are created within specific environments. You must [add end-users](/en/control-plane/add-end-users) before you can assign them to a user group. Each end-user group must have at least one end user assigned to it.

## Create an end-user group

End-user groups are specific to each environment. You must select the environment before you can create a group.

Complete the following steps to create an end-user group in an environment:

1. Sign in to Workato.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**. Control plane opens in a new tab by default.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **End user access > Authentication & groups**.
   
6. Select the environment where you plan to add the user group.
   
7. Click **\+ Create end-user group**.
   
   ![Click Create end-user group](/assets/end-user-group.BeU3jlRM.png)_Click **\+ Create end-user group**_
   
8. Provide a name for the group in the **Name** field.
   
9. Click **Create**.
   

## User group authentication

End users sign in with their email address and password by default. You can define how end users authenticate across all linked workspaces in Control plane by environment by configuring SAML identity providers for end user groups. Identity providers are shared with linked workspaces. Workspace admins can choose whether to use the IdP.

Complete the following steps to define user group authentication settings for a Control plane environment:

1. Go to **End user access > SAML identity providers**.
   
2. Click **\+ Set up new provider**.
   
3. Go to the **Enforce SAML authentication for** section and select either **All domains** or **Selected domains**. You must enter multiple domains separated by commas in the **Specify domains** field if you choose **Selected domains**.
   
4. Go to the **SP Entity ID** field and click **Copy**. You must add this value to your IdP to configure SAML SSO.
   
5. Go to the **ACS (Reply) URL** field and click **Copy**. You must add this value to your IdP to configure SAML SSO.
   
6. Go to the **Do you have your identity provider metadata URL?** section and select the option that applies to you.
   
   **Yes: You have your identity provider metadata URL**
   
   1. Select **Yes**.
      
   2. Paste your metadata URL into the **Metadata URL** field. Workato uses this URL to automatically import your SAML configuration.
      
      You can find this URL in your IdP's SAML setup:
      
      - **Okta**: Go to your app's **Sign On** tab and scroll to **Metadata URL**. It typically follows this format: `https://{your-okta-domain}/app/{app-name}/{app-id}/sso/saml/metadata`
      - **Microsoft Entra ID**: Go to your app's **Single sign-on** settings and scroll to **SAML Certificates**. The URL is labeled **App Federation Metadata URL** and typically follows this format: `https://login.microsoftonline.com/{tenant-id}/federationmetadata/2007-06/federationmetadata.xml?appid={app-id}`
      - **Google Workspace**: Go to your app's **SSO Configuration** and scroll to **IDP metadata**. Click **Download metadata** to get the XML file, or use the URL directly if your Google admin has published it.
   
   **No: You don't have your identity provider metadata URL**
   
   1. Select **No**.
      
   2. Paste your IdP SSO URL into the **Identity provider single sign-on URL** field.
      
   3. Provide your IdP unique identifier in the **Identity provider issuer** field. This is the Entity ID your IdP uses to identify itself and must match exactly what your IdP is configured to send in SAML assertions.
      
      You can find this value in your IdP's SAML setup instructions:
      
      - **Okta**: Go to your app's **Sign On** tab and click **View SAML setup instructions**. The value is listed as **Identity Provider Issuer** and typically uses the following format: `http://www.okta.com/examplekey123`
      - **Microsoft Entra ID (Azure AD)**: Go to your app's **Single sign-on** settings. The value is listed as **Microsoft Entra Identifier** and typically uses the following format: `https://sts.windows.net/{tenant-id}/`
      - **Google Workspace**: Go to **Apps > Web and mobile apps**, select your app, and open **SSO Configuration**. The value is listed as **Entity ID** and typically uses the following format: `https://accounts.google.com/o/saml2?idpid={idp-id}`
   4. Paste your IdP X509 certificate, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines in the **X.509 certificate** field. This is the public certificate Workato uses to validate that SAML responses genuinely came from your IdP.
      
      You can find your X509 certificate in your IdP app:
      
      - **Google Workspace**: Go to **Apps > Web and mobile apps**, select your app, and open **SSO Configuration**. Go to the **SSO certificate** section and click **Download certificate**. Open the downloaded `.pem` file in your text editor to copy the certificate.
      - **Microsoft Entra ID**: Go to your Microsoft Entra ID app's **Single sign-on** section. Go to the **SAML Certificates** section and download the **Certificate (Base64)** file. Open the downloaded `.cer` or `.pem` file in your text editor to copy the certificate.
      - **Okta**: Go to your Okta app's **Sign On** tab and scroll to **SAML Signing Certificates**. Click **Actions** next to the active certificate and click **Download certificate**. Open the downloaded `.cer` or `.pem` file in your text editor to copy the certificate.
      - **OneLogin**: Go to the **SSO** section and click **More Actions**. Right-click **SAML Metadata** and select **Copy link address**.
   
7. Click **Setup**.

---
