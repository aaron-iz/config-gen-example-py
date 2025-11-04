from fastapi import APIRouter
from config.config_container import config

router = APIRouter()

def placeholder_response():
    """
    Placeholder response for development phase
    """
    return {"status": "ok"}

@router.get(config.AuthRoutesConfig.HealthEndpoint)
def health_check():
    return placeholder_response()

@router.post(config.AuthRoutesConfig.RegisterEndpoint)
def register_user():
    return placeholder_response()

@router.post(config.AuthRoutesConfig.LoginEndpoint)
def login_user():
    return placeholder_response()

@router.post(config.AuthRoutesConfig.VerifyEndpoint)
def verify_token():
    return placeholder_response()


# TODO: Implemnt + doc-string