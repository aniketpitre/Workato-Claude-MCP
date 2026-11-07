---
url: 'https://docs.workato.com/en/connectors/jwt-tools/decode-jwt.md'
description: >-
  The Decode JWT action in the JWT tools by Workato connector decodes a JSON Web
  Token and validates its iat, exp, and nbf claims when present.
---

# JWT tools by Workato - Decode JWT action

This action decodes a JSON Web Token (JWT) and validates its `iat` (Issued At), `exp` (Expiration Time), and `nbf` (Not Before) claims, if they are present. It raises an exception if the token is invalid.

![Decode JWT action](/assets/decode-jwt.DDotGJnK.png)_JWT tools by Workato - Decode JWT action_

## Input

- JSON web token
  
- The decoded JWT string.
  
- Exp leeway
  
- The leeway time in seconds before the JWT expires.
  

## Output

- Payload
  
- The data extracted from the JWT after decoding.
  
  - Subject
    
  - The principal subject of the JWT.
    
  - Issued at (iat)
    
  - The timestamp of when the JWT was issued.
    
  - Expiration time (exp)
    
  - The timestamp for when the JWT is set to expire.
    
  - Not before time (nbf)
    
  - The timestamp indicating when the JWT becomes valid.
    
  - Issuer (iss)
    
  - The issuer of the JWT.
    
  - Audience (aud)
    
  - The recipients of the JWT.
    
  - JWT ID (jti)
    
  - The unique identifier for the JWT.
    
  - Scopes
    
  - The information about the permissions the JWT carries.
    
- Header
  
- The part of the JWT that is decoded.
  
  - Key ID (kid)
    
  - The key identifier used to secure the JWT.
    
  - Algorithm
    
  - The cryptographic algorithm used to secure the JWT.

---
