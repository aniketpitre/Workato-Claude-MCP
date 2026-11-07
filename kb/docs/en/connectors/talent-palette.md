---
url: 'https://docs.workato.com/en/connectors/talent-palette.md'
description: >-
  The Talent Palette connector lets you automate talent management workflows:
  import members and organizations and check import job status.
---

# Talent Palette

[Talent Palette](https://www.pa-consul.co.jp/talentpalette/) is a talent management system targeted at Japanese enterprises seeking to maximize operational efficiency.

## API Documentation

Complete the following steps to access Talent Palette's API documentation:

1. Sign in to the Talent Palette admin dashboard.
   
2. Go to the **FAQ** page and search for `API`.
   

This page provides information about API specifications, obtaining an API token, and formatting files for importing.

## Prerequisites

Complete the following steps to generate a client ID and client secret in Talent Palette:

1. Sign in to the Talent Palette admin dashboard.
   
2. Go to the **Admin Menu** tab.
   
3. Go to the **Others** section. If **Others** is not visible, click **Show All**.
   
4. Click **API**.
   
5. Click **\+ Add Client** to generate a new Client ID and Secret. These values are required to establish the connection in Workato.
   

## How to connect to Talent Palette on Workato

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Talent Palette** as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![Talent Palette connection](/assets/talent-palette-connection.CtZ8hbx2.png)_Talent Palette connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Talent Palette **Client ID**.
   
6. Enter your Talent Palette **Client secret**.
   
7. Enter your Talent Palette **Username**.
   
8. Enter your Talent Palette **Password**.
   
9. Click **Connect** to complete the connection.
   

## Actions

The Talent Palette connector supports the following actions:

- [Check job status](/en/connectors/talent-palette/check-job-status-action)
- [Import members](/en/connectors/talent-palette/import-members-action)
- [Import organizations](/en/connectors/talent-palette/import-organizations-action)

![Talent Palette Actions](/assets/talent-palette-actions.B7UfrG6U.png)_Talent Palette actions_

---

---
url: >-
  https://docs.workato.com/en/connectors/talent-palette/check-job-status-action.md
description: >-
  The Check job status action checks the status of bulk import jobs in Talent
  Palette.
---

# Talent Palette - Check job status action

The **Check job status** action checks the status of bulk import jobs in Talent Palette.

## Input

| Input field | Description |
| --- | --- |
| Job ID | Provide the Talent Palette ID of the registered job. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the current job in Talent Palette. |
| Registered date | The date and time the job was registered (JST). |
| Error | The error object, if the `Status` is `error`. |
| Retry Job ID | The Talent Palette ID of the retry job, if a 500 error occurred. |

---
