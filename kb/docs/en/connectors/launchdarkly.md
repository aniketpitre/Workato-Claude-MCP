---
url: 'https://docs.workato.com/en/connectors/launchdarkly.md'
description: >-
  The LaunchDarkly connector automates feature management: create, update,
  search, and switch feature flags, and trigger recipes on flag changes.
---

# LaunchDarkly

LaunchDarkly is a feature management framework that provides a unified platform to monitor feature flags and to use them in development, testing, and experimentation. The primary object within LaunchDarkly is the feature flag, which links to all other objects and processes.

With the LaunchDarkly connector on Workato, you can automate your entire feature management flow seamlessly. You can easily monitor changes to a feature flag, perform experiment analytics, and even use feature flags to control the flow of recipes. With LaunchDarkly, you can seamlessly adds users to beta testing for customer support teams, and internal users for early access as a part of pre-existing onboarding flows.

> **INFO**
> 
> This connector is released to the [community](https://app.workato.com/custom_adapters/186249/details?community=true). You have to [install it to your workspace](/en/developing-connectors/community/community#how-do-i-find-and-install-community-connectors) before using it.

## How to connect to LaunchDarkly on Workato

The LaunchDarkly connector uses Personal Access Token to connect to LaunchDarkly. To fully utilize all triggers and actions of the connector, you must have the admin role. If this isn't feasible, we recommend that you create a token with the minimum set of scopes necessary to accomplish your use case within Workato. You can generate this access token in the LaunchDarkly UI. For more information, check the [LaunchDarkly documentation](https://docs.launchdarkly.com/home/members/role-create).

![LaunchDarkly Access Token](/assets/launchdarkly_access_token.C4b7PGua.gif)_LaunchDarkly Access Token - Account Setting > Authorization_

## Triggers

### Updated feature flag targeting status

This is a real-time trigger that sends an event when someone updates the targeting status of a feature flag in LaunchDarkly. You can monitor feature flags across an entire project, allow for more granular control by selecting an environment, or even just a single feature flag. You can also specify a webhook name that displays in the UI.

### New event trigger

This is a generic trigger that enables users to select an object to monitor. The user can make a selection from events that relate to several objects, such as Feature Flag, Project, Segment, Code Reference Repository, and Environment. For each of these objects, the user can choose to either monitor all events, or receive event notifications only for create/update/delete.

If you plan to monitor other objects, or specify a custom policy that models your business processes, select the custom option. Here, the resource specifies the object you plan to monitor, and the action specifies the set of changes to monitor. Review an example set of policies in the [LaunchDarkly documentation](https://docs.launchdarkly.com/home/members/example-policies/).

## Actions

### Create record

The creation record action supports the **Feature flag** and **Project** objects. Provide the necessary fields to create the object in LaunchDarkly.

For feature flags, you can clone an existing feature flag and inherit all the relevant settings.

### Delete record

The delete record action supports **Feature Flag**, **Project** and **User** objects. Provide the relevant identifying key to delete the object.

### Get record details by ID

The get record action supports **Feature Flag**, **Feature Flag Status**, **Flag Setting for User**, **Project**, and **User**.

> **INFO**
> 
> The get feature flag status doesn't evaluate the feature flag value for a user; instead, it checks at this [endpoint](https://apidocs.launchdarkly.com/tag/Feature-flags/#operation/getFeatureFlagStatus), and returns a status. The status is one of the following:
> 
> - `new`: The feature flag was created within the last seven days, and has not been requested yet
> - `active`: The feature flag was requested by your servers or clients within the last seven days
> - `inactive`: The feature flag was created more than seven days ago, and hasn't been requested by your servers or clients within the past seven days
> - `launched`: One variation of the feature flag has been rolled out to all your users for at least 7 days

The get flag setting for user does not perform an evaluation either; it returns the variation of the flag the user set to receive, based on the information in LaunchDarkly. This is the relevant [endpoint](https://apidocs.launchdarkly.com/tag/User-settings#operation/getUserFlagSettings).

### List records

The list records action supports **Feature Flag Status**, **Flag Setting for User**, and **Expiring User Targets on Feature Flag**.

The list expiring user targets on feature flag returns an array of users who can be used with the Update action to add, update, or remove the expiry date.

### Search records

The search records action supports **Feature Flag**, **Project** and **User**.

> **INFO**
> 
> When searching for feature flags and using the tags attribute, LaunchDarkly provides only one tag. When obtaining project values, no additional fields return, by default. If you need these fields in the recipe, you must specify them in the properties input.

### Switch feature flag status

The switch feature flag status is a simplified version of the update feature flag action, so the user can easily switch the flag on or off.

> **INFO**
> 
> Switching an already on flag on, or an already off flag to off does not produce errors.

### Update record

The update record action supports **Feature Flag**, **Feature Flag Setting for User**, **Expiring User Targets on Feature Flag**, and **Feature Flag Targets**.

> **INFO**
> 
> We do not support adding/removing targeting rules or percentage rollout configurations in the update feature flag action.

### Custom action

This connector supports creating your own custom actions. You can easily create new actions that support your organization's business processes and use cases.

---
