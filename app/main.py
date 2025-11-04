from fastapi import FastAPI
from app.api.routes_auth import router as auth_router

# Move this to a configuration generator project and pull using configuration loader from json.
class AppConfig:
    Title: str = "Infra-AuthenticationService"
    AuthExtension: str = "/api/auth"

config = AppConfig()

# Fast API:
app = FastAPI()
app.include_router(auth_router, prefix=config.AuthExtension, tags=["auth"])