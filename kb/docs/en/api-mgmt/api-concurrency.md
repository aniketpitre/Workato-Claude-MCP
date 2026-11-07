---
url: 'https://docs.workato.com/en/api-mgmt/api-concurrency.md'
description: >-
  Configure API concurrency in Workato to set how your workspace queues or
  rejects requests when the simultaneous request quota is reached.
---

# API concurrency

API concurrency refers to the number of requests that can be processed simultaneously by your workspace at a given time. API concurrency enables you to manage high volumes of API requests by defining how your workspace handles requests when the concurrency quota is reached.

![API concurrency settings](/assets/api-concurrency-settings.D0B3j3C5.png)_API concurrency settings_

## Configure API concurrency

To manage your API concurrency settings:

1. Go to **Platform > API Platform > Settings** and click the **API concurrency** tab within your Workato account.
   
2. Review the **Concurrency limit**. This field displays the number of API requests your workspace can process simultaneously. Contact your Customer Success Manager to increase this quota.
   
3. Select your preferred method for managing requests when the concurrency quota is exceeded. Requests are queued by default.
   
   - **Queue requests**: Select this option to queue incoming requests that exceed the concurrency quota. Requests in the queue are throttled and processed when other concurrent requests complete.
     
   - **Reject requests**: Select this option to immediately reject any new requests that exceed the concurrency quota.
     
   
   Specify the **Queue size** if you chose to **Queue requests**. This determines how many requests are queued after the concurrency quota is exceeded. The queue size can be a value between 1 and 100.
   
4. Click **Save** to apply your settings.

---
