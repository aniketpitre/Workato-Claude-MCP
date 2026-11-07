---
url: 'https://docs.workato.com/en/connectors/coingecko.md'
description: >-
  CoinGecko is an independent cryptocurrency data aggregator providing prices,
  market data, historical charts, and metadata for thousands of coins.
---

# CoinGecko

[CoinGecko](https://www.coingecko.com/) is an independent cryptocurrency data aggregator providing prices, market data, historical charts, and metadata for thousands of coins. This connector lets you get coin prices and details, list coins by market data, and search coins, exchanges, categories, and NFTs from Workato recipes.

## Install CoinGecko from the community library

Complete the following steps to install the CoinGecko connector from the [community library](https://www.workato.com/browse/connectors):

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

The CoinGecko connector uses API key authentication.

### CoinGecko setup

Complete the following steps to create an API key in CoinGecko:

1. Sign in to your CoinGecko account and open the [developer dashboard](https://www.coingecko.com/en/developers/dashboard).
   
2. Click the **API keys** tab.
   
3. Click **Add New Key**.
   
4. Copy your API key for use in Workato.
   

### Connect to CoinGecko using API key

Complete the following steps to connect to CoinGecko in Workato:

1. Click **Create > Connection**.
   
2. Search for `CoinGecko` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![CoinGecko connection setup](/assets/coingecko-connection-setup.BXN-IFgv.png)_CoinGecko connection setup._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Plan** drop-down menu to select **Demo** or **Pro**, depending on your API key. Demo keys use the `api.coingecko.com` host, while Pro keys use `pro-api.coingecko.com`.
   
6. Enter your API key in the **API key** field.
   
7. Click **Connect**.

---
