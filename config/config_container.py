from config.models.app_config import AppConfig
from config.models.auth_routes_config import AuthRoutesConfig

class ConfigContainer:
    """
    Holds all config instances for global use.
    """
    AppConfig: AppConfig
    AuthRoutesConfig: AuthRoutesConfig

# Load all configs automatically
config = ConfigContainer()
config.AppConfig = AppConfig.load()
config.AuthRoutesConfig = AuthRoutesConfig.load()