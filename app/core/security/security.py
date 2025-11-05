import jwt

# Consts:
ALGO = "HS256"

# Properties:
__jwt_secret = None

# Load (abstracts away implemetation):
def load_secret():
    global __jwt_secret
    if __jwt_secret is not None:
        return __jwt_secret
    
    # get certificate from config
    # request the secret
    __jwt_secret = "PLACEHOLDER" # placehoder see the config model file for explanation
    return __jwt_secret

# simple impl not verifying audiences etc, will be added later
def create_token(data: dict):
    secret = load_secret()
    
    return jwt.encode(data, secret, algorithm=ALGO)

def validate_token(token: str):
    secret = load_secret()
    
    try:
        jwt.decode(token, secret, algorithms=[ALGO])
        return True
    except jwt.ExpiredSignatureError:
        return False