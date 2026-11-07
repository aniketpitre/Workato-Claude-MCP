---
url: 'https://docs.workato.com/en/oem/jwt-direct-linking.md'
description: >-
  Set up JWT direct linking for Workato Embedding: generate a key pair, install
  a direct link URL microservice, and create a signed JWT.
---

# JWT direct linking

JSON Web Token (JWT) is an open standard that defines a compact and self-contained method for securely transmitting information between two parties as a JSON object. JWTs are signed with private/public key pairs, which verify the integrity of the token and add an additional layer of security.

JSON Web Tokens authenticate users and provide verified access to applications and resources. Generate a JWT before implementing any Workato Embedding models.

JWT direct linking consists of the following steps:

1. [Generate a public/private key pair](#step1)
2. [Install a direct link URL microservice](#step2)
3. [Generate a JWT](#step3)

## Prerequisites

The following information is required to implement JWT direct linking:

- Private and public key pair
  
- **Required**. The JWT token must be signed using a private key generated with the RS256 algorithm. The key must be formatted as PEM, and can follow either the PKCS#1 or PKCS#8 standard, as long as RS256 is used. PKCS#1 is used only for RSA private keys, and contains only the RSA private key material, such as the modulus, public exponent, private exponent, and more. PKCS#1 is commonly used with `openssl genrsa`. PKCS#8 is for private keys of any algorithm, such as RSA, EC, DSA, and more. PKCS#8 wraps the key into a generic, standardized format with algorithm identification, and is commonly used with `openssl genpkey`. Workato uses the public key to verify the generated JWT tokens. Use the [Update JWT signing key API](/en/oem/oem-api/jwt-direct-link-configurations#update-jwt-signature-verification-key) to set the public key or provide the public key to your Workato Success Representative.
  
- Embedded vendor ID
  
- **Required**. The Embedded vendor ID is required to generate the JWT. Use the vendor ID returned by the [Update JWT signing key API](/en/oem/oem-api/jwt-direct-link-configurations#update-jwt-signature-verification-key) or obtain it from your Workato Success Representative after providing your public key.
  
- Customer workspace ID
  
- **Required**. The customer workspace ID uniquely identifies the Embedded customer. Obtain the customer workspace ID from the UI by navigating to the **Admin console** and selecting the specific customer. When selected, the customer workspace ID appears in the URL. Alternatively, fetch the customer workspace ID by calling our [get customer API](/en/oem/oem-api/managed-users#get-customer-account). If using an external ID instead of the Workato ID, the segment should start with the prefix `E`.
  
- Customer user ID
  
- **Optional**. The customer user ID uniquely identifies an individual workspace member in the customer workspace. Include the customer user ID when the user's specific role must apply to the Workato session being created. You can fetch the customer user ID by calling our [get customer workspace member API](/en/oem/oem-api/managed-users#get-list-of-customer-account-members). Ensure each user is created using the [add member to customer workspace API](/en/oem/oem-api/managed-users#add-member-to-customer-account) per customer team. If using an external ID instead of the Workato ID, the segment should start with the prefix `E`.
  
- Origin URL
  
- **Required**. The origin URL is the default domain where you embed the Workato `iframe`. Include the origin URL in the JWT payload when the Workato `iframe` is fully embedded within a partner's application. Additionally, include it when using the Auth Widget with multiple origin URLs allowlisted in the OEM Config. Provide your Workato Success Representative with the origin URL.
  

## Step 1: Generate a private and public key pair

### Generate a private key

To generate the private key from scratch, use the following:

```shell
$ openssl genrsa -out private.key 2048
$ cat private.key
-----BEGIN RSA PRIVATE KEY-----

...

-----END RSA PRIVATE KEY-----
```

### Generate a public key

Then, extract the public key using the following:

```shell
$ openssl rsa -in private.key -pubout -out public.key
$ cat public.key
-----BEGIN PUBLIC KEY-----

...

-----END PUBLIC KEY-----
```

### Convert keys to PEM format

If you used a different method to generate your public/private key pair, convert your keys to PEM format before sending them to Workato.

To convert from an SSH public key:

```shell
$ ssh-keygen -f key.pkcs -e -m pem > key.pem
```

## Step 2: Install a direct link URL generation microservice

The purpose of the direct link URL microservice is to automatically generate a JWT when needed to facilitate access to secure resources. Install a direct link URL microservice to your server.

The microservice must meet the following specifications:

- The endpoint must require vendor authentication.
- The microservice must accept the path to the Workato asset.
- The microservice must generate a URL with the following structure:

```
https://app.workato.com/direct_link/<resource_path>?<query_params>#<fragment>
```

### Example microservice:

```javascript
import nanoid from 'nanoid';
import {sign} from 'jsonwebtoken';

function getToken(WorkatoEmbeddedVendorId, customerAccountId, privateKey) {
  return sign({
    sub: `${WorkatoEmbeddedVendorId}:${customerAccountId}`,
    jti: nanoid()
  },
  privateKey,
  {
    algorithm: 'RS256'
  });
}
```

## Step 3: JWT direct linking

### JWT structure

A JWT consists of a header, payload, and signature. In their compact form, JWT sections are separated by `.`.

```
header.payload.signature
```

<dl><dt>Header</dt><dd>The first part of the token is the header. The header usually consists of two parts: the type of token and the type of algorithm used to generate the signature.</dd><dt>Payload</dt><dd>The second part of the token is the payload, which contains the claims. Claims are statements about the user and additional data.</dd><dt>Signature</dt><dd>The final part of the token is the signature. Signatures verify the integrity of the claims.</dd></dl>

### Direct link URL

You must generate a JWT token on your server and construct the direct link URL. The direct link URL format differs depending on the CX option you plan to implement.

Embedded connection widget

The direct link URL format for the [Embedded connection widget](/en/oem/workato-embedded-implementation#connection-widget) should match the following examples. For more information on direct link URLs for other widgets, refer to [Constructing a direct link URL](/en/oem/workato-embedded-implementation#construct-url).

**Workato accounts hosted in the US Data Center**

```html
https://app.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Europe Data Center**

```html
https://app.eu.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Singapore Data Center**

```html
https://app.sg.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Japan Data Center**

```html
https://app.jp.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Australia Data Center**

```html
https://app.au.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Israel Data Center**

```html
https://app.il.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the China Data Center**

```html
https://app.workatoapp.cn/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the South Korea Data Center**

```html
https://app.kr.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the United Kingdom Data Center**

```html
https://app.uk.workato.com/direct_link/embedded/connections/<connection_id>?workato_dl_token=<jwt_token>
```

Fully Embedded

The direct link URL format for [Fully Embedded](/en/oem/workato-embedded) should match the following examples:

**Workato accounts hosted in the US Data Center**

```html
https://app.workato.com/direct_link?workato_dl_path=<workato_path>&workato_
dl_token=<jwt_token>
```

**Workato accounts hosted in the Europe Data Center**

```html
https://app.eu.workato.com/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

**Workato accounts hosted in the Singapore Data Center**

```html
https://app.sg.workato.com/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

**Workato accounts hosted in the Japan Data Center**

```html
https://app.jp.workato.com/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

**Workato accounts hosted in the Australia Data Center**

```html
https://app.au.workato.com/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

**Workato accounts hosted in the Israel Data Center**

```html
https://app.il.workato.com/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

**Workato accounts hosted in the China Data Center**

```html
https://app.workatoapp.cn/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

**Workato accounts hosted in the South Korea Data Center**

```html
https://app.kr.workato.com/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

**Workato accounts hosted in the United Kingdom Data Center**

```html
https://app.uk.workato.com/direct_link?workato_dl_path=<workato_path>&workat
o_dl_token=<jwt_token>
```

Branded access SSO

The direct link URL format for [Branded access SSO](/en/oem/branded-access-implementation) should match the following examples:

**Workato accounts hosted in the US Data Center**

```html
https://app.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Europe Data Center**

```html
https://app.eu.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Singapore Data Center**

```html
https://app.sg.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Japan Data Center**

```html
https://app.jp.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Australia Data Center**

```html
https://app.au.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Israel Data Center**

```html
https://app.il.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the China Data Center**

```html
https://app.workatoapp.cn/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the South Korea Data Center**

```html
https://app.kr.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the United Kingdom Data Center**

```html
https://app.uk.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

### Generate a JWT

Generating a JWT consists of the following steps:

1. [Configure the header](#step1-header)
2. [Configure the payload](#step2-payload)
3. [Sign the token](#step3-signature)

1. Step 1: Configure the header
   
   <dl><dt>alg</dt><dd>Set the <code>alg</code> claim to RS256, the algorithm used to generate the signature.</dd><dt>typ</dt><dd>Set the <code>typ</code> claim to JWT, the type of token used.</dd></dl>
   
   Example:
   
   ```json
   {
     "alg": "RS256",
     "typ": "JWT"
   }
   ```
   
2. Step 2: Configure the payload
   
   <dl><dt>sub</dt><dd>Set the <code>sub</code> claim to:</dd></dl>
   
   ```json
   <workato_embedded_vendor_id>:<customer_team_id>:<customer_user_id>
   ```
   
   > **PREREQUISITES**
   > 
   > Visit the [Prerequisites](#prerequisites) section for detailed instructions on obtaining the Embedded vendor ID, customer workspace ID, and customer user ID.
   
   <dl><dt>iat</dt><dd>Set the <code>iat</code> claim to the current time in epoch.</dd><dt>jti</dt><dd>Set the <code>jti</code> claim to a globally unique value. Use the value only one time in a 10-minute duration.</dd><dt>origin</dt><dd>The origin claim is required when the connection <code>iframe</code> is embedded in two or more origins.</dd></dl>
   
   > **MULTIPLE ORIGINS**
   > 
   > If you are embedding the Connection Widget in multiple domains, you must configure the origin URL in each customer workspace. To override the origin URL in an individual account, go to the **Admin console > manage customers**, and access the relevant **customer workspace**. Access the **settings** menu and update the origin URL.
   
   Example:
   
   ```json
   {
     "sub": "911672h4203fae7ffbe2eca1bbcaa79cc8c47af5377a6c6240:303363:313646",
     "iat":"1624043461",
     "jti": "3oay2t2kntGbxr1yhSINn",
     "origin": "http://www.acme.com"
   }
   ```
   
   See more [JWT microservice examples.](https://github.com/auth0/node-jsonwebtoken)
   
3. Step 3: Sign the JWT
   
   Sign the JWT with your private key generated with the RS256 algorithm in [Step 1.](#step1) The private key must match the public key previously provided to Workato.

---
