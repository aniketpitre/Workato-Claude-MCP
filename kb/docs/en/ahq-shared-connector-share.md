---
url: 'https://docs.workato.com/en/ahq-shared-connector-share.md'
description: >-
  Share a custom connector across your organization in Workato Automation HQ,
  choosing open source or proprietary closed source code for distribution.
---

# Share a connector

One of the critical advantages of managing your organization in Automation HQ is that you can easily manage all connections and update the workspaces to use the latest connector versions. This insures consistency, uninterrupted and reliable data access, and adherence to security policies you implement for the organization.

> **PREREQUISITE**
> 
> You must first develop, test, and release your [connector](/en/developing-connectors/sdk) before you can share it.

You can choose to share your custom connector with [open](#open-source-code) or [closed](#closed-source-code) code source.

## Share a connector with open source code

When you share your connector with open source code, all details about your custom connector's triggers, actions, and source code are publicly available. This option allows anyone to install, modify, and distribute your connector and its source code after installation.

## Share a custom connectors with proprietary code

You can share your custom connector as closed source. This allows you to share the connector while keeping your proprietary source code private. Proprietary code is controlled by partners and can't be viewed, modified, shared, or distributed without permission from the owner after it is installed. Sharing your connector as closed source also enables you to determine which Workato workspaces are allowed to install your connector.

> **FEATURE AVAILABILITY**
> 
> Closed code source connector sharing is subject to the following limitations:
> 
> - Collaborating workspaces must use the same data center as the custom connector's developer. Refer to [Share data between regions](/en/datacenter/datacenter-overview#share-data-between-regions) for more information on cross-region collaboration.
> - Partners must be given access to this feature. Contact your Customer Success Representative to learn more.

## Share a custom connector in Automation HQ

Complete the following steps to share a connector in Automation HQ:

1. Sign in to your Workato account.
   
2. Go to **Automation HQ**.
   
3. Select the **Shared connectors** tab.
   
   ![Shared connectors tab](/assets/automation-hq-workspace-shared-connectors.Dsp3-tRu.png)_**Shared connectors** tab_
   
4. Click **Share connector with all workspaces**.
   
5. Use the drop-down menus in the **Share connector** dialog to select a custom connector and the version you plan to share, then click **Share connector**.
   
   ![The Share connector dialog](/assets/share-connector-dialog.CuFbjRVX.png)_The **Share connector** dialog_
   
6. If your workspace has access to closed source connector sharing, you can decide to share your connector as open or closed source:
   
   **Share your connector as open source**
   
   1. Keep the **Share without source code** toggle off to make your source code visible to all users.
      
      ![Share your connector as open source](/assets/set-up-connector-sharing.C4_YPPvJ.png)_Share your connector as open source_
      
   2. Click **Start sharing**.
      
   
   **Share your connector as closed source**
   
   1. Click the **Share without source code** toggle to keep the source code of your connector private.
      
      ![Share your connector without source code](/assets/set-up-connector-sharing-closed-source._CxNZ09P.png)_Share your connector without source code_
      
   2. Enter the email addresses of workspaces that require access to your connector. Separate each email with a comma. These workspaces can view and install your custom connector but will not have access to your connector's source code.
      
      Refer to [Share your connector](/en/developing-connectors/sdk/quickstart/sharing#manage-closed-source-connector-access) for more information about managing access to your closed source connector.
      
   3. Click **Start sharing**.
      
   

## More resources

- [Shared connectors](/en/ahq-shared-connector)
- [Version a connector](/en/ahq-shared-connector-version)
- [Stop sharing a connector](/en/ahq-shared-connector-stop-sharing)

---
