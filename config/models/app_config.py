from typing import ClassVar
from config.base_config_model import BaseConfigModel

class AppConfig(BaseConfigModel):
    ConfigFileName: ClassVar[str] = "app_config"
    
    Title: str
    AuthExtension: str
    JwtSecretFileName: str