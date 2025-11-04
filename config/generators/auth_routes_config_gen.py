from config.config_generation import ConfigGenerator
from config.models.auth_routes_config import AuthRoutesConfig
from config.environment_keys import LOCAL_ENV, STAGE_ENV, PROD_ENV, IL_PROD_ENV
from typing import Dict

class AuthRoutesConfigGenerator(ConfigGenerator):
    """
    Generator for AuthRoutesConfig. Returns the same default routes for all environments.
    """

    def generate(self) -> Dict[str, AuthRoutesConfig]:
        default_config = AuthRoutesConfig(
            HealthEndpoint="/health",
            RegisterEndpoint="/register",
            LoginEndpoint="/login",
            VerifyEndpoint="/verify"
        )

        return {
            LOCAL_ENV: default_config,
            STAGE_ENV: default_config,
            PROD_ENV: default_config,
            IL_PROD_ENV: default_config,
        }
