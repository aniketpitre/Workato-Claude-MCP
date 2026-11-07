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
