---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-homepage.md'
description: >-
  Explore the App homepage for the ELT Pipeline for Snowflake accelerator, with
  quick links, pipeline options, and your list of ELT pipelines.
---

# ELT Pipeline for App homepage

The ELT Pipeline for Snowflake **App homepage** contains three main sections:

- [Quick links](#quick-links)
- [ELT pipeline options](#pipeline-options)
- [List of ELT pipelines](#pipeline-list)

## Quick links

The **Quick links** section lets you pin links to the top of the **App homepage**. For example, you can pin the link to the Admin guide (a pdf version of the ELT pipeline accelerator documentation) and other helpful links. You can customize these links using properties listed in our [ELT pipeline properties documentation](/en/accelerator-elt-pipeline-properties).

<dl><dt>Admin/installation guide</dt><dd>Change the URL in the <strong>elt.admin_guide</strong> property.</dd><dt>ELT | Access | Snowflake</dt><dd>Change the URL in the <strong>elt.snowflake_guide</strong> property.</dd><dt>ELT | User section text</dt><dd>Change the button's label text and URL by modifying the <strong>elt.user_button1_label</strong> and <strong>elt.user_section_text</strong> properties. To customize the section text, edit the <strong>elt.user_section_text</strong> property.</dd></dl>

## ELT pipeline options

The **ELT pipeline options** interface enables you to [create a pipeline](/en/accelerator-elt-pipeline-create), [search for a pipeline](/en/accelerator-elt-pipeline-search), [add a source object](/en/accelerator-elt-pipeline-add-source), and [add/update users](/en/accelerator-elt-pipeline-modify-user).

> **USER PERMISSIONS**
> 
> Only users with an **Admin** role have permission to add a source object or modify users.

## List of ELT pipelines

The **List of ELT pipelines** section contains the following lists of pipelines:

<dl><dt>Most recent active pipelines</dt><dd>Active pipelines that the ELT Pipeline bot recently processed.</dd><dt>Most recent pending pipelines.</dt><dd>Recent pipelines that are awaiting processing.</dd><dt>Most recent inactive pipelines.</dt><dd>Pipelines that have errored out or were manually deactivated.</dd></dl>

---
