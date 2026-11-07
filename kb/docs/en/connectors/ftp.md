---
url: 'https://docs.workato.com/en/connectors/ftp.md'
description: >-
  The FTP/FTPS connector enables you to automate file operations on an FTP or
  FTPS server, including downloading, uploading, renaming, and removing files.
---

# FTP/FTPS

The FTP/FTPS connector enables Workato to perform file operations on an FTP or FTPS server, such as downloading, uploading, renaming, and removing files. You can use this connector to build workflows that sync files between systems, process incoming data files, or archive completed reports.

## Prerequisites

You must complete the following prerequisites before you use the FTP/FTPS connector:

- **Configure passive mode**: Ensure your server is in standard passive mode, not extended passive mode (EPSV). The process for enabling standard passive mode varies depending on your server implementation. Refer to your server’s documentation for specific instructions.
  
- **Verify external accessibility**: Ensure your server’s IP address is accessible from outside your network. Workato throws an error if you attempt to connect using an internal IP address that isn't visible on the internet.
  

The following example shows how to test FTP server connectivity and passive mode configuration on a Linux-based FTP server:

![FTP server setup](/assets/setup_test.Ci_wzyfA.png)

## How to connect to an FTP server from Workato

Workato supports the following connection types:

- **Cloud (direct) connections**: Connect directly to your FTP or FTPS server
  - [Create an FTP server connection](#workato-setup-cloud)
  - [Create an FTPS server connection](#workato-setup-cloud-ftps)
- **On-prem connections**: Connect through an on-prem agent
  - [Create an on-prem connection](#workato-setup-on-prem)

### Create an FTP server connection

Complete the following steps to create a cloud (direct) connection to your FTP server in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `FTP/FTPS` as your connection on the **New Connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Connect to FTP server](/assets/ftp-connect.DTZY1sEO.png)_Connect to FTP server_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**. This option creates a direct connection to your server. Refer to [Create an on-prem connection](#workato-setup-on-prem) to connect using an on-prem agent instead.
   
6. Use the **Server type** drop-down menu to select `FTP`.
   
7. Enter a fully qualified domain name (FQDN) or an IP address in the **Host name** field. For example:
   
   - **FQDN**: `companyname.sampleftp.com`
   - **IP address**: `192.0.2.10`
8. Enter the **Username** and **Password** to authenticate with the FTP server. The connection inherits provisions and scopes from this user.
   
9. Expand the **Advanced settings** section and specify the **Port** number if your FTP server uses a port other than the default (`21`).
   
10. Optional. In the **Advanced settings** section, use the **Login before send buffer size** drop-down menu to select whether to send `PASS` before any other FTP command.
    
11. Click **Connect**.
    

### Create an FTPS server connection

FTPS (File Transfer Protocol Secure) is a secure extension of FTP that adds support for encrypted data transfer using SSL and TLS. FTPS is ideal for handling sensitive data and complying with security policies.

Complete the following steps to create a cloud (direct) connection to your FTPS server in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **FTP/FTPS** as your connection on the **New Connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![FTPS server setup](/assets/ftps-connect.pZ29Dsb3.png)_FTPS server setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**. This option creates a direct connection to your server. Refer to [Create an on-prem connection](#workato-setup-on-prem) to connect using an on-prem agent instead.
   
6. Use the **Server type** drop-down menu to select `FTP-S`.
   
   > **ALLOW TRAFFIC TO WORKATO**
   > 
   > Ensure traffic to Workato is allowed from your server. Refer to the [IP allowlists](/en/security/ip-allowlists#traffic-to-workato) guide to add Workato to your allowlist.
   
7. Use the **Verify cert** drop-down menu to select whether to verify FTPS server certificates.
   
8. Select an **Ftps connection type**. Set the connection type to `Explicit` if your FTPS server uses a port number other than the default (`21`).
   
9. Enter a fully qualified domain name (FQDN) or an IP address in the **Host name** field. For example:
   
   - **FQDN**: `companyname.sampleftp.com`
   - **IP address**: `192.0.2.10`
10. Enter the **Username** and **Password** to authenticate with the FTPS server. The connection inherits provisions and scopes from this user.
    
11. Expand the **Advanced settings** section and specify the **Port** number if your FTPS server uses a port other than the default (`21`).
    
12. Optional. In the **Advanced settings** section, use the **Login before send buffer size** drop-down menu to select whether to send `PASS` before any other FTP command.
    
13. Click **Connect**.
    

### Create an on-prem connection

Complete the following steps to create an on-prem connection to an FTP/FTPS server in Workato:

> **OPA REQUIREMENTS**
> 
> OPA [version 25.0](/en/on-prem/agents/versions#v25) or higher is required to create an on-prem connection to an FTP/FTPS server.
> 
> Refer to the [connection profiles documentation](/en/on-prem/agents/connection/profile#on-prem-ftp-profile) if your on-premise group connections use `config.yml`. Alternatively, you can configure the FTP connection directly in Workato using a [cloud profile](/en/on-prem/agents/connection/cloud). Some properties may not be supported for on-premise connections.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **FTP/FTPS** as your connection on the **New Connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down to select an [on-prem group](/en/on-prem/groups).
   
6. Enter a fully qualified domain name (FQDN) or an IP address in the **Host name** field. For example:
   
   - **FQDN**: `companyname.sampleftp.com`
   - **IP address**: `192.0.2.10`
7. Specify the **Port** number if your server uses a port other than the default (`21`).
   
8. Enter the **Username** and **Password** to authenticate with the server. The connection inherits provisions and scopes from this user.
   
9. Expand the **SSL settings** section and select `Explicit` or `Implicit` as the **Ftps connection type**.
   
10. Enter an X.509 **Server certificate** in `.pem` format.
    
11. Optional. Use the **Trust all** drop-down menu to select whether to force the client to trust any certificate chain. Workato supports self-signed server certificates. Defaults to `No`.
    
12. Optional. Expand the **Connection encoding settings** section and enter an encoding type for the connection in the **Control encoding** field. For example: `UTF-8` or `US-ASCII`
    
    > **OPA REQUIREMENTS**
    > 
    > The **Connection encoding settings** section is only available for OPA [version 28.0](/en/on-prem/agents/versions#v28) or higher.
    
13. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/ftp/new-csv-file-in-directory-trigger.md
description: This trigger monitors a server directory for newly added CSV files.
---

# FTP/FTPS - New CSV file added in directory on FTP/FTPS server (batch)

The **New CSV file added in directory on FTP/FTPS server** trigger monitors a server directory for newly added CSV files. Jobs are only triggered from CSV files located at the first level of the directory that contains rows.

Use the [New/updated file in directory trigger](/en/connectors/ftp/new-updated-file-in-directory-trigger) to instead monitor new and updated files.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. Refer to the [Polling intervals](/en/recipes/polling-intervals) documentation for more information. |
| Directory path | Select a directory from the menu, or enter it manually. The trigger processes files in this directory by time last modified in ascending order. |
| Column names | Provide the column names in the CSV file. Input the columns manually or upload a sample CSV file to enter them all at once. |
| Column delimiter | Select the column delimiter in the CSV file. The following options are available: comma (`,`), space, tab, colon (`:`), semicolon (`;`), and pipe (`|`). |
| Contains header row? | Set to `Yes` if the first row in the CSV file is a header row containing column names. |
| Batch size | Specify the number of CSV rows to retrieve in each batch. Refer to the [Batch processing](/en/features/batch-processing) documentation for more information. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the CSV file. |
| First batch | Indicates if this is the first batch of rows from the file. |
| Last batch | Indicates if this is the last batch of rows from the file. |
| Lines | An array of objects representing the rows in the CSV file. Each object contains column data. |

---

---
url: >-
  https://docs.workato.com/en/connectors/ftp/new-updated-file-in-directory-trigger.md
description: This trigger monitors a server directory for new or updated files.
---

# FTP/FTPS - New/updated file in directory trigger

The **New/updated file in directory** trigger monitors an FTP or FTPS directory for new or updated files. Jobs are only triggered from CSV files located at the first level of the directory.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the full path of the directory to monitor. For example, `/user/personal_folder/`. |
| From | Select the date and time from which to start monitoring for new or updated files. Defaults to one hour ago if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Name | The name of the file. |
| Full path | The full path of the file. |
| Directory | Indicates whether the entry is a directory. This returns `false` for files and `true` for directories. |
| Size | The size of the file in bytes. |
| Permissions | The permissions associated with the directory or file. |
| Owner | The owner of the directory or file. |
| Group | The group associated with the directory or file. |
| Modification time | The time the file or directory was last modified. |

---
