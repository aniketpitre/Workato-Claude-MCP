---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-cyberark-conjur.md
description: >-
  Set up CyberArk Conjur for project-level secrets management to scope
  connection credentials to individual Workato projects.
---

# Set up CyberArk Conjur for project-level secrets management

Existing external secrets references that are scoped to the workspace level will stop working when you switch to project-specific secrets management.

* * *

> **FEATURE AVAILABILITY**
> 
> Secrets management is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Conjur host configuration for Workato

Integration between Workato and Conjur is based on the host/workload API key authentication.

For Workato to retrieve a secret from your Conjur instance, an API authentication request is first sent to your Conjur server based on the parameters specified when configuring the CyberArk Conjur connector. If the credentials are valid, Conjur responds with a short-lived access token. Workato then uses this access token to retrieve the actual secret value stored in Conjur if the host has the necessary `execute` and `read` permissions.

Policies on Conjur are written as `.yml` files. Visit the CyberArk Conjur documentation for [policy best practices](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/policy-best-practices.htm). The following steps describe how to develop a policy file.

For more information on policy syntax operators, refer to the [CyberArk Conjur documentation](https://docs.cyberark.com/conjur-open-source/Latest/en/Content/Operations/Policy/policy-syntax.htm).

1. Declare a group at the root policy:
   
   ```yaml
   - !policy
     id: workato-app
     body:
       - !group workato-secret-users
   ```
   
2. Declare variables and assign the group `[read, execute]` permissions.
   
   This example creates the `sql-password-prod` and `sql-host-prod` variables which store the password for a SQL database as well as the host name:
   
   ```yaml
   - &variables
     - !variable
       id: sql-password-prod
       kind: password
     - !variable
       id: sql-host-prod
       kind: password
   - !permit
     role: !group /workato-app/workato-secret-users       # group declared earlier
     privileges: [read, execute]
     resources: *variables
   ```
   
3. Declare the host, a layer, and assign membership of the host into the layer:
   
   ```yaml
   - !host workato-us-prod-1
   - !layer workato-us-prod
   - !grant
        role: !layer workato-us-prod
        members:
           - !host workato-us-prod-1
   ```
   
   - [Host documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-host.htm)
   - [Layer documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-grant.htm)
4. Grant membership of the layer into the group:
   
   ```yaml
   - !grant
     role: !group workato-app/workato-secret-users
     member: !layer workato-app/ workato-us-prod
   ```
   
   - [Grant documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-grant.htm)
5. Create a new secret on Conjur:
   
   ```yaml
   - !variable
     id: ddog-api-key
     kind: password
   ```
   
   - [Variable documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-variable.htm)
6. Grant `execute` and `read` permissions to group on selected variables:
   
   ```yaml
   - !permit
     role: !group /workato-app/workato-secret-users     # layer declared earlier
     privileges: [read, execute]
     resources: !variable ddog-api-key
   ```
   
   - [Permit documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-permit.htm)

Expand for an example of a full policy

```yaml
- !policy
  id: workato-app-dev
  body:
    - !group workato-secrets-dev
    - &variables
        - !variable
            id: sql-password-prod
            kind: password
        - !variable
            id: sql-host-prod
            kind: password
    - !permit
        role: !group /workato-app-dev/workato-secrets-dev       # group declared earlier
        privileges: [read, execute]
        resources: *variables
    - !host workato-us-dev-1
    - !layer workato-us-dev
    - !grant
        role: !layer workato-us-dev
        members:
            - !host workato-us-dev-1
    - !grant
        role: !group workato-secrets-dev
        member: !layer workato-us-dev
```

To which the expected response would be:

```json
{
    "created_roles": {
        "workato:host:workato-app-dev/workato-us-dev-1": {
            "id": "workato:host:workato-app-dev/workato-us-dev-1",
            "api_key": "1q3ye3gxxxx"
        }
    },
    "version": 1
}
```

## Select project-level scope for secrets management

1. Sign in to your Workato workspace.
   
2. Navigate to **Workspace admin > Settings > Security > External secrets manager**.
   
3. In **Scope**, select the option **Set up secrets management for each project individually**.
   
   ![Set up secrets management for the entire workspace](/assets/scope-project.DXME4lQ2.png)_Set up secrets management for each project individually_
   
4. Select **Save**.
   

## Select the project

1. In Workato, navigate to your projects.
   
2. Select the project that you plan to configure with secrets management.
   
3. In the project, navigate to **Workspace admin > Settings > External secrets manager**.
   
4. In the **Which secrets manager do you want to use?** field, select **CyberArk Conjur**.
   
   ![Secrets management interface of a project](/assets/scope-project-settings.tUH09fCk.png)
   
5. Click **Set up connection**
   

## Configure the connection in Workato

1. Configure the following fields in Workato:
   
   ![Configure CyberArk Conjur connection](/assets/setup.BJAAwE3z.png)_Configure CyberArk Conjur connection_
   
   - Connection name
     
   - Name your CyberArk Conjur connection.
     
   - Connection type
     
   - Workato supports both cloud and on-prem connection types. If you plan to use an on-prem group, select one from the drop-down.
     
   - Server URL
     
   - To connect to Conjur Cloud, the server URL must follow this format:
     
     ```html
     https://<subdomain>.secretsmgr.cyberark.cloud/api/
     ```
     
   - Organization account name
     
   - To connect to Conjur Cloud, input `conjur`.
     
   - Login ID
     
   - For host authentication, the ID must be prefixed with `host/`, for example: `host/workato-app/workato-user-1`.
     
   - API key
     
   - Conjur generates an API key for every user when the user resource is created. Learn more about generating an API key in [CyberArk Conjur's documentation](https://docs.cyberark.com/conjur-enterprise/latest/en/Content/Operations/Services/default_authn.htm).
