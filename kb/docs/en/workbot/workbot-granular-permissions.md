---
url: 'https://docs.workato.com/en/workbot/workbot-granular-permissions.md'
description: >-
  Learn how to migrate Enterprise Workbots from the deprecated Slack bot scope
  to granular permission scopes and what changes.
---

# Moving to granular permission scopes

On 22 January 2020, Slack released [granular permissions](https://api.slack.com/docs/token-types#granular_bot), deprecating the old `bot` scope.

Previously, bot users were special and required the umbrella `bot` scope. Now, new Slack apps can request individual scopes for their bot users.

If you had Enterprise Workbots before 22 January 2020, there's a high chance it has the `bot` scope and **will require migration to the new scopes** by **late 2021**. You can check whether your Enterprise Workbot has the `bot` scope by heading over to your app management page (note that you either have to be the app creator or collaborator to have access to this page), and looking under **OAuth & Permissions**.

## Migration timeline

- **February 21, 2020** Slack will require any **NEW** apps to use granular permissions. There's no real action on your part - just be aware that if you create any new Enterprise Workbots, it's normal for them to have different scopes than your old bots.
  
- **Late 2021** Existing apps that have not upgraded will be assessed by Slack and conversations involving those apps will be delisted by them. We strongly recommend that you migrate your Enterprise Workbot way before this time.
  

## What happens if I do not update my Enterprise Workbot scopes?

By late 2021, conversations involving your Enterprise Workbot may be delisted by Slack upon their assessment. It's highly recommended to do it way before that - especially since migration is easy.

## Will any of my bot functionality be affected before/after migration?

For the most part, **no**. [SCIM APIs](https://api.slack.com/scim), [Web APIs](https://api.slack.com/web), the [Events API](https://api.slack.com/events-api) and all related methods are compatible with both old and new bot tokens.

However, the [RTM API](https://api.slack.com/rtm) is not accessible to the new bot tokens (and hence aren't usable after migration). If your app requires RTM functionality, Slack has advised **not** to perform this migration for your app.

## Migrating to the new scopes

On your app management page on Slack, head over to **Update to Granular Scopes**. ![Update to granular scopes](/assets/navigate-to-granular-scopes.erFZw9oH.png)_Navigate to granular permission scopes_

In Step 1, select the following bot token scopes:

- `app_mentions:read`
- `channels:read`
- `chat:write`
- `commands`
- `files:read`
- `files:write`
- `groups:read`
- `im:history`
- `im:write`
- `users:read`
- `users:read.email`

Click **Continue**.

In Step 2, select the following user token scopes:

- `users:read`

![User token scopes](/assets/user-token-scopes.DCTsDRUW.png)_User token scopes_

Click **Continue**.

In Step 3, verify your scope selections, then select **Yes, migrate my app**. When further prompted by Slack to ensure that your app does not require RTM APIs, select **Yes I'm sure** (Workbot does not use RTM APIs).

![Verify scope selections](/assets/verify-scope-selections.RVonQOot.png)_Verify scope selections_

In Step 4, you do not have to change your OAuth code as it is handled by Workato. Select **I've updated my app**.

![Confirm update scopes](/assets/confirm-update-scopes.DciM4Jdz.png)_Select **I've updated my app**_

Finally, reinstall your app for the new permission scopes to take effect. ![Reinstall app](/assets/reinstall-app.BUzmE-9w.png)_Reinstall your app_

For more information on migrating your app, you can head over to [Slack's migration guide](https://api.slack.com/authentication/migration#update_ui).

---
