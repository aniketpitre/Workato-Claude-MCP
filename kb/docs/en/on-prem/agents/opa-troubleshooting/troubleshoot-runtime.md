---
url: >-
  https://docs.workato.com/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime.md
description: >-
  Troubleshoot Workato on-prem agent runtime issues, including heap space
  errors, logging errors, long query errors, and stuck jobs.
---

# On-prem runtime and performance issues

This guide covers issues that can occur during the on-prem agent (OPA) runtime. These include heap space errors, logging errors, long query errors, and jobs stuck due to dropped database connections.

## Java heap space errors

The following error log indicates the agent has reached its memory quota:

```
java.lang.OutOfMemoryError: Java heap space
```

This error indicates that OPA doesn't have enough memory to process large jobs or payloads. By default, the heap size is set to a fraction of available system memory.

**Windows**

1. Open the Windows **Start** menu.
   
2. Go to **All apps > Workato**.
   
3. Open the **Service Wrapper Configuration** app for the agent you plan to configure.
   
4. Go to the **Java** tab.
   
5. Enter the `-Xmx` parameter in the **Java Options** field. For example, enter `-Xmx10G` to allocate 10 GB of heap memory.
   
6. Click **Apply**.
   
7. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
   

**Linux, Mac, and Docker**

Open `run.sh` and add the `-Xmx` flag to the `JAVA_OPTIONS` variable to adjust heap memory on Linux, Mac, or Docker. For example, the following line allocates 10 GB:

```bash
JAVA_OPTIONS="${JAVA_OPTIONS:-} -Xmx10G"
```

Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.

## Resolve gateway names on servers with OPA installed

You may encounter the following errors when resolving Workato gateway names on servers with OPA installed:

- `sg3.workato.com`
- `sg4.workato.com`

Complete the following troubleshooting steps to resolve gateway names:

1. Connect to the server where your OPA instance runs.
   
2. Open your server's console.
   
3. Run the following commands to verify if the gateway names can be resolved from your Windows, Linux, and Mac server:
   
   `nslookup sg3.workato.com`
   
4. Run the following command on Linux and Mac servers to verify if the gateway names can be resolved:
   
   `dig sg3.workato.com`
   
   Your output is similar to the following:
   
   ```bash
   sg3.workato.com	canonical name = public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com.
   Name:	public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com
   Address: 54.224.75.148
   Name:	public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com
   Address: 52.206.161.203
   Name:	public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com
   Address: 52.204.114.159
   ```
   
   This successful output indicates that it is possible to resolve the domain name.
   

## Check gateway connectivity

You may encounter issues with establishing gateway connectivity on servers with OPA installed.

Complete the following troubleshooting steps to check gateway connectivity:

1. Connect to the server where your OPA instance runs.
   
2. Open your server's console.
   
3. Run the following commands to verify if the gateway names can be resolved from your Windows, Linux, and Mac server:
   
   ```bash
   curl -k -vvv -GET --no-alpn --key conf/cert.key --cert conf/cert.pem https://sg3.workato.com/gateway/ping
   ```
   
   Your output is similar to the following:
   
   ```bash
   * TLSv1.2 (IN), TLS handshake, Finished (20):
   * SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
   *
   (LINES SKIPPED)
   >
   < HTTP/1.1 200 OK
   < Content-Type: application/json
   < Date: Mon, 25 Jul 2022 21:33:42 GMT
   < Content-Length: 81
   <
   {"gateway_version":"1.0.1","os_platform":"linux","os_release":"4.19.0-10-amd64"}
   ```
   

## Verify the server certificate chain

You may encounter issues verifying the server certificate chain on servers with OPA installed.

Complete the following troubleshooting steps to verify the server certificate chain:

1. Go to your OPA installation folder. Refer to the [Accessing on-prem](/en/on-prem) documentation for more information about installation.
   
2. Download the Workato root certificate and save it in your OPA installation folder. Refer to the [HTTP SSL](/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime#download-the-certificate-chain) documentation for instructions.
   
3. Run the following command for Linux and Mac:
   
   ```bash
   curl -vvv -GET --no-alpn --cacert root_ca_cert.pem --key conf/cert.key --cert conf/cert.pem https://sg3.workato.com/gateway/ping
   ```
   
   The expected output contains the following:
   
   `SSL certificate verify ok`
   
   This indicates that the server certificate chain was successfully verified.
   

## OPA stopped creating logs

You may encounter an issue where OPA stops generating logs when running on Linux. This issue occurs when there is either no free space remaining on the disk or when the logging level settings are incorrect. Complete the following troubleshooting procedure to resolve this issue:

1. Run the following command to determine if there is free space left on the disk:
   
   ```bash
   df -h
   cat /etc/fstab
   parted -l
   ```
   
   This determines if the issue is related to disk space.
   
2. Verify that the logging permissions are correct.
   
   1. Run `ls -lah /var/log/workato-agent` to view log permissions.
      
   2. Run the following command if a user or group does not have permissions set to `workato`:
      
      ```bash
      chown -R workato:workato /var/log/workato-agent
      ```
      
3. Check that the logging level is set to debug in the config file. For example:
   
   `logger: debug`
   

## Jobs stuck indefinitely due to dropped TCP connections

Jobs that hang without producing an error or timeout are often caused by a firewall or NAT device silently dropping an idle TCP connection between OPA and the database. The JVM thread holding the socket receives no notification and waits indefinitely for a response.

You can configure TCP keepalive at the OS level to periodically probe idle connections and detect when they drop, allowing the stuck thread to fail and recover.

> **GLOBAL SETTINGS**
> 
> Keepalive settings typically affect all applications on the host, not just the Workato OPA.

**Windows**

Complete the following steps to configure keepalive settings on Windows:

1. Open the Windows registry editor (Regedit).
   
2. Go to the following path:
   
   ```text
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters
   ```
   
3. Create or update the following two **DWORD** values under the `Parameters` key:
   
   | Registry value | Description |
   | --- | --- |
   | `KeepAliveTime` | Milliseconds of inactivity before the first probe is sent. |
   | `KeepAliveInterval` | Milliseconds between subsequent probes. |
   
   For example, set `KeepAliveTime` to `300000` and `KeepAliveInterval` to `5000` to begin detection after 5 minutes of inactivity, and send probes every 5 seconds until the connection is confirmed dead.
   
4. Save your changes, then restart your machine for the changes to take effect.
   

**Linux**

Complete the following steps to configure keepalive settings on Linux:

1. Add the following lines to `/etc/sysctl.conf` to configure keepalive settings that persist across reboots:
   
   ```text
   net.ipv4.tcp_keepalive_time = INITIAL_WAIT
   net.ipv4.tcp_keepalive_intvl = INTERVAL
   net.ipv4.tcp_keepalive_probes = NUMBER_OF_PROBES
   ```
   
   Replace the placeholders with values suited to your network environment:
   
   | Parameter | Description |
   | --- | --- |
   | `INITIAL_WAIT` | Seconds of inactivity before the first probe is sent. |
   | `INTERVAL` | Seconds between subsequent probes. |
   | `NUMBER_OF_PROBES` | Number of unanswered probes before the connection is considered dead. |
   
   For example, the following configuration detects a dead connection in a maximum of 5 minutes and 15 seconds:
   
   ```text
   net.ipv4.tcp_keepalive_time = 300
   net.ipv4.tcp_keepalive_intvl = 5
   net.ipv4.tcp_keepalive_probes = 3
   ```
   
2. Save your changes, then run the following command to apply them without rebooting:
   
   ```bash
   sudo sysctl -p
   ```
   

## Long query error

You may encounter the following error when using the **On-prem files** connector with a database connector, such as **MySQL**:

```
Long query error: java.lang.IllegalArgumentException: Missing files profile laws rds cx
```

This error occurs when the **On-prem files** connector and a database connector use different on-prem groups. Set both connections to use agents in the same on-prem group to resolve this error.
