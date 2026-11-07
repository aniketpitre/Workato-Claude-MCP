---
url: 'https://docs.workato.com/en/connectors/recipeops.md'
description: >-
  Use RecipeOps by Workato to monitor and manage active recipes, automating
  responses to stopped recipes and failed jobs.
---

# RecipeOps by Workato

The RecipeOps connector enables you to build recipes to monitor and manage active recipes.

Stopped recipes and failed jobs can have automated responses and notifications to mitigate their impact on critical business processes. You can also retrieve account, recipe, and job details using the RecipeOps connector.

> **FEATURE AVAILABILITY**
> 
> RecipeOps by Workato is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

* * *

## Usage inspiration

Need some inspiration? The RecipeOps connector can help you achieve the following:

- Notify designated workspace members when a key recipe is stopped. Workato sends notifications through Gmail, SMS, Twilio phone call or IVR, Slack, and more.
- Schedule on-call workspace members and build escalation policies.
- Flag low transaction counts and notify workspace members.
- Build job history report logs or audit reports in Google Sheets.
- Build recipe reports for an overview of automations and connected apps.

* * *

## Connection setup

You can use RecipeOps to monitor your workspace or someone else's.

Complete the following steps to set up your RecipeOps connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `RecipeOps` on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![RecipeOps connection setup](/assets/connect.CK_MBk8V.png)_RecipeOps connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Whose account are you managing?** drop-down menu to select the workspace you plan to monitor. Available options include:
   
   - **My account**: Monitor your own workspace.
   - **Someone else's account**: Monitor someone else's workspace. An admin from this workspace must create an [API client](/en/workato-api/api-clients) and share its API token with you to establish the connection.
   
   > **CONNECTION PRIVILEGES**
   > 
   > RecipeOps connections configured to monitor **My account** have admin privileges and access to all RecipeOps actions and triggers in your workspace, regardless of the role of the user creating the connection.
   
6. If you selected **Someone else's account**, enter the **API key** for the workspace you plan to monitor.
   
7. Click **Connect**.
   

> **EMBEDDED PARTNER WORKSPACE TRIGGERS**
> 
> The [Usage threshold reached](/en/connectors/recipeops/triggers/customer-usage-threshold-reached) trigger only works in Embedded partner workspaces. Although the trigger appears in other workspace types, jobs fail with an error if you add it to a recipe. Enter an API token from the Embedded partner workspace when you set up the RecipeOps connection. API tokens from Embedded customer workspaces result in an insufficient permissions error.

## Triggers

The RecipeOps connector supports the following recipe triggers:

- [Account connected](/en/connectors/recipeops/triggers/account-connected)
- [Account credentials refresh failed](/en/connectors/recipeops/triggers/account-credentials-refresh-failed)
- [Account disconnected](/en/connectors/recipeops/triggers/account-disconnected)
- [API concurrency threshold exceeded](/en/connectors/recipeops/triggers/concurrency-exceeded)
- [API policy quota violation](/en/connectors/recipeops/triggers/api-policy-violation)
- [API policy rate limit violation](/en/connectors/recipeops/triggers/rate-limit-violation)
- [Deployment approved](/en/connectors/recipeops/triggers/deployment-approved)
- [Deployment complete](/en/connectors/recipeops/triggers/deployment-complete)
- [Deployment failed](/en/connectors/recipeops/triggers/deployment-failed)
- [Deployment rejected](/en/connectors/recipeops/triggers/deployment-rejected)
- [Deployment re-opened for review](/en/connectors/recipeops/triggers/deployment-re-opened-for-review)
- [Job failed](/en/connectors/recipeops/triggers/new-failed-job)
- [Member invitation accepted](/en/connectors/recipeops/triggers/member-invitation-accepted)
- [New deployment submitted for review](/en/connectors/recipeops/triggers/new-deployment-submitted-for-review)
- [On-prem agent disconnected](/en/connectors/recipeops/triggers/opa-disconnected)
- [Package deployed](/en/connectors/recipeops/triggers/package-deployed)
- [Recipe started](/en/connectors/recipeops/triggers/recipe-started)
- [Recipe stopped by user](/en/connectors/recipeops/triggers/recipe-stopped-by-user)
- [Recipe stopped by Workato](/en/connectors/recipeops/triggers/recipe-stopped-by-workato)
- [Usage threshold reached](/en/connectors/recipeops/triggers/customer-usage-threshold-reached) (_Embedded partner workspaces only_)

* * *

## Actions

The RecipeOps connector supports the following recipe actions:

- [Get account details](/en/connectors/recipeops/actions/get-account-details)
- [Get recipe details](/en/connectors/recipeops/actions/get-recipe-details)
- [List connections](/en/connectors/recipeops/actions/list-connections)
- [List recipes](/en/connectors/recipeops/actions/list-recipes)
- [Rerun jobs](/en/connectors/recipeops/actions/rerun-jobs)
- [Search job history](/en/connectors/recipeops/actions/search-job-history)
- [Search recipes](/en/connectors/recipeops/actions/search-recipes)
- [Start recipe](/en/connectors/recipeops/actions/start-recipe)
- [Stop recipe](/en/connectors/recipeops/actions/stop-recipe)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/concurrency-exceeded.md
description: >-
  The API concurrency threshold exceeded trigger in the RecipeOps connector
  fires when workspace API requests exceed 80% of the concurrency quota.
---

# RecipeOps - API concurrency threshold exceeded

Monitors API requests across your workspace and triggers when requests exceed 80% of your concurrency quota. Additional trigger events are created for each 5% increment, up to the workspace quota. This trigger is limited to one event per threshold every five minutes to reduce noise. Subsequent requests for the same threshold within a five-minute window will not result in a job.

* * *

## Output

| Field | Description |
| --- | --- |
| **Concurrency limit** | API concurrency quota for this workspace. |
| **Concurrency** | Number of concurrency requests reached. |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/api-policy-violation.md
description: >-
  The API policy quota violation trigger in the RecipeOps connector fires when
  an access profile exceeds a policy quota threshold of 80, 90, or 100 percent.
---

# RecipeOps - API policy quota violation trigger

This trigger monitors API usage for the workspace. A trigger event occurs each time an access profile exceeds a policy quota threshold. For policies with longer quota intervals, duplicate events occur if the same threshold is exceeded every 30 days.

Learn more about our [API access policies](/en/api-mgmt/api-access-policies#create-new-access-policy).

## Trigger behavior

For each workspace, this trigger captures instances when a unique access profile exceeds the following policy request thresholds:

- 80% of quota
- 90% of quota
- 100% of quota

> **RECIPEOPS BEHAVIOR**
> 
> The 30-day reference only affects policies with a quota interval longer than 30 days. For example, with a policy of 1,000 requests and a 90-day interval, the system triggers an event if you reach 800 requests (80% threshold) in the first month. If there are no new requests in the following month and the usage still stands at 800 requests (80%), a second event triggers. For longer quota intervals, every 30 days, a trigger event is created when hitting the same threshold.

## Input

This trigger doesn't require any input.

## Output

| Field name | Description |
| --- | --- |
| Event message | `Your API policy has reached X% of its usage quota.` |
| API policy ID | The unique identifier of the API policy. |
| API policy name | The name of the API policy. |
| Usage limit | The total number of API calls that can be made within a specific longer time period, typically 30 days. |
| Limit time interval | The duration of the time period for the usage quota, such as 30 days. |
| Client ID | The unique identifier of the client. |
| Client name | The name of the client associated with the event. |
| Access profile ID | The unique identifier of the access profile. |
| Access profile name | The name of the access profile. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/rate-limit-violation.md
description: >-
  The API policy rate limit violation trigger in the RecipeOps connector fires
  when an access profile exceeds its assigned API rate limits.
---

# RecipeOps - API policy rate limit violation trigger

Actively monitors API usage across all access profiles and generates events when an access profile exceeds its assigned rate limits. It creates trigger events every five minutes for each unique access profile that goes beyond these quotas. To reduce noise, it generates only one event per access profile within this interval, even if rate limits are exceeded multiple times. For example, even if an access profile exceeds its rate limit three times within the same five-minute interval, this trigger only registers one trigger event.

Learn more about our [API access policies](/en/api-mgmt/api-access-policies#create-new-access-policy).

## Input

This trigger doesn't require any input.

## Output

| Field name | Description |
| --- | --- |
| Event message | `The rate limits for your API policy have been exceeded` |
| API policy ID | The unique identifier of the API policy. |
| API policy name | The name of the API policy. |
| Rate limit | The maximum number of API calls allowed within a specified short time interval. |
| Rate limit time interval | The time frame for the rate limit, such as a minute, hour, or day. |
| Client ID | The unique identifier of the client. |
| Client name | The name of the client associated with the event. |
| Access profile ID | The unique identifier of the access profile. |
| Access profile name | The name of the access profile. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/api-request-timeout.md
description: >-
  The API request timeout trigger in the RecipeOps connector fires when an API
  request to any workspace endpoint exceeds its configured timeout limit.
---

# RecipeOps - API request timeout trigger

The **API request timeout** trigger monitors the API request runtime for all endpoints in the workspace. The trigger activates when an API request exceeds the timeout limit of N seconds.

## Input

This trigger doesn't require user input.

## Output

| Output field | Description |
| --- | --- |
| API collection ID | Unique identifier of the API collection containing the timed-out endpoint. |
| API endpoint ID | Unique identifier of the specific endpoint that timed out. |
| API endpoint name | The name of the endpoint that exceeded the timeout limit. |
| Endpoint timeout limit (seconds) | The configured timeout threshold that was exceeded. |

---
