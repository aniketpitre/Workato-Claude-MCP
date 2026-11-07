---
url: 'https://docs.workato.com/en/getting-started/use-cases/mcp/github-mcp-app.md'
description: >-
  Create an MCP app to render pannable and zoomable images from your GitHub repo
  in your LLM chat.
---

# GitHub interactive images MCP app

This use case provides step-by-step instructions to add a custom GitHub fetch file tool to your MCP server to enable your LLM to render pannable and zoomable images from your GitHub repo directly in your LLM chat.

## What does this MCP app do?

This MCP app enables you to view, pan, and zoom your GitHub repo images directly in your LLM, such as ChatGPT, Claude, or Cursor.

```mermaid
graph LR
subgraph x[<strong>Configuration phase</strong>]
    direction TB
    B("GitHub connection") -->
    C("GitHub fetch file skill") -->
    D("MCP server") -->
    E("MCP app") -->
    F("LLM MCP integration")
end
subgraph y[<strong>Operational phase</strong>]
    direction TB
    BB("User prompt <br> in LLM") -->
    CC("MCP <br> tool call") -->
    DD("MCP app <br> renders <br> image") -->
    DDD("User pans <br> and zooms")
end

x --> y

classDef default fill:#fff,stroke:#000,stroke-width:2px,color:#000;
classDef WorkatoBlue fill:#5159f6,stroke:#5159f6,stroke-width:2px,color:#fff;
classDef WorkatoPink fill:#f66,stroke:#fff,stroke-width:2px;
classDef WorkatoTeal fill:#67eadd,stroke:#fff,stroke-width:2px,color:#000;

class x WorkatoBlue
class y WorkatoTeal
```

## Create an MCP app

Complete the following steps to build an MCP app that enables you to view, pan, and zoom your GitHub repo images directly in your LLM, such as ChatGPT, Claude, or Cursor.

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to tool configurations, MCP server connections, or conditional logic may be necessary to adapt this recipe to your workflow. This use case has been tested with ChatGPT, Claude, and Cursor. MCP app configuration and usage may vary with other LLMs.

1. Sign in to your Workato account.
   
2. Create a GitHub connection.
   
   ### Create a GitHub connection
   
   Connect to GitHub on Workato using one of the following authentication methods:
   
   - OAuth authentication. Workato recipes act on your behalf.
   - GitHub Apps. Workato recipes act as the app. Refer to [GitHub App authentication](#github-app-authentication).
   - A personal access token
   
   Refer to the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/developers/apps/differences-between-github-apps-and-oauth-apps) for more information.
   
   #### OAuth authentication
   
   View OAuth authentication steps
   
   Complete the following steps to connect your GitHub to Workato using OAuth authentication:
   
   1. Sign in to your Workato account and go to the project where you plan to add your GitHub connection.
      
   2. Click **Create > Connection** (or press C twice), then select **GitHub** as your connection.
      
   3. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu and select **OAuth App**.
      
   6. Optional. Click **Advanced configuration** to display the **Host name** field.
      
   7. Optional. Enter a **Host name**. This is applicable when using Github Enterprise Server. Enter your Github subdomain. For example, if your host URL is `https://github.example-organisation.com`, the subdomain is `github.example-organisation.com`.
      
   8. Click **Connect**. Workato redirects you to GitHub. The OAuth App requests authorization to access your GitHub account.
      
   
   #### GitHub App authentication
   
   You must first [register the app](#register-your-github-app) in your GitHub account and retrieve the credentials to connect to GitHub using a GitHub App.
   
   ![GitHub app auth](/assets/github-app-view.CmRUHryh.png)_Select Authentication type as GitHub app and collect details from your GitHub App!_
   
   ##### Register your GitHub app
   
   View step to register your GitHub App
   
   Complete the following steps to register your GitHub App and retrieve the credentials required to connect it to Workato:
   
   1. Complete the [steps](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) in the GitHub documentation to register your GitHub App.
      
   2. Retrieve your **GitHub App ID** in the **General** settings page of your GitHub app.
      
      ![app id](/assets/github-app-app-id.hjpO7iTw.png)_Save this App ID and place it into your connection_
      
   3. Generate a **Private key** on the same page. GitHub automatically downloads this `.pem` file to your machine.
      
      ![Generate private key](/assets/github-app-private-key.Dqjm0LL8.png)_Generate the private key_
      
   4. Open the `.pem` file in a text editor. The file should look similar to the following:
      
      ```
      -----BEGIN RSA PRIVATE KEY-----
      MIIEpAIBAAKCAQEAyL/wuiSaWoH0pyf366G5E7dbzzmON1qMMrWvls8RtZtgOLjb
      FBxj6gO2aUfoGbMCMqOYRV6xCn6tK118sGYMd5U/kCFu3IRPr/2GoEtcrf0TecQG
      ON+27ijH0Vpn62o8NzGejdy0AWujrtAl6F8xGZeze0PzrGvW6h/GnAdZO1gJnp8t
      wmEqEMXqAsPOQ0hkY+r+pE8RKQVsJCe+PIanBKp7RKWDi9usPFZQdQ==
      -----END RSA PRIVATE KEY-----
      ```
      
   5. Copy the entire private key, including the `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`. Use this private key when you set up the connection in Workato.
      
   6. Retrieve your **Installation ID** from the organization or user where you installed your GitHub App:
      
      - Users accounts: Go to **Settings > Applications > Your GitHub App > Configure**.
      - Organizations: Go to your organization's GitHub homepage. Click **Settings > Installed GitHub Apps > Configure**.
      
      The installation ID appears in the URL. For example, if the URL is `https://github.com/settings/installations/13876669`, the installation ID is `13876669`.
      
   7. Save the installation ID. Enter this ID when creating the GitHub App connection in Workato.
      
   
   ##### Configure GitHub app authentication
   
   View steps to authenticate your GitHub app
   
   1. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
      
   2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   3. Use the **Authentication type** drop-down menu and select **GitHub App**.
      
   4. Enter your **GitHub App ID**.
      
   5. Enter your **Github App Private key**.
      
   6. Enter your **Installation ID**.
      
   7. Optional. Click **Advanced configuration** to display the **Host name** field.
      
   8. Optional. Enter a **Host name** if using GitHub Enterprise Server. Use your GitHub subdomain. For example, if your host URL is `https://github.example-organisation.com`, the subdomain is `github.example-organisation.com`.
      
   9. Optional. Enter a **Custom OAuth profile**. This selection ensures that all requests to the app use the specified profile.
      
   10. Click **Connect**.
       
   
   #### Personal access token authentication
   
   Retrieve your personal access token from GitHub to connect your GitHub account to Workato using a personal access token:
   
   View steps to retrieve your GitHub personal access token
   
   1. Go to **Github account > Settings > Developer settings > Personal access tokens > Generate new token**.
      
   2. Click **Generate new token**.
      
   3. Copy the token. Enter this token in Workato to authenticate the connection.
      
   
   #### Complete setup in Workato
   
   View Complete setup in Workato steps
   
   Complete the following steps to set up your GitHub connection using a personal access token:
   
   1. Sign in to your Workato account and go to the project where you plan to add your GitHub connection.
      
   2. Click **Create > Connection** (or press C twice), then select **GitHub** as your connection.
      
   3. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu and select **Personal Access Token**.
      
   6. Optional. Click **Advanced configuration** to display the **Host name** field.
      
   7. Optional. Enter a **Host name**. This is applicable when using Github Enterprise Server. Enter your Github subdomain. For example, if your host URL is `https://github.example-organisation.com`, your subdomain is `github.example-organisation.com`.
      
   8. Enter your **Personal Access Token**.
      
   9. Optional. Enter a **Custom OAuth profile**. This ensures all requests to the app use the specified profile.
      
   10. Click **Connect**.
       
   
3. Create a GitHub fetch file tool.
   
   ### Create a GitHub skill
   
   This section provides steps to create and configure a GitHub fetch image skill that you can add to an MCP server.
   
   Create a skill and set up the trigger.
   
   #### Create a skill and set up the trigger
   
   This step creates a skill with a trigger that defines how the MCP server calls your recipe and what parameters it expects.
   
   Complete the following steps to create the skill and configure the trigger:
   
   1. Go to **Projects** and click **Create > Skill**.
      
   2. Enter a name for the skill in the **Skill name** field.
      
   3. Use the **Location** drop-down menu to select the project where you plan to store the skill.
      
   4. Click **Start building**.
      
   5. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
      
   6. Enter the following description for your skill workflow in the **When should this skill run?** field. This description helps the LLM recognize when to fetch a file from a GitHub repository versus when a user asks a general question.
      
      ```plaintext
      Fetch a file (such as PNG, JPG, SVG, or other binary/text file) from a GitHub repository. Returns the file contents (base64-encoded for binary files) along with metadata like size, encoding, and download URL.
      ```
      
      ![Enter a description for the skill](/assets/github-mcp-app-trigger.BIFm4VxM.png)_Enter a description for the skill_
      
   7. Go to the **What inputs does this skill need to run?** section and click **Use JSON**.
      
   8. Copy and paste the following JSON schema to provide a description of the schema recipe parameters:
      
      ```json
      [
        {
          "name": "owner",
          "type": "string",
          "optional": false,
          "control_type": "text",
          "hint": "Repository owner (user or organization), such as 'octocat'"
        },
        {
          "name": "repo",
          "type": "string",
          "optional": false,
          "control_type": "text",
          "hint": "Repository name, such as 'Hello-World'"
        },
        {
          "name": "path",
          "type": "string",
          "optional": false,
          "control_type": "text",
          "hint": "File path within the repository, such as 'images/logo.png'"
        },
        {
          "name": "ref",
          "type": "string",
          "optional": true,
          "control_type": "text",
          "hint": "Optional branch name, tag, or commit SHA. Defaults to the repository's default branch."
        }
      ]
      ```
      
   9. Go to the **What information does this skill send back?** section and click **Use JSON**.
      
   10. Copy and paste the following JSON schema to define the skill output:
       
       ```json
       [
         {
           "name": "name",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "path",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "sha",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "size",
           "type": "integer",
           "optional": true,
           "control_type": "number"
         },
         {
           "name": "type",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "encoding",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "content",
           "type": "string",
           "optional": true,
           "control_type": "text",
           "hint": "File contents. Base64-encoded for binary files (PNG/JPG/SVG/etc.)."
         },
         {
           "name": "download_url",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "html_url",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "git_url",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "url",
           "type": "string",
           "optional": true,
           "control_type": "text"
         },
         {
           "name": "error",
           "type": "string",
           "optional": true,
           "control_type": "text"
         }
       ]
       ```
       
   11. Click **Save**.
       
   
   Create a GitHub fetch image action.
   
   #### Create a GitHub fetch image action
   
   This step queries your GitHub repo and returns the image contents.
   
   Complete the following steps to create the GitHub action:
   
   1. Click **\+ Add step** and select **Action in app**.
      
      ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Action in app**_
      
   2. Search for `GitHub` and select it as your app.
      
   3. Select **Custom action**.
      
      > **DON'T USE GUIDED SETUP**
      > 
      > The steps in this use case don't use the guided setup option. Steps for guided setup vary from the steps provided in this use case.
      
   4. Enter a name in the **Action name** field. For example: `Get repository image contents`.
      
      ![Set up the action](/assets/get-github-files.CInuq4QG.png)_Set up the action_
      
   5. Use the **Method** drop-down menu to select **GET**.
      
   6. Go to the **Path** field and switch to formula mode.
      
   7. Copy and paste the following formula into the **Path** field, replacing each datapill placeholder, such as `<RefStep 1 datapill>`, `<OwnerStep 1 datapill>`, `<RepoStep 1 datapill>`, and `<PathStep 1 datapill>`, by mapping the corresponding datapill from the **RECIPE DATA** panel:
      
      ```
      <RefStep 1 datapill>.present? ? '/repos/' + <OwnerStep 1 datapill> + '/' + <RepoStep 1 datapill> + '/contents/' + <PathStep 1 datapill> + '?ref=' + <RefStep 1 datapill> : '/repos/' + <OwnerStep 1 datapill> + '/' + <RepoStep 1 datapill> + '/contents/' + <PathStep 1 datapill>
      ```
      
      The resulting formula should look like this:
      
      ![Path formula](/assets/path-formula.DRyqZU0p.png)_**Path** formula_
      
   8. Ensure that **Response type** is set to **JSON response**.
      
   9. Expand the **Request headers** section and click **Add header**.
      
   10. Enter `Accept` in the **Name** field and `application/vnd.github+json` in the **Value** field.
       
   11. Go to the **Response body** section and click **Use JSON**.
       
   12. Copy and paste the following schema into the field:
       
       ```json
       [
         {
           "control_type": "text",
           "name": "name",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "path",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "sha",
           "type": "string"
         },
         {
           "control_type": "integer",
           "name": "size",
           "type": "integer"
         },
         {
           "control_type": "text",
           "name": "type",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "encoding",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "content",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "download_url",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "html_url",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "git_url",
           "type": "string"
         },
         {
           "control_type": "text",
           "name": "url",
           "type": "string"
         }
       ]
       ```
       
   13. Click **Save**.
       
   
   Configure the RETURN response.
   
   #### Configure the RETURN response
   
   This step defines the response the skill returns.
   
   Complete the following steps to configure the RETURN response:
   
   1. Click the **RETURN response** step in the recipe editor.
      
   2. Map the Name (Step 2) datapill to the **Name** field.
      
      ![Map the corresponding datapills for the RETURN response](/assets/return-response.DMZDDg67.png)_Map the corresponding datapills for the **RETURN response**_
      
   3. Map the Path (Step 2) datapill to the **Path** field.
      
   4. Map the Sha (Step 2) datapill to the **Sha** field.
      
   5. Map the Size (Step 2) datapill to the **Size** field.
      
   6. Map the Type (Step 2) datapill to the **Type** field.
      
   7. Map the Encoding (Step 2) datapill to the **Encoding** field.
      
   8. Map the Content (Step 2) datapill to the **Content** field.
      
   9. Map the Download URL (Step 2) datapill to the **Download URL** field.
      
   10. Map the Html URL (Step 2) datapill to the **Html URL** field.
       
   11. Map the Git URL (Step 2) datapill to the **Git URL** field.
       
   12. Map the URL (Step 2) datapill to the **URL** field.
       
   13. Click **Save**.
       
   
4. Go to **AI Hub > Enterprise MCP > Custom servers** and click **\+ Create an MCP server**.
   
5. Create an MCP server.
   
   ### Create an MCP server
   
   This step creates a MCP server and adds your skill to it. Skills you add to the MCP server become tools you can use in your LLM.
   
   Complete the following steps to create an MCP server:
   
   1. Go to the **Start from scratch** section and click **New MCP server**. Refer to [GitHub MCP server](/en/mcp/prebuilt-mcps/github-mcp-server#github-mcp-server) if you plan to use the GitHub prebuilt MCP server template.
      
   2. Select **Project assets** as your tool source.
      
   3. Use the **Project** drop-down menu to select the project where you plan to store the MCP server.
      
   4. Select the tool you built in the preceding steps.
      
      ![Select the tool you built in the preceding steps](/assets/create-mcp-server.DbeCUlzi.png)_Select the tool you built in the preceding steps_
      
   5. Enter a name for your MCP server in the **Server name** field.
      
   6. Optional. Enter instructions for the LLM to understand the purpose and goals for the MCP server in the **Server instruction** field.
      
   7. Click **Start building**. The MCP server tools, description, remote MCP URL, and additional server information displays in the **Details** tab.
      
   
6. Create an MCP app.
   
   ### Create an MCP app
   
   This steps creates an MCP app for your GitHub fetch image tool that enables it render images from your GitHub repo. You can pan and zoom images directly in an LLM chat.
   
   Complete the following steps to create MCP app for your GitHub tool:
   
   1. Go to **AI Hub > Enterprise MCP > Custom servers**.
      
   2. Select the MCP server where you plan to add an MCP app.
      
   3. Go to the **Server capabilities** section and select the **Apps** tab.
      
      ![Select the Apps tab](/assets/apps-tab.CqJQhYA6.png)_Select the **Apps** tab_
      
   4. Click **\+ Add App**.
      
   5. Enter a name for the MCP app in the **Name** field.
      
      ![Configure the MCP app](/assets/add-app.DmyxbEaE.png)_Configure the MCP app_
      
   6. Use the **Linked tool** drop-down menu to select the tool you created in the preceding steps.
      
   7. Expand the **Content security policy** section to select the following external content and resources the MCP app is allowed to access:
      
      1. Go to the **Connect domains** section and add the following domains:
         
         - `https://api.github.com`
         - `https://*.githubusercontent.com`
      2. Go to the **Resource domains** section and add the following domains:
         
         - `https://cdn.jsdelivr.net`
         - `raw.githubusercontent.com`
         - `https://*.githubusercontent.com`
      3. Go to the **Frame domains** section and add the following domains:
         
         \-`https://github.com`
         
   8. Select **Start from scratch**.
      
      ![Select Start from scratch](/assets/start-building-options.BFRi-y2w.png)_Select **Start from scratch**_
      
   9. Copy and paste the following code into the code editor:
      
      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <style>
          body { margin: 0; font-family: system-ui, sans-serif; background: #0d1117; }
          #status { padding: 8px 12px; color: #8b949e; font-size: 13px; word-break: break-all; }
          #viewport {
            overflow: hidden;
            width: 100%;
            height: 80vh;
            min-height: 420px;
            background: #0d1117;
            cursor: grab;
            touch-action: none;
            position: relative;
          }
          #viewport.grabbing { cursor: grabbing; }
          #img {
            max-width: 100%;
            display: block;
            transform-origin: 0 0;
            user-select: none;
            -webkit-user-drag: none;
          }
          .controls {
            position: absolute; top: 8px; right: 8px; z-index: 2;
            display: flex; gap: 6px;
          }
          .controls button {
            background: #21262d; color: #c9d1d9; border: 1px solid #30363d;
            border-radius: 6px; padding: 6px 10px; cursor: pointer; font-size: 13px;
            min-width: 34px;
          }
          .controls button:hover { background: #30363d; }
        </style>
      </head>
      <body>
        <div id="status">Connecting…</div>
        <div id="viewport">
          <div class="controls">
            <button id="zoomout" title="Zoom out">−</button>
            <button id="zoomin" title="Zoom in">+</button>
            <button id="reset">Reset</button>
            <button id="expand">⤢ Expand</button>
          </div>
          <img id="img" alt="" draggable="false" />
        </div>
      
        <script type="module">
          import { App } from 'https://cdn.jsdelivr.net/npm/@modelcontextprotocol/ext-apps@1.3.1/dist/src/app-with-deps.js';
      
          const app = new App({ name: 'GitHub Image Viewer', version: '1.0.0' });
      
          // NOTE: this host does not send the `ui/notifications/tool-input`
          // notification (it's optional in the MCP Apps spec), so `ontoolinput`
          // never fires here reliably. `ontoolresult` DOES fire — but it can
          // fire more than once per turn, e.g. if the model made an earlier
          // exploratory call (like reading README.md) before the actual image
          // fetch. So we don't latch onto the *first* result — we inspect every
          // result that arrives and only render the ones that actually look
          // like image data. Non-image results still update our "last known
          // context" (owner/repo/path), which we use as a fallback if nothing
          // image-shaped ever arrives on its own.
          const TOOL_NAME = 'GitHub_Fetch_File';   // verify exact name in AI Hub > Tools
      
          let lastContext = {};
          let imageRendered = false;
      
          function mimeFromPath(p) {
            const ext = (p.split('.').pop() || '').toLowerCase();
            return ({
              png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg',
              gif: 'image/gif', webp: 'image/webp', svg: 'image/svg+xml',
              bmp: 'image/bmp', ico: 'image/x-icon'
            })[ext] || 'application/octet-stream';
          }
      
          function isImageData(data) {
            const p = data?.path || data?.download_url || data?.name || '';
            return mimeFromPath(p).startsWith('image/');
          }
      
          function extractData(raw) {
            let parsed = raw && raw.structuredContent;
            if (!parsed) {
              const text = raw?.content?.[0]?.text;
              try { parsed = text ? JSON.parse(text) : raw; } catch { parsed = raw; }
            }
            return parsed?.result ? parsed.result : parsed;
          }
      
          function renderImage(data, fallbackPath) {
            if (data?.download_url) {
              img.src = data.download_url;
              return true;
            }
            if (data?.content && data?.encoding === 'base64') {
              const clean = data.content.replace(/\s/g, '');
              img.src = `data:${mimeFromPath(data.path || fallbackPath || '')};base64,${clean}`;
              return true;
            }
            return false;
          }
      
          app.ontoolinput = (params) => {
            Object.assign(lastContext, params?.arguments || {});
          };
      
          app.ontoolresult = (result) => {
            const data = extractData(result);
            if (!data) return;
            if (data.error) {
              status.textContent = 'Tool error: ' + (typeof data.error === 'string' ? data.error : JSON.stringify(data.error));
              return;
            }
            // Remember context even from non-image results (e.g. an earlier lookup).
            if (data.owner) lastContext.owner = data.owner;
            if (data.repo) lastContext.repo = data.repo;
            if (data.path) lastContext.path = data.path;
            if (data.ref) lastContext.ref = data.ref;
      
            if (isImageData(data)) {
              imageRendered = renderImage(data, data.path);
            }
          };
      
          const status = document.getElementById('status');
          const vp = document.getElementById('viewport');
          const img = document.getElementById('img');
      
          img.addEventListener('error', () => {
            status.textContent = 'Image failed to load: ' + (img.src || '(empty src)');
          });
          img.addEventListener('load', () => {
            status.textContent = `Image loaded ✓ (${img.naturalWidth}×${img.naturalHeight})`;
          });
      
          async function callTool(name, args) {
            const raw = await app.callServerTool({ name, arguments: args });
            return extractData(raw);
          }
      
          await app.connect();
      
          // Give the host a few seconds to deliver an actual image result via
          // ontoolresult on its own. If nothing image-shaped has shown up yet,
          // but we've picked up enough context (owner/repo/path) from whatever
          // did arrive, make an explicit fetch call ourselves as a fallback.
          setTimeout(async () => {
            if (imageRendered) return;
            const FILE = {
              owner: lastContext.owner,
              repo: lastContext.repo,
              path: lastContext.path,
              ref: lastContext.ref || 'main'
            };
            if (!FILE.owner || !FILE.repo || !FILE.path) {
              status.textContent = 'Waiting for image data. Last known context: ' + JSON.stringify(lastContext);
              return;
            }
            try {
              const data = await callTool(TOOL_NAME, FILE);
              if (data?.error) {
                status.textContent = 'Tool error: ' + (typeof data.error === 'string' ? data.error : JSON.stringify(data.error));
              } else if (!renderImage(data, FILE.path)) {
                status.textContent = 'No image data returned. Keys: ' + Object.keys(data || {}).join(', ');
              }
            } catch (e) {
              status.textContent = 'Error: ' + e.message;
            }
          }, 4000);
      
          // ---- Pan / zoom state ----
          let scale = 1, x = 0, y = 0, dragging = false, sx = 0, sy = 0;
          const MIN = 0.2, MAX = 10;
          const apply = () => { img.style.transform = `translate(${x}px,${y}px) scale(${scale})`; };
      
          // Zoom toward a point (cx, cy) in viewport coordinates so the content
          // under the cursor / center stays put. Buttons pass the viewport center.
          function zoomAt(factor, cx, cy) {
            const newScale = Math.min(Math.max(scale * factor, MIN), MAX);
            const ratio = newScale / scale;
            x = cx - (cx - x) * ratio;
            y = cy - (cy - y) * ratio;
            scale = newScale;
            apply();
          }
      
          function zoomCenter(factor) {
            const r = vp.getBoundingClientRect();
            zoomAt(factor, r.width / 2, r.height / 2);
          }
      
          // Wheel zoom toward the cursor.
          vp.addEventListener('wheel', e => {
            e.preventDefault();
            const r = vp.getBoundingClientRect();
            zoomAt(e.deltaY < 0 ? 1.1 : 0.9, e.clientX - r.left, e.clientY - r.top);
          }, { passive: false });
      
          // Drag to pan.
          vp.addEventListener('pointerdown', e => {
            if (e.target.tagName === 'BUTTON') return;
            dragging = true; sx = e.clientX - x; sy = e.clientY - y;
            vp.classList.add('grabbing'); vp.setPointerCapture(e.pointerId);
          });
          vp.addEventListener('pointerup', () => { dragging = false; vp.classList.remove('grabbing'); });
          vp.addEventListener('pointermove', e => {
            if (!dragging) return;
            x = e.clientX - sx; y = e.clientY - sy; apply();
          });
      
          // ---- Controls ----
          document.getElementById('zoomin').addEventListener('click', () => zoomCenter(1.25));
          document.getElementById('zoomout').addEventListener('click', () => zoomCenter(0.8));
          document.getElementById('reset').addEventListener('click', () => {
            scale = 1; x = 0; y = 0; apply();
          });
          let expanded = false;
          document.getElementById('expand').addEventListener('click', () => {
            expanded = !expanded;
            vp.style.height = expanded ? '100vh' : '80vh';
          });
        </script>
      </body>
      </html>
      ```
      
   10. Click **Save**.
       
   
7. Go to the LLM where you plan to create an MCP integration and complete the following configuration steps:
   
   Configure your MCP integration for ChatGPT.
   
   ### ChatGPT MCP configuration
   
   This step configures a new MCP server connector in your OpenAI account.
   
   1. Go to your ChatGPT account.
      
   2. Go to **Settings > Apps & Connectors > Advanced settings** and enable the **Developer mode** toggle.
      
   3. Go to **Settings > Apps & Connectors**.
      
   4. Click **Create**. This button is only visible when the **Developer mode** toggle is enabled.
      
   5. Enter a name for your MCP connector in the **Name** field.
      
      ![ChatGPT connector](/assets/chatgpt-connector.B98_tSbx.png)_Configure your ChatGPT MCP connector_
      
   6. Paste your MCP URL and token in the **URL field**.
      
   7. Optional. Enter a description in the **Description** field.
      
   8. Use the **Authentication** drop-down menu to select **No Auth**.
      
   9. Select the checkbox to accept the risk of adding a custom MCP server.
      
   10. Click **Create**.
       
   11. Create a new chat in ChatGPT to use your MCP tools.
       
   
   Configure your MCP integration for Claude.
   
   ### Claude MCP configuration
   
   This step configures a new MCP server connector in your Anthropic account.
   
   1. Go to **Settings > Connectors**.
      
   2. Click **\+ Add new connector**.
      
   3. Enter a name for your MCP connector in the **Name** field.
      
      ![Claude connector](/assets/claude-mcp-setup.CLtAsbY0.png)_Configure your Claude MCP connector_
      
   4. Paste your MCP URL and token into the **Remote MCP server URL** field.
      
   5. Click **Add**. The newly created MCP connector appears in the list of connectors.
      
   6. Click **Configure**.
      
   7. Use the permissions drop-down menu to select **Always ask permission** or **Allow unsupervised**. **Always ask permission** is selected by default.
      
   8. Create a new chat in Claude to use your MCP tools.
      
   
   Configure your MCP integration for Cursor.
   
   ### Cursor MCP configuration
   
   This step configures a new MCP server connector in your Cursor account.
   
   1. Go to **Settings > Cursor settings**.
      
   2. Click **MCP & Integrations** in the sidebar.
      
   3. Click **\+ New MCP Server** to open the `mcp.json` file.
      
      ![New MCP server](/assets/configure-cursor.DhhCFK4N.png)_Click **\+ New MCP Server**_
      
   4. Update the configuration to use the MCP URL and token you copied in the preceding steps. For example:
      
      ```json
      
      {
        "mcpServers": {
          "snowflake-tools": {
            "url": "https://2255.apim.mcp.workato.com?wkt_token=YOUR_API_TOKEN"
          },
          "github-tools": {
            "url": "https://387.apim.mcp.workato.com/abc247/example-collection-name-v1?wkt_token=YOUR_API_TOKEN"
          }
        }
      }
      ```
      
   5. Save your changes.
      
   6. Create a new chat with your Cursor agent to use your MCP tools.
      
      You must start a new chat with your agent. Cursor agents only have access to the tools and capabilities available when a chat begins. Agents can't detect or use new MCP configurations, servers, or tools added after starting a chat.
      
   
   8
   
   Test your MCP tool in your LLM.
   
   ![Cursor example chat](/assets/github-image-mcp-app.Dzdnq2mg.gif)_Cursor example chat_
   
8. Test your MCP tool in your LLM.
   
   ![Cursor example chat](/assets/github-image-mcp-app.Dzdnq2mg.gif)_Cursor example chat_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/data-tables/data-tables-use-cases.md
description: >-
  Explore Data tables use cases with step-by-step guides for building data
  tables that integrate and enhance your workflows.
---

# Data tables use cases

Data tables enable you to store data from chargeable APIs from third-party systems that are frequently referenced in recipes, workflow apps data, or conversation IDs from Agent Studio genies.

Data tables use cases provide steps on how to perform the following actions:

- Create a data table
- Add columns
- Integrate the data table with a recipe
- Use data tables in skills

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Modifications, such as triggers, actions, data table columns, and skills may require adjustments for your specific setup.

### [Store agent conversation IDs to create a persistent memory for an agent](https://docs.workato.com/en/getting-started/use-cases/data-tables/store-agent-conversation-ids-in-a-data-table)

This use case enables you to [create a data table to store agent conversation IDs](https://docs.workato.com/en/getting-started/use-cases/data-tables/store-agent-conversation-ids-in-a-data-table) to allow an agent to continue a conversation with context.

## More resources

- [Learn key concepts](/en/workato-concepts)
- [Data tables](/en/data-tables)
- [Data tables permissions](/en/data-tables/data-table-permissions)
- [Create your first genie](/en/agentic/agent-studio/genies-configuration#create-your-first-genie)
- [Getting started with skills](/en/agentic/skills#getting-started-with-skills)

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/data-tables/store-agent-conversation-ids-in-a-data-table.md
description: >-
  Use a Workato data table to store genie conversation IDs so your genie
  remembers previous messages from each user.
---

# Build a data table to store genie conversation IDs

This use case shows how to use a [data table](/en/data-tables) as persistent memory for a genie. Each task assigned to a genie starts a new conversation by default. Your genie needs a way to match each user to their existing genie conversation and retain context when it receives messages from multiple users through an interface, such as Telegram.

This use case demonstrates how a data table stores a mapping between each Telegram user ID and the genie's conversation ID. The recipe looks up the sender in the data table before each task and, if a record exists, continues the same conversation. The recipe upserts the conversation ID back into the table after each task.

You can add skills that use this conversation memory to your genies to carry out tasks that span multiple messages, such as scheduling a calendar event from a conversation about an upcoming appointment.

## What does this genie do?

This genie receives Telegram messages through a Workato recipe and uses a data table to store conversation IDs to match users to conversations and retain context.

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph T[&nbsp Create a <br/> data table &nbsp]
      direction LR
    end
    subgraph TT[Add columns for <br/> Telegram ID and <br/> genie conversation ID]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[&nbsp Create a <br/> Telegram recipe &nbsp]
        direction LR
    end
    subgraph RRR[Connect your <br/> Telegram bot and genie]
        direction LR
    end
  end
  subgraph N[" "]
    direction LR
    subgraph O[&nbsp Search and upsert <br/> data table records &nbsp]
        direction LR
    end
    subgraph OO[Look up the sender's <br/> conversation ID before the task <br/> and save it after the task]
        direction LR
    end
  end

  A([Build a genie <br/> with memory]) -- Create your data table --> M -- Create a <br/> Telegram recipe --> Q -- Add data table actions --> N --> B([Genie continues <br/> each user's conversation])
  T --> TT
  O --> OO
  RR --> RRR
  classDef default fill:#fff,stroke:#67eadd,stroke-width:2px;
  classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef WorkatoPurple fill:#fff,stroke:#a99ff5,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#67eadd,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashPurple fill:#a99ff5,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashBlue fill:#5159f6,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
  classDef SubgraphLight stroke:#68eade,stroke-width:2px
  class A,B WorkatoTeal
  class O,OO SubgraphDash
  class T,TT SubgraphDashPurple
  class N SubgraphLight
  class RR,RRR SubgraphDashBlue
  class M WorkatoPurple
  class Q WorkatoBlue
```

## Why use a data table for conversation IDs?

Data tables are a good fit for this scenario for the following reasons:

- **Persistence across recipe jobs**: Each recipe job runs independently. A data table retains the conversation ID after the job ends, so the next message from the same user can pick up where the last message left off.
- **Fast lookups by key**: The recipe searches the table by a single `telegram-id` column.
- **No external database to maintain**: Data tables are scalable and secure, so you don't need to provision or manage separate storage.
- **Easy to inspect and edit**: You can open the table in the **Data tables** interface to view stored conversation IDs or delete a record to reset a user's conversation.

> **DATA TABLE LIMITATIONS**
> 
> Data tables aren't designed to store sensitive PCI data, such as credit card numbers, or to function as large relational databases. This use case stores only user IDs and conversation IDs. Don't use data tables to store the contents of sensitive conversations.

## Build your genie with a conversation ID data table

Complete the following steps to create a Telegram-based genie that uses a data table to maintain conversation context for each user:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Modifications, such as triggers, actions, data table columns, or connection permissions may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Create a data table to store conversation IDs.
   
   ### Create a data table to store conversation IDs
   
   This step creates a data table that persists the genie's conversation ID against each Telegram user's ID. This allows the genie to retain context across multiple messages from the same user.
   
   > **FIRST-TIME USERS**
   > 
   > The first time a user messages your Telegram bot, the **Search records** action doesn't return records because the user doesn't have a conversation ID yet. Leave the genie's conversation ID empty so the genie starts a new conversation. The upsert step in the next section saves the new conversation ID for future messages.
   
   1. Go to the project where you plan to store your data table and click **Create > Data table** or press C+T.
      
   2. Enter a name for your data table in the **Data table name** field. For example: `Telegram genie conversations`.
      
   3. Use the **Location** drop-down menu to select a location for your data table.
      
   4. Click **Start building**.
      
   5. Add a column with the label `telegram-id` to store the Telegram user's sender ID.
      
   6. Add a second column with the label `genie-conversation-id` to store the genie's conversation ID.
      
      ![Add columns to your data table](/assets/create-a-data-table.MXv1Z3Y8.png)_Add columns to your data table_
      
   7. Click **Save**.
      
   
3. Set up your Telegram bot.
   
   ### Set up your Telegram bot
   
   This step creates a new Telegram bot and retrieves the API token needed to connect it to Workato.
   
   1. Sign in to your Telegram app and search for the **@BotFather** account.
      
   2. Start a conversation with **@BotFather** and enter the `/newbot` command.
      
      ![Create a new Telegram bot](/assets/create-telegram-bot.z3bFUQV5.png)_Create a new Telegram bot_
      
   3. Enter a human-readable name for your Telegram bot when prompted. For example: `Workato PA genie`.
      
   4. Enter a unique username that ends with `bot` when prompted. For example: `workato_bot`.
      
   5. Copy the secret API token that **@BotFather** provides in the confirmation message. You must use this token to connect your Telegram bot to Workato.
      
   
4. Create a Telegram connection.
   
   ### Create a Telegram connection
   
   This step installs the Telegram community connector and creates a connection between Workato and your Telegram bot.
   
   1. Sign in to your Workato account.
      
   2. Go to **Community Library > Custom Connectors**.
      
   3. Search for `Telegram` and select it as your app.
      
   4. Click **Install**.
      
      ![Install the Telegram community connector](/assets/install-telegram-community-connector.CnGRAEgg.gif)_Install the Telegram community connector_
      
   5. Enter a name for your connection in the **Name** field.
      
   6. Use the **Save connection in** drop-down menu to select a location for your connection.
      
   7. Enter the API token you received from **@BotFather** in the **API token** field.
      
   8. Click **Connect**.
      
   
5. Set up a recipe to process incoming Telegram messages.
   
   ### Set up a recipe to process incoming Telegram messages
   
   This step ensures that messages sent to your Telegram bot reach Workato and are processed correctly.
   
   1. Go to the project where you plan to store your recipe and click **Create > Recipe** or press C+R.
      
   2. Enter a name for your recipe in the **Name** field and use the **Save recipe in** drop-down menu to select a project location.
      
   3. Click **Pick a starting point > Select an app**.
      
   4. Search for `Telegram` and select it as your app.
      
   5. Select the **New Event** trigger and connect using the Telegram connection you created in the preceding steps.
      
   6. Click **\+ Add step** and search for and select `Telegram`.
      
      ![Set up your Telegram Send message action](/assets/telegram-send-message-action.AHCnUhxi.gif)_Set up your Telegram **Send message** action_
      
   7. Select the **Send message** action.
      
   8. Map the Telegram Message > Chat ID (Step 1) datapill to the **Chat ID** field.
      
   9. Enter `Message received` in the **Message to send** field.
      
   10. Optional. Click **Test recipe** and send a message to your Telegram bot. Your recipe is configured correctly if you receive a reply.
       
   
6. Add a genie to the recipe.
   
   ### Add a genie to the recipe
   
   This step creates a genie that processes incoming Telegram messages and replies to the user.
   
   1. Go to the project where you plan to store your genie and click **Create > Genie**, or press C+G.
      
   2. Enter a request or goal for your genie in the **What would you like your genie to help with?** field. For example:
      
      ```plaintext
      You are a personal assistant who responds to users' messages. If the message contains
      information about an upcoming event, you can create a calendar event for the user
      with the given information.
      ```
      
   3. Use the **Save genie in** drop-down menu to select a location for your genie.
      
      ![Create a new genie](/assets/telegram-pa-genie.ChI4azAY.png)_Create a new genie_
      
   4. Click **Start building**. The genie **Build** page displays with the **Job description** automatically generated based on the input you provided. You can edit this to suit your requirements.
      
   5. Return to the recipe editor and click **\+ Add step** _before_ the Telegram Send Message action step.
      
      ![Click + Add step before the Telegram Send Message action step](/assets/assign-task-to-genie.7yTLCF8p.gif)_Click **\+ Add step** _before_ the Telegram Send Message action step_
      
   6. Select **Action in app**, search for `Workato Genie`, and select it as your app.
      
   7. Select the **Assign task to genie** action.
      
   8. Use the **Genie** drop-down menu to select the genie you created in the preceding steps.
      
   9. Enter a description that instructs the genie to process the incoming message in the **Task Description** field.
      
   10. Map the Telegram trigger Text (Step 1) datapill after your description in the **Task Description** field.
       
       ![Configure the Task Description field](/assets/genie-task-description.DGPRTrDw.png)_Configure the **Task Description** field_
       
   11. Click **Save**.
       
   
7. Look up the sender's conversation ID in the data table.
   
   ### Look up the sender's conversation ID in the data table
   
   This step adds a Workato Data tables **Search records** action that checks whether the sender's Telegram ID has a corresponding conversation ID in the data table. An existing conversation ID indicates a previous conversation that the genie can continue.
   
   > **FIRST-TIME USERS**
   > 
   > The first time a user messages your Telegram bot, the **Search records** action doesn't return records because the user doesn't have a conversation ID yet. Leave the genie's conversation ID empty so the genie starts a new conversation. The upsert step in the next section saves the new conversation ID for future messages.
   
   1. Return to the recipe editor and click **\+ Add step** _before_ the **Assign task to genie** action step.
      
   2. Select **Action in app**, search for `Workato Data Tables`, and select it as your app.
      
   3. Select the **Search records** action.
      
   4. Use the **Data table** drop-down menu to select the data table you created in the preceding steps.
      
   5. Go to the **Filter** section and click **Add filter**.
      
   6. Use the **Column name** drop-down menu to select **telegram-id**.
      
   7. Use the **Operand** drop-down menu to select **equals**.
      
   8. Map the Telegram ID (Step 1) datapill to the **Value** field. This datapill is located under **Telegram > Message > From**.
      
      ![Configure the data table to search Telegram](/assets/telegram-data-table-configuration.BvJOfw8t.gif)_Configure the data table to search Telegram_
      
   9. Click **Save**.
      
   
8. Pass the stored conversation ID to the genie.
   
   ### Pass the stored conversation ID to the genie
   
   This step maps the conversation ID returned by the data table search to the **Assign task to genie** action. This is what allows the genie to continue an existing conversation instead of starting a new one.
   
   1. Click the **Assign task to genie** step in the recipe editor.
      
   2. Go to the **Conversation ID** field.
      
   3. Map the Workato Data tables genie-conversation-id (Step 2) datapill from the **Search records** step to the **Conversation ID** field. Use the first record in the search results.
      
   4. Click **Save**.
      
   
9. Save the conversation ID to the data table.
   
   ### Save the conversation ID to the data table
   
   This step adds a Workato Data tables **Upsert record** action that saves the conversation ID returned by the genie. The action creates a record for new users and updates the record for returning users.
   
   1. Click **\+ Add step** _after_ the **Assign task to genie** action step.
      
   2. Select **Action in app**, search for `Workato Data Tables`, and select it as your app.
      
   3. Select the **Upsert record** action.
      
   4. Use the **Data table** drop-down menu to select the data table you created in the preceding steps.
      
      ![Configure the Upsert record action](/assets/upsert-record-action.B59Jf31_.gif)_Configure the **Upsert record** action_
      
   5. Use the **Primary key** drop-down menu to select **telegram-id**.
      
   6. Go to the **Record fields** section and map the Telegram From ID (Step 1) datapill to the **telegram-id** field.
      
   7. Map the Workato Genie Conversation ID (Step 3) datapill to the **genie-conversation-id** field.
      
   8. Click **Save**.
      
   
10. Test your genie's memory.
    
    ### Test your genie's memory
    
    This step confirms that the data table is storing conversation IDs and that the genie uses them.
    
    1. Click **Test recipe** and send a message to your Telegram bot. For example: `My dentist appointment is next Tuesday.`
       
    2. Open your data table and confirm that a new record exists with your Telegram ID and a genie conversation ID.
       
    3. Send a follow-up message that depends on the first one. For example: `Actually, make that 4 PM.` The genie should respond with the earlier appointment in mind.
       
    4. Return to your data table and confirm that the same record was updated rather than a duplicate record created.
       
    
11. Optional. Extend your genie with a Google Calendar skill.
    
    ### Extend your genie with a Google Calendar skill
    
    You can give your genie skills that benefit from context with conversation memory in place. This step adds a skill that converts messages into Google Calendar events. Users can refine events across several messages because the genie remembers earlier messages.
    
    #### Create a Google Calendar connection
    
    This step creates a connection between Workato and your Google Calendar account to allow your genie to create calendar events on your behalf.
    
    Refer to the following sections to set up your Google Calendar connection:
    
    ##### OAuth 2.0 authentication
    
    Complete the following steps to set up your Google Calendar connection using OAuth 2.0:
    
    View OAuth 2.0 authentication steps
    
    1. Click **Create > Connection** or press C twice.
       
    2. Search for and select `Google Calendar` as your connection on the **New connection** page.
       
    3. Provide a name for your connection in the **Connection name** field.
       
    4. Select the project where you plan to store the connection from the **Location** drop-down menu.
       
    5. Select **OAuth 2.0** as the **Authentication type**.
       
    6. Click **Sign in with Google**, then sign in to your Google account. Ensure your Google account has sufficient permissions to manage the events and calendars you plan to use in Workato. ![Click Sign in with Google](/assets/google-calendar-sign-in-with-google.DQ57V-DM.png)_Click **Sign in with Google**._
       
    
    ##### Service account authentication
    
    View Service account authentication steps
    
    A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.
    
    Service accounts provide the following benefits:
    
    - **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
    - **Dedicated permissions:** Service accounts can only access projects that you share with them.
    - **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.
    
    Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.
    
    Service account authentication consists of the following actions:
    
    - [Set up a Google service account](#set-up-a-google-service-account)
    - [Enable the Google Calendar API](#api-setup)
    - [Complete setup in Workato](#setup)
    
    ###### Minimum scopes for service account connections
    
    The following scopes are required to connect to Google Calendar using a service account:
    
    - `https://www.googleapis.com/auth/calendar`
    - `https://www.googleapis.com/auth/calendar.events`
    - `https://www.googleapis.com/auth/admin.directory.resource.calendar`
    - `https://www.googleapis.com/auth/tasks`
    - `https://www.googleapis.com/auth/userinfo.email`
    
    A `401 Unauthorized error` may occur when the service account uses the `Owner` role or lacks required scopes. Assign the `Editor` role to the service account in the Google Cloud Console and confirm it includes all required scopes listed above. This ensures the service account can authenticate and access Google Calendar successfully.
    
    Refer to the [Google Calendar API scopes](https://developers.google.com/calendar/api/auth) documentation for a complete list of supported scopes.
    
    ###### Set up a Google service account
    
    View Set up a Google service account steps
    
    Complete the following steps to set up a Google service account:
    
    1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
       
    2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account. ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
       
    3. Click the **Email** of the service account you intend to use. ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
       
    4. Copy the service account's **Email** and save it to configure your connection later. ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
       
    5. Go to the **KEYS** tab.
       
    6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
       
    7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
       
    
    ###### Enable the Google Calendar API
    
    View Enable the Google Calendar API steps
    
    You must enable the Google Calendar API before you return to Workato to finish setting up your connection.
    
    1. Sign in to Google's [API library](https://console.developers.google.com/apis/library).
       
    2. Search for and select the `Google Calendar API`.
       
    3. Click **Enable** to enable the API. ![Enable the Google Calendar API](/assets/google-calendar-api.DMWBkrRb.png)_**Enable** the `Google Calendar API`_
       
    
    ##### Complete setup in Workato
    
    View Workato setup steps
    
    Complete the following steps in Workato to set up your Google Calendar connection using a service account:
    
    1. Click **Create > Connection** or press C twice.
       
    2. Search for and select `Google Calendar` as your connection on the **New connection** page.
       
    3. Provide a name for your connection in the **Connection name** field.
       
    4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
       
    5. Select **Service account** as the **Authentication type**.
       
    6. Enter your service account's **Private key**.
       
    7. Provide the **User email** of the account you plan to impersonate.
       
       User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Calendar. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Calendar. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
       
    8. Click **Sign in with Google** to complete the setup. ![Configure Google Calendar service account connection](/assets/service-account-connection.CG2N5lxI.png)_Configure Google Calendar service account connection_
       
    
    #### Create a skill to convert messages into Google Calendar events
    
    This step creates a custom skill that enables your genie to detect messages that should be converted into Google Calendar events.
    
    1. Go to the **Build** page of the genie you created in the preceding steps.
       
    2. Go to the **Skills** section and click **\+ Add > Skill**.
       
    3. Select **New skill** and click **Create new skill**.
       
       Alternatively, you can create a skill from the **Projects** page by clicking **Create > Skill** or pressing C+S.
       
    4. Provide a name for your skill in the **Name** field. For example: `Create Google Calendar event`.
       
    5. Use the **Location** drop-down menu to select a location for your skill.
       
    6. Click **Start building**. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
       
    7. Select the **Start workflow** trigger.
       
    8. Go to the **What inputs will your genie require to run this skill?** section and click **Add fields manually**. Add the following fields:
       
       | Label | Data type |
       | --- | --- |
       | `event_title` | String |
       | `event_date` | Date |
       | `event_time` | String |
       | `event_description` | String |
       
    9. Go to the **What should be returned to the genie after this skill is run?** section and add the following field:
       
       | Label | Data type |
       | --- | --- |
       | `created_event` | Boolean |
       
       ![Configure inputs and output](/assets/google-calendar-inputs.DRjCBEBv.png)_Configure inputs and output_
       
    10. Click **\+ Add step**, search for `Google Calendar`, and select it as your app.
        
    11. Select the **Create event** action.
        
    12. Map the Start datetime (Step 1) datapill to the **Start date time** field.
        
        ![Configure the Create event action](/assets/create-event-action.D6XicUFp.png)_Configure the **Create event** action_
        
    13. Map the End datetime (Step 1) datapill to the **End date time** field.
        
    14. Map the Event name (Step 1) datapill to the **Name** field.
        
    15. Map the Event description (Step 1) datapill to the **Event description** field.
        
    16. Click **\+ Add step** and select **IF condition** to handle the result of the calendar event creation.
        
    17. Map the Google Calendar ID (Step 2) datapill to the **Data field**.
        
    18. Use the **Condition** drop-down menu to select **is present**.
        
    19. Go to the **Yes** branch and click **Select an app and action**.
        
    20. Search `Workato Genie` and select it as your app.
        
    21. Select **Return response to genie** as your action.
        
    22. Go to the **Results** section and use the **Created Event** drop-down menu to select **Yes**.
        
        ![Set up your IF condition](/assets/if-condition-setup.BsASC_IL.png)_Set up your IF condition_
        
    23. Go to the **No** branch. The **Return response to genie** action should already be present.
        
    24. Click the **Return response to genie** action to open it.
        
    25. Configure the **Yes** and **No** paths of the **IF** block to return the appropriate `created_event` boolean response to the genie.
        
    26. Click **Save**.
        
    
    #### Update your genie task description
    
    This step updates the genie task description to include instructions on how the genie should use the Google Calendar skill.
    
    1. Click the **Assign task to genie** step in the recipe editor.
       
    2. Go to the **Task Description** field and update the description to use the following instructions:
       
       > **DON'T REMOVE THE TELEGRAM DATAPILL**
       > 
       > Don't remove the Telegram datapill you mapped to the **Task Description** field in previous steps.
       
       ```plaintext
       
       Do the following based on the user's message and conversation history:
       
       1. Identify if the message contains an event where you need to set up a calendar event.
       2. If yes, then call the skill to create the event in Google Calendar.
       3. If not, then respond normally.
       4. When responding, you do not need to include your classification of whether it was a task.
       ```
       
    3. Click **Save**.
       
       ![Update the Task Description](/assets/updated-task-description.CLVsbtwC.png)_Update the **Task Description**_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/recipes/recipe-use-cases.md
description: >-
  Explore Workato recipe use cases that show how to set up connections,
  configure triggers and actions, map datapills, and more.
---

# Recipe use cases

Recipe use cases are designed to help you discover the power of automation through practical, real-world applications on Workato's low-code/no-code platform. This section contains a curated collection of use cases that showcase how diverse organizations use our platform to streamline operations, enhance workflows, and drive efficiency across various teams and departments.

Our collection of recipe use cases provides steps on how to achieve the following:

- Set up a connection for an app
- Configure a trigger
- Configure an action
- Use conditional statements
- Map datapills
- And much more

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Recipe modifications such as trigger and action configuration and conditional logic may require adjustments if you plan to include these recipes in your own workflows.

## AI and machine learning

### [Generate Confluence release notes from merged GitHub PRs](https://docs.workato.com/getting-started/use-cases/openai-github-confluence.html)

This use case integrates [OpenAI, GitHub, and Confluence](https://docs.workato.com/getting-started/use-cases/openai-github-confluence.html) to create a recipe that creates release notes in Confluence based on merged pull requests in GitHub.

### [Extract data from Google Slides with IDP by Workato](https://docs.workato.com/getting-started/use-cases/recipes/idp-by-workato-google-drive.html)

This use case integrates [Google Drive and IDP by Workato](https://docs.workato.com/getting-started/use-cases/recipes/idp-by-workato-google-drive.html) to create a recipe that searches a Google Drive folder for Google Slides presentations, creates a PDF export for intelligent document processing, and records extracted data in Google Sheets.

## Customer service

### [Create Zendesk and Jira issues with Workbot for Slack](https://docs.workato.com/getting-started/use-cases/zendesk-jira-workbot-slack.html)

This use case integrates [Zendesk, Jira, and Workbot for Slack](https://docs.workato.com/getting-started/use-cases/zendesk-jira-workbot-slack.html) to trigger the creation of a Zendesk ticket and Jira issue using Workbot for Slack.

## Databases

### [Sync MySQL records to Salesforce in batches](https://docs.workato.com/getting-started/use-cases/mysql-salesforce.html)

This use case integrates [MySQL and Salesforce](https://docs.workato.com/getting-started/use-cases/mysql-salesforce.html) to create a recipe that syncs records from MySQL to Salesforce in batches.

### [Validate Salesforce contact information with JavaScript and upsert to Snowflake](https://docs.workato.com/getting-started/use-cases/salesforce-js-snippets-snowflake-email.html)

This use case integrates [Salesforce, JavaScript snippets by Workato, and Snowflake](https://docs.workato.com/getting-started/use-cases/salesforce-js-snippets-snowflake-email.html) to create a recipe that ensures phone numbers are validated before upserting contacts from Salesforce to Snowflake.

### [Sync data between Amazon S3 and SQL Server](https://docs.workato.com/getting-started/use-cases/amazon-s3-sql-server.html)

This use case integrates [Amazon S3 and SQL Server](https://docs.workato.com/getting-started/use-cases/amazon-s3-sql-server.html) to create a recipe that syncs data on a recurring schedule.

## Developer

### [Create summarized Confluence notes and Jira comments from closed GitHub PRs](https://docs.workato.com/getting-started/use-cases/github-jira-confluence.html)

This use case integrates [GitHub, Jira, and Confluence](https://docs.workato.com/getting-started/use-cases/github-jira-confluence.html) to create a recipe that searches for closed issues in a GitHub repository, adds the identified issues to a list, and then creates a Confluence page summarizing the issues while also adding comments to related Jira tickets.

### [Post GitHub milestones with Workbot for Slack](https://docs.workato.com/getting-started/use-cases/github-workbot-for-slack.html)

This use case integrates [GitHub and Workbot for Slack](https://docs.workato.com/getting-started/use-cases/github-workbot-for-slack.html) to create a recipe that monitors new or updated milestones in GitHub and automatically posts details to Slack.

### [Update Quickbase records from SFTP CSV files](https://docs.workato.com/getting-started/use-cases/sftp-csv-by-workato-quickbase.html)

This use case integrates [SFTP, CSV tools by Workato, and Quickbase](https://docs.workato.com/getting-started/use-cases/sftp-csv-by-workato-quickbase.html) to create a recipe that fetches a CSV file from an SFTP server, parses its content, and updates records in a Quickbase table.

## DevOps and IT

### [Provision Jira and Okta users for new employees in Workday](https://docs.workato.com/getting-started/use-cases/workday-jira-okta.html)

This use case integrates [Workday, Jira, and Okta](https://docs.workato.com/getting-started/use-cases/workday-jira-okta.html) to monitor Workday for new employees and create new users in Jira and Okta.

### [Create or update Jira issues from new PagerDuty incidents](https://docs.workato.com/getting-started/use-cases/pagerduty-jira.html)

This use case integrates [PagerDuty and Jira](https://docs.workato.com/getting-started/use-cases/pagerduty-jira.html) to create a recipe that synchronizes new incidents from PagerDuty to Jira.

### [Upload a CSV of Active Directory entries to an SFTP server](https://docs.workato.com/getting-started/use-cases/active-directory-csv-sftp.html)

This use case integrates [Active Directory, CSV tools by Workato, and SFTP](https://docs.workato.com/getting-started/use-cases/active-directory-csv-sftp.html) to create a recipe that searches for specific entries in Active Directory, composes a CSV string from the results, and uploads the CSV file to an SFTP server.

## Files

### [Invite DocuSign signees to collaborate in Box and notify your team in Slack](https://docs.workato.com/getting-started/use-cases/docusign-box-slack.html)

This use case integrates [DocuSign, Box, and Slack](https://docs.workato.com/getting-started/use-cases/docusign-box-slack.html) to create a recipe that monitors DocuSign for newly signed documents.

### [Load Box CSV data to Google BigQuery with Google Cloud Storage](https://docs.workato.com/getting-started/use-cases/box-google-cloud-storage-bigquery.html)

This use case integrates [Box, Google Cloud Storage, and Google BigQuery](https://docs.workato.com/getting-started/use-cases/box-google-cloud-storage-bigquery.html) to create a recipe that monitors a Box folder for new CSV files, downloads each file’s contents, uploads the content to Google Cloud Storage, and then loads the data into a Google BigQuery table.

### [Share image attachments from email in Slack using a public link](https://docs.workato.com/getting-started/use-cases/gmail-filestorage-slack.html)

This use case integrates [Gmail, Workato FileStorage, and Slack](https://docs.workato.com/getting-started/use-cases/gmail-filestorage-slack.html) to create a recipe that extracts image attachments from Gmail, stores them in Workato FileStorage, generates a public link, and posts it in Slack.

## Finance and accounting

### [Sync Quickbase employees to Oracle EBS and notify your team in Slack](https://docs.workato.com/getting-started/use-cases/quickbase-oracle-ebs-slack.html)

This use case integrates [Quickbase, Oracle EBS, and Slack](https://docs.workato.com/getting-started/use-cases/quickbase-oracle-ebs-slack.html) to create a recipe that monitors Quickbase for new user records, creates a new employee in Oracle EBS, and posts a notification in Slack.

## HR

### [Sync Greenhouse new hires to SAP SuccessFactors](https://docs.workato.com/getting-started/use-cases/greenhouse-sap-successfactors-odata.html)

This use case integrates [Greenhouse and SAP SuccessFactors OData](https://docs.workato.com/getting-started/use-cases/greenhouse-sap-successfactors-odata.html) to create a recipe that monitors Greenhouse for new hires and creates new user accounts in SAP SuccessFactors in real time.

### [Export Workday workers to CSV with Python and upload to Google Drive](https://docs.workato.com/getting-started/use-cases/workday-python-google-drive.html)

This use case integrates [Workday, Python snippets by Workato, and Google Drive](https://docs.workato.com/getting-started/use-cases/workday-python-google-drive.html) to create a recipe that performs a daily search for workers in Workday, converts the output data from JSON to CSV format using Python, and uploads the resulting CSV file to Google Drive.

### [Sync Greenhouse offer letter to Box and create onboarding request in ServiceNow](https://docs.workato.com/getting-started/use-cases/greenhouse-box-servicenow-workbot.html)

This use case integrates [Greenhouse, Box, ServiceNow, and Workbot for Slack](https://docs.workato.com/getting-started/use-cases/greenhouse-box-servicenow-workbot.html) to create a recipe that automates offer letter generation, review, and delivery before initiating the onboarding process for new hires.

## Product and project management

### [Sync PlanGrid safety reports to Microsoft SharePoint](https://docs.workato.com/getting-started/use-cases/plangrid-sharepoint.html)

This use case integrates [PlanGrid and Microsoft SharePoint](https://docs.workato.com/getting-started/use-cases/plangrid-sharepoint.html) to create a recipe that synchronizes new and updated safety inspection field reports from PlanGrid to Microsoft SharePoint.

### [Create Jira issues for new ServiceNow incidents](https://docs.workato.com/getting-started/use-cases/servicenow-jira.html)

This use case integrates [ServiceNow and Jira](https://docs.workato.com/getting-started/use-cases/servicenow-jira.html) to create a recipe that monitors ServiceNow for new incidents and creates a corresponding Jira issue if one does not already exist.

### [Sync Zendesk tickets to Salesforce and notify your team in Slack](https://docs.workato.com/getting-started/use-cases/zendesk-salesforce-slack.html)

This use case integrates [Zendesk, Salesforce, and Slack](https://docs.workato.com/getting-started/use-cases/zendesk-salesforce-slack.html) to create a recipe that syncs tickets from Zendesk to Salesforce and then posts a notification in Slack.

## Sales and marketing

### [Display Salesforce account details with Workbot for Slack](https://docs.workato.com/getting-started/use-cases/salesforce-workbot-slack.html)

This use case integrates [Salesforce and Workbot for Slack](https://docs.workato.com/getting-started/use-cases/salesforce-workbot-slack.html) to create a recipe that displays Salesforce account details in Slack.

### [Create Salesforce tasks and Snowflake rows from Marketo lead activity](https://docs.workato.com/getting-started/use-cases/marketo-salesforce-snowflake.html)

This use case integrates [Marketo, Salesforce, and Snowflake](https://docs.workato.com/getting-started/use-cases/marketo-salesforce-snowflake.html) to create a recipe that creates Salesforce tasks and inserts Snowflake rows when new lead activity is detected in Marketo.

### [Create Salesforce leads from new HubSpot deals](https://docs.workato.com/getting-started/use-cases/hubspot-salesforce-workbot-for-teams.html)

This use case integrates [HubSpot, Salesforce, and Workbot for Microsoft Teams](https://docs.workato.com/getting-started/use-cases/hubspot-salesforce-workbot-for-teams.html) to build a recipe that creates new Salesforce leads from new HubSpot deals and posts a message in Microsoft Teams.

## More resources

- [Learn key concepts](/en/workato-concepts)
- [Create your first recipe](/en/getting-started/build-first-recipe)
- [Recipe design](/en/recipes/building-recipes)

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/openai-github-confluence.md
description: >-
  Build a recipe that connects OpenAI, GitHub, and Confluence to generate
  release notes pages from merged pull requests each week.
---

# Generate Confluence release notes from merged GitHub PRs recipe

This use case guides you through connecting [OpenAI](/en/connectors/openai), [GitHub](/en/connectors/github), and [Confluence](/en/connectors/confluence) to create a powerful automation.

## What does this recipe do?

This recipe retrieves merged pull requests (PRs) weekly from GitHub, iterates through each one to check for a specific Jira project key in the PR body, and, if found, sends the PR body to ChatGPT for a summary of the changes. Each summarized PR is then added to a new release notes page in Confluence.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB
    subgraph Scheduler[&nbsp Scheduler by Workato New recurring event trigger &nbsp]
      t1(Trigger) --- setup1(setup)
    end
    subgraph GitHub[&nbsp GitHub Search issues/pull requests action &nbsp]
      Action1(Action) --- setup2(setup)
    end
    subgraph CreateVariable[&nbsp Variables by Workato Create variable action &nbsp]
      Action2(Action) --- setup3(setup)
    end
    subgraph OpenAI[&nbsp OpenAI Send messages to OpenAI models action &nbsp]
      Action3(Action) --- setup6(setup)
    end
    subgraph UpdateVariable[&nbsp Variables by Workato Update variable action &nbsp]
      Action4(Action) --- setup7(setup)
    end
    subgraph Confluence[&nbsp Confluence Create page action &nbsp]
      Action5(Action) --- setup8(setup)
    end
  end
  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  Scheduler --> GitHub --> CreateVariable --> OpenAI --> UpdateVariable --> Confluence
  classDef default fill:#fff,stroke:#67eadd,stroke-width:2px;
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class t1,setup1,setup2,setup3,setup4,setup5,setup6,setup7,setup8,Action1,Action2,Action3,Action4,Action5,CreateRecipe,Workflow,x,xx,y,yy WorkatoTeal
  class Scheduler,GitHub,CreateVariable,OpenAI,UpdateVariable,Confluence SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## Create your recipe

Complete the following steps to create a recipe that creates release notes in Confluence based on merged pull requests in GitHub:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for OpenAI, GitHub, and Confluence:
   
   Create a OpenAI connection.
   
   ### Create an OpenAI connection
   
   This step creates a connection between Workato and your OpenAI account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `OpenAI` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![OpenAI connection setup](/assets/connect.Ckw6Urii.png)_OpenAI connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter your API key in the **API key** field. You can obtain this value from the [OpenAI API keys page](https://platform.openai.com/account/api-keys).
      
   6. Click **Connect**.
      
   
   Create a GitHub connection.
   
   ### Create a GitHub connection
   
   This step creates a connection between Workato and your GitHub account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `GitHub` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![GitHub connection setup](/assets/connect.nJKnT94C.png)_GitHub connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Connection type** drop-down menu to select the connection method you plan to use. You can select your [on-prem group](/en/on-prem/groups) name or select **Cloud** to use a direct connection.
      
   6. Select either [**OAuth App**](/en/connectors/github#traditional-oauth), [**GitHub App**](/en/connectors/github#github-app-authentication), or **Personal Access Token** in the **Authentication type** drop-down menu.
      
      **If you selected GitHub App**:
      
      1. Provide your app ID in the **GitHub App ID** field.
         
      2. Enter the private key in the **GitHub App Private key** field.
         
      3. Fill in the **Installation ID** field.
         
      4. Optional. Expand **Advanced configuration** to provide the **API Root URL**, which is applicable when using GitHub Enterprise Server.
         
      
      **If you selected Personal Access Token**:
      
      1. Enter your personal access token in the **Personal Access Token** field.
         
   7. Click **Connect**.
      
   
   Create a Confluence connection.
   
   ### Create a Confluence connection
   
   This step creates a connection between Workato and your Confluence account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Confluence` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Confluence connection setup](/assets/connect.DBcdaEC0.png)_Confluence connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Connection type** drop-down menu to select the connection method you plan to use. You can select your [on-prem group](/en/on-prem/groups) name or select **Cloud** to use a direct connection.
      
   6. Use the **Auth type** drop-down menu to select your authentication method. Options include **Basic**, **API token**, and **OAuth 2.0**.
      
   7. Provide your connection information.
      
      - **If using a cloud connection**: Enter your Confluence subdomain in the **Confluence subdomain field**.
      - **If using an on-prem connection**: Enter the root URI (includes protocol, optional port, and hostname) of your Confluence host in the **Confluence root URI** field.
   8. Provide your authentication information.
      
      **If you selected Basic authentication**:
      
      1. Enter your username (not email) in the **Username** field.
         
      2. Enter your password in the **Password** field.
         
      
      **If you selected API token**:
      
      1. Enter your email in the **Email** field.
         
      2. Enter your API token in the **API token** field. You can create one by going to your Atlassian account and selecting **[Security](https://id.atlassian.com/manage/api-tokens) > API tokens > Create API token**.
         
      
      **If you selected OAuth 2.0**:
      
      1. Enter your client ID in the **Client ID** field.
         
      2. Enter your client secret in the **Client secret** field.
         
      3. Optional. Expand **Advanced settings** to select scopes to request for this connection. The following scopes are selected by default:
         
         - `read:confluence-groups`
         - `read:confluence-content.summary`
         - `write:confluence-content`
         - `search:confluence`
   9. Click **Connect**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Use the **Location** drop-down menu to select the project where you plan to store the recipe.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Run on a schedule**. This creates a new recipe with the Scheduler by Workato [New recurring event trigger](/en/features/scheduler/triggers/new-recurring-event). This trigger doesn't require a connection.
   
9. Set up your Scheduler by Workato New recurring event trigger.
   
   ### Set up Scheduler by Workato New recurring event trigger
   
   This trigger sets the interval for how frequently the recipe runs. The Scheduler by Workato trigger doesn't require connection setup.
   
   1. Click the trigger in the recipe editor.
      
      ![Click the trigger](/assets/click-trigger.Cxrovggz.png)_Click the trigger_
      
   2. Use the **Time unit** drop-down menu to select **Weeks**.
      
      - Available options include **Minutes**, **Hours**, **Days**, **Weeks**, **Months**, or **Custom schedule**.
   3. Enter `1` in the **Trigger every** field to run the recipe weekly.
      
   4. Choose the days the recipe should run in the **Days of the week** field. For example, select **Monday**.
      
   5. Specify the time for the recipe to run in the **Trigger at** field. For example, enter `12:00 AM`.
      
   6. Optional. Select the timezone in the **Timezone** field. If left blank, the default is **America/Los\_Angeles**.
      
   7. Optional. Set the start date and time in the **Start after** field, or leave it blank to activate the trigger immediately after you start the recipe. You can't change this value after you run or test the recipe.
      
      ![Configure the trigger](/assets/trigger-config.pNyPMahZ.png)_Configure the trigger_
      
   8. Click **Save**.
      
   
10. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
11. Set up your GitHub Search issues/pull requests (batch) action.
    
    ### Set up GitHub Search issues/pull requests (batch) action
    
    This step searches for pull requests in your selected GitHub repository that were merged since the previous week.
    
    1. Search for `GitHub` and select it as your app.
       
       ![Choose GitHub](/assets/choose.33_OBN7A.png)_Choose GitHub_
       
    2. Select the **Search issues/pull requests** action.
       
       ![Select the Search issues/pull requests action](/assets/search-issues.DBLtx7JU.png)_Select the Search issues/pull requests action_
       
    3. Select the GitHub connection you created in the preceding steps.
       
    4. Use the **Organization** drop-down menu to select the organization containing the repository you plan to access.
       
    5. Use the **Repository name** drop-down menu to select your repository.
       
    6. Use the **Type** drop-down menu to select **PR**.
       
    7. Use the **Status** drop-down menu to select **Merged**.
       
    8. Switch the **Closed after** field to [formula mode](/en/formulas/formula-mode).
       
    9. Map the Scheduler by Workato Scheduled time (Step 1) datapill to the **Closed after** field.
       
    10. Append `- 7.days` in the **Closed after** field.
        
        ![Fill out the Closed after field](/assets/closed-after.DKTq8l4X.gif)_Fill out the Closed after field_
        
        This formula filters the search to retrieve only pull requests merged since the previous week.
        
    11. Click **Save**.
        
    
12. Click **\+ Add step** and select **Action in app**.
    
13. Set up your Variables by Workato Create variable action.
    
    ### Set up Variables by Workato Create variable action
    
    This step creates an empty variable named `Content`.
    
    1. Search for `Variables by Workato` and select it as your app.
       
       ![Choose Variables by Workato](/assets/choose.DetQOqPQ.png)_Choose Variables by Workato_
       
    2. Select the **Create variable** action.
       
       ![Select the Create variable action](/assets/create-variable.s1hMgsWx.png)_Select the Create variable action_
       
    3. Click **Add a variable**.
       
    4. Enter `Content` in the **Label** field.
       
    5. Click **Add variable**.
       
    6. Switch the **Content** field to [formula mode](/en/formulas/formula-mode) and enter `""` to initialize the variable with an empty string.
       
       ![Fill out the Content field](/assets/content.CcFlf0rw.png)_Fill out the Content field_
       
       This initialization is necessary for a later step, as you can't append a string (the content generated from ChatGPT) to a `nil` variable.
       
    7. Click **Save**.
       
    
14. Click **\+ Add step** and select **Repeat for each**.
    
    ![Add repeat for each](/assets/repeat-for-each-standard.IXsKDXgV.png)_Click **Add step > Repeat for each**_
    
    How does the Repeat for each condition work?
    
    ### Repeat for each condition GitHub and Jira example
    
    A [Repeat for each](/en/recipes/repeat-for-each) loop _repeats_ one or more actions _for each_ item in a list. The loop ends automatically when the entire list is processed.
    
    ```mermaid
    flowchart TD
      A(["Start"]) --> B("Another merged GitHub pull request from the past week?")
      B -- "Yes" --> C("Check if PR body contains Jira project key") --> MoreSteps("Additional steps")
      B -- "No" --> D(["End loop"])
    classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
    classDef WorkatoPink fill:#f3c1c2,stroke:#f3c1c2,stroke-width:1px;
    class A,D WorkatoPink
    ```
    
15. Set up your Repeat for each loop.
    
    ### Set up a Repeat for each loop for GitHub pull requests
    
    This step iterates through each of the pull requests that were merged in the past week.
    
    1. Map the GitHub Issues (Step 2) list datapill to the **Input list** field. This datapill contains a list of pull requests that match the search criteria specified in step 2.
       
    2. Use the **Repeat mode** drop-down menu to select **One item at a time**.
       
    3. Ensure **No** is selected in the **Clear step output** drop-down menu.
       
       ![Configure the Repeat for each loop](/assets/foreach-config.QMFrd1Q-.png)_Configure the Repeat for each loop_
       
    4. Click **Save**.
       
    
16. Click the **`…`** (ellipsis) next to the placeholder step in the recipe editor and select **Delete**.
    
    ![Delete placeholder](/assets/delete-placeholder.C2n16nJT.png)_Delete the placeholder step_
    
17. Click **\+ Add step** and select **IF condition**. Ensure this step is nested within the Repeat for each loop.
    
    ![Add IF condition](/assets/if-condition-standard.DI59XkdU.png)_Click **Add step > IF condition**_
    
    How do IF conditions work?
    
    ### Jira and GitHub IF condition example
    
    An [IF condition](/en/features/if-conditions) enables you to make decisions based on specific conditions. You can control your recipe workflow by executing different actions depending on whether a condition you specify is true or false.
    
    ```mermaid
    flowchart TD
        B(Does the PR body contain a specific Jira project key string?)
        B -->|Yes| C(Send message to OpenAI model with merged PR details)
        B ---->|No| E(No action required)

        classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
        classDef WorkatoPink fill:#f3c1c2,stroke:#f3c1c2,stroke-width:1px;
        class E WorkatoPink
    ```
    
18. Set up your IF condition for GitHub and Jira.
    
    ### Set up an IF condition for GitHub and Jira
    
    This step verifies if the GitHub pull request includes a specific Jira project key in the title or body. This ensures that only relevant pull requests linked to the designated Jira project are included in the release notes.
    
    1. Map the Foreach Body (Step 4) datapill to **Data field**. Alternatively, you can use the Title (Step 4) datapill.
       
    2. Use the **Condition** drop-down menu to select **contains**.
       
    3. Enter the relevant Jira project key in the **Value** field. For example, to only include merged PRs with the Jira project key `CT` in release notes, enter `CT-` in this field.
       
       ![Configure the IF condition](/assets/if-condition.BktlAuh6.png)_Configure the IF condition_
       
    4. Click **Save**.
       
    
19. Click **Select an app and action**.
    
20. Set up your OpenAI Send messages to OpenAI models action.
    
    ### Set up OpenAI Send messages to OpenAI models action
    
    This step sends a message to ChatGPT and asks it to generate a description of the merged pull request based on the PR body.
    
    1. Search for `OpenAI` and select it as your app.
       
       ![Choose OpenAI](/assets/choose.D7kzBUIa.png)_Choose OpenAI_
       
    2. Select the **Send messages to OpenAI models** action.
       
       ![Select the Send messages to OpenAI models action](/assets/send-messages-openai.COkauuJg.png)_Select the Send messages to OpenAI models action_
       
    3. Select the OpenAI connection you created in the preceding steps.
       
    4. Use the **Message type** drop-down menu to select **Single message**.
       
    5. Enter the following prompt in the **Text to send** field:
       
       > Generate a clear, user-friendly description of the update using the details provided in the pull request description. Format each change as a standalone release note item without additional headings or introductory text. Keep it concise and use plain language.
       > 
       > Description:
       
    6. Append the Foreach Body (Step 4) datapill to the end of the message in the **Text to send** field.
       
       ![Map the Body datapill](/assets/text-to-send.TeQh4asL.png)_Map the Body (Step 4) datapill_
       
    7. Optional. Use the **Model** drop-down menu to select the GPT model to use. For example, select **gpt-4o-mini**. Defaults to **gpt-3.5-turbo** if left blank.
       
    8. Click **Save**.
       
    
21. Click **\+ Add step** and select **Action in app**. Ensure this step is nested within the IF condition.
    
22. Set up your Variables by Workato Update variables action.
    
    ### Set up Variables by Workato Update variables action
    
    This step appends the ChatGPT response to the `Content` variable. The step links each merged PR title to the corresponding GitHub pull request and adds bullet points that summarize the changes described in the PR body.
    
    1. Search for `Variables by Workato` and select it as your app.
       
       ![Choose Variables by Workato](/assets/choose.DetQOqPQ.png)_Choose Variables by Workato_
       
    2. Select the **Update variables** action.
       
       ![Select the Update variables action](/assets/update-variables.Cj1zjItz.png)_Select the Update variables action_
       
    3. Use the **Variable name** drop-down menu to select **Content (step 3)**.
       
    4. Switch the **Content** field to [formula mode](/en/formulas/formula-mode) and perform the following actions:
       
       1. Map the Variables by Workato Content (Step 3) datapill.
          
       2. Enter `+ "\n" + "<a href='" +` to place the link on a new line.
          
       3. Map the Foreach Html URL (Step 4) datapill.
          
       4. Enter `+ "'>" +`.
          
       5. Map the Foreach Title (Step 4) datapill.
          
       6. Enter `+ "</a>" + "\n" +` to add the closing link tag and begin a new line.
          
       7. Map the OpenAI Best choice (Step 6) datapill.
          
       8. Enter `+ "\n"` to create a new line for details about the next merged PR.
          
          ![Update the Content variable](/assets/update-variable-content.DW96k3Ll.png)_Update the Content variable_
          
    5. Click **Save**.
       
    
23. Click **\+ Add step** and select **Action in app**. Ensure this step is placed outside of the IF condition and Repeat for each loop.
    
24. Set up your Confluence Create page action.
    
    ### Set up Confluence Create page action
    
    This step creates the Confluence page with the release notes.
    
    1. Search for `Confluence` and select it as your app.
       
       ![Choose Confluence](/assets/choose.BcDbzAxu.png)_Choose Confluence_
       
    2. Select the **Create page** action.
       
       ![Select the Create page action](/assets/create-page.D7F6BwNa.png)_Select the Create page action_
       
    3. Select the Confluence connection you created in the preceding steps.
       
    4. Enter the space key in the **Space key** field. This tells Confluence in which space the page should be created.
       
    5. Switch the **Title** field to [formula mode](/en/formulas/formula-mode) and enter the following:
       
       ```ruby
       "Release Notes for: " + today.to_s
       ```
       
       This formula creates the title for the Confluence page in the following format: `Release Notes for: YYYY-MM-DD`.
       
    6. Map the Variables by Workato Content (Step 3) datapill to the **Body** field.
       
       ![Example configuration](/assets/create-page-config.J_Cc1qrM.png)_Example configuration of the Create page action_
       
    7. Click **Save**.
       
    

Your **Generate Confluence release notes from merged GitHub PRs** recipe is ready to test and implement.

Example recipe configuration.

![OpenAI, GitHub, and Confluence recipe](/assets/recipe.CKVFSgda.png)_**Generate Confluence release notes from merged GitHub PRs** recipe_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/recipes/idp-by-workato-google-drive.md
description: >-
  Create a recipe that searches a Google Drive folder for Google Slides
  presentations, creates a PDF export for intelligent document processing, and
  records extracted data in Google Sheets.
---

# Extract Google Slides data with IDP by Workato

This use case guides you through connecting [Google Drive](/en/connectors/google-drive) and [IDP by Workato](/en/connectors/idp-by-workato) to create a powerful automation.

This recipe searches a Google Drive folder for Google Slides presentations, creates a PDF export for intelligent document processing, and records extracted data in Google Sheets.

## What does this recipe do?

This recipe enables you to extract matching content from Google Slides files stored in your Google Drive using IDP by Workato.

```mermaid
flowchart TD
  subgraph M[" "]
    direction TB
    subgraph D[&nbsp Scheduler by Workato New recurring event trigger &nbsp]
        direction RL
        x(setup) --- xx(Trigger)
    end
    subgraph H[Google Drive Search files action]
        xxx(Action) --- E(setup)
    end
    subgraph Y[Repeat for each loop]
        ww(Condition) --- V(setup)
    end
    subgraph J[Google Drive Export file action]
        www(Action) --- C(setup)
    end
    subgraph R[&nbsp IDP by Workato Process a document action &nbsp]
        AA(Action) --- CC(setup)
    end
    subgraph S[&nbsp Google Sheets Add row action &nbsp]
        AAA(Action) --- EEE(setup)
    end
  end
  A([Create recipe]) -- Configure your recipe --> M --> B([Automated workflow])
  D --> H
  H --> Y
  Y --> J
  J --> R
  R --> S
  classDef default fill:#fff,stroke:#67eadd,stroke-width:2px;
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class x,xx,xxx,ww,www,E,AA,EE,AAA,EEE,A,B,C,CC,V WorkatoTeal
  class D,H,R,S,Y,J SubgraphDash
  class M, default
```

## Create your recipe

Complete the following steps to create a recipe that extracts information you specify from Google Slides and records it in Google Sheets:

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create a connection for Google Drive:
   
   > **WORKATO UTILITY CONNECTORS DON'T REQUIRE SETUP**
   > 
   > The [Scheduler by Workato](/en/features/scheduler) and IDP by Workato connectors don’t require connection setup.
   
   Create a Google Drive connection.
   
   ### Create a Google Drive connection
   
   The Google Drive connector supports the following authentication types:
   
   - [OAuth 2.0 authentication](#oauth2-authentication)
   - [Service account](#service-account-authentication)
   
   #### OAuth 2.0 authentication
   
   OAuth 2.0 authentication requires specific permissions and scopes.
   
   View Google Drive OAuth 2.0 connection setup steps.
   
   #### Minimum and default scopes
   
   Workato requests the following scopes by default in addition to the scopes you select:
   
   - `drive`: See, edit, create, and delete all your Google Drive files
   - `drive.readonly`: See and download all your Google Drive files
   
   Additionally, your Google account must have the `Edit` permission for all files and folders that you plan to use in Workato recipes.
   
   #### Connect to Google Drive using OAuth 2.0
   
   Complete the following steps to set up an OAuth 2.0 connection to in Workato:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select **Google Drive** as your connection on the **New Connection** page.
      
   3. Enter a name for your connection in the **Connection name** field.
      
      ![Connection setup](/assets/google-drive-connection-setup.o_esWDm7.png)_Google Drive connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
      
   6. Optional. Expand the **Advanced settings** section and use the **Requested permissions** drop-down menu to specify OAuth scopes to request for your connection.
      
   7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
      
   8. Click **Sign in with Google**.
      
   9. Click **Allow** to authorize Workato to access your Google Drive.
      
   
   #### Service account authentication
   
   Service account authentication requires a Google service account and an enabled Google Workspace API.
   
   View service account connection setup steps.
   
   A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.
   
   Service accounts provide the following benefits:
   
   - **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
   - **Dedicated permissions:** Service accounts can only access projects that you share with them.
   - **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.
   
   Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.
   
   ##### Set up a Google service account
   
   Complete the following steps to set up a Google service account:
   
   1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
      
   2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
      
      ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
      
   3. Click the **Email** of the service account you intend to use.
      
      ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
      
   4. Copy the service account's **Email** and save it to configure your connection later.
      
      ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
      
   5. Go to the **KEYS** tab.
      
   6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
      
   7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
      
   
   ##### Connect to Google Drive using service account authentication
   
   Service account authentication requires the following prerequisites:
   
   - [Create a service account and generate a private key](#service-account-setup)
   - [Enable the Google Workspace API](https://support.google.com/googleapi/answer/6158841)
   
   Complete the following steps to set up a service account connection to Google Drive in Workato:
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for `Google Drive` and select it as your app.
      
   3. Enter a name for your connection in the **Connection name** field.
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Authentication type** drop-down menu to select **Service account**.
      
   6. Enter the service account's email address in the **GCP project service account email** field.
      
      ![Retrieve your GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Retrieve your GCP Project service account email_
      
   7. Enter the **Private key**. Retrieve the private key from the downloadable JSON. Include both `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----\n`.
      
   8. Optional. Enter the **User email** of the account to impersonate. If left blank, Workato accesses the service account's Drive.
      
      User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Drive. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Drive. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
      
   9. Optional. Expand the **Advanced settings** section and use the **Requested permissions** drop-down menu to specify OAuth scopes to request for your connection.
      
   10. Click **Sign in with Google**.
       
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Use the **Location** drop-down menu to select the project where you plan to store the recipe.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Run on a schedule**. This creates a new recipe with the Scheduler by Workato [New recurring event trigger](/en/features/scheduler/triggers/new-recurring-event). This trigger doesn't require a connection.
   
9. Set up your Scheduler by Workato New recurring event trigger.
   
   ### Set up Scheduler by Workato New recurring event trigger
   
   This trigger sets the interval for how frequently the recipe runs. The Scheduler by Workato trigger doesn't require connection setup.
   
   1. Click the trigger in the recipe editor.
      
      ![Click the trigger](/assets/click-trigger.Cxrovggz.png)_Click the trigger_
      
   2. Use the **Time unit** drop-down menu to select **Weeks**.
      
      - Available options include **Minutes**, **Hours**, **Days**, **Weeks**, **Months**, or **Custom schedule**.
   3. Enter `1` in the **Trigger every** field to run the recipe weekly.
      
   4. Choose the days the recipe should run in the **Days of the week** field. For example, select **Monday**.
      
   5. Specify the time for the recipe to run in the **Trigger at** field. For example, enter `12:00 AM`.
      
   6. Optional. Select the timezone in the **Timezone** field. The default is **America/Los\_Angeles** if left blank.
      
   7. Optional. Set the start date and time in the **Start after** field, or leave it blank to activate the trigger immediately after you start the recipe. You can't change this value after you run or test the recipe.
      
      ![Configure the trigger](/assets/trigger-config.pNyPMahZ.png)_Configure the trigger_
      
   8. Click **Save**.
      
   
10. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
11. Set up your Google Drive Search files or folders (Batch) action.
    
    ### Set up the Google Drive Search files or folders action
    
    This step searches a Google Drive folder you specify for Google Slides files.
    
    1. Search for `Google Drive` and select it as your app.
       
    2. Select the **Search files or folders (Batch)** action.
       
    3. Use the **Files or folders** drop-down menu to select **Files**.
       
       ![Set up the Search files or folders (Batch) action](/assets/google-drive-search-files-folders.Dybv46S8.png)_**Search files or folders** (Batch) action_
       
    4. Set **Folder** to **Select folder** and use the drop-down menu to select the folder you plan to search for files.
       
    5. Optional. Enter a name in the **Name** field to fetch files or folders that contain partial matches.
       
    6. Go to the **Query** field and enter the following value to filter your search to Google Slides files:
       
       ```
       mimeType='application/vnd.google-apps.presentation'
       ```
       
    7. Click **Save**.
       
    
12. Click **\+ Add step** and select **Repeat for each**.
    
13. Set up your Repeat for each step.
    
    ### Set up the Repeat for each step
    
    This step iterates through each Google Slides file in the folder you select.
    
    1. Map the Google Drive (Step 2) datapill to the **Input list** field.
       
       ![Set up the Repeat for each step](/assets/repeat-for-each.DW3y1h5e.png)_Set up the Repeat for each step_
       
    2. Use the **Repeat mode** drop-down menu to select **One item at a time**.
       
    3. Use the **Clear step output** drop-down menu to select **No**.
       
    4. Click **Save**.
       
    
14. Click **\+ Add step** and select **Action in app**.
    
15. Set up your Google Drive Export file action.
    
    ### Set up the Google Drive Export file action
    
    This step exports the Google Slides file as a PDF. IDP by Workato doesn't support Google Slides document types.
    
    1. Search for `Google Drive` and select it as your app.
       
    2. Select the **Export file** action.
       
    3. Use the **File** drop-down menu to select **Use file ID**.
       
       ![Set up the Google Drive Export file action](/assets/export-file-action.Dd9QSPXq.png)_Set up the Google Drive **Export file** action_
       
    4. Map the Foreach (Step 3) datapill to the **File** value field.
       
    5. Set **MIME type** to **Select MIME type** and use the value drop-down menu to select **PDF**.
       
    6. Click **Save**.
       
    
16. Click **\+ Add step** and select **Action in app**.
    
17. Set up your Process a document using IDP by Workato action.
    
    ### Set up the Process a document using IDP by Workato action
    
    This step processes the exported PDF for fields you identify.
    
    1. Search for `IDP by Workato` and select it as your app.
       
    2. Select the **Process a document using IDP by Workato** action.
       
    3. Map the Google Drive (Step 4) datapill to the **File contents** field.
       
       ![Set up the Process a document using IDP by Workato action](/assets/idp-process-document.C4NLYLvu.png)_Set up the **Process a document using IDP by Workato** action_
       
    4. Set **File type** to **Select from list** and use the value drop-down menu to select **PDF**.
       
    5. Use the **Document type** drop-down menu to select **Documents**.
       
    6. Use the **IDP version** drop-down menu to select **OCR augmented LLM extraction**.
       
    7. Copy the following JSON schema and paste it into the **Fields to identify** section:
       
       ```json
       [
         {
           "name": "FileName",
           "type": "string",
           "optional": false,
           "description": "Project Name",
           "control_type": "text",
           "label": "Project name"
         },
         {
           "name": "ProductManager",
           "type": "string",
           "optional": true,
           "description": "Product Manager",
           "control_type": "text",
           "label": "Product manager"
         },
         {
           "name": "PrintFileDeliveryDate",
           "type": "string",
           "optional": true,
           "description": "Print File Delivery Date",
           "control_type": "text",
           "label": "Print file delivery date"
         },
         {
           "name": "ProductFeatureName",
           "type": "string",
           "optional": false,
           "description": "Presentation feature or topic",
           "control_type": "text",
           "label": "Brand range"
         },
         {
           "name": "FeatureOverview",
           "type": "string",
           "optional": true,
           "control_type": "text",
           "label": "Feature overview",
           "description": "Summary or overview section title"
         },
         {
           "name": "Marketswherelaunched",
           "type": "string",
           "optional": true,
           "description": "Markets Where Launched",
           "control_type": "text",
           "label": "Markets where launched"
         }
       ]
       ```
       
    8. Click **Save**.
       
    
18. Click **\+ Add step** and select **Action in app**.
    
19. Set up your Google Sheets Add row in a sheet action.
    
    ### Set up the Google Sheets Add row in a sheet action
    
    This step adds the content identified in the IDP by Workato processing step to a new row in a Google sheet you select.
    
    1. Search for `Google Sheets` and select it as your app.
       
    2. Select the **Add row** action.
       
    3. Use the **Google Drive** drop-down menu to select the drive you plan to use.
       
       ![Set up the Add row action](/assets/google-sheet-add-row.Cu_XuRWe.png)_Set up the Add row action_
       
    4. Use the **Spreadsheet** drop-down menu to select the spreadsheet where you plan to add the new row.
       
    5. Use the **Sheet** drop-down menu to select the sheet where you plan to add the new row.
       
    6. Expand the **Columns** section.
       
    7. Map the File name (Step 5) datapill to the **ProjectName** field.
       
    8. Map the Product manager (Step 5) datapill to the **ProductManager** field.
       
    9. Map the Print file delivery date (Step 5) datapill to the **PrintFileDeliveryDate** field.
       
    10. Map the Product feature name (Step 5) datapill to the **ProductFeatureName** field.
        
    11. Map the Feature overview (Step 5) datapill to the **FeatureOverview** field.
        
    12. Map the Markets where launched (Step 5) datapill to the **Marketswherelaunched** field.
        
        ![Map the datapills to the corresponding fields](/assets/map-idp-extracted-content.D3dDsBEq.gif)_Map the datapills to the corresponding fields_
        
    13. Click **Save**.
        
    

Your **Extract Google Slides data with IDP by Workato** recipe is ready to test and implement.

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/zendesk-jira-workbot-slack.md
description: >-
  Build a recipe that creates Zendesk tickets and Jira issues from a Workbot for
  Slack action and posts the details in Slack.
---

# Create Zendesk and Jira issues with Workbot for Slack recipe

This use case guides you through connecting [Zendesk](/en/connectors/zendesk), [Jira](/en/connectors/jira), and [Workbot for Slack](/en/workbot/workbot#workbot-for-slack) to Workato to create a powerful automation.

## What does this recipe do?

This recipe enables you to execute a message action in Workbot for Slack, which creates a Zendesk ticket and a Jira issue using the input fields from the trigger's command. After creating these tickets, the details are posted in Slack to a channel or direct message of your choice.

```mermaid
flowchart TD
  subgraph M[" "]
    direction TB
    subgraph D[&nbsp Workbot for Slack New shortcut trigger &nbsp]
        direction RL
        s1(setup) --- t1(Trigger)
    end
    subgraph H[&nbsp Jira Create issue action &nbsp]
        a1(Action) --- E[setup]
    end
    subgraph R[&nbsp Jira Get issue details action &nbsp]
        AA[Action] --- EE[setup]
    end
    subgraph L[&nbsp Zendesk Create ticket action &nbsp]
        AB[Action] --- EF[setup]
    end
    subgraph S[&nbsp Workbot for Slack Post message action &nbsp]
        AC[Action] --- EG[setup]
    end
  end
  A([Create recipe]) -- Configure your recipe --> M --> B([Automated workflow])
  D --> H
  H --> R
  R --> L
  L --> S

  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class s1,t1,a1,E,AA,EE,AB,EF,AC,EG,A,B WorkatoTeal
  class D,H,R,L,S SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class M SubgraphLight
```

## Create your recipe

Complete the following steps to design a recipe that creates a Zendesk ticket and a Jira issue when you run an action command in Workbot for Slack.

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for Zendesk, Jira, and Workbot for Slack:
   
   Create a Zendesk connection.
   
   ### Create a Zendesk connection
   
   This step creates a connection between Workato and your Zendesk account. The Zendesk connector supports OAuth 2.0 authentication.
   
   > **DEPRECATED AUTHENTICATION METHODS**
   > 
   > Effective March 31, 2026, you can no longer create new Zendesk connections using Basic authentication or Custom OAuth profiles. This change is required by [Zendesk's updated Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/).
   > 
   > Existing connections using these authentication methods will continue to work until **April 30, 2027**. On this date, Zendesk connections still using Basic authentication or a Custom OAuth profile will be terminated, and recipes relying on these connections will stop functioning.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Zendesk` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Zendesk connection setup](/assets/connect.xFOTYqmj.png)_Zendesk connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Enter the **Subdomain** for your Zendesk URL. For example, if your Zendesk URL is `https://acme.zendesk.com`, your subdomain is `acme`.
      
   6. Click **Connect**.
      
   
   Create a Jira connection.
   
   ### Create a Jira connection
   
   This step creates a connection between Workato and your Jira account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Jira` on the **New connection** page.
      
   3. Enter a name for your Jira connection in the **Connection name** field.
      
      ![Jira connection setup](/assets/connect.DE7n2rdP.png)_Jira connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Select your **Connection type**.
      
   6. Use the **Auth type** drop-down menu to select your authentication method. Supported options include [Basic](/en/connectors/jira#basic-authentication-with-password), [API token](/en/connectors/jira#api-tokens), [OAuth 2.0](/en/connectors/jira#oauth2-0), and [Personal access token](/en/connectors/jira#personal-access-tokens).
      
   7. Provide your **Host name**. For example, if your Jira URL is `https://acme.atlassian.net`, your host name is `acme.atlassian.net`.
      
   8. Click **Connect**.
      
   
   Create a Workbot for Slack connection.
   
   ### Create a Workbot for Slack connection
   
   This step creates a connection between Workato and your Workbot for Slack account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Workbot for Slack` on the **New connection** page.
      
   3. Provide a name for your connection in the **Name** field.
      
      ![Workbot for Slack connection setup](/assets/connect.DudoV0Fs.png)_Workbot for Slack connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Optional. Select the NLU provider you plan to use, such as DialogFlow or Amazon Lex NLU. You must connect to the NLU provider for it to appear in the drop-down menu.
      
   6. Optional. Click **Advanced** to configure **Slash commands verification tokens**, **custom help** content, your **Slack app status** (classic or not), and your **Custom OAuth profile**.
      
   7. Click **Connect**, sign in to your Slack workspace when prompted, and click **Continue** to verify the connection.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Enter a name for your recipe in the **Name** field.
   
6. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
7. Click **Start building**.
   
   ![Start building your recipe](/assets/start-building.CdeBSfVN.png)_Start building your recipe_
   
8. Click **Pick a starting point**, then select **Trigger from an app**.
   
9. Click **Select an app and trigger event**.
   
10. Set up your Workbot for Slack New shortcut trigger.
    
    ### Set up Workbot for Slack New shortcut trigger
    
    This trigger monitors Workbot for Slack for new shortcuts.
    
    1. Search for `Workbot for Slack` and select it as your app.
       
       ![Choose Workbot for Slack as your app](/assets/choose.6f8uKzDW.png)_Choose Workbot for Slack as your app_
       
    2. Select the **New Shortcut** trigger.
       
       ![New shortcut trigger](/assets/new-shortcut-trigger.C7STZ0GQ.png)_New Shortcut trigger_
       
    3. Use the **Shortcut type** drop-down menu to select **Message**.
       
       ![Setup shortcut trigger](/assets/shortcut-trigger.bSLJQhtA.png)_Set up your Shortcut trigger_
       
    4. Enter a name in the **Shortcut name** field. For example, `Create issue & ticket`.
       
    5. Click **Add field** in the **Parameters** section.
       
    6. Enter `Summary` in the **Name** field.
       
    7. Enter a label in the **Label** field.
       
    8. Select **String** from the **Data type** drop-down menu.
       
    9. Select **No** from the **Optional?** drop-down menu.
       
    10. Enter additional help text in the **Hint** field.
        
    11. Select **Text** from the **Dialog control type** drop-down menu.
        
        ![Summary input field](/assets/summary-input-field.V1RDVUD2.png)_`Summary` input field_
        
    12. Click **Add field** under **Parameters** to add a second input field.
        
    13. Enter `Description` in the **Name** field.
        
    14. Enter a label in the **Label** field.
        
    15. Select **String** from the **Data type** drop-down menu.
        
    16. Select **No** from the **Optional?** drop-down menu.
        
    17. Enter additional help text in the **Hint** field.
        
    18. Select **Textarea** from the **Dialog control type** drop-down menu.
        
        ![Description input field](/assets/description-input-field.BX1Ym-IO.png)_`Description` input field_
        
    19. Click **Add field** under **Parameters** to add a third input field.
        
    20. Enter `Priority` in the **Name** field.
        
    21. Enter a label in the **Label** field.
        
    22. Select **String** from the **Data type** drop-down menu.
        
    23. Select **No** from the **Optional?** drop-down menu.
        
    24. Enter additional help text in the **Hint** drop-down menu.
        
    25. Select **Static** from the **Menu options** drop-down menu.
        
    26. Enter a list of comma-separated priority levels in the **Options** field.
        
        ![Priority input field](/assets/priority-input-field.DazrJh62.png)_`Priority` input field_
        
    27. Click the **Add field** button under **Parameters** to add a fourth input field.
        
    28. **Name** your input field `notify-user` > add a **Label** > set **Data type** to `String` > set **Optional?** to `No` > provide a **Hint** for your input field > set **Menu options** to `Conversations` > and then click **Save**.
        
        ![notify\_user input field](/assets/notify-user-input-field.DBN6AJe2.png)_`notify_user` input field_
        
    29. Use the **Copy original text into dialog field** drop-down menu to select **Description**.
        
        ![notify\_user input field](/assets/dialogue-field.C0NuiXJi.png)_Select Description_
        
    30. Click **Save**.
        
    
11. Click **\+ Add step** and select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
12. Set up your Jira Create issue action.
    
    ### Set up Jira Create issue action
    
    This step creates a new issue in Jira and uses the description from Workbot for Slack.
    
    1. Search for `Jira` and select it as your app.
       
       ![Choose Jira as your app](/assets/choose.Cz1B1oV7.png)_Choose Jira as your app_
       
    2. Select the **Create issue** action.
       
    3. Use the **Project issue type** drop-down menu to select the issue type you plan to create. For example: task, bug fix, or onboarding.
       
       ![Configure Create issue](/assets/configure-jira-create-issue.Dmhn3aBI.gif)_Select your issue type_
       
    4. Map the Workbot for Slack Summary (Step 1) datapill to the **Summary** field.
       
    5. Map the Workbot for Slack Description (Step 1) datapill to the **Description** field.
       
    6. Map the Workbot for Slack Priority (Step 1) datapill to the **Priority name** field.
       
    7. Click **Save**.
       
    
13. Click **\+ Add step** and select **Action in app**.
    
14. Set up your Jira Get issue action.
    
    ### Set up Jira Get issue action
    
    This steps retrieves Jira issues by ID.
    
    1. Search for `Jira` and select it as your app.
       
       ![Choose Jira as your app](/assets/choose.Cz1B1oV7.png)_Choose Jira as your app_
       
    2. Select the **Get issue** action.
       
       ![Get issue](/assets/get-issue.CmH6VfqE.png)_Select the Get issue action_
       
    3. Map the Jira ID (Step 2) datapill to the **Issue ID or key** field.
       
       ![Get issue setup](/assets/get-issue-setup.Doe3crxz.png)_Configure the Issue ID or key field_
       
    4. Click **Save**.
       
    
15. Click **\+ Add step** and select **Action in app**.
    
16. Set up your Zendesk Create ticket action.
    
    ### Set up Zendesk Create ticket action
    
    This step creates a Zendesk ticket with information from Jira and Workbot for Slack.
    
    1. Search for `Zendesk` and select it as your app.
       
       ![Choose Zendesk as your app](/assets/choose.B01IpRki.png)_Choose Zendesk as your app_
       
    2. Select the **Create ticket** action.
       
       ![Create ticket](/assets/create-ticket.BwQT3lda.png)_Select the Create ticket action_
       
    3. Map the Jira Summary (Step 3) datapill to the **Subject** field.
       
    4. Use the **Priority** drop-down menu to select **Enter custom value** and then click **Formula**.
       
       ![Set priority to formula](/assets/set-priority-to-formula.DmYTC-VN.gif)_Set the Priority field to Formula_
       
    5. Copy and paste the following formula into the **Priority** field:
       
       ```
       =["Higher", "Highest"].include?(_dp('{"pill_type":"output","provider":"jira","line":"9e7af602","path":["fields","priority","name"]}')) ? "urgent" :  "Medium" == _dp('{"pill_type":"output","provider":"jira","line":"9e7af602","path":["fields","priority","name"]}') ?  "normal" : _dp('{"pill_type":"output","provider":"jira","line":"9e7af602","path":["fields","priority","name"]}') == "High" ?  "high" : "low"
       ```
       
       ![Priority formula](/assets/priority-formula.YA6Jwres.png)_Priority formula_
       
    6. Use the **Status** drop-down menu to select **Open**.
       
    7. Map the Jira Due date (Step 3) datapill to the **Due at** field.
       
       ![Map due date](/assets/map-due-date.2528YwON.png)_Configure the Due at field_
       
    8. Map the Workbot for Slack Description (Step 1) datapill to the **Text comment** field.
       
       ![Map description](/assets/map-description.B6S4SIGu.png)_Configure the Text comment field_
       
    9. Click **Save**.
       
    
17. Click **\+ Add step** and select **Action in app**.
    
18. Set up your Workbot for Slack Post message action.
    
    ### Set up Workbot for Slack Post message action
    
    This step posts a Slack message notify the users and channels you specify about the new Zendesk ticket.
    
    1. Search for `Workbot for Slack` and select it as your app.
       
    2. Select the **Post message** action.
       
    3. Map the Workbot for Slack Notify user (Step 1) datapill to the **Channel name/DM** field.
       
       ![Notify user](/assets/workbot-slack-notify-user.CPh_YOhg.png)_Configure the Channel name/DM field_
       
    4. Click **Add block to message** and use the **Type** drop-down menu to select **Section with text**.
       
       ![Add block message](/assets/add-block-message.BBiA39m2.png)_Click the **Add block to message** button_
       
    5. Map the Zendesk Subject (Step 4) datapill, the Zendesk Ticket ID (Step 4) datapill, and the Workbot for Slack User ID (Step 1) datapill to the **Section text** field.
       
       ![Map section text](/assets/section-text.CgJRfoxb.png)_Map the **Section text** field_
       
    6. Click **Add block to message** and use the **Type** drop-down menu to **Section with fields**.
       
       ![Section with fields](/assets/section-with-fields.CNswwRy2.png)_Section with fields_
       
    7. Locate the **Attachment fields** section and click **Add field**.
       
       ![Add field](/assets/add-field.BdnSaDFA.png)_Click the **Add field** button_
       
    8. Enter `Subject` in the **Title** field.
       
    9. Map the Zendesk Subject (Step 4) datapill to the **Value** field.
       
       ![Attachment fields](/assets/attachment-fields.vxL37T4i.png)_Add a Subject field_
       
    10. Click **Add field** to add a second field.
        
    11. Enter `Priority` in the **Title** field.
        
    12. Map the Zendesk Priority (Step 4) datapill to the **Value** field.
        
    13. Click **Add field** to add a third field.
        
    14. Enter `Description` in the **Title** field.
        
    15. Switch the **Value** field to [formula mode](/en/formulas/formula-mode) and copy and paste the following formula:
        
        ```
        ="\n"+_dp('{"pill_type":"output","provider":"zendesk","line":"create_ticket","path":["description"]}')[0...65]+"..."
        ```
        
        ![Attachment fields](/assets/description-formula.B-Z7KDps.png)_Add a Description field_
        
    16. Click **Add field** to add a fourth field.
        
    17. Enter `Status` in the **Title** field.
        
    18. Map the Zendesk Status (Step 4) datapill to the **Value** field.
        
    19. Expand the **Divider** section and use the **Type** drop-down menu to select **Divider**.
        
        ![Divider](/assets/workbot-divider.DETLwNuT.png)_Select Divider_
        
    20. Click **Save**.
        
    
19. Click **\+ Add step** and select **Action in app**.
    
20. Set up your second Workbot for Slack Post message action.
    
    ### Set up a second Workbot for Slack Post message action
    
    This step posts a Slack message notify the users and channels you specify about the new Jira issue.
    
    1. Search for `Workbot for Slack` and select it as your app.
       
    2. Map the Workbot for Slack Notify user (Step 1) datapill into the **Channel name/DM** field.
       
       ![Notify user](/assets/workbot-slack-notify-user.CPh_YOhg.png)_Configure the Channel name/DM field_
       
    3. Click **Add block to message** and use the **Type** menu to select **Section with text**.
       
       ![Add block message](/assets/add-block-message.BBiA39m2.png)_Click the **Add block to message** button_
       
    4. Map the Jira Key (Step 3) datapill and the Workbot for Slack User ID (Step 1) datapill to the **Section text** field.
       
       ![Map section text](/assets/section-text-for-jira.D5WJn6A9.png)_Map the **Section with text** field_
       
    5. Click **Add block to message** and use the **Type** drop-down menu to select **Section with fields**.
       
    6. Locate the **Attachment fields** section and click **Add field**.
       
       ![Add field](/assets/add-field.BdnSaDFA.png)_Click the **Add field** button_
       
    7. Enter `Summary` in the **Title** field.
       
    8. Map the Jira Summary (Step 3) datapill to the **Value** field.
       
       ![Attachment fields](/assets/attachment-fields-for-jira.CKk3tBXS.png)_Add a Summary field_
       
    9. Click **Add field** to add a second field.
       
    10. Enter `Priority` in the **Title** field,
        
    11. Map the Jira Name (Step 3) datapill to the **Value** field.
        
    12. Click **Add field** to add a third field.
        
    13. Enter `Description` in the **Title** field.
        
    14. Switch the **Value** field to [formula mode](/en/formulas/formula-mode) and copy and paste the following formula:
        
        ```
        ="\n"+ _dp('{"pill_type":"output","provider":"jira","line":"9e7af602","path":["fields","description"]}')[0...65]+"..."
        ```
        
        ![Description field](/assets/jira-description-field.VqB85_xO.png)_Add a Description field_
        
    15. Click **Add field** to add a fourth field.
        
    16. Enter `Status` in the **Title** field.
        
    17. Map the Jira Name (Step 3) datapill to the **Value** field.
        
    18. Click **Save**.
        
    

Your **Create Zendesk and Jira issues with Workbot for Slack** recipe is ready to test and implement.

---
