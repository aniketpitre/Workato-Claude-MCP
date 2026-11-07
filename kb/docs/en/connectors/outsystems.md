---
url: 'https://docs.workato.com/en/connectors/outsystems.md'
description: >-
  The OutSystems connector lets you create, update, search, and get records,
  including in batches, and trigger on new or updated records.
---

# OutSystems

[OutSystems](https://www.outsystems.com/) provides a low-code development platform that allows you to use visual tools and AI-based automation to develop, deploy, and manage your applications. OutSystems includes starter templates for customer portals, internal applications, and more.

## API version

The OutSystems connector uses the [OutSystems API](https://success.outsystems.com/documentation/11/reference/outsystems_apis/).

## Configuration

You must complete the steps in the following sections before you can set up your Workato OutSystems connection.

- [Create API key](#create-api-key)
- [Download OutSystems Workato Connector](#download-outsystems-workato-connector)

Refer to [OutSystems' documentation](https://success.outsystems.com/documentation/how_to_guides/integrations/how_to_integrate_outsystems_with_workato/) for more information about integration between OutSystems and Workato.

### Create API key

You must create an API key to connect your OutSystems account to Workato. To create an OutSystems API key:

1. Log in to your OutSystems account.
   
2. Click your profile name in the upper left corner and then click **My Settings**.
   
3. Click **Environments** in the top navigation menu to view the Environments page.
   
4. Click the environment you plan to connect to your Workato account. This displays the OutSystems Service Center.
   
5. Click **Administration** in the top navigation menu, click **Security**, and then click **Applications Authentication** under Environment Security.
   
   ![Environment security](/assets/environment-security.D0Fsak8N.png)_Click Administration > Security > Applications Authentication_
   
6. Click the **Generate** button for **Authentication and Encryption Keys**.
   
   ![Generate API key](/assets/generate-api-key.D2tF2vnm.png)_Generate the API key_
   
7. Click the **Add new key** button to add the API key to your environment.
   
   ![Add new key](/assets/add-new-key.B8bUid0x.png)_Add new key_
   
8. Copy the API key and store it in a safe location.
   
   ![Copy the API key](/assets/copy-api-key.B9nXL6xP.png)_Copy the API key_
   

### Download OutSystems Workato Connector

Complete the following steps to download the OutSystems Workato Connector to your OutSystems account.

1. Log in to your OutSystems account and navigate to the environment you plan to use for your Workato connection.
   
2. Click **Community** in the navigation bar. The Community page displays.
   
   ![Click Community](/assets/community-tab.CA-pMq8d.png)_Click Community_
   
3. Click **Forge** in the navigation bar. The Forge repository page opens.
   
   ![Click Forge](/assets/forge-tab.qyXTiiad.png)_Click Forge_
   
4. Enter `OutSystems Workato Connector` in the search box and then click **Search**.
   
5. Click **OutSystems Workato Connector** in the search results. The OutSystems Workato Connector information page displays.
   
   ![Click OutSystems Workato Connector](/assets/outsystems-workato-connector.B7jfOKk2.png)_Click OutSystems Workato Connector_
   
6. Click the **Download** button and then click **Agree and download** in the confirmation pop-up window.
   
   ![Click Download](/assets/download.CeUbj7jd.png)_Click Download_
   

## Connection setup

Complete the following steps to create an OutSystems connection in Workato.

1. Provide a **Connection name** that identifies which OutSystems instance Workato is connected to.
   
   ![Connection setup](/assets/connection-setup.mD9dBLu_.png)_Connection setup_
   
2. Use the **Connection type** drop-down menu to select your connection type.
   
3. Enter the API key for your connection in the **API key** field. Refer to the [Create API key section](#create-api-key) for more information.
   
4. Enter the URL for the OutSystems environment you plan to connect to your Workato account in the **Environment URL** field. This must be the same environment where you generated your API key in the previous section.
   
5. Click **Connect**.

---
