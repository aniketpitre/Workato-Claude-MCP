---
url: 'https://docs.workato.com/en/connectors/on-prem-command-line-scripts.md'
description: >-
  The On-prem command-line scripts connector is a utility connector that runs
  allowlisted command-line scripts in your private network through the on-prem
  agent.
---

# On-prem command-line scripts

Workato's On-prem command-line scripts connector allows you to run allowlisted command-line scripts in your private network through the on-prem agent. You can allowlist any command supported by the system that runs the on-prem agent.

> **CONTROL COMMAND LINE SCRIPT ACCESS**
> 
> Use the [Command line scripts](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#on-premise) privilege to manage who can create, edit, and delete connections for this connector. Limit this privilege to prevent unauthorized script execution.

## How to connect to On-prem command-line scripts

Complete the following steps to connect to the On-prem command-line scripts connector:

> **PREREQUISITES**
> 
> This connector requires an active on-prem agent. Refer to the following guides set up the agent:
> 
> - [Create an on-prem group](/en/on-prem/groups/create-group)
> - [Add an agent to a group](/en/on-prem/groups/add-agent)
> - [Run an agent](/en/on-prem/agents/run)

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `On-prem command-line scripts` on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![On-prem files connection setup](/assets/on-prem-scripts-connection.CsfjjSr3.png)
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **On-prem group** drop-down menu to select the on-prem group you plan to use.
   
6. Enter a concurrency quota in the **Concurrency limit** field. Requests that exceed this quota are queued. Defaults to 10 if not specified.
   
7. Enter the number of seconds to allow each script to run before timing out in the **Timeout** field. Defaults to 90 if not specified. For agents versions 2.14.0 and later, you can also set the timeout in the [Execute command-line script action](#execute-command-line-script-action).
   
8. Define the command-line scripts in the **Scripts** field. You can run these scripts through the on-prem agent using the [Execute command-line script action](#execute-command-line-script-action).
   
9. Click **Connect** to complete the setup.
   

## Execute command-line script action

The **Execute command-line script** action runs a predefined command-line script through the connected on-prem agent. You can define a script in one of the following:

- The`command_line_scripts` section of the on-prem agent's `config.yml` file.
- The **Scripts** field when you [configure your connection](#how-to-connect-to-on-prem-command-line-scripts). Commands you define in either location are automatically allowlisted. Refer to the [Command-line Scripts Profile](/en/on-prem/agents/connection/profile#command-line-scripts-profile) section for more information on script definition.

### Input

| Input field | Description |
| --- | --- |
| Command-line script | Select the script to run through the connected on-prem agent. |
| Timeout limit (minutes) | Enter the number of minutes to allow the script to run before timing out. The maximum value is 1440 minutes (24 hours). Defaults to 2 minutes if not specified. Only agent versions 2.14.0 and later are supported. Earlier versions use the `timeout` value specified in `config.yml`. |
| Run script in background? | Optional. Select whether to proceed with the recipe without waiting for the script to complete. In agents versions 2.14.0 and later, scripts that exceed 24 hours will timeout. |

Define additional inputs

You can specify additional input parameters in your script configuration. The following example specifies `target_directory` and `source_file` as parameters:

```yaml
command_line_scripts:
  workday_reports:
    concurrency_limit: 3
    timeout: 30
    scripts:
      copy_file:
        name: Copy file
        command:
          - /bin/cp "{{source_file}}" "{{target_directory}}"
        parameters:
          - { name: source_file }
          - { name: target_directory }
```

Workato displays these parameters as required values in the **Script input** section.

![Parameters on Workato recipe](/assets/input-parameters-action2.Bib2qPIY.png)_Input parameters in the recipe_

Refer to the [Command-line Scripts Profile](/en/on-prem/agents/connection/profile#command-line-scripts-profile) section for more information.

Escaping parameter values

You can use an escape character to handle parameter values with special characters. The `escape_char` value is set to `\` on Unix and `""` on Windows.

The following example escapes characters in the `target_file` value with a backslash:

```yaml
command_line_scripts:
  workday_reports:
    concurrency_limit: 3
    timeout: 30
    scripts:
      append_file_to_another:
        name: Append file to another
        command:
          - cat {{source_file}} >> {{target_file}}
        parameters:
          # Parameter quoting
          - { name: source_file, quote: '""' }
          # Advanced parameter quoting
          - { name: target_file, quote: {start: '""', end: '""', quote: '""', escape_char: \ } }
```

Refer to the [Command-line Scripts Profile](/en/on-prem/agents/connection/profile#command-line-scripts-profile) section for more information.

### Output

| Output field | Description |
| --- | --- |
| Process ID | Unique ID of the command-line script process. |
| Exit code | Exit status of the completed script. A successful command returns `0`, and an unsuccessful one returns an error code. |
| System out | Output message returned by the script. The maximum length is 50,000 characters. |

---
