import jwt
from datetime import datetime, timedelta,timezone
import os
secret_key = os.environ.get("secret_key")
def generate_jwt(data: dict):
    temp = data.copy()
    expiration_time = datetime.now(timezone.utc) + timedelta(hours=1)
    temp.update({"exp": expiration_time, "iat": datetime.now(timezone.utc)})

    token = jwt.encode(temp,secret_key,algorithm="HS256")
    return token