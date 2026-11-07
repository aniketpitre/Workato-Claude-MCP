---
url: 'https://docs.workato.com/en/on-prem/agents/proxy.md'
description: >-
  Set up proxy server access for a Workato on-prem agent operating in an
  environment with limited internet connectivity.
---

# Set up proxy access for your on-prem agent

A proxy server allows an on-prem agent to operate in an environment with limited internet connectivity.

> **PKIX PATH BUILDING FAILED ERROR**
> 
> This error occurs when the agent can't validate the SSL certificate chain for the target service. This can happen if intermediate or root certificates are missing, if SSL inspection tools replace or modify certificates, or if a proxy or firewall intercepts the connection between the OPA host and the service.
> 
> Refer to [PKIX path building failed error](/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup#pkix-path-building-failed-error) for more information.

To define proxy settings for your agent, create a `proxy` section in your configuration file with the following parameters and modify your agent's activation command:

| Config file definition | Description | Activation command parameter |
| --- | --- | --- |
| `host` | The IP address of the host. | `--proxy-host=<host-ip-address>` |
| `port` | The port number the proxy uses. | `--proxy-port=<port-number>` |
| `username` | _Optional._ Defines a username for the connection. | `--proxy-username=<username>` |
| `password` | _Optional._ Defines a password for the connection. | `--proxy-password=<password>` |

Run the `activate` script with `--help` parameter to display the full list of accepted parameters.

> **ALLOWLIST WORKATO GATEWAYS**
> 
> Ensure your proxy server allows `CONNECT` requests to the Workato gateways if you plan to establish a secure tunnel. Refer to [On-premise gateway addresses](/en/security/ip-allowlists#on-premise-agent) for more information about the gateways to allowlist for your datacenter.

## Example configuration

The following `config.yml` section defines a password-protected proxy connection:

```yaml
proxy:
  host: 192.168.1.1
  port: 8080
  username: proxy_user
  password: proxy_password

database: ...

jms: ...
```

The following command activates the agent and connects it to the password-protected proxy:

```
bin\activate.cmd --code={activation-code} --proxy-host=192.168.1.1 --proxy-port=8080 --proxy-username=proxy_user --proxy-password=proxy_password
```

---
