---
url: 'https://docs.workato.com/en/connectors/jira/triggers.md'
description: >-
  Explore the Jira triggers in Workato, including real-time and polling triggers
  for new or updated issues, comments, worklogs, and events.
---

# Jira - Triggers

The following Jira triggers can be used to kickstart workflows in your recipes.

To simplify API responses, the Jira REST API uses resource expansion, which means that the API will only return parts of a resource when explicitly requested. Workato automatically fetches and expands all parameters. Learn more about [Jira's resource expansion](https://developer.atlassian.com/cloud/jira/platform/rest/#expansion).

## How Jira real-time triggers work in Workato

When you use Jira real-time triggers in your recipes, Workato automatically registers a webhook in your Jira instance **when the recipe is started**. When the recipe is stopped, **the webhook is removed**.

![Jira webhook registration](/assets/jira-webhook-registration.C_f8eynu.png)_Jira webhooks registered by starting recipes_

Registering and removing webhooks requires Jira administrator global permissions. If your Jira connection doesn't have these permissions, use a [webhook trigger with the Webhooks connector](/en/connectors/workato-webhooks) instead.

Regardless of the state of the webhook, Workato continues to run a backup poll running every 6 hours, to pick up any events (related to the recipe trigger). Workato automatically removes any duplicates from the full list of events returned by Jira.

> **REAL-TIME TRIGGER SUPPORT FOR OAUTH 2.0**
> 
> OAuth 2.0 doesn't support real-time triggers because it is incompatible with webhooks. Refer to the [Jira connection](/en/connectors/jira) guide to configure a different authentication method if you plan to use real-time triggers.
> 
> Alternatively, you can register the [Webhooks connector](/en/connectors/workato-webhooks) in Jira to use Jira's static webhook functionality. Refer to the [Cloud Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-webhooks/) or [Jira Datacenter](https://confluence.atlassian.com/adminjiraserver/managing-webhooks-938846912.html) webhook documentation for registration steps.

## Deleted object (real-time)

The [Deleted object (real-time)](/en/connectors/jira/deleted-object-trigger) trigger monitors Jira for deleted objects in real-time.

## Export new issues in Jira

The [Export new issues in Jira](/en/connectors/jira/export-new-issues-trigger) trigger retrieves new issues from Jira on a schedule you specify.

## Export new/updated issues in Jira

The [Export new/updated issues in Jira](/en/connectors/jira/export-new-updated-issues-trigger) trigger retrieves new or updated issues from Jira on a schedule you specify.

## New event (real-time)

The [New event (real-time)](/en/connectors/jira/new-event-trigger) trigger monitors Jira for new events in real-time.

## New issue

The [New issue](/en/connectors/jira/new-issue-trigger) trigger checks Jira for new issues at an interval you specify.

## New issue (batch)

The [New issue (batch)](/en/connectors/jira/new-issue-batch-trigger) trigger retrieves new issues from Jira in batches at an interval you specify.

## New/updated comment (real-time)

The [New/updated comment](/en/connectors/jira/new-updated-comment-trigger) trigger monitors Jira for new or updated comments in real-time.

## New/updated issue (real-time)

The [New/updated issue](/en/connectors/jira/new-updated-issue-trigger) trigger monitors Jira for new or updated issues in real-time.

## New/updated worklog (real-time)

The [New/updated worklog](/en/connectors/jira/new-updated-worklog-trigger) trigger monitors Jira for new or updated worklogs in real-time.

## Updated issue

The [Updated issue](/en/connectors/jira/updated-issue-trigger) trigger checks Jira for updated issues at an interval you specify.

## Updated issue (batch)

The [Updated issue (batch)](/en/connectors/jira/updated-issue-batch-trigger) trigger retrieves updated issues from Jira in batches at an interval you specify.

---
