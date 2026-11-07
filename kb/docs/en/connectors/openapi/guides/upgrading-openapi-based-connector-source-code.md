---
url: >-
  https://docs.workato.com/en/connectors/openapi/guides/upgrading-openapi-based-connector-source-code.md
description: >-
  Learn how to apply new versions of the OpenAPI source code and re-release the
  connector in your workspace, for both customized and non-customized
  connectors.
---

# Upgrading An OpenAPI-based Connector's Source Code

Over time, new versions of the OpenAPI source code will be released. These updates can include new features, enhancements, and/or bug fixes.

When a new version of the OpenAPI is available, the following banner will display on the connector's source code page:

![Updated OpenAPI connector version banner in the Workato UI](/assets/upgrade-available-banner.ucDRZCvl.png)

To take advantage of the updates, you'll need to apply the new version and re-release the connector in your workspace. How you perform the upgrade depends on whether you've customized the connector or not:

- [Non-customized connector](#upgrade-non-custom-connector)
- [Customized connector](#upgrade-custom-connector)

* * *

## Prerequisites

To upgrade an OpenAPI connector's source code, you'll need:

- **Familiarity with the Workato Connector SDK.** Refer to the [SDK documentation](/en/developing-connectors/sdk) for more info.
  
- **Privileges in Workato that allow you to:**
  
  - Modify SDK connections
- **For [customized connectors](#upgrade-custom-connector), you'll need a file comparison tool** like [Diffchecker](https://www.diffchecker.com/).
  

* * *

## Upgrading A Non-Customized Connector

1. Sign into your Workato account, if you aren't already.
   
2. Navigate to **Tools > Connector SDK**.
   
3. Click the tile of the OpenAPI connector you want to upgrade.
   
4. In the **An update is available!** banner, click the **Update connector** button:
   
   ![Updated OpenAPI connector version banner in the Workato UI](/assets/upgrade-available-banner.ucDRZCvl.png)
   
5. After reviewing the changes, click the **Release latest version** button in the top right corner of the page. This releases the new version of the connector in your workspace and allows it to be used in recipes.
   
6. In the window that displays, summarize the changes:
   
   ![Change summary and confirmation window](/assets/confirm-version-release-window.Co6Sj0jz.png)
   
7. When finished, click **Release**.
   

If successful, a **Successfully released version \[X\]** banner will display.

* * *

## Upgrading A Customized Connector

If you've customized your connector's source code, the upgrade process has some additional steps:

- [Step 1: Retrieve code for both versions](#retrieve-code-versions)
- [Step 2: Compare versions and resolve conflicts](#compare-resolve-code)
- [Step 3: Test the new version](#test-new-version)
- [Step 4: Release the new version](#release-new-version-custom)

This tutorial uses a file comparison tool - like the one built into GitHub - to identify differences between code versions. If you've used Workato's [Recipe Diff](/en/recipe-development-lifecycle/compare-versions-with-recipe-diff) feature, the concept is the same but for recipes.

In the image below, for example, is a text comparison of a file in GitHub:

![Example of a diff in GitHub](/assets/github-diff.HkViAs-G.png)

### Step 1: Retrieve Code For Both Versions

In this step, you'll retrieve your customized connector code and the source code for the new version.

1. Sign into your Workato account, if you aren't already.
   
2. Navigate to **Tools > Connector SDK**.
   
3. Click the tile of the OpenAPI connector you want to upgrade.
   
4. Select and copy the customized **Source code** to a convenient location, like a text file. **You'll need this in the next step.**
   
5. In the **An update is available!** banner, click the **Update connector** button. This will overwrite the customized source code with the new version:
   
   ![Updated OpenAPI connector version banner in the Workato UI](/assets/upgrade-available-banner.ucDRZCvl.png)
   

Leave this page open for now - you'll need it in the next step.

### Step 2: Compare Versions And Resolve Conflicts

In this step, you'll compare the code versions in your file comparison tool, apply changes, and resolve conflicts.

The instructions and examples in this section use [Diffchecker](https://www.diffchecker.com/), but you can use the file comparison tool you're comfortable with.

1. In your file comparison tool, copy and paste your **customized code** into the **Original Text** field.
   
2. Copy and paste the **new version source code** in the **Changed Text** field.
   
   Your setup should be similar to this:
   
   ![Code setup in the Diffchecker app](/assets/diffchecker-code-setup.Bp2NDGfw.png)
   
3. Click **Find Difference**.
   
4. Differences between the code versions will be highlighted. On a section-by-section basis, compare the versions and decide what to **keep from your customized code** and what to **use from the new version code**.
   
   In the example below, we kept the **title of our customized connector** by merging it into the **new version code**:
   
   ![Applying a change from customized code to new version code](/assets/diffchecker-apply-changes.DwODFDZZ.gif)
   
5. Repeat the previous step until you've reviewed the entirety of the changes between the versions.
   

### Step 3: Test The New Version

In this step, you'll use the [SDK Test code tab](/en/developing-connectors/sdk/quickstart/debugging) to test the new version of the connector.

**Note**: At least one active connection is required to use the **Test code** tab.

1. In your file comparison tool, copy the new version of your customized code.
   
2. Navigate back to the browser window where the connector is open in your Workato account.
   
3. Paste the customized code into the **Source code** field.
   
4. In the **Debug** section, use the **Connection** and **Actions** options to test the new version.
   
   **Note**: The **Test code** tab runs on the latest version of the code currently in the code editor. Before a test is run, unsaved changes will be saved and a new latest version of the connector will be created. A notification will display when this occurs.
   

When you've finished testing and resolving any issues, move onto [releasing the new version](#release-new-version-custom).

### Step 4: Release The New Version

In this step, you'll release the new version of the connector in your workspace. Releasing the new version allows it to be used in recipes.

1. After you've finished testing the new version, click the **Release latest version** button in the top right corner of the page.
   
2. In the window that displays, summarize the changes:
   
   ![Change summary and confirmation window](/assets/confirm-version-release-window.Co6Sj0jz.png)
   
3. When finished, click **Release**.
   

If successful, a **Successfully released version \[X\]** banner will display.
