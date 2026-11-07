---
url: 'https://docs.workato.com/en/connectors/wrike.md'
description: >-
  The Wrike connector lets you automate project management: manage tasks,
  projects, folders, attachments, timelogs, and approvals, and trigger on
  changes.
---

# Wrike

[Wrike](https://www.Wrike.com/) is an online project management software that enables collaboration between co-located and distributed teams.

## API version

The Wrike connector uses [Wrike REST API v4](https://developers.wrike.com/documentation/api/overview).

## How to connect to Wrike on Workato

The Wrike connectors uses OAuth 2.0 authentication. This allows you to:

- Define the scopes for the connector
- Authenticate with Wrike

### Scopes for Wrike connector

Entailed in the permissions are scopes that define how the connectors is allowed to interact with Wrike data. For example, the [create task action](/en/connectors/wrike/create-task-action) requires the following scopes: _Default_, _wsReadWrite_.

You can edit the scope of the connectors by selecting **Advanced settings** > **Api scope**.

| Field | Description |
| --- | --- |
| Api scope | Select permissions to request for this connection. To enable the full suite of Workato triggers and action, you can **select all** to request for all scopes. If left blank, the connector will only request: _Default_. |
| Custom OAuth profile | Optional. Select a custom OAuth profile for this connection. |

### Authenticate with Wrike

Click **Connect** to sign in with your user credentials.

![Wrike connection setup](/assets/wrike-connector.D-hi5wgR.png)_Wrike connection setup_

A popup will appear that requests for your Wrike login credentials. Input your **Username / Password** into the fields provided.

![Username/password connection](/assets/wrike-connector-login.KUivamOh.png)_Username/Password connection_

| Field | Description |
| --- | --- |
| Email | The email of the Wrike account to connect. |
| Password | The password of the Wrike account to connect. |

---
