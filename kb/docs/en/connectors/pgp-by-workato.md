---
url: 'https://docs.workato.com/en/connectors/pgp-by-workato.md'
description: >-
  PGP tools by Workato is a utility connector that encrypts, decrypts, signs,
  and verifies data using the AES256 cipher and SHA256 digest.
---

# PGP tools by Workato

The PGP tools by Workato connector encrypts, decrypts, signs, and verifies data using the AES256 cipher and SHA256 digest. Use this connector to secure sensitive files or confirm the integrity of signed content across systems.

## How PGP tools by Workato works

This connector uses the AES256 cipher and SHA256 digest to process files based on the common PGP standard. Each action handles a specific part of the encryption or signing workflow:

- [Encrypt data action](/en/connectors/pgp-by-workato/encrypt-data-action): Encrypts file content using a public key.
- [Decrypt data action](/en/connectors/pgp-by-workato/decrypt-data-action): Decrypts content using the private key and passphrase.
- [Sign a message action](/en/connectors/pgp-by-workato/sign-message-action): Signs content using the private key and passphrase from the connection.
- [Verify a signed message action](/en/connectors/pgp-by-workato/verify-signed-message): Verifies the integrity of signed content using a public key.

## Set up PGP tools by Workato

PGP tools by Workato requires a public and private key pair to perform encryption, decryption, signing, and verification. Complete the following steps to generate keys and create the connection in Workato.

- [Step 1: Generate a PGP key pair](#generate-a-pgp-key-pair)
- [Step 2: Create the connection in Workato](#complete-the-setup-in-workato)

### Generate a PGP key pair

Complete the following steps to generate a set of PGP keys, if you don't already have one:

1. Download and install the [GPG command line tools](https://www.gnupg.org/download/) for your operating system. Ensure that the GPG version used is **v2.2.x or lower**.
   
2. Open the **Terminal** or **Command Prompt**.
   
3. Run the following command to generate a PGP key pair:
   
   ```
   gpg --full-generate-key
   ```
   
4. Select **RSA key** and **3072 bits** using the command prompts.
   
5. Enter your user ID information, including a valid name and email address.
   
6. Enter a secure passphrase. Save this passphrase for when you [set up the connection](#complete-the-setup-in-workato) in Workato.
   
7. Run the following command to list the PGP keys for which you have both a public and private key:
   
   ```
   gpg --list-secret-keys --keyid-format LONG
   ```
   
8. Copy the PGP key ID you plan to use from the list of PGP keys. The PGP key ID in the following example is `7F87F1F21EEAAAB9`:
   
   ![PGP key ID](/assets/gpg-key-id.CNehwq9H.png)
   
9. Run the following commands with your PGP key ID in place of `7F87F1F21EEAAAB9` to display your `Public Key` and `Private Key`:
   
   ```
   gpg --armor --export 7F87F1F21EEAAAB9
   
   gpg --armor --export-secret-key 7F87F1F21EEAAAB9
   ```
   
10. Return to Workato to [complete the setup](#complete-the-setup-in-workato).
    

### Complete the setup in Workato

Complete the following steps to configure PGP tools by Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `PGP tools by Workato` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your PGP **Private key**. This field is required for the **Decrypt data** and **Sign a message** actions.
   
6. Enter your PGP **Passphrase**.
   
7. Enter your PGP **Public key**. This field is required for the **Encrypt** action.
   
8. Click **Connect** to complete the setup. ![PGP Connection](/assets/pgp-connection.f7KQlXfc.png)_Complete the connection fields and click **Connect**_

---
