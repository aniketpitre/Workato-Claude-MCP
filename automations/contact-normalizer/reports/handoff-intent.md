# Handoff: Intent stage, contact-normalizer

- **Role:** Business Analyst (workato-analyst)
- **Date:** 2026-11-07
- **Spec:** `automations/contact-normalizer/spec.yaml` (status: draft, approvals null)
- **spec_check:** `python3 tools/spec_check.py automations/contact-normalizer/spec.yaml` gives `ok`, with 0 errors and 0 warnings.

## Summary

This is a reusable **recipe function** (trigger `workato_recipe_function` / "New call for function") that
cleans one contact record. Other recipes call it synchronously now. It may become a Genie skill or MCP tool later.

- **Inputs** (all optional strings): `first_name`, `last_name`, `email`, `phone`.
- **Outputs:** `first_name`, `last_name`, `full_name`, `email`, `phone`, `is_valid` (boolean), `issues` (text).
- **Rules:**
  - Trim every field.
  - Title-case the names.
  - Build `full_name` by joining the non-empty name parts with one space.
  - Trim and lower-case the email, then check its shape. It must have one `@`, a non-empty local part, a dotted domain and no whitespace.
  - Keep only the digits of the phone, plus a `+` when it is the first character.
  - `is_valid` is true only when `issues` is empty.
- **Never fails on bad input.** Unexpected errors are logged with Logger, with no raw PII in the message, and the function returns `is_valid=false` and `issues` containing "internal error".
- **Volumes and SLA:** up to 1,000 calls/day; synchronous, under 2 s. `retries: 0`.
- **Security:** PII (names, emails, phones), classified internal. The function does not persist inputs.

### Acceptance tests (synthetic data)

| ID | Given | Expect |
| --- | --- | --- |
| AT-1 | `"  aNNA  "`, `" SMITH  "`, `"  Anna.Smith@Example.COM "`, `"(415) 555-0100"` | `Anna` / `Smith` / `Anna Smith` / `anna.smith@example.com` / `4155550100`, is_valid true, issues `""` |
| AT-2 | email `ben.lee(at)example.com` (other fields valid) | is_valid false, issues contains `invalid email` (only), job succeeds |
| AT-3 | all inputs omitted, `""`, or whitespace-only | all strings `""`, is_valid false, issues contains `missing email`, no job fails |
| AT-4 | phone `" +1 (415) 555-0100 "` | phone `+14155550100`, is_valid true |
| AT-5 | first name empty, `"  o'neil-SMITH "`, `DEV.TEST@EXAMPLE.ORG`, `415.555.0102 ext 7` | clean full_name = last_name, email `dev.test@example.org`, phone `41555501027`. Casing and validity depend on Q1/Q3 |
| AT-6 | phone `555+0103` | phone `5550103` (a `+` that isn't first is dropped) |
| AT-7 | 20 sequential calls | each call under 2 s, AT-1 output |

## Open questions (for the requester)

1. **Q1:** Should a missing first or last name make `is_valid` false, or is email the only required field?
2. **Q2:** What format should `issues` use: separator (proposal `"; "`), fixed wording and order? Should it be a list instead of text?
3. **Q3:** How should names with apostrophes, hyphens or particles be title-cased (O'Neil, Smith-Jones, van der Berg, McDonald)?
4. **Q4:** Should a missing or digit-less phone add an issue or make the record invalid? Is there a minimum digit count? Should extensions be handled?
5. **Q5:** Should a missing field come back as `""` (proposed) or `null`?
6. **Q6:** Should an invalid email be returned normalised (proposed) or blanked?
7. **Q7:** What is the peak calls per hour (200 assumed)? Does the expected volume fit the Free plan's credit grant?
8. **Q8:** Is PII in job history acceptable, or is data masking or reduced job data retention needed? Both are plan-dependent.

Q1–Q6 change the expected values in the tests (AT-5 is partly blocked on Q1 and Q3), so the requester should answer them before confirming.

## Feasibility

| Check | Result |
| --- | --- |
| Connectors in `kb/connectors/catalog.json` | `workato_recipe_function` is present: trigger `execute` "New call for function", action `return_result`. `logger` is present: action `log_message`. Both have `requires_connection: false`. |
| Connections | **None needed.** The spec omits `connection`. `config/environments.yaml` dev has `connections: {}`, which is fine. |
| Target | dev workspace, project **Test** (project_id 50879, folder_id 74743), from `config/environments.yaml`. |
| Recipe function behaviour | A synchronous call is subject to the job timeout (90 min by default), so the 2 s SLA isn't at risk. Sources: `kb/docs/en/connectors/recipe-functions/actions/call-recipe-function-synchronously.md` and `kb/docs/en/recipes/jobs.md` (Timeouts). |
| Usage / Free plan | A synchronous call inherits the caller's usage metric. The call and the function's action steps each count as Tasks (`kb/docs/en/recipes/tasks.md`). Free is a one-time grant of 50,000 credits (`kb/docs/en/pricing/self-service/self-service.md`). At 1,000 calls/day the grant could become the limiting factor over time (Q7). The KB doesn't state an exact credit-per-task rate. |
| PII handling | Data masking is "included in specific pricing plans" (`kb/docs/en/features/data-masking.md`). It may not be available on Free (Q8). |
| Other Free-plan constraints | Single environment and no AIRO. Neither affects this automation. |

No Workato MCP tools were called. The workspace was not read or changed.

## Ready for spec confirmation: **no**

The spec passes spec_check. The requester should answer Q1–Q6, since they change the expected test values, and decide on Q8 (PII in job history). Q7 can be confirmed alongside them. Once those answers are in, the Analyst updates the spec and the requester can confirm it.
