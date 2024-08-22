from jose import JWSError, jwt
from datetime import datetime, timedelta


SECRET_KEY = '1234567890oiuytrewazxcvjm123456789iuytreasdfghjklmnbvcxzxcvbnm'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 15


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})

    jwt_encode = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_encode

