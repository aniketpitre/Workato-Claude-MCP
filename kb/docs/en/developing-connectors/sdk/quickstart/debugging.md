---
url: 'https://docs.workato.com/en/developing-connectors/sdk/quickstart/debugging.md'
description: >-
  Use the Workato SDK Test code tab to test connections, actions, and triggers
  on the latest version of your custom connector before releasing it.
---

# Use the Test code tab

The SDK **Test code** tab is located within the **Source code** tab. The **Test code** tab enables you to test the connections, actions, and triggers in your connector before releasing it. The **Test code** tab also allows you to run tests on the latest version of your custom connector code.

![Test code tab](/assets/test-code-tab.CD-tLfB4.png)_**Test code** tab_

> **LATEST VERSION**
> 
> The **Test code** tab runs on the latest version of your connector code in your code editor. Any unsaved changes in the code editor result in the custom connector creating a new latest version before running any tests. A notification informs you when this happens.

Connections, actions, and triggers are hidden if there is an error in your latest version. You must correct the error before you can resume testing.

![Test code tab with error](/assets/test-code-with-error.DjE9R7XS.png)_**Test code** tab when there is an error_

## Test a connection

You must establish a successful connection before you can use the **Test code** tab. You can test this connection immediately in the **Connection** section of the **Test code** tab, after you define the connection inside the source code.

The **Test code** tab displays a `Connection success` message to inform you that the connection is successful. This connection is used for all following tests you execute in the **Test code** tab.

> **CREATE A CONNECTION TO TEST ACTIONS AND TRIGGERS**
> 
> You can't test actions or triggers until a successful connection is made. HTTP requests sent during triggers and actions can't actively authenticate with the API endpoint without a successful connection.

Learn more about configuring a connection in our SDK and the [connection types we support](/en/developing-connectors/sdk/guides/authentication).

## Test actions and triggers

You can test actions and triggers you have defined using the **Test code** tab after establishing a successful connection.

> **USE FULL-SCREEN MODE**
> 
> Use full-screen mode for an easier experience as you cycle through writing and testing your connector code.

![Test actions or triggers](/assets/testing-actions-triggers.ScTK3-YG.png)_Click the drop-down menus for triggers or actions to see the full list available in your latest version_

Click the **Test** button next to an action or trigger to test it. This opens a new window which mimics the action or trigger in the recipe editor. Changes to your connector code are saved automatically before the test begins when you attempt to test the action or trigger.

You can see the input and output for the action or trigger, as well as the network activity triggered when API requests are sent. The console tab shows the result of any `puts` Ruby methods executed during the test. This is useful for debugging and shows if the test was unsuccessful due to a logic error in the action or trigger.

The **Test code** tab highlights errors in red and displays an **Error** tab that contains the error message raised due to the logic error as well as the exact line of code that causes the framework to raise this error. A trace of the lines of code called that lead up to the final error is provided if the line of code was raised in a block other than the `execute` block.

## Rerun test

You may be required to make edits or change the configuration of your action after you test your custom connector. We recommend that your re-test your code after making updates.

Your recent test actions are stored and accessible from the code editor. This allows you to rerun tests without using the test editor to set up input data every time you make code adjustments. Click **Retest action** to retest your code.

![Input popup](/assets/sdk_rerun_test.CKH-a9r7.png)_Rerun test from the **Test code** tab_

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/quickstart/version-control.md
description: >-
  Manage versions of a custom Workato SDK connector, edit the latest source
  code, and release stable versions for your recipes.
---

# Version control

Version control in the Workato SDK platform can be done directly through the UI. The source code of the latest version of your custom connector automatically displays in the code editor when you first enter a custom connector homepage. This represents the latest source code that you or anyone with access to your workspace has worked on and committed into a version.

Since the latest version of your custom connector may not be the version you want your active recipes to work off, we've also introduced the concept of releasing a specific version of your connector to be used by all recipes in your account.

This enables you to have a stable version of your custom connector released for use in all your recipes while you continue to improve your connector before releasing the next version.

> **CHECK THE VERSION**
> 
> You can check the latest released version of a custom connector on the custom connector's homepage.

## Edit the latest version

The Workato SDK platform only allows you to edit the latest version of a custom connector's source code. By making changes directly in the code editor in the **Source code** tab, you can effectively edit the latest version. These changes are not saved until you click **Save changes** or test the code. The new custom connector source code is saved as the latest version when these changes are saved.

1. Click **Tools > Connector SDK**.
   
2. Select the custom connector you plan to edit.
   
3. Make your changes directly in the code editor on the **Source code** tab.
   
4. Click **Save**.
   

## Release the latest version

You can only release the latest version of your custom connector on the SDK platform. Recipes in your Workato account using this custom connector begin using this version from the next job onwards when you release the latest version of a custom connector. Test thoroughly using the **Test code** tab before releasing a version to prevent any bugs from disrupting your active recipes.

Workato actively searches for errors in your code and prevents you from releasing a version with errors. This is to prevent your recipes from breaking. You are informed of the line of code which contains the error so you can fix it.

> **RELEASE TO ENABLE SEARCH**
> 
> You must release a version of your connector before you can search for it while building your first connector. The currently released version of the connector displays on the custom connector homepage.

### Viewing and reverting to an old version

You can view and revert to an older version of your custom connector.

Navigate to the **Versions** tab of the custom connector homepage to view a table of versions. Clicking on any version will bring you to a page that contains a snapshot of the custom connector at that version.

1. Click **Tools > Connector SDK**.
   
2. Select the custom connector you plan to view or revert to.
   
3. Click the **Versions** tab and select a specific version to view.
   
   ![View old version](/assets/viewing-old-version.Blq57c9h.gif)_Select a specific version to view details about it and you can choose to revert to that specific version_
   
4. Optional. Click **Restore this version** to revert the version used in your recipes. This restores the version by creating a copy of the version's source code as a new latest version. You can begin editing or immediately release this version.
   

## Annotate your versions

You can annotate different versions of your connector with notes as your connector grows in functionality (and versions). Annotation enables you and your team to know what changed in each version from the previous version, such as the addition of a new action or fixing a bug. This allows other developers to immediately know what state the connector is in and what work remains to be done.

![Version notes plain view](/assets/base-view-version-notes.CNtGf8iM.png)_Annotate your versions with crucial information such as milestones_

You can filter the list of versions to see only versions that have been released to your production recipes if they contain version notes or both. This allows you to strip away smaller intermediary versions that might clutter your view. We recommend that you annotate your versions after a round of enhancements to make it easier to collaborate with teammates to build robust and powerful connectors.

![Version notes plain view](/assets/filtered-view-version-notes.U5Cmv0iu.png)_Version table when only those with version notes are chosen_

A popup displays to remind you to include any important notes before you release the latest version of your custom connector. This provides a simple and quick reminder to include what you have changed or added in this released version. This popup is optional and may be submitted without notes if you choose to do so.

![Version notes plain view](/assets/modal-popup-version-notes.DXLdliJr.png)_When releasing versions, let people know what you're doing. Whether it's testing changes you made to the front end of your connector or introducing new functionality_

---
