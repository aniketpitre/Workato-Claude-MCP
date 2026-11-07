---
url: 'https://docs.workato.com/en/control-plane/ai-usage.md'
description: >-
  Monitor AI token and request usage across every workspace linked to your
  Control plane, broken down by workspace, identity, and consumer.
---

# AI usage

AI usage provides a centralized view of AI token and request activity across every workspace linked to your Control plane. Use AI usage to see where usage originates, who's driving it, and what's consuming it, across [Model Gateway](/en/ai-gateway/routes) routes, [MCP servers](/en/mcp/mcp-servers), and [agents](/en/agentic/agent-studio/genies-configuration).

![AI usage overview](/assets/ai-usage-overview.CHmC8WCL.png)_AI usage overview_

## Access AI usage

Complete the following steps to access AI usage:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Click **AI usage** in the side navigation menu.
   

## Time range and filters

Use the time range drop-down menu to scope AI usage to a specific window, from the past 15 minutes up to the past year.

![Time range drop-down menu](/assets/ai-usage-time-range.CnSbr29C.png)_Time range drop-down menu_

Click **\+ Filters** to narrow the entire page to specific values across the following dimensions:

- Workspace
- Environment
- Business unit
- Route
- Model
- Consumer
- Identities
- User

![Filters menu with the available dimensions](/assets/ai-usage-filters.Cs-D_l3x.png)_Filters menu with the available dimensions_

## Usage overview

The usage overview chart plots activity over the selected time range. Click **Tokens** or **Requests** to switch which metric drives the chart and its accompanying breakdown.

**Tokens**

### Tokens

The **Tokens by type** panel shows the total tokens consumed in the selected period, split into the following categories:

- Input
  
- Cached read
  
- Output
  
- Cached write
  
- Reasoning
  

![Tokens by type breakdown](/assets/ai-usage-tokens.DLCYjylg.png)_Tokens by type breakdown_

**Requests**

### Requests

The **Requests by status** panel shows the total requests made in the selected period, split into the following categories:

- Success
- Rate limit exceeded
- Invalid request
- Server error
- Other errors

![Requests by status breakdown](/assets/ai-usage-requests.BcugNDRM.png)_Requests by status breakdown_

AI usage also displays the following metrics for the selected period, each with a percentage change compared to the previous period:

- **Avg tokens / request**: The average number of tokens consumed per request.
- **Active keys**: The number of API keys that made at least one request in the selected period.

### Segment the chart

Use the **Segment by** drop-down menu above the chart to change how chart bars are broken down. Available dimensions include:

- **Token type** (Tokens only): Input, Cached read, Output, Cached write, and Reasoning tokens.
  
- **Response** (Requests only): Success, Rate limit exceeded, Invalid request, Server error, and Other errors.
  
- **Workspace**: The workspace where the usage originates.
  
- **Environment**: The [Environment](/en/features/environments) (DEV, TEST, or PROD) the usage occurred in.
  
- **Route**: The Model Gateway [route](/en/ai-gateway/routes#create-a-route) that handled the request.
  
- **Model**: The underlying AI model that served the request.
  
- **Consumer**: The app, agent, recipe, or direct API key that made the request.
  

Hover over a bar to see the exact values behind it for that interval. The remaining values are grouped into **Everything else** when a dimension has more distinct values than the chart can display individually.

For example, segmenting the **Tokens** chart by **Model** shows how token consumption splits across models:

![Tokens chart segmented by Model](/assets/ai-usage-segment-by-tokens.xIPjEbsp.png)_Tokens chart segmented by Model_

Segmenting the **Requests** chart by **Route** instead shows how request volume splits across routes:

![Requests chart segmented by Route](/assets/ai-usage-segment-by-requests.DdumSb43.png)_Requests chart segmented by Route_

## Usage breakdown

AI usage breaks down activity into three panels. Each panel lists the top contributors for the selected period and a summary of how much of the total they represent.

### Workspaces

The **Workspaces** panel displays where usage originates. Use the drop-down menu to select breakdowns for **Environments**, **Models**, or **Routes**.

![Workspaces breakdown panel](/assets/ai-usage-workspaces._zJCy1kZ.png)_Workspaces breakdown panel_

### Identities

The **Identities** panel displays who's behind the usage. Use the drop-down menu to select breakdowns for **User** or **Non-human** identities. The panel also reports what portion of spend is attributable to a named identity versus machine-driven, for example, usage from service accounts or automated agents rather than a signed-in user.

![Identities breakdown panel](/assets/ai-usage-identities.CD06mKYm.png)_Identities breakdown panel_

### Consumers

The **Consumers** panel shows what's consuming tokens. Use the drop-down menu to select breakdowns for **Apps**, **Agents**, **Recipes**, or **Direct API**:

- **Apps**, **Agents**, and **Recipes**: Group usage by the client application, agent, or recipe making the request, aggregated across everyone who uses it.
- **Direct API**: Lists individual API keys used to call the Model Gateway directly. Each entry shows the key's label and the collaborator who created it.

![Consumers breakdown panel](/assets/ai-usage-consumers.DCSrAdYd.png)_Consumers breakdown panel_

---
