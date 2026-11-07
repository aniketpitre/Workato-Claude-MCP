---
url: 'https://docs.workato.com/en/connectors/replicon.md'
description: >-
  The Replicon connector lets you automate time tracking: trigger on new
  projects, users, and clients, ready-to-sync invoices, and updated timesheets.
---

# Replicon

[Replicon](https://www.replicon.com/) is a suite of software for time-tracking, advanced project management, task collaboration, resource allocation, and professional services automation.

## How to connect to Replicon on Workato

The Replicon connector supports both basic authentication and token-based authentication to authenticate with Replicon.

![Replicon connection setup](/assets/connection.6ad-kb6w.png)_Replicon connection setup_

These are the parameters of the Replicon connection:

<dl id="replicon-parameters"><dt>Connection name</dt><dd>Give this Replicon connection a unique name that identifies the Replicon instance of the connection.</dd><dt>Location</dt><dd>Specify where the Replicon connection resides in your Projects folder directory.</dd><dt>Company</dt><dd>The name of the company to which the Replicon instance is registered.</dd><dt>User-token authentication?</dt><dd>If <em>Yes</em>, authentication is based on the <strong>User token</strong>. If <em>No</em>, authentication is based on the <strong>Username</strong> and <strong>Password</strong>.</dd><dt>User token</dt><dd>If you selected <strong>user token</strong> authentication, provide the user token generated from the Authentication Service.</dd><dt>Login name</dt><dd>Login name to connect to Replicon.</dd><dt>Password</dt><dd>Password to connect to Replicon.</dd><dt>Subdomain</dt><dd>Name of the Replicon instance subdomain. Defaults to <strong>global</strong> if connecting to production instances.</dd></dl>

## How to generate user tokens on Replicon

### Using Replicon Security API reference page

1. Navigate to Replicon's Security API reference in [Replicon API Documentation](https://www.replicon.com/help/api-authentication/#authorizing-using-token-based-authentication). If prompted, log into your account.
2. On the Security API reference page, look for the `AuthenticationService1.svc/CreateAccessToken2` and click **Try it now**.
3. Replace the JSON payload with the following code, and edit the fields as needed. You can remove the `lifetime` field, which creates a permanent token.
   
   ```json
   {
     "identity": {
       "loginName": "user_name"
     },
     "lifetime": {
       "days": 0,
       "hours": 0,
       "minutes": 0,
       "seconds": 30,
       "milliseconds": 0
     },
     "description": "test",
     "unitOfWorkId": "12345"
   }
   ```
   
4. Click **Execute**.
5. Ensure that the Response Code is `200`, and that a token generates inside the JSON response body.
6. Copy the generated token and place it inside the Workato connection setup.

## Triggers and actions

To learn more about Replicon triggers, see the following articles:

- [New client trigger](/en/connectors/replicon/new-client-trigger)
- [New project trigger](/en/connectors/replicon/new-project-trigger)
- [New user trigger](/en/connectors/replicon/new-user-trigger)
- [New/updated ready to sync invoice trigger](/en/connectors/replicon/new-or-updated-invoice-ready-to-sync-trigger)
- [Updated timesheet trigger](/en/connectors/replicon/updated-timesheet-trigger)

---
