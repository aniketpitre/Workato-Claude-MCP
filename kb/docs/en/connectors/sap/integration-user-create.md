---
url: 'https://docs.workato.com/en/connectors/sap/integration-user-create.md'
description: >-
  Create a dedicated Workato integration user in SAP, including activating the
  user, creating an integration role, and linking the user to the role.
---

# Create a Workato integration user in SAP

Creating a Workato integration user in Sap consists of the following steps:

1. [Create a new user in SAP](#new-user-create)
2. [Activate your newly-created Workato user](#new-user-activate)
3. [Create a Workato integration role](#role-create)
4. [Link your user to your newly-created role](#user-link)

* * *

## Create a new user in SAP

To begin, you must first create a user in your SAP system which is dedicated to Workato. This user is used later on with the minimum required permissions to run your integrations.

> **RECOMMENDED USER TYPE**
> 
> We recommend you use the `Communication` user type in SAP. This is reserved by SAP for dialog-free communication between systems (through RFC) and does not provide GUI access.

1. Go to transaction code `SU01`, give the new user a name that is relevant to Workato. In the following example, we have named the user **WORKATO\_INT**.
   
2. When creating a user, you must provide mandatory fields like **Last name** and **password**. These are located in the **Address** and **Logon Data** tab respectively.
   
   ![Create new user](/assets/create_new_user.C6pOIMtS.png)
   

> **USER PERMISSIONS**
> 
> This user's permission dictates which RFCs Workato can run and which IDocs Workato can send and receive.

* * *

## Activate your newly-created Workato user

After creating your new user, you must log in to SAP change the password to productive, if you are using **Dialog** user type. Note your password and the username as both are required to set up your OPA in Workato.

* * *

## Create a Workato Integration Role

Assign a role to this newly-created user. This role grants access to specific objects in your SAP system. This guide demonstrates how to configure the minimum authorizations required to connect to SAP from Workato.

> **USER PERMISSIONS**
> 
> These instructions do not include authorizations required to run any RFCs, receive IDocs, and send any IDocs required for the connector, but they are the set of base authorizations required to establish a connection and fetch IDoc and RFC metadata. Additionally, to determine the permissions required to run actions and triggers for IDoc in Workato, please refer to the [minimum permissions section](/en/connectors/sap/permissions-sap) of this guide.

1. Go to transaction code `PFCG` and type in the role to assign to this Workato user. In our example, we have name the role `Z_MIN_AUTH_ROLE_WORKATO`.
   
2. Select the **Single role** button after providing your chosen name.
   
   ![Create new role in PFCG](/assets/create_new_role.c6NYy1pz.png)
   
3. Give your new role a description.
   
4. Navigate to the **Authorizations** tab. Generate a profile by selecting the button next to the **Profile Name** input field.
   
5. After the profile is generated, select **Change Authorization Data**. You must assign the following permissions. These permissions help the Workato connector with Authentication and reading metadata from your SAP system. Assign permissions by maintaining the role manually with the button located in the top section of the interface.
   
   Summary of authorization objects to be added
   
   <dl><dt>S_RFC</dt><dd>Required to authorize Workato to call certain function groups and modules. (Also, responsible for establishing basic connection with Workato)</dd><dt>S_TABU_DIS</dt><dd>Determines which group of tables using authorization groups users can access.</dd><dt>S_TABU_NAM</dt><dd>Determines which exact table(s) users can access. This authorization object permits users to access a specific table within an authorization group that they otherwise cannot access.</dd></dl>
   
   Authorization Field Values for S\_RFC Object
   
   <dl><dt>Required for Basic Connection</dt><dd><dl class="horizontal-dl"><dt>RFC_NAME</dt><dd>Name of RFC object</dd><dt>Values:</dt><dd><ul><li>EDIMEXT</li><li>RFC_METADATA</li><li>SDTX</li><li>SVRZ</li><li>SYST</li><li>OCS_CRM</li><li>RFC1 (For Older Enhancement Packages in SAP ERP)</li></ul></dd></dl></dd><dd><dl class="horizontal-dl"><dt>ACTVT</dt><dd>Activity</dd><dt>Values:</dt><dd><ul><li>16</li></ul></dd></dl></dd><dd><dl class="horizontal-dl"><dt>RFC_TYPE</dt><dd>Type of RFC Object</dd><dt>Values:</dt><dd><ul><li>FUGR</li></ul></dd></dl></dd></dl>
   
   <dl><dt>Required for further Connector Operations (RFC, IDoc)</dt><dd><dl class="horizontal-dl"><dt>RFC_NAME</dt><dd>Name of RFC object</dd><dt>Values:</dt><dd><ul><li>SDIFRUNTIME</li><li>RFC2</li><li>BASR</li><li>ARFC (Only required if sending IDocs)</li><li>EDIN (Only required if sending IDocs)</li></ul></dd></dl></dd><dd><dl class="horizontal-dl"><dt>ACTVT</dt><dd>Activity</dd><dt>Values:</dt><dd><ul><li>16</li></ul></dd></dl></dd><dd><dl class="horizontal-dl"><dt>RFC_TYPE</dt><dd>Type of RFC Object</dd><dt>Values:</dt><dd><ul><li>FUGR</li></ul></dd></dl></dd></dl>
   
   Authorization Field Values for S\_TABU\_DIS Object
   
   <dt>Required for Connector Operations</dt>
   
   <dd><dl class="horizontal-dl"><dt>DICBERCLS</dt><dd>Table Authorization Group</dd><dt>Values:</dt><dd><ul><li>SS</li><li>SC</li><li>SA</li></ul></dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>ACTVT</dt><dd>Activity</dd><dt>Values:</dt><dd><ul><li>02</li><li>03</li></ul></dd></dl></dd>
   
   Authorization Field Values for S\_TABU\_NAM Object
   
   <dt>Required for Connector Operations</dt>
   
   <dt>*Change and Display access to below tables*</dt>
   
   <dd><dl class="horizontal-dl"><dt>TABLE</dt><dd>Table Name</dd><dt>Values:</dt><dd><ul><li>TAPLT</li><li>TFDIR</li><li>RFCDES</li><li>EDIPOA</li></ul></dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>ACTVT</dt><dd>Activity</dd><dt>Values:</dt><dd><ul><li>02</li><li>03</li></ul></dd></dl></dd>
   
   <dt>*Display access to below tables*</dt>
   
   <dd><dl class="horizontal-dl"><dt>TABLE</dt><dd>Table Name</dd><dt>Values:</dt><dd><ul><li>TFTIT</li><li>EDP13</li><li>TBD05</li><li>EDP21</li></ul></dd></dl></dd>
   
   <dd><dl class="horizontal-dl"><dt>ACTVT</dt><dd>Activity</dd><dt>Values:</dt><dd><ul><li>03</li></ul></dd></dl></dd>
   
6. Your final Authorization should look like this:
   
   ![Authorizations for profile](/assets/authorisations.BkK-KK3P.png)
   
7. Press the **generate** button (the white and red circular button in your top bar) to save your Authorization.
   

* * *

## Link your user to your newly-created role

To link your user to your newly-created role:

1. Go to transaction code `SU01` and edit the user you created in [Step 1: Create a new user in SAP using SU01](#new-user-create).
   
2. Click the **Roles** tab.
   
3. Proceed ahead and `Assign` the role which you have just created.
   
   ![Assign role to user](/assets/role_assignment.C75iU-Ev.png)
   
4. Click **Save**.
   

* * *

> **FURTHER READING**
> 
> To complete your connection to SAP RFC, read the following guides:
> 
> 1. [Configure OPA for SAP](/en/connectors/sap/opa-configure).
> 2. [Configure the Workato SAP connector](/en/connectors/sap/sap-connector).
> 3. [Optional: Configure IDocs to/from Workato in SAP](/en/connectors/sap/configure-idoc-sap).

---
