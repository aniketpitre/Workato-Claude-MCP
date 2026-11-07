---
url: 'https://docs.workato.com/en/agentic/skills/skill-prompt.md'
description: >-
  Learn how to write effective skill prompts using a complete template so the
  LLM reliably decides when to invoke a skill and how to use it.
---

# Skill prompt

The skill prompt is the description the LLM reads when deciding whether to invoke a skill and how to use it. A well-written skill prompt produces reliable invocation and accurate skill selection.

This page provides a complete template with examples to help you write effective skill prompts. Ensure that you review each section of the template to understand what each part of the skill prompt does and why it matters.

## Skill prompt template

Every skill prompt should use the following template:

```plaintext
Purpose: [One-line summary of what the Skill does]

Description: [Two to three sentence explanation of
the Skill's functionality, what system it interacts
with, and what it returns]

When to Use:
- [Specific scenario 1 where this Skill is appropriate]
- [Specific scenario 2]
- [Specific scenario 3 if needed]

When NOT to Use:
- [Scenario where a different Skill should be used instead]
- [Limitation or constraint that disqualifies this Skill]
- [Scenario where no Skill should be called]

Input Requirements:
- [Field name]: [How to populate it, where the value
  comes from, format requirements, valid values]
- [Field name]: [Repeat for each input field]

Output Requirements:
- [What the Skill returns and how the Genie should
  use or present it]
- [Whether a source URL should be cited]
- [Any formatting instructions for the output]
```

### Purpose

The purpose is a single sentence that summarizes what the skill does. It's the first thing the LLM reads when evaluating whether to invoke this skill for a user request. The purpose line should be specific enough that the LLM can distinguish this skill from other skills without reading further. If two skills have similar purpose lines, the LLM struggles to choose between them.

Write it in the form: `[Action] [object] [in/from system]`

**Recommended** ✅

```plaintext
Purpose: Submits a leave request to Workday
on behalf of the requesting user.
```

```plaintext
Purpose: Retrieves an account summary from
Salesforce including open opportunities,
key contacts, and recent activity.
```

```plaintext
Purpose: Creates a support ticket in Jira
Service Management with the specified
category and priority.
```

**Not recommended** ❌

```plaintext
Purpose: Leave stuff.
```

```plaintext
Purpose: This Skill handles leave requests
in the HR system and does the submission
thing when users want time off.
```

```plaintext
Purpose: Workday API call.
```

### Description

The description expands on the purpose in two to three sentences. It covers what system the skill interacts with, what the skill does internally if that context helps the LLM use it correctly, and what it returns. The description is where context that doesn't fit in a single purpose line goes. It's also where you can note any prerequisites if prerequisites aren't already captured in the When to Use section. For example: `this skill should only be called after the user has confirmed the request details`

**Recommended** ✅

```plaintext
Description: Calls the Workday absence
management API to create a leave request
record for the authenticated user. Accepts
the leave type, start date, end date, and
an optional reason. Returns the request
reference number and submission status.
```

**Not recommended** ❌

```plaintext
Description: Calls the Workday API.
```

### When to Use

When to Use is a list of specific scenarios that should trigger this skill. This includes the skill's general applicability with concrete and specific conditions that map to real user requests. Write each When to Use item as a specific trigger condition, not a general statement.

**Recommended** ✅

```plaintext
When to Use:
- The user has confirmed they want to submit
  a leave request and all required fields
  have been collected
- The user explicitly asks to book, request,
  or apply for time off and the leave type
  and dates have been confirmed
- A leave request flow is in progress and
  the user has provided explicit confirmation
  to proceed
```

**Not recommended** ❌

```plaintext

When to Use:
- Leave requests
- When the user wants time off
- HR-related actions
```

### When NOT to Use

When NOT to Use is the most underused part of the skill prompt and the most important for preventing incorrect invocations. It tells the LLM when not to call this skill.

This section is where you define the boundaries between this skill and other skills. When two skills serve related purposes, explicit When NOT to Use clauses that reference the other skill prevent the LLM from choosing incorrectly.

Write When NOT to Use clauses for:

- Common misrouting scenarios when users phrase a request in a way that sounds like it should trigger this skill but should actually invoke a different skill.
- Alternative skills that serve related purposes. Make the boundary between the skills explicit.
- Prerequisite conditions that haven't been met. Explicitly block premature invocation.
- Limitations of this skill with scenarios the skill can't handle correctly.

**Recommended** ✅

```plaintext
When NOT to Use:
- The user is asking a question about leave
  policy or eligibility - use the Knowledge
  Base instead
- The user has not yet confirmed the request
  details - collect confirmation first
- The leave type or dates are still ambiguous
  or have not been provided
- The user is asking to check the status of
  an existing leave request - use the Get
  Leave Status Skill instead
- The user is asking to cancel a leave request
  - use the Cancel Leave Request Skill instead
```

**Not recommended** ❌

```plaintext
When NOT to Use:
Don't call this skill if the information is in the knowledge base.
```

### Input requirements

Input requirements cover every input field the skill accepts. Input requirements are where most skill failures are corrected. A field that's being populated with the wrong value, in the wrong format, or from the wrong source almost always has an insufficient field hint as its root cause.

Pay particular attention to:

- **Identity fields**: Always specify identity fields, such as user email or user ID, in your skill prompt. This must come from the authenticated skill context, not from the conversation. This prevents a user from saying `do this for my colleague` and having the genie act on behalf of someone else.
  
- **Fields derived from prior skill outputs**: When a field should be populated from the output of a previous skill, such as a service desk ID from a **Get Service Desks Skill**, a leave type ID from a **Get Leave Balance Skill**, say so explicitly. `Use the leave_type_id field from the Get Leave Balance Skill output, not the leave type name the user provided`.
  
- **Enumerated fields**: List valid values explicitly. Don't rely on the LLM to know what values are valid from general knowledge.
  

Specify the following for each field:

- Where the value should come from
- Format requirements if the field has format constraints
- Valid values if the field is enumerated
- Whether the field is required or optional
- Special handling instructions

**Example**

```plaintext
Input requirements:
- leave_type (required): The type of leave
  being requested. Must match exactly one of
  the leave types returned by the Get Leave
  Balance Skill. Present the options to the
  user and use the exact value they select -
  do not paraphrase or abbreviate.

- start_date (required): The first day of
  the leave period. Format: YYYY-MM-DD.
  Convert natural language dates ("next
  Monday", "the 14th") to this format before
  passing to the Skill.

- end_date (required): The last day of the
  leave period. Format: YYYY-MM-DD. Must be
  on or after start_date.

- reason (optional): The reason for the leave
  request. Required only if the selected leave
  type requires a reason - check the leave type
  details from Get Leave Balance. If not
  required, leave this field empty.

- user_email (required): The email address of
  the requesting user. Use the authenticated
  user email from the Skill trigger context -
  do not use any email address mentioned in
  the conversation.
```

### Output requirements

Output requirements tells the genie what the skill returns and how to use it. It's often skipped in first builds, which produces inconsistent output handling. Output requirements are particularly important when:

- Skill output requires conditional handling based on a status field
- Skill output contains a URL that should be cited or linked
- Skill output must be formatted in a specific way for the user
- Skill output feeds into a subsequent skill call and the genie needs to know which field to pass

**Example**

```plaintext
Output Requirements:
- Returns the request reference number
  (request_id field) and submission status
  (status field)
- Present the reference number to the user
  as confirmation: "Your leave request has
  been submitted. Reference number: [id]"
- If status is "pending_approval", inform
  the user that the request requires manager
  approval before it is confirmed
- If status is "error", inform the user that
  the submission failed and suggest contacting
  HR directly
```

## Example skill prompt

The following is a complete skill prompt for a Submit Leave Request skill using all sections of the template:

```plaintext
Purpose: Submits a leave request to Workday
on behalf of the requesting user.

Description: Calls the Workday absence
management API to create a leave request
for the authenticated user. Requires leave
type, start date, and end date. Returns the
request reference number and submission
status. The user must confirm the request
details before this Skill is invoked.

When to Use:
- The user has confirmed they want to submit
  a leave request
- All required fields have been collected:
  leave type, start date, and end date
- The user has explicitly confirmed the
  request summary presented to them

When NOT to Use:
- The user is asking about leave policy or
  eligibility - search the Knowledge Base
  instead
- The user has not yet confirmed the request
  details - do not submit without confirmation
- The leave type or dates are ambiguous or
  have not been provided
- The user wants to check an existing request
  - use Get Leave Status instead
- The user wants to cancel a request - use
  Cancel Leave Request instead

Input Requirements:
- leave_type (required): Must match exactly
  one of the leave types from Get Leave
  Balance output. Use the exact value
  returned by that Skill.

- start_date (required): First day of leave.
  Format: YYYY-MM-DD. Convert natural language
  dates to this format.

- end_date (required): Last day of leave.
  Format: YYYY-MM-DD. Must be on or after
  start_date.

- reason (optional): Required only if the
  leave type requires a reason per Get Leave
  Balance output. Leave empty if not required.

- user_email (required): Use the authenticated
  user email from the Skill trigger context.
  Never use an email from the conversation.

Output Requirements:
- Return the request_id to the user as their
  reference number
- If status is "pending_approval": inform
  the user approval is required before
  confirmation
- If status is "error": inform the user the
  submission failed and suggest contacting
  HR directly
```

---
