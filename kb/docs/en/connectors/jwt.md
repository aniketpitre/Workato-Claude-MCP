---
url: 'https://docs.workato.com/en/connectors/jwt.md'
description: >-
  The JWT tools by Workato connector is a utility connector that generates and
  decodes JSON Web Tokens for secure authentication and information exchange.
---

# JWT tools by Workato

The JWT tools by Workato connector provides a secure method for generating and decoding JSON Web Tokens (JWT), ensuring secure authentication and information exchange. JWTs are compact, URL-safe methods to represent claims between two parties. These claims are encoded as a JSON object. You can use them in a JSON Web Signature (JWS) structure or as plaintext in a JSON Web Encryption (JWE) structure. This allows you to create digital signatures and integrity protection with a Message Authentication Code (MAC) or encryption.

## Prerequisites

Before using the JWT tools connector, you must complete the following steps:

1. [Generate a public/private key pair](/en/oem/jwt-direct-linking#step1)
   
2. [Install a direct link URL microservice](/en/oem/jwt-direct-linking#step2)
   
3. [Generate a JWT](/en/oem/jwt-direct-linking#step3)
   

## How to connect to the JWT connector on Workato

![JWT connection](/assets/jwt-connection.VPlVw4-3.png)_Connection setup_

- Connection name
  
- Enter a unique identifier for your connection to identify and reuse it in your recipes.
  
- Signing algorithm
  
- Choose the JWT signing algorithm required for your connection.
  
- HMAC shared secret
  
- Input the shared HMAC secret key for signing the token. It must be a string with a minimum length of 32 characters.
  

### Actions

The JWT tools by Workato connector supports the following recipe actions:

- [Generate JWT](/en/connectors/jwt-tools/generate-jwt)
- [Decode JWT](/en/connectors/jwt-tools/decode-jwt)

---
