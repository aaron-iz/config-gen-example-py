from config.models.app_config import AppConfig
from config.models.auth_routes_config import AuthRoutesConfig
import os

ENV_NAME_ENV_VAR_KEY = "SERVICE_ENV_NAME"

class ConfigContainer:
    """
    Holds all config instances for global use.
    """
    AppConfig: AppConfig
    AuthRoutesConfig: AuthRoutesConfig
    
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