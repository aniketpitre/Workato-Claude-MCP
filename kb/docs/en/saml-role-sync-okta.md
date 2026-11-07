---
url: 'https://docs.workato.com/en/saml-role-sync-okta.md'
description: >-
  Configure Okta to sync Workato environment roles and collaborator groups
  through SAML attributes for DEV, PROD, and TEST environments.
---

# Okta SAML role sync configuration

When using Okta as your identity provider, you can sync environment roles and collaborator groups through SAML.

> **MIGRATION TO THE NEW PERMISSIONS MODEL**
> 
> If your organization is migrating from the legacy permissions model to the new permissions model, you must update your SAML and SCIM configurations in Okta. Workato doesn't automatically translate existing assignments. Update the following:
> 
> - Map SAML attributes such as `workato_role` and any environment-specific attributes (`workato_role_prod`, `workato_role_test`) to the new environment roles.
> - Configure the `workato_user_groups` SAML attribute if you use collaborator groups. Use direct attribute mappings for a small number of groups, or group attribute statements with regex for larger sets.
> 
> After you make these updates, test by assigning a user in Okta to the Workato app and verify in the [Activity audit log](/en/features/activity-audit-log) that the correct role and group claims are passed.

Here, we configure role sync for basic Workato environments: DEV (default), PROD, and TEST.

## Prerequisites

- Configure the SAML SSO for your Okta tenant.
- Enable just-in-time provisioning in the Workato UI.
- Enforce SAML SSO for your team or organization.

## Add environment role attributes to the Workato app user profile in Okta

Complete the following steps to add a new `workato_role` attribute to the Workato user profile.

Repeat the following steps for each environment you use in Workato:

1. Go to **Directory > Profile Editor > Workato App > + Add Attribute** in Okta.
   
2. Set the **Data type** to `string`.
   
3. Set the **Display name** to the environment attribute. For example, enter `workato_role` for the `DEV` environment. If your organization uses multiple environments, configure attribute statements for each one. Add additional attributes such as `workato_role_test` for the TEST environment and `workato_role_prod` for the PROD environment. The default `workato_role` attribute maps to the DEV environment.
   
4. Enter a **Description** for the attribute.
   
5. Select the **Define enumerated list of values** checkbox.
   
6. Add environment role values under **Attribute members**:
   
   | Display name | Value |
   | --- | --- |
   | Environment admin | Environment admin |
   | Environment manager | Environment manager |
   | Member | Member |
   | NoAccess | NoAccess |
   
   Values are case sensitive. If your workspace still uses the legacy permissions model, refer to the corresponding role values:
   
   LEGACY ROLES VALUES
   
   | Display name | Value |
   | --- | --- |
   | Admin | Admin |
   | Operator | Operator |
   | Analyst | Analyst |
   | NoAccess | NoAccess |
   
7. Define the length parameters of the attribute in the **Attribute length** field.
   
8. Select **Yes** in the **Attribute required** field.
   
9. Select **Personal** in the **Attribute type** field.
   
10. Set the **Mutability** field to `READ_WRITE`.
    
11. Click **Save Attribute**.
    

## Create Okta groups for environment roles

Create environment permission groups in Okta to map user access for each Workato environment.

Use the following naming convention:

```text
WKT-ENV | <ENVIRONMENT> | <ROLE>
```

For example:

- `WKT-ENV | DEV | Admin`: Assigns `workato_role` to the **Environment admin** role
- `WKT-ENV | DEV | Manager`: Assigns `workato_role` to the **Manager** role
- `WKT-ENV | DEV | Member`: Assigns `workato_role` to the **Member** role

Repeat for each environment.

### Assign groups to the Workato application

After creating your environment permission groups in Okta, assign them to the Workato application.

1. Go to **Applications and Resources > Applications > Workato > Assignments > Groups** in Okta.
   
2. Add all environment role groups you created for your Workato environments. For example, `WKT-ENV | DEV | Admin` or `WKT-ENV | PROD | Operator`. Environment groups map to the environment role attributes (`workato_role`, `workato_role_test`, `workato_role_prod`) that you configured in the user profile.
   

Users added to these Okta groups automatically receive the corresponding environment roles in Workato.

## Configure collaborator group assignments

Workato supports two approaches to assign the `workato_user_groups` attribute through SAML. Choose the option that fits the number of collaborator groups you manage:

- [Direct assignment](#direct-assignment): Use this method if your organization manages only a small number of collaborator groups (for example, fewer than 10). This approach pre-defines the list of groups in the Okta user profile.
  
- [Group-based assignment with regex](#okta-group-assign): Use this method if your organization manages many collaborator groups. This approach uses Okta groups with a standardized naming convention and a group attribute statement that dynamically passes all matching group names.
  

### Direct assignment

If your organization manages only a small number of collaborator groups, you can assign them directly to users by configuring the `workato_user_groups` attribute in Okta. Direct assignment is recommended when you manage a small, fixed set of collaborator groups.

1. Go to **Directory > Profile Editor > Workato App > + Add Attribute** in Okta.
   
2. Set the **Data type** to `string`.
   
3. Enter `workato_user_groups` as the **Display name** of the new attribute.
   
4. Optional. Enter a **Description** for the attribute.
   
5. Select the **Define enumerated list of values** checkbox.
   
6. Add collaborator group names under **Attribute members**. These names must exactly match the existing collaborator groups in Workato.
   
   For example:
   
   | Display name | Value |
   | --- | --- |
   | Analytics\_Team | Analytics\_Team |
   | Engineering\_Admins | Engineering\_Admins |
   | QA\_Reviewers | QA\_Reviewers |
   | All collaborators | All collaborators |
   
   > **ATTRIBUTE BEHAVIOR**
   > 
   > The `workato_user_groups` attribute manages project-level access in workspaces using the new permissions model.
   > 
   > The behavior of `workato_user_groups` depends on the values you configure in your identity provider (IdP):
   > 
   > - **Empty or omitted**: The user's existing collaborator group memberships remain unchanged.
   > - **All collaborators**: Removes the user from all explicit collaborator groups. The user retains access only if they inherit it through default environment roles.
   > - **Specific group names**: Adds the user to the specified collaborator groups. The user inherits the project-level permissions configured for those groups in Workato.
   
7. Select **Yes** in the **Attribute required** field.
   
8. Select **Personal** in the **Attribute type** field.
   
9. Set the **Mutability** field to `READ_WRITE`.
   
10. Click **Save Attribute**.
    

### Group-based assignment with regex

If your organization manages many collaborator groups, we recommend that you use Okta groups and a group attribute statement. This avoids having to predefine each group in the user profile. Group-based assignment is recommended if you have a large number of collaborator groups.

#### Create Okta groups for collaborator mapping

Use the following naming convention for collaborator groups:

```text
WKT | <ROLE> | <TEAM>
```

For example:

```text
WKT | Admin | Finance
WKT | Builder | HR Operations
WKT | Admin | Sensitive Projects
WKT | Admin | Reusable Assets
```

These group names must match existing collaborator groups defined in Workato.

Next, [configure the group attribute statement](#saml-attribute-statements) to pass these collaborator groups to Workato.

## Convert existing user assignments to groups

If your organization previously assigned roles at the user level, you can convert them to group-level assignments:

1. Go to **Applications and Resources > Applications > Workato > Assignments** in Okta.
   
2. Select **Convert Assignments**.
   
3. Search for a user by name to verify if they are eligible for conversion.
   
4. Choose **Convert selected** to migrate individual users to group-based assignments, or click **Convert all assignments** for bulk conversion.
   
   _Convert individual user assignments to group assignments_
   
5. Confirm that the user's assignment is now managed by a group, then click **Save**.
   
   _Verify app assignment management through groups_
   

## Configure SAML attribute statements for roles and groups

You must configure the SAML attribute statements to include `workato_role` and `workato_user_groups` attribute values each time a user signs into Workato through SAML SSO:

1. Go to **Applications and Resources > Applications** in Okta and select your Workato app integration.
   
2. Open the **Sign On** tab.
   
3. Click **Show legacy configuration** in the **Attribute statements** section.
   
   _Legacy attribute statements on the Sign On tab in Okta_
   
   This section also includes an **Add expression** option. This guide uses the legacy configuration.
   
4. Click **Edit** in the **Profile attribute statements** section and add the following **Name** and **Value** pairs. The **Name format** field is optional.
   
   <dl><dt>workato_role</dt><dd>appuser.workato_role</dd><dt>workato_role_test</dt><dd>appuser.workato_role_test</dd><dt>workato_role_prod</dt><dd>appuser.workato_role_prod</dd></dl>
   
   If you use [direct assignment](#direct-assignment) for collaborator groups, also add `workato_user_groups` with the value `appuser.workato_user_groups`.
   
5. Optional. Add a collaborator group attribute statement in the **Group attribute statements** section:
   
   - **Name**: `workato_user_groups`
   - **Name format**: Unspecified
   - **Filter**: Matches regex
   - **Regex**: `^WKT \|.*`
   
   This passes any Okta group whose name starts with `WKT |` as a value in `workato_user_groups`.
   
   _Configure group attribute statement for collaborator groups_
   
   > **GROUP ATTRIBUTE MAPPING**
   > 
   > Use this regex-based group attribute statement if your organization manages many collaborator groups and has adopted the group-based assignment model. The regex function depends on the naming convention of your groups.
   > 
   > If you configured the `workato_user_groups` attribute [directly](#direct-assignment) in the user profile, you can skip this step.
   

## Configure environment-specific Workato roles in Okta

If the [Lifecycle Management](/en/features/environments) feature is enabled in your Workato instance, you must configure environment-specific SAML attributes for each environment you use.

| Environment | SAML attribute |
| --- | --- |
| Dev (main) | `workato_role` |
| Test | `workato_role_test` |
| Prod | `workato_role_prod` |
| Sandbox | `workato_role_sandbox` |
| UAT | `workato_role_uat` |
| Stage | `workato_role_stage` |
| Pre-prod | `workato_role_preprod` |

## Assign the application to a user

Complete the following steps to assign the Workato application to an individual user:

1. Go to **Directory > Users > {Select User} > Assign Application > Workato** in Okta.
   
2. Confirm the **User Name** (email) is correct.
   
   _Assign the application to the user_
   
3. Assign the `workato_role_prod` attribute to a **PROD** environment role for the user.
   
4. Assign the **DEV** (default) environment role using the `workato_role` attribute. The same role options apply as in the previous step.
   
5. Assign the **TEST** environment role using the `workato_role_test` attribute. The same role options apply as in the previous step.
   
6. Click **Save**.
   

## Update the user role

To update a user's role, select a new value from the appropriate environment attribute (for example, `workato_role`, `workato_role_prod`, or `workato_role_test`), and then click **Save**.

_Change the user's role_

For example, you can update the **workato\_role\_prod** value for the user **dave.lee** from **Environment admin** to a custom **DevOps\_Admin** role.

## Remove environment access

To remove access to a specific environment that you specified earlier, change the user's role for any environment attribute to `NoAccess`.

For example, you can restrict access to the production environment by setting the **workato\_role\_prod** attribute to `NoAccess`.

## Verify role changes

If your organization uses Workato's Activity Audit Logs feature, you can verify the automatic role sync when the user logs in through SAML SSO.

Role changes triggered by SAML assertions appear under the **Source** attribute, with the value `saml_auto_sync`.

Manual role changes made in the Workato UI use the source `user`.

You can also see the **New Role** and **Previous Role** values.

_SAML roles sync activity audit log_

---
