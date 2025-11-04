from fastapi import FastAPI
from app.api.routes_auth import router as auth_router
from config.config_container import config

# Fast API:
app = FastAPI()
app.include_router(auth_router, prefix=config.AppConfig.AuthExtension, tags=["auth"])