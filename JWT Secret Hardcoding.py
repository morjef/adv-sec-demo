# Example 7: JWT Secret Hardcoding
import jwt
secret = "mysecretkey"
payload = {"user": "testuser"}
encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
