---
url: 'https://docs.workato.com/en/oem/admin-console/shared-connectors.md'
description: >-
  Build, share, version, and remove custom connectors across all Embedded
  customer workspaces using shared connectors in the Admin console.
---

# Shared connectors

Shared connectors are [custom connectors](/en/developing-connectors/sdk) shared through the Embedded Admin console exclusively to all customers. Partners can build and manage the versions of the connectors required by their customer community, resulting in quicker turnaround time and greater control over the connector's functionality.

The shared connectors feature also enables Embedded partners to limit the use of their private APIs to their customers only if the custom connectors require them.

![Shared connectors](/assets/shared-connectors.RsP7bh3d.png)_Shared connectors tab in the Admin Console_

## Build a connector

[Video](https://www.youtube.com/embed/bfmavANqHNI?rel=0&rel=0)

You must build your custom connector in the admin account before you can share it. A custom connector enables Workato to interact with a single application through a series of [triggers](/en/recipes/triggers) and [actions](/en/recipes/actions).

Connectors built on the SDK are private, meaning they are only visible and available to the connector's owner. The connectors are first built in the admin account as custom connectors and then shared as **shared connectors**.

View the [SDK developer program](/en/developing-connectors/sdk) documentation to get started with building a connector.

## Share a connector

You can push your custom connector to your customer community after you build and test it. Ensure you release the version of the connector you plan to share, as there are often multiple versions of the same connector.

> **FEATURE AVAILABILITY**
> 
> Closed code source connector sharing is subject to the following limitations:
> 
> - Collaborating workspaces must use the same data center as the custom connector's developer. Refer to [Share data between regions](/en/datacenter/datacenter-overview#share-data-between-regions) for more information on cross-region collaboration.
> - Partners must be given access to this feature. Contact your Customer Success Representative to learn more.

1. Sign in to your Workato account.
   
2. Go to **Manage customers**, then select the **Shared connectors** tab.
   
3. Click **Share connector with all workspaces**.
   
4. Use the drop-down menus in the **Share connector** dialog to select a custom connector and the version you plan to share.
   
5. Click **Share connector**.
   
   ![The Share connector dialog](/assets/share-connector-dialog.CuFbjRVX.png)_The **Share connector** dialog_
   
6. Choose how to share your connector if your workspace supports closed source sharing:
   
   **Share your connector as open source**
   
   1. Keep the **Share without source code** toggle off to make your source code visible to all users.
      
      ![Share your connector as open source](/assets/set-up-connector-sharing.C4_YPPvJ.png)_Share your connector as open source_
      
   2. Click **Start sharing**.
      
   
   **Share your connector as closed source**
   
   1. Enable the **Share without source code** toggle to keep the source code of your connector private.
      
      ![Share your connector without source code](/assets/set-up-connector-sharing-closed-source._CxNZ09P.png)_Share your connector without source code_
      
   2. Enter the email addresses of workspaces that require access. Separate each address with a comma. These workspaces can view and install the connector but can't access its source code.
      
      Refer to [Share your connector](/en/developing-connectors/sdk/quickstart/sharing#manage-closed-source-connector-access) to manage closed source access.
      
   3. Click **Start sharing**.
      
   

After customers install the custom connector, they can use it in their recipes by selecting it in the recipe editor. The connector is unavailable on the customer's **Tools > Connector SDK** page.

### Version management

Partners may continually develop the connector while customers use a prior version of the connector. After development and test cycles, Embedded partners can release the latest version of the connector.

![Shared connectors](/assets/shared-connectors-versioning.DVtzOZp2.png)_Select a connector to share_

Workato prompts you to update to the latest version when you release a new version of a shared connector. Click **Update version** to choose from a list of released versions.

Partners may also revert to a previous version of the connector by clicking the overflow menu on each shared connector and selecting **Switch shared version**.

## Export shared connectors

You can export custom connectors from the admin account to customer or external accounts.

### Export to customer workspaces

If you previously shared the connector with your customers, it is already available in their accounts. Do not include the custom connector as part of the package during the export process if the custom connector is already present in their accounts.

![Shared connectors](/assets/shared-connectors-export.CtTSxCHk.png)_Select a connector to share_

Workato displays a warning message during the export process to remind users to remove the connector if they have already shared it with the intended account. In the example, the manifest used to build the package excludes the Simpletexting custom connector. The recipes work with the version of the connector shared by the partner in the admin account's Shared connectors page when imported.

### Export to other accounts

Include the custom connector in the manifest and package when exporting a shared connector to environments outside of customer workspaces. This installs the packaged connector if it doesn't exist, or updates the connector if it is already present in the other workspace.

## Remove shared connectors

Removing shared connectors is an irreversible action that prevents the discovery and usage of the connector in customer workspaces. Additionally, removing shared connectors stops customer recipes that use the connector. You must stop all active recipes using the connector before you remove it.

---
