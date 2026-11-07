---
url: 'https://docs.workato.com/en/connectors/greenhouse.md'
description: >-
  Use the Greenhouse connector to automate workflow for applicant tracking and
  recruiting.
---

# Greenhouse

[Greenhouse](https://www.greenhouse.io/) is an applicant tracking system and recruiting software that's designed to help companies build better hiring processes and hire for what's next.

The Greenhouse connector enables you to build even more automation around applicant and candidate workflow, and connect with other human resource management systems.

## Use cases

Connect Greenhouse with your HR and IT systems to automate hiring and onboarding. You can integrate the Greenhouse connector with other apps to sync candidate data, automate onboarding, and improve efficiency across your HR and IT workflows. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can use the Greenhouse connector to create powerful multi-app workflows:

- [Sync Greenhouse offer letters](/en/getting-started/use-cases/greenhouse-box-servicenow-workbot) to Box and create onboarding requests in ServiceNow.
- [Sync Greenhouse new hires](/en/getting-started/use-cases/greenhouse-sap-successfactors-odata) to SAP SuccessFactors.

Watch a quick video

[Video](https://www.youtube.com/embed/39yAfAr8zYw?rel=0&rel=0)

## API version

The Greenhouse connector uses both legacy (v1/v2) and v3 APIs:

- API key authentication uses v1/v2 APIs
- OAuth 2.0 authorization code grant authentication uses v3 APIs

> **MIGRATION REQUIRED**
> 
> If your connections use API key authentication (v1/v2), migrate to OAuth 2.0 authorization code grant authentication and replace all v1/v2 triggers and actions with their v3 equivalents before August 30, 2026. Greenhouse will remove support for the v1 and v2 APIs on this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) and the [Greenhouse v3 object coverage guide](/en/connectors/greenhouse/object-coverage) for more information.

Existing connections that use API key authentication continue to run until August 30, 2026.

## Connection setup

The Greenhouse connector supports the following authentication types:

- [OAuth 2.0 authorization code (v3)](#oauth-2-0-authorization-code-v3)
- [API key (v1/v2)](#api-key-v1-v2)

Connections that use API key authentication support only v1/v2 actions; connections that use OAuth 2.0 support only v3 actions.

New Greenhouse connections support OAuth 2.0 authorization code grant authentication only. API key authentication is available for existing connections only.

If you use API key authentication, refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your existing connections and recipes.

### OAuth 2.0 authorization code grant authentication (v3)

Use OAuth 2.0 authorization code grant authentication to connect to Greenhouse with v3 APIs. This is the default authentication method for all new connections.

#### Minimum and default scopes

Harvest OAuth scopes define the level of access Workato has to your Greenhouse instance.

View minimum scopes

The following scope is included when you select specific scopes:

- `harvest:users:list`

View default scopes

All scopes in this list are requested if you leave the **Harvest OAuth scopes** field blank:

- `harvest:ai_opt_out_statuses:list`
- `harvest:application_stages:list`
- `harvest:applications:convert_to_candidate`
- `harvest:applications:create`
- `harvest:applications:destroy`
- `harvest:applications:hire`
- `harvest:applications:list`
- `harvest:applications:move`
- `harvest:applications:reject`
- `harvest:applications:unreject`
- `harvest:applications:update`
- `harvest:applied_candidate_tags:create`
- `harvest:applied_candidate_tags:destroy`
- `harvest:applied_candidate_tags:list`
- `harvest:approval_flows:create`
- `harvest:approval_flows:list`
- `harvest:approval_flows:replace_approver_groups`
- `harvest:approval_flows:request_approvals`
- `harvest:approval_flows:update`
- `harvest:approver_groups:list`
- `harvest:approver_groups:replace_approver`
- `harvest:approvers:list`
- `harvest:attachments:create`
- `harvest:attachments:destroy`
- `harvest:attachments:list`
- `harvest:bulk_requests:list`
- `harvest:candidate_attribute_types:list`
- `harvest:candidate_educations:create`
- `harvest:candidate_educations:destroy`
- `harvest:candidate_educations:list`
- `harvest:candidate_employments:create`
- `harvest:candidate_employments:destroy`
- `harvest:candidate_employments:list`
- `harvest:candidate_tags:create`
- `harvest:candidate_tags:destroy`
- `harvest:candidate_tags:list`
- `harvest:candidates:anonymize`
- `harvest:candidates:create`
- `harvest:candidates:destroy`
- `harvest:candidates:list`
- `harvest:candidates:merge`
- `harvest:candidates:update`
- `harvest:close_reasons:list`
- `harvest:custom_field_departments:create`
- `harvest:custom_field_departments:destroy`
- `harvest:custom_field_departments:list`
- `harvest:custom_field_offices:create`
- `harvest:custom_field_offices:destroy`
- `harvest:custom_field_offices:list`
- `harvest:custom_field_options:create`
- `harvest:custom_field_options:destroy`
- `harvest:custom_field_options:list`
- `harvest:custom_field_options:update`
- `harvest:custom_fields:create`
- `harvest:custom_fields:destroy`
- `harvest:custom_fields:list`
- `harvest:custom_fields:update`
- `harvest:default_interviewers:list`
- `harvest:demographic_answer_options:list`
- `harvest:demographic_answers:list`
- `harvest:demographic_question_sets:list`
- `harvest:demographic_questions:list`
- `harvest:departments:create`
- `harvest:departments:list`
- `harvest:departments:update`
- `harvest:eeoc:list`
- `harvest:email_templates:list`
- `harvest:focus_candidate_attributes:list`
- `harvest:future_job_permissions:create`
- `harvest:future_job_permissions:destroy`
- `harvest:future_job_permissions:list`
- `harvest:interview_kits:list`
- `harvest:interview_media:list`
- `harvest:interviewer_tags:list`
- `harvest:interviewers:list`
- `harvest:interviews:create`
- `harvest:interviews:destroy`
- `harvest:interviews:list`
- `harvest:interviews:update`
- `harvest:job_board_custom_locations:list`
- `harvest:job_boards:list`
- `harvest:job_candidate_attributes:list`
- `harvest:job_hiring_managers:create`
- `harvest:job_hiring_managers:destroy`
- `harvest:job_hiring_managers:list`
- `harvest:job_interview_stages:list`
- `harvest:job_interviews:list`
- `harvest:job_notes:create`
- `harvest:job_notes:destroy`
- `harvest:job_notes:list`
- `harvest:job_notes:update`
- `harvest:job_owners:create`
- `harvest:job_owners:destroy`
- `harvest:job_owners:list`
- `harvest:job_post_locations:create`
- `harvest:job_post_locations:destroy`
- `harvest:job_post_locations:list`
- `harvest:job_post_searchable_locations:list`
- `harvest:job_posts:create`
- `harvest:job_posts:list`
- `harvest:job_posts:update`
- `harvest:jobs:create`
- `harvest:jobs:list`
- `harvest:jobs:update`
- `harvest:notes:create`
- `harvest:notes:list`
- `harvest:offers:create`
- `harvest:offers:list`
- `harvest:offers:update`
- `harvest:offices:create`
- `harvest:offices:list`
- `harvest:offices:update`
- `harvest:openings:create`
- `harvest:openings:destroy`
- `harvest:openings:list`
- `harvest:openings:update`
- `harvest:pay_input_ranges:list`
- `harvest:pay_inputs:list`
- `harvest:prospect_details:list`
- `harvest:prospect_pool_stages:list`
- `harvest:prospect_pools:list`
- `harvest:referrers:list`
- `harvest:rejection_details:list`
- `harvest:rejection_details:update`
- `harvest:rejection_reasons:list`
- `harvest:rejection_reasons:show`
- `harvest:scorecard_candidate_attributes:create`
- `harvest:scorecard_candidate_attributes:list`
- `harvest:scorecard_candidate_attributes:update`
- `harvest:scorecard_question_answer_options:create`
- `harvest:scorecard_question_answer_options:list`
- `harvest:scorecard_question_answers:list`
- `harvest:scorecard_question_candidate_attributes:list`
- `harvest:scorecard_question_options:list`
- `harvest:scorecard_questions:list`
- `harvest:scorecards:create`
- `harvest:scorecards:list`
- `harvest:scorecards:update`
- `harvest:sources:list`
- `harvest:tracking_links:list`
- `harvest:user_emails:create`
- `harvest:user_emails:list`
- `harvest:user_job_permissions:create`
- `harvest:user_job_permissions:destroy`
- `harvest:user_job_permissions:list`
- `harvest:user_roles:list`
- `harvest:users:activate`
- `harvest:users:create`
- `harvest:users:deactivate`
- `harvest:users:list`
- `harvest:users:revoke_permissions`
- `harvest:users:update`
- `harvest:webhooks:create`
- `harvest:webhooks:destroy`
- `harvest:webhooks:list`
- `harvest:webhooks:update`

#### Connect to Greenhouse with OAuth 2.0 authorization code grant authentication

Complete the following steps to set up an OAuth 2.0 authorization code grant authentication connection to Greenhouse in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Greenhouse` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Authentication using OAuth 2.0](/assets/greenhouse-oauth-connection.CC0R86qm.png)_Authentication using OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Select the required **Harvest OAuth scopes**. Refer to [Minimum and default scopes](#oauth-scopes) for more information.
   
6. Optional. Enter a value in the **Custom domain** field. Leave blank to use the default Harvest API host: `https://harvest.greenhouse.io`. If your organization uses a custom subdomain, such as `https://acme.greenhouse.io`, enter `acme.greenhouse.io`.
   
7. Click **Connect**.
   
8. Sign in to your Greenhouse account and authorize access.
   

### API key authentication (v1/v2)

Use API key authentication to manage existing Greenhouse connections that use legacy APIs. API key authentication isn't available for new connections.

> **DEPRECATED AUTHENTICATION**
> 
> Greenhouse will remove support for v1 and v2 APIs on August 30, 2026. Use OAuth 2.0 authorization code grant authentication for new connections.

#### Greenhouse setup for API key authentication

We recommend using an Integration System User (ISU) for integration with Workato. This ensures that permissions are consistent and all operations can be logged on a single account.

#### Create an API token

Complete the following steps to create an API token in Greenhouse:

1. Navigate to **Settings > Dev Center > API Credential Management**.
   
2. Select **Harvest v3 (OAuth)** or **Harvest v1/v2** to create a new API key for Workato.
   
3. Click **Create new API credentials**.
   
4. Use the **API type** drop-down menu to select **Harvest** or **Harvest V3 (OAuth)**.
   
5. Use the **Partners** drop-down menu to select **Workato**.
   
6. Use the **Description** field to enter an API description.
   
7. Click **Manage permissions**.
   
8. Copy and save the **API key** for use in Workato.
   
9. Click **Close**.
   
10. Provide the necessary permissions for this API key. Refer to [Minimum permissions for Harvest API](#api-permissions) for more information.
    
    > **PERMISSIONS**
    > 
    > Ensure that you give this API credential the correct permissions. Incorrect permissions may prevent some Greenhouse connector actions and triggers from working, even if the connection is successful.
    
11. Click **Save**.
    

#### Minimum permissions for Harvest API

The Greenhouse connector requires an API key with access to specific Harvest API objects. These permissions ensure all triggers and actions function correctly. For example, the [reject application](/en/connectors/greenhouse/reject-application-action) action requires the **Applications** permission.

Grant the following permissions when you create the Harvest API key for Workato. These permissions support standard connector operations:

- `Applications`
- `Candidates`
- `Close Reasons`
- `Custom Field Options`
- `Custom Fields`
- `Departments`
- `Education`
- `Job Openings`
- `Job Posts`
- `Jobs`
- `Offers`
- `Offices`
- `Rejection Reasons`
- `Scheduled Interviews`
- `Scorecards`
- `Sources`
- `Tags`
- `Tracking Links`
- `Users`
  - `Get: Retrieve User`
  - `Get: List Users`

You can view and manage the permissions for each API key in the Greenhouse **API credential** page.

If you encounter **403 Forbidden** errors, the API key likely lacks required permissions. Review the API key permissions and ensure all listed objects are selected. Refer to the [Greenhouse Harvest API documentation](https://developers.greenhouse.io/harvest.html) for more information.

#### Connect to Greenhouse using API key authentication (v1/v2)

Complete the following steps to set up an API key authentication connection to Greenhouse in Workato using legacy APIs:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Greenhouse` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the Greenhouse API token in the **API key** field. Refer to [Create an API token](#how-to-create-an-api-token-for-workato) for more information.
   
6. Use the **On-Behalf-Of user** drop-down menu to select the Greenhouse user for the `On-Behalf-Of` header. Options include **User email** and **User ID**.
   
7. Enter the email address or user ID associated with this API token in the **User email / User ID** field.
   
8. Optional. Enter a value in the **Custom domain** field. Leave blank to use the default Harvest API host: `https://harvest.greenhouse.io`. If your organization uses a custom subdomain, such as `https://acme.greenhouse.io`, enter `acme.greenhouse.io`.
   
9. Click **Connect**.

---
