---
url: 'https://docs.workato.com/en/workato-identity/identity-provider-user-access.md'
description: >-
  Configure Okta as a SAML identity provider for Workato Identity, including
  attribute statements and user assignments.
---

# Okta SAML configuration

This guide describes how to configure Okta as a SAML identity provider (IdP) for Workato Identity.

SAML enables secure authentication between an IdP, such as Okta, and a service provider like Workato. Users authenticate once through Okta and gain access to Workato with a single login instead of managing separate credentials for each application.

> **PREREQUISITES**
> 
> - Workato Identity is available for [Agent Studio](/en/agentic/agent-studio), [Workato GO](/en/agentic/workato-go), [MCP](/en/mcp), and the [API developer portal](/en/api-mgmt/api-developer-portal).
>   
> - [Configure SAML-based authentication](/en/workato-identity/saml-sso#configure-saml-based-authentication) in Workato Identity before you begin. The **Specify Single sign-on URL** and **Service provider (SP) entity ID** values from that setup are required to complete the following steps.
>   

## Configure SAML authentication in Okta

Complete the following steps to configure SAML authentication in Okta:

> **NOT FOR WORKFLOW APPS SAML-BASED SSO**
> 
> This documentation is specific to Workato Identity. Refer to [SAML-based single sign-on authentication](/en/workflow-apps/saml) to configure SAML authentication for [Workflow apps](/en/workflow-apps).

1. Sign in to your [Okta](https://login.okta.com/) account.
   
2. Go to **Applications > Applications** and click **Create App Integration**.
   
   ![Add application in Okta](/assets/okta-saml-config-new-app-integration.CvmRcMJy.png)_Add application in Okta_
   
   Refer to the [Okta documentation](http://developer.okta.com/standards/SAML/setting_up_a_saml_application_in_okta) for more information.
   
3. Select **SAML 2.0** as the **Sign-in method** and click **Next**.
   
   ![Create a new application in Okta](/assets/okta-saml-config-create-app.CQarAWjI.png)_Create a new application in Okta_
   
4. Enter a name for the app in the **App name** field. For example, `Workato Agentic` or `MCP Servers`.
   
5. Click **Next**.
   
6. Paste your Workato **Specify Single sign-on URL** into the corresponding field in Okta.
   
7. Select the **Use this for Recipient URL and Destination URL** checkbox.
   
8. Paste the **Service provider (SP) entity ID** into the **Audience URI (SP Entity ID)** field.
   
9. Set **Name ID format** to `EmailAddress`.
   
10. Go to the **Attribute Statements** section and add the following attributes:
    
    | Name | Value |
    | --- | --- |
    | `workato_end_user_name` | `user.displayName` |
    | `workato_end_user_groups` | `appuser.workato_end_user_groups` |
    
11. Click **Next**.
    
12. Use the **App type** drop-down menu to choose `This is an internal app that we have created`.
    
13. Click **Finish**.
    
14. Go to **Directory > People** and add one or more users. You must complete the verification steps for each user.
    
15. Go to **Applications > My App > Assignments**.
    
16. Click **Assign > Assign to People** and add one or more users for **My App**.
    
17. Click **Done**.
    
18. Go to **Applications > \[Your App\] > Sign On** in Okta.
    
19. Copy the **Metadata URL**. You must use this URL in the **Do you have your identity provider metadata URL?** section of the **Set up a new provider** wizard in Workato Identity.
    
20. Click **Save changes**.
    
21. Set your Okta app visibility to hide the application icon from users. This prevents users from attempting IdP-initiated login which isn't supported for Workato features.
    
    > **DIRECT SIGN-IN FROM IDP UNSUPPORTED**
    > 
    > You can't sign in to Workato directly from your IdP. Authentication is only supported when initiated through a conversation in your connected LLM.
    

## Troubleshooting

Use this section to troubleshoot Okta errors you may encounter.

### Multiple Okta groups issue

Okta's default behavior concatenates the group names as a comma-separated string in the SAML group attribute when a user is a member of multiple Okta groups. Workato Identity expects the group attribute to be an array of individual group values rather than a concatenated string. The concatenated string format causes group mapping to fail, and users don't receive the correct Workato user group assignments.

**Solution**

You must have the `SAML_SUPPORT_ARRAY_ATTRIBUTES` flag enabled in your account to ensure that `string array` types are returned as multiple values. Contact Okta support to enable the `SAML_SUPPORT_ARRAY_ATTRIBUTES` flag if it's not already present in your account.

---
