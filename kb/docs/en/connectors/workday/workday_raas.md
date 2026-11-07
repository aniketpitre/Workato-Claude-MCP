---
url: 'https://docs.workato.com/en/connectors/workday/workday_raas.md'
description: >-
  Learn how Workday Reports-as-a-Service (RaaS) exposes custom reports as web
  services and how to find a report URL for use in Workato.
---

# Workday RaaS

Workday Reports-as-a-Service (RaaS) is a feature that exposes reports as web services. These reports must be configured as **Advanced** type reports to be web service enabled.

## Custom Reports Setup

Custom Reports (advanced type) can be exposed as a Web Service to be used programmatically. Workato uses this web service to automate report run and to integrate report data from Workday to other applications.

### How to find report URL

Find URL in Actions > Web Service > View URLs

![View RaaS URL](/assets/view_raas_url.CUMbVsVV.png)_View Report URLs_

Right-click `JSON` and choose "Copy URL"

![RaaS JSON URL](/assets/copy_raas_json_url.C4rkfuLh.png)_Copy RaaS JSON URL_

JSON endpoint example

```
https://wd2-impl-services1.workday.com/ccx/service/customreport2/workato/workato/Investors?format=json&Worker_Type!WID=d588c41a446c11de98360015c5e6daf6&Base_Pay=0
```

## Filter parameters

Prompts behave like request parameters. In the UI, it is presented as input fields before generating the actual report.

![RaaS prompts](/assets/raas_prompts.DzG0skyx.png)_Raas prompts on Workday UI_

As a REST endpoint, these prompts are passed as request parameters. To do so, you have to set the report type and configure prompts. You can also define filters for your prompts.

#### Report type

Switch to advanced type if not already. Only Advanced custom reports can be used in RaaS.

![RaaS change to advance](/assets/raas_change_to_advance.DqGlTIDw.png)_Use advanced report_

#### Add prompts

Add all default prompts that are required of web-service-enabled reports. Add additional prompts as desired.

![Add RaaS prompts](/assets/raas_add_prompts.aI_CKqgF.png)_Add RaaS prompts_

In this example, Base Pay is assigned to Prompt Qualifier as Prompt #1, which will be used in filters.

#### Add filters

Apply logic to filter prompt values.

Use values from Prompt to compare against report column values. Example, assign Prompt parameter Base Pay as Prompt #1.

![Add RaaS filters](/assets/raas_add_filter.B_rx4Ucf.png)_Add RaaS filters_

When generating a report, Base Pay parameter will be checked. If a value is provided, only records with Base Pay greater than the provided value will be included in the report.

## Limitations

Based on the [Workday documentation](https://doc.workday.com/r/3DMnG~27o049IYFWETFtTQ/sGhnezv85Vfp9LabNN~EWw), there is a quota of 2GB for advanced custom report enabled for web services and exposed for integrations.

---
