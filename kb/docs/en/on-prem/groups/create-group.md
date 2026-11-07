---
url: 'https://docs.workato.com/en/on-prem/groups/create-group.md'
description: >-
  Create an on-prem group in Workato to organize on-prem agents and set the
  connection type used to reach on-premises resources.
---

# Create group

Complete the following steps to create an on-prem group:

1. Sign in to Workato.
   
2. Go to **Tools > On-prem groups**. ![On-prem menu option](/assets/navigate-to-opa.Ie_o-suc.png)_On-prem menu option_
   
3. Click **Create on-prem group** to open the **New on-prem group** dialog.
   
   ![Empty on-prem group page](/assets/on-prem-group-empty-state.BxaczdB5.png)_Empty on-prem group page_
   
4. Enter a meaningful **Group name** and use the **Set up connections** field menu to select the type of connection you plan to set up.
   
   > **CONNECTION TYPES ARE PERMANENT**
   > 
   > You can't change an on-prem group's connection type after its creation.
   
   **Directly in Workato - Cloud profiles**
   
   Selecting **Directly in Workato** allows you to set up a connection directly in Workato as a [cloud profile](/en/on-prem/agents/connection/cloud) instead of managing a local configuration file. ![On-prem group for connection profiles](/assets/on-prem-cloud-profile.CvVG1H5O.png)_On-prem group for cloud profiles_
   
   **Manually in each agent - Connection profiles**
   
   Selecting **Manually in each agent** requires you to set up connection details in an on-prem agent configuration file as a [connection profile](/en/on-prem/agents/connection/profile). This is the legacy method of setting up connections. ![On-prem group for connection profiles](/assets/on-prem-conn-profile.DPszXNmy.png)_On-prem group for connection profiles_
   
5. Click **Create group** to create the new on-prem group.
   

Refer to [Add an agent](/en/on-prem/groups/add-agent) after creating your on-prem group to create an on-prem agent.

---
