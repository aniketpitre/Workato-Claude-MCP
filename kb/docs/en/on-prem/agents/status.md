---
url: 'https://docs.workato.com/en/on-prem/agents/status.md'
description: >-
  Reference for the Workato on-prem agent /status endpoint, which returns the
  agent process ID, state, version, active requests, and profiles.
---

# Status endpoint

You can programmatically retrieve the status of the on-prem agent by calling its `/status` endpoint.

## Sample request

```shell
$ curl https://localhost:3000/status -i

HTTP/1.1 200
Content-Type: application/json;charset=utf-8
Content-Length: 237
Date: Mon, 07 Mar 2022 07:19:08 GMT

{
  "pid":76801,
  "state":"connected",
  "active":"true",
  "version":"2.10.0",
  "active_requests":0,
  "active_tasks":0,
  "profiles":[
    {"profile":"sql","adapter":"sqlserver"},
    {"profile":"sql2","adapter":"postgresql"},
    {"profile":"sql3","adapter":"mysql"}
  ]
}
```

## Response schema

| Name | Type | Description |
| --- | --- | --- |
| pid | Number | Process ID of the agent |
| state | String | State of the agent. Possible values: initial, connecting, connected, disconnected, stopping |
| active | String | `true` if agent is enabled, `false` otherwise |
| version | String | Release version of the agent |
| active\_requests | Number | Number of active requests from agent to other services |
| active\_tasks | Number | Number of pending tasks. An async action involves one or more tasks. |
| profiles | Array | Lists the valid profiles configured on the agent |

---
