---
url: 'https://docs.workato.com/en/oem/embedded-connections.md'
description: >-
  Implement the Embedded Connection Widget to let customers authenticate app
  connections in an iframe without leaving your application.
---

# Embedded Connection Widget implementation

You can use the Embedded Connection Widget to build and maintain integrations on a customer's behalf (this is also referred to as the Managed Services model). The Embedded Connection Widget is recommended for cases in which the Embedded partner builds and maintains integrations on their customers' behalf.

The Embedded Connection Widget is an embedded `iframe` within the partner UI. The embedded `iframe` contains a login window for customers to authenticate their connections in Workato without leaving the partner's application. After the app connections are authenticated, partners can programmatically start or stop the recipes built for their customers using Workato’s Embedded APIs.

You must construct a direct link URL and embed it within the `iframe` of the partner UI to use the Embedded Connection Widget.

> **WORKATO ACADEMY**
> 
> [Workato Academy](https://academy.workato.com/learn/courses/23/embedded-connection-widget) provides detailed instructions on implementing one of the Embedded Connection Widget's most common use cases.

This page consists of the following sections:

- [Prerequisites](#prerequisites)
- [Construct a direct link URL](#construct-url)
- [Embed the URL in an iframe](#embed-url)
- [PostMessage API](#postmessage)

## Prerequisites

Ensure that you have the following prerequisites before you construct a direct link URL.

- JSON Web Token (JWT)
  
- (**Required**) JWTs authenticate users and provide verified access to applications and resources. [Generate a JWT](/en/oem/jwt-direct-linking#step3) to facilitate secure access to connections in Workato.
  
- RSA Private and Public key
  
- The embedded iFrames are authenticated using JWT tokens which must be signed using a private key generated with the RS256 algorithm. You must provide the public key to your Workato Success Representative. The key is used to verify the generated JWT tokens. The generated keys must be in PEM format. Refer to the Workato documentation for instructions on [how to generate the private/public key pair](/en/oem/jwt-direct-linking#step1).
  
- Embedded vendor ID
  
- Leverage the [Update JWT signature verification key](/en/oem/oem-api/jwt-direct-link-configurations#update-jwt-signature-verification-key) API endpoint to retrieve your embedded vendor ID. Use this ID to generate the JWT token.
  
- Workato API key
  
- This API key is used to authenticate access to the Embedded Partner APIs. You can create an API key by going to **Workspace admin > API clients**, creating a new API client, and saving the generated API token.
  
- Origin URL
  
- The origin URL is the default domain where you embed the Connection Widget `iframe`. This enables the parent window to receive messages through [PostMessage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage). Provide your Workato Success Representative with the origin URL.
  

> **MULTIPLE ORIGINS**
> 
> If you are embedding the Connection Widget in multiple domains, include the unique origin in the [payload of the JWT.](/en/oem/jwt-direct-linking) Additionally, you must configure the origin URL in each customer workspace. Go to **Admin console > Manage customers** to access the relevant customer workspace. Click the **Settings** menu and update the origin URL.

- Connection ID
- (**Required**) Each Workato connection has a corresponding connection ID. For each Workato connection you want your customers to authenticate with the Widget, you need the connection's connection ID. If you don’t know the connection ID, you can obtain it by calling our [list connections API](/en/oem/oem-api/connections#list-connections).

> **NO CONNECTIONS IN CUSTOMER WORKSPACE**
> 
> If you do not have any connections in the customer workspace, including connections created manually or using Recipe Lifecycle Management import, you can create a shell connection in the customer workspace using the Embedded API. This is useful if you plan to have your customers authenticate access to applications before you have built the recipes for their use case.

- Customer Team Account ID
  
- (**Required**) This is the unique ID of the Embedded customer workspace. You can be obtain the Team account ID in the UI or the API. To obtain the Team ID from the UI: navigate to the Admin Console > select the specific customer and the Team ID is present in the URL. The Team ID can also be retrieved by calling Workato’s Embedded Partner API to fetch a customer workspace or list of customer workspaces.
  
- Direct URL
  
- (**Required**) The base of the direct link URL depends on the [data center](/en/datacenter/datacenter-overview) you use. You must construct a direct URL formatted for the data center you use to embed the Connection Widget into the partner UI.
  

> **OTHER USEFUL EMBEDDED APIS**
> 
> - [Get customer](/en/oem/oem-api/managed-users#get-customer-account)
> - [Create customer](/en/oem/oem-api/managed-users)

## Configure URL parameters

The direct URL format varies depending on which data center you use. The format uses the following structure:

```
https://<data_center>/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**US Data Center**`https://app.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**EU Data Center**`https://app.eu.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**JP Data Center**`https://app.jp.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**SG Data Center**`https://app.sg.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**AU Data Center**`https://app.au.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**IL Data Center**`https://app.il.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**CN Data Center**`https://app.workatoapp.cn/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**KR Data Center**`https://app.kr.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

**UK Data Center**`https://app.uk.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>`

## Embed URL in an iframe

Embed the direct link URL in an `iframe` in your application using the following code:

```html
<iframe src="https://www.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>"></iframe>
```

## PostMessage API

Workato uses the [window.PostMessage()](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) method to send messages from the Connection Widget to your application. This method renders different UI states for the Embedded Connection Widget window. Post messages follow this format:

```
{ type: string, payload: object }
```

> **TEST THE WIDGET**
> 
> If you are testing the Embedded Connection Widget for the first time, provide your Workato Customer Success Representative with the `origin URL`. This enables the `Window` object to receive the messages through the PostMessage API.

### Supported PostMessages

#### heightChange

Changes the height of the content, enabling the `iframe` to adjust its size to match the partner's UI.

Payload:

```
{
   height: number
}
```

Sample post message:

```json
{
    "wk": true,
    "type": "heightChange",
    "payload": {
        "height": 467
    }
}
```

#### connectionStatusChange

Reports a change in connection status. Use this event to handle different workflows, including starting a recipe, calling external APIs, or other instances where the connection status changes.

Payload:

```
{
  id: number,
  provider: string,
  connected: boolean,
  error: string
}
```

Sample post message:

```json
{
    "wk": true,
    "type": "connectionStatusChange",
    "payload": {
        "id": 453799,
        "provider": "google_drive",
        "connected": false
    }
}
```

#### `error`

Reports an error message.

Payload:

```
{
  message: string
}
```

Sample Post message:

```json
{
  "wk": true,
  "type": "error",
  "payload": {
    "type": "FatalEmbeddingError",
    "message": "Fatal embedding error: sub_missing",
    "details": {
      "reason": "sub_missing"
    }
  }
}
```

### Example of supported PostMessages

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script>
      window.addEventListener('message', receiveMessage);
      function receiveMessage(event) {
        var data = JSON.parse(event.data);

        switch (data.type) {
          case 'heightChange':
            document.getElementById('workatoId').style.height = data.payload.height + 'px';
            break;
          case 'connectionStatusChange':
            var message = data.error || (data.payload.connected ? 'Connected' : 'Disconnected');
            document.getElementById('statusId').innerText = message;
            break;
          case 'error':
            console.log(data.payload.message);
        }
      }
    </script>
  </head>
  <body>
    <h4>Status: <span id="statusId"></span></h4>
    <iframe id="workatoId" src="https://www.workato.com/direct_link/embedded/connections/<connection_id>>?workato_dl_token=<token>" style="width: 500px; height: 150px; border: 0"></iframe>
  </body>
</html>
```

---
