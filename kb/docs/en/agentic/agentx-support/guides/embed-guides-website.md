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
