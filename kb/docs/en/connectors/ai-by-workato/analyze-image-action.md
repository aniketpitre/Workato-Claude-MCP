---
url: 'https://docs.workato.com/en/connectors/ai-by-workato/analyze-image-action.md'
description: >-
  The Analyze image action in the AI by Workato connector answers questions
  about an image or PDF based on the instructions you provide.
---

# AI by Workato - Analyze image action

The **Analyze image** action analyzes an image or PDF to answer a question you provide. For example, you can pull the vendor name and total from a scanned invoice. The output datapill value is `null` if the action doesn't find an answer in the file.

> **FEATURE AVAILABILITY**
> 
> AI by Workato is available for customers on specific pricing plans in the US, EU, AU, JP, SG, IL, KR, and UK data centers.
> 
> AI by Workato processes data using Anthropic's models in most regions. Workato enforces data residency in the US and EMEA by ensuring data is processed within the same region (US or EMEA) as the source data center. The SG, JP, and AU data centers process AI by Workato data within the APAC region. The Israel data center processes data in the US using OpenAI's models.
> 
> AI by Workato isn't available to workspaces in the CN data center. This reflects local regulatory requirements and Workato's commitment to data sovereignty and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.
> 
> You can opt in to this feature by agreeing to our [AI feature addendum](https://www.workato.com/legal/ai-feature-addendum). Contact your Customer Success representative to learn more.

## Input

| Input field | Description |
| --- | --- |
| File contents | Map the file datapill that contains the image or PDF you plan to analyze. Files can be up to 20 MB, and PDFs can have up to 15 pages. Alternatively, you can switch this field to [formula mode](/en/formulas/formula-mode) and enter a base64-encoded string using `.decode_base64`. For example, `"BASE64_TEXT".decode_base64`. Entering base64 text without decoding it may return a `Server has returned an internal error` message. |
| File name | Enter the file name with its extension, such as `invoice.png`, so Workato can infer the file type. Specify the type in **File type** if you leave this field blank. |
| File type | Select the file type of the contents: `png`, `jpg`, `jpeg`, `webp`, `gif`, or `pdf`. This overrides the type inferred from **File name**. |
| Instruction | Provide instructions on how to analyze the file, such as an analysis technique or a question to answer. |

## Output

| Output | Description |
| --- | --- |
| Analysis result | The result of the action. The output is determined by the instructions you provide. The datapill value is `null` if the action doesn't find an answer in the file. |
| Remaining calls (deprecated) | The number of remaining calls Workato can execute out of the overall daily quota. This field has been deprecated. |
| Consumed calls (deprecated) | The number of actions completed out of the overall daily quota. This field has been deprecated. |
| Reset time (deprecated) | The time the daily quota resets. This field has been deprecated. |

> **RATE LIMIT DEPRECATION**
> 
> Workato has removed daily usage quotas from AI by Workato actions. Refer to the AI by Workato [Quotas](/en/connectors/ai-by-workato#limits) section to see the quotas that still apply.

---
