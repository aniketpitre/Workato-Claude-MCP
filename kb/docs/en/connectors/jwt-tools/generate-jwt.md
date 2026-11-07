---
url: 'https://docs.workato.com/en/connectors/jwt-tools/generate-jwt.md'
description: >-
  The Generate JWT action in the JWT tools by Workato connector lets you create
  a JSON Web Token by specifying the payload and header details.
---

# JWT tools by Workato - Generate JWT action

This action allows you to create a JSON Web Token by specifying the payload and header details. This action rounds down the values for `iat`, `exp`, and `nbf` to the nearest second.

![Generate JWT action](/assets/generate-jwt.Cz6bb3z5.png)_JWT tools by Workato - Generate JWT action_

## Input

- Payload
  
- The data about the entity and additional metadata, encoded as a JSON object.
  
  - Subject
    
  - The principal subject of the JWT.
    
  - Issued at (iat)
    
  - The timestamp of when the JWT was issued.
    
  - Expiration time (exp)
    
  - The timestamp for when the JWT is set to expire.
    
  - Not before Time (nbf)
    
  - The timestamp before which the JWT is not valid.
    
  - Issuer (iss)
    
  - The issuer of the JWT.
    
  - Audience (aud)
    
  - The recipients of the JWT.
    
  - JWT ID (jti)
    
  - A unique identifier for the JWT.
    
  - Scopes
    
  - The scopes included in the JWT.
    
  - Custom claims
    
  - Additional claims or data included in the JWT.
    
- Header
  
- The token type and the algorithm used for signing, encoded as a JSON object.
  
  - Key ID (kid)
  - The key identifier used to sign the JWT.

## Output

- JSON web token
- The encoded JWT string.

---
