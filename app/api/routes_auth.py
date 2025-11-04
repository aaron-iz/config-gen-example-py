from fastapi import APIRouter

router = APIRouter()

def placeholder_response():
    """
    Placeholder response for development phase
    """
    return {"status": "ok"}

@router.get("/health")
def health_check():
    return placeholder_response()

@router.post("/register")
def register_user():
    return placeholder_response()

@router.post("/login")
def login_user():
    return placeholder_response()

@router.post("/verify")
def verify_token():
    return placeholder_response()


# TODO: Implemnt + doc-string