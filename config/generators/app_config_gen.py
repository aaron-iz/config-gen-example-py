from config.config_generation import ConfigGenerator
from config.models.app_config import AppConfig
from config.environment_keys import LOCAL_ENV, STAGE_ENV, PROD_ENV, IL_PROD_ENV
from typing import Dict, List

class AppConfigGenerator(ConfigGenerator):
    """
    Generator for AppConfig. Returns the same default config for all environments.
    """

    def generate(self) -> Dict[str, AppConfig]:
        default_config = AppConfig(
            Title="Infra-AuthenticationService",
            AuthExtension="/api/auth",
            JwtSecretFileName=".secret"
        )

        return {
            LOCAL_ENV: default_config,
            STAGE_ENV: default_config,
            PROD_ENV: default_config,
            IL_PROD_ENV: default_config,
        }
