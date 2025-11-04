from typing import ClassVar
from config.base_config_model import BaseConfigModel

# How it works:
# Secret is not saved in config - bc its a bad idea
# Secret is retrieved from some keyvault and saved in the instance!
# You can only retrieve if you have a certificate on your machine
# Not implemented yet but here to explain how it works

class SecurityConfig(BaseConfigModel):
    ConfigFileName: ClassVar[str] = "security_config"
    
    # must have a dev-certificate on your machine to be able to retrieve the secret locally.
    JwtSecretKeyVault: str # env-specific
    CertificateFileName: str