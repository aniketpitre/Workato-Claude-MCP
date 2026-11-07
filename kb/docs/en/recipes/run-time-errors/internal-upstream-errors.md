---
url: >-
  https://docs.workato.com/en/recipes/run-time-errors/internal-upstream-errors.md
description: >-
  Learn how to distinguish and troubleshoot internal Workato errors from
  upstream and downstream application errors in your recipes.
---

# Internal and upstream/downstream application errors

Identifying the origin of an error in your solution is crucial for effective troubleshooting. Understanding whether the issue occurred within Workato, an intermediary middleware layer, or a backend database can help you streamline your efforts and achieve a timely resolution.

Differentiating between internal and external errors is important for both triggers and actions. Action errors typically receive more attention due to their complexity. However, addressing trigger errors is also critical, as they may indicate connectivity or configuration issues, particularly when interacting with external systems.

The following sections provide specific troubleshooting steps for each type of error:

## Internal errors

Refer to the following sections for common scenarios and troubleshooting methods for internal errors in Workato's platform-specific actions:

### SQL Collection by Workato

SQL Collection by Workato uses SQLite. Ensure your SQLite code adheres to the SQLite version 3.42.0 standards.

Refer to the relevant tab for troubleshooting tips based on the scenario you encounter:

**Create list: Action errors**

If you encounter the following error when using the **Create list** action:

![Create list action error](/assets/list-error.DhMQvChS.png)_Create list action error_

Verify the input fields. Ensure that the list source is an array and that it is set to **Formula** mode. ![Verify input](/assets/verify-input.QaP6DbNG.png)_Verify input_

**Query lists: Incomplete output**

If you encounter an `Incomplete output` error when using the **Query lists** action, update and sequence your output list schema correctly if the output appears incomplete. ![Sequence output](/assets/sequence-output.Dqm58TOa.png)_Sequence your output list schema_

**Query lists: No such column error**

If you encounter a `No such column error` when using the **Query lists** action, use the API name, not the label name, when writing the query. ![Use API name](/assets/api-name._t5aG_by.png)_Use API name_

### Parsers and readers (XML/JSON/CSV)

Errors with parsers typically result from data input that does not match the expected formats.

Complete the following steps to troubleshoot parsers and readers:

1. Ensure that the data does not contain prohibited strings or delimiters, such as commas in a CSV string.
   
2. Ensure XML strings do not contain unescaped `<` or `>` symbols, and handle backslashes carefully when parsing data.
   
3. Verify that your source data adheres to the expected format rules. Use tools such as Notepad++ or Sublime Text for on-prem validation.
   
4. Follow XML rules for parsers, and ensure your sample document accurately represents the documents you are parsing.
   

### RecipeOps

RecipeOps actions can help automate troubleshooting and error handling in your Workato recipes. They offer key functions to manage and resolve errors effectively, including the following:

- Error aggregation
  
- Use RecipeOps to gather errors from various jobs and recipes.
  
- Recipe restart
  
- Restart recipes that have been interrupted, typically due to trigger errors.
  
- Action retry scope
  
- Implement retries in the On Error block, retrying specific actions within a Monitor block.
  
- Complete reruns
  
- Repeat all job actions using the original trigger data.
  
- System recovery
  
- Support recovery strategies during frequent system outages, such as server downtimes or critical errors.
  

Errors associated with RecipeOps are uncommon. Learn more about [RecipeOps](/en/connectors/recipeops).

## Upstream/downstream application errors

Upstream and downstream application errors arise from applications connected to Workato, rather than from Workato itself. They often occur when connecting to external or internal systems.

Common scenarios include the following:

- Cloud connections
  
- Errors involving interactions with external cloud services such as Salesforce, Netsuite, or ServiceNow.
  
- On-premise connections
  
- Issues that occur when dealing with on-premise solutions such as SAP.
  
- Database interactions
  
- Errors due to connection timeouts, data discrepancies, or schema changes when interacting with databases.
  
- HTTP requests
  
- Problems with the Workato HTTP action, such as incorrect endpoints, timeouts, or payload formatting issues.
  
- Custom connectors
  
- Errors related to custom connectors can result from outdated APIs, incorrect configurations, or service downtimes.
  
- File system connections
  
- Errors can occur when actions involve file systems like SFTP or FTP due to permission issues, incorrect file paths, or server downtimes.
  

Handling these application errors requires an in-depth understanding of the external system. While Workato support can offer general guidance, consulting an expert on the specific external application can help you quickly pinpoint and resolve the problem.

### Troubleshoot external cloud connections

When managing actions related to external cloud systems in Workato, understanding the nature and source of errors is essential. Complete the following steps to troubleshoot these issues:

1. Check the HTTP error codes to identify why the call from Workato failed.
   
2. Inspect the debug tab for detailed HTTP interactions between Workato and the external system. If the tab only shows the execution time or is unavailable, try rerunning the job for more details.
   
3. Determine if the errors are intermittent or constant. Intermittent errors may indicate temporary connectivity issues, while constant errors suggest problems with the external application or your Workato request.
   
4. Consult the external application for logs or records related to the error in Workato. If there are no logs of Workato's message, it may indicate connectivity issues or rate limit constraints.
   

### Troubleshoot Workato HTTP actions

When using an HTTP connector action in Workato to connect with an external endpoint, complete the following steps to troubleshoot potential issues:

1. Verify connectivity to ensure the external application that Workato is attempting to reach is hosted on a server with internet access.
   
2. Include [Workato's IP addresses](/en/security/ip-allowlists) if the application needs to be added to an allowlist.
   
3. Verify incoming calls by checking the application logs for any calls from Workato.
   

### Categorize HTTP status responses

After addressing connectivity, IP allowlisting, and incoming call verification, categorize the errors according to the status codes outlined in the following tabs:

**2XX status codes**

2XX status codes indicate successful communication, with 200 being a common example. If you encounter issues with these codes in Workato, review how the external system generates and sends the 200 response.

**4XX status codes**

4XX status codes indicate client-side errors. The response should typically include details explaining the cause of the error.

**5XX status codes**

5XX status codes suggest server-side errors, indicating that the external system detected an issue or couldn't process your request.

Visit [Workato's systems status page](https://status.workato.com/) to check the current platform status.

**Non-HTTP status code responses**

If your error lacks an HTTP status code, it may be due to an internal error in the application making the call. Check your application logs to gain more clarity on these issues.

### Troubleshoot on-prem connectivity

When troubleshooting on-prem connectivity issues, log files are critical for gaining insights into potential problems.

The on-prem agent (OPA) logger creates a new log file at the beginning of each day, according to the on-premise system's time. Additionally, a new log file is generated once the file size exceeds 20 MB. If multiple log files are created in a single day due to this size quota, they are sequentially numbered for differentiation. For example:

- `/agent-2019-11-01.0.log`: This is the first file created for the day. If logs for the day don't exceed 20MB, this is the only file.
- `/agent-2019-11-01.1.log`: This is the next log file created if additional logs are needed that day. The last number in the file name gets incremented if there is a need for more files in that particular day.

OPA logs are stored in different locations depending on whether your system is running Windows or Linux.

**Windows**

Log files are stored in `%SYSTEMROOT%\System32\LogFiles\Workato` by default for on-prem agents operating as a Windows service. You can navigate to this file manually or use the shortcut in the **Start** menu under **All apps > Workato**.

Complete the following steps to change the log storage location:

1. Open the Windows **Start** menu.
   
2. Go to **All apps > Workato**.
   
3. Open the **Service Wrapper Configuration** app for the agent you plan to configure.
   
4. Go to the **Logging** tab.
   
5. Enter a new log storage location in the **Log path** field. This field locates the Windows service wrapper's lifecycle log (`Agent.<date>.log`), its stdout and stderr capture files (`<service-name>-stdout.<date>.log` and `<service-name>-stderr.<date>.log`), and the service's PID file (`workato.pid`).
   
6. Go to the **Startup** tab.
   
7. Go to the **Arguments** field and update the `--logs=` argument to point to the new log storage location. This argument configures the OPA's application log (`agent.log`).
   
8. Click **Apply**.
   
9. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
   

> **OPA LOG CONTENTS**
> 
> The level of detail included in your OPA logs depends on your agent configuration. Refer to the [Workato logging levels](/en/on-prem/agents/logging#logging-opa-activity) section for more information.

**Linux**

Log files are stored in `/var/log/messages` by default for on-prem agents operating as a Linux service through `systemd`. Because this file also contains logs from other Linux services, you must use the `journalctl` command to access OPA specific logs.

```shell
journalctl -u [name of the OPA service].service
```

The `-u` switch filters the logs returned by the service that created them. Replace `[name of the OPA service]` with the name you set for the OPA during installation.

You can further refine your log search using the following commands:

- `> [output-file]`: Exports the result of `journalctl` to a file.
- `--since`: Limits the generated logs to after a specific date and time.
- `--until`: Limits the generated logs to before a specific date and time.

For example:

```shell
journalctl -u workato.service --since "2020-07-26 23:15:00" --until "2020-08-5 23:20:00" > OPALogs.txt
```

Refer to Loggly's [Using journalctl](https://www.loggly.com/ultimate-guide/using-journalctl/) guide for additional journalctl information.

> **OPA LOG CONTENTS**
> 
> The level of detail included in your OPA logs depends on your agent configuration. Refer to the [Workato logging levels](/en/on-prem/agents/logging#logging-opa-activity) section for more information.

#### IP allowlisting

Ensure that you complete the necessary IP allowlisting steps if the external application requires it.
