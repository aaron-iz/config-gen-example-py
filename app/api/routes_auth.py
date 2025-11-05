from datetime import timedelta
import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi import security
from fastapi.security import HTTPAuthorizationCredentials
from app.api.user_login_dto import UserLoginDTO
from app.api.user_registration_dto import UserRegistrationDTO
from app.core.security import create_token, decode_token
from app.db.database import find, save
from app.models.user import User
from config.config_container import config
import bcrypt


router = APIRouter()


def placeholder_response():
    """
    Placeholder response for development phase
    """
    return {"status": "ok"}


@router.get(config.AuthRoutesConfig.HealthEndpoint)
def health_check():
    return placeholder_response()


def create_jwt_token(user: User):
    jwt_token = create_token({
        "user_id": user["id"],
        "username": user["username"],
        "full_name": user["full_name"],
        "exp": datetime.utcnow() + timedelta(minutes=180)  # Move this to configuration
    })
    
    return {"token": jwt_token}


@router.post(config.AuthRoutesConfig.RegisterEndpoint)
def register_user(user_registration_dto: UserRegistrationDTO):
    hashed_password = bcrypt.hashpw(user_registration_dto.password.encode(), bcrypt.gensalt())
    
    user = User(
        username=user_registration_dto.username,
        password=hashed_password.decode(),
        full_name=user_registration_dto.full_name
    )
    
    save(user.model_dump())
    
    return create_jwt_token(user)


@router.post(config.AuthRoutesConfig.LoginEndpoint)
def login_user(user_login_dto: UserLoginDTO):
    # Find the user in the database
    user = find(user_login_dto.username)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if the password is correct
    if not bcrypt.checkpw(user_login_dto.password.encode(), user["password"].encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return create_jwt_token(user)


@router.post(config.AuthRoutesConfig.VerifyEndpoint)
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        # Decode the token
        decoded_token = decode_token(token)
        user_id = decoded_token.get("user_id")

        # Find the user in the database
        user = find(user_id)

        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"message": "Token verified successfully"}

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


# TODO: this code is too ugly commonize to some functions and just make it prettier + add logs.