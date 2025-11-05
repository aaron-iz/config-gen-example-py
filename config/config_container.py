from config.models.app_config import AppConfig
from config.models.auth_routes_config import AuthRoutesConfig
from app.core.security.security_config import SecurityConfig
import os

ENV_NAME_ENV_VAR_KEY = "SERVICE_ENV_NAME"

class ConfigContainer:
    """
    Holds all config instances for global use.
    """
    AppConfig: AppConfig
    AuthRoutesConfig: AuthRoutesConfig
    SecurityConfig: SecurityConfig
    
    def __init__(self):
        self._env = os.environ.get(ENV_NAME_ENV_VAR_KEY, None)
        
    @property
    def env(self):
        return self._env

# Load all configs automatically
config = ConfigContainer()

# register your config here and pass it the env:
config.AppConfig = AppConfig.load(config.env)
config.AuthRoutesConfig = AuthRoutesConfig.load(config.env)
# config.SecurityConfig = SecurityConfig.load(config.env) will fail now, no generator