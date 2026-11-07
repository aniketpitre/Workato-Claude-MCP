---
url: 'https://docs.workato.com/en/connectors/linkedin/new-advertising-form.md'
description: >-
  The New lead gen form submitted trigger in the LinkedIn connector fires when
  someone completes a lead gen form in any of your LinkedIn campaigns.
---

# LinkedIn - New lead gen form submitted trigger

The **New lead gen form submitted** trigger allows you to create jobs immediately when someone completes a lead gen form in any of your LinkedIn Campaigns. This trigger sends the information to your CRM, providing your sales team with visibility into new leads.

> **LEAD GEN FORM MUST BE ACTIVE**
> 
> The lead gen form in your LinkedIn Campaigns must be active to successfully create a subscription and start the recipe. An inactive lead gen form returns a `404 Not Found Error`.

![LinkedIn Trigger](/assets/linkedin-new-form-trigger.DOSz13oo.png)_Filter leads by advertising account, campaign, and form_

## Input

At a minimum, you must select the advertising account containing the campaigns, which, in turn, contain the lead gen forms from which you plan to retrieve leads.

| Input field | Description |
| --- | --- |
| Advertising account | This is the advertising account containing the advertising form to trigger off. If only this field is configured, this recipe considers all advertising form submissions across all campaigns and advertising forms within this advertising account as trigger events. You can only have one recipe listening on the same advertising account. |
| Campaign | Use this to scope advertising form submissions to a specific campaign in your LinkedIn advertising account. If this field is configured, this recipe considers all advertising form submissions on this specific campaign as trigger events. You cannot have more than one advertising form trigger listening on the same campaign. |
| Form | Use this to filter by specific lead gen forms in your advertising account or campaign. |
| When first started, this recipe should pick up events from | This allows you to retrospectively pull leads from LinkedIn. This would be useful for initial loads when starting this recipe. You can pull leads created in the past 90 days. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger is a lightweight record that contains the identifiers of this lead gen form submission and its parent creative, campaign, account, and form.

![LinkedIn record](/assets/linkedin-new-form-trigger-output-field.IiryaAa4.png)

## How to use the trigger

1. Overcoming restrictions on the trigger

As LinkedIn imposes a one recipe rule for each advertising account or campaign, you will be unable to start multiple recipes that trigger off the same advertising account or campaign. To handle multiple automations based off the same advertising account or campaign, use [Recipe functions](/en/connectors/recipe-functions).

2. Getting details of the lead gen form response

To get the contents of the answers to a specific lead gen form response, use the `Get lead gen form response` action.

---

---
url: >-
  https://docs.workato.com/en/connectors/linkedin/get-advertising-form-response-by-id.md
description: >-
  The Get lead gen form response by ID action in the LinkedIn connector lets you
  retrieve a specific lead gen form submission, with its questions and answers.
---

# LinkedIn - Get lead gen form response by ID action

We recommend using this action with our `New lead gen form submitted` trigger. This allows you to retrieve the information about a specific lead gen form submission, including the questions, answers, and contexts about the parent campaign, advertising account, or creative.

![Get lead gen form response](/assets/get-advertising-response.BW83ij40.png)_Map "Form response ID" from the trigger_

## Input

| Input field | Description |
| --- | --- |
| Advertising account | The advertising account where the form is coming from. You can't map a datapill to this field. |
| Form | The form to which this advertising response belongs. This is required for Workato to identify the custom questions within this advertising form. |
| Lead gen form response ID | The lead gen form response ID. This is available in the output of the trigger. |

## Output

The output of this action contains all information relevant to a user who has filled up this form. This includes campaign, creative, and answer information.

## Handling multiple lead gen form types

When your advertising account or campaign has multiple lead gen forms used in the child creatives, you must use logical flows to route these responses to the correct `Get lead gen form response by ID` action. This can be done by discerning the ID of the form through the output of the trigger.

![Use variables by Workato to store the form ID](/assets/get-advertising-id.VdDj1-8O.png)_Use variables by Workato to store the form ID_

![Find the ID of the form from the end of the URL in the Campaign Manager](/assets/get-advertising-form-id-in-linkedin.DwsY5Gw-.png)_You can find the ID of the form from the end of the URL in the Campaign Manager_

![Use multiple if statements](/assets/use-if-statements.BCdV4ac-.png)_Use multiple if statements to route the responses to the correct **Get lead gen form response by ID** action which has the form selected_

---

---
url: >-
  https://docs.workato.com/en/connectors/linkedin/search-advertising-form-responses.md
description: >-
  The Search lead gen form responses action in the LinkedIn connector lets you
  search responses, filtered by campaign, form, and creative.
---

# LinkedIn - Search lead gen form responses action

Use this action to search for all lead gen form responses.

![Search lead gen form response](/assets/search-advertising-response.CIIXcOfU.png)_Search lead gen form responses by campaign, form, and creative_

## Input

| Input field | Description |
| --- | --- |
| Advertising account | The advertising account where the form is coming from. You can't map a datapill to this field. |
| Form | The form to which this lead gen response belongs. This is required for Workato to identify the custom questions within this lead gen form. |
| Pull reports within a specified time range | Specify the date range for the reports you plan to retrieve. The start date must be a maximum of 90 days in the past. |
| Offset | Used for pagination. |
| Limit | Limit the number of leads this action can pull. |
| Campaign | Limit responses to a specific campaign. |
| Creative | Limit responses to a specific creative. |

## Output

The output of this action contains all information relevant to leads based on your search filters.

---
