---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-use-cases.md'
description: >-
  Example use cases for Workato Event streams, including decoupling recipes and
  creating batches from real-time events with topics.
---

# Event streams example use cases

This guide provides example use cases for Event streams. Example use cases provide an overview and resolution for specific scenarios.

## Decoupling recipes

Consider the following example. Our organization has a recipe that creates leads in Salesforce after receiving a WebToLead HTTP request, which was built to retrieve contact data from leads who filled in a form online. After creating the lead, the recipe updates an analytics database in Postgres.

![Original recipe](/assets/example-old-recipe.DddBmbcL.png)_Recipe moving leads from an online form to Salesforce and PostgreSQL_

If our organization was to change databases from PostgreSQL to RedShift, and start using MailChimp as a mailing list application, we can take one of the following approaches:

- [Modify the original recipe without using Event streams](#modify-recipe)
- [Use Event streams](#with-event-streams)

### Modify the original recipe without using Event streams

We would need to update our recipe as follows.

![Modified recipe](/assets/example-modified-recipe.4kfpiMjJ.png)_Modified recipe to add rows to Redshift instead of PostgreSQL and add subscribers to MailChimp_

The change to the original recipe would require additional iterations of the recipe development lifecycle, as the recipe would need to be modified, tested for backward compatibility, and pushed to production. Any bugs slipping through QA would result in downtime for the production recipe.

### Use Event streams

If we utilize Event streams, we build the original recipe in this way, to create a Salesforce lead before publishing the lead data to a topic. This recipe does not need to care about its consumers, and therefore to know that downstream recipes are changing.

![Publisher recipe](/assets/example-publish-recipe.Bj2p2aYv.png)_Publisher recipe that creates a lead in Salesforce and publishes lead data to a topic_

The corresponding consumer recipe that creates a Redshift row with the lead data will look as follows.

![Consumer recipe creating Redshift row](/assets/example-consume-recipe-redshift.BtmV8HFO.png)_Consumer recipe that consumes the lead data from the topic and creates a Redshift row with the lead data_

The corresponding consumer recipe that creates a MailChimp lead with the lead data will look as follows.

![Consumer recipe creating MailChimp lead](/assets/example-consume-recipe-mailchimp.OA1QcAcS.png)_Consumer recipe that consumes the lead data from the topic and creates a MailChimp lead with the lead data_

## Creating batches from real-time events

For example, in the same scenario the leads are generated at a very high rate, and we plan to optimize the number of API calls to Salesforce and PostgreSQL. WebToLead publishes leads one by one, so we cannot achieve that in a single recipe.

Using the Event topic you can aggregate new leads and publish them in batches once in a time interval. The original recipe only publishes new leads to the Event topic one at a time.

![Publisher recipe](/assets/example-new-leads-publish.4nao0Om2.png)_Publisher recipe that receives a new lead from WebToLead and publishes to Event streams_

The corresponding consuming recipe uses the [New batch of messages trigger](/en/connectors/pubsub/pubsub-batch-trigger) and runs once per hour. It then publishes the whole batch to Salesforce and PostgreSQL in just one API call each.

![Consuming recipe](/assets/example-new-leads-sf.BCci-Wx_.png)_Consuming recipe that receives a batch of new leads and publishes to Salesforce and PostgreSQL_

---
