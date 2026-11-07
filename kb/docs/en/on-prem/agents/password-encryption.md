---
url: 'https://docs.workato.com/en/on-prem/agents/password-encryption.md'
description: >-
  Encrypt passwords and private keys in the on-prem agent config file using the
  OPA encryptor tool to secure sensitive data.
---

# Password Encryption

To avoid exposure of any sensitive data (like passwords or private keys) in your configuration file (`config.yml`), it is recommended to secure your passwords. You can encrypt them using the OPA [encryptor tool](#how-to-use-the-encryptor-tool) or use an [external secrets manager](/en/on-prem/agents/secrets-manager).

## How to use the encryptor tool

You will have to be in your on-prem agent's installed folder to use the encryptor.

1. Make sure you have your agent keys properly downloaded and placed into the `conf` folder. They are required for encryption.
   
2. Run the encryptor tool in your command line.
   
   - For Windows: `<INSTALL_HOME>\bin\encryptor.cmd`
   - For Linux and Mac: `<INSTALL_HOME>/bin/encryptor.sh`
3. When prompted, enter your secret value twice.
   
4. The script will print an encrypted text. Example:
   
   ```shell
   {encrypted: 'RCVtuGPjJWNqwkFQvhT...'}
   ```
   
5. Copy and paste the provided text as a value into `config.yml`. Make sure your value is in a single line. For example, in a database profile:
   
   ```yaml
   database:
     sales:
       url: jdbc:postgresql://sales.database:5432/sales
       username: joe
       password: {encrypted: 'RCVtuGPjJWNqwkFQvhT...'}
   ```
   

> **Unique encrypted key for each agent**
> 
> The encryption is based on your agent's private key. You cannot use encrypted value from one agent inside another agent's configuration. Note that only _YAML_ values can be encrypted (you cannot encrypt _YAML_ property keys).

---
