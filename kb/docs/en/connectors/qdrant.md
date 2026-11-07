---
url: 'https://docs.workato.com/en/connectors/qdrant.md'
description: >-
  Store, search, and manage vectors in Qdrant collections from Workato recipes
  for RAG, semantic search, and AI agent knowledge bases.
---

# Qdrant

[Qdrant](https://qdrant.tech) is an open-source vector database that stores embeddings with payloads and runs similarity search. The Qdrant connector lets you store, search, and manage vectors in Qdrant collections from Workato recipes.

Use the Qdrant connector to:

- Upsert points into a collection.
- Query the nearest points using an embedding from an upstream step.
- Scroll through points with pagination.
- Retrieve points by ID, or delete points by ID or filter.
- List collections, get collection details, and create collections.

> **EMBEDDINGS ARE CREATED UPSTREAM**
> 
> Qdrant stores and searches vectors. It doesn't create them. Generate embeddings in a separate recipe step, such as an AI by Workato action, before you upsert or query points. Vector inputs are arrays of floats, not raw text.

## Install Qdrant from the community library

Complete the following steps to install the Qdrant connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Qdrant connector uses API key authentication.

### Qdrant setup

How you retrieve the Qdrant cluster and API key depends on what type of Qdrant instance you have. Use the instructions that match your use case.

- [Qdrant Cloud](#qdrant-cloud)
- [Self-hosted Qdrant](#qdrant-self-hosted)

#### Qdrant Cloud

1. Sign in to the [Qdrant Cloud console](https://cloud.qdrant.io).
   
2. Create a cluster. Skip this step if you plan to use an existing cluster.
   
   1. Click **Clusters > Create** on the cloud dashboard.
      
   2. Enter a name for your cluster in the **Name** field.
      
   3. Select a cloud provider to use in Qdrant.
      
   4. Select your region in the **Region** drop-down menu.
      
   5. Click **Create**.
      
3. Retrieve your cluster URL.
   
   1. Click **Clusters** in the side navigation menu.
      
   2. Select the cluster you plan to use.
      
   3. Copy the **Cluster URL**. For example, `https://xyz-example.region.provider.cloud.qdrant.io:6333`.
      
4. Generate a database API key.
   
   1. Go to the **Clusters** section in the side navigation menu.
      
   2. Click **API keys > Create database API key**.
      
   3. Copy the key to use in Workato.
      

#### Self-hosted Qdrant

1. Set the `QDRANT__SERVICE__API_KEY` environment variable on your instance. How you do this depends on the deployment method you choose, such as Docker CLI, Docker Compose, or Kubernetes. Refer to the Qdrant [security guide](https://qdrant.tech/documentation/guides/security/) for more information.
   
   > **AUTHENTICATION NOT ENABLED BY DEFAULT**
   > 
   > Self-hosted Qdrant instances don't have authentication enabled by default.
   
2. Enable TLS to prevent the key from being sent in plain text. How you do this depends on the deployment method you choose, such as Docker Compose or the `config.yaml` file. Refer to the Qdrant [security guide](https://qdrant.tech/documentation/guides/security/) for more information.
   

> **SELF-HOSTED INSTANCES MUST BE PUBLIC**
> 
> Workato can't reach `localhost` or private network addresses. Expose your instance at a public address or through a tunnel, and use that address as the cluster URL. For example, `https://qdrant.mycompany.com:6333`.

### Connect to Qdrant using API key authentication

Complete the following steps to set up a Qdrant connection in Workato:

1. Click **Create > Connection**.
   
2. Search for `Qdrant` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Qdrant connection setup page with Connection name, Location, Cluster URL, and API key fields.](/assets/qdrant-connection-setup.BrHhiInh.png)_Qdrant connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the full URL of your Qdrant cluster, including the port, in the **Cluster URL** field. For example, `https://xyz-example.region.provider.cloud.qdrant.io:6333`.
   
6. Enter your database API key in the **API key** field.
   
7. Click **Connect**.

---
