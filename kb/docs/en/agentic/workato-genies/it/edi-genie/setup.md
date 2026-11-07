---
url: 'https://docs.workato.com/en/agentic/workato-genies/it/edi-genie/setup.md'
description: >-
  Step-by-step instructions for setting up EDI Genie, including package
  installation, connection configuration, project properties, and genie
  activation.
---

# Set up EDI Genie

Use this guide to install and configure EDI Genie in your workspace.

## Prerequisites

Complete the following before beginning setup:

- Confirm that the Genie Installer is already installed in your workspace. Contact your Workato account team to complete this one-time setup if it isn’t already installed.
- Confirm you have an active Orderful account with API access enabled.
- Confirm that trading partner data, transaction logs, and error records are accessible through Orderful APIs.
- Collect admin email addresses for alert notifications.
- Choose a notification channel: Slack, Microsoft Teams, or Workato GO. EDI Genie is preconfigured for Slack. You can use Microsoft Teams or Workato GO instead with additional configuration.

## Install EDI Genie

Complete the following steps to install the required packages for EDI Genie:

1. Go to **Agentic | Installer > Templates > FUNC | \[SAMPLE\] 3. Install Genie Module**.
   
2. Click **Edit**, then do the following:
   
   1. [Refresh](/en/recipes/editor#refresh-schema) the recipe to load the latest available packages.
      
   2. In **Step 2**, select the latest version of **Agentic | EDI Genie** from the **Genie Module** drop-down menu. Set **Get dependencies** to `No`.
      
      ![Selecting the genie module package in the install recipe](/assets/select-package.DU44zZHr.png)_Select the latest version of the genie module_
      
      > **MODULE NOT VISIBLE**
      > 
      > If **Agentic | EDI Genie** doesn't appear in the drop-down menu, your workspace may not have been granted access. Contact your Workato account team and repeat this step once access is confirmed.
      
   3. In **Step 4**, set the **Folder** field based on your install type:
      
      - **Fresh install**: Leave the field empty. If you see an **x** icon next to the **Folder** field, click it to clear the cached value before running the job.
      - **Upgrade**: Select the existing **Agentic | EDI Genie** project. This preserves your existing configuration.
      
      ![Selecting the folder in the install recipe](/assets/select-folder.Aq4GS2Fh.png)_Select the folder to install EDI Genie_
      
3. Click **Test** and wait for it to complete. Confirm that the output of **Step 4** in the recipe shows a success status.
   
4. Confirm that **Agentic | EDI Genie** now appears in your workspace's projects list.
   

## Configure connections

Complete the following steps to configure connections:

1. Go to **Agentic | EDI Genie > Config > Connections**.
   
2. Locate **CON | EDI** and update the API key for the Orderful connection. Refer to [Workato EDI connector](/en/connectors/workato-edi#connection-setup) for connection setup instructions.
   
3. Locate the Slack connection and connect it to your Slack workspace. This authorizes EDI Genie to send and receive messages through the preconfigured Slack chat interface.
   

## Configure project properties

Complete the following steps to configure project properties:

1. Go to **Agentic | EDI Genie > Settings > Project properties**.
   
2. [Edit](/en/features/project-properties-manage#edit) the following project properties:
   
   | Property | Description | Example |
   | --- | --- | --- |
   | **file\_storage\_directory\_path** | Enter the directory path for storing Orderful guides if you are using file storage. | `Orderful Guides` |
   

## Configure EDI Genie

Complete the following steps to configure EDI Genie:

1. Go to **Agentic | EDI Genie**, select **EDI Genie**, and click **Edit**.
   
2. Select your [AI model](/en/agentic/agent-studio/ai-model/ai-model). EDI Genie is preconfigured to use Slack as its chat interface, so you don't need to configure one. Don't change the EDI Genie description.
   
   To use Microsoft Teams or Workato GO instead, see [Use Microsoft Teams or Workato GO](#use-microsoft-teams-or-workato-go).
   
3. Go to **Agentic | EDI Genie > Extensions > App Events** and open **Error pattern recognition and proactive alert generation**. In the **Business event** action step, select **EDI Genie** from the drop-down menu.
   
4. Go to **Agentic | EDI Genie > Core > EDI Skills > Orderful** and start all skills in the folder. For each skill, click the skill name, then click **Start recipe**.
   
5. Click **Start genie**.
   

> **SETUP COMPLETE**
> 
> EDI Genie is now configured. Use [Activate and test](#activate-and-test) to confirm it's working, or [Extend EDI Genie](#extend-edi-genie) to add knowledge base content and custom skills.

### Use Microsoft Teams or Workato GO

EDI Genie is preconfigured to use Slack as its chat interface. To use Microsoft Teams or Workato GO instead, create a new genie that replicates the EDI Genie configuration:

1. Create a new genie and give it a name and description similar to EDI Genie.
   
2. Copy the job description from EDI Genie and paste it into the new genie without changes.
   
3. Select your [AI model](/en/agentic/agent-studio/ai-model/ai-model) and [chat interface](/en/agentic/agent-studio/chat-interface/chat-interface). Don't change the genie description.
   
4. Add the core skills you want to use, along with the knowledge base.
   

## Extend EDI Genie

You can extend EDI Genie to add knowledge base content and build custom skills. All steps in this section are optional.

The **Core** folder holds the foundational logic for EDI Genie and can't be modified. You can extend EDI Genie through the **Extensions** and **Custom Extensions** folders without changing its default behavior.

### Extensions

The **Extensions** folder contains the **Knowledge Ingestion** module, maintained by Workato. Complete the following steps to ingest Orderful guides into the EDI Genie knowledge base:

1. Go to **Agentic | EDI Genie > Extensions > Knowledge Ingestion** to ingest Orderful guides into the EDI Genie knowledge base. Download the knowledge ingestion module for Google Drive or the file storage app you plan to use.
   

### Custom extensions

The **Custom Extensions** folder is where you build new skills or modify existing Extension skills. Clone assets from the **Extensions** folder into **Custom Extensions** before making changes. Assets in **Core** and **Extensions** are managed by Workato and can't be modified directly.

Complete the following steps to build a custom skill:

1. Go to **Agentic | EDI Genie > Custom Extensions > \[App Name\]**. Templates for new apps are already configured.
   
2. Rename the folder and skill to match the app name.
   
3. Add the skill to EDI Genie.
   

## Activate and test

Complete the following steps to confirm your setup.

> **SLACK EXAMPLE**
> 
> These steps use Slack, the preconfigured chat interface. If you created a separate genie for Microsoft Teams or Workato GO, access it through that interface instead. The verification step is the same: send a message and confirm the genie's reply.

1. Open Slack and go to the channel or direct message where you interact with EDI Genie.
   
2. Enter `Who are you?` and send the message. EDI Genie greets you by name, confirms its name, and describes its role.

---
