---
url: 'https://docs.workato.com/en/connectors/on-prem-files.md'
description: >-
  The On-prem files connector lets you upload, download, move, rename, and
  delete files, manage folders and CSV files, and trigger on new files in your
  network.
---

# On-prem files

Workato's On-prem files connector allows you to access files within a secure network, such as files behind a corporate firewall that can't be accessed directly.

> **CONTROL ON-PREM FILE ACCESS**
> 
> Use the [On-prem files](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#on-premise) privilege to manage who can access, create, edit, and delete on-prem files using this connector.

## How to connect to On-prem files

Complete the following steps to connect to the On-prem files connector:

> **PREREQUISITES**
> 
> This connector requires an active on-prem agent. Refer to the following guides to set up an on-prem agent:
> 
> - [Create an on-prem group](/en/on-prem/groups/create-group)
> - [Add an agent to a group](/en/on-prem/groups/add-agent)
> - [Run an agent](/en/on-prem/agents/run)

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `On-prem files` on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![On-prem files connection](/assets/connection.DDSYIqKA.png)_On-prem files connection using on-prem agent_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **On-prem group** drop-down menu to select the on-prem group you plan to use.
   
6. Specify the folder to use as the starting location for [relative paths](#relative-path) in the **Base** field.
   
7. Click **Connect** to complete the setup.
   

## Working with the On-prem files connector

### File paths

Inputs for this connector use relative paths. You can define the starting point for these paths in your agent's [config.yml](/en/on-prem/agents/connection/profile#on-prem-files-profile) file or when you [configure your connection in Workato](#how-to-connect-to-on-prem-files-on-workato).

- Absolute path
  
- Specifies the full location of a file or folder, starting from the root file. For example: `C:\folder1\folder2\filename.csv`.
  
- Relative path
  
- Specifies the location of a file or folder in relation to the location of another file or folder. For example: `..\folder2\filename.csv`.
  

Usage example

The following `config.yml` file defines the `base` path as `/Users/admin/projects`:

```yml
files:
  projects:
    base: /Users/admin/projects
```

To point to `/Users/admin/projects/engineering/2018_roadmap.csv` using this base path, use the relative path `/engineering/2018_roadmap.csv`.

### File name wildcards

Wildcard characters are supported in this connector.

- Single character wildcard `?`
  
- Represents one instance of any character. For example, `Report_draft_?.pdf` can represent `Report_draft_1.pdf`, `Report_draft_2.pdf` or `Report_draft_3.pdf`.
  
- Multiple character wildcard `*`
  
- Represents zero or more instances of any character. For example, `Report_draft*.pdf` can represent `Report_draft.pdf`, `Report_draft_1.pdf`, `Report_draft_2.pdf` or `Report_draft_3.pdf`.
  

> **REGEX FORMULAS**
> 
> Alternatively, you can switch the inputs field to [formula mode](/en/formulas/formula-mode) to use [Regex](/en/regex).

Usage example

For example, a single folder may contain multiple files following different naming conventions:

- :open\_file\_folder: ProductHour
  - :page\_facing\_up: Attendees\_2018\_10\_29.csv
  - :page\_facing\_up: Attendees\_2018\_11\_01.csv
  - :page\_facing\_up: Mailing\_list.csv
  - :bar\_chart: Slides\_2018\_10\_29.pptx
  - :bar\_chart: Slides\_2018\_11\_01.pptx

You can use wildcard characters to filter the files in this folder :

| Use case | Filter | Output |
| --- | --- | --- |
| Return all csv files with attendee information | Attendees\*.csv | Attendees\_2018\_10\_29.csv, Attendees\_2018\_11\_01.csv |
| Return all presentation slides from November | Slides\_2018\_11\_??.pptx | Slides\_2018\_11\_01.pptx |

### Long query error

You may encounter the following error when using the **On-prem files** connector with a database connector, such as **MySQL**:

```
Long query error: java.lang.IllegalArgumentException: Missing files profile laws rds cx
```

This error occurs when the **On-prem files** connector and a database connector use different on-prem groups. Set both connections to use agents in the same on-prem group to resolve this error.

---
