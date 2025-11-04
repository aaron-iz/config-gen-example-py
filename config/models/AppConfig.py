from config.BaseConfigModel import BaseConfigModel

class AppConfig(BaseConfigModel):
    ConfigFileName = "app_config"
    
    Title: str
    AuthExtension: str