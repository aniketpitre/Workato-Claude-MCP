---
url: 'https://docs.workato.com/en/connectors/apify/launch-actor-and-wait-action.md'
description: >-
  The Launch actor and wait action starts an Actor run in Apify, waits for it to
  finish, and returns the run with its default dataset items.
---

# Apify - Launch actor and wait action

The **Launch actor and wait** action starts an Actor run in Apify, waits for it to finish, and returns the run with its default dataset items.

If the run fails, is aborted, or times out on Apify, the action fails with an error.

## Input

Input fields are dynamically generated based on the Actor you select. The following input field is common to all Actors. Refer to the [Apify API documentation](https://docs.apify.com/api/v2) for more information on available input fields.

| Input field | Description |
| --- | --- |
| Actor | Select an Actor you plan to launch from the drop-down menu, or use a custom value. A custom value is an Actor ID, or the username and Actor name joined with a tilde. For example, `apify~hello-world`. |

## Output

Output fields are dynamically generated based on the Actor you select. Refer to the [Apify API documentation](https://docs.apify.com/api/v2) for more information on available output fields.

---
