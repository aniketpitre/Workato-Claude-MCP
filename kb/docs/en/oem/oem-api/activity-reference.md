---
url: 'https://docs.workato.com/en/oem/oem-api/activity-reference.md'
description: >-
  Reference for the resource types and event types used to filter results from
  the Workato Embedded activity audit log API.
---

# Embedded API - Activity audit log reference

This page provides a reference for the resource types and event types you can use as query parameters to filter responses from the [Get activity audit log API](/en/oem/oem-api/environment-management#get-audit-log).

- **Resource types** specify which resource categories the API should include in the activity audit log results. For example, use `include_resource_types[]=flow` to retrieve only activities related to recipes.
- **Event types** define the events logged for these resource types, such as creating or deleting a recipe.

The resource types and event types listed in this document are specific to **Embedded customer workspaces**. You can use the following query parameters to include or exclude these types in your results:

- `include_resource_types[]`
- `include_event_types[]`
- `exclude_resource_types[]`
- `exclude_event_types[]`

## Resource types

The following table maps each `resource_type` used in the API to its corresponding display name in the user interface.

| Resource type | Display name |
| --- | --- |
| [`AccountProperty`](#accountproperty) | [Environment properties](/en/features/account-properties) |
| [`Adapter`](#adapter) | [Custom connectors](/en/developing-connectors/sdk#what-is-a-custom-connector) |
| [`ApiAccessProfile`](#apiaccessprofile) | [API access profiles](/en/api-mgmt/api-client-mgmt#access-profile) |
| [`ApiClient`](#apiclient) | [Developer API clients](/en/workato-api/api-clients) |
| [`ApiCustomer`](#apicustomer) | [API clients (API platform)](/en/api-mgmt/api-client-mgmt#api-clients) |
| [`ApiEndpoint`](#apiendpoint) | [API endpoints](/en/api-mgmt/api-endpoints) |
| [`ApiGroup`](#apigroup) | [API collections](/en/api-mgmt/api-collections) |
| [`ApiPolicy`](#apipolicy) | [API access policies](/en/api-mgmt/api-access-policies) |
| [`ApiPrivilegeGroup`](#apiprivilegegroup) | [Developer API client roles](/en/workato-api/api-clients#create-a-client-role) |
| [`AuditLogReplicationSettings`](#auditlogreplicationsettings) | [Audit log streaming](/en/features/activity-audit-log-streaming) |
| [`CommunityAdapterPublication`](#communityadapterpublication) | [Community connectors](/en/developing-connectors/community/community) |
| [`CustomOauthKey`](#customoauthkey) | [Custom OAuth profiles](/en/custom-oauth-profiles) |
| [`Deployment`](#deployment) | [Project deployments](/en/features/environments/deployment) |
| [`ExportManifest`](#exportmanifest) | [Manifests](/en/recipe-development-lifecycle/export#export-manifests) |
| [`Flow`](#flow) | [Recipes](/en/recipes) |
| [`Folder`](#folder) | [Folders](/en/projects#create-a-folder) |
| [`LookupTable`](#lookuptable) | [Lookup tables](/en/features/lookup-tables) |
| [`ManagedUserGrant`](#managedusergrant) | [Workspace collaborators and moderators](/en/user-accounts-and-teams/team-collaboration) |
| [`MemberInvitation`](#memberinvitation) | [Workspace invitations](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators) |
| [`OnPremAgent`](#onpremagent) | [On-prem agents](/en/on-prem/agents) |
| [`Package`](#package) | [Packages](/en/recipe-development-lifecycle#packages) |
| [`PrivilegeGroup`](#privilegegroup) | [Collaborator roles](/en/roles) |
| [`Project`](#project) | [Projects](/en/projects) |
| [`ProjectBuild`](#projectbuild) | [Project builds](/en/workato-api/projects#understanding-project-deployment) |
| [`ProjectProperty`](#projectproperty) | [Project properties](/en/features/project-properties) |
| [`SecureGatewayTunnel`](#securegatewaytunnel) | [On-prem groups](/en/on-prem/groups) |
| [`SharedAccount`](#sharedaccount) | [Connections](/en/connections) |
| [`SharingToken`](#sharingtoken) | [Sharing tokens](/en/recipes/settings#sharing) |
| [`Tags::Models::Tag`](#tagsmodelstag) | [Tags](/en/recipes/tags) |
| [`TeamProfile`](#teamprofile) | [Workspace admin settings](/en/workspace#workspace-admin) |
| [`Topic`](#topic) | [Event topics](/en/connectors/pubsub/pubsub-settings) |
| [`User`](#user) | Users. This resource type includes the `Workspace` and `Environments` subtypes, which you may encounter as the `resource[type]` in the API response. |
| [`WorkatoDbTable`](#workatodbtable) | [Data tables](/en/data-tables) |
| [`WorkatoSchema`](#workatoschema) | [Common data models](/en/features/common-data-model) |
| [`WorkatoTemplate`](#workatotemplate) | [Message templates](/en/features/message-template) |
| [`dashboards_page`](#dashboards_page) | [Insights dashboards](/en/insights/dashboards) |
| [`field_map_schema`](#field_map_schema) | [Dynamic field mapping](/en/oem/dynamic-field-mapping) |
| [`test_case`](#test_case) | [Test cases](/en/test-automation/test-case) |

## Event types

The following events are grouped by their associated resource type. Each resource type represents a category of activities tracked in the audit log.

### `AccountProperty`

| Event type | Description |
| --- | --- |
| `account_property_created` | An environment property was created. |
| `account_property_deleted` | An environment property was deleted. |
| `account_property_updated` | An environment property was updated. |

### `Adapter`

| Event type | Description |
| --- | --- |
| `connector_created` | A custom connector was created. |
| `connector_deleted` | A custom connector was deleted. |
| `connector_installed` | A custom connector was installed in the workspace. |
| `connector_released` | A custom connector was released. |
| `connector_shared` | A custom connector was shared. |
| `connector_shared_closed_source_changed` | The source code sharing settings of a custom connector were modified. |
| `connector_updated` | A custom connector was updated. |

### `ApiAccessProfile`

| Event type | Description |
| --- | --- |
| `access_profile_api_key_refreshed` | The API key for an access profile was refreshed. |
| `access_profile_created` | An API access profile was created. |
| `access_profile_deleted` | An API access profile was deleted. |
| `access_profile_updated` | An API access profile was updated. |

### `ApiClient`

| Event type | Description |
| --- | --- |
| `developer_api_client_created` | A Developer API client was created. |
| `developer_api_client_deleted` | A Developer API client was deleted. |
| `developer_api_client_updated` | A Developer API client was updated. |
| `token_leaked` | The API token for a Developer API client was leaked. |
| `token_regenerated` | A token was regenerated for a Developer API client. |

### `ApiCustomer`

| Event type | Description |
| --- | --- |
| `api_customer_created` | An API client was created in the API platform. |
| `api_customer_deleted` | An API client was deleted in the API platform. |
| `api_customer_updated` | An API client was updated in the API platform. |

### `ApiEndpoint`

| Event type | Description |
| --- | --- |
| `endpoint_activated` | An API endpoint was activated in an API collection. |
| `endpoint_created` | An API endpoint was created in an API collection. |
| `endpoint_deactivated` | An API endpoint was deactivated in an API collection. |
| `endpoint_deleted` | An API endpoint was deleted from an API collection. |
| `endpoint_updated` | An API endpoint was updated in an API collection. |

### `ApiGroup`

| Event type | Description |
| --- | --- |
| `api_collection_created` | An API collection was created. |
| `api_collection_deleted` | An API collection was deleted. |
| `api_collection_updated` | An API collection was updated. |

### `ApiPolicy`

| Event type | Description |
| --- | --- |
| `api_policy_created` | An API policy was created. |
| `api_policy_deleted` | An API policy was deleted. |
| `api_policy_updated` | An API policy was updated. |

### `ApiPrivilegeGroup`

| Event type | Description |
| --- | --- |
| `api_privilege_group_created` | A Developer API client role was created. |
| `api_privilege_group_deleted` | A Developer API client role was deleted. |
| `api_privilege_group_updated` | A Developer API client role was updated. |

### `AuditLogReplicationSettings`

| Event type | Description |
| --- | --- |
| `audit_log_streaming_content_updated` | The audit log streaming content was updated. |
| `audit_log_streaming_destination_updated` | The audit log streaming destination was updated. |
| `audit_log_streaming_disabled` | Audit log streaming was disabled. |
| `audit_log_streaming_enabled` | Audit log streaming was enabled. |

### `CommunityAdapterPublication`

| Event type | Description |
| --- | --- |
| `community_adapter_publication_approved` | A community connector listing was approved. |
| `community_adapter_publication_deleted` | A community connector listing was removed. |
| `community_adapter_publication_for_review` | A community connector listing was submitted for review. |
| `community_adapter_publication_updated_by_admin` | A community connector listing was updated by an admin. |

### `CustomOauthKey`

| Event type | Description |
| --- | --- |
| `custom_oauth_key_created` | A custom OAuth profile was created. |
| `custom_oauth_key_deleted` | A custom OAuth profile was deleted. |
| `custom_oauth_key_updated` | A custom OAuth profile was updated. |

### `Deployment`

| Event type | Description |
| --- | --- |
| `deployment_failed` | A deployment failed. |
| `deployment_finished` | A deployment finished. |
| `deployment_review_approved` | A deployment was approved. |
| `deployment_review_comment_created` | A comment was added to a deployment asset. |
| `deployment_review_created` | A review was created for a deployment. |
| `deployment_review_created_comment` | A comment was added to a deployment review. |
| `deployment_review_deleted` | A deployment review was deleted. |
| `deployment_review_rejected` | A deployment was rejected. |
| `deployment_review_reset` | A deployment was re-opened for review. |
| `deployment_review_updated_comment` | A comment added to a deployment review was updated. |
| `deployment_submitted_for_review` | A deployment was submitted for review. |

### `ExportManifest`

| Event type | Description |
| --- | --- |
| `manifest_created` | A manifest was created. |
| `manifest_deleted` | A manifest was deleted. |
| `manifest_updated` | A manifest was updated. |

### `Flow`

| Event type | Description |
| --- | --- |
| `recipe_concurrency_updated` | A recipe's concurrency setting was updated. |
| `recipe_copied` | A recipe was copied. |
| `recipe_created` | A recipe was created. |
| `recipe_data_retention_settings_updated` | A recipe's data retention settings were updated. |
| `recipe_deleted` | A recipe was deleted. |
| `recipe_made_private` | A recipe was made private. |
| `recipe_made_public` | A recipe was made public. |
| `recipe_moved` | A recipe was moved to a different folder. |
| `recipe_renamed` | A recipe was renamed. |
| `recipe_started` | A recipe was started. |
| `recipe_stopped` | A recipe was stopped. |
| `recipe_trigger_reset` | A recipe's trigger was reset. |
| `recipe_undeleted` | A recipe was restored. |
| `recipe_updated` | A recipe was edited. |
| `tags_added` | Tags were added to a recipe. |
| `tags_removed` | Tags were removed from a recipe. |

### `Folder`

| Event type | Description |
| --- | --- |
| `folder_created` | A folder was created. |
| `folder_deleted` | A folder was deleted. |
| `folder_moved` | A folder was moved to a different project or folder. |
| `folder_renamed` | A folder was renamed. |

### `LookupTable`

| Event type | Description |
| --- | --- |
| `lookup_table_created` | A lookup table was created. |
| `lookup_table_deleted` | A lookup table was deleted. |
| `lookup_table_exported` | A lookup table was exported as a CSV file. |
| `lookup_table_imported` | A lookup table was imported as a CSV file. |
| `lookup_table_moved` | A lookup table was moved to a different project. |
| `lookup_table_renamed` | A lookup table was renamed. |
| `lookup_table_truncated` | A lookup table was truncated. |
| `lookup_table_updated` | A lookup table was updated. |

### `ManagedUserGrant`

| Event type | Description |
| --- | --- |
| `team_membership_created` | A user joined a workspace with a specific role. |
| `team_membership_deleted` | A user was removed from the workspace. |
| `team_membership_updated` | A user's collaborator role was updated. |
| `workspace_moderator_assigned` | A workspace moderator was assigned. |
| `workspace_moderator_removed` | A workspace moderator was removed. |
| `workspace_moderator_updated` | A workspace moderator was updated. |

### `MemberInvitation`

| Event type | Description |
| --- | --- |
| `saml_sso_team_invitation_accept` | A collaborator accepted the workspace invitation for a workspace with SAML SSO enforcement enabled and joined with a specific role. |
| `team_invitation_accept` | A user accepted the workspace invitation and joined the workspace with a specific role. |
| `team_invitation_created` | A user invited another user to join the workspace with a specific role. |
| `team_invitation_deleted` | A user cancelled the invitation for a user to join the workspace. |
| `team_invitation_reject` | An invited user refused to join the workspace. |
| `team_invitation_updated` | A user updated another user's invitation by changing their collaborator role. |

### `OnPremAgent`

| Event type | Description |
| --- | --- |
| `on_prem_agent_activated` | An on-prem agent was activated with an activation code. |
| `on_prem_agent_created` | An on-prem agent was registered in an on-prem group. |
| `on_prem_agent_deleted` | An on-prem agent was removed from an on-prem group. |
| `on_prem_agent_disabled` | An on-prem agent was disabled. |
| `on_prem_agent_enabled` | An on-prem agent was enabled. |
| `on_prem_agent_renamed` | An on-prem agent was renamed. |

### `Package`

| Event type | Description |
| --- | --- |
| `package_exported` | A package was exported. |
| `package_imported` | A package was imported. |

### `PrivilegeGroup`

| Event type | Description |
| --- | --- |
| `role_created` | A collaborator role was created. |
| `role_deleted` | A collaborator role was deleted. |
| `role_permissions_changed` | The permissions for a collaborator role changed. |
| `role_updated` | A collaborator role was updated. |

### `Project`

| Event type | Description |
| --- | --- |
| `project_created` | A project was created. |
| `project_deleted` | A project was deleted. |

### `ProjectBuild`

| Event type | Description |
| --- | --- |
| `project_build_downloaded` | A project build was downloaded. |

### `ProjectProperty`

| Event type | Description |
| --- | --- |
| `project_property_created` | A project property was created. |
| `project_property_deleted` | A project property was deleted. |
| `project_property_updated` | A project property was updated. |

### `SecureGatewayTunnel`

| Event type | Description |
| --- | --- |
| `on_prem_group_created` | An on-prem group was created. |
| `on_prem_group_deleted` | An on-prem group was deleted. |
| `on_prem_group_renamed` | An on-prem group was renamed. |
| `on_prem_group_setting_updated` | An on-prem group setting was updated, such as the allowlist, email alerts, or log management configuration. |

### `SharedAccount`

| Event type | Description |
| --- | --- |
| `connection_connected` | A connection was established successfully. |
| `connection_created` | A connection was created. |
| `connection_deleted` | A connection was deleted. |
| `connection_disconnected` | A connection was disconnected. |
| `connection_moved` | A connection was moved to a different folder. |
| `connection_updated` | A connection was updated. |
| `tags_added` | Tags were added to a connection. |
| `tags_removed` | Tags were removed from a connection. |

### `SharingToken`

| Event type | Description |
| --- | --- |
| `sharing_token_created` | A sharing token was generated for a recipe. |
| `sharing_token_deleted` | A sharing token was revoked for a recipe. |

### `Tags::Models::Tag`

| Event type | Description |
| --- | --- |
| `tag_created` | A tag was created. |
| `tag_deleted` | A tag was deleted. |
| `tag_updated` | A tag was updated. |

### `TeamProfile`

| Event type | Description |
| --- | --- |
| `scim_token_created` | A System for Cross-domain Identity Management specification (SCIM) token was created. |
| `scim_token_refreshed` | A SCIM token was refreshed. |
| `scim_token_revoked` | A SCIM token was revoked. |
| `team_profile_auth_method_changed` | The workspace authentication method was changed. |
| `team_profile_created` | The workspace authentication method was created. |
| `team_profile_handle_changed` | The workspace ID was changed. |
| `team_profile_jit_provisioning_disabled` | SAML SSO Just-in-Time (JIT) provisioning was disabled for the workspace. |
| `team_profile_jit_provisioning_enabled` | SAML SSO Just-in-Time (JIT) provisioning was enabled for the workspace. |
| `team_profile_name_changed` | The workspace name was changed. |
| `team_profile_role_sync_disabled` | Roles sync through SAML SSO was disabled for the workspace. |
| `team_profile_role_sync_enabled` | Roles sync through SAML SSO was enabled for the workspace. |
| `team_profile_saml_configured` | SAML SSO setting was saved for the workspace using a specific SAML provider. |
| `team_profile_saml_required_disabled` | SAML SSO enforcement was disabled for the workspace. |
| `team_profile_saml_required_enabled` | SAML SSO enforcement was enabled for the workspace. |

### `Topic`

| Event type | Description |
| --- | --- |
| `topic_created` | An event topic was created. |
| `topic_deleted` | An event topic was deleted. |
| `topic_moved` | An event topic was moved to a different project or folder. |
| `topic_reset` | An event topic was reset. |
| `topic_retention_updated` | The message history retention of the event topic was updated. |
| `topic_schema_updated` | An event topic schema was updated. |
| `topic_updated` | An event topic was updated. |

### `User`

| Event type | Description |
| --- | --- |
| `account_activated` | A workspace was activated. |
| `account_activation_email_resent` | A workspace activation email was re-sent. |
| `account_activation_email_sent` | A workspace activation email was sent. |
| `account_email_updated` | An account email was updated. |
| `admin_two_fa_disabled` | Two-factor authentication (2FA) was disabled for the workspace. |
| `app_access_changed` | App access for the workspace was updated. |
| `aws_iam_external_id_scope_updated` | Amazon Web Services (AWS) Identity and Access Management (IAM) external scope was updated. |
| `data_retention_settings_updated` | The workspace data retention settings were updated. |
| `email_change_initiated` | An email change was initiated. |
| `emails_receiving_admin_notifications_updated` | The admin notification email addresses were updated. |
| `emails_receiving_error_notifications_updated` | The error notification email addresses were updated. |
| `environment_provisioned` | Environments were enabled for the workspace or a specific customer workspace. |
| `error_notification_throttling_disabled` | Error notification throttling was disabled. |
| `error_notification_throttling_enabled` | Error notification throttling was enabled. |
| `flows_concurrency_batch_update` | The recipe concurrency was updated. |
| `kms.key_id_updated` | The key management system key ID was updated. |
| `kms.key_material_updated` | The key management system key material was updated. |
| `kms.policy_changed` | The key management system policy was changed. |
| `kms.policy_enabled` | The key management system policy was enabled. |
| `kms.policy_updated` | The key management system policy was updated. |
| `max_worker_concurrency_changed` | The maximum number of concurrent workers that can be assigned to a recipe was changed. |
| `password_changed` | The account password was changed. |
| `password_reset_requested` | A password reset was requested. |
| `password_set` | An account password was set. |
| `password_was_reset` | An account password was reset. |
| `plan_addons_changed` | The capabilities for a workspace were changed. |
| `plan_detail_changed` | The plan detail was updated. |
| `plan_limit_changed` | The plan limit was changed. |
| `secret_manager_cache_cleared` | The secrets manager cache was cleared. |
| `secret_manager_created` | An external secrets manager was added to the workspace. |
| `secret_manager_scope_updated` | The external secrets manager scope was updated. |
| `secret_manager_updated` | The external secrets manager for the workspace was updated. |
| `switch_environment` | A user switched to a different environment. |
| `two_factor_authentication_disabled` | Two-factor authentication was disabled for an account. |
| `two_factor_authentication_enabled` | Two-factor authentication was enabled for an account. |
| `two_factor_authentication_recovery_codes_downloaded` | The two-factor authentication recovery codes for an account were downloaded. |
| `two_factor_authentication_recovery_codes_viewed` | The two-factor authentication recovery codes for an account were viewed. |
| `user_deleted` | A user account was deleted. |
| `user_login` | A user signed in to their account. |
| `user_login_failed` | A user's sign-in attempt failed. |
| `user_logout` | A user signed out of their account. |
| `user_restored` | A previously deleted user account was restored. |
| `workspace_automatically_provisioned` | Access to a workspace was automatically provisioned. |
| `workspace_automatically_updated` | Access to a workspace was automatically updated. |

### `WorkatoDbTable`

| Event type | Description |
| --- | --- |
| `tags_added` | Tags were added to a data table. |
| `tags_removed` | Tags were removed from a data table. |
| `workato_db_table_created` | A data table was created. |
| `workato_db_table_deleted` | A data table was deleted. |
| `workato_db_table_download` | The CSV file was downloaded for a data table. |
| `workato_db_table_file_column_download` | A data table file column was downloaded. |
| `workato_db_table_record_created` | A record was added to a data table. |
| `workato_db_table_record_deleted` | A record was removed from a data table. |
| `workato_db_table_record_updated` | A record was edited in a data table. |
| `workato_db_table_renamed` | A data table was renamed. |
| `workato_db_table_schema_updated` | The structure of a data table was modified. |

### `WorkatoSchema`

| Event type | Description |
| --- | --- |
| `common_data_model_created` | A common data model was created. |
| `common_data_model_deleted` | A common data model was deleted. |
| `common_data_model_updated` | A common data model was updated. |

### `WorkatoTemplate`

| Event type | Description |
| --- | --- |
| `message_template_created` | A message template was created. |
| `message_template_deleted` | A message template was deleted. |
| `message_template_updated` | A message template was updated. |

### `dashboards_page`

| Event type | Description |
| --- | --- |
| `dashboards_page_created` | An Insights dashboard was created. |
| `dashboards_page_deleted` | An Insights dashboard was deleted. |
| `dashboards_page_renamed` | An Insights dashboard was renamed. |
| `dashboards_page_updated` | An Insights dashboard was updated. |

### `field_map_schema`

| Event type | Description |
| --- | --- |
| `field_map_schema_updated` | Dynamic field mapping for a recipe was updated. |

### `test_case`

| Event type | Description |
| --- | --- |
| `test_case_copied` | A test case was copied. |
| `test_case_created` | A test case was created. |
| `test_case_deleted` | A test case was deleted. |
| `test_case_renamed` | A test case was renamed. |
| `test_case_updated` | A test case was updated. |

---
