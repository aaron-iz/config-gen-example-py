from config.config_container import config
import requests
import jwt

def load_using_s2s():
    s2s_secret_file = config.SecurityConfig.CertificateFileName
    s2s_secret = None
    with open(s2s_secret_file, "r") as f:
        s2s_secret = f.read()
        
    if s2s_secret is None:
        raise Exception("Could not retrieve dev-certificate")
        
    s2s_jwt = jwt.encode(s2s_secret, s2s_secret, algorithm="HS256")
    keyvault_endpoint = config.SecurityConfig.JwtSecretKeyVault
    response = requests.get(keyvault_endpoint, headers={"Authorization": f"Bearer {s2s_jwt}"})
    response_data = response.json()
    
    return response_data['secret'] # idk if that's the path to the secret in the json