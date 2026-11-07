---
url: >-
  https://docs.workato.com/en/connectors/quickbooks/quickbooks-troubleshooting-connection.md
description: >-
  Use this guide to troubleshoot errors that occur while creating a QuickBooks
  Online connection in Workato.
---

# Troubleshoot QuickBooks Online connection errors

Use this guide to troubleshoot errors that occur while creating a QuickBooks Online connection in Workato.

## `app_already_purchased` error while creating a connection

![QBO purchased](/assets/QBO_purchased.GW_BjjXm.png)

You may receive the `app_already_purchased` error when creating a QuickBooks Online connection if someone else is already connected to Workato using the company account you provided. QuickBooks only allows one active connection to Workato per company account. Contact the user listed in the error message to delete their Workato connection or use a different company account to resolve this error.

## `Object Not Found` error while accessing QuickBooks API

![QBO errorobjnotfound](/assets/QBO_errorobjnotfound.CZ8rmYNi.png)

You may receive the `Object Not Found` error when you try to get a QuickBooks object based on an ID that doesn't exist.

![QBO errorobjnotfound3](/assets/QBO_errorobjnotfound3.eKNUNNKq.png)

For example, in the preceding image, the recipe tries to get an item from QuickBooks based on its ID. Unfortunately, the object does not exist in the QuickBooks account.

You can find the object's ID in its QuickBooks Online URL. For example, in the following image, `ID=6` shows that 6 is the object's ID.

![QBO errorobjnotfound2](/assets/QBO_errorobjnotfound2.DG3-M8tc.png)

To resolve the issue using a fixed value, find the correct ID using the QuickBooks Online URL, then rerun the job. To resolve the issue using a datapill, ensure your recipe provides the action with the correct IDs, then rerun the job.

## `784:unexpected token` QuickBooks API server not responding

![QBO APIerror](/assets/QBO_APIerror.3DX9zF3v.png)

You may receive the `784:unexpected token` error when the QuickBooks API experiences an outage or other intermittent issues. To resolve the issue, monitor [Intuit's Status page](http://status.developer.intuit.com) and re-run the job when the API is operational.

## `403 forbidden` error

You may receive the `403 forbidden` error when there are connectivity issues with the QuickBooks Online app. To resolve the issue, go to your recipe's **Connections** tab, then **Disconnect** and reconnect to the app.

![QBO connect3](/assets/QBO_connect3.BM-_JzRu.png)
