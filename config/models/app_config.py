from config.base_config_model import BaseConfigModel

class AppConfig(BaseConfigModel):
    ConfigFileName = "app_config"
    
    Title: str
    AuthExtension: str