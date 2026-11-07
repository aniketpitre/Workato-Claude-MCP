---
url: 'https://docs.workato.com/en/control-plane/get-started.md'
description: >-
  Learn the key components needed to configure Control plane and get started
  governing multiple workspaces through a centralized identity.
---

# Get started with Control plane

Control plane enables you to govern multiple workspaces through a centralized identity. Use this documentation to understand Control plane key components and essential administrator configuration requirements.

## Control plane key components

Control plane consists of the following key components:

| Control plane component | Function | Description | Get started |
| --- | --- | --- | --- |
| [Workspaces](/en/control-plane/manage-workspaces) | Links multiple workspaces to a single identity for centralized policy management. | Send link requests to workspace owners, and resend, cancel, or unlink workspaces from Control plane. Workspace owners accept or reject link requests from their workspace settings. | [Get started with linking workspaces](/en/control-plane/manage-workspaces#link-a-workspace-to-control-plane) |
| [Collaborators](/en/control-plane/collaborators) | Collaborators help govern workspaces within Control plane. Control plane collaborators are separate from workspace collaborators. | Administrators can invite collaborators, assign roles, and remove access. | [Get started with collaborators](/en/control-plane/collaborators#invite-a-collaborator) |
| [End user access](/en/control-plane/add-end-users) | Controls which environments end users can access and which groups users belong to. | Add end users manually, assign environment access, and organize users into environment-specific end-user groups. | [Get started with end users](/en/control-plane/add-end-users#add-an-end-user-manually) |
| [AI registry](/en/control-plane/ai-registry) | Provides a central place to discover, govern, and share the AI assets built across your organization. | Includes an asset catalog of agents, MCP servers, and AI model routes from linked workspaces. Publish or unpublish assets, and give users and AI clients access through the User portal and Registry MCP. | [Get started with the AI registry](/en/control-plane/ai-registry#access-asset-catalog) |
| [AI usage](/en/control-plane/ai-usage) | Monitors AI token and request activity across all linked workspaces. | View usage by workspace, environment, route, model, identity, and consumer to see where usage originates, who's driving it, and what's consuming it. | [Get started with AI usage](/en/control-plane/ai-usage#access-ai-usage) |
| [Subdomain](/en/control-plane/configure-subdomain) | Provides the URL where end users access Control plane. | A unique subdomain for your organization. | [Get started with subdomains](/en/control-plane/configure-subdomain#configure-subdomain) |

## Configure Control plane

Administrators must complete the following steps to configure Control plane:

1. [Invite collaborators](/en/control-plane/collaborators#invite-a-collaborator) who help govern workspaces linked to Control plane.
   
2. [Set up collaborator authentication](/en/control-plane/authentication#set-up-a-saml-sso-provider) with your IdP, and then configure either [SCIM](/en/control-plane/scim-provisioning), [JIT](/en/control-plane/jit-provisioning), or [manual provisioning](/en/control-plane/manual-provisioning).
   
3. [Configure a subdomain](/en/control-plane/configure-subdomain#configure-subdomain) so end users can access Control plane.
   
4. [Link workspaces](/en/control-plane/manage-workspaces#link-a-workspace-to-control-plane) to enable centralized identity governance.
   
5. [Create end-user groups](/en/control-plane/user-groups#create-an-end-user-group) for specific environments.
   
6. [Set up end-user group authentication](/en/control-plane/user-groups#user-group-authentication).
   
   > **END-USER GROUP AUTHENTICATION IS SEPARATE FROM COLLABORATOR AUTHENTICATION**
   > 
   > End-user group authentication requires a separate configuration from collaborator authentication.
   
7. [Add end users](/en/control-plane/add-end-users#add-an-end-user-manually) and then assign each user to an end-user group.

---
