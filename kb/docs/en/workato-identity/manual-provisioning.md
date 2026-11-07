---
url: 'https://docs.workato.com/en/workato-identity/manual-provisioning.md'
description: >-
  Configure manual provisioning to add users to Workato Identity environments
  and groups manually.
---

# Manual provisioning

You manually configure user provisioning. This option doesn't enable you to sync users or groups from your IdP. You must define the user's environment access and user group membership when you manually add a user.

Complete the following steps to configure manual provisioning:

1. Sign in to your Workato account and go to **Workspace admin**.
   
2. Click **Authentication & Groups** in the sidebar.
   
3. Select the environment you plan to configure. The environment **End-user group** page displays by default.
   
   > **ENVIRONMENT AVAILABILITY**
   > 
   > Workspaces without [Environments](/en/features/environments) provisioned only have one environment available.
   
4. Select the **Authentication** tab.
   
5. Ensure that the **SAML-based SSO authentication** toggle is enabled.
   
   ![SAML toggle](/assets/saml-toggle.DpLwU7zn.png)_Ensure the **SAML-based SSO authentication** toggle is enabled_
   
6. Go to the **Select an identity provider (IdP)** section and click **\+ Set up new provider**.
   
7. Provide a name for your IdP in the **Identity provider (IdP) name** field. For example: `Okta Dev`.
   
8. Go to the **Enforce SAML authentication for** section and select **All domains** or **Selected domains**.
   
9. Click **Next**.
   
10. Copy the **Specify Single sign-on URL** and **Service provider (SP) entity ID** values and paste each value into your IdP to enable access to Workato-powered apps and services.
    
    ![Copy the Specify Single sign-on URL and Service provider (SP) entity ID values](/assets/create-a-saml-application-in-your-idp.Ghew-MOc.png)_Copy the **Specify Single sign-on URL** and **Service provider (SP) entity ID** values_
    
11. Locate the **Do you have your identity provider metadata URL?** field and select **Yes** or **No** depending on whether you have access to your IdP metadata URL.
    
    **Yes: you have your IdP metadata URL**
    
    1. Provide your metadata URL in the **Metadata URL** field.
       
       ![Yes: you have your IdP metadata URL](/assets/yes-metadata-url.CWtgUFb_.png)_Provide your metadata URL_
       
    
    **No: you don't have your IdP metadata URL**
    
    1. Provide your IdP SSO URL in the **Identity provider single sign-on URL** field.
       
       ![No: you don't have your IdP metadata URL](/assets/no-metadata-url.DBQU-Va3.png)_Provide your IdP information_
       
    2. Provide the unique identifier of your IdP in the **Identity provider issuer** field.
       
    3. Provide the IdP X.509 certificate your IdP uses for request validations in the **X.509 certificate** field.
       
    
12. Click **Set up**. You are redirected to the **Authentication** tab where your configured IdP displays.
    
13. Go to the IdP you configured in the preceding steps and click **Set up**.
    
    ![Click Set up.](/assets/idp-setup-button.Dp_C80br.png)_Click **Set up**._
    
14. Click **Manual provisioning** in the **Provisioning** modal.
    
    ![Select Manual provisioning](/assets/manual-provisioning.BHvq3cm_.png)_Select **Manual provisioning**._
    
15. Click **Save**.
    
16. Refer to [Add an end user manually](/en/workato-identity/add-end-user-manually#add-an-end-user-manually) for next steps.

---
