---
url: 'https://docs.workato.com/en/connectors/email-custom.md'
description: >-
  Email (Custom) is a utility connector that lets you send and receive email
  over SMTP and IMAP, with TLS and SSL/TLS support.
---

# Email (Custom)

[Email (Custom)](https://app.workato.com/custom_adapters/890909/details?community=true) is a utility connector that lets you send and receive email over SMTP and IMAP. It supports TLS for SMTP and SSL/TLS for IMAP as required.

## Prerequisites

Ensure you have the following before you establish a connection to Email (Custom) in Workato:

- An email account
- SMTP Server address
- SMTP Server port

## Connect to Email (Custom)

Complete the following steps to connect Workato to Email (Custom):

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Email (Custom)** as your connection on the **New Connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![Email (Custom) connection setup](/assets/email-custom-connection-setup.CG7q1TFV.png)_Email (Custom) Connection Setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Username**, **Password**, **SMTP Server**, and **SMTP Port.**
   
6. Set the **Use STARTTLS for SMTP?** field to **Yes** if you use TLS for SMTP.
   
7. Select **IMAP** or **POP3** in the **Receiving protocol** field to receive emails:
   
   - For IMAP, enter the **IMAP server** and **IMAP port**.
   - For POP3, enter the **POP3 server** and **POP3 port**.
8. Set the **Enable SSL/TLS for IMAP?** or **Enable SSL/TLS for POP3?** field to **Yes** if you use SSL/TLS to receive emails.
   
9. Click **Connect**.

---
