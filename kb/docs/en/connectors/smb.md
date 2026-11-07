---
url: 'https://docs.workato.com/en/connectors/smb.md'
description: >-
  The SMB connector enables you to automate file-sharing workflows, uploading,
  downloading, and managing files and folders on SMB servers from Workato.
---

# SMB

Server Message Block (SMB) is a communication protocol used to share files. SMB relies on the TCP and IP protocols for transport. This combination allows file sharing over complex, interconnected networks, including the public Internet. The SMB server component uses TCP port 445. The SMB protocol supports both Windows and Unix operating systems. Use the Universal Naming Convention (UNC) to specify the location of resources that you plan to access with the connector.

The SMB connector supports the following actions and triggers:

- [New/updated file trigger](/en/connectors/smb/new-file-trigger)
- [Download file](/en/connectors/smb/download-file-action)
- [Upload file](/en/connectors/smb/upload-file-action)
- [Create folder](/en/connectors/smb/create-folder)
- [Delete resource](/en/connectors/smb/delete-action)
- [Get metadata](/en/connectors/smb/metadata-action)
- [List directory contents](/en/connectors/smb/list-action)

> **ON-PREM AGENT VERSION**
> 
> OPA 27.0 or newer is required to use the SMB connector.

## How to connect to SMB

Complete the following steps to set up your SMB connection using OPA:

> **CLOUD PROFILES**
> 
> Refer to [cloud profiles](/en/on-prem/agents/connection/cloud) to configure the SMB connection directly in Workato cloud instead of connecting through OPA.

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `SMB` as your connection on the **New connection** page.
   
3. Select **API Key (Internal integration)** in the **Authentication** field.
   
4. Provide a name for your SMB connection in the **Connection name** field. ![Connection setup](/assets/smb-connection-setup.BTgrFAEX.png)_SMB connection setup_
   
5. Select the project where you plan to store the connection from the **Location** drop-down menu.
   
6. Select an existing [on-prem group](/en/on-prem/groups). Workato uses agents from this group to establish a connection. Refer to the [connection profiles documentation](/en/on-prem/agents/connection/profile#on-prem-smb-profile) to configure an on-prem group that uses `config.yml`.
   
7. Enter the hostname or IP address of the server hosting SMB share in the **Host** field.
   
8. Enter the **Port** to connect to. The default port for SMB is `445`.
   
9. Enter the shared folder's name in the **Share name** field.
   
10. Optional. Enter the name of the domain to sign in to in the **Domain name** field.
    
11. Enter the user name of the SMB server in the **Username** field.
    
12. Enter the **Password** for the SMB server.
    
13. Click **Connect** to complete the setup.
    

## Relative path

A relative file path specifies the location of a file or folder in relation to the location of another folder. This is different from an absolute file path, which specifies the full location of a file.

---
