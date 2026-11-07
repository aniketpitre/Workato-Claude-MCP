---
url: 'https://docs.workato.com/en/control-plane/manage-workspaces.md'
description: Use Control plane to link multiple workspaces.
---

# Link workspaces

You must link workspaces to your Control plane to enable centralized identity governance. A workspace provides a single location for projects, Workato [tools](/en/tools), such as data orchestration, event streams, and API platform, and other platform features, such as agents and MCP servers.

> **CONTROL PLANE ISN'T A WORKSPACE**
> 
> Control plane isn't a workspace. Control plane doesn't provide the configuration or tools for teams to collaborate, build recipes, and deploy recipes for a department, level of business, or organization unit.

## Link a workspace to Control plane

Complete the following steps to link a workspace to your Control plane:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Workspaces**.
   
6. Click **\+ Link new workspace**.
   
   ![Click + Link new workspace](/assets/link-new-workspace.U1diCE2Q.png)_Click **\+ Link new workspace**_
   
7. Enter the workspace linking ID in the **Workspace linking ID** modal.
   
8. Click **Send request**. The request is sent to the workspace owner for approval. The workspace is listed in your Workspaces with a **Pending** label. You can manage the workspace from the Control plane after the owner approves the request.
   
   ![Workspaces](/assets/manage-workspaces.UixWvDkC.png)_Workspaces_
   

## Resend link request

You can resend a Control plane link request for workspaces with the following labels:

- Pending
- Canceled
- Rejected
- Unlinked

Complete the following steps to resend a link request:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Workspaces**.
   
6. Click the **...** (ellipsis) option menu of the workspace you plan to send another request to.
   
7. Click **Resend request**.
   

## Cancel link request

You can only cancel a link request on workspaces labeled as **Pending** in Control plane.

Complete the following steps to cancel a link request:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Workspaces**.
   
6. Click the **...** (ellipsis) option menu of the workspace where you plan to cancel your link request.
   
7. Click **Cancel request**.
   
8. Click **Cancel request** in the **Cancel request?** modal.
   

## Unlink a workspace

Complete the following steps to unlink a workspace from your Control plane:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Workspaces**.
   
6. Click the **...** (ellipsis) option menu of the workspace you plan to unlink.
   
7. Click **Unlink**.
   
8. Click **Unlink** in the **Unlink workspace?** modal.
   

## Accept an invitation to link a workspace

Complete the following steps to accept an invitation to link your workspace to a control plane:

1. Go to your email account associated with your workspace.
   
2. Locate the email invitation in your inbox.
   
3. Click **View invitation** in the body of the email.
   
   ![Control plane email invitation](/assets/control-plane-email-invitation.BXyOXjKX.png)_Control plane email invitation_
   
4. Sign in to your Workato account when redirected to the login screen.
   
5. Go to **Workspace admin > Settings > Control plane**.
   
6. Click **Accept**.
   

## Reject an invitation to link a workspace

Complete the following steps to reject an invitation to link your workspace to a control plane:

1. Go to your email account associated with your workspace.
   
2. Locate the email invitation in your inbox.
   
3. Click **View invitation** in the body of the email.
   
4. Sign in to your Workato account when redirected to the login screen.
   
5. Go to **Workspace admin > Settings > Control plane**.
   
6. Click **Reject**.

---
