---
url: 'https://docs.workato.com/en/airo/build/genies.md'
description: >-
  Create a genie, its knowledge base, and its skills by describing them to AIRO,
  in Workato or through an MCP client.
---

# Build genies with AIRO

You can build a genie, its knowledge base, and its skills by describing them to AIRO in plain language, including the decision path it should follow. For example, a help desk genie might check a policy document first, search similar support tickets next, and only file a new ticket as a last resort.

Build either by [chatting with AIRO](/en/airo/chat) in Workato, or through an MCP client connected to [AIRO Connect](/en/airo/mcp).

Refer to [Create your first genie](/en/agentic/agent-studio/create-a-genie) for the equivalent step-by-step workflow in Agent Studio.

## Prerequisites

- AIRO enabled in your workspace, plus a connection to [AIRO Connect](/en/airo/mcp) if you're building from an MCP client.
- The **Genies** and **Knowledge Bases** privileges, with Create/Edit access, in the target project. Refer to [Genie building privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#genie-building).
- Existing Workato connections for any app a skill needs, for example Jira or Salesforce.
- A document for the knowledge base to answer from.

Confirm that your connection to AIRO Connect points to the intended workspace and environment before you start. Check whether your MCP client is set to approve AIRO Connect tools without prompting.

## Example: Build a help desk genie

This example builds a help desk genie that follows this decision path:

1. Check the IT support policy.
2. Search existing Jira tickets for a similar issue.
3. Explain how a similar ticket was resolved.
4. File a new ticket only as a last resort, after the user confirms.

### Create the knowledge base

Open AIRO and describe the knowledge base.

```text
Create a knowledge base called "IT support policy". Genies should treat it as the single source of truth for policy questions and never invent an answer it doesn't contain.
```

AIRO creates the knowledge base in your workspace. Next, add the policy document to it.

- **In Workato**: [Select your knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-base-management), click **\+ Add knowledge**, select **Upload documents**, then drag and drop the file or select **Upload from device**.
- **In an MCP client**: Ask AIRO to upload the document. AIRO adds the file to the knowledge base and starts ingestion.

Sample document to test this example

Copy the following into a `.md` or `.txt` file:

```text
# IT support policy

## Account lockouts

An account locks after 5 failed login attempts and unlocks automatically after 15 minutes. Contact the help desk if you're still locked out after 30 minutes.

## VPN issues

Restart the VPN client and confirm multi-factor authentication before escalating a VPN connection issue.

## Hardware issues

Hardware issues are high priority. First response is within 4 business hours during business hours, and the next business day for requests submitted after hours.
```

### Build the skills

The skills handle what the policy document can't answer. This example builds three skills:

- One that searches for similar existing tickets.
- One that explains how an existing ticket was resolved.
- One that files a new ticket as a last resort.

Each skill needs a description of when the genie should use it, the inputs it takes, and the result it returns.

**Search for similar existing tickets**

```text
Add a skill called "Search Jira tickets" that searches our existing Jira tickets for issues similar to the user's question. Use my existing Jira connection. Run this before considering a new ticket. It takes a query string and returns a list of matching tickets with key, summary, status, resolution, and URL, plus a total count.
```

Review the skill's description and the input and output fields AIRO configured before you move on.

**Explain how an existing ticket was resolved**

```text
Add a skill called "Get ticket resolution" that reads a Jira ticket's comments. Use this after finding a similar existing ticket, so the genie can explain how the issue was resolved instead of just saying a duplicate exists. It takes an issue key and returns a list of comments with author, created date, and body, plus a total count.
```

**File a new ticket as a last resort**

```text
Add a skill called "File a new ticket" that files a new Jira ticket in the PLG project, using my existing Jira connection. This is a last resort: Use it only after neither the policy knowledge base nor existing tickets resolve the issue. Require user confirmation before this skill runs. It accepts a question, name, and email. The summary is the question. The description includes the question, name, and email. It returns the created ticket's key and URL.
```

Requiring user confirmation means the end user sees and approves the exact request before the skill files the ticket.

### Create the genie

The genie combines the knowledge base and skills.

Attach the three skills and the knowledge base, and describe the order the genie should work in. You need each skill's handle (`skl-...`) to attach it.

- **In Workato**: AIRO may ask you for each skill's handle. You can also [add existing skills to a genie manually](/en/agentic/agent-studio/create-a-genie#add-existing-skills-to-a-genie).
- **In an MCP client**: AIRO already has each skill's handle from building them earlier in the session.

```text
Create a genie called "Help desk genie" that answers IT support questions. Check the policy knowledge base first. If it doesn't answer the question, search existing Jira tickets and explain how a similar issue was resolved. Only file a new ticket as a last resort, and only after the user confirms. Attach the three skills I just built and the IT support policy knowledge base.
```

AIRO writes a job description, then creates the genie with the knowledge base and skills attached.

Review the job description before you rely on the genie, especially the skill order and the confirmation requirement on ticket filing. Refer to [Create a job description](/en/agentic/agent-studio/create-a-genie#create-a-genie-profile) for how to review and edit it.

## Complete setup in Workato

AIRO creates the assets. Complete the remaining setup in Workato. An MCP client can use the [Developer API MCP server](/en/mcp/developer-api-mcp) for some of these tasks.

- **Start the genie and its skills**: Start the genie manually in Workato, then start each skill separately. Starting the genie doesn't start its skills, and AIRO can't start or stop either one. In an MCP client, use the [Developer API MCP server](/en/mcp/developer-api-mcp)'s recipe start and stop endpoints.
- **Connect the chat interface**: Connect the genie's [chat interface](/en/agentic/agent-studio/chat-interface/chat-interface) manually in Workato.
- **Add end users**: Create an end-user group and add members manually in Workato, or use the [Developer API MCP server](/en/mcp/developer-api-mcp)'s user group endpoints from an MCP client.

## Update an existing genie

Update a genie by describing the specific change, such as a new skill to add or a boundary to set.

### Add a skill to an existing genie

Name the genie, describe the new skill, and say when the genie should use it relative to what it already does.

```text
Open the "Help desk genie" genie. Add a skill that checks a user's password reset status before searching Jira tickets, so the genie can answer that specific question without a ticket search.
```

AIRO loads the genie's current configuration before adding the skill, then rewrites the complete job description to place the new skill in the order.

### Change what a genie won't do

State the new boundary directly and where it fits among the genie's existing constraints.

```text
Update "Help desk genie" so it never discusses an employee's disciplinary history, even if a linked Jira ticket mentions it. Add this to what the genie should avoid.
```

## Build from an MCP client

AIRO Connect exposes each build step as a separate tool to MCP clients such as Claude Code, Claude Desktop, and Cursor. Your client may prompt you to approve operations that modify Workato, such as creating a genie or saving a skill.

Each skill has a `requires_user_confirmation` field that controls confirmation. Set it to `"true"` for a skill that should always ask the end user to approve it first, such as filing a new ticket. The skill's `description` field states when the genie uses the skill.

AIRO Connect builds genies, knowledge bases, and skills, but it can't create a folder, start skills, or create an end-user group. Connect the [Developer API MCP server](/en/mcp/developer-api-mcp) alongside AIRO Connect in the same MCP client to cover those tasks.

Video guide: Build a genie with AIRO Connect and the Developer API MCP server

[Video](https://www.youtube.com/embed/0aV2J-PNkTo)

## Limitations

- AIRO can't start or stop a genie or its skills.
- AIRO can't delete a genie or its skills.
- AIRO can't create a folder.
- AIRO can't create an end-user group.

Manage these manually in Workato, or with the [Developer API MCP server](/en/mcp/developer-api-mcp) from an MCP client.

## Troubleshooting

Most problems come from how a skill is described, whether its confirmation setting is enabled, or whether Workato has finished ingesting and indexing a document uploaded to the knowledge base.

### The genie doesn't use a skill you expect

A genie routes to a skill based on its "when to use it" description, not its name. Ask AIRO to review and rewrite that description, and say when the skill should run relative to the genie's other skills and knowledge bases.

### A skill runs without asking for confirmation

Check the **Require user confirmation before executing skill?** field on the skill's Start workflow trigger in Workato, or ask AIRO to check it. Only this field makes the skill ask for confirmation. Mentioning confirmation in the job description alone doesn't enforce it.

### The genie can't answer from a document you just added

Ingestion runs in the background after you add a document to a knowledge base. Ask AIRO to check the document's status before assuming the upload failed.

### AIRO can't find the genie or skill you expect

Ask AIRO to search by a partial or approximate name, especially if the asset was renamed or is in a different folder than expected.

---
