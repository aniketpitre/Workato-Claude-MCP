---
url: 'https://docs.workato.com/en/agentic/agentx-support/guides/customize-guides.md'
description: >-
  Customize AgentX Support guides to match your brand by configuring themes,
  logos, colors, and custom styling and scripts.
---

# AgentX Support - Customize guides

AgentX Support allows you to customize guides to align with your brand identity. You can access this page by going to **Guide > UI**.

![Customize guides](/assets/guide-ui.Cb--xpYe.png)_Customize guides_

This page includes two main sections:

- **Settings**: Configure theme options and add custom styling and scripts.
- **Guide view**: Preview the theme as it appears in your guide.

## Settings

- [Theme](#theme)
- [Configuration](#configuration)

### Theme

The **Theme** tab allows you to [create new themes](#create-a-custom-theme) or select existing ones to apply to your guide.

| Field | Description |
| --- | --- |
| Header Logo | Displays during guide loading and at the top of the interface. Provide a logo URL to enable this. |
| Primary Color | Sets the guide's primary color, which affects all clickable elements. You can choose a color directly or define it using a HEX code, RGBA, or a color spectrum. |
| Header logo height | Sets the height of the header logo in pixels. |
| Header logo width | Sets the width of the header logo in pixels. |

#### Create a custom theme

Complete the following steps to create a custom theme for a guide:

1. Go to **Guide > UI**.
   
2. Click **New**.
   
3. Enter a name for your custom theme.
   
4. Configure [theme settings](#theme).
   
5. Click **Submit**.
   

### Configuration

The **Configuration** tab contains the following sections:

- [Launcher](#launcher)
- [External styling](#external-styling)
- [External scripts](#external-scripts)

#### Launcher

Enable or disable the following launcher options:

| Field | Description |
| --- | --- |
| Show History | Displays a user's navigation path through the guide. Disabling this hides the option to view past steps. |
| Show Header | Toggles the visibility of the header. |
| Show Restart | Shows or hides the **Start Over** button, allowing users to restart the guide at any point. |
| Continue on end | Adds a **Back** button at the end of the guide, letting users revisit and adjust earlier choices. |

#### External styling

Use this section to add custom styling:

| Field | Description |
| --- | --- |
| CSS styles | Opens an editor for entering custom CSS. Changes are applied upon saving. |
| Stylesheets | Add external stylesheet URLs. Multiple stylesheets can be included. |

#### External scripts

Embed JavaScript directly or through external URLs to extend guide functionality.

| Field | Description |
| --- | --- |
| Inline Script | Add custom JavaScript directly. |
| Scripts | Reference external scripts through URL. |

## Guide view

Use the **Guide view** section to preview how your theme looks when applied to any existing guide.

---

---
url: >-
  https://docs.workato.com/en/agentic/agentx-support/guides/embed-guides-website.md
description: >-
  Embed AgentX Support guides on your website inline with an iframe or in a
  modal popup using the unique URL for each guide.
---

# AgentX Support - Embed guides on your website

You can display guides on your website using one of the following methods:

- Embed a specific guide directly within a webpage
- Display the guide in a modal popup

## Embed a guide within a webpage

Each guide has a unique URL that can be embedded using an `<iframe>`. This allows the guide to be displayed inline on your website.

Complete the following steps to embed a guide:

1. Open the guide you plan to embed.
   
2. Click **Advanced**.
   
   ![Click the Advanced button](/assets/guide-advanced.CQhVC2dy.png)_Click the Advanced button_
   
3. Copy the iframe code snippet provided.
   
   ![Copy the code snippet](/assets/embed-guide-iframe.ClXJs_VO.png)_Copy the code snippet_
   
4. Paste the snippet into the HTML of the webpage where you intend for the guide to appear.
   

## Display a guide in a modal popup

Guides can also be launched in a fullscreen modal to keep users focused on the guide while maintaining the current page context. This method uses a lightweight script to open the guide in a modal iframe.

The modal is triggered when an HTML element, such as a button or link, with the CSS class `dc-guide-{guide_id}` is clicked.

Complete the following steps to enable the modal popup:

1. Open the guide you plan to deploy.
   
2. Click **Advanced**.
   
   ![Click the Advanced button](/assets/guide-advanced.CQhVC2dy.png)_Click the Advanced button_
   
3. Copy the code from the **Guide in Modal Popup** section and paste it into the `<head>` of your website.
   
   ![Copy the code snippet](/assets/guide-modal-popup.tWVMwSOO.png)_Copy the code snippet_
   
4. Add the CSS class `dc-guide-{guide_id}` to any HTML element you plan to use as a trigger.

---

---
url: >-
  https://docs.workato.com/en/agentic/agentx-support/guides/embed-guides-agent.md
description: >-
  Embed AgentX Support guides in AI agents with the Guide node so customers
  follow step-by-step instructions within the conversation.
---

# AgentX Support - Embed guides in AI agents

You can embed guides directly into AI agents using the **Guide** node. This allows customers to follow step-by-step instructions within the conversation and troubleshoot issues seamlessly.

The following example illustrates how a guide appears during an AI agent interaction:

![Interact with guides from the AI agent chat interface](/assets/guide.as63sGAy.gif)_Interact with guides from the AI agent chat interface_

When a customer interacts with a guide, one of the following outcomes is recorded:

- **Solved**
- **Unsolved**
- **Skipped**

If the guide is marked as **Solved** or **Unsolved**, it is tracked as **Answer Feedback** for that specific guide.

---

---
url: >-
  https://docs.workato.com/en/agentic/agentx-support/guides/copy-guides-across-sites.md
description: >-
  Copy AgentX Support guide flows across sites to reuse interactive
  troubleshooting guides without rebuilding them.
---

# AgentX Support - Copy guides across sites

You can copy guide flows across sites in AgentX Support.

> **FEATURE AVAILABILITY**
> 
> This feature is only available to users on specific pricing plans. Refer to your pricing plan and contract to learn more.

Complete the following steps to perform the copy:

1. Go to **Guide > Guide Flows**.
   
2. Click the icon next to the guide you plan to copy.
   
3. Select **Copy**.
   
   ![Copy the guide](/assets/copy-guide.5ykEU3OE.png)_Copy the guide_
   
4. Choose the target site you plan to copy the guide to.
   
   ![Select target site](/assets/select-target-site.Cml4KVAP.png)_Select the target site_
   
5. Click **OK** to confirm.
   

> **GUIDE FLOW VERSIONING**
> 
> - If the target site already has a guide flow with the same ID, a **new version** is created under the existing guide flow ID.
> - If the guide flow ID doesn't exist on the target site, a **new guide flow** is created, and the copied version is set as the latest.

---
