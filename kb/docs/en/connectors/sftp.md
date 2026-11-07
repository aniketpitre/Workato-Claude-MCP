---
url: 'https://docs.workato.com/en/connectors/sftp.md'
description: >-
  The SFTP connector enables you to automate secure file transfer workflows,
  reading, writing, and managing files on your SFTP server.
---

# SFTP

[Video](https://www.youtube.com/embed/5Xos6eSUYHw?rel=0&rel=0)

SSH File Transfer Protocol (SFTP) is a file transfer protocol that encodes and transmits data through a secure channel. It establishes security by encrypting both authentication credentials and data files being transferred.

Use this connector for bi-directional SFTP integrations. This connector allows you to read, write, and manage files in your SFTP server.

With the SFTP connector, you use the triggers to monitor your SFTP server for events (for example, [New/updated CSV file in directory](/en/connectors/sftp/updated-csv-trigger)). You can also integrate recipe actions like [Upload file](/en/connectors/sftp/upload-file-action), [Rename file](/en/connectors/sftp/rename-file-action), and [Download file](/en/connectors/sftp/download-file-action).

## Use cases

Integrate the SFTP connector with your business applications to securely transfer and manage files. You can automate data imports, synchronize records, and ensure seamless file exchanges between systems. Automated workflows can eliminate manual file handling and improve data accuracy across your applications. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can optimize SFTP file transfers:

- [Update Quickbase records from CSV files](/en/getting-started/use-cases/sftp-csv-by-workato-quickbase) in SFTP.
- [Upload a CSV file](/en/getting-started/use-cases/active-directory-csv-sftp) with Active Directory entries to an SFTP server.

### How to authenticate with SFTP

Because SFTP is built on top of the Secure Shell Protocol (SSH), you can include SSH keys as part of your authentication flow. SSH keys can be used in combination with user ID/password or used independently to authenticate Workato to your SFTP server. This extends the security of your connection with SSH encryption for your public and private keys.

> **ON-PREM SSH-RSA SUPPORT**
> 
> SSH-RSA relies on SHA-1, which no longer meets modern security standards. Workato doesn't support SSH-RSA for cloud connections to SFTP. Use the [Workato on-prem agent (OPA)](/en/on-prem/agents) to create an on-prem connection if you need to authenticate using SSH-RSA, or contact your server administrator to enable a stronger host key algorithm.
> 
> Refer to the [SFTP connection profile](/en/on-prem/agents/connection/profile#on-prem-sftp-profile) to configure the OPA for SSH-RSA.

## Connection setup

![Connection setup](/assets/sftp-connection-setup.DXskpiMs.png)_SFTP connection setup_

| Input field | Description |
| --- | --- |
| Connection name | Given this connection a unique name that identifies which SFTP server it is connected to. |
| Location | Select an existing [project](/en/projects) for this connection or create a new one. |
| Connection type | If you want to connect using an [on-prem group](/en/on-prem/groups), select the group name from the picklist. Otherwise, to use a direct connection, select **Cloud**. |
| Auth type | Select which authentication method to use. |
| Username | The user name of the SFTP server to be connected. |
| Password | The password credential to the SFTP server to be connected. |
| _Private key_ | _Only for **Public/private key** authentication type._ The SSH private key for the SFTP server to be connected. You must provide the SSH private key in [OpenSSH format](http://www.openssh.org/). To save a key in this format, specify `SecureShellPrivateKeyFormat.NewOpenSecureShell` value as the format parameter. Refer to the [Private key example format](#private-key-example-format) for more information. |
| Hostname | The address of your SFTP server. |
| Port | The default port for SFTP is `22`. |
| Host key fingerprint | A hash of the SSH public key. Workato supports SHA256 and MD5 encryption. For on-premise connection contact SFTP server administrator for the public key in Base64 format. |
| Transfer buffer size | The size of the buffer used to transfer files. |
| Force close | Shuts down the SSH connection at the end of each transaction. Toggle this if your SFTP server connection attempts get stuck. Otherwise, leave it blank. |

### Connecting to SFTP using Workato on-prem agent

Access your SFTP server using the Workato on-prem agent by selecting the on-prem group under the **Connection type** field.

Configure the SFTP connection directly in Workato cloud when using [cloud profiles](/en/on-prem/agents/connection/cloud). Note that some properties may not be supported for on-premise connections.

Refer to the [SFTP profile](/en/on-prem/agents/connection/profile#on-prem-sftp-profile) for more information about supported properties if your on-prem group connection uses a `config.yml` file.

Contact your support team to troubleshoot any issues with connecting to a legacy SFTP server or if you encounter a "connection closed" error.

> **ON-PREM AGENT VERSION**
> 
> OPA 24.0 or newer is required to use the SFTP connector.

> **TROUBLESHOOT UNKNOWNHOSTEXCEPTION ERRORS**
> 
> Refer to the [On-prem connections issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-opa-connections#sftp-unknownhostexception-error) troubleshooting guide if you encounter an `UnknownHostException` error.

### Private key example format

You must specify the `SecureShellPrivateKeyFormat.NewOpenSecureShell` value as the format parameter to save your key in the OpenSSH format.

An example private key in OpenSSH format:

```
-----BEGIN OPENSSH PRIVATE KEY-----
EcvBi0CzMfLzAAAAgQCd/q/q1zxTyIWYW3+Io+eMvuMc7w17fVJEwCILNiB6CQea
dPt3OWWr4boMjnaKOf6HvgCMgAQVoKzHEnM6wpa3Xm1CaS17xBRe/1fZl4lClzoZ
ebrOYmmt/nWj8cgWxB/aFGcBfk5Zn/DPOTMPTiIsTKQR7R6CBMWpw8Ssa6hEvQAA
AIBEmhtgDjsztfMyeWHygUs0965DeT69XxqOd0J4kuaeF6MP29Q1AZiojey/E2hF
Z8TLqynQ6hHWVzij489TsxiWiDFs46rUoX2K3FVTGOXAV/JE8V0AaQLymv1PhIce
1Vq89CXM1fNPRv6/yQ9RSlJA7vDg6vCPrmyA4bK6/Oq80w==
-----END OPENSSH PRIVATE KEY----- |
```

## Related resources

The SFTP connector documentation contains the following resources:

- [New/updated file trigger](/en/connectors/sftp/updated-file-trigger)
- [New/updated CSV file trigger (batch)](/en/connectors/sftp/updated-csv-trigger)
- [Create folder](/en/connectors/sftp/create-folder-action)
- [Delete file](/en/connectors/sftp/remove-file-action)
- [Delete folder](/en/connectors/sftp/delete-folder-action)
- [Download file](/en/connectors/sftp/download-file-action)
- [Get file information](/en/connectors/sftp/get-file-information-action)
- [List folder](/en/connectors/sftp/list-directory-action)
- [Rename/move file](/en/connectors/sftp/rename-file-action)
- [Search files/folders](/en/connectors/sftp/search-files-action)
- [Upload file](/en/connectors/sftp/upload-file-action)

---
