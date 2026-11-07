---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-properties.md'
description: >-
  Reference for the environment properties used to configure the ELT Pipeline
  for Snowflake accelerator in Slack and Microsoft Teams.
---

# ELT Pipeline for Snowflake accelerator - Assets - Environment properties

The ELT Pipeline for Snowflake accelerator has nine environment properties that are common to both Slack and Microsoft Teams implementations:

- [elt.user\_section\_text](#section-text)
- [elt.user\_button1\_url](#button-url)
- [elt.user\_button1\_label](#button-label)
- [elt.snowflake\_url](#snowflake)
- [elt.s3bucketregion](#bucket-region)
- [elt.s3bucketname](#bucket-name)
- [elt.bot\_app\_id](#app-id)
- [elt.aws\_secret\_key](#secret-key)
- [elt.aws\_key\_id](#key-id)
- [elt.admin\_guide](#admin-guide)

In addition, this accelerator has two environment properties that are specific to either Slack or Microsoft Teams:

- [elt.slack\_notification\_channel](#slack-channel)
- [elt.msteams\_notification\_channel](#teams-channel)

## elt.user\_section\_text

This is the customizable **section text** for the button located in the left column of the ELT Bot's **Homepage**.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd><strong>Button section text</strong></dd></dl>

## elt.user\_button1\_url

The URL for the customizable user button on the ELT Bot's Homepage.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>https://example.com</code></dd></dl>

## elt.user\_button1\_label

This is the label text for the customizable button for the ELT Bot **Homepage**.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd><strong>Label text</strong></dd></dl>

## elt.snowflake\_url

This is the URL for your Snowflake instance.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>https://xyz.snowflake.com</code></dd></dl>

## elt.s3bucketregion

Sets the S3 region. Navigate to **Bucket > Properties >Static website hosting** to find your region in the endpoint URL.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd>us-west-2</dd></dl>

## elt.s3bucketname

Case-sensitive bucket name.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd>elt-pipeline-accelerator</dd></dl>

## elt.bot\_app\_id

The ID of the app. Locate the app ID in Slack under the app's basic information page.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd>XA02B82C</dd></dl>

## elt.aws\_secret\_key

Obtain this key from your S3 Admin. Use this key to create a staging area in Snowflake.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd>fbFv7K8qs9zpGCpS6O8s4LosFwErc76Z112unTxT</dd></dl>

## elt.aws\_key\_id

Obtain this key from your S3 Admin. Use this key to create a staging area in Snowflake.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd>AKIA3J9TYYRU7CVUXG5N</dd></dl>

## elt.admin\_guide

The URL to a Google docs version of the admin guide for this accelerator.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>https://docs.google.com</code></dd></dl>

## elt.slack\_notification\_channel

Channel where you plan to receive notifications from the ELT Pipeline Slack bot.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd>#elt-notifications</dd></dl>

## elt.msteams\_notification\_channel

Channel where you plan to receive notifications from the ELT Pipeline Microsoft Teams bot.

<dl class="horizontal-dl"><dt>Sample value:</dt><dd>#elt-notifications</dd></dl>

---
