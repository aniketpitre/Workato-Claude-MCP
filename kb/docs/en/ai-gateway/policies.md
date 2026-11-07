---
url: 'https://docs.workato.com/en/ai-gateway/policies.md'
description: >-
  Create Model Gateway policies that apply rate limits, token limits, and IP
  access restrictions to routes and access keys.
---

# Policies

A policy is a reusable set of rate limits, token limits, and IP access restrictions in [Model Gateway](/en/ai-gateway). Policies are optional. Assign a policy to an [access key](/en/ai-gateway/access-keys) or a [route](/en/ai-gateway/route-builder#assign-a-policy-to-a-route) to apply its limits.

## Create a policy

Complete the following steps to create a policy:

1. Go to **Model Gateway > Policies**.
   
2. Click **\+ Create policy**.
   
   ![Add policy](/assets/add-new-policy.BS5e-SQo.png)_Create policy_
   
3. Enter a name in the **Name** field.
   
   ![Create new policy](/assets/create-policy.Bi1OvH1V.png)_Create new policy_
   
4. Optional. Expand **Rate limit** to specify the request limit per key, then configure the following fields:
   
   1. Use the **Time interval** drop-down menu to select the interval the limit applies to.
      
   2. Enter the number of requests allowed per key in the selected time interval in the **Number of requests** field.
      
5. Optional. Expand **Token limit** to define each key's token limit, then configure the following fields:
   
   1. Use the **Time interval** drop-down menu to select the interval the limit applies to.
      
   2. Enter the number of tokens allowed per key in the selected time interval in the **Number of tokens** field.
      
6. Optional. Expand **IP access control** to restrict access by IP address, then configure the following fields:
   
   1. Optional. Enter one or more IP addresses in the **Allowed IPs** field to allow requests only from those addresses. Separate multiple IP addresses with commas, or define a netmask, for example `106.226.96.0/20`.
      
   2. Optional. Enter one or more IP addresses in the **Blocked IPs** field to block requests from those addresses. Separate multiple IP addresses with commas, or define a netmask, for example `106.226.96.0/20`.
      
7. Click **Create**.

---
