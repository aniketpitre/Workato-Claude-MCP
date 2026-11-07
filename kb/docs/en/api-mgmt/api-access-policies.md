---
url: 'https://docs.workato.com/en/api-mgmt/api-access-policies.md'
description: >-
  Learn how API access policies use rate limit and request quota rules to
  control how clients call your Workato APIs.
---

# API access policies

Access policies control how clients use APIs. This helps prevent the overuse of an API by a single client, which could result in degraded performance for the community of API users. While an access policy is optional, if you do not create and associate an access policy with a client, then there are no API usage quotas on the client.

Each access policy has two types of quotas:

| Policy type | Description |
| --- | --- |
| Rate limit policy | Restricts the number of API calls that can be made within a short time period, such as a minute. |
| Request limit policy | Restricts the number of API calls that can be made within a longer time period, such as 30 days. |

Go to **Platform** > **API platform** > **Policies** to view existing and [create new access policies](#create-new-access-policy).

## Create new access policy

Complete the following steps to create a new access policy:

1. Go to **Platform** > **API platform** > **Policies**.
   
2. Click **\+ New policy**. The **Create New Policy** dialog displays.
   
   ![Create API Policy](/assets/api-policy-create.BKdO3u52.png)_Create new policy_
   
3. Enter a unique **Name** for the policy.
   
4. Select the **Time interval** for rate limits.
   
5. Specify the **Number of requests** allowed per client within the rate limit interval.
   
6. Select the **Time interval** for the usage quota.
   
7. Specify the **Number of requests** allowed per client within the usage quota.
   
8. Click **Create policy**. The new policy appears on the **Policies** page.
   

After creating the policy, assign it to a client. You can [create a new client](/en/api-mgmt/api-client-mgmt#create-new-client) or edit an existing client's access configuration to assign the policy.

## Manage policy usage

When an API access policy exceeds rate limits or usage quotas, the server returns a `429` error. To assist clients with troubleshooting, responses for requests associated with an API access policy include additional details:

| Header | Description |
| --- | --- |
| `retry-after` | Indicates the timestamp for the next valid request, based on rate limits or usage allowances. |

---
