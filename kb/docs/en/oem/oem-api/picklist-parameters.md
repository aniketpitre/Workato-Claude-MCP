---
url: 'https://docs.workato.com/en/oem/oem-api/picklist-parameters.md'
description: >-
  Reference for the picklist names and parameters required to retrieve picklist
  values by connector through the Workato platform API.
---

# Embedded API - Picklist parameters (Platform API)

This document contains all the connection parameters required for obtaining [a list of picklist values](/en/oem/oem-api/picklists#get-picklist-values) via Workato's platform APIs.

The privilege required to use this API endpoint is currently available to Embedded partners only.

## Guide

### Provider

Identifier for the connector. The provider value should be supplied while creating a connection using Embedded platform API.

### Picklist name

Internal name of the picklist.

### Parameters

If a picklist requires parameters, the name of the parameter is specified here. See the [sample request](/en/oem/oem-api/picklists#sample-request) for an example of how this is used.

## Picklist names/parameters by Adapter

| Adapter | Picklist name | Parameters |
| --- | --- | --- |
| active\_reg\_online | events\_for\_picklist |  |
| adobe\_experience\_manager | folder\_path | \_\_parent\_id |
| adobe\_experience\_manager | path |  |
| airtable | bases |  |
| airtable | tables | base\_id |
| airtable | views | base\_id,table\_id |
| amazon\_s3 | buckets |  |
| amazon\_s3\_secondary | buckets |  |
| anaplan | workspaces\_list |  |
| apttus | all\_sobjects |  |
| apttus\_intelligent\_cloud | object\_list |  |
| asana | workspaces |  |
| ascent\_erp | all\_sobjects |  |
| aws\_lambda | functions |  |
| aws\_sns | topic\_arn\_list |  |
| bamboohr | get\_fields\_pick\_list |  |
| bamboohr | table\_list |  |
| basecamp | my\_projects\_todolists |  |
| basecamp | my\_projects |  |
| basecamp | my\_people |  |
| basecamp | my\_calendars |  |
| bigtincan | form\_id |  |
| bigtincan | channel\_id |  |
| bim360 | hub\_list |  |
| bim360 | project\_list | hub\_id |
| bim360 | folders\_list | hub\_id, project\_id |
| bim360 | folder\_items | project\_id,folder\_id |
| bim360 | item\_versions | project\_id,item\_id |
| bim360 | file\_types |  |
| bim360 | version\_types |  |
| bim360 | resource\_types |  |
| bim360 | issue\_child\_objects |  |
| bim360 | issue\_container\_lists | hub\_id |
| bim360 | issue\_type | hub\_id,project\_id |
| bim360 | issue\_sub\_type | hub\_id,project\_id,ng\_issue\_type\_id |
| bim360 | project\_types |  |
| bim360 | assigned\_type\_list |  |
| bim360 | status\_list |  |
| bim360 | issue\_status\_list |  |
| bim360 | service\_types |  |
| box | my\_folders |  |
| box | enterprise\_users |  |
| box | my\_folders\_csv\_file |  |
| box | template\_list |  |
| box | my\_folders\_wo\_root |  |
| box | list\_user\_files |  |
| brick\_ftp | folder\_list |  |
| capsulecrm | list\_milestones |  |
| cisco\_spark | rooms |  |
| concur | my\_lists |  |
| concur | payment\_type\_picklist |  |
| concur | expense\_type\_picklist |  |
| concur | attendee\_type\_picklist |  |
| concur | expense\_group\_picklist |  |
| coupa | create\_object\_types |  |
| coupa | update\_object\_types |  |
| coupa | object\_types |  |
| coupa | suppliers |  |
| coupa | trigger\_object\_types |  |
| coupa | accelerate\_statuses |  |
| coupa | accounts |  |
| coupa | account\_types |  |
| coupa | addresses |  |
| coupa | all\_countries |  |
| coupa | attachment\_objects |  |
| coupa | approval\_limits |  |
| coupa | asn\_headers |  |
| coupa | audit\_statuses |  |
| coupa | content\_groups |  |
| coupa | contract\_types |  |
| coupa | contracts |  |
| coupa | comments |  |
| coupa | commodities |  |
| coupa | consents |  |
| coupa | countries |  |
| coupa | currencies |  |
| coupa | default\_locales |  |
| coupa | departments |  |
| coupa | document\_types |  |
| coupa | expense\_categories |  |
| coupa | frugalities |  |
| coupa | integration\_history\_actions |  |
| coupa | integration\_statuses |  |
| coupa | inventory\_types |  |
| coupa | invoice\_line\_types |  |
| coupa | invoice\_matching\_levels |  |
| coupa | items |  |
| coupa | lookup\_values |  |
| coupa | lookups |  |
| coupa | match\_types |  |
| coupa | order\_types |  |
| coupa | payment\_methods |  |
| coupa | payment\_terms |  |
| coupa | periods |  |
| coupa | po\_transmission\_methods |  |
| coupa | receipts |  |
| coupa | remit\_to\_address\_objects |  |
| coupa | requisitions |  |
| coupa | roles |  |
| coupa | security\_types |  |
| coupa | service\_types |  |
| coupa | shipping\_terms |  |
| coupa | system\_catalogs |  |
| coupa | tax\_codes |  |
| coupa | tax\_registrations |  |
| coupa | term\_types |  |
| coupa | transmission\_statuses |  |
| coupa | units |  |
| coupa | uoms |  |
| coupa | users |  |
| coupa | user\_groups |  |
| coupa | warehouses |  |
| coupa | yes\_or\_no\_options |  |
| deputy | employee\_role\_pick\_list |  |
| deputy | stress\_profile\_pick\_list |  |
| docparser | parsers |  |
| docusign | get\_values |  |
| docusign\_secondary | get\_values |  |
| dropbox | get\_folder\_tree |  |
| dropbox | get\_folder\_and\_csv\_tree |  |
| dropbox | get\_file\_tree |  |
| event\_brite | list\_organizations |  |
| event\_brite | get\_user\_events\_desc |  |
| event\_brite | get\_contact\_list\_pick\_list |  |
| evernote | get\_notebooks |  |
| evernote | get\_latest\_notes |  |
| expensify | currency\_list |  |
| fairsail | all\_sobjects |  |
| feedly | list\_categories |  |
| feedly | list\_tags |  |
| financialforce | all\_sobjects |  |
| forcecom | all\_sobjects |  |
| fresh\_books | category\_pick\_list |  |
| fresh\_books | status\_pick\_list |  |
| fresh\_desk | get\_all\_contacts\_list |  |
| fresh\_desk | get\_all\_agents\_list |  |
| ftps | directories |  |
| ftps\_secondary | directories |  |
| github | orgs |  |
| github | repository | owner |
| github | repos | org |
| github | issue |  |
| github | milestones |  |
| github | pullrequest |  |
| github | repo\_owner |  |
| github | repository\_name | repository\_owner |
| github | repos\_name | user |
| gmail | mailbox\_labels |  |
| google\_big\_query | projects\_picklist |  |
| google\_big\_query | datasets\_picklist |  |
| google\_big\_query | tables\_picklist |  |
| google\_big\_query | columns\_picklist |  |
| google\_calendar | my\_calendars |  |
| google\_calendar | tasklist\_picklist |  |
| google\_contacts | get\_contact\_groups\_pick\_list |  |
| google\_drive | folders |  |
| google\_drive | files |  |
| google\_sheets | sheets\_pick\_list\_v3 |  |
| google\_sheets | sheets\_pick\_list |  |
| google\_sheets | teamdrives\_list |  |
| google\_sheets | spreadsheets\_pick\_list | with\_sheets,offset |
| google\_sheets | teamdrives\_picklist |  |
| google\_translate | list\_languages |  |
| hipchat | room\_public |  |
| hipchat | room\_private |  |
| hubspot | get\_lists |  |
| hubspot | contact\_property\_list |  |
| hubspot | property\_list |  |
| hubspot | get\_list |  |
| hubspot | get\_workflows |  |
| hubspot | deal\_pipelines |  |
| hubspot | deal\_stages |  |
| hubspot | owners\_picklist |  |
| ibm\_workspace | space\_list |  |
| infusionsoft | get\_category\_picklist |  |
| infusionsoft | stage\_list |  |
| infusionsoft | user\_list |  |
| insightly | category\_list |  |
| insightly | currency\_list |  |
| instagram | my\_follows |  |
| intacct | bankaccount\_picklist |  |
| intacct | customers |  |
| intacct | departments |  |
| intacct | employees |  |
| intacct | expense\_types |  |
| intacct | glaccount\_picklist |  |
| intacct | intacct\_objects |  |
| intacct | items |  |
| intacct | locations |  |
| intacct | projects |  |
| intacct | vendors |  |
| intercom | admin\_pick\_list |  |
| jdbc | columns\_list | table |
| jdbc | sql\_columns\_list | sql,output\_schema |
| jdbc | unique\_columns\_list | table |
| jdbc | timestamp\_columns\_list | table |
| jdbc | tables\_list |  |
| jdbc\_secondary | columns\_list | table |
| jdbc\_secondary | sql\_columns\_list | sql,output\_schema |
| jdbc\_secondary | unique\_columns\_list | table |
| jdbc\_secondary | timestamp\_columns\_list | table |
| jdbc\_secondary | tables\_list |  |
| jira | assignee\_picklist | query, demo, project, KAN |
| jira | priority\_picklist |  |
| jira | status\_picklist |  |
| jira | get\_project\_issuetypes |  |
| jira | resolution\_picklist |  |
| jira\_secondary | assignee\_picklist | query, demo, project, KAN |
| jira\_secondary | priority\_picklist |  |
| jira\_secondary | status\_picklist |  |
| jira\_secondary | get\_project\_issuetypes |  |
| jira\_secondary | resolution\_picklist |  |
| jira\_service\_desk | service\_desk |  |
| jira\_service\_desk | request\_type | service\_desk\_id |
| jms | workato\_schema\_list |  |
| jobscience | all\_sobjects |  |
| jump\_cloud | create\_association\_types |  |
| jump\_cloud | create\_objects |  |
| jump\_cloud | delete\_association\_types |  |
| jump\_cloud | delete\_objects |  |
| jump\_cloud | get\_objects |  |
| jump\_cloud | list\_objects |  |
| jump\_cloud | list\_objects\_by\_id |  |
| jump\_cloud | search\_objects |  |
| jump\_cloud | search\_by |  |
| jump\_cloud | update\_objects |  |
| jump\_cloud | trigger\_objects |  |
| jump\_cloud | target\_list |  |
| kafka | topic\_list |  |
| kafka | workato\_schema\_list |  |
| kenandy | all\_sobjects |  |
| knack | objects |  |
| linked\_objects | linkable\_objects |  |
| linkedin | status\_list |  |
| lookup\_table | lookup\_table\_list |  |
| magento | type\_id |  |
| magento | attributes |  |
| mailchimp | mailing\_lists |  |
| mailchimp | mailing\_lists\_v3 |  |
| mailchimp | languages |  |
| marketo | my\_lists |  |
| marketo | fields\_list |  |
| marketo | lead\_activities\_types |  |
| marketo | lookup\_types |  |
| marketo | custom\_objects\_picklist |  |
| marketo | my\_lists\_with\_ids |  |
| marketo | partitions |  |
| marketo | lead\_fields |  |
| marketo | lead\_fields\_for\_upsert |  |
| marketo\_secondary | my\_lists |  |
| marketo\_secondary | fields\_list |  |
| marketo\_secondary | lead\_activities\_types |  |
| marketo\_secondary | lookup\_types |  |
| marketo\_secondary | custom\_objects\_picklist |  |
| marketo\_secondary | my\_lists\_with\_ids |  |
| marketo\_secondary | partitions |  |
| marketo\_secondary | lead\_fields |  |
| marketo\_secondary | lead\_fields\_for\_upsert |  |
| microsoft\_dynamics\_crm | crm\_object |  |
| microsoft\_dynamics\_crm | crm\_fields | object\_name |
| microsoft\_dynamics\_crm | crm\_audit\_object |  |
| microsoft\_dynamics\_crm | crm\_with\_date\_object |  |
| microsoft\_dynamics\_crm | crm\_with\_updated\_date\_object |  |
| microsoft\_sharepoint | list |  |
| microsoft\_sharepoint | folders |  |
| microsoft\_sharepoint | name\_list |  |
| miro\_board | boards |  |
| miro\_board | frames |  |
| miro\_board | board\_access\_by\_link |  |
| miro\_board | board\_access\_by\_team |  |
| mixpanel | funnel\_pick\_list |  |
| mssql | columns\_list | table |
| mssql | sql\_columns\_list | sql,output\_schema |
| mssql | unique\_columns\_list | table |
| mssql | timestamp\_columns\_list | table |
| mssql | tables\_list | quota |
| mssql | tables\_pick\_list |  |
| mssql | columns\_pick\_list | table |
| mssql | procedures\_pick\_list |  |
| mssql\_secondary | columns\_list | table |
| mssql\_secondary | sql\_columns\_list | sql,output\_schema |
| mssql\_secondary | unique\_columns\_list | table |
| mssql\_secondary | timestamp\_columns\_list | table |
| mssql\_secondary | tables\_list | quota |
| mssql\_secondary | tables\_pick\_list |  |
| mssql\_secondary | columns\_pick\_list | table |
| mssql\_secondary | procedures\_pick\_list |  |
| mysql | columns\_list | table |
| mysql | sql\_columns\_list | sql,output\_schema |
| mysql | unique\_columns\_list | table |
| mysql | timestamp\_columns\_list | table |
| mysql | tables\_list |  |
| mysql | tables\_pick\_list |  |
| mysql | procedures\_list |  |
| mysql | columns\_pick\_list | table |
| mysql\_secondary | columns\_list | table |
| mysql\_secondary | sql\_columns\_list | sql,output\_schema |
| mysql\_secondary | unique\_columns\_list | table |
| mysql\_secondary | timestamp\_columns\_list | table |
| mysql\_secondary | tables\_list |  |
| mysql\_secondary | tables\_pick\_list |  |
| mysql\_secondary | procedures\_list |  |
| mysql\_secondary | columns\_pick\_list | table |
| namely | job\_title |  |
| nationbuilder | my\_published\_events |  |
| netsuite | body\_custom\_fields | netsuite\_object |
| netsuite | custom\_object\_fields | netsuite\_object |
| netsuite | column\_custom\_fields | netsuite\_object |
| netsuite | netsuite\_add\_update\_objects |  |
| netsuite | get\_custom\_types\_script |  |
| netsuite | netsuite\_objects |  |
| netsuite | netsuite\_classification\_search\_types |  |
| netsuite | custom\_body\_pick\_list | netsuite\_object |
| netsuite | custom\_column\_pick\_list | netsuite\_object |
| netsuite | netsuite\_standard\_search\_types |  |
| netsuite | saved\_search\_list | netsuite\_search\_type |
| netsuite | join\_object\_list | netsuite\_search\_type |
| netsuite | object\_field\_list | netsuite\_search\_type,object\_list |
| netsuite | get\_custom\_types |  |
| netsuite | custom\_saved\_search\_list |  |
| netsuite | join\_custom\_object\_list |  |
| netsuite | object\_custom\_field\_list | object\_list |
| netsuite | netsuite\_attach\_contact\_types |  |
| netsuite | netsuite\_attach\_file\_types |  |
| netsuite | get\_search\_types |  |
| netsuite | get\_search\_objects | category |
| netsuite | netsuite\_search\_objects |  |
| netsuite | field\_list | netsuite\_object |
| netsuite | netsuite\_execute\_search\_types |  |
| netsuite | custom\_object\_pick\_list | netsuite\_object |
| netsuite | subsidary\_list |  |
| netsuite | entity\_list |  |
| netsuite | item\_location\_list |  |
| netsuite | case\_status\_list |  |
| netsuite | case\_priority\_list |  |
| netsuite | case\_issue\_list |  |
| netsuite | case\_assignee\_list |  |
| netsuite | standard\_field\_list | netsuite\_object |
| netsuite | custom\_field\_list |  |
| netsuite\_secondary | body\_custom\_fields | netsuite\_object |
| netsuite\_secondary | custom\_object\_fields | netsuite\_object |
| netsuite\_secondary | column\_custom\_fields | netsuite\_object |
| netsuite\_secondary | netsuite\_add\_update\_objects |  |
| netsuite\_secondary | get\_custom\_types\_script |  |
| netsuite\_secondary | netsuite\_objects |  |
| netsuite\_secondary | netsuite\_classification\_search\_types |  |
| netsuite\_secondary | custom\_body\_pick\_list | netsuite\_object |
| netsuite\_secondary | custom\_column\_pick\_list | netsuite\_object |
| netsuite\_secondary | netsuite\_standard\_search\_types |  |
| netsuite\_secondary | saved\_search\_list | netsuite\_search\_type |
| netsuite\_secondary | join\_object\_list | netsuite\_search\_type |
| netsuite\_secondary | object\_field\_list | netsuite\_search\_type,object\_list |
| netsuite\_secondary | get\_custom\_types |  |
| netsuite\_secondary | custom\_saved\_search\_list |  |
| netsuite\_secondary | join\_custom\_object\_list |  |
| netsuite\_secondary | object\_custom\_field\_list | object\_list |
| netsuite\_secondary | netsuite\_attach\_contact\_types |  |
| netsuite\_secondary | netsuite\_attach\_file\_types |  |
| netsuite\_secondary | get\_search\_types |  |
| netsuite\_secondary | get\_search\_objects | category |
| netsuite\_secondary | netsuite\_search\_objects |  |
| netsuite\_secondary | field\_list | netsuite\_object |
| netsuite\_secondary | netsuite\_execute\_search\_types |  |
| netsuite\_secondary | custom\_object\_pick\_list | netsuite\_object |
| netsuite\_secondary | subsidary\_list |  |
| netsuite\_secondary | entity\_list |  |
| netsuite\_secondary | item\_location\_list |  |
| netsuite\_secondary | case\_status\_list |  |
| netsuite\_secondary | case\_priority\_list |  |
| netsuite\_secondary | case\_issue\_list |  |
| netsuite\_secondary | case\_assignee\_list |  |
| netsuite\_secondary | standard\_field\_list | netsuite\_object |
| netsuite\_secondary | custom\_field\_list |  |
| okta | events |  |
| okta | event\_select | eventcategory |
| okta | result\_types |  |
| onedrive | my\_drive\_folders |  |
| onedrive | select\_csv\_file |  |
| onprem\_command\_line\_scripts | script\_list\_pick\_list |  |
| onprem\_files | my\_folders |  |
| onprem\_files | my\_files |  |
| onprem\_files | columns\_pick\_list | file,column\_separator |
| onprem\_files\_secondary | my\_folders |  |
| onprem\_files\_secondary | my\_files |  |
| onprem\_files\_secondary | columns\_pick\_list | file,column\_separator |
| oracle | columns\_list | table |
| oracle | sql\_columns\_list | sql,output\_schema |
| oracle | unique\_columns\_list | table |
| oracle | timestamp\_columns\_list | table |
| oracle | tables\_list | quota |
| oracle | packages\_list |  |
| oracle\_ebs | get\_operations | service\_name |
| oracle\_secondary | columns\_list | table |
| oracle\_secondary | sql\_columns\_list | sql,output\_schema |
| oracle\_secondary | unique\_columns\_list | table |
| oracle\_secondary | timestamp\_columns\_list | table |
| oracle\_secondary | tables\_list | quota |
| oracle\_secondary | packages\_list |  |
| out\_systems | module\_list |  |
| out\_systems | module\_entities | module\_name |
| out\_systems | module\_list\_create |  |
| out\_systems | module\_entities\_create | module\_name |
| out\_systems | module\_list\_update |  |
| out\_systems | module\_entities\_update | module\_name |
| outlook | my\_calendars |  |
| outlook | timezones |  |
| outlook | my\_folder\_objs |  |
| outlook | my\_calendar\_objs |  |
| percolate | object\_types |  |
| percolate | tenant\_licenses |  |
| percolate | platforms | scope\_ids |
| percolate | schemas | scope\_ids,platform\_id |
| percolate | upsert\_object\_types |  |
| percolate | channels | scope\_ids,platform\_id |
| percolate | folders | scope\_id |
| percolate | trigger\_object\_types |  |
| percolate | quorums |  |
| percolate | on\_approved\_list |  |
| percolate | participant\_outcomes |  |
| percolate | approval\_statuses |  |
| percolate | subject\_types |  |
| percolate | access\_scopes |  |
| percolate | approval\_workflow\_list |  |
| percolate | asset\_types |  |
| percolate | transcoding\_statuses |  |
| percolate | orientation\_list |  |
| percolate | user\_tenants |  |
| percolate | event\_change\_types |  |
| percolate | get\_object\_types |  |
| percolate | campaign\_workflow\_list | scope\_id |
| percolate | post\_workflow\_list | scope\_id |
| percolate | terms\_list |  |
| percolate | post\_statuses |  |
| pipedrive | stage\_list |  |
| pipedrive | user\_list |  |
| plan\_grid | create\_object\_list |  |
| plan\_grid | update\_object\_list |  |
| plan\_grid | get\_objects |  |
| plan\_grid | search\_objects |  |
| plan\_grid | upload\_object\_list |  |
| plan\_grid | object\_list |  |
| plan\_grid | object\_list\_new |  |
| plan\_grid | project\_list |  |
| plan\_grid | project\_types |  |
| plan\_grid | project\_folders | project\_uid |
| podio | organization\_list |  |
| podio | workspace\_list | organization\_id |
| podio | space\_app\_list | workspace\_id |
| postgresql | columns\_list | table |
| postgresql | sql\_columns\_list | sql,output\_schema |
| postgresql | unique\_columns\_list | table |
| postgresql | timestamp\_columns\_list | table |
| postgresql | tables\_list |  |
| postgresql | tables\_pick\_list |  |
| postgresql\_secondary | columns\_list | table |
| postgresql\_secondary | sql\_columns\_list | sql,output\_schema |
| postgresql\_secondary | unique\_columns\_list | table |
| postgresql\_secondary | timestamp\_columns\_list | table |
| postgresql\_secondary | tables\_list |  |
| postgresql\_secondary | tables\_pick\_list |  |
| prontoforms | get\_form\_list |  |
| propel | all\_sobjects |  |
| quickbase | table\_field\_list | table\_id |
| quickbase | sort\_field\_list | table\_id |
| quickbase | table\_field\_list\_app\_token | table\_id,apptoken |
| quickbase | sort\_field\_list\_app\_token | table\_id,apptoken |
| quickbase | table\_input\_field\_list | table\_id |
| quickbase | table\_input\_field\_list\_app\_token | table\_id,apptoken |
| quickbase | table\_input\_field\_list\_app\_token\_upsert |  |
| quickbase | list\_applications |  |
| quickbase | list\_tables | app\_name |
| quickbase | list\_reports\_in\_table | table\_id |
| quickbase | list\_tables\_upsert | app\_name |
| quickbase\_secondary | table\_field\_list | table\_id |
| quickbase\_secondary | sort\_field\_list | table\_id |
| quickbase\_secondary | table\_field\_list\_app\_token | table\_id,apptoken |
| quickbase\_secondary | sort\_field\_list\_app\_token | table\_id,apptoken |
| quickbase\_secondary | table\_input\_field\_list | table\_id |
| quickbase\_secondary | table\_input\_field\_list\_app\_token | table\_id,apptoken |
| quickbase\_secondary | table\_input\_field\_list\_app\_token\_upsert |  |
| quickbase\_secondary | list\_applications |  |
| quickbase\_secondary | list\_tables | app\_name |
| quickbase\_secondary | list\_reports\_in\_table | table\_id |
| quickbase\_secondary | list\_tables\_upsert | app\_name |
| quickbooks | get\_customers |  |
| quickbooks | currency\_list |  |
| quickbooks | get\_customer\_tax\_code |  |
| quickbooks | get\_terms |  |
| quickbooks | get\_payment\_methods |  |
| quickbooks | get\_accounts |  |
| quickbooks | get\_classes |  |
| quickbooks | get\_vendors |  |
| quickbooks | get\_tax\_codes |  |
| quickbooks | get\_purchase\_accounts |  |
| quickbooks | get\_entities |  |
| quickbooks | get\_items |  |
| quickbooks | get\_payable\_accounts |  |
| quickbooks | get\_tax\_rates |  |
| quickbooks | get\_departments |  |
| quickbooks | get\_accounts\_receivable |  |
| quickbooks | get\_purchase\_items |  |
| quickbooks | get\_customer\_types |  |
| raisers\_edge | constituent\_type |  |
| raisers\_edge | online\_presence\_types |  |
| raisers\_edge | constituent\_code\_types |  |
| raisers\_edge | custom\_field\_category\_list |  |
| redshift | columns\_list | table |
| redshift | sql\_columns\_list | sql |
| redshift | unique\_columns\_list | table |
| redshift | timestamp\_columns\_list | table |
| redshift | tables\_list |  |
| redshift | tables\_pick\_list |  |
| redshift | databases\_pick\_list | host,port,username,password |
| redshift | columns\_pick\_list | table |
| relateiq | contacts\_list |  |
| replicon | get\_employee\_types\_for\_picklist |  |
| replicon | get\_policy\_set\_for\_picklist |  |
| replicon | get\_permission\_set\_for\_picklist |  |
| replicon | get\_timesheet\_approval\_path\_picklist |  |
| replicon | get\_department\_picklist |  |
| replicon | invoice\_sync\_status |  |
| replicon | get\_all\_project\_status\_label |  |
| replicon | get\_currency\_list |  |
| replicon | billing\_rate\_list |  |
| replicon | break\_type\_list |  |
| replicon | activity\_list |  |
| sagelive | all\_sobjects |  |
| salesforce | sobject\_input\_field\_list | sobject\_name |
| salesforce | sobject\_table\_list | sobject\_name |
| salesforce | sobject\_parent\_table\_list | sobject\_name |
| salesforce | sobject\_field\_list |  |
| salesforce | all\_sobjects |  |
| salesforce | sobject\_with\_mdate |  |
| salesforce | all\_events |  |
| salesforce | sobject\_with\_cdate |  |
| salesforce | createable\_sobjects |  |
| salesforce | updateable\_sobjects |  |
| salesforce | upsertable\_sobjects |  |
| salesforce | external\_fields\_list | sobject\_name |
| salesforce | get\_all\_process\_definition |  |
| salesforce | opportunity\_Type |  |
| salesforce | opportunity\_StageName |  |
| salesforce | opportunity\_LeadSource |  |
| salesforce | account\_Type |  |
| salesforce | account\_Industry |  |
| salesforce | account\_Ownership |  |
| salesforce | account\_Rating |  |
| salesforce | lead\_Salutation |  |
| salesforce | lead\_Status |  |
| salesforce | lead\_LeadSource |  |
| salesforce | lead\_Industry |  |
| salesforce | lead\_Rating |  |
| salesforce | contact\_Salutation |  |
| salesforce | case\_Status |  |
| salesforce | case\_Origin |  |
| salesforce | case\_Type |  |
| salesforce | case\_Reason |  |
| salesforce | case\_Priority |  |
| salesforce | campaign\_Type |  |
| salesforce | campaign\_Status |  |
| salesforce | campaignMember\_Status |  |
| salesforce | get\_reports |  |
| salesforce | all\_deletable\_sobjects |  |
| salesforce | sobject\_fields | sobject\_name |
| salesforce | upsert\_sobject\_fields | sobject\_name |
| salesforce | sobject\_field\_values\_list | sobject\_name |
| salesforce | get\_duplicate\_record\_sets |  |
| salesforce\_chatter | topics\_list |  |
| salesforce\_marketing\_cloud | data\_extensions |  |
| salesforce\_marketing\_cloud | fields\_list | key |
| salesforce\_marketing\_cloud | list\_templates |  |
| salesforce\_secondary | sobject\_input\_field\_list | sobject\_name |
| salesforce\_secondary | sobject\_table\_list | sobject\_name |
| salesforce\_secondary | sobject\_parent\_table\_list | sobject\_name |
| salesforce\_secondary | sobject\_field\_list |  |
| salesforce\_secondary | all\_sobjects |  |
| salesforce\_secondary | sobject\_with\_mdate |  |
| salesforce\_secondary | all\_events |  |
| salesforce\_secondary | sobject\_with\_cdate |  |
| salesforce\_secondary | createable\_sobjects |  |
| salesforce\_secondary | updateable\_sobjects |  |
| salesforce\_secondary | upsertable\_sobjects |  |
| salesforce\_secondary | external\_fields\_list | sobject\_name |
| salesforce\_secondary | get\_all\_process\_definition |  |
| salesforce\_secondary | opportunity\_Type |  |
| salesforce\_secondary | opportunity\_StageName |  |
| salesforce\_secondary | opportunity\_LeadSource |  |
| salesforce\_secondary | account\_Type |  |
| salesforce\_secondary | account\_Industry |  |
| salesforce\_secondary | account\_Ownership |  |
| salesforce\_secondary | account\_Rating |  |
| salesforce\_secondary | lead\_Salutation |  |
| salesforce\_secondary | lead\_Status |  |
| salesforce\_secondary | lead\_LeadSource |  |
| salesforce\_secondary | lead\_Industry |  |
| salesforce\_secondary | lead\_Rating |  |
| salesforce\_secondary | contact\_Salutation |  |
| salesforce\_secondary | case\_Status |  |
| salesforce\_secondary | case\_Origin |  |
| salesforce\_secondary | case\_Type |  |
| salesforce\_secondary | case\_Reason |  |
| salesforce\_secondary | case\_Priority |  |
| salesforce\_secondary | campaign\_Type |  |
| salesforce\_secondary | campaign\_Status |  |
| salesforce\_secondary | campaignMember\_Status |  |
| salesforce\_secondary | get\_reports |  |
| salesforce\_secondary | all\_deletable\_sobjects |  |
| salesforce\_secondary | sobject\_fields | sobject\_name |
| salesforce\_secondary | upsert\_sobject\_fields | sobject\_name |
| salesforce\_secondary | sobject\_field\_values\_list | sobject\_name |
| salesforce\_secondary | get\_duplicate\_record\_sets |  |
| sap | idoc\_list\_outbound |  |
| sap | idoc\_list\_inbound |  |
| sap | rfm\_list |  |
| sap | bapi\_list |  |
| sap\_erp | type\_pick\_list\_for\_trigger |  |
| sap\_erp | type\_pick\_list | service\_name |
| sap\_erp | all\_fields\_picklist | service\_name,type |
| sap\_erp | type\_pick\_list\_to\_create | service\_name |
| sap\_erp | type\_pick\_list\_to\_update | service\_name |
| service\_max | all\_sobjects |  |
| service\_now | tables\_pick\_list |  |
| service\_now | templates\_pick\_list | table |
| service\_now\_secondary | tables\_pick\_list |  |
| service\_now\_secondary | templates\_pick\_list | table |
| sftp | directories |  |
| sftp\_secondary | directories |  |
| slack | get\_user\_picklist |  |
| slack | get\_channel\_picklist |  |
| slack | get\_group\_picklist |  |
| slack | button\_recipe\_list |  |
| slack\_bot | nlu\_shared\_account\_list |  |
| slack\_bot | application\_picklist |  |
| slack\_bot | events\_pick\_list |  |
| slack\_bot | get\_params\_fields | parameters |
| slack\_bot | document\_type\_list | domain |
| slack\_bot | domains\_pick\_list |  |
| slack\_bot | get\_conversations\_picklist |  |
| slack\_bot | bot\_command\_pick\_list |  |
| slack\_secondary | get\_user\_picklist |  |
| slack\_secondary | get\_channel\_picklist |  |
| slack\_secondary | get\_group\_picklist |  |
| slack\_secondary | button\_recipe\_list |  |
| smartsheet | sheets |  |
| smartsheet | columns\_list | sheet\_id |
| smartsheet | reports |  |
| snowflake | columns\_list | table |
| snowflake | sql\_columns\_list | sql,output\_schema |
| snowflake | unique\_columns\_list | table |
| snowflake | timestamp\_columns\_list | table |
| snowflake | tables\_list |  |
| snowflake | stage\_list |  |
| snowflake | file\_format\_list |  |
| snowflake\_secondary | columns\_list | table |
| snowflake\_secondary | sql\_columns\_list | sql,output\_schema |
| snowflake\_secondary | unique\_columns\_list | table |
| snowflake\_secondary | timestamp\_columns\_list | table |
| snowflake\_secondary | tables\_list |  |
| snowflake\_secondary | stage\_list |  |
| snowflake\_secondary | file\_format\_list |  |
| soap | template\_list |  |
| splunk | saved\_searches\_query |  |
| splunk | saved\_searches |  |
| steelbrick | all\_sobjects |  |
| surveymonkey | survey\_pick\_list |  |
| taskray | all\_sobjects |  |
| teams\_bot | get\_folder\_tree |  |
| teams\_bot | choice\_set\_picklist |  |
| teams\_bot | bot\_command\_picklist |  |
| trackvia | apps |  |
| trackvia | views | app\_name |
| trackvia | document\_fields | view\_id |
| trackvia | mime\_types |  |
| trello | get\_board\_picklist |  |
| tsheets | user\_picklist |  |
| tsheets | jobcode\_picklist |  |
| twilio | sms\_numbers |  |
| twilio | voice\_numbers |  |
| twitter\_ads | field\_list |  |
| utility | linkable\_objects |  |
| veeva | all\_sobjects |  |
| vend | get\_payment\_type |  |
| vend | get\_products\_picklist |  |
| vlocity | all\_sobjects |  |
| webmerge | documents |  |
| webmerge | routes |  |
| workato\_app | connection\_list |  |
| workato\_app | invitation\_list |  |
| workato\_app | recipe\_list |  |
| workato\_mapper | workato\_schema\_list |  |
| workato\_pub\_sub | topic\_list |  |
| workato\_service | service\_recipe\_list |  |
| workato\_template | template\_list |  |
| workato\_variable | $$\_line\_list |  |
| workday | web\_services\_pl |  |
| workday | trigger\_objects |  |
| workday | objects |  |
| workday | custom\_objects |  |
| workday\_rest | job\_change\_reason |  |
| workday\_rest | supervisory\_organization |  |
| workflow | list\_workflow\_user\_pick\_list |  |
| workfront | objects |  |
| workfront | forms | object\_type |
| workplace\_bot | get\_users |  |
| workplace\_bot | bot\_command\_picklist |  |
| wrike | custom\_fields |  |
| wrike | folders |  |
| wrike | timelog\_categories |  |
| wrike | custom\_statuses |  |
| wrike | task\_status |  |
| wrike | accounts |  |
| wrike | field\_list |  |
| wrike\_secondary | custom\_fields |  |
| wrike\_secondary | folders |  |
| wrike\_secondary | timelog\_categories |  |
| wrike\_secondary | custom\_statuses |  |
| wrike\_secondary | task\_status |  |
| wrike\_secondary | accounts |  |
| wrike\_secondary | field\_list |  |
| wufoo | get\_forms\_list |  |
| xactly | tables |  |
| xero | currencies |  |
| xero | branding\_theme\_for\_picklist |  |
| xero | get\_items\_for\_picklist |  |
| xero | get\_accounts\_for\_picklist |  |
| xero | get\_tax\_types\_for\_picklist |  |
| xero | get\_accounts\_for\_prepayment\_picklist |  |
| zendesk | ticket\_form\_list |  |
| zendesk | ticket\_type |  |
| zendesk | ticket\_priority |  |
| zendesk | ticket\_status |  |
| zendesk | locales\_list |  |
| zendesk | custom\_objects\_picklist |  |
| zendesk | relationship\_picklist |  |
| zendesk\_secondary | ticket\_form\_list |  |
| zendesk\_secondary | ticket\_type |  |
| zendesk\_secondary | ticket\_priority |  |
| zendesk\_secondary | ticket\_status |  |
| zendesk\_secondary | locales\_list |  |
| zendesk\_secondary | custom\_objects\_picklist |  |
| zendesk\_secondary | relationship\_picklist |  |
| zenefits | companies |  |
| zenefits | employee\_events |  |
| zenefits | employment\_events |  |
| zoho\_invoice | currency\_rate\_picklist |  |
| zohocrm | account\_picklist |  |
| zohocrm | vendor\_picklist |  |
| zohocrm | campaign\_picklist |  |
| zuora\_forcecom | all\_sobjects |  |

---
