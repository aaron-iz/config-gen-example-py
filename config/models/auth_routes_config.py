from config.base_config_model import BaseConfigModel

class AuthRoutesConfig(BaseConfigModel):
    ConfigFileName = "auth_routes_config"
    
    HealthEndpoint: str
    RegisterEndpoint: str
    LoginEndpoint: str
    VerifyEndpoint: str