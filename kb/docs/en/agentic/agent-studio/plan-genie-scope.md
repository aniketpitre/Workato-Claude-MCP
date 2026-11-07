---
url: 'https://docs.workato.com/en/agentic/agent-studio/plan-genie-scope.md'
description: >-
  Learn how to scope a genie for reliability in Agent Studio by defining
  subdomains, designing for a user persona, and writing a focused job
  description.
---

# Plan your genie scope

Your genie is more reliable when your [job description](/en/agentic/agent-studio/ai-model/ai-model#job-description) is clear and focused. A clear and focused job description results in a well-scoped genie. Genies scoped too broadly get built, demoed, and quietly abandoned because they are unreliable in production, hard to maintain, and impossible to improve incrementally.

This page explains how to scope a genie for reliability.

## Define scope using subdomains

A business domain is a broad functional area, such as IT, HR, Sales, or Finance. A subdomain is a focused slice within that domain that serves a specific user persona with a specific set of tasks. The subdomain is the recommended unit to scope your genie.

The following examples show how common business domains break down into well-scoped subdomains:

**HR**

- **Employee self-service**: Leave requests, policy questions, and personal data updates for all employees
- **Recruiting coordination**: Interview scheduling, candidate communication, and requisition tracking for recruiters
- **Onboarding**: New hire task completion, equipment requests, and system access for employees in their first 90 days
- **Benefits administration**: Enrollment, changes, and eligibility questions for benefits-eligible employees

**IT**

- **Employee helpdesk**: Password resets, access requests, and software installation for all employees
- **Incident management**: P1/P2 escalation, stakeholder communication, and resolution tracking for IT support agents
- **License management**: Usage monitoring, optimization recommendations, and provisioning for IT admins
- **Change management**: Change request submission, approval routing, and impact assessment for engineers

**Sales**

- **Account research**: Account summaries, prospect intelligence, and news monitoring for account executives
- **Pipeline management**: Opportunity updates, renewal tracking, and forecast hygiene for sales managers
- **CPQ**: Quote creation, discount approval, and product configuration for deal desk and AEs
- **SDR productivity**: Lead research, outreach drafting, and meeting scheduling for SDRs

## Design for a specific user persona

You must design your genie for a specific user persona in addition to scoping by subdomain.

Genies that serve too many user types receives too many different kinds of requests. This requires different [skills](/en/agentic/skills#getting-started-with-skills), different [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) content, and different response styles. Answer the following questions before you write the job description for your genie:

- **Who is the primary user?**: Name the specific role or persona. This should be a specific person in a specific role doing a specific job.
- **What are the three to five tasks this persona performs most frequently?**: These tasks become your use case categories in the job description.
- **What does this persona already know?**: The genie's response style and level of detail should reflect the persona's existing knowledge.
- **What would this persona never ask?**: Knowing the boundaries of the persona's requirements defines what is out of scope.

Use the following examples to create your persona definition:

| ❌ Not recommended | ✅ Recommended |
| --- | --- |
| `Employees` | `New hires in their first 90 days` |
| `Users` | `Enterprise account executives managing renewals` |
| `Staff` | `IT support agents triaging P1 incidents` |

## Start with a focused genie

Start with a focused scope genie and expand deliberately. A narrow scope ensures that your genie can perform a small number of tasks reliably. You can add use case categories, skills that serve the same persona, and expand the knowledge base with additional content after the genie is in production and working reliably.

A well-scoped genie typically has the following:

- Two to three use case categories in the job description
- Three to five skills
- One focused knowledge base
- One clearly defined user persona

## Scope your genie

Use the following guidelines as a reference to define your genie's scope:

| ❌ Not recommended | ✅ Recommended |
| --- | --- |
| A single genie that handles an entire business domain, such as an HR Genie covering every HR process for every employee type. | A separate genie per subdomain, with each genie built around a specific persona and task set. For example, a leave management genie for individual contributors. |
| A knowledge base that mixes IT policies, HR documentation, sales playbooks, and finance procedures. | A focused knowledge base scoped to one subdomain to ensure that relevant results are retrieved. |
| A genie with many skills across multiple domains, creating ambiguity in skill selection. | Three to five skills within a single domain to enable the LLM to select the correct skill consistently. |
| A job description that covers many scenarios, use cases, and routing rules across domains. | A job description focused on two to three use case categories for one persona. |
| Adding use cases for a different persona to an existing genie | Creating a new genie for a new subdomain and connecting through [Agent orchestration](/en/agentic/agent-studio/agent-orchestration). |

### Governance benefits

A focused genie is also easier to govern:

- **Access control is cleaner**: The user group is clearly defined and the skills it can access are clearly bounded.
- **Audit trails are more meaningful**: Every action maps to a specific subdomain to streamline compliance reviews.
- **Investigations are contained**: The scope of the investigation is limited to a single subdomain when something goes wrong.

Refer to [Genie governance](/en/agentic/agent-studio/genie-governance/genie-governance) for more information.

## Decide how many genies to build

The next step after designing your subdomains is to determine how many genies to build and how they relate to each other. This decision has two parts that must be addressed separately:

**How many genies should exist internally?**: This is an architectural question about how your automation is organized. How many job descriptions, skill sets, and knowledge bases you maintain, and how they relate to each other.

**How many genies should users interact with?**: This is a user experience question about how many entry points users must know about, and whether users choose which genie to use or have that decision made for them.

These questions typically have independent answers. You can have multiple internal genies that users don't see and a single user-facing genie that routes to the internal genies.

Start with the minimum number of genies needed to serve your first use cases. Add genies and orchestration as use cases expand.

### Architecture framework

Use the following questions to determine which architectural option fits your situation:

| Question | Yes | No |
| --- | --- | --- |
| Do your users know which subdomain their request belongs to? | [Option 1](#option-1-multiple-user-facing-genies-per-subdomain) or [Option 3](#option-3-hybrid) | [Option 2](#option-2-single-user-facing-genie-with-internal-orchestration) or [Option 3](#option-3-hybrid) |
| Are cross-domain queries common? | [Option 2](#option-2-single-user-facing-genie-with-internal-orchestration) or [Option 3](#option-3-hybrid) | [Option 1](#option-1-multiple-user-facing-genies-per-subdomain) |
| Do the same builder teams maintain all genies? | Any option | [Option 1](#option-1-multiple-user-facing-genies-per-subdomain) |
| Are skills shared across subdomains? | [Option 2](#option-2-single-user-facing-genie-with-internal-orchestration) or [Option 3](#option-3-hybrid) | [Option 1](#option-1-multiple-user-facing-genies-per-subdomain) |
| Is this your first genie build? | [Option 1](#option-1-multiple-user-facing-genies-per-subdomain) | Any option |

### Option 1: Multiple user-facing genies per subdomain

Each subdomain has its own genie with its own chat interface. Users choose which genie to interact with based on what they need.

- **User experience**: Users select the genie that matches their need. For example, the IT genie in one Slack channel and the HR genie in another.
  
- **Internal architecture**: Each genie is independent, with its own job description, skills, and knowledge base.
  
- **Use this option when**:
  
  - Subdomain boundaries are clear and well understood by users
  - Users reliably know which genie to use for which need
  - Builder teams maintaining each genie are independent
  - Cross-domain queries are rare
- **Watch for**: Your boundaries aren't clear enough if users frequently go to the wrong genie. Consider sharing skills across genies if the same skill is being rebuilt in multiple genies.
  

### Option 2: Single user-facing genie with internal orchestration

A single user-facing genie receives all requests and routes them internally to specialized subdomain genies. Users interact with one genie and don't know that multiple agents are involved.

- **Unified user experience**: Users ask one genie anything within the overall domain, and the genie determines where to route it.
  
- **Internal architecture**: The user-facing genie acts as an orchestrator. It identifies the subdomain and either handles the request directly or delegates to the appropriate specialist genie using the **[Assign task to genie](/en/agentic/agent-studio/agent-orchestration#assign-task-action)** action or the delegate/handover pattern.
  
- **Use this option when**:
  
  - Users don't need to know which subdomain their request belongs to
  - Cross-domain queries are common
  - The builder team maintains all genies and can coordinate orchestration logic
- **Watch for**: The orchestrating genie's job description must be well-structured to route correctly. The limitations of Agent orchestration, including no support for [Verified user access](/en/agentic/agent-studio/verified-user-access) or [Business approvals](/en/agentic/agent-studio/business-approvals), apply to any subdomain genie called this way.
  

### Option 3: Hybrid

Some subdomain genies are user-facing and accessible directly, and others are only accessible through the orchestrating genie.

- **Flexible user experience**: Power users who know which specialist genie they need. Everyone else uses the main genie.
  
- **Internal architecture**: The main genie orchestrates between subdomain genies. Each subdomain genie also has its own chat interface for direct access.
  
- **Use this option when**:
  
  - Some user groups are sophisticated enough to use specialist genies directly
  - Some users benefit from a unified entry point
  - Cross-domain queries are possible but not the majority of interactions
- **Watch for**: Maintaining consistency between the direct experience and the orchestrated experience requires discipline. Users notice if a genie behaves differently when called directly versus through the main genie.
  

## Organize your workspace to match your architecture

The architectural option you choose affects how you organize your Workato workspace:

- **Option 1**: Maps to separate projects per subdomain. Each team maintains their own project with their own skills, knowledge bases, and [App Events](/en/agentic/agent-studio/app-events). Duplicate skills are acceptable because team autonomy outweighs the cost of duplication. Teams can also share skills and knowledge bases across projects without consolidating into a single project. This preserves independent ownership while reducing duplication.
  
- **Options 2 and 3**: Organize related genies together and share skills and knowledge bases across projects as needed. A common project can hold [Data tables](/en/data-tables), functions, and other reusable assets that multiple teams depend on. This approach eliminates skill duplication and simplifies orchestration, but requires coordination between builder teams.

---
