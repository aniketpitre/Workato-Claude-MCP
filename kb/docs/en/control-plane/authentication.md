---
url: 'https://docs.workato.com/en/control-plane/authentication.md'
description: >-
  Use Control plane to manage a single identity for authentication across
  multiple workspaces.
---

# Authentication

Control plane allows you to manage a single identity for authentication across multiple workspaces.

Collaborators sign in with their email address and password by default. You can enable SAML-based SSO to require collaborators to authenticate through your identity provider (IdP) for all domains or selected domains.

## Set up a SAML-SSO provider

Complete the following steps to set up a SAML-SSO provider:

> **NOT FOR WORKFLOW APPS SAML-BASED SSO**
> 
> This documentation is specific to Control plane. Refer to [SAML-based single sign-on authentication](/en/workflow-apps/saml) to configure SAML authentication for [Workflow apps](/en/workflow-apps).

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Control plane settings > Authentication**.
   
6. Enable the **SAML-based SSO authentication** toggle.
   
7. Click **\+ Set up identity provider**.
   
   ![Click + Set up identity provider](/assets/setup-identity-provider.DWZkbpZh.png)_Click **\+ Set up identity provider**_
   
8. Go to the **Enforce SAML authentication for** section and select either **All domains** or **Selected domains**. You must enter multiple domains separated by commas in the **Specify domains** field if you choose **Selected domains**.
   
9. Go to the **SP Entity ID** field and click **Copy**. You must add this value to your IdP to configure SAML SSO.
   
10. Go to the **ACS (Reply) URL** field and click **Copy**. You must add this value to your IdP to configure SAML SSO.
    
11. Go to the **Do you have your identity provider metadata URL?** section and select the option that applies to you.
    
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
    
12. Click **Setup**.

---
