---
url: 'https://docs.workato.com/en/agentic/agent-studio/genie-design-patterns.md'
description: >-
  Learn the eleven genie design patterns in Agent Studio and use the decision
  matrix to choose the right architecture for your build.
---

# Genie design patterns

Every genie has one or more design patterns. Building with patterns intentionally means you can explain and maintain your architecture.

This page provides information on the eleven design patterns available for genie builds and explains how to use the decision matrix to select the right design pattern.

### What is a design pattern

A design pattern is a reusable architectural approach that solves a recurring problem in a known context. Patterns are architectural choices you make at design time before you write a [job description](/en/agentic/agent-studio/ai-model/ai-model#job-description), build a [skill](/en/agentic/skills#getting-started-with-skills), and ingest data into a [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases).

### Eleven genie design patterns

| Pattern | Description |
| --- | --- |
| **Deterministic flow** | The skill sequence is fixed in the job description before execution. The LLM processes output between steps and converses with the user, but the overall flow doesn't vary. |
| **Event router** | A central genie receives events from multiple sources and routes each one to the appropriate skill or skill chain based on pre-defined criteria in the prompt. |
| **Guided skill chaining** | Each skill output determines which skill runs next. The flow is conditional and runtime-determined rather than pre-specified in the job description. |
| **Dynamic input builder** | A single skill adapts to variable input schemas at runtime by fetching the schema definition before building the payload. This eliminates the need for one skill per ticket category or form type. |
| **Query generation** | Object definitions and relationships are loaded into the knowledge base. The LLM generates the required query at runtime from user intent rather than using a pre-defined query. |
| **Persistent state and data enrichment** | The genie stores and retrieves domain-specific data beyond conversational history, enabling reporting over time, stateful workflows, and consistent scoring across sessions. |
| **Information summarization** | The genie collects data from multiple sources and synthesizes it into a single, structured response. |
| **Controlled data volume** | The genie applies filters, aggregation, and pagination before returning data to the LLM to prevent context window overflow when working with large datasets. |
| **Record system** | The genie acts as a lightweight record system using [Data tables](/en/data-tables) for CRUD operations when an external system is unavailable or unnecessary. |
| **App Event-triggered** | An external business event triggers a genie workflow. Two modes: continue an existing conversation or start a new one. |
| **Genie as MCP server** | A [genie exposed as an MCP server](/en/mcp/genies-as-mcp-clients) can be called from Claude, ChatGPT, custom UIs, or other agents. |

### Genie design pattern decision matrix

Find the row that matches your use case across all four dimensions to select your starting pattern:

| Pattern | Workflow characteristics | Decision making | Human interaction | Skill input characteristics |
| --- | --- | --- | --- | --- |
| Deterministic flow | Pre-defined, fixed steps | Not required for steps. Validation may apply. | User reviews step input and output | Derived. Can be dynamic. |
| Event router | Initiated from events. Multiple subscribers. | Pre-defined criteria for routing | Any | Any |
| Guided skill chaining | Pre-defined steps. Complex branching may apply. | Dynamic. Driven from skill outputs. | User reviews step input and output | Any |
| Dynamic input builder | Any | Uses knowledge bases or skills to resolve schema | User reviews step input and output | Dynamic and derived at runtime |
| Query generation | Any | Uses knowledge bases or skills to generate query | User reviews step input and output | Dynamic and derived at runtime |
| Persistent state and data enrichment | Any | Uses knowledge bases or skills before persisting | Any | Any |
| Information summarization | Multiple sources. Pre-defined criteria. | Uses knowledge bases or skills | No intermediate review. Summarize only. | Any |
| Controlled data volume | Multiple sources. Pre-defined criteria to filter data. | Uses knowledge bases or skills | No intermediate review. Summarize only. | Required filters applied to limit output |
| Record system | Pre-defined definition and scope of application | Uses knowledge bases or skills before persisting | User reviews step input and output | Any |
| App Event-triggered | Initiated from external events | Steps decided based on events and criteria | Any | Any |
| Genie as MCP server | Initiated from external events or client calls | Uses knowledge bases or skills | Any | Any |

### Combine patterns for real-world use cases

Most genies use more than one pattern. The patterns are composable. A single genie might use Guided skill chaining as the primary flow, Controlled data volume when a skill returns a large dataset, and Persistent state to store the workflow outcome for reporting.

Identify your primary pattern first. The primary pattern determines the job description structure and the overall skill sequencing logic. Secondary patterns influence how specific skills are designed and how data is handled at specific points in the flow.

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/design-workflows-with-multiple-steps.md
description: >-
  Learn how to design genie workflows with multiple steps using a
  recipe-orchestrated architecture of specialized genies for accurate, reliable
  results.
---

# Design genie workflows with multiple steps

Workflows with multiple steps require multiple genies for accurate processing and results. Complex workflows must be broken down into a recipe-orchestrated architecture that uses multiple specialized genies. This enables your recipe to handle deterministic data retrieval and sequencing, while individual genies focus on specific inference tasks.

Workato recommends that you avoid using a single genie to handle an entire end-to-end business process. A genie asked to perform 20 to 30 steps in a single run loops repeatedly, misses steps, or produces inconsistent results. For example, a team building an expense report review automation creates a genie with seven stated steps but approximately 20-30 sub-steps. The genie is expected to complete the following tasks:

- Retrieve expense report details from Coupa
- Get travel dates for the expense report
- Refer to the Knowledge base to retrieve policies
- Log any policy violations on the overall expense report
- Extract receipt data and validate against the policy for each expense line
- Log violations on individual expense lines
- Summarize findings and route for approval

This workflow design forces the genie to run for an extended time when processing multiple expense lines, which increases chances for hallucination, overblown context, and skipped steps.

You can create a streamlined version of this workflow with multiple genies:

```mermaid
flowchart TD
    a(Recipe triggers: <br/> New expense report in<br>Coupa)
    b(Recipe retrieves <br/> expense report details <br/> from Coupa API)
    c(Recipe retrieves <br/> travel dates from <br/> Calendar API)
    d(<strong>Assign task to Genie 1</strong> <br/> <em>Validate this expense report <br/> against company policies</em>)
    e[(Genie 1: Policy Validator <br/> Reviews report against <br/> Knowledge base policies)]
    f(Genie 1 returns <br/> policy violations and <br/> validation results)
    g(Recipe loops through <br/> each expense line item)
    h(<strong>Assign task to Genie 2</strong> <br/> <em>Validate this expense<br>line against policy<br>requirements</em>)
    i[(Genie 2: Line Item Validator <br/> Checks receipt data <br/> against policy rules)]
    j(Genie 2 returns <br/> line item validation <br/> results)
    k(Recipe aggregates <br/> all validation results)
    l(Recipe routes <br/> for approval)
    a --> b
    b --> c
    c --> d
    d --> e
    e --> f
    f --> g
    g --> h
    h --> i
    i --> j
    j --> k
    k --> l
    classDef WorkatoBlue fill:#5159f6,stroke:#5159f6,stroke-width:2px,color:#fff;
    classDef WorkatoBlue2 fill:#fff,stroke:#5159f6,stroke-width:2px,color:#000;
    classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px;
    class d,h,f,j WorkatoBlue;
    class e,i WorkatoBlue2;
    class a,b,c,g,k,l WorkatoTeal
```

## Create a workflow with multiple genies

Use the following guidelines to create a recipe architecture that supports multiple genies in a single workflow:

- **Recipe as orchestrator**: Create a Workato recipe to manage the overall workflow, such as calling external systems and coordinating genies in a sequence.
- **Deterministic steps in the recipe**: Use deterministic recipe steps to retrieve data, call APIs, and perform predictable transformations in recipe actions rather than through skill calls.
- **Specialized genies for inference**: Use a single genie to handle one focused task that requires judgment, such as `validate this expense report against policy` or `check this individual expense line`.
- **Assign task action for genie invocation**: Use the **[Assign task to genie](/en/agentic/agent-studio/agent-orchestration#assign-task-action)** action to invoke each specialized genie with required context.

## When to use multiple genie orchestration architecture

Use multiple genie orchestration architecture in the following scenarios:

- Expense report review and approval workflows
- Document processing pipelines with validation steps
- Workflows with 10 or more steps that require both inference and deterministic actions
- Processes that iterate over multiple items, such as line items, records, and documents
- Workflows that require different types of expertise at different stages
- Long-running processes that include human approval steps

## Multiple step workflow best practices

Use the following guidelines to build robust workflows with multiple steps:

- **Avoid diluted prompting**: Don't use large job descriptions that include multiple steps for your genie to process. This creates unreliable and inconsistent results.
- **Debug and troubleshoot**: Use individual genies for tasks to enable streamlined debugging and troubleshooting if a genie fails to perform a task properly.
- **Deterministic versus agentic separation**: Add recipe steps that execute the same way, such as expense report retrieval or travel dates retrieval. Save genie invocations for steps that require judgment or inference.
- **Specialized prompting per genie**: Create a focused job description for each genie in a workflow with multiple steps. A genie that validates overall expense reports requires different instructions than a genie checking individual line items.
- **Parallel processing for line items**: Use concurrent genie runs rather than using one genie to loop through line items sequentially when processing items, such as 50 to 100 expense lines. You can use a [Repeat for each loop](/en/recipes/repeat-for-each) to handle parallelism.
- **Consider batching**: Rather than one genie call per line item, evaluate whether a genie can process 5 to 10 items at once. Test for reliability and efficiency.
- **Keep the front-end genie separate**: Use a recipe as an orchestrator for complex processing if users interact with a conversational agent. You can use [Business approvals](/en/agentic/agent-studio/business-approvals) to receive results and notify users.

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/agent-studio/agent-studio-use-cases.md
description: >-
  Explore Agent Studio use cases with step-by-step guides for building genies
  that talk to users, understand requests, and perform actions.
---

# Agent Studio use cases

Agent Studio enables you to use AI-powered agents known as genies that can talk to people, understand what users need, and then perform actions, such as fetch information, run automations, or complete tasks. A genie takes action unlike a typical chatbot that simply provides answers.

Agent Studio use cases provide steps on how perform the following actions:

- Create a genie
- Create and connect a knowledge base
- Create a knowledge base recipe
- Create a skill
- Add [Agent orchestration](/en/agentic/agent-studio/agent-orchestration) to your workflow
- [Upload files and images](/en/agentic/agent-studio/upload-files-and-images) to your genie

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Agent Studio modifications, such as triggers, actions, knowledge base configuration, and skills may require adjustments for your specific setup.

### [Connect your Confluence account to your genie knowledge base](https://docs.workato.com/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case)

This use case enables you to [connect a knowledge base to Confluence](https://docs.workato.com/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case) with knowledge base recipe that scans for pages periodically and automatically syncs and updates available information.

### [Configure a skill to send Slack messages](https://docs.workato.com/en/getting-started/use-cases/agent-studio/skills/slack-send-message-skill)

This use case enables you to [configure a skill that sends Slack messages](https://docs.workato.com/en/getting-started/use-cases/agent-studio/skills/slack-send-message-skill) from your genie's AI model.

### [Upload files and images for Coupa verification](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/expense-genie-coupa-use-case)

This use case enables you to [upload and verify files and images](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/expense-genie-coupa-use-case), such as itemized recipes, before you submit expenses to Coupa.

### [Build a personal assistant genie with Telegram](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/personal-assistant-genie-telegram-agent-orchestration-use-case)

This use case enables you to [build a personal assistant genie in Telegram](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/personal-assistant-genie-telegram-agent-orchestration-use-case) using Agent orchestration.

### [Process purchase orders with a procurement genie](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/procurement-genie-decision-model)

This use case enables you to [configure a procurement genie](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/procurement-genie-decision-model) that uses a decision model to apply deterministic fulfillment rules to purchase order requests.

### [Route requests across agents with a decision model](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/route-requests-across-agents-decision-model)

This use case enables you to [build a front-facing genie](https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/route-requests-across-agents-decision-model) that uses a decision model to route user requests to the correct specialist genie.

## More resources

- [Learn key concepts](/en/workato-concepts)
- [Create your first genie](/en/agentic/agent-studio/genies-configuration#create-your-first-genie)
- [Getting started with knowledge bases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases#getting-started-with-knowledge-bases)
- [Getting started with knowledge base recipes](/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes#getting-started-with-knowledge-base-recipes)
- [Getting started with skills](/en/agentic/skills#getting-started-with-skills)

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case.md
description: >-
  Connect a genie knowledge base to Confluence so it periodically scans pages
  and syncs updates, giving your genie company-specific knowledge.
---

# Connect your knowledge base to Confluence

This use case connects your Confluence account to your genie knowledge base. The knowledge base recipe scans for pages periodically and automatically syncs updates from Confluence to your knowledge base. This gives your genie contextualized information about your company’s policies, practices, and other relevant information.

## What does this knowledge base recipe do?

This knowledge base recipe enables you to connect your knowledge base to your Confluence account and empower your genie with company-specific knowledge.

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph D[&nbsp Create a <br/> genie &nbsp]
      direction LR
    end
    subgraph DD[&nbsp Create a <br/> knowledge base &nbsp]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[&nbsp Create a knowledge <br/> base recipe &nbsp]
        direction LR
    end
    subgraph RRR[Connect your <br/> Confluence account]
        direction LR
    end
  end
  A([Add knowledge <br/> to your genie]) -- Create your genie --> M -- Create a <br/> knowledge base <br/> recipe --> Q --> B([Knowledge retrieval <br/> from custom sources])
  D --> DD
  RR --> RRR

  classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef SubgraphDash fill:#67eadd,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class A,B WorkatoTeal
  class D,DD,RR,RRR SubgraphDash
  class M WorkatoPink
  class Q WorkatoBlue
```

## Create your knowledge base recipe

Complete the following steps to create a knowledge base recipe that scans for pages periodically and automatically syncs updates from Confluence to your knowledge base.

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Knowledge base recipe modifications, such as triggers or custom actions may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Select the project where you plan to create your knowledge base recipe.
   
3. Create a Confluence connection.
   
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
      
   
4. Go to **AI Hub > Agent Studio**.
   
5. Create a genie.
   
   ### Create a genie
   
   This step creates a genie where you can store your knowledge base.
   
   1. Sign in to Workato.
      
   2. Go to **AI Hub > Agent Studio** and click **\+ Create genie**. Alternatively, go to the **Projects** page and click **Create > Genie** or press C+G.
      
   3. Select **New genie** to create a blank genie.
      
   4. Use the **Location** drop-down menu to select a location for your genie.
      
   5. Enter a request or goal for your genie in the **What would you like your genie to help with?** field.
      
      ![Create a genie](/assets/genie-start-building.BqOHwuGZ.png)_Create a genie_
      
   6. Click **Start building**. The genie **Build** page displays.
      
      > **JOB DESCRIPTIONS ARE AUTOMATICALLY GENERATED**
      > 
      > The **Job description** is automatically generated based on the input you provide to the **What would you like your genie to help with?** field during genie setup and can be edited to suit your requirements.
      
      ![Genie build page](/assets/genie-build-page.DQ8_sDC8.png)_Genie build page_
      
   
6. Create a knowledge base.
   
   ### Create a knowledge base
   
   This step creates a knowledge base where you can store your knowledge base recipes.
   
   1. Go to the genie **Build** page.
      
   2. Go to the **Knowledge base** section and click **\+ Add > New knowledge base**.
      
   3. Provide a name for your knowledge base in the **Knowledge base name** field.
      
      ![Create a knowledge base](/assets/add-knowledge-base.D7qlZXNz.png)_Create a knowledge base_
      
   4. Use the **Location** drop-down menu to select a location for your knowledge base.
      
   5. Optional. Enter a description for your knowledge base in the **Description** field. Genies use descriptions to understand the context and purpose of the knowledge base to determine when to use it.
      
   6. Go to the **How will you add data** section and select **Uploads and recipes**.
      
   7. Click **Create knowledge base**.
      
   
7. Create a knowledge base recipe.
   
   ### Connect your knowledge base to Confluence
   
   Knowledge base recipes function like other Workato recipes, but must contain the **Store document in a knowledge base** action. This step connects your Confluence account to your knowledge base.
   
   1. Go to the **Knowledge bases** section and select the knowledge base you created in the preceding steps.
      
   2. Click **\+ Add knowledge**.
      
   3. Select **New knowledge recipe**.
      
   4. Enter a name for your knowledge recipe in the **Recipe name** field.
      
   5. Use the **Location** drop-down menu to select a location for your knowledge recipe.
      
      ![Set up your knowledge recipe](/assets/set-up-knowledge-recipe.DSLepKGW.png)_Set up your knowledge recipe_
      
   6. Click **Start building**. The recipe editor opens with the **Store knowledge in a knowledge base** action automatically selected.
      
      ![Knowledge recipe with Store knowledge in a knowledge base action automatically selected](/assets/knowledge-recipe.CqTvF1Cz.png)_Knowledge recipe with **Store knowledge in a knowledge base** action automatically selected_
      
   
8. Set up your Scheduler by Workato trigger.
   
   ### Set up your Scheduler by Workato trigger
   
   This step triggers your knowledge recipe to refresh Confluence content in your knowledge base every five minutes. This recipe uses the Scheduler by Workato trigger because the Confluence connector doesn't provide a trigger.
   
   1. Click **Select an app and trigger event**.
      
   2. Search for and select `Scheduler by Workato`.
      
   3. Use the **Time unit** drop-down menu to select **Minutes**.
      
   4. Go to the **Trigger every** field and enter **5**.
      
      ![Scheduler by Workato trigger configuration](/assets/scheduler-trigger-configuration.McVsnUVj.png)_Scheduler by Workato trigger configuration_
      
   
9. Click **\+ Add step** before the Step 2 **Store knowledge in a knowledge base**. The **Store knowledge in a knowledge base** action should now be Step 3.
   
10. Select **Action in app**.
    
    ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
    
11. Set up your Confluence Search pages action.
    
    ### Set up your Confluence Search pages action
    
    This step tells your recipe to search Confluence when the trigger activates.
    
    1. Search for and select `Confluence`.
       
    2. Select the **Search pages** action.
       
       ![Select the Search pages action](/assets/search-pages-action.AzikOKBL.png)_Select the **Search pages** action_
       
    3. Select the Confluence connection you set up in the preceding steps. No additional configuration is required for this action.
       
    
12. Click **\+ Add step** before the Step 3 **Store knowledge in a knowledge base**. The **Store knowledge in a knowledge base** action should now be Step 4.
    
13. Set up your Confluence Custom action.
    
    ### Set up your Confluence Custom action
    
    Confluence doesn't have a pre-built action that enables you to retrieve page content for all Confluence documents in a space. You must create custom HTTP request that downloads the content with the **Custom action**.
    
    1. Search for and select `Confluence`.
       
    2. Select **Custom action**.
       
    3. Select the Confluence connection you set up in the preceding steps.
       
    4. Go to the **Action name** field and enter **GET pages**.
       
       ![Name your custom action GET pages](/assets/custom-action.BrwyY58Z.gif)_Name your custom action **GET pages**_
       
    5. Click **Resume guided setup**.
       
    6. Use the **Method** drop-down menu to select **GET**.
       
    7. Go to the **Path** field and enter **content**.
       
       ![Provide your method and path](/assets/confluence-request-url.BQ_6juei.png)_Provide your method and path_
       
    8. Click **Next**.
       
    9. Use the **Response type** drop-down to select **JSON response**.
       
    10. Expand the **Request URL parameters** section.
        
    11. Click **Add URL parameter**.
        
        ![Click Add URL parameter](/assets/add-request-parameter.C1zSYPb2.png)_Click **Add URL parameter**_
        
    12. Go the **Parameter name** field and enter the `spaceKey`, then enter your parameter value in the **Value** field. For example: If your Confluence URL is `https://yoursite.atlassian.net/wiki/spaces/DOCS/pages/`, your API request would look similar to this: `GET /rest/api/content?spaceKey=DOCS`, and you would enter **DOCS**.
        
        ![Configure your URL parameter](/assets/request-parameter.59_knEFL.png)_Configure your URL parameter_
        
    13. Click **\+ Add URL parameter** to add a second parameter.
        
    14. Go the **Parameter name** field and enter the `expand`, then enter your go to the **Value** field and enter `body.view`.
        
    15. Click **Send request**. The **Review response** page displays. You should see `200 OK` followed by the response from the sample request.
        
    16. Verify that the response contains a list of pages from your Confluence space with respective content for each page in the `body.view` property.
        
    17. Click **Apply configuration**.
        
    
14. Go to the recipe builder and select Step 4 **Store knowledge in a knowledge base** action.
    
15. Set up your Store knowledge in a knowledge base action.
    
    ### Set up your Store knowledge in a knowledge base action
    
    This step adds the content pulled from your Confluence account to your knowledge base.
    
    1. Use the **Knowledge base** drop-down menu to select the knowledge base you created in the preceding steps.
       
    2. Expand the **Documents** section.
       
    3. Map the ID (Step 2) datapill to the **Document ID** field.
       
    4. Map the Title (Step 2) datapill to the **Document title** field.
       
    5. Map the Value (Step 3) datapill to the **Document body** field.
       
    6. Map the Self (Step 3) datapill to the **Document URL** field.
       
       ![Set up your Store knowledge in a knowledge base action](/assets/configure-store-document-in-knowledge-base.LVbDn3Dy.png)_Set up your Store knowledge in a knowledge base action_
       
    7. Click **Save**.

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/agent-studio/skills/slack-send-message-skill.md
description: >-
  Add a Slack skill to your genie so it can send a custom message to a channel
  you specify directly from your genie chat.
---

# Send a Slack message

This use case connects your Slack account to your genie as a skill. The skill sends a message to a Slack channel you specify in your genie chat. This gives your genie the ability to push real-time notifications, updates, and alerts directly into your team's Slack workspace.

Watch a quick video guide: Create a new Slack skill in Agent Studio

[Video](https://www.youtube.com/embed/g2USuFRW1-o?rel=0&si=KRzsZFmcxt9j91OJ)

## What does this skill do?

This skill enables your genie to send a custom Slack message to a channel you specify.

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph D[&nbsp Create a <br/> genie &nbsp]
      direction LR
    end
    subgraph DD[&nbsp Create a <br/> skill &nbsp]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RRR[Connect your <br/> Slack account]
        direction LR
    end
    subgraph RR[&nbsp Build the <br/> skill &nbsp]
        direction LR
    end
  end
  A([Add skills <br/> to your genie]) -- Create your genie --> M -- Build a <br/> skill --> Q --> B([Send Slack messages <br/> from your genie])
  D --> DD
  RRR --> RR
  classDef default fill:#fff,stroke:#67eadd,stroke-width:2px;
  classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef SubgraphDash fill:#67eadd,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class A,B WorkatoTeal
  class D,DD,RR,RRR SubgraphDash
  class M WorkatoPink
  class Q WorkatoBlue
```

## Create your skill

Complete the following steps to create a skill that sends a Slack message when triggered by your genie.

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Skill modifications, such as triggers, inputs, or custom actions, may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Select the project where you plan to create your skill.
   
3. Go to **AI Hub > Agent Studio**.
   
4. Create a genie.
   
   ### Create a genie
   
   This step creates a genie where you can store your knowledge base and skills.
   
   1. Sign in to Workato.
      
   2. Go to **AI Hub > Agent Studio** and click **\+ Create genie**. Alternatively, go to the **Projects** page and click **Create > Genie** or press C+G.
      
   3. Select **New genie** to create a blank genie.
      
   4. Use the **Location** drop-down menu to select a location for your genie.
      
   5. Enter a request or goal for your genie in the **What would you like your genie to help with?** field.
      
      ![Create a genie](/assets/genie-start-building.BqOHwuGZ.png)_Create a genie_
      
   6. Click **Start building**. The genie **Build** page displays.
      
      > **JOB DESCRIPTIONS ARE AUTOMATICALLY GENERATED**
      > 
      > The **Job description** is automatically generated based on the input you provide to the **What would you like your genie to help with?** field during genie setup and can be edited to suit your requirements.
      
      ![Genie build page](/assets/genie-build-page.DQ8_sDC8.png)_Genie build page_
      
   
5. Create a skill.
   
   ### Create a skill
   
   This step adds a new skill to your genie where you can build your Slack messaging recipe.
   
   1. Go to the **Enterprise skills** section and click **\+ Add**.
      
   2. Select **Skill**.
      
   3. Select **New skill** and click **Create new skill**.
      
      ![Create a new skill](/assets/create-new-skill.BhFy7Ct5.gif)_Create a new skill_
      
      Alternatively, you can create a skill from the **Projects** page by clicking **Create > Skill** or pressing C+S.
      
   4. Enter `Send Slack message` in the **Skill name** field. A clear, descriptive name allows you and your genie to understand what the skill does at a glance.
      
   5. Use the **Location** drop-down menu to select a location for your skill.
      
   6. Click **Start building**. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
      
   
6. Set up your skill trigger.
   
   ### Set up your skill trigger
   
   This step defines when and why the genie should run this skill, and specifies the inputs it requires from the user.
   
   1. Provide a description for your skill workflow in the **When should your genie run this skill?** field. The genie uses this description to decide when to trigger this workflow. For example:
      
      ```plaintext
      - Run this skill when the user asks to post a goal or initiative update to a Slack channel. For example: Post a message to #general letting the team know that our revenue goal for the quarter is on track and what percentage of our target we've hit.
      - Run this skill when the user asks to announce a new feature release to a Slack channel. For example: Send a message to #product-updates announcing that a new feature has just been released and is now available to all users on the platform.
      ```
      
   2. Go to the **What inputs will your genie require to run this skill?** section and click **Use JSON** or **Add fields manually** to provide a description of the schema recipe parameters. This use case adds the following two inputs:
      
      - **Channel ID** — the ID of the Slack channel the message will be sent to.
      - **Message** — the content of the message to send.
      
      The genie automatically prompts users for the missing information if the input isn't provided in their request.
      
      ![Add required genie inputs](/assets/skill-trigger-input.NHpB7fHm.png)_Add required genie inputs_
      
   3. Go to the **Outputs** section and click **Use JSON** or **Add fields manually** to provide a description of the output. This use case adds the following output:
      
      - **Message ID** — the ID of the Slack message that was sent.
      
      ![Add required genie outputs](/assets/output-trigger.DBHE1CPf.png)_Add required genie outputs_
      
   4. Click **Save**.
      
   
7. Set up your Slack Send message action.
   
   ### Set up your Slack Send message action
   
   This step connects your Slack account and maps the user's inputs to the Slack action.
   
   1. Go to the action block in the recipe editor.
      
   2. Search for and select `Slack` as your app.
      
   3. Select the **Send message** action.
      
   4. Connect your Slack account.
      
      ### Create a Slack connection
      
      This step creates a connection between Workato and your Slack account.
      
      1. Click **Create > Connection** or press C twice.
         
      2. Search for and select `Slack` on the **New connection** page.
         
      3. Enter a name for your connection in the **Connection name** field.
         
         ![Slack connection setup](/assets/connect.CHSRBplW.png)_Slack connection setup_
         
      4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
         
      5. Optional. Configure **Advanced** and **Custom OAuth profile** settings if required for your account type.
         
      6. Click **Connect**.
         
      
   5. Map the Channel ID (Step 1) datapill to the **Channel** field.
      
   6. Map the Message (Step 1) datapill to the **Message** field. This dynamically maps the user's input to the Slack action.
      
      ![Configure your Slack action](/assets/setup-slack-action.C8YFZAFq.png)_Configure your Slack action_
      
   7. Click **Save**.
      
   
8. Configure the Return response action.
   
   ### Configure the Return response action
   
   This step configures the response returned to the genie after the skill executes successfully.
   
   1. Select the **Return response** action in the recipe editor.
      
      ![Configure Return response action](/assets/configure-response.DXGYB8Fh.png)_Configure the **Return response** action_
      
   2. Map the Message ID (Step 2) datapill to the **Message ID** field. You can also include a generic confirmation with the datapill. For example: `Your Slack message has been sent successfully.`
      
      > **RETURN RESPONSE DOWNSTREAM ACTIONS**
      > 
      > The **Return response** action is where you can configure output data for use in downstream actions for other skills, such as returning a record ID or a summary from a database lookup.
      
   3. Click **Save**.
      
   
9. Test your skill.
   
   ### Test your skill
   
   This step verifies that your skill works as expected before you make it available to end users.
   
   1. Return to the Genie Build page and click **Test**.
      
   2. Chat with your genie and enter a request that asks to send a Slack message. For example:
      
      ```plaintext
      
      - Post a message to #sales-team letting the team know that our Q2 revenue goal is on track and we've hit 80% of our target ahead of schedule.
      - Send a message to #general announcing that dark mode has just been released and is now available to all users on the platform.
      ```
      
   3. Verify that the genie executes the skill, sends the message to the specified Slack channel, and returns a confirmation. Edit your recipe and test again if the results aren't correct.
      
      ![Successful Slack post](/assets/slack-post.CR-TTFoP.png)_Successful Slack post_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/expense-genie-coupa-use-case.md
description: >-
  Build an expense genie that connects to Coupa and validates employee expenses
  by extracting data from receipt uploads as the source of truth.
---

# Validate Coupa expenses with an expense genie

This use case connects your Coupa account to a genie configured with specialized skill and knowledge base recipes that turn your genie into a customized expense validator. The skill triggers when a user uploads a receipt image, such as a `jpg`, `png`, or `PDF`.

The genie automates your expense workflow by extracting relevant expenses from employee receipt uploads. This ensures that the receipt is the source of truth and removes the need for manual entry.

## What does this genie do?

This genie enables you to connect your knowledge base to your Coupa account to empower your genie with company-specific knowledge. It uses a custom skill to teach your genie how to validate and process expense receipts."

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph D[Create a <br/> genie &nbsp]
      direction LR
    end
    subgraph DD[&nbsp Add a <br/> detailed job description <br/> and an AI model &nbsp]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[&nbsp Create a knowledge <br/> base recipe &nbsp]
        direction LR
    end
    subgraph RRR[Connect your <br/> Coupa account]
        direction LR
    end
  end
  subgraph N[" "]
    direction LR
    subgraph O[Create a <br/> skill]
        direction LR
    end
    subgraph OO[Give your genie <br/> the ability to determine <br/> when a user wants to submit <br/> an expense and when <br/> they're asking  <br/> expense-related questions. ]
        direction LR
    end
  end

  A([Build a custom <br/> expense genie]) -- Create your genie --> M  -- Optional. Create a <br/> knowledge base <br/> recipe --> Q -- Create skills --> N --> B([Validate expenses before <br/> submitting to Coupa])
  D --> DD
  O --> OO
  RR --> RRR

  classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef WorkatoPurple fill:#fff,stroke:#a99ff5,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#67eadd,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashPurple fill:#a99ff5,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashBlue fill:#5159f6,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
  class A,B WorkatoTeal
  class O,OO SubgraphDash
  class D,DD SubgraphDashPurple
  class RR,RRR SubgraphDashBlue
  class M WorkatoPurple
  class Q WorkatoBlue
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class N SubgraphLight
```

## Create your knowledge base recipe

Complete the following steps to create a custom expense genie that enables you to upload and verify files and images, such as itemized recipes, before you submit expenses to Coupa:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Genie modifications, such as triggers or custom actions, may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Create a Coupa connection.
   
   ### Create a Coupa connection
   
   This step creates a connection between Workato and your Coupa account.
   
   1. Sign in to your Coupa instance, for example `https://[your-instance-name].coupacloud.com/oauth2/clients`.
      
   2. Click **Create** to create a new OAuth client.
      
   3. Use the **Grant type** drop-down menu to select **Authorization Code** or **Client Credentials**. You must select the same option in Workato for the **Authentication type**.
      
   4. Provide a name in the **Name** field. For example: `Workato Coupa OAuth connection`.
      
   5. Enter the redirect URIs you plan to use in the **Redirect URIs** field. Add the link `https://www.workato.com/oauth/callback` if you plan to use **Authorization code**.
      
   6. Select the scopes you plan to provide to Workato. Include all objects and features you plan to automate with the Coupa connector. The scopes you select must match the scopes you configure in Workato. You must include the `core.common.read` and `offline_access` scopes at a minimum to establish a connection.
      
      ![Coupa creating a client](/assets/coupa-create-client.BgDfen2E.png)_Create a new client_
      
   7. Click **Save**.
      
   8. Copy and store the **Identifier** and the **Secret** for use in Workato.
      
   9. Return to your Workato account and go to the project where you plan to add your connection.
      
   10. Click **Create > Connection** or press C twice.
       
   11. Search for and select `Coupa` as your connection on the **New connection** page.
       
   12. Provide a unique name for the connection in the **Connection name** field.
       
   13. Use the **Location** drop-down menu to select the project where you plan to store the connection.
       
   14. Use the **Authentication** drop-down to select the **Grant type** provided in Coupa.
       
   15. Enter the **Client ID** and **Client secret**.
       
   16. Enter the Coupa URL for your instance in the **Host** field. For example, enter `acme` if your URL is `http://acme.coupacloud.com`.
       
   17. Use the **Scopes** drop-down menu to select the same scopes you configured in Coupa. Include the required scopes `core.common.read` and `offline_access` to connect successfully.
       
   18. Click **Connect**.
       
   
3. Create a genie.
   
   ### Create a genie
   
   This step creates a genie where you can store your knowledge base and skills.
   
   1. Sign in to Workato.
      
   2. Go to **AI Hub > Agent Studio** and click **\+ Create genie**. Alternatively, go to the **Projects** page and click **Create > Genie** or press C+G.
      
   3. Select **New genie** to create a blank genie.
      
   4. Use the **Location** drop-down menu to select a location for your genie.
      
   5. Enter a request or goal for your genie in the **What would you like your genie to help with?** field.
      
      ![Create a genie](/assets/genie-start-building.BqOHwuGZ.png)_Create a genie_
      
   6. Click **Start building**. The genie **Build** page displays.
      
      > **JOB DESCRIPTIONS ARE AUTOMATICALLY GENERATED**
      > 
      > The **Job description** is automatically generated based on the input you provide to the **What would you like your genie to help with?** field during genie setup and can be edited to suit your requirements.
      
      ![Genie build page](/assets/genie-build-page.DQ8_sDC8.png)_Genie build page_
      
   
4. Optional. Create a knowledge base.
   
   ### Create a knowledge base
   
   This step creates a knowledge base where you can store your knowledge base recipes. This use case doesn't require a knowledge base. Adding a knowledge base enables you to enhance the genie's capabilities with policy documents or other information sources.
   
   1. Go to the genie **Build** page.
      
   2. Go to the **Knowledge base** section and click **\+ Add > New knowledge base**.
      
   3. Provide a name for your knowledge base in the **Knowledge base name** field.
      
      ![Create a knowledge base](/assets/add-knowledge-base.D7qlZXNz.png)_Create a knowledge base_
      
   4. Use the **Location** drop-down menu to select a location for your knowledge base.
      
   5. Optional. Enter a description for your knowledge base in the **Description** field. Genies use descriptions to understand the context and purpose of the knowledge base to determine when to use it.
      
   6. Go to the **How will you add data** section and select **Uploads and recipes**.
      
   7. Click **Create knowledge base**.
      
   
5. Optional. Create a knowledge base recipe.
   
   ### Create a knowledge base recipe
   
   Knowledge base recipes function like other Workato recipes, but must contain the **Store document in a knowledge base** action. This use case doesn't require a knowledge recipe. However, adding a knowledge base and recipe can enhance your genie with company policies, spending rules, and other internal information.
   
   1. Go to the **Knowledge bases** section and select the knowledge base you created in the preceding steps.
      
   2. Click **\+ Add knowledge**.
      
   3. Select **New knowledge recipe**.
      
   4. Enter a name for your knowledge recipe in the **Recipe name** field.
      
   5. Use the **Location** drop-down menu to select a location for your knowledge recipe.
      
      ![Set up your knowledge recipe](/assets/set-up-knowledge-recipe.DSLepKGW.png)_Set up your knowledge recipe_
      
   6. Click **Start building**. The recipe editor opens with the **Store knowledge in a knowledge base** action automatically selected.
      
      ![Knowledge recipe with Store knowledge in a knowledge base action automatically selected](/assets/knowledge-recipe.CqTvF1Cz.png)_Knowledge recipe with **Store knowledge in a knowledge base** action automatically selected_
      
   
6. Create a skill.
   
   ### Create a skill
   
   This step creates a custom skill that enables your genie to process uploaded images.
   
   1. Go to the genie **Build** page.
      
   2. Go to the **Enterprise skills** section and click **\+ Add > Skill**.
      
   3. Select **New skill** and click **Create new skill**.
      
      ![Select New skill](/assets/create-new-skill.DRmGQ4Wd.png)_Select **New skill**_
      
      Alternatively, you can create a skill from the **Projects** page by clicking **Create > Skill** or pressing C+S.
      
   4. Provide a name for your skill in the **Skill name** field. For example: `Scan images/files into Coupa`
      
   5. Use the **Location** drop-down menu to select a location for your skill.
      
   6. Click **Start building**. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
      
   7. Select the **Start workflow** trigger.
      
   8. Enter the following description for your skill workflow in the **When should your genie run this skill?** field. This description helps the genie recognize when to process an expense versus when a user asks a general question.
      
      ```plaintext
      Run this skill when:
      - A user uploads a receipt image (jpg, png, PDF)
      - The user asks to process an expense, submit an expense, or create an expense report
      - Keywords: "receipt", "expense", "reimbursement", "submit receipt"
      
      Do not run this skill for:
      - General questions about expense policies
      - Questions about past expenses without uploading a receipt
      - Requests to view or search existing expense reports
      ```
      
   9. Go to the **What inputs will your genie require to run this skill?** section and click **Use JSON** to provide a description of the schema recipe parameters.
      
   10. Click **Use JSON**.
       
   11. Paste the following JSON schema into the **JSON sample** field and then click **Next**.
       
       ```json
       {
         "expense_fields_schema": {
           "transaction_date": {
             "type": "date",
             "description": "When the transaction happened",
             "format": "YYYY-MM-DD"
           },
           "amount": {
             "type": "string",
             "description": "Total amount of the receipt or invoice"
           },
           "expense_name": {
             "type": "string",
             "description": "Specific name of the expense"
           },
           "description": {
             "type": "string",
             "description": "Item description"
           },
           "currency": {
             "type": "string",
             "description": "Currency that the expense report is in"
           },
           "expense_category": {
             "type": "string",
             "description": "Specify the predefined categories that is accepted in your expense management system"
           }
         }
       }
       ```
       
   12. Review the sample JSON tree and then click **Generate schema**.
       
   13. Go to the **What should be returned to the genie after this skill is run?** section and click **Use JSON**. The **What should be returned to the genie after this skill is run?** section defines the `RETURN` response for the genie step at the end of your recipe.
       
   14. Paste the following JSON schema into the **JSON sample** field and then click **Next**.
       
       ```json
       {
         "output_fields": {
           "summary_response": {
             "type": "string",
             "description": "Defining this output allows the Genie to return a defined response after the recipe has completed the execution"
           }
         }
       }
       ```
       
   15. Review the sample JSON tree and then click **Generate schema**.
       
   
7. Click **\+ Add step** and select **Handle errors**.
   
   ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **\+ Add step > Handle errors**_
   
   How does the Handle errors control statement work?
   
   The [Handle errors control statement](/en/recipes/steps#handle-errors-step) allows you to monitor your recipe for errors in actions, similar to the try/catch concept in programming languages. You have the opportunity to perform the following actions if an error occurs:
   
   - Retry the sequence of actions again, in case it was a temporary error such as network issues.
     
   - Take remedial actions, such as notifying users of the error through email or error messages in the app, or to carry out a rollback. For example, you can reverse the job by deleting any created or half-created records.
     
   
   This control statement consists of two blocks: the **Monitor** block and the **Error** block. Place the actions that you plan to monitor for errors within the **Monitor** block. If all actions are successful, Workato ignores the **Error** block. However, if any action in the **Monitor** block results in an error, the actions within the **Error** block are executed.
   
   ```mermaid
   graph TD
       A(Monitor action for errors) ---> B((Error found?))
       B --> C{Yes}
       B --> D{No}
       C --> E(Define how to <br/> handle the error)
       D --> F(Continue processing <br/> the recipe)
      classDef default fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
   ```
   
8. Set up your Coupa Create Object action.
   
   This step creates an expense line in Coupa. Note that this step is nested within the Monitor block.
   
   1. Search for and select Coupa as the app to monitor.
      
   2. Select the **Create object** action.
      
   3. Use the **Object** drop-down menu to select **Expense line**.
      
      ![Set up your Expense line action](/assets/coupa-create-object-expense-line.GY0egJc9.gif)_Set up your **Expense line** action_
      
   4. Ensure that **Return type** is set to default.
      
   5. Map the Description (Step 1) datapill to the **Description** field.
      
   6. Map the Transaction date (Step 1) datapill to the **Expense date** and **Start date** fields.
      
   7. Click **Save**.
      
   
9. Configure your ERROR FOUND? block.
   
   This step defines how the recipe responds if the **Expense line** action returns an error.
   
   Complete the following steps to configure your **ERROR FOUND?** block:
   
   1. Go to the **ERROR FOUND?** block and confirm that the **Yes** branch shows **DO NOT RETRY**. This option is typically set by default.
      
      ![Error found block](/assets/error-found-block.B-zgqhof.png)_**ERROR FOUND?** block_
      
   2. Go to the **Yes** branch and click **Select and app and action**.
      
   3. Search for and select `Workato Skill` as your app.
      
   4. Select the **Return response** action.
      
   5. Map the Error type (Step 4) datapill to the **Type** field.
      
   6. Map the Error message (Step 4) datapill to the **Description** field.
      
      ![Map the error information](/assets/error-response.C-yeJTs-.png)_Map the error information_
      
   7. Click **Save**.
      
   8. Go to the **No** branch. The **Return response** action should already be present.
      
   9. Click the **Return response** action to open it.
      
   10. Map the Type (Step 1) datapill to the **Type** field.
       
   11. Map the Description (Step 1) datapill to the **Description** field.
       
       ![Map the error information](/assets/no-error-response.Btk_CXI3.png)_Map the response information_
       
   12. Click **Save**.
       
   

Example genie recipe configuration

![Configured genie recipe example](/assets/configured-genie-recipe.B6UowP-7.png)_Configured genie recipe example_

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/personal-assistant-genie-telegram-agent-orchestration-use-case.md
description: >-
  Build a personal assistant genie that connects to Telegram, processes incoming
  messages, and automates scheduling through a custom skill.
---

# Build a personal assistant genie with Telegram

This use case connects your Telegram account to a genie configured with a specialized skill that turns your genie into a personal assistant. The genie automates your scheduling workflow by intelligently evaluating incoming Telegram messages and creating Google Calendar events for meetings, appointments, or reminders on your behalf. This removes the need to manually switch between apps to log appointments.

## What does this genie do?

This genie enables you to connect Telegram to a Workato recipe and genie to process incoming messages intelligently. It uses a custom skill to teach your genie how to detect calendar events in messages and create Google Calendar events automatically.

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph D[&nbsp Create a <br/> genie &nbsp]
      direction LR
    end
    subgraph DD[&nbsp Add a <br/> detailed job description <br/> and an AI model &nbsp]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[&nbsp Create a <br/> Telegram recipe &nbsp]
        direction LR
    end
    subgraph RRR[Connect your <br/> Telegram bot]
        direction LR
    end
  end
  subgraph N[" "]
    direction LR
    subgraph O[&nbsp Create a <br/> skill &nbsp]
        direction LR
    end
    subgraph OO[Give your genie <br/> the ability to detect <br/> calendar events in messages <br/> and create them <br/> in Google Calendar.]
        direction LR
    end
  end

  A([Build a personal <br/> assistant bot]) -- Create your genie --> M -- Create a <br/> Telegram recipe --> Q -- Create skills --> N --> B([Send and receive messages <br/> and create calendar events])
  D --> DD
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
  class D,DD SubgraphDashPurple
  class N SubgraphLight
  class RR,RRR SubgraphDashBlue
  class M WorkatoPurple
  class Q WorkatoBlue
```

## Build your Telegram personal assistant bot

Complete the following steps to create a personal assistant bot on Telegram that intelligently processes your messages and creates Google Calendar events on your behalf:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Genie modifications, such as triggers, actions, or connection permissions may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Set up your Telegram bot.
   
   ### Set up your Telegram bot
   
   This step creates a new Telegram bot and retrieves the API token needed to connect it to Workato.
   
   1. Sign in to your Telegram app and search for the **@BotFather** account.
      
   2. Start a conversation with **@BotFather** and enter the `/newbot` command.
      
      ![Create a new Telegram bot](/assets/create-telegram-bot.z3bFUQV5.png)_Create a new Telegram bot_
      
   3. Enter a human-readable name for your bot when prompted. For example: `Workato PA genie`.
      
   4. Enter a unique bot username that ends with `bot` when prompted. For example: `workato_bot`.
      
   5. Copy the secret API token that **@BotFather** provides in the confirmation message. You must use this token to connect your bot to Workato.
      
   
3. Create a Telegram connection.
   
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
      
   
4. Create a Google Calendar connection.
   
   ### Create a Google Calendar connection
   
   This step creates a connection between Workato and your Google Calendar account to allow your genie to create calendar events on your behalf.
   
   Refer to the following sections to set up your Google Calendar connection:
   
   #### OAuth 2.0 authentication
   
   Complete the following steps to set up your Google Calendar connection using OAuth 2.0:
   
   View OAuth 2.0 authentication steps
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Google Calendar` as your connection on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
   4. Select the project where you plan to store the connection from the **Location** drop-down menu.
      
   5. Select **OAuth 2.0** as the **Authentication type**.
      
   6. Click **Sign in with Google**, then sign in to your Google account. Ensure your Google account has sufficient permissions to manage the events and calendars you plan to use in Workato. ![Click Sign in with Google](/assets/google-calendar-sign-in-with-google.DQ57V-DM.png)_Click **Sign in with Google**._
      
   
   #### Service account authentication
   
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
   
   ##### Minimum scopes for service account connections
   
   The following scopes are required to connect to Google Calendar using a service account:
   
   - `https://www.googleapis.com/auth/calendar`
   - `https://www.googleapis.com/auth/calendar.events`
   - `https://www.googleapis.com/auth/admin.directory.resource.calendar`
   - `https://www.googleapis.com/auth/tasks`
   - `https://www.googleapis.com/auth/userinfo.email`
   
   A `401 Unauthorized error` may occur when the service account uses the `Owner` role or lacks required scopes. Assign the `Editor` role to the service account in the Google Cloud Console and confirm it includes all required scopes listed above. This ensures the service account can authenticate and access Google Calendar successfully.
   
   Refer to the [Google Calendar API scopes](https://developers.google.com/calendar/api/auth) documentation for a complete list of supported scopes.
   
   ##### Set up a Google service account
   
   View Set up a Google service account steps
   
   Complete the following steps to set up a Google service account:
   
   1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
      
   2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account. ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
      
   3. Click the **Email** of the service account you intend to use. ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
      
   4. Copy the service account's **Email** and save it to configure your connection later. ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
      
   5. Go to the **KEYS** tab.
      
   6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
      
   7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
      
   
   ##### Enable the Google Calendar API
   
   View Enable the Google Calendar API steps
   
   You must enable the Google Calendar API before you return to Workato to finish setting up your connection.
   
   1. Sign in to Google's [API library](https://console.developers.google.com/apis/library).
      
   2. Search for and select the `Google Calendar API`.
      
   3. Click **Enable** to enable the API. ![Enable the Google Calendar API](/assets/google-calendar-api.DMWBkrRb.png)_**Enable** the `Google Calendar API`_
      
   
   #### Complete setup in Workato
   
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
   
   This step creates a genie that intelligently processes incoming Telegram messages and decides when to create a calendar event Google Calendar.
   
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
      
   9. Enter a description that instructs the genie to process the incoming message and use the Google Calendar skill when appropriate in the **Task Description** field.
      
   10. Map the Telegram trigger Text (Step 1) datapill after your description in the **Task Description** field.
       
       ![Configure the Task Description field](/assets/genie-task-description.DGPRTrDw.png)_Configure the **Task Description** field_
       
   11. Click **Save**.
       
   
7. Create a Data table to store conversation IDs.
   
   ### Create a Data table to store conversation IDs
   
   This step creates a Data table to persist the genie's conversation ID against each Telegram user's ID. This allows the genie to retain context across multiple messages from the same user.
   
   1. Go to the project where you plan to store your data table and click **Create > Data table** or press C+T.
      
   2. Enter a name for your Data table in the **Data table name** field.
      
   3. Use the **Location** drop-down menu to select a location for your Data table.
      
   4. Click **Start building**.
      
   5. Add a column with the label `telegram-id` to store the Telegram user's sender ID.
      
   6. Add a second column with the label `genie-conversation-id` to store the genie's conversation ID.
      
      ![Add columns to your data table](/assets/create-a-data-table.MXv1Z3Y8.png)_Add columns to your data table_
      
   7. Click **Save**.
      
   
8. Add the Conversation ID to the recipe.
   
   ### Add the Conversation ID to the recipe
   
   This steps adds a Workato Data tables **Search records** action that allows the recipe to refer to the Data table to see if the sender's Telegram ID has a corresponding Conversation ID in the data table. An existing Conversation ID indicates that there's a previous conversation which the genie can refer to.
   
   1. Return the recipe editor and click **\+ Add step** _before_ the **Assign task to genie** action step.
      
   2. Select **Action in app**, search for `Workato Data Tables`, and select it as your app.
      
   3. Select the **Search records** action.
      
   4. Use the **Data table** drop-down menu to select the data table you created in the preceding steps.
      
   5. Go to the **Filter** section and click **Add filter**.
      
   6. Use the **Column name** drop-down menu to select **telegram-id**.
      
   7. Use the **Operand** drop-down menu to select **equals**.
      
   8. Map the Telegram ID (Step 1) datapill to the **Value** field. This datapill is located under Telegram > Message > From.
      
      ![Configure the data table to search Telegram](/assets/telegram-data-table-configuration.BvJOfw8t.gif)_Configure the data table to search Telegram_
      
   9. Click **\+ Add step** _after_ the **Assign task to genie** action step.
      
   10. Select **Action in app**, search for `Workato Data Tables`, and select it as your app.
       
   11. Select the **Upsert record** action.
       
   12. Use the **Data table** drop-down menu to select the data table you created in the preceding steps.
       
       ![Configure the Upsert record action](/assets/upsert-record-action.B59Jf31_.gif)_Configure the **Upsert record** action_
       
   13. Use the **Primary key** drop-down menu to select **telegram-id**.
       
   14. Go to the **Record fields** section and map the Telegram From ID (Step 1) datapill to the **telegram-id** field.
       
   15. Map the Workato Genie Conversation ID (Step 3) datapill to the **genie-conversation-id** field.
       
   16. Click **Save**.
       
   
9. Create a skill to convert messages into Google Calendar events.
   
   ### Create a skill to convert messages into Google Calendar events
   
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
       
   19. Go to the **Yes** branch and click **Select and app and action**.
       
   20. Search `Workato Genie` and select it as your app.
       
   21. Select **Return response to genie** as your action.
       
   22. Go to the **Results** section and use the **Created Event** drop-down menu to select **Yes**.
       
       ![Set up your IF condition](/assets/if-condition-setup.BsASC_IL.png)_Set up your IF condition_
       
   23. Go to the **No** branch. The **Return response to genie** action should already be present.
       
   24. Click the **Return response to genie** action to open it.
       
   25. Configure the **Yes** and **No** paths of the **IF** block to return the appropriate `created_event` boolean response to the genie.
       
   26. Click **Save**.
       
   
10. Update your genie task description.
    
    ### Update your genie task description
    
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
  https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/procurement-genie-decision-model.md
description: >-
  Build a procurement genie that uses a decision model to evaluate purchase
  order requests and decide whether to accept, reject, or back-order them.
---

# Process purchase orders with a procurement genie

This use case configures a procurement genie with a skill that calls a [decision model](/en/recipes/decision-models) to evaluate purchase order requests. Rather than encoding business rules in prompts, the decision model applies your organization's fulfillment logic, such as holiday freezes, price deviation thresholds, and inventory checks, and returns a deterministic decision that the skill uses to route the order.

## What does this genie do?

This genie processes purchase order requests from users and uses a decision model in a skill to determine whether to accept, reject, or back-order the purchase.

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph D[&nbsp Create a <br/> genie &nbsp]
      direction LR
    end
    subgraph DD[&nbsp Add a job description <br/> and AI model &nbsp]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[&nbsp Create a <br/> decision model &nbsp]
        direction LR
    end
    subgraph RRR[&nbsp Define fulfillment rules <br/> as a decision table &nbsp]
        direction LR
    end
  end
  subgraph N[" "]
    direction LR
    subgraph O[&nbsp Create a <br/> skill recipe &nbsp]
        direction LR
    end
    subgraph OO[&nbsp Call the decision model <br/> and route on output &nbsp]
        direction LR
    end
  end

  A([Procurement genie <br/> with decision model]) -- Create genie --> M -- Create decision model --> Q -- Create skill --> N --> B([Deterministic purchase <br/> order decisions])
  D --> DD
  RR --> RRR
  O --> OO
  classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef WorkatoPurple fill:#fff,stroke:#a99ff5,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#67eadd,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashPurple fill:#a99ff5,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashBlue fill:#5159f6,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
  class A,B WorkatoTeal
  class O,OO SubgraphDash
  class D,DD SubgraphDashPurple
  class RR,RRR SubgraphDashBlue
  class M WorkatoPurple
  class Q WorkatoBlue
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class N SubgraphLight
```

## Create your procurement genie

Complete the following steps to build a procurement genie that uses a decision model to process purchase orders:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Genie modifications, such as triggers or custom actions, may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Select the project where you plan to create your genie and skill.
   
3. Go to **AI Hub > Agent Studio**.
   
4. Create a genie.
   
   ### Create a genie
   
   This step creates the procurement genie that users will interact with to submit and check purchase orders.
   
   1. Sign in to Workato.
      
   2. Go to **AI Hub > Agent Studio** and click **\+ Create genie**. Alternatively, go to the **Projects** page and click **Create > Genie** or press C+G.
      
   3. Select **New genie** to create a blank genie.
      
   4. Use the **Location** drop-down menu to select a location for your genie.
      
   5. Enter a request or goal for your genie in the **What would you like your genie to help with?** field.
      
      ![Create a genie](/assets/genie-start-building.BqOHwuGZ.png)_Create a genie_
      
   6. Click **Start building**. The genie **Build** page displays.
      
      > **JOB DESCRIPTIONS ARE AUTOMATICALLY GENERATED**
      > 
      > The **Job description** is automatically generated based on the input you provide to the **What would you like your genie to help with?** field during genie setup and can be edited to suit your requirements.
      
      ![Genie build page](/assets/genie-build-page.DQ8_sDC8.png)_Genie build page_
      
   
5. Create the decision model.
   
   ### Create the decision model
   
   This step defines the fulfillment rules your skill will use to evaluate purchase orders. The decision model is the single source of truth for your business logic. Rules can be updated here independently of the genie or skill.
   
   1. Go to **Projects** and click **Create > Decision model**.
      
   2. Enter a name for your decision model in the **Decision model name** field. For example: `Purchase order fulfillment`.
      
   3. Click **Start building**.
      
   4. Define your input schema in the **Model Inputs** node. These are the fields your skill will supply when calling the model. For example:
      
      - `supplier_score` (Number): The supplier's risk or performance score
      - `risk_level` (String): The supplier's risk classification, such as `Low`, `Medium`, or `High`
      - `request_type` (String): The type of purchase request, such as `Standard` or `Emergency`
      - `order_value` (Number): The total value of the purchase order
      - `lead_time_days` (Number): The supplier's current lead time in days
      - `current_stock` (Number): Current inventory level for the ordered item
      
      ![Define the decision model input schema](/assets/input-node.CToAL0vt.png)_Add fields to the **Model Inputs** node_
      
   5. Go to the **Fields** sidebar and create a `decision` field (String). This field carries the model's output, such as `Approved`, `Rejected`, `Escalate`, or `Review`, back to the skill.
      
   6. Configure the **Model Outputs** node to return `decision`.
      
   7. Open the **Decision table** node and add your fulfillment rules as rows. Rules are evaluated top to bottom: the first row that matches all conditions determines the output. You can also set a **Default output** that applies when no rule matches. For example:
      
      | Rule name | Supplier score | Risk level | Request type | Order value | Lead time days | Current stock | Decision |
      | --- | --- | --- | --- | --- | --- | --- | --- |
      | No stock | Any | Any | Any | Any | Any | < 0 | `Rejected` |
      | Emergency reorder | Any | Any | `Emergency` | Any | Any | \> 100 | `Approved` |
      | High risk supplier | < 50 | `High` | `Standard` | Any | Any | Any | `Rejected` |
      | Large order escalate | Any | Any | `Standard` | \> 100000 | Any | Any | `Escalate` |
      | Trusted supplier | ≥ 80 | `Low` | Any | ≤ 50000 | Any | Any | `Approve` |
      | Long lead time review | Any | `Medium` | `Standard` | Any | \> 14 | < 500 | `Review` |
      | Standard approval | ≥ 60 | `Low` | `Standard` | ≤ 25000 | ≤ 7 | Any | `Approve` |
      | **Default output** | — | — | — | — | — | — | `Review` |
      
      ![Configure fulfillment rules in the decision table](/assets/procurement-genie-decision-table.CoXe6CNi.png)_Add fulfillment rules as rows in the decision table_
      
   8. Click **Save**.
      
   
6. Create a skill.
   
   ### Create a skill
   
   This step adds a new skill to your genie where you can build the purchase order processing recipe.
   
   1. Go to the genie **Build** page.
      
   2. Go to the **Enterprise skills** section and click **\+ Add**.
      
   3. Select **Skill**.
      
   4. Select **New skill**.
      
   5. Click **Create new skill**.
      
      Alternatively, you can create a skill from the **Projects** page by clicking **Create > Skill** or pressing C+S.
      
   6. Enter a name for your skill in the **Skill name** field. For example: `Process purchase order`.
      
   7. Use the **Location** drop-down menu to select a location for your skill.
      
   8. Click **Start building**. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
      
   
7. Set up your skill trigger.
   
   ### Set up your skill trigger
   
   This step tells the genie when to invoke this skill and what information to extract from the user's message.
   
   1. Select the **Start workflow** trigger.
      
   2. Enter a description in the **When should your genie run this skill?** field. For example:
      
      ```plaintext
      Run this skill when a user submits a purchase order or asks whether a purchase order will be fulfilled. Extract the product ID, order value, and request type from the user's message.
      
      Do not run this skill for:
      - General questions about procurement policy
      - Requests to look up order history
      ```
      
   3. Go to the **What inputs will your genie require to run this skill?** section and add the fields the genie will extract from the user's message and pass to the recipe. For example:
      
      - `product_id` (String): The product being ordered
      - `order_value` (Number): The total value of the purchase order
      - `request_type` (String): The type of purchase request, such as `Standard` or `Emergency`
   4. Go to the **What should be returned to the genie after this skill is run?** section and add a `decision_result` (String) output field. The skill uses this to return the fulfillment outcome to the genie.
      
   5. Click **Save**.
      
   
8. Set up the Decision Models action.
   
   ### Set up the Decision Models action
   
   This step adds the **Decision Models by Workato** connector to the skill and maps the purchase order data to the decision model's inputs.
   
   1. Add any steps needed to fetch data the decision model requires before making a decision. For example, use the **Search** action in a connector such as NetSuite to look up supplier risk scores and current inventory levels for the submitted `product_id`.
      
   2. Click **\+ Add step** in the recipe editor.
      
   3. Search for and select **Decision Models by Workato**.
      
   4. Select the **Make a decision** action.
      
   5. Use the **Model name** drop-down to select your `Purchase order fulfillment` model.
      
   6. Map the input datapills to the model's input fields. For example:
      
      - `order_value` → Order value (Step 1) from the skill trigger
      - `request_type` → Request type (Step 1) from the skill trigger
      - `supplier_score` → Supplier score from your supplier lookup step
      - `risk_level` → Risk level from your supplier lookup step
      - `lead_time_days` → Lead time days from your supplier lookup step
      - `current_stock` → Current stock from your supplier lookup step
      
      ![Map datapills to decision model inputs](/assets/decision-model-input-mapping.BXbSnkdI.png)_Map datapills from earlier recipe steps to the decision model's input fields_
      
   7. Click **Save**.
      
   
9. Configure the Return Response to Genie block.
   
   ### Configure the Return Response to Genie block
   
   This step returns the decision model's output to the genie so it can relay the fulfillment outcome to the user.
   
   1. Select **Return Response to Genie** in the recipe editor.
      
   2. Map the Decision output datapill from the **Make a decision** step to the `decision_result` output field. The genie uses this value to inform the user of the fulfillment outcome.
      
   3. Click **Save**.
      
   
10. Test your skill.
    
    ### Test your skill
    
    This step verifies that your genie correctly invokes the skill and that the decision model returns the expected fulfillment decision.
    
    1. Return to the genie **Build** page and click **Test**.
       
    2. Enter a purchase order request in the chat. For example:
       
       ```plaintext
       I'd like to submit a purchase order for product SKU-1234, order date today, at $450. Can you process this?
       ```
       
    3. Verify that the genie invokes the skill, the decision model evaluates the order against your rules, and the genie returns the fulfillment decision. Edit your decision table or skill and test again if the results aren't correct.

---

---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/agent-studio/genies/route-requests-across-agents-decision-model.md
description: >-
  Build a front-facing genie that uses a decision model to route each user
  request to the right specialist genie based on its category.
---

# Route requests across agents with a decision model

This use case configures a front-facing genie that uses a [decision model](/en/recipes/decision-models) to route user requests to the correct specialist genie. Rather than relying on prompts to determine which agent should handle a request, the decision model applies predefined routing rules deterministically, giving you full control, auditability, and testability over how requests are distributed across your agent network.

End users interact with a single genie. Behind the scenes, the decision model routes each request to the appropriate specialist genie based on the request category and other criteria you define.

## What does this genie do?

This genie receives user requests, extracts the request category and domain, and uses a decision model in a skill to assign the request to the correct specialist genie.

```mermaid
flowchart TD
  subgraph M[" "]
    direction LR
    subgraph D[&nbsp Create a <br/> front-facing genie &nbsp]
      direction LR
    end
    subgraph DD[&nbsp Single interface <br/> for end users &nbsp]
        direction LR
    end
  end
  subgraph Q[" "]
    direction LR
    subgraph RR[&nbsp Create a <br/> routing decision model &nbsp]
        direction LR
    end
    subgraph RRR[&nbsp Define routing rules <br/> as a decision table &nbsp]
        direction LR
    end
  end
  subgraph N[" "]
    direction LR
    subgraph O[&nbsp Create a <br/> routing skill &nbsp]
        direction LR
    end
    subgraph OO[&nbsp Route to specialist <br/> genies based on output &nbsp]
        direction LR
    end
  end

  A([Multi-agent routing <br/> with decision model]) -- Create genie --> M -- Create decision model --> Q -- Create skill --> N --> B([Deterministic routing <br/> to specialist genies])
  D --> DD
  RR --> RRR
  O --> OO
  classDef WorkatoTeal fill:#67eadd,stroke:#67eadd,stroke-width:2px,color:#000;
  classDef WorkatoPink fill:#fff,stroke:#f66,stroke-width:2px;
  classDef WorkatoBlue fill:#fff,stroke:#5159f6,stroke-width:2px,color:#fff;
  classDef WorkatoPurple fill:#fff,stroke:#a99ff5,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#67eadd,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashPurple fill:#a99ff5,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  classDef SubgraphDashBlue fill:#5159f6,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
  class A,B WorkatoTeal
  class O,OO SubgraphDash
  class D,DD SubgraphDashPurple
  class RR,RRR SubgraphDashBlue
  class M WorkatoPurple
  class Q WorkatoBlue
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class N SubgraphLight
```

## Set up your routing genie

Complete the following steps to build a front-facing genie that uses a decision model to route requests to specialist genies:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> Use cases are intended to serve as examples. Genie modifications, such as triggers or custom actions, may require adjustments for your specific setup.

1. Sign in to Workato.
   
2. Select the project where you plan to create your genie and skill.
   
3. Go to **AI Hub > Agent Studio**.
   
4. Create a front-facing genie.
   
   ### Create a front-facing genie
   
   This step creates the genie that end users interact with. This genie acts as a single entry point and delegates requests to specialist genies behind the scenes.
   
   1. Sign in to Workato.
      
   2. Go to **AI Hub > Agent Studio** and click **\+ Create genie**. Alternatively, go to the **Projects** page and click **Create > Genie** or press C+G.
      
   3. Select **New genie** to create a blank genie.
      
   4. Use the **Location** drop-down menu to select a location for your genie.
      
   5. Enter a request or goal for your genie in the **What would you like your genie to help with?** field.
      
      ![Create a genie](/assets/genie-start-building.BqOHwuGZ.png)_Create a genie_
      
   6. Click **Start building**. The genie **Build** page displays.
      
      > **JOB DESCRIPTIONS ARE AUTOMATICALLY GENERATED**
      > 
      > The **Job description** is automatically generated based on the input you provide to the **What would you like your genie to help with?** field during genie setup and can be edited to suit your requirements.
      
      ![Genie build page](/assets/genie-build-page.DQ8_sDC8.png)_Genie build page_
      
   
5. Create the routing decision model.
   
   ### Create the routing decision model
   
   This step defines the routing rules that determine which specialist genie handles each request. The decision model is maintained independently of the genie, so you can update routing logic without modifying any skills or prompts.
   
   1. Go to **Projects** and click **Create > Decision model**.
      
   2. Enter a name for your decision model in the **Decision model name** field. For example: `Request routing`.
      
   3. Click **Start building**.
      
   4. Define your input schema in the **Model Inputs** node. These are the fields the front-facing genie will extract from the user's message and pass to the model. For example:
      
      - `domain` (String): The area of the request, such as `Software/App`, `Device/Hardware`, or `Office/Facilities`
      - `purchase_needed` (Boolean): Whether the request requires a purchase
      - `catalog_type` (String): The catalog category for purchase requests, such as `IT`, `Office`, or `Not in catalog`
      
      ![Decision model input schema](/assets/input-node.CToAL0vt.png)_Add fields to the **Model Inputs** node_
      
   5. Go to the **Fields** sidebar and create a `genie` field (String). This field returns the name of the specialist genie the request should be routed to.
      
   6. Configure the **Model Outputs** node to return `genie`.
      
   7. Open the **Decision table** node and add your routing rules as rows. Rules are evaluated top to bottom: the first matching row determines the output. You can also set a **Default output** that applies when no rule matches. For example:
      
      | Rule name | Domain | Purchase needed | Catalog type | Genie |
      | --- | --- | --- | --- | --- |
      | New purchases | Any | `true` | `Not in catalog` | `Procurement` |
      | IT purchases | Any | `true` | `IT` | `IT` |
      | Office purchases | Any | `true` | `Office` | `Office Management` |
      | Office/Facilities issues | `Office/Facilities` | Any | Any | `Office Management` |
      | Printing/AV issues | `Printing/AV` | Any | Any | `Office Management` |
      | Software issues | `Software/App` | Any | Any | `IT` |
      | Hardware issues | `Device/Hardware` | Any | Any | `IT` |
      | Network/VPN issues | `Network/VPN` | Any | Any | `IT` |
      | Access/Account issues | `Access/Account` | Any | Any | `IT` |
      | **Default output** | — | — | — | `Escalation` |
      
      ![Configure routing rules in the decision table](/assets/request-routing-decision-table.CrpcPoxE.png)_Add routing rules as rows in the decision table_
      
   8. Click **Save**.
      
   
6. Create a skill.
   
   ### Create a skill
   
   This step adds a routing skill to your front-facing genie.
   
   1. Go to the genie **Build** page.
      
   2. Go to the **Enterprise skills** section and click **\+ Add**.
      
   3. Select **Skill**.
      
   4. Select **New skill** and click **Create new skill**.
      
      Alternatively, you can create a skill from the **Projects** page by clicking **Create > Skill** or pressing C+S.
      
   5. Enter a name for your skill in the **Skill name** field. For example: `Route request to specialist`.
      
   6. Use the **Location** drop-down menu to select a location for your skill.
      
   7. Click **Start building**. The recipe editor opens with the **Start workflow** trigger and **Return response** action automatically selected.
      
   
7. Set up your skill trigger.
   
   ### Set up your skill trigger
   
   This step defines when the genie should invoke the routing skill and what information it needs to extract from the user's message.
   
   1. Select the **Start workflow** trigger.
      
   2. Enter a description in the **When should your genie run this skill?** field. For example:
      
      ```plaintext
      Run this skill for every new request that needs to be routed to a specialist. Extract the domain, whether a purchase is needed, and the catalog type from the user's message before invoking this skill.
      ```
      
   3. Go to the **What inputs will your genie require to run this skill?** section and add the fields the genie will extract and pass to the recipe. For example:
      
      - `domain` (String): The area of the request extracted from the user's message
      - `purchase_needed` (Boolean): Whether the request requires a purchase
      - `catalog_type` (String): The catalog category for purchase requests
   4. Click **Save**.
      
   
8. Set up the Decision Models action.
   
   ### Set up the Decision Models action
   
   This step calls the routing decision model and retrieves the name of the specialist genie to assign the request to.
   
   1. Click **\+ Add step** in the recipe editor.
      
   2. Search for and select **Decision Models by Workato**.
      
   3. Select the **Make a decision** action.
      
   4. Use the **Model name** drop-down to select your `Request routing` model.
      
   5. Map the input datapills to the model's input fields:
      
      - `domain` → Domain (Step 1) from the skill trigger
      - `purchase_needed` → Purchase needed (Step 1) from the skill trigger
      - `catalog_type` → Catalog type (Step 1) from the skill trigger
      
      ![Map datapills to routing decision model inputs](/assets/routing-decision-model-mapping.0WaxyOLn.png)_Map skill trigger datapills to the routing model's input fields_
      
   6. Click **Save**.
      
   
9. Set up the agent orchestration action.
   
   ### Set up the agent orchestration action
   
   This step uses IF conditions to branch on the decision model's `Genie` output and assign the task to the correct specialist genie using [agent orchestration](/en/agentic/agent-studio/agent-orchestration).
   
   1. Click **\+ Add step** in the recipe editor.
      
   2. Select **IF condition**.
      
   3. Set the **Data field** to the Genie output datapill from the **Make a decision** step, set **Condition** to `equals`, and enter the name of the first specialist genie as the **Value**, for example, `IT`.
      
   4. Go to the **Yes** branch, click **\+ Add step**, search for and select **Workato Genie**, and select the **Assign a task to genie** action.
      
   5. Configure the action to assign the request to the matching specialist genie.
      
   6. Repeat steps 1–3 for each routing value from the decision model, for example, `Office Management` and `Procurement`. Each branch can assign the task to a specialist genie or trigger a different action. For example, an `Escalation` branch could update a Jira issue and assign it to an on-call team instead of routing to a genie.
      
      ![Configure agent orchestration IF conditions](/assets/agent-orchestration-action.B3JLqonc.png)_Add an IF condition and action step for each routing value_
      
   7. Click **Save**.
      
   
10. Test your skill.
    
    ### Test your skill
    
    This step verifies that the front-facing genie correctly routes requests to the appropriate specialist genie.
    
    1. Return to the genie **Build** page and click **Test**.
       
    2. Enter requests that should route to different specialist genies. For example:
       
       ```plaintext
       I need to order new monitors for my team.
       ```
       
       ```plaintext
       My laptop won't connect to the VPN and I have a presentation in an hour.
       ```
       
    3. Verify that the genie invokes the skill, the decision model returns the correct specialist genie for each request, and the orchestration action assigns the task accordingly. Edit your decision table and test again if any requests are routed incorrectly.
       
    

## More resources

- [Decision models](/en/recipes/decision-models)
- [Decision Models by Workato connector](/en/features/decision-models/decision-models-by-workato)
- [Agent orchestration](/en/agentic/agent-studio/agent-orchestration)
- [Process purchase orders with a procurement genie](/en/getting-started/use-cases/agent-studio/genies/procurement-genie-decision-model)

---
