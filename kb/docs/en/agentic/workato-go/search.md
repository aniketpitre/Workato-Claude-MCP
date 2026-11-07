---
url: 'https://docs.workato.com/en/agentic/workato-go/search.md'
description: >-
  Search in Workato GO across world knowledge or company knowledge to get
  summarized answers with links to apps and documentation.
---

# Search for knowledge

You can filter Workato GO responses to show information from the following knowledge sources:

- **World knowledge**: Search across publicly available information.
- **Company knowledge**: Search across your company's third-party apps and internal documentation.

## Search with Workato GO

Complete the following steps to search in Workato GO:

1. Go to your Workato GO account.
   
2. Use the search drop-down menu to select **World knowledge** or **Company knowledge**.
   
   ![Knowledge source](/assets/knowledge-source.xtPmfOUD.png)_Select **World knowledge** or **Company knowledge**_
   
3. Enter a search term or ask a question in the search box. Workato GO provides a summarized response with links to external resources if you selected **World knowledge** or links your company's apps and internal documentation if you selected **Company knowledge**.
   
   ![Search results](/assets/search-results.BddInxTu.png)_**Company knowledge** search results_
   

## Troubleshoot search and real-time chat issues

Use this section to check for issues with the Server-Sent Events (SSE) connection when real-time search or chat stops working.

### SSE connection issues

You may experience blocked or terminated Server-Sent Events (SSE) connections when you access the production URL. This issue causes the following problems:

- Chat messages aren't updating in real-time
- Connection appears to close immediately
- No continuous event stream received

You must test the connection directly from the affected machine to determine whether the network blocks the SSE connection.

#### Test method

Complete the following steps to determine if your SSE connection is blocking Workato GO functionality:

> **SSE IS A NETWORK-LEVEL ISSUE**
> 
> This is a network-level issue, not a browser-specific problem. The curl test helps isolate whether the issue exists at the network layer.

1. Press the `F12` key to open Developer Tools in your browser.
   
2. Go to the **Network** tab.
   
3. Look for the `subscribe` request.
   
4. Copy your Bearer token from the request headers.
   
5. Run the following curl command from your terminal or Postman:
   
   ```bash
   curl -v https://api-prod.matrix.workato.com/api/v1/chat/conversations/<conversation_id>/subscribe \
     -H "Authorization: Bearer <paste_token_here>"
   ```
   
6. Ensure that your connection behaves as expected by confirming the following:
   
   - Connection remains open continuously and doesn't close immediately after connecting
   - Stream `event:` messages in real-time
   
   > **CONFIRMATION OF SSE ISSUE**
   > 
   > The SSE connection is blocked or terminated if the connection closes immediately or doesn't stream events. This is caused by one or more of the following configuration settings:
   > 
   > - Network firewall rules
   > - Corporate proxy settings
   > - Internet service provider restrictions
   

#### Solution

Contact your IT department or network administrator and submit a request to perform the following actions:

- Whitelist your data center-specific domain. For example: `api-prod.matrix.workato.com`
- Allow SSE/streaming connections to this endpoint
- Ensure proxy settings permit long-lived HTTP connections
- Verify firewall rules don't terminate persistent connections

---
