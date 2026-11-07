---
url: 'https://docs.workato.com/en/api-mgmt/limits.md'
description: >-
  Reference for Workato API platform quotas, including the default thresholds
  and notes that apply to API platform usage.
---

# API platform quotas

The API platform has the following quotas:

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

| Description | Quota | Notes |
| --- | --- | --- |
| Job timeout | 30 seconds (default), 240 seconds (maximum) | You can configure the job timeout to a maximum of 240 seconds. However, testing an API endpoint directly in Workato using an endpoint's **Test request** tab is limited to a fixed 30-second job timeout, regardless of your configured value. |
| Request header size (single header) | 16 KB | NA |
| Request headers and url size combined (all headers) | 64 KB | NA |
| Maximum JWKS size | 64 KB | NA |
| Maximum payload size | 5 MB | NA |
| Maximum attachment size | 5 GB | Attachments accept multipart/form-data. |
| Maximum tracer payload | 1 MB | The tracer payload is the complete record of an API request captured for debugging and monitoring. It includes details of the request, and metadata. The tracer payload may be truncated if the total request size exceeds 1 MB. |
| Maximum cache key size | 10 kB | NA |
| Maximum cache entry value size | 10 kB | Requests exceeding this quota do not cache even when successful. Contact your Workato Customer Success Manager to adjust this quota. |
| Maximum number of API keys per API client | 20 | NA |
| Maximum cache entry count per user ID | 10,000 entries | If exceeded, entries are flushed, from oldest to newest, to accommodate new entries. To adjust this quota, contact your Workato Customer Success Manager for support. |

> **FURTHER READING**
> 
> Refer to the [Platform quotas](/en/limits) documentation for more information about Workato quotas.

---
