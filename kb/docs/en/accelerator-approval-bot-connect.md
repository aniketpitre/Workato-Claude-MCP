---
url: 'https://docs.workato.com/en/accelerator-approval-bot-connect.md'
description: >-
  Connect the Approval bot accelerator to Slack or Microsoft Teams and your
  source applications so it can route approval requests.
---

# Connect the Approval bot accelerator to your applications

Where you plan to implement the Approval bot accelerator determines the applications you must connect. For example, if you plan to implement the Approval bot in Slack, you must connect Slack to your Workato workspace. Similarly, you must connect to Microsoft Teams to implement the Approval bot in Microsoft Teams.

## Connect to Slack

Add a custom bot to your Workato workspace and connect it to your Workato instance by following these steps:

1. Sign in to your Workato account.
   
2. Go to **Platform** and select **Workbot**.
   
   ![Create workbot](/assets/approval-workbot-create.Ot0Acd7b.png)
   
3. Configure the Workbot profile. Reference our [Workbot for Slack setup guide](/en/workbot/workbot-for-slack-setup) for instructions.
   
4. Navigate to **Approval Bot > Slack > Connections** and select **ABS | CON-001 | Workbot for Slack**.
   
5. Select **Approval Bot profile**.
   
6. Click **Connect**.
   

### Connect to Microsoft Teams

1. In Workato, navigate to **Assets > Approval bot/Microsoft Teams Workspace** folder.
   
2. Select **ABT | CON-001 | Microsoft Teams Connection**.
   
3. Connect to Microsoft Teams by authenticating your connection with Microsoft.
   
   ![Connect to Microsoft teams](/assets/approval-connect-teams.BVUWePpm.png)
   

## Connect to Google Sheets

1. Connect to the spreadsheet.
   
   ![Connect to google sheets](/assets/approval-bot-connect-gsheets.BahTfHyH.png)_Connect to Google Sheets_
   
2. Google prompts you to allow Workato access. Click **Allow**.
   

> **CUSTOMIZE CONNECTORS**
> 
> The spreadsheet connector is a placeholder for the approval workflow of your choice. See [Customize the Approval bot for Slack](/en/accelerator-approval-bot-customize-slack) or [Customize the Approval bot for Microsoft Teams](/en/accelerator-approval-bot-customize-teams) for instructions on replacing Google Sheets with an application of your choice. You can also contact customer success for support.

---
