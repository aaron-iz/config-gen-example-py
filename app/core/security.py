import jwt
from config.config_container import config


# Consts:
ALGO = "HS256"


# Properties:
__jwt_secret = None


# Load jwt secret
def load_jwt_secret():
    global __jwt_secret
    filename = config.AppConfig.JwtSecretFileName
    
    with open(filename, "r") as f:
        __jwt_secret = f.read().strip()
    
    __jwt_secret


def secret():
    if __jwt_secret is None:
        load_jwt_secret()
        
    if __jwt_secret is None:
        raise Exception("Failed to load JWT secret")
    
    return __jwt_secret


# JWT functions
def create_token(data: dict):
    return jwt.encode(data, secret(), algorithm=ALGO)


def decode_token(token: str):
    return jwt.decode(token, secret(), algorithms=[ALGO])


def verify_token(token: str):
    try:
        return decode_token(token)
    except:
        return None