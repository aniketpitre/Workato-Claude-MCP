---
url: 'https://docs.workato.com/en/connectors/eloqua.md'
description: >-
  The Eloqua connector lets you automate marketing workflows: create, update,
  delete, get, and search records, and trigger on new or updated records.
---

# Eloqua

Eloqua is a Marketing Automation Platform that helps teams build a unified brand experience across multiple marketing channels. At its core, Eloqua holds and aggregates your customer data which then allows you to utilize this data to build personal engagements across all customer touchpoints. Eloqua helps you do this through advanced segmentation and targeting, adaptive campaign orchestration and lead/asset management.

## API Version

The Eloqua connector uses the [Eloqua REST API v2](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/index.html).

## How to connect to Eloqua on Workato

The Eloqua connector uses OAuth 2.0 to connect to Eloqua. We recommend provisioning and assigning a dedicated integration user to Workato. This connection on Workato inherits the same permissions as the user that was used to authenticate.

![Configuring Eloqua connection](/assets/connection.jzhY1CEb.png)

| Field | Description |
| --- | --- |
| Connection name | Give this Eloqua connection a unique name that identifies which Eloqua instance it is connected to. |
| Custom OAuth profile | Optional. Select a custom OAuth profile for this connection. |

## Using depth to control how much information is returned from Eloqua

The Eloqua connector allows you to adjust how much information is returned from Eloqua for `Search` and `Get` record details. This control is done in recipe configuration via the `depth` input field. The depth input field supports the following values - `Minimal`, `Partial`, `Complete`. [More information here.](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/APIRequests_RequestDepth.html)

![Using Depth control](/assets/depth_control.C5xq0rw2.png)

---
